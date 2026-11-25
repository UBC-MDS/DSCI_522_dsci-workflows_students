# Course materials: 2026-11-24 lecture

## Links

- Demo repository: <https://github.com/chendaniely/2026-11-24-docker>
  - [`Dockerfile`](https://github.com/chendaniely/2026-11-24-docker/blob/main/Dockerfile)
  - [`docker-compose.yml`](https://github.com/chendaniely/2026-11-24-docker/blob/main/docker-compose.yml)
  - [`pyproject.toml`](https://github.com/chendaniely/2026-11-24-docker/blob/main/pyproject.toml), [`uv.lock`](https://github.com/chendaniely/2026-11-24-docker/blob/main/uv.lock) and [`.python-version`](https://github.com/chendaniely/2026-11-24-docker/blob/main/.python-version)
  - [`hello.py`](https://github.com/chendaniely/2026-11-24-docker/blob/main/hello.py)
  - [Commits](https://github.com/chendaniely/2026-11-24-docker/commits/main)
- The textbook's example project with Python and R in one image (chapters 32-34): <https://github.com/chendaniely/docker-uv-renv>
- uv's guide to installing uv in a Docker image: <https://docs.astral.sh/uv/guides/integration/docker/#installing-uv>
- Textbook, *Reproducible and Trustworthy Workflows for Data Science*:
  <https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/>
  - [22 uv: pinning exact versions](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/virtual-environments-python-uv-exact-pins.html)
  - [27 Introduction to containerization](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html)
    - [27.7 Image vs container?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#image-vs-container)
    - [27.8 What is a container registry?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#what-is-a-container-registry)
  - [28 Using and running containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html)
    - [28.1.2 Mounting volumes to containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#mounting-volumes-to-containers)
    - [28.1.5 Use a container to execute a script](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#use-a-container-to-execute-a-script)
    - [28.2 Docker command-line commands](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#docker-command-line-commands)
  - [29 Customizing and building containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html)
    - [29.1.3 Layer caching](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#layer-caching)
    - [29.1.4 Guidelines for `RUN` commands](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#guidelines-for-run-commands)
    - [29.2.1 `CMD` or `ENTRYPOINT`?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#cmd-or-entrypoint)
    - [29.3 Choosing a base image for your Dockerfile](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#choosing-a-base-image-for-your-dockerfile)
  - [30 Python packages with uv in an image](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv.html)
  - [32 Python and R in one image](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv-renv.html)
  - [33 Containers: Docker Compose](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-docker-compose.html)
  - [34 Working in a container over ssh with Positron](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-ssh-positron.html)
  - [35 Building images for several platforms](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-platforms.html)

## About these materials

What this lecture worked from: the class's demo repository, and textbook chapters from
*Reproducible and Trustworthy Workflows for Data Science*
(<https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/>),
as published on 2026-11-24. Each textbook heading links to its published section.

The syllabus lists chapters 29, 30, 32, 34 and 35 for this lecture (chapter 31 is the R
version of chapter 30; this class used Python). The 2026-11-19 lecture had already covered
most of chapter 29. This lecture took up the sections of chapters 27-29 and the Docker
Compose chapter (33) that the 2026-11-19 lecture didn't reach, and the uv chapter on
pinning exact versions (22). The instructor counts all of these as covered by this
lecture, so none of them is held back for next class.

## Demo repository

The repository the class worked in: <https://github.com/chendaniely/2026-11-24-docker>. As GitHub shows it on 2026-11-24, it has two
commits and no issues or pull requests.

The first commit is the warm-up exercise: the instructor had Claude Code create the
repository with a `Dockerfile` on `rocker/r-ver:4.6.2`, which Claude Code gave a default
command of R. It also wrote a `README.md` and a `Makefile`, which still describe this
R image:

```dockerfile
FROM rocker/r-ver:4.6.2

CMD ["R"]
```

The second commit, "files from class", has what the class built during the lecture. The
`Dockerfile` now starts from Ubuntu and installs the Python packages of a uv project:

```dockerfile
FROM ubuntu:24.04

# how to install uv
COPY --from=ghcr.io/astral-sh/uv:0.13.7 /uv /uvx /usr/local/bin/

WORKDIR /workspace

ENV UV_PROJECT_ENVIRONMENT=/opt/venv
COPY pyproject.toml uv.lock .python-version ./
RUN uv sync --locked
```

The uv project: `pyproject.toml`,

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

`.python-version`,

```
3.14
```

`uv.lock`,

```toml
version = 1
revision = 5
requires-python = ">=3.14"

[[package]]
name = "2026-11-24-docker"
version = "0.1.0"
source = { virtual = "." }
dependencies = [
    { name = "cowsay" },
]

[package.metadata]
requires-dist = [{ name = "cowsay", specifier = "==6.1" }]

[[package]]
name = "cowsay"
version = "6.1"
source = { registry = "https://pypi.org/simple" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/f1/13/63c0a02c44024ee16f664e0b36eefeb22d54e93531630bd99e237986f534/cowsay-6.1-py3-none-any.whl", hash = "sha256:274b1e6fc1b966d53976333eb90ac94cb07a450a700b455af9fbdf882244b30a", size = 25560, upload-time = "2023-09-25T16:30:01.619Z" },
]
```

and `hello.py`:

```python
import cowsay

cowsay.cow("hello, moo.")
```

`my_secrets.txt`, the file the class used to show that a mounted folder is shared
between the computer and the container:

```
i'm afraid of the dark.
i eat baby food.
```

The `docker-compose.yml` the class wrote. In class, `docker compose up` didn't keep the
container running, and the instructor plans to fix the demo next class:

```yaml
services:
  analysis-env:
    build: .
    image: 2026-11-24-docker
    volumes:
      - .:/workspace
```

## [22 uv: pinning exact versions](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/virtual-environments-python-uv-exact-pins.html)

### [Learning Objectives](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/virtual-environments-python-uv-exact-pins.html#learning-objectives)

1.  Explain the difference between a lower bound (`>=`) and an exact pin (`==`) in `pyproject.toml`, and what `uv.lock` records in each case
2.  Explain why a data analysis project declares exact versions while a package declares ranges
3.  Configure `uv add` to write exact pins with `add-bounds = "exact"`, convert existing lower bounds, and change a pinned version

### [22.1 What `uv add` writes by default](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/virtual-environments-python-uv-exact-pins.html#what-uv-add-writes-by-default)

In [uv: projects](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/virtual-environments-python-uv-projects.html), `uv add` wrote a *lower bound* for each package. Here is a fresh project after `uv add pandas`:

*Terminal*

``` bash
uv add pandas
```

*Output*

``` out
Using CPython 3.14.3
Creating virtual environment at: .venv
Resolved 5 packages in 19ms
Installed 4 packages in 65ms
 + numpy==2.5.5
 + pandas==3.1.1
 + python-dateutil==4.0.0
 + tzdata==2026.6
```

    pyproject.toml

``` toml
[project]
name = "pins-demo"
version = "0.1.0"
requires-python = ">=3.14"
dependencies = [
    "pandas>=3.1.1",
]
```

`pandas>=3.1.1` declares “pandas 3.1.1 or anything newer”. The exact version you got is still written down, but only in `uv.lock`:

    uv.lock

``` toml
[[package]]
name = "pandas"
version = "3.1.1"
```

So the project *declares* a range and *locks* one version. As long as everyone runs `uv sync` against that `uv.lock`, everyone gets pandas 3.1.1.

### [22.2 Why an analysis project declares exact versions](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/virtual-environments-python-uv-exact-pins.html#why-an-analysis-project-declares-exact-versions)

The range in `pyproject.toml` matters whenever the lockfile is not the thing being read.

- **The lockfile gets regenerated.** `uv lock --upgrade`, a deleted `uv.lock`, or a merge conflict resolved by re-locking lets every package move anywhere inside its range, and nothing in `pyproject.toml` records that the analysis was run with 3.1.1.
- **People read `pyproject.toml`, not `uv.lock`.** It is short enough to read in a code review or a README. `pandas==3.1.1` says what the analysis was run with, and `pandas>=3.1.1` does not.
- **Other tools read `pyproject.toml` too.** `pip install --only-deps .` installs from it, and it ignores `uv.lock`.

With an exact pin in `pyproject.toml`, the declared version and the locked version are the same, and a version only changes when someone changes the pin. That change shows up in the diff of `pyproject.toml`, where reviewers will see it.

A **package**, the kind of project you will build in the [packaging chapters](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/packaging.html), is the opposite case. A package gets installed into *other people’s* environments, next to whatever versions of pandas their projects already use. Exact pins there would make your package impossible to install alongside theirs, so packages declare ranges and leave the exact choice to the project that installs them.

| Kind of project | Declares | Why |
|----|----|----|
| Data analysis (an application) | exact versions, `pandas==3.1.1` | The result depends on the exact versions, and nobody installs it into another environment |
| Package (a library) | ranges, `pandas>=3.0` | It has to fit into other people’s environments |

### [22.3 Making `uv add` write exact versions](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/virtual-environments-python-uv-exact-pins.html#making-uv-add-write-exact-versions)

`uv` has a setting for this. Add a `[tool.uv]` table to `pyproject.toml`:

    pyproject.toml

``` toml
[tool.uv]
# `uv add` writes an exact version (==)
add-bounds = "exact"
```

That table and comment are taken from the [docker-uv-renv](https://github.com/chendaniely/docker-uv-renv) example project (MIT license), which the container chapters build on.

From then on, `uv add` writes `==`. Here is the same project after removing pandas and adding it again:

*Terminal*

``` bash
uv remove pandas
uv add pandas
```

*Output*

``` out
Resolved 1 package in 5ms
Uninstalled 4 packages in 200ms
 - numpy==2.5.5
 - pandas==3.1.1
 - python-dateutil==4.0.0
 - tzdata==2026.6
Resolved 5 packages in 7ms
Installed 4 packages in 29ms
 + numpy==2.5.5
 + pandas==3.1.1
 + python-dateutil==4.0.0
 + tzdata==2026.6
```

    pyproject.toml

``` toml
[project]
name = "pins-demo"
version = "0.1.0"
requires-python = ">=3.14"
dependencies = [
    "pandas==3.1.1",
]

[tool.uv]
add-bounds = "exact"
```

The setting lives in `pyproject.toml`, so everyone on the project gets the same behavior from `uv add`.

For a single command, `uv add --bounds exact pandas` does the same thing without the setting. `--bounds` also accepts `lower` (the default), `major`, and `minor`, which write wider ranges.

**Existing lower bounds do not change**

The setting only changes what `uv add` writes *from now on*. Running `uv add pandas` again in a project that already has `pandas>=3.1.1` leaves that line as it is.

To convert a package you already have, look up the version you are using and add it again with that version:

*Terminal*

``` bash
uv tree --depth 1
```

*Output*

``` out
Resolved 6 packages in 13ms
penguin-analysis v0.1.0
├── palmerpenguins v0.1.6
└── pandas v3.1.1
```

*Terminal*

``` bash
uv add "pandas==3.1.1" "palmerpenguins==0.1.6"
```

### [22.4 Changing a pinned version](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/virtual-environments-python-uv-exact-pins.html#changing-a-pinned-version)

With an exact pin, `uv lock --upgrade-package pandas` cannot move pandas, because `pyproject.toml` only allows one version. To move it, change the pin:

*Terminal*

``` bash
uv add "pandas==3.0.5"
```

*Output*

``` out
Resolved 5 packages in 118ms
Downloading pandas (9.5MiB)
 Downloaded pandas
Prepared 1 package in 1.16s
Uninstalled 1 package in 100ms
Installed 1 package in 14ms
 - pandas==3.1.1
 + pandas==3.0.5
```

One command updates `pyproject.toml`, `uv.lock`, and `.venv/` together, and the commit that changes the pin is the record of when and why it moved.

The packages you did not name, such as `numpy` and `python-dateutil` here, are still pinned exactly, but only in `uv.lock`. `uv lock --upgrade-package numpy` moves one of them, as in [uv: sharing and managing an environment](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/virtual-environments-python-uv-sharing.html).

### [22.5 The same idea in R](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/virtual-environments-python-uv-exact-pins.html#the-same-idea-in-r)

R projects declare their packages in a `DESCRIPTION` file, and this book pins those exactly too:

    DESCRIPTION

``` default
Depends:
    dplyr (== 1.2.1)
```

`DESCRIPTION` with `==` plays the part of `pyproject.toml` with `add-bounds = "exact"`, and `renv.lock` plays the part of `uv.lock`. [renv: declaring packages in `DESCRIPTION`](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/virtual-environments-r-renv-description.html) shows how.

## [27 Introduction to containerization](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html)

### [27.7 Image vs container?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#image-vs-container)

Analogy: The program Chrome is like a Docker image, whereas a Chrome window is like a Docker container.

![](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/img/instance_analogy.png)

You can list the container **images** on your computer that you pulled using Docker via `docker images`. After pulling the images for this chapter, the list includes these three, and any other images you have:

*Terminal*

``` bash
docker images
```

*Output*

``` out
IMAGE                                             ID             DISK USAGE   CONTENT SIZE   EXTRA
quay.io/jupyter/datascience-notebook:2025-03-14   bf25d19758c0       9.06GB         2.17GB        
rocker/r-ver:4.3.2                                4e32addfc4da       1.11GB          313MB        
rocker/rstudio:4.4.2                              6bfc87fb66d0       3.16GB          734MB        
```

`DISK USAGE` is how much space an image takes on your computer, and `CONTENT SIZE` is about how much was downloaded.

You can list the states of containers that have been started by Docker on your computer (and not yet removed) via `docker ps -a`. Here, the R container from the first exercise and the RStudio container from the second are both running:

*Terminal*

``` bash
docker ps -a
```

*Output*

``` out
CONTAINER ID   IMAGE                  COMMAND   CREATED        STATUS                  PORTS                                         NAMES
adf3ea77f63f   rocker/rstudio:4.4.2   "/init"   1 second ago   Up Less than a second   0.0.0.0:8787->8787/tcp, [::]:8787->8787/tcp   objective_hoover
adca5933388b   rocker/r-ver:4.3.2     "R"       1 second ago   Up Less than a second                                                 hardcore_swartz
```

### [27.8 What is a container registry?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#what-is-a-container-registry)

A container registry is a remote repository, or collection of repositories, used to share container images. This is similar to remote version control repositories for sharing code. Instead of code, however, it is container images that are pushed and pulled to/from there. For this course we will focus on the widely used Docker Hub container registry: <https://hub.docker.com/>.

However, there are many container registries that can be used, including:

- <https://github.com/>
- <https://quay.io/>
- <https://aws.amazon.com/ecr/>

In the examples above, we have used the `rocker/rstudio` container, which comes from Docker Hub, and the Jupyter server comes from `quay.io`.

**Exercise**

**Exploring container registries**

Let’s visit the repositories for the two container images that we used in the exercise earlier in class:

- [rocker/rstudio](https://hub.docker.com/r/rocker/rstudio)
- [quay.io/jupyter/datascience-notebook](https://quay.io/repository/jupyter/datascience-notebook?tab=tags)

Question: you pulled these images with `docker pull` before you started. What would `docker run ...` have done if you had not?

Answer: `docker run ...` will first look for images you have locally, and run those if they exist. If they do not exist, it then attempts to pull the image from the registry named in the image (Docker Hub, if the image name does not name a registry).

## [28 Using and running containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html)

#### [28.1.2 Mounting volumes to containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#mounting-volumes-to-containers)

Oftentimes, we want to use the software made available to us in containers on files on our computers. To do this, we need to explicitly tell Docker to mount a volume to the container. We can do this via: `-v <path_to_local_computer_directory>:<absolute_path_to_container_directory>`.

Often, we want to mount the volume from our current directory (where we are working), and we can do that with `$(pwd)`, which prints the current directory, in place of the path to our computer’s directory. This is a useful shorthand command when you work with multiple people, so the same command will work on different computers since you are not hard-coding the local computer path.

To mount our current directory at `/workspace` in a container from the `ubuntu:24.04` image, we type the following on our laptop:

- [macOS and Linux](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html)
- [Windows (Git Bash)](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html)
- [Windows (PowerShell)](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html)

*Terminal*

``` bash
docker run --rm -it -v "$(pwd):/workspace" ubuntu:24.04
```

*Terminal*

``` bash
docker run --rm -it -v "/$(pwd):/workspace" ubuntu:24.04
```

``` powershell
docker run --rm -it -v "${PWD}:/workspace" ubuntu:24.04
```

Then, at the container’s prompt, go to the directory where you mounted your files and list them:

*Terminal*

``` bash
cd /workspace
ls
```

*Output*

``` out
hello.R
```

Here, the current directory on the laptop held one file, `hello.R`.

**Why `/$(pwd)` in Git Bash?**

Git Bash turns command-line arguments that start with `/` into Windows paths, so `/workspace` could reach Docker as `C:/Program Files/Git/workspace`. Doubling the first slash stops that (see “Known issues” in the [Git for Windows release notes](https://github.com/git-for-windows/build-extra/blob/main/ReleaseNotes.md#known-issues)). `/$(pwd)` does it for the mount, and a path inside the container, such as `/workspace/hello.R` below, is written `//workspace/hello.R` in Git Bash.

**Note**

If you are mounting volumes to a container from a Docker image that runs a web app, be sure to read the documentation to see where you should mount that volume. Usually, the web apps are only exposed to certain directories, and you will only be able to access the files in the mounted volume if you mount them to the correct place. For example, in the `rocker/rstudio` image that we loaded earlier, volumes need to be mounted within `/home/rstudio/` to be able to access them via the RStudio Server web app.

##### [Windows notes for mounting volumes](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#windows-notes-for-mounting-volumes)

- Windows machines need to explicitly share drives with Docker. This should be part of your computer setup!
- On Windows, the laptop path depends on what shell you are using. Here are some details:
  - If you are going to run it in Windows terminal, then the command to share the current directory should be:

  *Terminal*

  ``` bash
  docker run --rm -it -v /$(pwd):<PATH_ON_CONTAINER> <IMAGE_NAME>
  ```

  - If you are going to run it in PowerShell, then the command should be:

  *Terminal*

  ``` bash
  docker run --rm -it -v <ABSOLUTE_PATH_ON_YOUR_COMPUTER>:<PATH_ON_CONTAINER> <IMAGE_NAME>
  ```

  (`pwd` and variants do not seem to work). And the path must be formatted like: `C:\Users\tiffany.timbers\Documents\project\:/home/project`

#### [28.1.5 Use a container to execute a script](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#use-a-container-to-execute-a-script)

What if, instead of running the container interactively, we wanted to run a script? Let’s take this R script, named `hello.R`, shown below, which prints the version of R that runs it, and a summary of a column of R’s built-in `mtcars` data:

``` r
# hello.R
cat("Hello from", R.version.string, "\n")
summary(mtcars$mpg)
```

Assuming that script is in our current working directory, we can mount the directory and then run the script with `Rscript` in a container from the `rocker/r-ver:4.3.2` image:

- [macOS and Linux](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html)
- [Windows (Git Bash)](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html)
- [Windows (PowerShell)](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html)

*Terminal*

``` bash
docker run --rm -v "$(pwd):/workspace" rocker/r-ver:4.3.2 Rscript /workspace/hello.R
```

*Terminal*

``` bash
docker run --rm -v "/$(pwd):/workspace" rocker/r-ver:4.3.2 Rscript //workspace/hello.R
```

``` powershell
docker run --rm -v "${PWD}:/workspace" rocker/r-ver:4.3.2 Rscript /workspace/hello.R
```

This should result in:

*Output*

``` out
Hello from R version 4.3.2 (2023-10-31) 
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
  10.40   15.43   19.20   20.09   22.80   33.90 
```

The script ran with R 4.3.2, the version in the image, whatever version of R your computer has.

Now, that was a small example, but the same `docker run` command can run a whole analysis non-interactively. [Python and R in one image](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv-renv.html) uses it to render a project’s reports in Python and R.

### [28.2 Docker command-line commands](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#docker-command-line-commands)

The table below summarizes the Docker commands we have learned so far and can serve as a useful reference when we are using Docker:

#### [28.2.1 Docker commands](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#docker-commands)

| command/flag | What it does |
|----|----|
| `pull` | Downloads a Docker image from Docker Hub |
| `images` | Tells you what container images are installed on your machine |
| `rmi` | Deletes a specified container image from your machine |
| `ps -a` | Tells you what containers are on your machine, including stopped ones |
| `stop` | Stops a specified running container |
| `rm` | Removes a specified stopped container |
| `run` | Launches a container from an image |
| `exit` | Exits a Docker container |

#### [28.2.2 Docker `run` commands](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#docker-run-commands)

| command/flag | What it does |
|----|----|
| `-it` | Tells Docker to run the container interactively |
| `--rm` | Makes a container ephemeral (deletes it upon exit) |
| `-v` | Mounts a volume of your computer to the Docker container |
| `-p` | Specifies the ports to map a web app to |
| `-e` | Sets environment variables in the container (*e.g.*, PASSWORD=“apassword”) |

## [29 Customizing and building containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html)

#### [29.1.3 Layer caching](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#layer-caching)

Docker saves each step’s result as a layer, and reuses a layer when nothing in its step, or in the steps above it, has changed. To see this, change only the message on the `CMD` line of the `Dockerfile`:

``` dockerfile
CMD ["Rscript", "-e", "cowsay::say('Moo! Only my message changed.')"]
```

Then build again:

*Terminal*

``` bash
docker build --tag hello-cowsay .
```

*Output*

``` out
[+] Building 0.2s (6/6) FINISHED                                               docker:desktop-linux
 => [internal] load build definition from Dockerfile                                           0.0s
 => => transferring dockerfile: 179B                                                           0.0s
 => [internal] load metadata for docker.io/rocker/r-ver:4.6.2                                  0.0s
 => [internal] load .dockerignore                                                              0.0s
 => => transferring context: 2B                                                                0.0s
 => [1/2] FROM docker.io/rocker/r-ver:4.6.2@sha256:8739c76d2d9316698a7145b032601f1e82249fdee3  0.0s
 => => resolve docker.io/rocker/r-ver:4.6.2@sha256:8739c76d2d9316698a7145b032601f1e82249fdee3  0.0s
 => CACHED [2/2] RUN Rscript -e "install.packages('cowsay')"                                   0.0s
 => exporting to image                                                                         0.1s
 => => exporting layers                                                                        0.0s
 => => exporting manifest sha256:f2d1c5ab15c8048a1863f62aa572f3bc2c971015fe8a2c04c5a4f1123137  0.0s
 => => exporting config sha256:0146dc6311dfcf1595b66373383e7f7bc1b4f0deae336219d9487b03da6d38  0.0s
 => => exporting attestation manifest sha256:bc8aca2ce37900fcdcd01fda5fed9286c997df019e23c971  0.0s
 => => exporting manifest list sha256:168f3c35f574628804baaf63e71be4164a7d1534ca35229a6827c7c  0.0s
 => => naming to docker.io/library/hello-cowsay:latest                                         0.0s
 => => unpacking to docker.io/library/hello-cowsay:latest                                      0.0s
```

The `RUN` step says `CACHED`. Docker reused the layer with cowsay installed and only changed the default command:

*Terminal*

``` bash
docker run --rm hello-cowsay
```

*Output*

``` out
 _______________________________ 
< Moo! Only my message changed. >
 ------------------------------- 
      \
       \

        ^__^ 
        (oo)\ ________ 
        (__)\         )\ /\ 
             ||------w|
             ||      ||
```

Installing one package took a few seconds, but installing many packages, or packages that R compiles from source, can take many minutes, and the cache skips all of it. This is why a `Dockerfile` puts the steps that change least often, such as installing software, near the top, and the steps that change most often near the bottom. A change to one step rebuilds that step and every step below it.

`docker image ls` lists the image, and `docker history` lists its layers, newest first (`head -5` keeps the first five lines):

*Terminal*

``` bash
docker image ls hello-cowsay
```

*Output*

``` out
IMAGE                 ID             DISK USAGE   CONTENT SIZE   EXTRA
hello-cowsay:latest   168f3c35f574       1.45GB          390MB        
```

*Terminal*

``` bash
docker history hello-cowsay | head -5
```

*Output*

``` out
IMAGE          CREATED          CREATED BY                                      SIZE      COMMENT
168f3c35f574   17 seconds ago   CMD ["Rscript" "-e" "cowsay::say('Moo! Only …   0B        buildkit.dockerfile.v0
<missing>      17 seconds ago   RUN /bin/sh -c Rscript -e "install.packages(…   4.17MB    buildkit.dockerfile.v0
<missing>      11 days ago      COPY scripts /rocker_scripts # buildkit         168kB     buildkit.dockerfile.v0
<missing>      11 days ago      CMD ["R"]                                       0B        buildkit.dockerfile.v0
```

The top two rows are the layers our `Dockerfile` added. The `RUN` layer holds the 4.17MB of R packages, and it shows that Docker ran the command with `/bin/sh -c`. The `CMD` layer adds no files, only the default command, so its size is 0B. The rows below come from `rocker/r-ver:4.6.2`, including its `CMD ["R"]`, which our `CMD` replaces.

**More information**

Docker runs `RUN` commands with the shell `/bin/sh`, not Bash, unless the `Dockerfile` picks another shell with the `SHELL` instruction (see Docker’s [`Dockerfile` reference](https://docs.docker.com/reference/dockerfile/)). For commands like these, the two shells behave the same.

#### [29.1.4 Guidelines for `RUN` commands](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#guidelines-for-run-commands)

Each `RUN` command creates a new layer in the Docker image. Each layer in a Docker image takes more disk space. As a consequence, we want to minimize the number of layers where reasonably possible. How can we do this?

Install everything that can be installed by a tool (e.g., `apt-get`, or `install.packages()` in R) at once (i.e., when installing 5 programs via `apt-get`, do not call `apt-get` five times; instead do: `apt-get install tool1 tool2 tool3 tool4 tool5`, and in R, `install.packages(c("pkg1", "pkg2"))`). However, doing this can lead to long lines. In response, we can break a single command across lines in the shell by using the `\` character. For example, to reduce the long line below, which uses `apt-get` to install the programs Git, Tiny Nano, Less, and wget:

*Terminal*

``` bash
apt-get install --yes git nano-tiny less wget
```

We can use `\` after each program to break the long command across lines and make the command more readable (especially if there were even more programs to install). Similarly, we indent the lines after `\` to increase readability:

*Terminal*

``` bash
apt-get install --yes \
    git \
    nano-tiny \
    less \
    wget
```

We can also group together related commands that depend upon each other. When doing this, we need to be careful, though, as sometimes we don’t want to run a command if the command that was run immediately before it failed. We can specify this in the shell using `&&`. For example, if we want to not run `apt-get` installation commands if `apt-get update` failed, we can write:

*Terminal*

``` bash
apt-get update && \
    apt-get install --yes git
```

#### [29.2.1 `CMD` or `ENTRYPOINT`?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#cmd-or-entrypoint)

Both set what a container runs when it starts. They differ in what `docker run` can replace. A command after the image name in `docker run` replaces `CMD`. For example, this runs `R --version` in the `hello-cowsay` image in place of its cowsay message (`head -1` keeps the first line):

*Terminal*

``` bash
docker run --rm hello-cowsay R --version | head -1
```

*Output*

``` out
R version 4.6.2 (2026-10-29) -- "Diversified Portfolio"
```

`ENTRYPOINT` is not replaced this way. Anything after the image name is passed to it as arguments, and replaces only `CMD`. With both, `ENTRYPOINT` holds the part that always runs, and `CMD` holds the default arguments. For example, this `Dockerfile`, in a folder of its own, always runs `Rscript -e`, with cowsay R code as the default:

``` dockerfile
FROM rocker/r-ver:4.6.2

RUN Rscript -e "install.packages('cowsay')"

ENTRYPOINT ["Rscript", "-e"]
CMD ["cowsay::say('Hello from my first image!')"]
```

*Terminal*

``` bash
docker build --tag cowsay-entrypoint .
docker run --rm cowsay-entrypoint
```

*Output*

``` out
 ____________________________ 
< Hello from my first image! >
 ---------------------------- 
      \
       \

        ^__^ 
        (oo)\ ________ 
        (__)\         )\ /\ 
             ||------w|
             ||      ||
```

Passing different R code replaces the default, but still runs it with `Rscript -e`:

*Terminal*

``` bash
docker run --rm cowsay-entrypoint "cowsay::say('Only the R code changed.')"
```

*Output*

``` out
 __________________________ 
< Only the R code changed. >
 -------------------------- 
      \
       \

        ^__^ 
        (oo)\ ________ 
        (__)\         )\ /\ 
             ||------w|
             ||      ||
```

The images in this book, `rocker/r-ver` among them, set only `CMD`, so that a command such as `bash` after the image name replaces it, as in step 3 of the workflow.

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

## [30 Python packages with uv in an image](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv.html)

### [Learning Objectives](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv.html#learning-objectives)

1.  Install a uv project’s Python packages into a Docker image with `uv sync --locked`
2.  Explain why the image keeps its virtual environment in `/opt/venv`, outside the mounted project folder
3.  Add a Python package to a project whose packages are in an image, and fix a `uv.lock` that no longer matches `pyproject.toml`

### [Download the images before you start](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv.html#download-the-images-before-you-start)

The examples in this chapter build on two images. Start Docker first (on macOS and Windows, open Docker Desktop), then download (pull) them before you start:

*Terminal*

``` bash
docker pull ubuntu:24.04
docker pull ghcr.io/astral-sh/uv:0.13.7
```

### [30.1 The project](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv.html#the-project)

This chapter puts the Python packages of a small uv project into a Docker image. It is a uv project like the ones in [Virtual environments: Python (uv)](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/virtual-environments-python-uv.html), and its files are in the book repository’s `demos/docker-uv/end` folder. `hello.py` prints a message with the [cowsay](https://pypi.org/project/cowsay/) package:

``` python
import cowsay

cowsay.cow("Hello from Python in my image!")
```

`pyproject.toml` lists the package with an exact version, and `add-bounds = "exact"` makes `uv add` write exact versions too (see [uv: pinning exact versions](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/virtual-environments-python-uv-exact-pins.html)):

``` toml
[project]
name = "docker-uv"
version = "0.1.0"
requires-python = ">=3.14"
dependencies = [
    "cowsay==6.1",
]

[tool.uv]
# `uv add` writes an exact version (==)
add-bounds = "exact"
```

`.python-version` holds `3.14`, and `uv.lock` locks cowsay and everything it needs. On your computer, `uv run` creates the project’s `.venv` folder and runs the script:

*Terminal*

``` bash
uv run hello.py
```

*Output*

``` out
Using CPython 3.14.3
Creating virtual environment at: .venv
Installed 1 package in 9ms
  ______________________________
| Hello from Python in my image! |
  ==============================
                              \
                               \
                                 ^__^
                                 (oo)\_______
                                 (__)\       )\/\
                                     ||----w |
                                     ||     ||
```

### [30.2 A `Dockerfile` for a uv project](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv.html#a-dockerfile-for-a-uv-project)

Here is the project’s `Dockerfile`. Its uv lines are the same as in [docker-uv-renv](https://github.com/chendaniely/docker-uv-renv), the example project that [Docker Compose](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-docker-compose.html) uses:

``` dockerfile
# Ubuntu Linux, with no Python: uv installs Python itself
FROM ubuntu:24.04

# install python uv
# https://docs.astral.sh/uv/guides/integration/docker/#installing-uv
COPY --from=ghcr.io/astral-sh/uv:0.13.7 /uv /uvx /usr/local/bin/

# The project is mounted over /workspace, so the packages go in /opt
WORKDIR /workspace

# python packages in /opt/venv
ENV UV_PROJECT_ENVIRONMENT=/opt/venv
COPY pyproject.toml uv.lock .python-version ./
# --locked: stop if uv.lock doesn't match pyproject.toml
RUN uv sync --locked
```

- `FROM ubuntu:24.04` starts from Ubuntu Linux, which has no Python. uv installs the Python version that `.python-version` asks for.
- `COPY --from=ghcr.io/astral-sh/uv:0.13.7` copies the `uv` and `uvx` programs out of the image that uv publishes, as [uv’s Docker guide](https://docs.astral.sh/uv/guides/integration/docker/#installing-uv) shows. The tag pins uv’s version, the same way a lockfile pins a package’s.
- `WORKDIR /workspace` makes `/workspace` the working directory, for the rest of the build and for containers that run from the image. You will mount your project folder there.
- `ENV UV_PROJECT_ENVIRONMENT=/opt/venv` tells uv to put the project’s virtual environment in `/opt/venv`, instead of in `.venv` inside the project folder (see [uv’s environment variables](https://docs.astral.sh/uv/reference/environment/#uv_project_environment)). The section after next shows why.
- `COPY pyproject.toml uv.lock .python-version ./` copies only the files that list the packages, not the code. Editing `hello.py` then never reinstalls the packages, because the `COPY` and `RUN` steps above it have not changed (see [Building images](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html)).
- `RUN uv sync --locked` installs Python and the packages listed in `uv.lock`. `--locked` stops the build if `uv.lock` does not match `pyproject.toml`.

### [30.3 Build the image](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv.html#build-the-image)

From the project folder:

*Terminal*

``` bash
docker build --tag docker-uv .
```

*Output*

``` out
[+] Building 8.8s (12/12) FINISHED                                             docker:desktop-linux
 => [internal] load build definition from Dockerfile                                           0.1s
 => => transferring dockerfile: 553B                                                           0.0s
 => [internal] load metadata for ghcr.io/astral-sh/uv:0.13.7                                   0.6s
 => [internal] load metadata for docker.io/library/ubuntu:24.04                                0.1s
 => [internal] load .dockerignore                                                              0.0s
 => => transferring context: 2B                                                                0.0s
 => CACHED FROM ghcr.io/astral-sh/uv:0.13.7@sha256:96f40d3904aad8d0bd010539001d36c8e2188b981e  0.2s
 => => resolve ghcr.io/astral-sh/uv:0.13.7@sha256:96f40d3904aad8d0bd010539001d36c8e2188b981e1  0.1s
 => CACHED [stage-0 1/5] FROM docker.io/library/ubuntu:24.04@sha256:008173c23f95b170204355c12  0.2s
 => => resolve docker.io/library/ubuntu:24.04@sha256:008173c23f95b170204355c12626cb5a965d779a  0.2s
 => [internal] load build context                                                              0.0s
 => => transferring context: 964B                                                              0.0s
 => [stage-0 2/5] COPY --from=ghcr.io/astral-sh/uv:0.13.7 /uv /uvx /usr/local/bin/             0.1s
 => [stage-0 3/5] WORKDIR /workspace                                                           0.0s
 => [stage-0 4/5] COPY pyproject.toml uv.lock .python-version ./                               0.0s
 => [stage-0 5/5] RUN uv sync --locked                                                         3.7s
 => exporting to image                                                                         3.9s
 => => exporting layers                                                                        2.8s
 => => exporting manifest sha256:6e630dbe112a1dc156ddc9fd6ad3c7b8585f9c045fdb5c95546843ec6ca2  0.0s
 => => exporting config sha256:bbae306c5d2d7852ecf4b128ed8508269a04e620187bc9e8a5fd9a5d68cfe3  0.0s
 => => exporting attestation manifest sha256:6e9b8ca9f5749e9b646d18487a8066fbb2a7ac07ae4971d5  0.0s
 => => exporting manifest list sha256:c7eced3c63cca5bff431f82a2ec381a1bc17a49a2839cd91ad1b5c0  0.0s
 => => naming to docker.io/library/docker-uv:latest                                            0.0s
 => => unpacking to docker.io/library/docker-uv:latest                                         1.0s
```

The first `FROM` line is uv’s image, which `COPY --from` reads `uv` from. To see what `uv sync` printed, build with `--progress=plain`, which shows each step’s own output, and `--no-cache`, which runs every step again instead of reusing its layer. Here is the `uv sync` step:

*Terminal*

``` bash
docker build --progress=plain --no-cache --tag docker-uv .
```

*Output*

``` out
#11 [stage-0 5/5] RUN uv sync --locked
#11 0.309 Downloading cpython-3.14.10-linux-aarch64-gnu (download) (29.2MiB)
#11 3.201  Downloaded cpython-3.14.10-linux-aarch64-gnu (download)
#11 3.352 Using CPython 3.14.10
#11 3.352 Creating virtual environment at: /opt/venv
#11 3.359 Resolved 2 packages in 2ms
#11 3.434 Prepared 1 package in 74ms
#11 3.451 Installed 1 package in 16ms
```

uv downloaded Python 3.14, created the virtual environment at `/opt/venv`, and installed cowsay into it.

### [30.4 Run the project in a container](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv.html#run-the-project-in-a-container)

The image has the packages but not the code. Mount the project folder at `/workspace`, and run the script with `uv run` in place of the image’s default command (see [Running containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html)):

- [macOS and Linux](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv.html)
- [Windows (Git Bash)](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv.html)
- [Windows (PowerShell)](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv.html)

*Terminal*

``` bash
docker run --rm -v "$(pwd):/workspace" docker-uv uv run hello.py
```

*Terminal*

``` bash
docker run --rm -v "/$(pwd):/workspace" docker-uv uv run hello.py
```

``` powershell
docker run --rm -v "${PWD}:/workspace" docker-uv uv run hello.py
```

*Output*

``` out
  ______________________________
| Hello from Python in my image! |
  ==============================
                              \
                               \
                                 ^__^
                                 (oo)\_______
                                 (__)\       )\/\
                                     ||----w |
                                     ||     ||
```

**Why `/$(pwd)` in Git Bash?**

Git Bash turns command-line arguments that start with `/` into Windows paths, so `/workspace` could reach Docker as `C:/Program Files/Git/workspace`. Doubling the first slash, which `/$(pwd)` does, stops that (see “Known issues” in the [Git for Windows release notes](https://github.com/git-for-windows/build-extra/blob/main/ReleaseNotes.md#known-issues)).

### [30.5 Why the packages go in `/opt/venv`](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv.html#why-the-packages-go-in-optvenv)

Without a mount, `/workspace` holds the three files the `Dockerfile` copied:

*Terminal*

``` bash
docker run --rm docker-uv ls -a
```

*Output*

``` out
.
..
.python-version
pyproject.toml
uv.lock
```

With the project folder mounted, `/workspace` shows your computer’s folder instead, including the `.venv` folder that `uv run` created on your computer:

- [macOS and Linux](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv.html)
- [Windows (Git Bash)](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv.html)
- [Windows (PowerShell)](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv.html)

*Terminal*

``` bash
docker run --rm -v "$(pwd):/workspace" docker-uv ls -a
```

*Terminal*

``` bash
docker run --rm -v "/$(pwd):/workspace" docker-uv ls -a
```

``` powershell
docker run --rm -v "${PWD}:/workspace" docker-uv ls -a
```

*Output*

``` out
.
..
.gitignore
.python-version
.venv
Dockerfile
hello.py
pyproject.toml
uv.lock
```

A mount hides whatever the image had at that path. If the image kept its packages in `/workspace/.venv`, the mount would hide them. Worse, uv in the container would find your computer’s `.venv` instead, which holds a program for your computer’s operating system, not for Linux. On a Mac:

*Terminal*

``` bash
file .venv/bin/python3
```

*Output*

``` out
.venv/bin/python3: Mach-O 64-bit executable arm64
```

With the `ENV` line left out of the `Dockerfile`, running `uv run hello.py` with the mount printed these lines, among others:

*Output*

``` out
Removed virtual environment at: .venv
Creating virtual environment at: .venv
```

uv deleted your computer’s `.venv` and made a Linux one in its place, which no longer works on your computer. With `UV_PROJECT_ENVIRONMENT=/opt/venv`, the container leaves `.venv` alone and uses the environment that the image built:

- [macOS and Linux](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv.html)
- [Windows (Git Bash)](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv.html)
- [Windows (PowerShell)](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv.html)

*Terminal*

``` bash
docker run --rm -v "$(pwd):/workspace" docker-uv uv run python -c "import sys; print(sys.prefix)"
```

*Terminal*

``` bash
docker run --rm -v "/$(pwd):/workspace" docker-uv uv run python -c "import sys; print(sys.prefix)"
```

``` powershell
docker run --rm -v "${PWD}:/workspace" docker-uv uv run python -c "import sys; print(sys.prefix)"
```

*Output*

``` out
/opt/venv
```

### [30.6 Add a package](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv.html#add-a-package)

To add a package, use uv on your computer, as in [uv: projects](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/virtual-environments-python-uv-projects.html), then build the image again. For example, to add pandas:

*Terminal*

``` bash
uv add pandas
```

*Output*

``` out
Resolved 6 packages in 26ms
Installed 4 packages in 100ms
 + numpy==2.5.5
 + pandas==3.1.1
 + python-dateutil==4.0.0
 + tzdata==2026.6
```

Because of `add-bounds = "exact"`, `uv add` wrote pandas into `pyproject.toml` with its exact version:

``` toml
dependencies = [
    "cowsay==6.1",
    "pandas==3.1.1",
]
```

It also updated `uv.lock` with pandas and the packages pandas needs. Build the image again:

*Terminal*

``` bash
docker build --tag docker-uv .
```

Here are the steps from the output:

*Output*

``` out
[+] Building 16.5s (12/12) FINISHED                                            docker:desktop-linux
 => [stage-0 1/5] FROM docker.io/library/ubuntu:24.04@sha256:008173c23f95b170204355c12626cb5a  0.0s
 => CACHED [stage-0 2/5] COPY --from=ghcr.io/astral-sh/uv:0.13.7 /uv /uvx /usr/local/bin/      0.0s
 => CACHED [stage-0 3/5] WORKDIR /workspace                                                    0.0s
 => [stage-0 4/5] COPY pyproject.toml uv.lock .python-version ./                               0.0s
 => [stage-0 5/5] RUN uv sync --locked                                                         7.4s
```

Docker reused the layers with uv in them, and ran the `COPY` and `uv sync` steps again, because `pyproject.toml` and `uv.lock` changed. pandas is now in the image:

- [macOS and Linux](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv.html)
- [Windows (Git Bash)](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv.html)
- [Windows (PowerShell)](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv.html)

*Terminal*

``` bash
docker run --rm -v "$(pwd):/workspace" docker-uv uv run python -c "import pandas; print(pandas.__version__)"
```

*Terminal*

``` bash
docker run --rm -v "/$(pwd):/workspace" docker-uv uv run python -c "import pandas; print(pandas.__version__)"
```

``` powershell
docker run --rm -v "${PWD}:/workspace" docker-uv uv run python -c "import pandas; print(pandas.__version__)"
```

*Output*

``` out
3.1.1
```

Commit `pyproject.toml` and `uv.lock` together, so that the lockfile in your repository always matches `pyproject.toml`.

### [30.7 When `uv.lock` does not match `pyproject.toml`](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv.html#when-uv.lock-does-not-match-pyproject.toml)

If you edit `pyproject.toml` by hand, without `uv add` or `uv lock`, `uv.lock` no longer matches it. For example, typing the pandas line into `pyproject.toml` yourself gives the same `dependencies` as `uv add pandas` did, but leaves `uv.lock` without pandas:

``` toml
dependencies = [
    "cowsay==6.1",
    "pandas==3.1.1",
]
```

The build then stops at `uv sync --locked`:

*Terminal*

``` bash
docker build --tag docker-uv .
```

*Output*

``` out
[+] Building 5.2s (11/11) FINISHED                                             docker:desktop-linux
 => [internal] load build definition from Dockerfile                                           0.0s
 => => transferring dockerfile: 553B                                                           0.0s
 => [internal] load metadata for ghcr.io/astral-sh/uv:0.13.7                                   0.8s
 => [internal] load metadata for docker.io/library/ubuntu:24.04                                0.1s
 => [internal] load .dockerignore                                                              0.0s
 => => transferring context: 2B                                                                0.0s
 => FROM ghcr.io/astral-sh/uv:0.13.7@sha256:96f40d3904aad8d0bd010539001d36c8e2188b981e1334471  0.0s
 => => resolve ghcr.io/astral-sh/uv:0.13.7@sha256:96f40d3904aad8d0bd010539001d36c8e2188b981e1  0.0s
 => [stage-0 1/5] FROM docker.io/library/ubuntu:24.04@sha256:008173c23f95b170204355c12626cb5a  0.0s
 => => resolve docker.io/library/ubuntu:24.04@sha256:008173c23f95b170204355c12626cb5a965d779a  0.0s
 => [internal] load build context                                                              0.0s
 => => transferring context: 985B                                                              0.0s
 => CACHED [stage-0 2/5] COPY --from=ghcr.io/astral-sh/uv:0.13.7 /uv /uvx /usr/local/bin/      0.0s
 => CACHED [stage-0 3/5] WORKDIR /workspace                                                    0.0s
 => [stage-0 4/5] COPY pyproject.toml uv.lock .python-version ./                               0.0s
 => ERROR [stage-0 5/5] RUN uv sync --locked                                                   4.3s
------
 > [stage-0 5/5] RUN uv sync --locked:
0.287 Downloading cpython-3.14.10-linux-aarch64-gnu (download) (29.2MiB)
3.631  Downloaded cpython-3.14.10-linux-aarch64-gnu (download)
3.817 Using CPython 3.14.10
3.817 Creating virtual environment at: /opt/venv
4.141 Resolved 6 packages in 319ms
4.143 error: The lockfile at `uv.lock` needs to be updated, but `--locked` was provided.
4.143
4.143 hint: To update the lockfile, run `uv lock`.
------
Dockerfile:15
--------------------
  13 |     COPY pyproject.toml uv.lock .python-version ./
  14 |     # --locked: stop if uv.lock doesn't match pyproject.toml
  15 | >>> RUN uv sync --locked
  16 |
--------------------
ERROR: failed to build: failed to solve: process "/bin/sh -c uv sync --locked" did not complete successfully: exit code: 1
What's next:
    Debug this build failure with Gordon → docker ai "help me fix this build failure"
```

This is what `--locked` is for. Without it, `uv sync` would quietly update `uv.lock` inside the image, and the image would no longer match the `uv.lock` in your repository. With it, a forgotten `uv lock` stops the build, and the error says how to fix it:

*Terminal*

``` bash
uv lock
```

*Output*

``` out
Using CPython 3.14.3
Resolved 6 packages in 49ms
Added numpy v2.5.5
Added pandas v3.1.1
Added python-dateutil v4.0.0
Added tzdata v2026.6
```

After `uv lock`, `docker build --tag docker-uv .` finishes, and `pyproject.toml` and `uv.lock` are ready to commit together.

## [32 Python and R in one image](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv-renv.html)

### [Learning Objectives](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv-renv.html#learning-objectives)

1.  Combine the uv and renv parts of a `Dockerfile` into one image that has Python and R
2.  Install software that is not a Python or R package, such as Quarto, in an image
3.  Run Python, R and Quarto in one container to render reports in both languages

### [Download the images before you start](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv-renv.html#download-the-images-before-you-start)

The image in this chapter builds on the two images from [Python packages with uv in an image](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv.html) and [R packages with renv in an image](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-renv.html). Start Docker first (on macOS and Windows, open Docker Desktop), then download (pull) them before you start:

*Terminal*

``` bash
docker pull rocker/r-ver:4.6.2
docker pull ghcr.io/astral-sh/uv:0.13.7
```

### [32.1 The example project](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv-renv.html#the-example-project)

Many data analyses use Python and R together, for example a Python script that cleans the data and an R script that fits a model. This chapter builds one image with both, from [docker-uv-renv](https://github.com/chendaniely/docker-uv-renv), the example project that the rest of this part of the book uses. Get a copy of it with Git:

*Terminal*

``` bash
git clone https://github.com/chendaniely/docker-uv-renv.git
cd docker-uv-renv
```

Its Python packages are listed in `pyproject.toml` and locked in `uv.lock`, as in the uv chapter:

``` toml
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
]

[tool.uv]
# `uv add` writes an exact version (==)
add-bounds = "exact"
```

Its R packages are listed in `DESCRIPTION` and locked in `renv.lock`, as in the renv chapter:

``` yaml
Type: project
Version: 2026.11.13
Description: The R packages this project uses. renv.lock locks them.
Depends:
    dplyr (== 1.2.1),
    ggplot2 (== 4.0.3),
    knitr (== 1.52),
    rmarkdown (== 2.32)
```

Its `reports/` folder has two Quarto reports that make the same table and chart, `report-python.qmd` with pandas and Altair, and `report-r.qmd` with dplyr and ggplot2.

### [32.2 The `Dockerfile`](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv-renv.html#the-dockerfile)

Here is the project’s whole `Dockerfile`:

``` dockerfile
# Ubuntu with R. Other versions:
# https://rocker-project.org/images/versioned/r-ver.html
FROM rocker/r-ver:4.6.2

# libuv1-dev: the fs R package needs it (see renv::sysreqs())
RUN apt-get update && apt-get install --yes \
    curl \
    git \
    less \
    libuv1-dev \
    make \
    nano \
    openssh-server

# install quarto
# quarto comes with Typst for PDFs, so no LaTeX.
# dpkg --print-architecture: amd64 or arm64, to match your computer.
RUN curl --location --output quarto.deb \
    https://github.com/quarto-dev/quarto-cli/releases/download/v1.11.9/quarto-1.11.9-linux-$(dpkg --print-architecture).deb \
  && apt-get install --yes ./quarto.deb \
  && rm quarto.deb

# install python uv
# https://docs.astral.sh/uv/guides/integration/docker/#installing-uv
COPY --from=ghcr.io/astral-sh/uv:0.13.7 /uv /uvx /usr/local/bin/

# The project is mounted over /workspace, so the packages go in /opt
WORKDIR /workspace

# python packages in /opt/venv
ENV UV_PROJECT_ENVIRONMENT=/opt/venv
# ssh logins don't see ENV, only /etc/environment
RUN echo "UV_PROJECT_ENVIRONMENT=$UV_PROJECT_ENVIRONMENT" >> /etc/environment
COPY pyproject.toml uv.lock .python-version ./
# --locked: stop if uv.lock doesn't match pyproject.toml
RUN uv sync --locked

# R packages in /opt/renv/library
RUN echo "RENV_PATHS_LIBRARY=/opt/renv/library" >> /usr/local/lib/R/etc/Renviron.site
COPY renv.lock .Rprofile ./
COPY renv/activate.R renv/
RUN Rscript -e "renv::restore()"

# For linux laptops:
# StrictModes no: sshd wants root to own the key file,
# but on Linux the mounted one is yours
# RUN echo "StrictModes no" > /etc/ssh/sshd_config.d/container.conf

# -D: stay in the foreground, so the container keeps running
CMD ["/usr/sbin/sshd", "-D"]
```

Most of it comes from the two previous chapters. It starts from the R image, because `rocker/r-ver` has no Python:

*Terminal*

``` bash
docker run --rm rocker/r-ver:4.6.2 bash -c 'command -v python3 || echo "no python3"'
```

*Output*

``` out
no python3
```

That does not matter, because uv installs the Python version in `.python-version`, as it did on top of Ubuntu. So the uv lines can be added to the R image unchanged:

- `FROM rocker/r-ver:4.6.2`, the `RENV_PATHS_LIBRARY` line, the two `COPY` lines for renv and `renv::restore()` are the lines from [R packages with renv in an image](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-renv.html).
- `COPY --from=ghcr.io/astral-sh/uv:0.13.7`, `ENV UV_PROJECT_ENVIRONMENT=/opt/venv`, the `COPY` line for uv and `uv sync --locked` are the lines from [Python packages with uv in an image](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv.html).
- `WORKDIR /workspace` is in both.

The rest is new:

- The `apt-get` line installs `curl` and `libuv1-dev`, as in the renv chapter. This project needs `libuv1-dev` because rmarkdown needs fs, through the packages bslib and sass. `git`, `less` and `nano` let you use Git, read files and edit files inside the container, `make` runs a `Makefile` (see [Data analysis pipelines with GNU Make](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/pipelines-make.html)), and `openssh-server` lets you log in to the container over ssh.
- The Quarto `RUN` line downloads Quarto 1.11.9 for your computer’s processor, installs it, and deletes the download. `$(dpkg --print-architecture)` runs `dpkg --print-architecture` and puts what it prints, `amd64` or `arm64`, into the download address. Deleting the download in the same `RUN` line keeps it out of the image’s layers (see [Building images](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html)). Quarto makes PDFs with [Typst](https://quarto.org/docs/output-formats/typst.html), which comes with it, so the image does not need LaTeX.
- The line that adds `UV_PROJECT_ENVIRONMENT` to `/etc/environment` is for ssh. `ENV` applies to the commands Docker starts in a container, but a session that logs in over ssh reads `/etc/environment` instead.
- `CMD ["/usr/sbin/sshd", "-D"]` makes a container run an ssh server when it starts, and `-D` keeps the server in the foreground, so the container keeps running. As in the earlier chapters, a command after the image name in `docker run` replaces it. [Docker Compose](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-docker-compose.html) starts this server, and a later chapter logs in to it.
- The commented-out `StrictModes no` line is for Linux computers, where the ssh server refuses a key file that the mount makes yours, not `root`’s.

The order follows [Building images](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html). The steps that rarely change, such as installing software, come first, and the files that list packages are copied last, so that adding a package rebuilds only the steps after its `COPY`.

**Exercise**

**Demonstration of container images being built from layers**

Let’s follow the images that the docker-uv-renv image is built on:

- [docker-uv-renv’s Dockerfile](https://github.com/chendaniely/docker-uv-renv/blob/main/Dockerfile)
- [rocker/r-ver:4.6.2’s Dockerfile](https://github.com/rocker-org/rocker-versioned2/blob/master/dockerfiles/r-ver_4.6.2.Dockerfile)
- [The Ubuntu image on Docker Hub](https://hub.docker.com/_/ubuntu)

Questions:

1.  What image does it build off?
2.  What image does that build off?
3.  And then the next one?

### [32.3 Build the image](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv-renv.html#build-the-image)

From the project folder:

*Terminal*

``` bash
docker build --tag docker-uv-renv .
```

On a computer that has not built the image before, every step runs. To show that here, the build below added `--no-cache`, which runs every step again instead of reusing its layer. The `FROM` steps still say `CACHED`, because `--no-cache` does not download the base images again:

*Terminal*

``` bash
docker build --no-cache --tag docker-uv-renv .
```

*Output*

``` out
[+] Building 143.8s (19/19) FINISHED                                           docker:desktop-linux
 => [internal] load build definition from Dockerfile                                           0.0s
 => => transferring dockerfile: 1.77kB                                                         0.0s
 => [internal] load metadata for docker.io/rocker/r-ver:4.6.2                                  0.1s
 => [internal] load metadata for ghcr.io/astral-sh/uv:0.13.7                                   0.9s
 => [internal] load .dockerignore                                                              0.0s
 => => transferring context: 2B                                                                0.0s
 => CACHED [stage-0  1/12] FROM docker.io/rocker/r-ver:4.6.2@sha256:8739c76d2d9316698a7145b03  0.0s
 => => resolve docker.io/rocker/r-ver:4.6.2@sha256:8739c76d2d9316698a7145b032601f1e82249fdee3  0.0s
 => CACHED FROM ghcr.io/astral-sh/uv:0.13.7@sha256:96f40d3904aad8d0bd010539001d36c8e2188b981e  0.0s
 => => resolve ghcr.io/astral-sh/uv:0.13.7@sha256:96f40d3904aad8d0bd010539001d36c8e2188b981e1  0.0s
 => [internal] load build context                                                              0.0s
 => => transferring context: 320.25kB                                                          0.0s
 => [stage-0  2/12] RUN apt-get update && apt-get install --yes     curl     git     less     22.1s
 => [stage-0  3/12] RUN curl --location --output quarto.deb     https://github.com/quarto-de  24.4s
 => [stage-0  4/12] COPY --from=ghcr.io/astral-sh/uv:0.13.7 /uv /uvx /usr/local/bin/           0.2s
 => [stage-0  5/12] WORKDIR /workspace                                                         0.0s
 => [stage-0  6/12] RUN echo "UV_PROJECT_ENVIRONMENT=/opt/venv" >> /etc/environment            0.1s
 => [stage-0  7/12] COPY pyproject.toml uv.lock .python-version ./                             0.0s
 => [stage-0  8/12] RUN uv sync --locked                                                      15.4s
 => [stage-0  9/12] RUN echo "RENV_PATHS_LIBRARY=/opt/renv/library" >> /usr/local/lib/R/etc/R  0.4s
 => [stage-0 10/12] COPY renv.lock .Rprofile ./                                                0.1s
 => [stage-0 11/12] COPY renv/activate.R renv/                                                 0.0s
 => [stage-0 12/12] RUN Rscript -e "renv::restore()"                                          53.4s
 => exporting to image                                                                        26.4s
 => => exporting layers                                                                       14.5s
 => => exporting manifest sha256:0f8447d08dc66aa1be883ab5e8bbf3ba35b66f630bc48f254d4258b54a89  0.0s
 => => exporting config sha256:c8db613a6eef3b72df13c615e421cf573d7b4547a158605a1aee8ff8f30688  0.0s
 => => exporting attestation manifest sha256:599b12f91bf84cb1b7ecf5f05593f5f1e9b13af508ca5101  0.0s
 => => exporting manifest list sha256:80dad0100177d131842bfcbe5d8e751c6f0b4ca58044338a5cf61fe  0.0s
 => => naming to docker.io/library/docker-uv-renv:latest                                       0.0s
 => => unpacking to docker.io/library/docker-uv-renv:latest                                   11.8s
```

The build took a little over two minutes. `renv::restore()` took longest, then installing Quarto and the `apt-get` packages. After this, a change to `pyproject.toml` or `renv.lock` reruns only the steps from its `COPY` down. The image is about 3 GB:

*Terminal*

``` bash
docker image ls docker-uv-renv
```

*Output*

``` out
IMAGE                   ID             DISK USAGE   CONTENT SIZE   EXTRA
docker-uv-renv:latest   80dad0100177       2.98GB          794MB        
```

### [32.4 Use Python and R in one container](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv-renv.html#use-python-and-r-in-one-container)

With the project folder mounted at `/workspace`, the same container runs Python with uv:

- [macOS and Linux](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv-renv.html)
- [Windows (Git Bash)](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv-renv.html)
- [Windows (PowerShell)](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv-renv.html)

*Terminal*

``` bash
docker run --rm -v "$(pwd):/workspace" docker-uv-renv uv run python --version
```

*Terminal*

``` bash
docker run --rm -v "/$(pwd):/workspace" docker-uv-renv uv run python --version
```

``` powershell
docker run --rm -v "${PWD}:/workspace" docker-uv-renv uv run python --version
```

*Output*

``` out
Python 3.14.4
```

and R:

- [macOS and Linux](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv-renv.html)
- [Windows (Git Bash)](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv-renv.html)
- [Windows (PowerShell)](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv-renv.html)

*Terminal*

``` bash
docker run --rm -v "$(pwd):/workspace" docker-uv-renv Rscript -e 'R.version.string'
```

*Terminal*

``` bash
docker run --rm -v "/$(pwd):/workspace" docker-uv-renv Rscript -e 'R.version.string'
```

``` powershell
docker run --rm -v "${PWD}:/workspace" docker-uv-renv Rscript -e 'R.version.string'
```

*Output*

``` out
[1] "R version 4.6.2 (2026-10-29)"
```

### [32.5 Render reports in both languages](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv-renv.html#render-reports-in-both-languages)

`uv run quarto render` renders both reports. `uv run` starts Quarto with the project’s Python environment in `/opt/venv`, so Quarto runs the Python code with the packages from `uv.lock`, including `ipykernel` and `nbclient`, which Quarto needs to run Python code. R finds the packages from `renv.lock` in `/opt/renv/library`, because of the `RENV_PATHS_LIBRARY` line:

- [macOS and Linux](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv-renv.html)
- [Windows (Git Bash)](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv-renv.html)
- [Windows (PowerShell)](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv-renv.html)

*Terminal*

``` bash
docker run --rm -v "$(pwd):/workspace" docker-uv-renv uv run quarto render
```

*Terminal*

``` bash
docker run --rm -v "/$(pwd):/workspace" docker-uv-renv uv run quarto render
```

``` powershell
docker run --rm -v "${PWD}:/workspace" docker-uv-renv uv run quarto render
```

Here are the main lines of the output, without the progress counters:

*Output*

``` out
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

Quarto rendered each report twice, once as HTML and once as a PDF with Typst, because the project’s `_quarto.yml` lists both formats. The warning about TCP comes from the Python kernel that Quarto starts, which talks to Quarto over a network connection inside the container. Nothing leaves the container, so it does not matter here.

The reports are written to the mounted folder, so they are in `reports/` on your computer:

*Terminal*

``` bash
ls reports
```

*Output*

``` out
report-python.html
report-python.pdf
report-python.qmd
report-r.html
report-r.pdf
report-r.qmd
```

[Docker Compose](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-docker-compose.html) shortens these `docker run` commands.

## [33 Containers: Docker Compose](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-docker-compose.html)

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

## [34 Working in a container over ssh with Positron](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-ssh-positron.html)

### [Learning Objectives](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-ssh-positron.html#learning-objectives)

1.  Explain how Positron works inside a running container over ssh
2.  Fix a missing ssh key and a changed host key

### [34.1 How it works](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-ssh-positron.html#how-it-works)

With the docker-uv-renv container running, you can work inside it from Positron, as if it were a remote Linux computer. Positron’s [Remote SSH](https://positron.posit.co/remote-ssh.html) documentation has the steps. Here is how the pieces from the earlier chapters fit together:

- The image runs an ssh server when a container starts, because of its `CMD ["/usr/sbin/sshd", "-D"]` (see [Python and R in one image](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv-renv.html)).
- `docker compose up --detach` starts the container in the background. Docker Compose maps port 2222 on your computer to the container’s port 22, and mounts your ssh public key as the key that may log in as `root` (see [Docker Compose](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-docker-compose.html), including how to make a key).
- In Positron, run “Remote SSH: Show Remote Menu” from the Command Palette, pick “Connect to Host”, and type `root@localhost:2222`. The first time, Positron installs its server inside the container, which takes a minute.
- Open the folder `/workspace`, which is your project folder. Positron’s terminals, and its Python and R sessions, now run in the container.
- For Python, pick the interpreter `/opt/venv/bin/python`, the environment the image built from `uv.lock`. R uses the packages in `/opt/renv/library` without any setup, because of the `RENV_PATHS_LIBRARY` line in R’s `Renviron.site`.
- An ssh login does not see the image’s `ENV` settings, only the ones in `/etc/environment`. That is why the `Dockerfile` also writes `UV_PROJECT_ENVIRONMENT` there, so that `uv` in a Positron terminal uses `/opt/venv` too.

### [34.2 When it does not connect](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-ssh-positron.html#when-it-does-not-connect)

These are the problems the docker-uv-renv README lists, and their fixes:

- `~/.ssh/id_ed25519.pub` is a folder. Docker made it because the key did not exist when the container started. Run `docker compose down`, delete the folder, make the key, and run `docker compose up --detach` again.

- Your key has a different name. Change the key’s path in `docker-compose.yml`.

- Positron or `ssh` says the remote host identification has changed. The container’s ssh server has its own keys, which the image made when `apt-get` installed `openssh-server`. Rebuilding that step makes new ones, so your computer no longer recognizes the container. Forget the old key, then connect again:

  *Terminal*

  ``` bash
  ssh-keygen -R "[localhost]:2222"
  ```

- On a Linux computer, the ssh server refuses the mounted key, because the file belongs to you, not to `root`. Uncomment the `StrictModes no` line in the `Dockerfile` and run `docker compose build`.

### [34.3 An optional ssh shortcut](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-ssh-positron.html#an-optional-ssh-shortcut)

To type `ssh docker-uv-renv` instead of `ssh -p 2222 root@localhost`, and to pick `docker-uv-renv` from a list in Positron, add this to `~/.ssh/config` on your computer:

    Host docker-uv-renv
      HostName localhost
      Port 2222
      User root
      StrictHostKeyChecking no
      UserKnownHostsFile /dev/null

The last two lines skip the host key check, so that a rebuilt image does not cause the host key error above.

## [35 Building images for several platforms](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-platforms.html)

### [Learning Objectives](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-platforms.html#learning-objectives)

1.  Explain why an image is built for one kind of processor
2.  Build an image for Intel/AMD and ARM computers on your own computer, and push both to Docker Hub
3.  Describe how a GitHub Actions workflow builds a project’s image

### [35.1 One image, one kind of processor](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-platforms.html#one-image-one-kind-of-processor)

An image holds programs compiled for one kind of processor. Macs with Apple silicon, and some Windows laptops, have ARM processors (`arm64`). Most other laptops, and GitHub’s usual Linux computers, have Intel or AMD processors (`amd64`). `docker build` builds for the computer it runs on, so the `hello-cowsay` image from [Building images](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html), built on a Mac with Apple silicon, is for `arm64` only:

*Terminal*

``` bash
docker image inspect hello-cowsay --format '{{.Os}}/{{.Architecture}}'
```

*Output*

``` out
linux/arm64
```

A classmate with an Intel laptop could not use it as it is, just as an ARM computer cannot pull the older `rocker/tidyverse` images (see the warning in [Building images](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html)).

### [35.2 Build for both kinds on your computer](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-platforms.html#build-for-both-kinds-on-your-computer)

`--platform` builds the image for each platform you list. Here are the steps of building `hello-cowsay` for both:

*Terminal*

``` bash
docker build --platform linux/amd64,linux/arm64 --tag hello-cowsay .
```

*Output*

``` out
[+] Building 65.7s (9/9) FINISHED                                              docker:desktop-linux
 => [linux/arm64 internal] load metadata for docker.io/rocker/r-ver:4.6.2                      0.1s
 => [linux/amd64 internal] load metadata for docker.io/rocker/r-ver:4.6.2                      1.4s
 => [linux/amd64 1/2] FROM docker.io/rocker/r-ver:4.6.2@sha256:8739c76d2d9316698a7145b032601  51.0s
 => [linux/arm64 1/2] FROM docker.io/rocker/r-ver:4.6.2@sha256:8739c76d2d9316698a7145b032601f  0.0s
 => CACHED [linux/arm64 2/2] RUN Rscript -e "install.packages('cowsay')"                       0.0s
 => [linux/amd64 2/2] RUN Rscript -e "install.packages('cowsay')"                             12.7s
```

The `arm64` steps were already cached. For `amd64`, Docker downloaded the `amd64` version of `rocker/r-ver:4.6.2`, and ran the `RUN` step by emulating an Intel processor, which is slower than running it on one. `docker image ls --tree` shows that the one tag now has both:

*Terminal*

``` bash
docker image ls --tree hello-cowsay
```

*Output*

``` out
IMAGE                 ID             DISK USAGE   CONTENT SIZE   EXTRA
hello-cowsay:latest   fcb420e64e33       1.86GB          800MB        
├─ linux/amd64        7f260b562e1c        410MB          410MB        
└─ linux/arm64        f2d1c5ab15c8       1.45GB          390MB        
```

`--platform` on `docker run` picks which one to run, and `uname -m` prints the processor the container sees:

*Terminal*

``` bash
docker run --rm --platform linux/amd64 hello-cowsay uname -m
docker run --rm --platform linux/arm64 hello-cowsay uname -m
```

*Output*

``` out
x86_64
aarch64
```

Docker’s guide to [multi-platform builds](https://docs.docker.com/build/building/multi-platform/) has the details, including what your Docker needs to build them.

### [35.3 Push both to Docker Hub](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-platforms.html#push-both-to-docker-hub)

To share the image, push it to a container registry such as [Docker Hub](https://hub.docker.com/), where you need a free account. The image’s name must start with your Docker Hub username, so replace `USERNAME` below with yours:

*Terminal*

``` bash
docker login
docker tag hello-cowsay USERNAME/hello-cowsay:0.1
docker push USERNAME/hello-cowsay:0.1
```

- `docker login` signs you in to Docker Hub.
- `docker tag` gives the image a second name, with your username and a version, `0.1`.
- `docker push` uploads it. Because the image has both platforms, it uploads both, under the one tag.

Anyone can then run `docker pull USERNAME/hello-cowsay:0.1`, and Docker downloads the version for their computer. To list the platforms an image in a registry has:

*Terminal*

``` bash
docker buildx imagetools inspect USERNAME/hello-cowsay:0.1
```

### [35.4 On GitHub Actions](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-platforms.html#on-github-actions)

A project can also build its image on GitHub’s computers, every time you push. [docker-uv-renv](https://github.com/chendaniely/docker-uv-renv) does this with [`build-and-render.yml`](https://github.com/chendaniely/docker-uv-renv/blob/main/.github/workflows/build-and-render.yml):

``` yaml
name: Build image and render reports

on:
  push:
    branches:
      - main
  pull_request:
  workflow_dispatch:

jobs:
  build-and-render:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v7

      - name: Build the image
        run: docker build --tag docker-uv-renv .

      # not `make render`: CI has no ssh key to mount
      - name: Render the reports
        run: docker run --rm --volume "$PWD:/workspace" docker-uv-renv uv run quarto render

      # download them from the run's Summary page
      - uses: actions/upload-artifact@v7
        with:
          name: reports
          path: |
            reports/*.html
            reports/*.pdf
```

On every push to `main` and every pull request, a fresh Linux computer (`ubuntu-latest`, an `amd64` computer) builds the image from the `Dockerfile` in the repository, renders the reports in a container, and keeps them for you to download from the run’s page, as in [this run](https://github.com/chendaniely/docker-uv-renv/actions/runs/43520328267). Because the build starts from nothing, it shows that the `Dockerfile` and lockfiles work on a computer other than yours. GitHub also has ARM computers (`ubuntu-24.04-arm`), and the project’s [`check-platforms.yml`](https://github.com/chendaniely/docker-uv-renv/blob/main/.github/workflows/check-platforms.yml) builds the image on both. [GitHub Actions](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/github-actions.html) explains how workflow files work.
