# Docker for a uv Project: Ubuntu Base Image, Volume Mounts, `/opt/venv` and Docker Compose

Date: 2026-11-24

Instructor: Daniel Chen

## Summary

The session opened with a short review exercise: create a GitHub repository whose `Dockerfile` uses the `rocker/r-ver:4.6.2` image from last class. The instructor did this live with a coding agent (Claude Code), then rebuilt and ran the image by hand. That reviewed the build context `.`, the `--rm` and `-it` flags, what a default `CMD` does, and how to override it with `bash`. He also pointed out that the course website now includes the other instructor's slide decks, summary notes, Bloom's-taxonomy question sets for each lecture, and a command-history page.

The main work was turning the image into a Python compute environment for a `uv` project, which is what the group projects use. The class:

- swapped the R base image for `ubuntu:24.04`;
- copied `uv` in from Astral's image and set `WORKDIR /workspace`;
- copied in the three files that define the environment (`pyproject.toml`, `uv.lock` and `.python-version`);
- ran `uv sync --locked` during the build.

Along the way the instructor explained why an analysis project should pin exact versions (`==`, plus `add-bounds = "exact"`), why the Python version is pinned in `.python-version`, and how the order of `Dockerfile` steps affects layer caching.

He then separated compute from code. Copying code into the image, or cloning it inside the container with Git, does not scale for work in progress. Instead the project folder is mounted at run time with `-v "$(pwd):/workspace"`, which turns it into a live shared folder between your computer and the container. Mounting exposed a cross-platform problem: inside the container, `uv` found the host's `.venv` (built for macOS) and replaced it. The fix is to install the image's environment at `/opt/venv` with `ENV UV_PROJECT_ENVIRONMENT=/opt/venv`.

Finally, the long `docker run` command was moved into a `docker-compose.yml` file. The live `docker compose up` demo did not keep the container running, and the instructor will fix it next class (Thursday, 2026-11-26). He closed with real self-hosted apps that ship Compose files. This week's milestone task is a `Dockerfile` that reproduces the compute environment for your group's analysis.

## Knowledge Points

### 1. Warm-up: building with a coding agent, and why the jargon matters

- **The exercise**: create a new repository with a `Dockerfile` that uses the given image. The solution is essentially one line: `FROM rocker/r-ver:4.6.2`.
- **Claude Code demo**: the instructor asked Claude Code to create the repository `2026-11-24-docker`.
  - What the agent ran: `ls`, checks that `docker` and `gh` exist, a Docker command to detect the machine type, and `mkdir`.
  - What it produced: it wrote the `Dockerfile`, then built and tested the image. It also committed the files with a co-author line.
  - Extra files: it added `README.md` and a `Makefile`, because the instructor's setup asks for those by default. Templates and defaults are a strength of coding agents.
  - Cost: about 50 cents.
  - Wrong folder: it created the repository in `~/temp` instead of `~/git`, probably because Claude was started in a different folder.
- **Why learning the vocabulary matters**: the prompt worked because it used the right terms ("Docker file", the exact image name). Someone who has never heard of Docker cannot steer an agent to the correct answer.
- **The `CMD ["R"]` line the agent added**: this sets the default command, so running the container without other inputs starts R. Think of it as "what opens when you double-click this file". You can always pass a different command instead. ([29.2.1 `CMD` or `ENTRYPOINT`?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#cmd-or-entrypoint))

  ```dockerfile
  FROM rocker/r-ver:4.6.2

  CMD ["R"]
  ```

- **Docker Desktop must be running.** On macOS and Windows, Docker commands fail if Docker Desktop is not open. Recent versions tell you so.

### 2. Building and running an image (review)

- **`docker build --tag <name> .`** builds an image from the `Dockerfile` and gives it a name. The tag can be anything ("you can call it pizza"). Without a version it gets the tag `latest`.
- **The `.` at the end is not punctuation.** It means "here", the current directory: the dot from week 1 of DSCI 521.
  - `docker build` looks for a file named `Dockerfile` (capital D) by default, but it still needs to be told *where* to look.
  - Treat it like a function argument that cannot be left empty.
- **Base images are downloaded once.** If the base image is already on your machine, the `FROM` step is instant (`CACHED`). With a new version you have not pulled, that step takes seconds to minutes depending on your internet.
- **`docker run --rm -it <image>`**:
  - `--rm` deletes the container when you exit, so it is not left running on your computer.
  - `-it` gives you interactive terminal access: your keystrokes are passed to the container.
- **Overriding the default command**: `docker run --rm -it <image> bash` replaces `CMD ["R"]` with Bash. You then have an ordinary Linux terminal, like Git Bash or the macOS terminal.
- **You start at the root of the filesystem** (`/`), and you see system folders such as `bin`, `etc` and `usr`.
  - `/home` is empty: no user is set up.
  - For a course analysis container this is fine, because everyone shares the same setup and it is not served to the public.
- **Containers are disposable.** Any change made inside a `--rm` container is gone after you exit. That makes containers a safe place to try risky installs (for example PyTorch): if it goes wrong, just restart. "Like another version of Git that automatically resets all your changes."
- References: [28 Using and running containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html), [28.2 Docker command-line commands](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#docker-command-line-commands).

### 3. Choosing a base image for a Python project

- **Containers run Linux.** Even on a Windows or Mac laptop, inside a container you are in Linux, most likely some version of Ubuntu.
- **`FROM ubuntu:24.04`**: no one in the class has an R project, so the R image was swapped for plain Ubuntu.
  - The R image carries a lot of R software you do not need.
  - Ubuntu has no Python, and `uv` installs it.
- **Keep images small.** Be respectful of other people's disk space, which is expensive now because of the AI boom.
  - Alpine is even smaller than Ubuntu, but you may have to install more yourself.
  - Ubuntu is a good starting point.
- **Mixed-language projects are valid.** One project using both Python and R (for example `ggplot2` for plots) is common. The textbook's example image, [docker-uv-renv](https://github.com/chendaniely/docker-uv-renv), has both. The class demo used Python only.
- References: [29.3 Choosing a base image for your Dockerfile](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#choosing-a-base-image-for-your-dockerfile), [32 Python and R in one image](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv-renv.html).

### 4. Installing `uv` and setting a working directory

- **`COPY`** copies files into the image. It can also copy from *another image*:

  ```dockerfile
  COPY --from=ghcr.io/astral-sh/uv:0.13.7 /uv /uvx /usr/local/bin/
  ```

  - Read the image name like a GitHub address: registry, then owner, then repository, then version tag.
  - This takes the `uv` and `uvx` programs out of Astral's image and puts them in `/usr/local/bin/`.
  - The line comes straight from [uv's Docker guide](https://docs.astral.sh/uv/guides/integration/docker/#installing-uv).
- **Why install `uv` at all?** You are building a machine from scratch, so it is a virtual copy of your setup. Everyone installed `uv` in orientation, and the image needs it too.
- **`WORKDIR /workspace`** sets the working directory for the rest of the build and for containers started from the image. It creates the folder if it does not exist.
  - You land in a project folder instead of `/`, where you could accidentally move or break system files.
  - The working-directory idea (`pwd`, `cd`, relative paths) never goes away: every command needs a starting point.

### 5. The three files that define a Python environment

- **`uv init --bare`** creates a minimal `pyproject.toml` with a name, a version and `requires-python`. Version numbers do not matter much for a milestone project.
- **`pyproject.toml`** is the human-readable list of the packages you care about. It is a general Python metadata file that other tools can read too.
- **`uv.lock`** records exact versions of every package and dependency. It is generated from `pyproject.toml`.
- **`.python-version`** says which Python version to install (here `3.14`). This was new in this lecture.
  - The Python version affects which package versions resolve, because not every package supports the newest Python.
  - PyTorch is almost never compatible with the latest Python, so you often have to pin an older one.
  - Package authors (more in DSCI 524) can point it at an upcoming release candidate to test that their package still works when Python updates.
- Summary: one file for the Python version, one for the exact package versions, and one human-readable file that controls it all. All three get copied into the image.
- Reference: [30 Python packages with uv in an image](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv.html).

### 6. Pinning exact versions (`==` vs `>=`)

- **By default `uv add cowsay` writes `cowsay>=6.1`**, meaning "6.1 or anything newer".
  - If cowsay releases 7.0 next week and you rebuild then, you can end up with 7.0.
  - Per the textbook, this happens whenever `uv.lock` gets regenerated.
- **Major version changes usually break backward compatibility.** Code relying on 6.x behaviour may stop working in 7.x (more in DSCI 524). For a long-running project, `>=` is a real risk.
- **Pin exactly in `pyproject.toml`**: change the dependency to `"cowsay==6.1"`.
- **Make `uv add` pin exactly from now on** by adding a `[tool.uv]` table. This section controls how `uv` itself behaves:

  ```toml
  [project]
  name = "2026-11-24-docker"
  version = "0.1.0"
  requires-python = ">=3.14"
  dependencies = [
      "cowsay==6.1",
  ]

  [tool.uv]
  # `uv add` writes an exact version (==)
  add-bounds = "exact"
  ```

- **Downstream dependencies can still move.**
  - `uv.lock` pins everything, but anything you did not name in `pyproject.toml` can change when the lock is regenerated.
  - The instructor has had pandas break because a dependency far downstream updated, even though pandas itself was pinned. The fix was to pin that dependency too.
  - Rule of thumb: pin explicitly the packages that matter, and let the resolver choose compatible versions for the rest.
- Reference: [22 uv: pinning exact versions](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/virtual-environments-python-uv-exact-pins.html).

### 7. Installing the packages at build time: `uv sync --locked`

- **`RUN uv sync --locked`** does in the image exactly what you do on your laptop when you get a new project or a homework repository.
- **`--locked`** makes `uv` fail if `pyproject.toml` and `uv.lock` are out of sync. You *want* that error: it is a deliberate tripwire, so the image is built exactly the way you expect.
- The build visibly pauses on this step, because it is downloading Python and installing packages.
- After building, `ls -a` in `/workspace` shows the copied files plus a `.venv`. `ls` alone hides the dot-files.

### 8. Layer caching and the order of `Dockerfile` steps

- **Each instruction is cached as a layer.** If a layer and everything above it are unchanged, Docker reuses the cached version.
- **Changing a layer reruns every step below it**, and deleting a line counts as a change.
- **Put slow, rarely-changing steps at the top** (installing software and packages) and **frequently-changing steps at the bottom** (copying your code).
  - Installing the tidyverse can take about 15 minutes. You should not wait that long because you fixed a typo in a script.
- In class, adding `COPY hello.py ./` at the end made the rebuild take under a second: every earlier step said `CACHED` and only the copy ran.
- **Fewer, combined `RUN` lines save disk space.** Many published `Dockerfile`s cram everything into a few steps. This does not change the outcome, and when you are starting out there is nothing wrong with more lines if it keeps things clear.
- Reference: [29.1.3 Layer caching](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#layer-caching), [29.1.4 Guidelines for `RUN` commands](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#guidelines-for-run-commands).

### 9. Separating compute from code: mounting a volume

- **Why not copy the code in?** You could `COPY` everything and rebuild, but then the code is frozen in the image.
  - You have to remember to rebuild after every commit.
  - You have to worry about *who* copied *which* version.
  - It does not scale while you are actively doing EDA for a milestone.
- **Why not `git clone` inside the container?** It is valid; the instructor has done it to mimic a student's terminal. But the container then needs its own SSH key or personal access token. If it makes a new key on every build, you are re-registering keys constantly. Avoid it.
- **Goal**: the image holds only the software and packages (compute). The source code stays on your computer.
- **`-v` / `--volume` mounts a folder** at run time:

  ```bash
  docker run --rm -it -v "$(pwd):/workspace" 2026-11-24-docker bash
  ```

  - `$(pwd)` runs `pwd` and substitutes your current directory. This is ordinary Bash, and it means teammates do not hard-code their own paths.
  - The folder is mounted at `/workspace`, matching `WORKDIR`.
  - On Windows (Git Bash) you may need an extra leading slash (`"/$(pwd):/workspace"`). The textbook has the per-OS versions.
- **It is a live shared folder, not a copy or a sync.**
  - Edits on your laptop appear immediately in the container, and the other way round. You are working on the same file.
  - Positron sometimes does not notice that a file changed on disk, so you may need to refresh.
- **Mounting happens at `docker run`, not `docker build`.** A build can only copy files.
- **Why this is useful**: you can run the same code locally and in the container (for example `uv run quarto render ...`). That checks it works on your machine *and* in the reproducible environment.
- Reference: [28.1.2 Mounting volumes to containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#mounting-volumes-to-containers).

### 10. Cross-platform environments: `UV_PROJECT_ENVIRONMENT=/opt/venv`

- **`.venv` holds the actual Python binary and the installed packages.** Inside the container, plain `python` does not exist; you go through `uv`, which knows to look in that folder.
- **Teammates have different machines.**
  - Operating systems: Windows, macOS, Linux.
  - CPU architectures: `amd64` and `arm64`.
  - That makes four to six different combinations to support.
- **`uv sync` installs only for the current system.** `uv.lock` contains hashes for all platforms, but only your platform's packages get installed. The image is Linux, so `uv sync` in the build installs Linux packages.
- **Mounting the project overlays the image's `/workspace`, including its `.venv`.** The container then sees your laptop's `.venv` (built for macOS) instead.
  - That is like taking a program installed on a Mac and hoping it runs on Windows.
  - Problems are most likely with packages that "run fast": compiled code or C extensions such as pandas, rather than cowsay.
  - **Warning:** in class, `uv run` in the container *removed the host's `.venv` and created a Linux one in its place*. Because of the mount, that happened in the real project folder on the laptop (see *What went wrong live*).
- **The fix is an environment variable set before `uv sync`.** The exact position does not matter as long as it comes before `uv sync`.

  ```dockerfile
  ENV UV_PROJECT_ENVIRONMENT=/opt/venv
  ```

  - `uv` then puts the environment in `/opt/venv`, outside the mounted folder.
  - From then on it ignores the project's `.venv` and uses the Linux environment built into the image.
- **Rebuild after the change.** `uv run which python` in the container then prints `/opt/venv/bin/python`. Your laptop keeps its own `.venv`, and the container keeps its Linux one, so the image works on any host OS.
- **The finished `Dockerfile` from class** ([demo repo](https://github.com/chendaniely/2026-11-24-docker/blob/main/Dockerfile)):

  ```dockerfile
  FROM ubuntu:24.04

  # how to install uv
  COPY --from=ghcr.io/astral-sh/uv:0.13.7 /uv /uvx /usr/local/bin/

  WORKDIR /workspace

  ENV UV_PROJECT_ENVIRONMENT=/opt/venv
  COPY pyproject.toml uv.lock .python-version ./
  RUN uv sync --locked
  ```

- Reference: [30.5 Why the packages go in `/opt/venv`](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv.html#why-the-packages-go-in-optvenv).

### 11. Docker Compose

- **The problem**: `docker run` keeps growing (`--rm`, `-it`, `-v`, and `-p` port forwarding for JupyterLab or RStudio). Editing a long pasted command means arrow-keying through it.
- **`docker-compose.yml`** is a YAML file that records how to build and run the container. Being a file, it can be version-controlled and its changes tracked.
- **Structure**:
  - It starts with `services:`, listing one or more containers.
  - Each service has a name (`analysis-env` here; "you can call this pizza").
  - `build: .` builds from the `Dockerfile` in this folder, and `image:` names the result.
  - Optional `ports:` uses the form `"<host-port>:<container-port>"`, for example `<host-port>:8787` for RStudio.
  - `volumes:` is the equivalent of `-v`, and you can mount several folders.
  - The instructor showed `ports:` and an extra volume, then deleted them for this demo. More on Thursday.

  ```yaml
  services:
    analysis-env:
      build: .
      image: 2026-11-24-docker
      volumes:
        - .:/workspace
  ```

- **Multiple containers (microservices)**: for example a dashboard container plus a separate database container, kept apart because some people only care about one. For one analysis container Compose is a bit of overkill, but still useful.
- **Commands**:
  - `docker compose build` builds whatever the file describes.
  - `docker compose up` starts the service.
  - `docker compose up --detach` (`-d`) runs it in the background and gives you the prompt back.
- **Outside MDS**: many self-hosted open-source apps ship a Compose file, so `docker compose up -d` downloads the image, starts the app, and you open it on a port in your browser.
  - Examples: Actual Budget and Firefly III (personal finance), Jellyfin (media server), n8n (AI automation), and a recipe manager.
  - The Actual Budget file shows the same parts plus environment variables and a health check.
  - You can run these on an old laptop "in your closet" or on a cloud machine.
- **Coming this week**: publishing an image to a registry, so others can `docker pull` it instead of building from the `Dockerfile`.
- Reference: [33 Containers: Docker Compose](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-docker-compose.html), demo [`docker-compose.yml`](https://github.com/chendaniely/2026-11-24-docker/blob/main/docker-compose.yml).

### 12. Extra software in your image (optional)

- A bare Ubuntu image has no text editor: `nano` and `vi` are both missing. You may add `RUN` lines to install one, or other tools.
- Some Python packages need system libraries. Geospatial analysis is the classic case, needing libraries installed from Ubuntu. What you need depends on your stack, so know *why* each install is there.

## Commands from class

### Inspect the agent-made repository and rebuild the R image

```bash
cd ~/temp/2026-11-24-docker
ls -alh                                   # Dockerfile, Makefile, README.md, plus .git
positron .                                # open the folder in Positron
docker images                             # 2026-11-24-docker:latest already built by Claude
docker build --tag 2026-11-24-docker .    # "." = look for the Dockerfile here
docker run --rm -it 2026-11-24-docker     # CMD ["R"] -> R starts; quit with q()
docker run --rm -it 2026-11-24-docker bash   # override CMD with a shell
pwd                                       # (in container) -> /
ls                                        # system folders, incl. rocker_scripts
cd home/
ls -alh                                   # empty: no user in this image
exit
```

### Set up the `uv` project on the laptop

```bash
uv init --bare        # minimal pyproject.toml
uv add cowsay         # installs cowsay==6.1, creates .venv
uv sync
uv run hello.py       # hello.py: import cowsay; cowsay.cow("hello, moo.")
```

Between these commands the instructor edited `pyproject.toml` by hand, changing to `cowsay==6.1` and adding `[tool.uv] add-bounds = "exact"`, and created `hello.py` and `.python-version`.

### Build the Ubuntu + `uv` image and look inside

```bash
docker build --tag 2026-11-24-docker .
docker run --rm -it 2026-11-24-docker bash
pwd                   # (in container) -> /workspace, thanks to WORKDIR
ls                    # pyproject.toml  uv.lock
ls -a                 # also .python-version and .venv
exit
```

The build steps show what each `Dockerfile` line became, and that `uv sync` is the slow step:

```
 => CACHED [stage-0 2/5] COPY --from=ghcr.io/astral-sh/uv:0.13.7 /uv /uvx   0.0s
 => CACHED [stage-0 3/5] WORKDIR /workspace                                 0.0s
 => [stage-0 4/5] COPY pyproject.toml uv.lock .python-version ./            0.0s
 => [stage-0 5/5] RUN uv sync --locked                                      2.3s
```

### Copy the code in at the end (caching demo)

```bash
# Dockerfile: add `COPY hello.py ./` as the last line
docker build --tag 2026-11-24-docker .
docker run --rm -it 2026-11-24-docker bash
uv run hello.py       # (in container) the cow says hello
exit
```

Only the new last step ran; everything above it was reused:

```
 => CACHED [stage-0 5/6] RUN uv sync --locked                               0.0s
 => [stage-0 6/6] COPY hello.py ./                                          0.0s
```

### Remove the code from the image and mount the folder instead

```bash
# Dockerfile: delete `COPY hello.py ./`, then rebuild
docker build --tag 2026-11-24-docker .
docker run --rm -it -v "$(pwd):/workspace" 2026-11-24-docker bash
ls                    # (in container) whole project, incl. my_secrets.txt
cat my_secrets.txt    # i'm afraid of the dark.
cat my_secrets.txt    # after editing on the laptop: a second line appears live
uv run hello.py       # works, but see "What went wrong live"
ls -alh
exit
```

### Move the environment to `/opt/venv`

```bash
# Dockerfile: add `ENV UV_PROJECT_ENVIRONMENT=/opt/venv` before `RUN uv sync --locked`
docker build --tag 2026-11-24-docker .        # uv sync step reruns
docker run --rm -it -v "$(pwd):/workspace" 2026-11-24-docker bash
which uv              # (in container) /usr/local/bin/uv
uv tree               # 2026-11-24-docker v0.1.0 └── cowsay v6.1
uv run which python   # /opt/venv/bin/python, not the mounted .venv
exit
```

### Docker Compose

```bash
docker compose build              # reads docker-compose.yml; every layer cached
docker compose up                 # container created, then exits immediately
docker compose ps                 # nothing running
```

### What went wrong live

- **The agent put the repository in the wrong place.** Claude Code created it under `~/temp` rather than `~/git`, likely because it was started from a different folder. The demo carried on in `~/temp/2026-11-24-docker`.
- **No text editor in the container.** The instructor tried to edit the mounted file inside the container:

  ```
  bash: nano: command not found
  bash: vi: command not found
  ```

  He edited on the laptop instead and used `cat` in the container to show the change. If you want an editor inside, install one with a `RUN` line.
- **Mounting overwrote the laptop's `.venv`.** This happened before the `ENV` line existed. `uv run hello.py` inside the container found the host's macOS `.venv`, deleted it, and made a Linux one in the shared folder:

  ```
  warning: Ignoring existing virtual environment linked to non-existent Python interpreter: `.venv/bin/python` -> `/Users/dan/.local/share/uv/python/cpython-3.14-macos-aarch64-none/bin/python3.14`
  Using CPython 3.14.10
  Removed virtual environment at: .venv
  Creating virtual environment at: .venv
  ```

  **This changes your real project folder, not a copy.** The fix was `ENV UV_PROJECT_ENVIRONMENT=/opt/venv` and a rebuild, after which `uv run which python` pointed at `/opt/venv/bin/python`. The same run also printed `warning: Failed to hardlink files; falling back to full copy`, which comes from installing across the mounted filesystem.
- **Two small typos.**
  - `ls 0alh` failed (`No such file or directory`); it should be `ls -alh`.
  - `python` returned `command not found`, because Python exists only through `uv` (`uv run ...`).
- **`uv which python` is not a command.** It failed with `error: unrecognized subcommand 'which'`; the fix was `uv run which python`.
- **`docker compose up` did not keep the container running.** It printed `analysis-env-1 exited with code 0` straight away.
  - `docker compose up --detatch` was a misspelling (`unknown flag: --detatch`); the flag is `--detach` (`-d`).
  - `docker compose ps` showed nothing, and `docker compose exec analysis-env bash` replied `service "analysis-env" is not running`.
  - The instructor ran out of time and will fix this demo next class (Thursday, 2026-11-26). Conceptually, Compose is meant to replace the long `docker run` command with flags read from the file.

## Assignments

- [ ] **This week's project milestone:** write the `Dockerfile` that reproduces the compute environment for your group's analysis. See the milestone page in the [student repository](https://github.com/UBC-MDS/DSCI_522_dsci-workflows_students); no due date was given in class.
  - Base it on the class example (Ubuntu, `uv`, copy `pyproject.toml`, `uv.lock` and `.python-version`, then `uv sync --locked`, with `UV_PROJECT_ENVIRONMENT=/opt/venv`).
  - You must be able to start the container, mount the folders that need mounting, and run `uv run quarto render` on your report inside it.
  - Grading: TAs build an image from your repository and try to run your analysis in a container from it.
  - Optional: add `RUN` lines for extra tools you need, such as a text editor or system libraries. Know why each one is there.
- [ ] Optional: browse the new material on the course website (slide decks, summary notes, Bloom's-taxonomy Q&A, command history).

---

- prompt: prompt-notes-original.md @ 979670b
- prompt-hash: f78026c179ce
- model: claude-opus-5-5 (requested: opus)
- backend: claude
- inputs: transcript-plaud.md, terminal.txt, materials.md
- generated: 2026-11-24
