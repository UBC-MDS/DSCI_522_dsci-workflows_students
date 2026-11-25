# Course materials: 2026-11-25 lecture (section 01)

## Links

- Demo repository: <https://github.com/chendaniely/2026-11-25-docker-validate>
  - [`Dockerfile`](https://github.com/chendaniely/2026-11-25-docker-validate/blob/main/Dockerfile)
  - [`docker-compose.yml`](https://github.com/chendaniely/2026-11-25-docker-validate/blob/main/docker-compose.yml)
  - [`pyproject.toml`](https://github.com/chendaniely/2026-11-25-docker-validate/blob/main/pyproject.toml), [`uv.lock`](https://github.com/chendaniely/2026-11-25-docker-validate/blob/main/uv.lock) and [`.python-version`](https://github.com/chendaniely/2026-11-25-docker-validate/blob/main/.python-version)
  - [`validation.py`](https://github.com/chendaniely/2026-11-25-docker-validate/blob/main/validation.py)
  - [Commits](https://github.com/chendaniely/2026-11-25-docker-validate/commits/main)
- The reference repository the class copied its `Dockerfile`, `pyproject.toml` and `docker-compose.yml` from, the textbook's example project with Python and R in one image: <https://github.com/chendaniely/docker-uv-renv>
- pointblank for Python: <https://posit-dev.github.io/pointblank/>
- Textbook, *Reproducible and Trustworthy Workflows for Data Science*:
  <https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/>
  - [29 Customizing and building containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html)
    - [29.1 Building container images from `Dockerfile`'s](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#building-container-images-from-dockerfiles)
    - [29.2 `Dockerfile` command summary](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#dockerfile-command-summary)
    - [29.3 Choosing a base image for your Dockerfile](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#choosing-a-base-image-for-your-dockerfile)
    - [29.4 Dockerfile FAQ](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#dockerfile-faq)
  - [33 Containers: Docker Compose](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-docker-compose.html)
  - [41 Data validation: Python (pointblank)](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/data-validation-python-pointblank.html)
- Not reached in class (next class; their text is in `materials-next-class.md`):
  - [29.1.2 Build your first image](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#build-your-first-image)
  - [29.1.3 Layer caching](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#layer-caching)
  - [29.1.4 Guidelines for `RUN` commands](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#guidelines-for-run-commands)
  - [29.2.1 `CMD` or `ENTRYPOINT`?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#cmd-or-entrypoint)
  - [41.5 Flagging every row](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/data-validation-python-pointblank.html#flagging-every-row)

## About these materials

What this lecture worked from: the class's demo repository, and textbook chapters from
*Reproducible and Trustworthy Workflows for Data Science*
(<https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/>),
as published on 2026-11-25. Each textbook heading links to its published section.

The instructor taught this section 01 lecture in place of its usual instructor, and named
three chapters for it: 29 (building images), 33 (Docker Compose) and 41 (data validation
with pointblank). The class reviewed building an image from the reference repository's
`Dockerfile`, then covered Docker Compose and pointblank. The sections of chapters 29 and
41 it didn't reach are listed above under "Not reached in class", titles and links only.

## Demo repository

The repository the class worked in: <https://github.com/chendaniely/2026-11-25-docker-validate>. As GitHub shows it on 2026-11-25, it has two
commits, "Initial commit" (a `README.md`) and "files from class", and no issues or pull
requests.

The `Dockerfile`, copied from the reference repository, with its Quarto and R parts
deleted in class:

```dockerfile
FROM rocker/r-ver:4.6.2

RUN apt-get update && apt-get install --yes \
    curl \
    git \
    less \
    libuv1-dev \
    make \
    nano \
    openssh-server

COPY --from=ghcr.io/astral-sh/uv:0.13.7 /uv /uvx /usr/local/bin/

WORKDIR /workspace

# python packages in /opt/venv
ENV UV_PROJECT_ENVIRONMENT=/opt/venv
# ssh logins don't see ENV, only /etc/environment
RUN echo "UV_PROJECT_ENVIRONMENT=$UV_PROJECT_ENVIRONMENT" >> /etc/environment
COPY pyproject.toml uv.lock .python-version ./
# --locked: stop if uv.lock doesn't match pyproject.toml
RUN uv sync --locked

# For linux laptops:
# StrictModes no: sshd wants root to own the key file,
# but on Linux the mounted one is yours
# RUN echo "StrictModes no" > /etc/ssh/sshd_config.d/container.conf

# -D: stay in the foreground, so the container keeps running
CMD ["/usr/sbin/sshd", "-D"]
```

The `docker-compose.yml`, copied from the reference repository:

```yaml
services:
  analysis-env:
    build: .
    image: docker-uv-renv
    ports:
      # 2222 on your computer, 22 in the container.
      # "127.0.0.1:2222:22" stops others on the same Wi-Fi from reaching it.
      - "2222:22"
    volumes:
      - .:/workspace
      # ro: read-only
      - ~/.ssh/id_ed25519.pub:/root/.ssh/authorized_keys:ro
```

The uv project: `pyproject.toml`, with the three packages the class added by hand for the
data validation demo (pandera, palmerpenguins and pointblank) after `uv add` failed,

```toml
[project]
name = "docker-uv-renv"
version = "2026.11.13"
requires-python = ">=3.14"
dependencies = [
    "altair==6.3.0",
    "pandas==3.1.1",
    # Altair charts as images, for PDFs
    "vl-convert-python==1.9.0.post1",
    # Quarto needs these to run Python code
    "ipykernel==7.4.0",
    "nbclient==0.11.0",
    "pyyaml==6.0.3",
    "pandera",
    "palmerpenguins",
    "pointblank"
]

[tool.uv]
# `uv add` writes an exact version (==)
add-bounds = "exact"
```

and `.python-version`:

```
3.14
```

`uv.lock` is in the repository. `hello.py` is empty: the class made it with `touch` inside
the container to show that a mounted folder is shared with the computer.

`validation.py`, the data validation demo:

```python
import pointblank as pb
from palmerpenguins import load_penguins

penguins = load_penguins()
penguins

pb.missing_vals_tbl(data=penguins)

values = (
    pb.Validate(
        data=penguins,
        label="Penguin measurements",
        thresholds=(0.01, 0.05, 0.10),  # warning, error, critical
    )
    .col_vals_in_set(columns="species", set=["Adelie", "Chinstrap"])
    .col_vals_between(columns="bill_length_mm", left=30, right=60, na_pass=True)
    .rows_distinct()
    .interrogate()
)

values

passed = values.get_sundered_data(type="pass")  # keep working with these
failed = values.get_sundered_data(type="fail")  # a teammate fixes these
pb.preview(data=failed)  # a quick look at the rows that failed
```

## [29  Customizing and building containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html)

### [Learning Objectives](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#learning-objectives)

1.  Write a container file (e.g., Dockerfile) that can be used to reproducibly build a container image that would contain the needed software and environment dependencies of your data science project
2.  Use manual and automated tools (e.g., Docker, GitHub Actions) to build and share container images
3.  List good container base images for data science projects

### [Download the images before you start](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#download-the-images-before-you-start)

The examples in this chapter build on `rocker/r-ver:4.6.2`, which takes more than a gigabyte of disk space. Start Docker first (on macOS and Windows, open Docker Desktop), then download (pull) it before you start:

*Terminal*

``` bash
docker pull rocker/r-ver:4.6.2
```

### [29.1 Building container images from `Dockerfile`’s](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#building-container-images-from-dockerfiles)

- A `Dockerfile` is a plain-text file that contains commands primarily about what software to install in the Docker image. This is the more trusted and transparent way to build Docker images.

- Once we have created a `Dockerfile`, we can build it into a Docker image.

- Docker images are built in layers, and as such, `Dockerfile`s always start by specifying a base Docker image that the new image is to be built on top of.

- Docker containers are all Linux containers and thus use Linux commands to install software. However, there are different flavors of Linux (e.g., Ubuntu, Debian, CentOS, Red Hat), and thus you need to use the right Linux install commands to match your flavor of container. For this course, we will focus on Ubuntu- or Debian-based images (and that means if we need to install software outside of R and Python packages, we will use `apt-get` as our installation program). However, most of what we’ll be doing for installation is R, Python, and their packages. For those, an image uses the same tools as your laptop, uv for Python and renv for R, which the next chapters put into an image.

**`apt` or `apt-get`?**

Ubuntu has two commands for its package manager. `apt` is designed for people typing at a terminal, and its behavior may change between versions. `apt-get` is the older command, which keeps working the same way, so Ubuntu’s [`apt` manual page](https://manpages.ubuntu.com/manpages/noble/man8/apt.8.html) recommends `apt-get` for scripts. The `RUN` lines in a `Dockerfile` are a script, so this book uses `apt-get` in them. `apt` even prints a warning when a script runs it:

*Output*

``` out
WARNING: apt does not have a stable CLI interface. Use with caution in scripts.
```

At a container’s prompt either command works, but using `apt-get` there too means you can copy the command that worked straight into the `Dockerfile`.

#### [29.1.1 Workflow for building a Dockerfile](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#workflow-for-building-a-dockerfile)

It can take a LOOOOOOOONNNG time to troubleshoot the building of Docker images. Thus, to speed things up and be more efficient, we suggest the workflow below:

1.  Choose a base image to build off (from <https://hub.docker.com/>).

2.  Create a `Dockerfile` named `Dockerfile` and save it in an appropriate project repository. Open that file and type `FROM <BASE_IMAGE>` on the first line. Add any files that need to be accessed at build time via the `COPY` command.

3.  In a terminal, type `docker run --rm -it <BASE_IMAGE> bash` and interactively try the install commands you think will work. Edit and try again until the install command works. The `bash` at the end starts a Bash shell in place of the image’s default command.

4.  Write working install commands in the `Dockerfile`, preceding them with `RUN`, and save the `Dockerfile`.

5.  After adding every 2–3 commands to your `Dockerfile`, try building the Docker image via `docker build --tag <TEMP_IMAGE_NAME> <PATH_TO_DOCKERFILE_DIRECTORY>`.

6.  Once the entire `Dockerfile` works from beginning to end on your laptop, then you can finally move to building remotely (e.g., creating a trusted build on GitHub Actions).

### [29.2 `Dockerfile` command summary](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#dockerfile-command-summary)

The most common `Dockerfile` commands I use:

| Command | Description |
|----|----|
| FROM | States which base image the new Docker image should be built on top of |
| RUN | Specifies that a command should be run in a shell |
| ENV | Sets environment variables |
| EXPOSE | Specifies the port the container should listen to at runtime |
| COPY or ADD | Adds files (or URLs in the case of ADD) to a container’s filesystem |
| CMD | Sets the default command a container runs when it starts; a command after the image name in `docker run` replaces it |
| ENTRYPOINT | Sets a command that always runs when a container starts; anything after the image name in `docker run` is passed to it as arguments |
| WORKDIR | Sets the working directory for any `RUN`, `CMD`, `ENTRYPOINT`, COPY and ADD instructions that follow it in the `Dockerfile` |

And more here in the [Dockerfile reference](https://docs.docker.com/reference/dockerfile/).

### [29.3 Choosing a base image for your Dockerfile](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#choosing-a-base-image-for-your-dockerfile)

![](https://themuslimtimesdotinfodotcom.files.wordpress.com/2018/10/newton-quotes-2.jpg?w=1334)

Source: <https://themuslimtimes.info/2018/10/25/if-i-have-seen-further-it-is-by-standing-on-the-shoulders-of-giants/>

#### [29.3.1 Good base images to work from for R or Python projects!](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#good-base-images-to-work-from-for-r-or-python-projects)

| Image | Software installed |
|----|----|
| [rocker/r-ver](https://hub.docker.com/r/rocker/r-ver) | Ubuntu Linux and R; the base of this book’s R examples |
| [rocker/rstudio](https://hub.docker.com/r/rocker/rstudio/) | R, RStudio |
| [rocker/tidyverse](https://hub.docker.com/r/rocker/tidyverse/) | R, R packages (including the tidyverse), RStudio, Make; ARM-based computers need tag `4.5.1` or later |
| [ubuntu](https://hub.docker.com/_/ubuntu) | Ubuntu Linux only; add uv to install Python and its packages |
| [python](https://hub.docker.com/_/python) | Debian Linux and Python; the `-slim` tags leave out software most projects do not need |
| [quay.io/jupyter/datascience-notebook](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html#jupyter-datascience-notebook) | JupyterLab, with libraries for data analysis from the Python, R and Julia communities |

**Use `rocker/tidyverse:4.5.1` or later**

`rocker/tidyverse` images before `4.5.1` were built only for Intel and AMD computers (`amd64`). From `4.5.1` on, they are also built for ARM computers (`arm64`), such as Macs with Apple silicon. On an ARM computer, pulling an older tag fails:

*Terminal*

``` bash
docker pull rocker/tidyverse:4.5.0
```

*Output*

``` out
Error response from daemon: no matching manifest for linux/arm64/v8 in the manifest list entries: no match for platform in manifest: not found
```

So use `4.5.1` as the minimum version. The [`rocker/tidyverse` tags page](https://hub.docker.com/r/rocker/tidyverse/tags) lists each tag with the platforms it was built for (`linux/amd64`, `linux/arm64`), so you can check a tag before you use it.

### [29.4 Dockerfile FAQ](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#dockerfile-faq)

These questions come up when you start writing your own `Dockerfile`.

#### [29.4.1 1. Where does the `Dockerfile` live?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#where-does-the-dockerfile-live)

The `Dockerfile` should live in the root directory of your project.

#### [29.4.2 2. How do I make an image from a `Dockerfile`?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#how-do-i-make-an-image-from-a-dockerfile)

There are 2 ways to do this! I use the first when developing my `Dockerfile` (to test quickly that it works), and then the second when I want a build that others can check, made from the `Dockerfile` in the repository.

1.  Build a Docker image locally on your laptop

2.  Build a Docker image on GitHub Actions (see [Building images for several platforms](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-platforms.html))

#### [29.4.3 3. How do I build an image locally on my laptop?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#how-do-i-build-an-image-locally-on-my-laptop)

From the directory that contains your `Dockerfile` (usually your project root):

*Terminal*

``` bash
docker build --tag IMAGE_NAME:VERSION .
```

**Note**

`--tag` lets you name and version the Docker image. You can call this anything you want. The version number/name comes after the colon.

After I build, I then try to `docker run ...` to test the image locally. If I don’t like it, or it doesn’t work, I delete the image with `docker rmi {IMAGE_NAME}`, edit my Dockerfile, and try to build and run it again.

## [33  Containers: Docker Compose](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-docker-compose.html)

### [Learning Objectives](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-docker-compose.html#learning-objectives)

1.  Read a `docker-compose.yml` file as the `docker build` and `docker run` commands it replaces
2.  Build, start, use and stop a container with `docker compose`

### [33.1 Docker Compose to launch containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-docker-compose.html#docker-compose-to-launch-containers)

It can be fiddly and error-prone to type long commands into the terminal, or a GUI every time you want to launch a container. Even if you are copying and pasting commands, it can be difficult to make changes to long commands because you cannot click to a location to make edits.

A better approach is to use Docker Compose to specify how you want to launch the container. This way, all the parts of your command are saved in a file. This helps document how to run the Docker image, and it can be version controlled as part of a project.

Docker Compose uses a YAML file, specifically named `docker-compose.yml`, to record how the container should be launched. This file can include details such as:

- the Docker image and version to use, or how to build it
- how to mount volumes
- what ports to map
- what environment variables to set

`docker run` commands are interchangeable with the parameters specified in `docker-compose.yml`; the compose file makes it easier to manage all the `docker run` parameters. See this resource that can convert a run command to a compose file: <https://www.composerize.com/>

Here is the `docker-compose.yml` file of [docker-uv-renv](https://github.com/chendaniely/docker-uv-renv), the project from [Python and R in one image](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv-renv.html):

``` yaml
services:
  analysis-env:
    build: .
    image: docker-uv-renv
    ports:
      # 2222 on your computer, 22 in the container.
      # "127.0.0.1:2222:22" stops others on the same Wi-Fi from reaching it.
      - "2222:22"
    volumes:
      - .:/workspace
      # ro: read-only
      - ~/.ssh/id_ed25519.pub:/root/.ssh/authorized_keys:ro
```

Without Docker Compose, building the image and starting the container takes these two commands, from the project folder:

*Terminal*

``` bash
docker build --tag docker-uv-renv .
docker run --detach -p 2222:22 -v "$(pwd):/workspace" -v ~/.ssh/id_ed25519.pub:/root/.ssh/authorized_keys:ro docker-uv-renv
```

Each part of the `docker run` command is a line of the file:

- `services:` lists the containers the project runs. This project has one, which it calls `analysis-env`.
- `build: .` builds the image from the `Dockerfile` in this folder, like `docker build .`.
- `image: docker-uv-renv` names the image, like `--tag docker-uv-renv`.
- `ports:` maps port 2222 on your computer to port 22 in the container, like `-p 2222:22`. Port 22 is where the container’s ssh server listens. The file uses 2222 on your computer, because your computer may already use 22.
- `volumes:` mounts two things, like the two `-v` options. `.:/workspace` mounts the project folder at `/workspace`. The second line mounts your ssh public key as the list of keys that may log in to the container as `root`, and `ro` makes it read-only inside the container. The key is the one from [SSH for authentication](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/ssh-authentication.html).

**No ssh key yet?**

To check that you have the key, list it:

*Terminal*

``` bash
ls ~/.ssh/id_ed25519.pub
```

If `ls` says `No such file or directory`, make a key as in [SSH for authentication](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/ssh-authentication.html):

*Terminal*

``` bash
ssh-keygen -t ed25519
```

Press Enter to save it in the default place, `~/.ssh/id_ed25519`. Make the key before you start the container. If the key is missing when the container starts, Docker makes a folder at `~/.ssh/id_ed25519.pub` instead, and you cannot log in to the container.

Docker Compose reads the paths in the file itself, so the same file works on macOS, Linux and Windows, without the Git Bash `/$(pwd)` change from the earlier chapters.

### [33.2 Docker Compose commands](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-docker-compose.html#docker-compose-commands)

Run these from the project folder. `docker compose build` builds the image. If you built it in [Python and R in one image](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv-renv.html), Docker reuses every layer:

*Terminal*

``` bash
docker compose build
```

*Output*

``` out
[+] Building 20.6s (21/21) FINISHED
 => [internal] load local bake definitions                                                     0.0s
 => => reading from stdin 853B                                                                 0.0s
 => [internal] load build definition from Dockerfile                                           0.0s
 => => transferring dockerfile: 1.77kB                                                         0.0s
 => [internal] load metadata for docker.io/rocker/r-ver:4.6.2                                  0.1s
 => [internal] load metadata for ghcr.io/astral-sh/uv:0.13.7                                   1.2s
 => [internal] load .dockerignore                                                              0.1s
 => => transferring context: 2B                                                                0.0s
 => [stage-0  1/12] FROM docker.io/rocker/r-ver:4.6.2@sha256:8739c76d2d9316698a7145b032601f1e  0.0s
 => => resolve docker.io/rocker/r-ver:4.6.2@sha256:8739c76d2d9316698a7145b032601f1e82249fdee3  0.0s
 => FROM ghcr.io/astral-sh/uv:0.13.7@sha256:96f40d3904aad8d0bd010539001d36c8e2188b981e1334471  0.0s
 => => resolve ghcr.io/astral-sh/uv:0.13.7@sha256:96f40d3904aad8d0bd010539001d36c8e2188b981e1  0.0s
 => [internal] load build context                                                              0.1s
 => => transferring context: 320.25kB                                                          0.1s
 => CACHED [stage-0  2/12] RUN apt-get update && apt-get install --yes     curl     git     l  0.0s
 => CACHED [stage-0  3/12] RUN curl --location --output quarto.deb     https://github.com/qua  0.0s
 => CACHED [stage-0  4/12] COPY --from=ghcr.io/astral-sh/uv:0.13.7 /uv /uvx /usr/local/bin/    0.0s
 => CACHED [stage-0  5/12] WORKDIR /workspace                                                  0.0s
 => CACHED [stage-0  6/12] RUN echo "UV_PROJECT_ENVIRONMENT=/opt/venv" >> /etc/environment     0.0s
 => CACHED [stage-0  7/12] COPY pyproject.toml uv.lock .python-version ./                      0.0s
 => CACHED [stage-0  8/12] RUN uv sync --locked                                                0.0s
 => CACHED [stage-0  9/12] RUN echo "RENV_PATHS_LIBRARY=/opt/renv/library" >> /usr/local/lib/  0.0s
 => CACHED [stage-0 10/12] COPY renv.lock .Rprofile ./                                         0.0s
 => CACHED [stage-0 11/12] COPY renv/activate.R renv/                                          0.0s
 => CACHED [stage-0 12/12] RUN Rscript -e "renv::restore()"                                    0.0s
 => exporting to image                                                                        18.3s
 => => exporting layers                                                                        0.0s
 => => exporting manifest sha256:4557e751a87e82b3a9de57cc050f041b1a9906f8ddcf6608497ae4553039  1.8s
 => => exporting config sha256:381ae72e85e27b2dfc6f930cc4e82457d2c5a26e254ea71651f8c1b917b494  0.0s
 => => exporting attestation manifest sha256:456fc1c36345b771766202511bb10ff31e2e2f804ec9aacc  0.0s
 => => exporting manifest list sha256:0f31cb20fb9602e3500fb9e402df9966ea2d3934625e97864f52758  0.0s
 => => naming to docker.io/library/docker-uv-renv:latest                                       0.0s
 => => unpacking to docker.io/library/docker-uv-renv:latest                                   16.4s
 => resolving provenance for metadata file                                                     0.0s
[+] build 1/1
 ✔ Image docker-uv-renv Built                                                                  20.8s
```

`docker compose up --detach` starts the container. `--detach` runs it in the background, so that you get your terminal back while the ssh server keeps running:

*Terminal*

``` bash
docker compose up --detach
```

*Output*

``` out
[+] up 2/2
 ✔ Network docker-uv-renv_default          Created                                              0.0s
 ✔ Container docker-uv-renv-analysis-env-1 Started                                              0.2s
```

Docker Compose made a network for the project’s containers, and named the container after the project folder and the service. `docker compose ps` lists the project’s running containers:

*Terminal*

``` bash
docker compose ps
```

*Output*

``` out
NAME                            IMAGE            COMMAND               SERVICE        CREATED        STATUS                  PORTS
docker-uv-renv-analysis-env-1   docker-uv-renv   "/usr/sbin/sshd -D"   analysis-env   1 second ago   Up Less than a second   0.0.0.0:2222->22/tcp, [::]:2222->22/tcp
```

`docker compose exec` runs a command in the running container. Run `bash` there to get a terminal in it, in `/workspace`:

*Terminal*

``` bash
docker compose exec analysis-env bash
```

Then, at the container’s prompt:

*Terminal*

``` bash
pwd
ls
```

*Output*

``` out
/workspace
DESCRIPTION  LICENSE   README.md    docker-compose.yml  renv       reports
Dockerfile   Makefile  _quarto.yml  pyproject.toml      renv.lock  uv.lock
```

`/workspace` shows the project folder, because it is mounted there. Type `exit` to leave the container, which keeps running. `docker compose down` stops and removes the container and its network:

*Terminal*

``` bash
docker compose down
```

*Output*

``` out
[+] down 2/2
 ✔ Container docker-uv-renv-analysis-env-1 Removed                                              0.3s
 ✔ Network docker-uv-renv_default          Removed                                              0.1s
```

### [33.3 Running a Docker container non-interactively using the Docker Compose](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-docker-compose.html#running-a-docker-container-non-interactively-using-the-docker-compose)

We can also use Docker Compose to run a command in a new container, non-interactively. `docker compose run` starts a new container for a service, runs the command you give it, and `--rm` deletes the container when the command finishes. For example, this renders the project’s reports, like the `docker run` command in [Python and R in one image](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv-renv.html), with the image and the mounts taken from `docker-compose.yml`:

*Terminal*

``` bash
docker compose run --rm analysis-env uv run quarto render
```

Here are the main lines of the output, without the progress counters:

*Output*

``` out
 Container docker-uv-renv-analysis-env-run-9991dfe97fe0 Creating
 Container docker-uv-renv-analysis-env-run-9991dfe97fe0 Created
[1/2] reports/report-python.qmd
Starting python3 kernel...[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
Done
Executing 'report-python.quarto_ipynb'
  Cell 1/2: ''...Done
  Cell 2/2: ''...Done
Starting python3 kernel...[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
Done
Executing 'report-python.quarto_ipynb'
  Cell 1/2: ''...Done
  Cell 2/2: ''...Done
[typst]: Compiling report-python.typ to report-python.pdf...DONE
[2/2] reports/report-r.qmd
processing file: report-r.qmd
output file: report-r.knit.md
processing file: report-r.qmd
output file: report-r.knit.md
[typst]: Compiling report-r.typ to report-r.pdf...DONE
Output created: reports/report-r.html
```

The reports are written to `reports/` in the project folder on your computer.

## [41  Data validation: Python (pointblank)](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/data-validation-python-pointblank.html)

pointblank started as an R package (see [Data validation: R (pointblank)](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/data-validation-r-pointblank.html)), and has been ported to Python: <https://posit-dev.github.io/pointblank/>

In this chapter we validate the Palmer penguins data, which records measurements of 344 penguins from three islands in Antarctica.

``` python
import pointblank as pb  # needs pointblank 1.3.0 or later, for get_row_flags()
from palmerpenguins import load_penguins

penguins = load_penguins()
penguins
```

|  | species | island | bill_length_mm | bill_depth_mm | flipper_length_mm | body_mass_g | sex | year |
|----|----|----|----|----|----|----|----|----|
| 0 | Adelie | Torgersen | 39.1 | 18.7 | 181.0 | 3750.0 | male | 2007 |
| 1 | Adelie | Torgersen | 39.5 | 17.4 | 186.0 | 3800.0 | female | 2007 |
| 2 | Adelie | Torgersen | 40.3 | 18.0 | 195.0 | 3250.0 | female | 2007 |
| 3 | Adelie | Torgersen | NaN | NaN | NaN | NaN | NaN | 2007 |
| 4 | Adelie | Torgersen | 36.7 | 19.3 | 193.0 | 3450.0 | female | 2007 |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |
| 339 | Chinstrap | Dream | 55.8 | 19.8 | 207.0 | 4000.0 | male | 2009 |
| 340 | Chinstrap | Dream | 43.5 | 18.1 | 202.0 | 3400.0 | female | 2009 |
| 341 | Chinstrap | Dream | 49.6 | 18.2 | 193.0 | 3775.0 | male | 2009 |
| 342 | Chinstrap | Dream | 50.8 | 19.0 | 210.0 | 4100.0 | male | 2009 |
| 343 | Chinstrap | Dream | 50.2 | 18.7 | 198.0 | 3775.0 | female | 2009 |

344 rows × 8 columns

### [41.1 Where are the missing values?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/data-validation-python-pointblank.html#where-are-the-missing-values)

Before we write any rules, it helps to know where the data is missing. `pb.missing_vals_tbl()` shows the missing values in each column, split into sections of rows from the top of the data to the bottom:

``` python
pb.missing_vals_tbl(data=penguins)
```

*(In the chapter, the output here is a table.)*

### [41.2 Checking values](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/data-validation-python-pointblank.html#checking-values)

We validate the data in two parts. The first part checks that the values we do have are sensible, and the second part, in the next section, checks for missing values. Keeping them apart makes each report easier to read, because a value outside its range and a value that is missing are different problems that we usually handle in different ways.

A validation starts with `pb.Validate()`, which takes the data and, optionally, a label for the report. Each validation step we chain onto it is one rule, and `interrogate()` runs every step:

``` python
values = (
    pb.Validate(
        data=penguins,
        label="Penguin measurements",
        thresholds=(0.01, 0.05, 0.10),  # warning, error, critical
    )
    .col_vals_in_set(columns="species", set=["Adelie", "Chinstrap", "Gentoo"])
    .col_vals_between(columns="bill_length_mm", left=30, right=60, na_pass=True)
    .col_vals_between(columns="body_mass_g", left=3000, right=5500, na_pass=True)
    .col_vals_ge(columns="flipper_length_mm", value=185, na_pass=True)
    .rows_distinct()
    .interrogate()
)
values
```

*(In the chapter, the output here is a table.)*

Setting `na_pass=True` lets missing values pass a step, so these steps only judge the values that are there.

The `thresholds` set how much failure we tolerate before pointblank raises a flag. A step is marked with a warning when at least 1% of its rows fail, an error at 5%, and critical at 10%. The report shows which level each step reached.

Each row of the report is one step. To see which penguins failed a step, we ask for that step’s report by its number:

``` python
values.get_step_report(i=3)  # which penguins failed step 3?
```

*(In the chapter, the output here is a table.)*

### [41.3 Checking missing values](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/data-validation-python-pointblank.html#checking-missing-values)

The second validation checks for missing values. `col_vals_not_null()` checks that a column has no missing values, and `rows_complete()` checks that no row has a missing value in any column:

``` python
missing = (
    pb.Validate(
        data=penguins,
        label="Penguin missing values",
        thresholds=(0.01, 0.05, 0.10),  # warning, error, critical
    )
    .col_vals_not_null(columns=["bill_length_mm", "sex"])
    .rows_complete()
    .interrogate()
)
missing
```

*(In the chapter, the output here is a table.)*

Giving `col_vals_not_null()` two columns creates one step for each column, so this validation has three steps. The thresholds turn these checks into a rule about how much missingness we accept, which is the “missingness not beyond expected threshold” item from the checklist in [Data validation](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/data-validation.html).

### [41.4 Splitting the passing and failing rows](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/data-validation-python-pointblank.html#splitting-the-passing-and-failing-rows)

After interrogating a validation, we can split the data into the rows that passed every step and the rows that failed at least one. We keep working with the rows that passed, and give the rows that failed to a teammate to fix:

``` python
passed = values.get_sundered_data(type="pass")  # keep working with these
failed = values.get_sundered_data(type="fail")  # a teammate fixes these
pb.preview(data=failed)  # a quick look at the rows that failed
```

*(In the chapter, the output here is a table.)*

``` python
failed.to_csv("penguins_to_fix.csv", index=False)
```

Because our value checks use `na_pass=True`, a row with missing values can still be in `passed`. Whether to drop or keep those rows is a decision for the missing values validation.

### [41.6 Learn more](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/data-validation-python-pointblank.html#learn-more)

- The [pointblank for Python documentation](https://posit-dev.github.io/pointblank/), including the [list of validation methods](https://posit-dev.github.io/pointblank/reference/).
