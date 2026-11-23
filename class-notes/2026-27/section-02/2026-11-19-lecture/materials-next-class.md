# Not reached in class: 2026-11-19 lecture (next class)

Sections of this lecture's readings the class ran out of time for, as published on
2026-11-19, each heading linked to its published section. The instructor plans to cover them
next class, whose `materials.md` starts from this file. No script sends this file to a
model: a model given readings the class didn't reach can teach them as class content.

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
