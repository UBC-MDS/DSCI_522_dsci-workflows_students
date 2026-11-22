"""Generate slide images with the OpenAI image API.

Two functions:

    generate_image(prompt, filename)   one image
    generate_from_csv(csv_path)        every row of a CSV with filename/prompt columns

By default both attach the lecture 1 otter images as style references, so the new
image keeps the same character and watercolour style. Pass `refs=None` to skip that
and do a plain text-to-image generation.

From the shell:

    uv run python scripts/generate_images.py "an otter holding a clock" otter_clock.png
    uv run python scripts/generate_images.py --csv website/slides/lec02_image_prompts.csv
    uv run python scripts/generate_images.py --csv website/slides/lec02_image_prompts.csv --index 3
    uv run python scripts/generate_images.py --csv website/slides/lec02_image_prompts.csv --index 1,4-6
"""

import base64
import csv
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

REPO_ROOT = Path(__file__).resolve().parents[1]
IMAGES_DIR = REPO_ROOT / "website" / "slides" / "images"

# Shown to the model so the otter and the style stay the same across lectures.
STYLE_REFS = [IMAGES_DIR / "hello_background.png", IMAGES_DIR / "watch.png"]

# The written form of "same style as this one, same character".
STYLE_LOCK = (
    "Generate an image in the EXACT SAME watercolor style as the attached reference "
    "image(s), using the EXACT SAME otter character. Pay attention to the details of the image you generated. Generate extremely high quality image please. Generate the new image with the new scene:\n\n"
)

load_dotenv(REPO_ROOT / ".env")


def generate_image(
    prompt, filename, refs=STYLE_REFS, size="1536x1024", quality="high", transparent=True
):
    """Generate one image and save it to website/slides/images/<filename>."""
    background = "transparent" if transparent else "opaque"
    client = OpenAI()

    if refs:
        files = [Path(ref).open("rb") for ref in refs]
        try:
            result = client.images.edit(
                model="gpt-image-2.5-sunburst",
                image=files,
                prompt=STYLE_LOCK + prompt,
                size=size,
                quality=quality,
                background=background,
                output_format="png",
            )
        finally:
            for file in files:
                file.close()
    else:
        result = client.images.generate(
            model="gpt-image-2.5-sunburst",
            prompt=prompt,
            size=size,
            quality=quality,
            background=background,
            output_format="png",
        )

    out = IMAGES_DIR / filename
    out.write_bytes(base64.b64decode(result.data[0].b64_json))
    return out


def parse_indices(spec):
    """Parse a row-selection string like "3" or "1,4-6" into [1, 4, 5, 6].

    Indices are 1-based and count data rows only (the header doesn't count),
    matching the row numbers you'd point to when reading the CSV.
    """
    indices = []
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            start, end = part.split("-")
            indices.extend(range(int(start), int(end) + 1))
        else:
            indices.append(int(part))
    return indices


def generate_from_csv(csv_path, refs=STYLE_REFS, overwrite=False, transparent=True, indices=None):
    """Generate an image per row of a CSV with `filename` and `prompt` columns.

    Pass `indices` (1-based, from `parse_indices`) to only generate those rows
    instead of the whole file.
    """
    with open(csv_path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    if indices is not None:
        bad = [i for i in indices if i < 1 or i > len(rows)]
        if bad:
            raise ValueError(f"row index out of range (CSV has {len(rows)} rows): {bad}")
        rows = [rows[i - 1] for i in indices]

    made = []
    for row in rows:
        filename, prompt = row["filename"], row["prompt"]
        if (IMAGES_DIR / filename).exists() and not overwrite:
            print(f"· {filename} exists, skipping")
            continue
        print(f"→ {filename}")
        made.append(generate_image(prompt, filename, refs=refs, transparent=transparent))
    return made


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("prompt", nargs="?", help="prompt for a single image")
    parser.add_argument("filename", nargs="?", help="output filename, e.g. otter.png")
    parser.add_argument("--csv", help="generate every row of this CSV instead")
    parser.add_argument(
        "--index",
        help="with --csv, only these row numbers (1-based, header excluded), e.g. '3' or '1,4-6'",
    )
    parser.add_argument("--no-refs", action="store_true", help="skip the style references")
    parser.add_argument("--overwrite", action="store_true", help="redo images that exist")
    parser.add_argument("--opaque", action="store_true", help="white background instead of transparent")
    args = parser.parse_args()

    refs = None if args.no_refs else STYLE_REFS
    if args.csv:
        indices = parse_indices(args.index) if args.index else None
        generate_from_csv(
            args.csv, refs=refs, overwrite=args.overwrite, transparent=not args.opaque, indices=indices
        )
    elif args.prompt and args.filename:
        print(generate_image(args.prompt, args.filename, refs=refs, transparent=not args.opaque))
    else:
        parser.error("give a prompt and a filename, or --csv")
