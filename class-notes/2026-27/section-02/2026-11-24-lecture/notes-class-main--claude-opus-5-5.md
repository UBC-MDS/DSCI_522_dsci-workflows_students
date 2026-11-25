# Building a Python analysis image with uv, volume mounts and Docker Compose

Date: 2026-11-24

Instructor: Daniel Chen

## Summary

This session began with a short review exercise. Students created a GitHub repository whose `Dockerfile` builds from the `rocker/r-ver:4.6.2` image. The instructor had Claude Code do the same task live. He used the result to show that a coding agent only works well when you already know the vocabulary (Dockerfile, image, tag) to put in the prompt. He then reviewed building with `docker build --tag <name> .` and running with `docker run --rm -it`, including what the trailing `.` means and how a command after the image name, such as `bash`, replaces the image's default `CMD`.

Most of the lecture rebuilt the image for a Python project managed with `uv`. The new image starts from `ubuntu:24.04` and copies the `uv` binaries in with `COPY --from`. It sets `WORKDIR /workspace`, copies `pyproject.toml`, `uv.lock` and `.python-version`, and installs the packages with `RUN uv sync --locked`. Along the way the instructor covered exact version pins in `pyproject.toml` (`==` rather than `>=`, and `add-bounds = "exact"`) and why `.python-version` matters. He also showed how layer caching rewards putting slow, rarely changing steps at the top of a `Dockerfile`.

The instructor then dealt with two practical problems. Copying code into the image freezes a snapshot of work that is still changing, so the class mounted the project folder at run time with `-v "$(pwd):/workspace"`. The mount brought the laptop's macOS `.venv` into the Linux container, so the image now keeps its environment at `/opt/venv` through `ENV UV_PROJECT_ENVIRONMENT=/opt/venv`. Finally, the instructor introduced `docker-compose.yml` as a version-controlled replacement for long `docker run` commands. The live `docker compose up` demo did not keep a container running, and he will fix it next class.

For the milestone this week, each group writes a `Dockerfile` that reproduces its analysis's compute environment. The TAs will build the image from the repository, mount the project, and run `uv run quarto render` inside the container.

## Key takeaways

- `docker build --tag <name> .` needs the trailing `.`: it tells Docker where to find the `Dockerfile` and the files to build from.
- A command after the image name in `docker run`, such as `bash`, replaces the image's default `CMD`, and `--rm` throws away every change you made in the container when you exit.
- For a `uv` project, the image copies in `uv` and installs packages from `pyproject.toml`, `uv.lock` and `.python-version` with `RUN uv sync --locked`, which stops the build if the lockfile and `pyproject.toml` disagree.
- Pin the packages your analysis depends on with `==` (and set `add-bounds = "exact"`), because a `>=` bound can pull in a new major version that breaks your code.
- Put slow, rarely changing steps near the top of a `Dockerfile` and fast-changing ones near the bottom, because changing a step reruns it and everything below it.
- Keep code out of the image and mount it at run time with `-v "$(pwd):/workspace"`, and set `UV_PROJECT_ENVIRONMENT=/opt/venv` so the mount's laptop `.venv` does not replace the image's Linux environment.
- A `docker-compose.yml` records the build and run options (image, ports, volumes) in a file you can version control, in place of a long `docker run` command.

## Knowledge Points

### 1. Warm-up exercise: a Dockerfile from a given image

*00:00:00–00:04:30*

- **The task**: create a new GitHub repository containing a `Dockerfile` that builds from a specific image, as review of the previous class.
- **The solution**: essentially one line in one file. The demo repository's first commit is:

  ```dockerfile
  FROM rocker/r-ver:4.6.2

  CMD ["R"]
  ```

- **Purpose**: the exercise was a way to set up the rest of the class, which builds on this repository.
- **Agent comparison**: while students worked, the instructor gave the same task to Claude Code to see what it would produce. The result is the [demo repository](https://github.com/chendaniely/2026-11-24-docker).

### 2. Course website updates and a Docker Desktop reminder

*00:04:30–00:07:21*

- **New look for the course site**: the other instructor's material has been folded into the student repo. Her slide decks are linked there, and the summary lecture notes now live on the course site, so you no longer need to dig through the GitHub student repo for them.
- **Notes from several language models**: the summaries are produced by different models, and you can compare them. Transcripts and links stay on the private side.
- **Question-and-answer breakdowns**: each lecture is also broken into questions at different levels of Bloom's taxonomy. Some are factual recall, and some need you to understand what happens under the hood. They are optional, and you could use them as a template for notes in other courses.
- **Command history page**: if all you want is the commands that were run, that page has them.
- **Start Docker Desktop first**: on Mac and Windows, Docker commands fail unless Docker Desktop is running. Recent versions usually tell you so, but check this first when a Docker command refuses to run.

### 3. Letting Claude Code build the repository

*00:07:21–00:11:24*

- **The prompt mattered**: the instructor asked for a repository named `2026-11-24-docker` with a `Dockerfile` built from the given image. He used the precise words (Dockerfile, image, the image name). Someone who had never heard of Docker could not have steered the agent toward the right answer, which is why learning the tooling vocabulary matters.
- **What the agent ran**: you can watch the shell commands it runs. It ran `ls`, checked that `docker` and `gh` exist, ran a Docker command to learn what machine it was on, ran `mkdir` to make the folder, and wrote a `Dockerfile` starting `FROM rocker/...`. It then built the image and ran a script in the container to test it.
- **It made choices of its own**: it created the folder under `~/temp` instead of `~/git`, probably because Claude was started in a different folder. Because of the instructor's usual defaults, it also wrote a `README.md` and a `Makefile` he hadn't asked for in this prompt. Templates and defaults like these are a benefit of using an agent once you have patterns you like.
- **Cost**: the run cost about fifty cents.

### 4. The default command: `CMD ["R"]` ([29.2.1 `CMD` or `ENTRYPOINT`?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#cmd-or-entrypoint))

*00:11:24–00:12:41*

- **Only `FROM` was required**, but Claude added `CMD ["R"]` on its own, reasoning that someone using an R image probably wants to do R things.
- **What `CMD` does**: it is the command a container runs when you start it without giving it any other command. Here, R starts.
- **Analogy**: if the image were a file and you double-clicked it, `CMD` decides what opens.
- **It can be overridden**: you can always pass another command when you run the container, as the next themes show.

### 5. Listing and building images ([27.7 Image vs container?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#image-vs-container))

*00:12:42–00:16:40*

- **`docker images`** lists the images on your computer. Claude had already built `2026-11-24-docker:latest`. `latest` is the tag Docker uses when you don't give one.
- **Building by hand**: `docker build --tag 2026-11-24-docker .`. The `--tag` (`-t`) value is any name you like, even `pizza`. Reusing an existing name rebuilds and replaces that image.
- **The trailing `.`**: `docker build` looks for a file named `Dockerfile` (capital D) by default, but you still have to tell it where to look. The `.` means "here", in the current directory. This is the `.` from the first week of 521. Think of it as a function argument that has no default, so you must pass it.
- **Base images are pulled once**: the rebuild finished almost instantly because `rocker/r-ver:4.6.2` was already downloaded from last class. A base image you don't have yet makes that `FROM` step take seconds or minutes, depending on your connection. You need some version of this image for this week's milestone.

> [!WARNING]
>
> Don't forget the `.` at the end of `docker build --tag <name> .`. It is not a full stop; it tells Docker where the `Dockerfile` is.

### 6. Running a container, overriding `CMD`, and throwaway containers ([28.2 Docker command-line commands](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#docker-command-line-commands))

*00:16:40–00:20:07*

- **`docker run --rm -it <image>`**:
  - `--rm` deletes the container when you exit, so it isn't left running on your computer.
  - `-it` gives you terminal access and passes what you type through to the container.
  - The image name says which machine to start. Here it started R because of `CMD ["R"]`.
- **Overriding the default**: `docker run --rm -it 2026-11-24-docker bash` replaces `R` with `bash`. You get a normal shell, like Git Bash or the macOS terminal, with full access to that Linux machine.
- **You start at the root of the file system**: `pwd` printed `/`, and `ls` showed system folders (`bin`, `etc`, `opt`, `usr`, …). `/home` was empty because the image has no user. For this course everyone uses the container as a shared analysis setup, not a service for the public, so ownership and users don't matter much.
- **Changes don't survive**: with `--rm`, everything you changed inside the container is gone after you exit. That makes containers a safe place to try risky things, such as installing PyTorch. If it goes wrong, restart the container and nothing bad has happened. The instructor compared it to a version of Git that automatically resets all your changes.

### 7. Choosing a base image for a Python project ([29.3 Choosing a base image for your Dockerfile](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#choosing-a-base-image-for-your-dockerfile))

*00:20:07–00:24:22*

- **The goal**: an image that already has the whole project environment installed. Anyone who pulls it can run your analysis without setting anything up, apart from the larger download.
- **Everyone in the class is on a Python project**, so the demo swapped the R base image for a Python setup that uses `uv`. The textbook's example image ([Python and R in one image](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv-renv.html), repository [docker-uv-renv](https://github.com/chendaniely/docker-uv-renv)) has both R and Python. Mixing languages in one project is common and valid, for example to use ggplot2 for plots.
- **Containers run Linux**: even on a Mac or Windows laptop, inside a container you are in the Linux world, most likely some version of Ubuntu. The new `Dockerfile` starts `FROM ubuntu:24.04`.
- **Why not the R image**: it carries a lot of R software you don't need. Keep images small out of respect for other people's disk space, which has become expensive. Smaller bases such as Alpine exist but may mean installing more yourself. Ubuntu is a good starting point.

### 8. Installing `uv` with `COPY --from`, and setting `WORKDIR` ([30.2 A `Dockerfile` for a uv project](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv.html#a-dockerfile-for-a-uv-project))

*00:24:22–00:27:42*

- **`COPY` from another image**: `COPY --from=ghcr.io/astral-sh/uv:0.13.7 /uv /uvx /usr/local/bin/` copies the `uv` and `uvx` programs out of uv's published image into the container's `/usr/local/bin/`.
  - Read the image name like a GitHub path: registry/owner, repository, then the version tag.
  - This line comes straight from [uv's Docker guide](https://docs.astral.sh/uv/guides/integration/docker/#installing-uv) and the textbook.
- **Why install `uv` at all**: you are building a machine from scratch. Everyone installed `uv` at orientation, so the "copy of my machine" you hand out has to have it too.
- **`WORKDIR /workspace`**: changes the container's working directory. When it starts, you land in a project folder instead of `/`, where moving the wrong system folder could break everything. The folder is created if it doesn't exist.
- **Working directories never go away**: from 521 onward, every tool needs to know its starting point, whether it is called `pwd`, `cd` or `WORKDIR`.

### 9. Setting up the `uv` project locally ([30.1 The project](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv.html#the-project))

*00:27:42–00:29:58*

- **What `uv` needs**: a `pyproject.toml`. `uv sync` creates `uv.lock`, and the lockfile is what installs the packages.
- **`uv init --bare`** created the `pyproject.toml`, with a name, a version (your milestone numbering doesn't matter much) and `requires-python = ">=3.14"`.
- **Adding a dependency**: you can type it into `dependencies` by hand, or run `uv add cowsay`. Here it installed `cowsay==6.1` and wrote `cowsay>=6.1` into `pyproject.toml`.
- **The image only gets this far on its own**: `uv` is now installed in the image. What remains is getting the project's packages installed in the container, and that still has to work on your own machine first.

### 10. Pinning exact versions in `pyproject.toml` ([22 uv: pinning exact versions](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/virtual-environments-python-uv-exact-pins.html))

*00:29:58–00:33:35*

- **The `>=` problem**: `cowsay>=6.1` allows any newer version. If cowsay 7.0 comes out next week and you rebuild the lockfile and image next week, you get 7.0.
- **Major versions break things**: a change in the first number usually means a backwards-incompatible change (more in 524). Something you rely on in 6.x may not work in 7.x.
- **Pin with `==`**: write `cowsay==6.1`. Make `uv add` do this from now on with a `[tool.uv]` table in `pyproject.toml` (see [22.3 Making `uv add` write exact versions](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/virtual-environments-python-uv-exact-pins.html#making-uv-add-write-exact-versions)):

  ```toml
  [tool.uv]
  # `uv add` writes an exact version (==)
  add-bounds = "exact"
  ```

  `pyproject.toml` is general Python metadata that many tools read. The `[tool.uv]` table holds the settings that control how `uv` itself behaves.
- **`uv.lock` vs `pyproject.toml`**: the lockfile always records one exact version, but it is generated from `pyproject.toml`. List the packages you care about in `pyproject.toml` with `==`, and let the resolver choose compatible versions for everything else.
- **Downstream dependencies can still move**: the instructor has pinned pandas and still had something far downstream update and break it. The fix was to pin that package in `pyproject.toml` too.

> [!WARNING]
>
> A `>=` bound in a long-running project can silently pull in a new major version the next time the lockfile or image is rebuilt, and break your analysis. Pin the packages your results depend on with `==`.

### 11. Running a script with the project environment

*00:33:35–00:35:01*

- **`hello.py`** (in the [demo repository](https://github.com/chendaniely/2026-11-24-docker/blob/main/hello.py)):

  ```python
  import cowsay

  cowsay.cow("hello, moo.")
  ```

- **Locally**: `uv sync` sets up the environment, then `uv run hello.py` runs Python in that environment and prints an ASCII cow saying "hello, moo."
- **Next step**: everything works on the laptop. To hand it to the class it has to be in the `Dockerfile`, because if it isn't in the `Dockerfile` the image can't be built, and if it can't be built it can't be shared.
- **Same process inside the image**: the container has to repeat exactly what you just did locally.

### 12. Copying the environment files and `uv sync --locked` ([30.7 When `uv.lock` does not match `pyproject.toml`](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv.html#when-uv.lock-does-not-match-pyproject.toml))

*00:35:01–00:39:25*

- **`COPY pyproject.toml uv.lock .python-version ./`** copies the three files into `./`. Because of `WORKDIR`, that is `/workspace`.
- **`.python-version`** (contents: `3.14`) tells `uv` which Python to install. `uv.lock` only locks packages, and this file locks the interpreter. This matters because the Python version decides which package versions can be installed. For example, PyTorch is almost never compatible with the newest Python, so you usually have to pin an older one to get the neural-network stack installed.
  - Package authors (524) can also point this file at an upcoming Python release candidate, to check that their package will work when Python updates.
- **The three files**:
  - `.python-version` gives the Python version.
  - `uv.lock` gives the exact packages and versions.
  - `pyproject.toml` is the human-readable file that controls them.
- **`RUN uv sync --locked`** does what you would do on a fresh project, but `--locked` requires `pyproject.toml` and `uv.lock` to agree. If one is out of date, the build errors. You want it to fail loudly instead of building something you didn't expect.

### 13. Building the image and layer caching ([29.1.3 Layer caching](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#layer-caching))

*00:39:25–00:44:33*

- **Rebuild with the same command**: use the up arrow to recall a command instead of retyping it. The build paused on the `RUN uv sync --locked` step, which was installing Python and the packages exactly as you would on your own computer.
- **Inside the new container**: `pwd` showed `/workspace` straight away. `ls -a` showed `.python-version`, `.venv`, `pyproject.toml` and `uv.lock`. Use `-a`, because some of those files are hidden.
- **Layers**: each instruction becomes a cached layer. When a layer and everything above it are unchanged, Docker reuses the cache. That is why many `Dockerfile`s squeeze work into few instructions to save space (see [29.1.4 Guidelines for `RUN` commands](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#guidelines-for-run-commands)). The outcome is the same either way, and more lines are fine when you are starting out.
- **Order by how often things change**: changing a layer reruns everything below it. Put slow installs near the top and fast-changing files, like your code, near the bottom. Otherwise a typo fix in a script could trigger a 15-minute tidyverse reinstall.
  - Demo: adding `COPY hello.py ./` as the last line rebuilt in under a second. Only that step ran, and `uv run hello.py` then worked inside the container.
- **Sharing**: you can hand someone the `Dockerfile` to build, or (coming this week) publish the image so they can `docker pull` it, as with any other image (see [27.8 What is a container registry?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#what-is-a-container-registry)).

### 14. Why not bake your code into the image ([30.4 Run the project in a container](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv.html#run-the-project-in-a-container))

*00:49:36–00:53:26*

- **The problem**: during the milestones you change files constantly (EDA, analysis). `COPY`ing code, or even `COPY`ing everything, snapshots it into the image. Anyone opening the container then has to ask when the code was copied, and by which teammate.
- **It doesn't scale**: every change means commit, push, *and* rebuild the image so it holds the right version of each file.
- **Cloning inside the container**: you could install Git in the image and clone the repository from inside the container. With what you knew before today that is valid, and the instructor has done it to mimic a student's terminal. There is a better way.
- **The goal: separate compute from source code**: the image holds the installed software and packages, and the code lives outside it. The `COPY hello.py ./` line was removed and the image rebuilt. Removing a line is a change to the image too. The environment files still have to be copied, because the image can't be built without them.
- **Watch your prompt**: you will jump between the laptop and the container. The terminal prompt is how you know which machine you are typing into.

### 15. Mounting the project folder with `-v` ([28.1.2 Mounting volumes to containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#mounting-volumes-to-containers))

*00:53:26–00:59:33*

- **`-v` (`--volume`) mounts a folder**: at run time it makes a folder from your computer appear inside the container, like a shared drive. Edits on either side are edits to the same file, not a sync.
- **The command**: `docker run --rm -it -v "$(pwd):/workspace" 2026-11-24-docker bash`.
  - In Bash, `$( )` runs a command and substitutes its output, so `$(pwd)` is your current folder.
  - The current folder appears at `/workspace` in the container.
  - Windows users may need a leading slash, `/$(pwd)`. The textbook section shows each shell.
- **Demo**: the instructor created `my_secrets.txt` on the laptop ("i'm afraid of the dark."), and it appeared in the container. He then added a line on the laptop ("i eat baby food." He says applesauce is great trail-running food), and `cat` in the container showed the new line immediately.
- **Why not Git in the container**: it would need its own SSH key or personal access token. A rebuilt container would make a new key each time, so you'd re-register keys over and over. Mounting avoids that problem, which 521 solved on your laptop.
- **Run, not build**: mounting happens at `docker run`. A build can only copy.
- **Testing in both places**: you can still run `uv run hello.py` (for you, `uv run quarto render ...`) inside the container. That checks your work on your laptop and in the container.
- **Editor caveat**: Positron sometimes doesn't notice a file changed on disk, so you may need to refresh it.

### 16. Keeping the image's environment in `/opt/venv` ([30.5 Why the packages go in `/opt/venv`](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv.html#why-the-packages-go-in-optvenv))

*00:59:33–01:06:53*

- **`.venv` holds the actual Python binary and the project's packages**. Plain `python` doesn't exist in the container (`bash: python: command not found`), and `uv run` knows to look in `.venv`.
- **The mount brings your laptop's `.venv` with it**: teammates' computers differ in operating system (Windows, macOS, Linux) and CPU architecture (AMD64 vs ARM64), which gives up to six combinations. `uv sync` installs only for the system it runs on, although `uv.lock` records packages for every platform. The image was built under Linux, but the mount covered `/workspace` with the Mac's `.venv`. Packages with compiled code (anything that "runs fast", like pandas) are where this breaks. The textbook's [Building images for several platforms](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-platforms.html#one-image-one-kind-of-processor) explains why an image is built for one kind of processor.
- **The fix, an environment variable set at build time**: `UV_PROJECT_ENVIRONMENT` tells `uv` where to put and find the project environment. Its position doesn't matter as long as it comes before `uv sync`. The final `Dockerfile`:

  ```dockerfile
  FROM ubuntu:24.04

  # how to install uv
  COPY --from=ghcr.io/astral-sh/uv:0.13.7 /uv /uvx /usr/local/bin/

  WORKDIR /workspace

  ENV UV_PROJECT_ENVIRONMENT=/opt/venv
  COPY pyproject.toml uv.lock .python-version ./
  RUN uv sync --locked
  ```

- **Checking it**: after rebuilding (`uv sync` reran because the steps below the change rerun), `uv run which python` inside the mounted container printed `/opt/venv/bin/python`. The container now ignores the mounted `.venv` and uses its own Linux environment, so the image works whoever's laptop the project folder comes from.

> [!WARNING]
>
> Without `UV_PROJECT_ENVIRONMENT`, a mounted project folder hands the container your laptop's `.venv`. That is like copying a Mac program onto Windows and hoping it runs. In class, `uv` in the container deleted the mounted `.venv` and rebuilt it, which changes the folder on your own computer.

### 17. Docker Compose ([33 Containers: Docker Compose](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-docker-compose.html))

*01:06:53–01:14:06*

- **Why**: `docker run` commands keep growing: `--rm`, `-it`, `-v`, and a `-p` port for tools like JupyterLab or RStudio. Pasted commands are hard to edit because you can't click inside them. A file can be version controlled and its changes tracked.
- **`docker-compose.yml`** is a YAML file listing how to build and run containers. Its main use is running several containers together (microservices, for example a dashboard and its database kept separate). With one container it is a little overkill, but still useful. The class's file ([`docker-compose.yml`](https://github.com/chendaniely/2026-11-24-docker/blob/main/docker-compose.yml)):

  ```yaml
  services:
    analysis-env:
      build: .
      image: 2026-11-24-docker
      volumes:
        - .:/workspace
  ```

  - `services:` lists the containers. `analysis-env` is just a name (it could be `pizza`).
  - `build: .` builds from the `Dockerfile` in this folder.
  - `image:` names the image, like `--tag`.
  - `ports:` maps ports when needed, for example `<host port>:8787` for an RStudio container. The class left ports out.
  - `volumes:` replaces `-v`, and can mount several folders. One more volume line in the template was deleted and left for Thursday, 2026-11-26.
- **Commands**: `docker compose build` reads the file and builds. `docker compose up --detach` (`-d`) starts the container in the background and gives your prompt back.
- **Live demo didn't work**: the container exited straight away and couldn't be reached. The instructor will fix the demo for next class. In principle Compose turns the file into the same flags as the `docker run` command used earlier.

### 18. This week's milestone: a Dockerfile for your analysis

*01:14:06–01:17:04*

- **Main task**: write the `Dockerfile` that is the compute environment for your group's analysis. It is almost copy-paste from today's example.
- **What it must do**: you should be able to mount the folders that need mounting and run `uv run quarto render` on your report inside the container, and have it render.
- **How it is graded**: TAs take your repository, build the image, and try to run the analysis in the container. Your `pyproject.toml` and analysis should already exist, and this adds the container.
- **Optional extras**: you may add `RUN` lines for tools you want in the container, such as a text editor (today's image had neither `nano` nor `vi`). Some packages need system libraries from Ubuntu, for example geospatial work. Know why you add each one.
- **Compose isn't required yet**: the `Dockerfile` is the key file this week, and the instructor will get Compose working in a later class.

### 19. Docker Compose outside the course

*01:17:04–01:20:07*

- **Ready-made Compose files**: many open-source tools ship a `docker-compose.yml`, so you don't need to know how to install them.
- **Example, Actual Budget** (similar to Firefly III): personal finance software. Its Compose file defines one service, `actual server`, with an image, ports, environment variables, volumes and a health check. `docker compose up -d` downloads the image and starts it, and you connect in the browser on that port.
- **Other examples**: Jellyfin (serving movies and media), n8n (AI automation), and a recipe manager. They are web apps running on a port, like RStudio.
- **Where to run them**: any machine you like, from an old laptop in a closet to a paid cloud machine. Containers are a skill beyond compute environments.

## Commands from class

### Inspecting the agent's repository and rebuilding the R image

```bash
cd ~/temp/2026-11-24-docker
ls -alh                                   # Dockerfile, Makefile, README.md, .git
positron .                                # open the folder in Positron
docker images                             # 2026-11-24-docker:latest already built by Claude
docker build --tag 2026-11-24-docker .    # FROM step was CACHED, so it finished in 0.2 s
docker run --rm -it 2026-11-24-docker     # starts R because of CMD ["R"]; q() to quit
docker run --rm -it 2026-11-24-docker bash   # bash replaces the default CMD
pwd                                       # inside the container: /
ls
cd home/
ls -alh                                   # empty: no user in this image
exit
```

### Setting up the uv project on the laptop

```bash
uv init --bare        # creates pyproject.toml
uv add cowsay         # installs cowsay==6.1, creates .venv and uv.lock
uv sync
uv run hello.py       # prints the "hello, moo." cow
```

`hello.py`, `.python-version` and the `[tool.uv]` `add-bounds = "exact"` setting were written in the editor. The `Dockerfile` was then changed to the Ubuntu + uv version shown in theme 16, without the `ENV` line at this point.

### Building the Python image, then baking in and removing `hello.py`

```bash
docker build --tag 2026-11-24-docker .        # runs RUN uv sync --locked
docker run --rm -it 2026-11-24-docker bash
pwd                                           # /workspace
ls -a                                         # .python-version .venv pyproject.toml uv.lock
exit
# added `COPY hello.py ./` as the last line of the Dockerfile
docker build --tag 2026-11-24-docker .
docker run --rm -it 2026-11-24-docker bash
uv run hello.py                               # works inside the container
exit
# removed the COPY hello.py line again
docker build --tag 2026-11-24-docker .
```

The second build shows layer caching: only the new last step ran.

```
 => CACHED [stage-0 2/6] COPY --from=ghcr.io/astral-sh/uv:0.13.7 /uv /uvx   0.0s
 => CACHED [stage-0 3/6] WORKDIR /workspace                                 0.0s
 => CACHED [stage-0 4/6] COPY pyproject.toml uv.lock .python-version ./     0.0s
 => CACHED [stage-0 5/6] RUN uv sync --locked                               0.0s
 => [stage-0 6/6] COPY hello.py ./                                          0.0s
```

### Mounting the project folder

```bash
docker run --rm -it -v "$(pwd):/workspace" 2026-11-24-docker bash
ls                        # the laptop's files, including my_secrets.txt
cat my_secrets.txt        # run again after editing on the laptop: the new line appears
uv run hello.py           # works, but replaced the mounted .venv (see below)
ls -alh
exit
```

### Moving the environment to `/opt/venv`

```bash
# added ENV UV_PROJECT_ENVIRONMENT=/opt/venv before the COPY/RUN lines
docker build --tag 2026-11-24-docker .        # uv sync --locked ran again
docker run --rm -it -v "$(pwd):/workspace" 2026-11-24-docker bash
which uv                                      # /usr/local/bin/uv
uv tree                                       # 2026-11-24-docker v0.1.0 └── cowsay v6.1
uv run which python                           # /opt/venv/bin/python
exit
```

### Trying Docker Compose

```bash
docker compose build                          # builds from docker-compose.yml
docker compose up                             # container created, then exited with code 0
docker compose ps                             # nothing running
docker compose exec analysis-env bash         # service "analysis-env" is not running
```

### What went wrong live

- **Agent put the repository in the wrong place**: Claude Code created it under `~/temp` instead of `~/git`, probably because it was started in a different folder. The class worked from `~/temp/2026-11-24-docker`.
- **No text editor in the container**: `nano my_secrets.txt` and `vi my_secrets.txt` both gave `command not found`, because `ubuntu:24.04` ships without them. The file was edited on the laptop instead and read with `cat` in the container. Installing an editor with a `RUN` line is an option.
- **The mounted macOS `.venv`**: in the mounted container, before the `ENV` line, `uv run hello.py` printed:

  ```
  warning: Ignoring existing virtual environment linked to non-existent Python interpreter: `.venv/bin/python` -> `/Users/dan/.local/share/uv/python/cpython-3.14-macos-aarch64-none/bin/python3.14`
  Using CPython 3.14.10
  Removed virtual environment at: .venv
  Creating virtual environment at: .venv
  ```

  `uv` found the Mac's environment, could not use it, and rebuilt `.venv` in the shared folder. Adding `ENV UV_PROJECT_ENVIRONMENT=/opt/venv` and rebuilding fixed it.
- **Typo**: `ls 0alh` gave `No such file or directory`, and `ls -alh` was the intended command.
- **`python` not found**: plain `python` does not exist in the container. Python is only reachable through `uv run`.
- **No `uv which`**: `uv which python` gave `error: unrecognized subcommand 'which'`. `uv run which python` worked and showed `/opt/venv/bin/python`.
- **Compose container didn't stay up**: `docker compose up` created the network and container, then printed `analysis-env-1 exited with code 0`. A retry with `docker compose up --detatch` failed with `unknown flag: --detatch` (the flag is spelled `--detach`). `docker compose ps` listed nothing, and `docker compose exec` with either the service name or the image name reported the service was not running. This was not resolved in class, and the instructor will fix the demo next class.

## Assignments

- [ ] This week's project milestone: write a `Dockerfile` that reproduces your analysis's compute environment, so that TAs can build the image from your repository, mount the project, and run `uv run quarto render` on your report in the container. The due date was not stated in class; see the [student repository](https://github.com/UBC-MDS/DSCI_522_dsci-workflows_students).

---

- prompt: prompt-notes.md @ 76ca356
- prompt-hash: a00c660964b7
- model: claude-opus-5-5 (requested: opus)
- backend: claude
- inputs: transcript-plaud.md, terminal.txt, materials.md
- generated: 2026-11-24
