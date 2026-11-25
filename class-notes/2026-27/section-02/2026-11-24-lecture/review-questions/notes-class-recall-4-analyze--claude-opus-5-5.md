# Building a Python analysis image with uv, volume mounts and Docker Compose: review questions, tier 4 — Analyze

Date: 2026-11-24

Instructor: Daniel Chen

*Tier 4 of 5: Analyze. Take each one apart yourself before you read the answer; tiers 1 to 3 cover the facts, reasons and steps it relies on.*

## 1. Letting Claude Code build the repository

*00:07:21–00:11:24*

- **Q:** Break down what Claude Code did when asked to create the `2026-11-24-docker` repository with a `Dockerfile`. Which commands were checks, which built the project, and which results were the agent's own choices rather than the prompt's?
    - **A:** The checks came first. It ran `ls`, checked that `docker` and the `gh` command exist, and ran a Docker command to find out what kind of computer it was on. Then it built the project: it ran `mkdir` to make the folder, wrote a `Dockerfile` starting from Rocker, built the image, and ran a script in the container to test it. Its own choices were to put the folder in the temp folder instead of the Git folder, to add a `README.md` and a `Makefile` (the instructor usually asks for these, so they had become defaults), and to add `CMD ["R"]`. The instructor said the precise words in the prompt, such as Dockerfile and the image name, are what steered it to the right answer. *(00:10:37)*

## 2. Listing and building images ([29 Customizing and building containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html))

*00:12:42–00:16:40*

- **Q:** Break down `docker build --tag 2026-11-24-docker .` into its parts. Then examine why the rebuild of the R image finished in 0.2 s with `CACHED [1/1] FROM docker.io/rocker/r-ver:4.6.2`.
    - **A:** `docker build` looks for a file named `Dockerfile` (capital D) by default. `--tag` (`-t`) gives the image a name, which can be anything, even `pizza`, and reusing an existing name rebuilds that image. The trailing `.` is not a full stop. It means "here": the location to look in, a required input with no default, like a function argument. The `Dockerfile` had only one build step, `FROM rocker/r-ver:4.6.2`, and that image was already downloaded from last class, so the step was cached. A base image you don't have yet would make that step take seconds or minutes, depending on your internet speed. *(00:15:45)*

## 3. Running a container, overriding `CMD`, and throwaway containers ([28 Using and running containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html))

*00:16:40–00:20:07*

- **Q:** Separate the parts of `docker run --rm -it 2026-11-24-docker bash` and relate each part to what happened in class. Why did this command give a shell at `/` when `docker run --rm -it 2026-11-24-docker` had started R?
    - **A:** `--rm` deletes the container when you exit. `-it` gives you terminal access and passes what you type through to the container. `2026-11-24-docker` picks the image to start. Without anything after the image name, the image's `CMD ["R"]` ran, so R started. Adding `bash` replaced that default, so you got a normal terminal instead. The `Dockerfile` set no working directory, so `pwd` printed `/` and the system folders were visible, and `/home` was empty because the image has no user. *(00:17:45)*

- **Q:** Distinguish what survives and what is thrown away when you exit a container started with `--rm`. How does that split make a container a safe place to experiment?
    - **A:** The image survives. The container, with every change you made inside it, is removed when you exit. Starting again builds a fresh container from the unchanged image, so your earlier changes are gone. The instructor compared this to a version of Git that automatically resets all your changes. That is why something risky, such as installing PyTorch, belongs in a container: if it goes wrong, you restart and nothing bad has happened. *(00:19:29)*

## 4. Choosing a base image for a Python project ([29.3 Choosing a base image for your Dockerfile](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#choosing-a-base-image-for-your-dockerfile))

*00:20:07–00:24:22*

- **Q:** Set `rocker/r-ver`, `ubuntu:24.04` and Alpine side by side, as the class discussed them. For each, what comes installed, how big it is, and how much you have to add yourself?
    - **A:** All three are Linux. Inside any container you are in the Linux world, most likely some version of Ubuntu, even on a Mac or Windows laptop. `rocker/r-ver` has a lot of R software installed, which a Python project doesn't need, so it is the largest. `ubuntu:24.04` is smaller, though still a fairly big image, and it is a good starting point: the class added `uv` to it. Alpine is even smaller, but you may have to install more yourself, depending on what you need. Smaller images matter because disk space has become expensive, and you should be respectful of other people's disk space. *(00:23:46)*

## 5. Installing `uv` with `COPY --from`, and setting `WORKDIR` ([30.2 A `Dockerfile` for a uv project](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv.html#a-dockerfile-for-a-uv-project))

*00:24:22–00:27:42*

- **Q:** Break down `COPY --from=ghcr.io/astral-sh/uv:0.13.7 /uv /uvx /usr/local/bin/` into its source, what it copies, and its destination. Then relate the destination to what `which uv` printed later in the mounted container.
    - **A:** `--from=ghcr.io/astral-sh/uv:0.13.7` names another image. Read it like a GitHub path: the owner, then the repository, then the version tag. `/uv` and `/uvx` are the programs copied out of that image. `/usr/local/bin/` is where they land in the new image. This installs `uv` in a machine built from scratch, just as everyone installed `uv` at orientation. Later, `which uv` inside the container printed `/usr/local/bin/uv`, the destination from this line. *(00:24:53)*

- **Q:** Examine `WORKDIR /workspace` in the Ubuntu image's `Dockerfile`. What does it change for the build steps after it, and for a container started from the image, as the R image's `pwd` and the Python image's `pwd` showed?
    - **A:** `WORKDIR /workspace` makes `/workspace` the current directory and creates the folder if it doesn't exist. For the steps after it, `COPY pyproject.toml uv.lock .python-version ./` copies to `./`, which is `/workspace`. For a running container, `pwd` printed `/workspace` straight away, while the R image without a `WORKDIR` had printed `/`. Landing in a project folder keeps you away from the system files at the root, where moving the wrong folder could break everything. *(00:40:54)*

## 6. Setting up the `uv` project locally ([22.1 What `uv add` writes by default](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/virtual-environments-python-uv-exact-pins.html#what-uv-add-writes-by-default))

*00:27:42–00:29:58*

- **Q:** Follow cowsay into the `2026-11-24-docker` project, from `uv init --bare` to `uv add cowsay`. What does each step create or change, and what did `uv add` record in `pyproject.toml` compared with what it installed?
    - **A:** `uv init --bare` created `pyproject.toml`, with a name, a version and `requires-python` set to 3.14 or newer. `uv add cowsay` added cowsay to the `dependencies` list, which you could also type in by hand. It also printed `Creating virtual environment at: .venv` and installed `cowsay==6.1`. The project folder then held a `uv.lock` next to `pyproject.toml`. `uv add` installed exactly 6.1, but by default it wrote the lower bound `cowsay>=6.1` into `pyproject.toml`. *(00:29:38)*

## 7. Pinning exact versions in `pyproject.toml` ([22 uv: pinning exact versions](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/virtual-environments-python-uv-exact-pins.html))

*00:29:58–00:33:35*

- **Q:** Trace how the line `cowsay>=6.1` could break a long-running analysis. Which outside event and which rebuild cause it, and which two changes to `pyproject.toml` close that path?
    - **A:** `>=` allows any newer version. Suppose cowsay 7.0 comes out next week. Rebuilding the container next week then installs 7.0, and the package updates without anyone asking for it. A change in the first number usually means a backwards-incompatible change, so behaviour your code relies on in 6.x may not work in 7.x, and the analysis breaks. The fix is to write `cowsay==6.1`, and to add a `[tool.uv]` table with `add-bounds = "exact"` so that `uv add` always writes `==` from then on. The instructor warned that `>=` in a long project carries a real chance of this break. *(00:31:06)*

- **Q:** Distinguish what `pyproject.toml` and `uv.lock` each record about versions. Which packages are left to the resolver, and what did the instructor do when one of them broke pandas?
    - **A:** `uv.lock` always pins one exact version of every package, but it is generated from `pyproject.toml`. `pyproject.toml` holds the versions you care about, pinned with `==`, and the resolver picks compatible versions for everything else. That means downstream dependencies can still update on their own. The instructor once had pandas pinned when something far downstream updated and broke pandas. The fix was to add that downstream package to `pyproject.toml` and pin it too. *(00:33:16)*

## 8. Copying the environment files and `uv sync --locked` ([30.2 A `Dockerfile` for a uv project](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv.html#a-dockerfile-for-a-uv-project))

*00:35:01–00:39:25*

- **Q:** Separate the three files in `COPY pyproject.toml uv.lock .python-version ./` by what each one controls. Then point out what `RUN uv sync --locked` checks between two of them.
    - **A:** `.python-version` (here `3.14`) says which version of Python to install. `uv.lock` only locks the packages and their dependencies. `pyproject.toml` is the human-readable file that controls the rest. The Python version matters for the packages too: it decides which package versions can be installed, and PyTorch, for example, is almost never compatible with the newest Python. `--locked` requires `pyproject.toml` and `uv.lock` to be in sync, and the build errors if one is out of date, so it fails when you want it to fail. *(00:37:44)*

## 9. Building the image and layer caching ([29.1.3 Layer caching](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#layer-caching))

*00:39:25–00:44:33*

- **Q:** Examine the build output after `COPY hello.py ./` was added as the last line of the `Dockerfile`. Which steps say `CACHED`, which step ran, and how does that relate to where the new line sits?
    - **A:** Steps 2/6 to 5/6 (`COPY --from` for `uv`, `WORKDIR /workspace`, copying the three environment files, and `RUN uv sync --locked`) all say `CACHED`. Only `[stage-0 6/6] COPY hello.py ./` ran, and the whole build took under a second. In the first Ubuntu build, by contrast, `RUN uv sync --locked` was the step that stalled while it installed Python and cowsay. Docker reruns a changed step and everything below it, so a new line at the bottom reruns only itself. Copying a file is fast, so the rebuild was fast. *(00:43:49)*

- **Q:** Distinguish the two habits for writing a `Dockerfile` that the instructor described: using as few instructions as possible, and ordering steps by how often they change. What does each one save, and does either change the resulting image?
    - **A:** Each instruction becomes a cached layer. Squeezing work into few instructions saves disk space. It doesn't affect the outcome, and having more lines is fine when you are starting out. Ordering matters for rebuild time: a change to a layer reruns everything after it. So slow, rarely changing installs go at the top and fast-changing files, such as your code, go at the bottom. Otherwise fixing a typo in a script could make you wait something like 15 minutes for tidyverse to reinstall. *(00:42:40)*

## 10. Why not bake your code into the image ([30.4 Run the project in a container](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv.html#run-the-project-in-a-container))

*00:49:36–00:53:26*

- **Q:** Break down what happens on every code change when a group's code is copied into the image with `COPY`. What questions does someone opening the container have to ask, and which `COPY` lines stay in the `Dockerfile` once the code is taken out?
    - **A:** Every change means you git commit and push, and you also have to remember to copy everything in and rebuild, so the image holds the right version of each file. The code in the image is a snapshot. Anyone opening the container has to ask when the code was copied and which teammate copied it. That does not scale for work that is changing quickly, such as EDA during the milestones. The goal is to separate compute from source code. `COPY hello.py ./` was removed, and removing a line is also a change that needs a rebuild. `pyproject.toml`, `uv.lock` and `.python-version` are still copied, because the image can't be built without them. *(00:50:47)*

## 11. Mounting the project folder with `-v` ([28.1.2 Mounting volumes to containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#mounting-volumes-to-containers))

*00:53:26–00:59:33*

- **Q:** Trace the `my_secrets.txt` demo step by step. At which step did the mount still look like a plain copy, and which step showed that it is a shared folder?
    - **A:** The file was created on the laptop with "i'm afraid of the dark." Running `docker run --rm -it -v "$(pwd):/workspace" 2026-11-24-docker bash` and then `ls` showed it in `/workspace`. At that point it looked as if every file had simply been copied in. `nano` and `vi` gave `command not found` in the container, so the instructor added "i eat baby food." on the laptop. Running `cat my_secrets.txt` again in the container showed the new line straight away. That proves the container and the laptop share the same folder. *(00:58:53)*

- **Q:** Break down `-v "$(pwd):/workspace"` into its parts. Then deduce why this is a `docker run` option and not something written in the `Dockerfile` at build time.
    - **A:** `-v` (`--volume`) mounts a volume. In Bash, `$(pwd)` runs `pwd` and substitutes your current working directory. That folder appears at `/workspace` in the container. On Windows a leading slash may be needed, and the textbook shows each shell. A build can only copy files into the image. Only at run time can Docker take a folder from your computer and keep it in sync at another location. *(00:56:06)*

- **Q:** Set two ways of getting a group's code into a running container side by side: installing Git in the image and cloning the repository, and mounting the folder with `-v`. Compare what each needs for authentication and what happens each time the container is rebuilt.
    - **A:** Cloning is valid, and the instructor has done it to mimic a student's terminal. But Git in the container needs its own SSH key or personal access token to push and pull. Every rebuilt container would make a new key, which you would have to register again each time, so Git becomes a big problem there. Mounting uses the folder on your laptop, where 521 already set up authentication. Inside the container, you are working on the same files as on your laptop. *(00:54:52)*

## 12. Keeping the image's environment in `/opt/venv` ([30.5 Why the packages go in `/opt/venv`](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv.html#why-the-packages-go-in-optvenv))

*00:59:33–01:06:53*

- **Q:** Examine what `uv run hello.py` printed in the mounted container before the `ENV` line was added. What does each line reveal, and what did it do to a folder your own computer uses?
    - **A:** The warning said the existing `.venv/bin/python` pointed to `/Users/dan/.local/share/uv/python/cpython-3.14-macos-aarch64-none/bin/python3.14`. That is the Mac's Python, which doesn't exist inside the Linux container. `Using CPython 3.14.10` shows uv fetching a Linux Python instead. `Removed virtual environment at: .venv` and `Creating virtual environment at: .venv` show uv deleting the mounted `.venv` and rebuilding it. Because `/workspace` is the laptop's own folder, the laptop's `.venv` was overwritten. The instructor warned that this is like copying your Mac files to Windows and hoping they run. *(01:02:40)*

- **Q:** Break down why a `.venv` that works on one teammate's laptop can't be trusted in the container. Name the two ways computers differ, what `uv sync` installs compared with what `uv.lock` records, and which packages are most likely to break.
    - **A:** Computers differ in operating system (Windows, Mac, Linux) and in CPU architecture (AMD64 or ARM64), which gives up to six combinations in one group. `uv sync` installs only for the system it runs on. `uv.lock` records the packages for every other system too, but they don't get installed. The image is built under Linux, so a Mac `.venv` mounted over it is for the wrong system. Pure-Python packages like cowsay get away with it. Packages with compiled C code, such as pandas, anything that "runs fast" in Python, are where it breaks. *(01:01:22)*

- **Q:** Trace the fix from `ENV UV_PROJECT_ENVIRONMENT=/opt/venv` to the check inside the container. Where must the line go, what reruns when you rebuild, and what showed that the mounted `.venv` is now ignored?
    - **A:** The variable tells uv where to save and look for the project environment, so it must come before `RUN uv sync --locked`. Its exact position otherwise doesn't matter. Adding it is a change to the image, so the rebuild ran `uv sync --locked` again, and this time the environment went into `/opt/venv` under Linux. In the mounted container, `uv run which python` printed `/opt/venv/bin/python`. uv now ignores the laptop's `.venv`, so the image works whoever's laptop the project folder comes from. *(01:06:20)*

## 13. Docker Compose ([33.1 Docker Compose to launch containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-docker-compose.html#docker-compose-to-launch-containers))

*01:06:53–01:14:06*

- **Q:** Relate each line of the class's `docker-compose.yml` (`services:`, `analysis-env:`, `build: .`, `image: 2026-11-24-docker`, `volumes: - .:/workspace`) to the `docker build` or `docker run` option it stands in for. Which option did the class leave out?
    - **A:** `services:` lists the containers, here one named `analysis-env`, a name you choose (it could be `pizza`). `build: .` builds from the `Dockerfile` in the current folder, like `docker build .`. `image: 2026-11-24-docker` names the image, like `--tag`. `volumes: - .:/workspace` mounts the current folder at `/workspace`, like `-v "$(pwd):/workspace"`. A `ports:` entry would replace `-p` for a tool like RStudio, but the class left it out. With the file in place, `docker compose build` reads it and builds, and the settings are version controlled instead of living in a pasted command. *(01:11:09)*

- **Q:** Examine the terminal output from the class's Compose attempt. Separate the commands that worked from the ones that didn't, and point out the typo among the failures.
    - **A:** `docker compose build` worked. Every step was `CACHED`, and it ended with `Image 2026-11-24-docker Built`. `docker compose up` created the network `2026-11-24-docker_default` and the container `2026-11-24-docker-analysis-env-1`, then printed `analysis-env-1 exited with code 0`, so no container stayed running. `docker compose up --detatch` failed with `unknown flag: --detatch`, a misspelling of `--detach`. Then `docker compose ps` listed nothing, and `docker compose exec analysis-env bash` reported the service was not running. The instructor left this unresolved and will fix the demo next class. *(01:12:32)*

## 14. This week's milestone: a Dockerfile for your analysis

*01:14:06–01:17:04*

- **Q:** Break down how the TAs check this week's milestone into its steps. What in the group's repository does each step depend on?
    - **A:** First, the TAs build an image from the repository's `Dockerfile`. That build needs the `pyproject.toml` and lockfile the analysis already uses, copied in so that the packages get installed. Next, they go into the container and mount the folders that need to be mounted, which brings the analysis code in. Finally, they run `uv run quarto render` on the report, and it should render inside the container. Extra `RUN` lines, such as a text editor or Ubuntu system libraries for geospatial work, are optional, as long as you know why you added each one. *(01:15:01)*

## 15. Docker Compose outside the course ([33 Containers: Docker Compose](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-docker-compose.html))

*01:17:04–01:20:07*

- **Q:** Break down the Actual Budget Compose file shown in class into its parts. Then relate what `docker compose up -d` does with it to what a user has to do.
    - **A:** It has `services` with one container, named `actual server`, which comes from a ready-made image rather than being built from a local `Dockerfile`. It also sets ports, environment variables the software needs to run, volumes, and a health check that keeps the server alive. `docker compose up -d` downloads the image, runs the software, and you connect to that port in your browser. The user doesn't need to know how to install the software, just how to run Docker. The machine can be an old laptop in a closet or a paid cloud machine. *(01:18:10)*

---

- prompt: prompt-recall-4-analyze.md @ 65eb21c
- prompt-hash: 7dde50dd5ebf
- model: claude-opus-5-5 (requested: opus)
- backend: claude
- inputs: transcript-plaud.md, terminal.txt, materials.md, notes-class-main--claude-opus-5-5.md
- generated: 2026-11-24
- notes-input: notes-class-main--claude-opus-5-5.md @ 0caf0d47e007, links and section references removed
