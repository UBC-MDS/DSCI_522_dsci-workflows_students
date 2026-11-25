# Python analysis images with uv, volume mounts and Docker Compose: review questions, tier 3 — Apply

Date: 2026-11-24

Instructor: Daniel Chen

*Tier 3 of 5: Apply. Work each situation through before you read the answer; tiers 1 (Remember) and 2 (Understand) cover the facts and reasons it relies on.*

## 1. Listing and building images ([29 Customizing and building containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html))

*00:12:42–00:16:40*

- **Q:** You are in `~/temp/2026-11-24-docker` and type `docker build --tag 2026-11-24-docker`, with nothing after the name. What is missing, and what do you add?
    - **A:** Add the trailing `.`, as in `docker build --tag 2026-11-24-docker .`. `docker build` looks for a file named `Dockerfile` by default, but it still needs a location to look in, and you can't leave that argument empty. The `.` means "here", the current directory. It is not a full stop. *(00:14:57)*

- **Q:** `docker images` already lists `2026-11-24-docker:latest`, and you have edited the `Dockerfile`. Which command replaces that image, and what happens if you pass `--tag pizza` instead?
    - **A:** Run `docker build --tag 2026-11-24-docker .`. Reusing the same name rebuilds that image and replaces it. The tag can be any name you like, so `--tag pizza` builds the same `Dockerfile` into an image called `pizza`. *(00:14:13)*

- **Q:** Rebuilding the `rocker/r-ver:4.6.2` image finishes in 0.2 seconds, and its `FROM` step says `CACHED`. You change `FROM` to an R version you have never downloaded. What do you expect from the next build?
    - **A:** The `FROM` step takes seconds or minutes, depending on your internet speed, because Docker has to download the new base image first. The first build was instant only because `rocker/r-ver:4.6.2` was already on your computer. *(00:16:15)*

## 2. Running a container, overriding `CMD`, and throwaway containers ([29.2.1 `CMD` or `ENTRYPOINT`?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#cmd-or-entrypoint))

*00:16:40–00:20:07*

- **Q:** Your `Dockerfile` is `FROM rocker/r-ver:4.6.2` followed by `CMD ["R"]`. What do you see after `docker run --rm -it 2026-11-24-docker`?
    - **A:** An R session starts, with R's startup banner, and you leave it with `q()`. With no command given after the image name, the container runs its default command, and `CMD ["R"]` sets that to R. *(00:17:17)*

- **Q:** You want to start a container from `2026-11-24-docker`, type into it, and have it deleted automatically when you exit. Which flags do you add to `docker run`?
    - **A:** Use `docker run --rm -it 2026-11-24-docker`. `--rm` deletes the container when you exit, so it isn't left running on your computer. `-it` gives you terminal access and passes what you type through to the container. *(00:16:53)*

- **Q:** You want a shell in `2026-11-24-docker` instead of R. What do you run, and where will `pwd` say you are?
    - **A:** Run `docker run --rm -it 2026-11-24-docker bash`. The `bash` after the image name replaces the default `R`. `pwd` prints `/`, the root of the file system, so `ls` shows system folders such as `bin`, `etc` and `usr`. *(00:18:12)*

- **Q:** You want to try installing PyTorch but worry it will wreck your setup. You do it inside a container started with `--rm`, then exit and start a new one. What state is the new container in?
    - **A:** It is back to the image exactly as built, because every change made in a `--rm` container is gone once you exit. That makes a container a safe place for risky experiments. If something goes wrong, restart the container and nothing bad has happened. *(00:19:58)*

## 3. Choosing a base image for a Python project ([29.3 Choosing a base image for your Dockerfile](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#choosing-a-base-image-for-your-dockerfile))

*00:20:07–00:24:22*

- **Q:** Your project is pure Python managed with `uv`, but your `Dockerfile` still starts `FROM rocker/r-ver:4.6.2`. What base do you switch to, and why?
    - **A:** Switch to `FROM ubuntu:24.04`. The R image carries a lot of R software that a Python project doesn't need, and a smaller image is more respectful of other people's disk space, which has become expensive. *(00:23:46)*

- **Q:** You want an even smaller image and consider Alpine instead of `ubuntu:24.04`. What trade-off do you accept?
    - **A:** Alpine is smaller, but you may have to install more software yourself, depending on what your project needs. Ubuntu is a good starting point for most of that. *(00:24:13)*

- **Q:** Your group's analysis is in Python, but one teammate wants to make the figures with ggplot2 in R. Is a single-language image required?
    - **A:** No. One project that mixes languages is common and valid. The textbook's example image has R and Python in the same container. *(00:22:42)*

- **Q:** You work on Windows or macOS and start a shell in a container. Which operating system's commands should you expect to use?
    - **A:** Linux, most likely some version of Ubuntu. Docker containers run on top of Linux whatever your laptop runs, so inside the container you are in the Linux world. *(00:23:33)*

## 4. Installing `uv` with `COPY --from`, and setting `WORKDIR` ([30.2 A `Dockerfile` for a uv project](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv.html#a-dockerfile-for-a-uv-project))

*00:24:22–00:27:42*

- **Q:** Your `Dockerfile` starts `FROM ubuntu:24.04` and later runs `uv sync`, but the base image has no `uv`. Which line do you add, and where does it put `uv`?
    - **A:** Add `COPY --from=ghcr.io/astral-sh/uv:0.13.7 /uv /uvx /usr/local/bin/`. It copies the `uv` and `uvx` programs out of uv's published image into the container's `/usr/local/bin/`. You are building a machine from scratch, so the copy of your setup that you hand out needs `uv` too. *(00:25:14)*

- **Q:** You add `WORKDIR /workspace`, rebuild, and run `docker run --rm -it 2026-11-24-docker bash`. Where does the prompt put you?
    - **A:** In `/workspace`. The prompt reads `root@…:/workspace` and `pwd` prints `/workspace`. `WORKDIR` changes the container's working directory, so you no longer land in `/` among the system files. *(00:40:54)*

- **Q:** `ubuntu:24.04` has no `/workspace` folder. Does `WORKDIR /workspace` make the build fail?
    - **A:** No. `WORKDIR` creates the folder if it doesn't exist and then makes it the working directory. *(00:27:23)*

## 5. Setting up the `uv` project locally ([30.1 The project](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv.html#the-project))

*00:27:42–00:29:58*

- **Q:** In a folder that holds only a `Dockerfile`, you want a `uv` project that depends on cowsay. In order, what do you run?
    - **A:** First `uv init --bare`, which creates `pyproject.toml`. Then `uv add cowsay`, which installs `cowsay==6.1` into a new `.venv` and records it in `uv.lock`. *(00:29:45)*

- **Q:** Right after `uv add cowsay` installs `cowsay==6.1`, what line do you expect in the `dependencies` of `pyproject.toml`?
    - **A:** `cowsay>=6.1`. By default `uv add` writes a lower bound, even though exactly 6.1 was installed. *(00:29:51)*

- **Q:** The `pyproject.toml` from `uv init --bare` only says `requires-python = ">=3.14"`. If you need the image to use one particular Python version, is that line enough?
    - **A:** No. `>=3.14` allows any newer Python, so you also need to set the Python version, which the project does with a `.python-version` file. *(00:29:07)*

## 6. Pinning exact versions in `pyproject.toml` ([22 uv: pinning exact versions](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/virtual-environments-python-uv-exact-pins.html))

*00:29:58–00:33:35*

- **Q:** Your `pyproject.toml` has `cowsay>=6.1`. cowsay 7.0 comes out next week, and you rebuild the image then. Which version do you get, and what is the risk?
    - **A:** You get 7.0, because `>=` allows anything newer. A change in the first number usually means a backwards-incompatible change, so behaviour you rely on in 6.x may stop working and your long-running project can break. *(00:30:17)*

- **Q:** You want cowsay to stay at 6.1 no matter when the image is rebuilt. What do you change in `pyproject.toml`?
    - **A:** Change the dependency to `cowsay==6.1`. The double equals pins that exact version. *(00:31:06)*

- **Q:** You want every future `uv add` in the project to write `==` instead of `>=`. What do you add to `pyproject.toml`?
    - **A:** Add a `[tool.uv]` table containing `add-bounds = "exact"`. The `[tool.uv]` table holds the settings that control how `uv` behaves, so from then on `uv add` writes exact versions. *(00:31:49)*

- **Q:** You pinned pandas with `==`, but pandas still breaks after a rebuild because a package far downstream updated. How do you fix it?
    - **A:** Add that downstream package to `pyproject.toml` and pin it with `==` too. Rolling it back to the version that worked makes pandas work again. *(00:32:47)*

- **Q:** Should you pin every package in the environment with `==` in `pyproject.toml`?
    - **A:** No. Pin the packages whose versions matter to you, and let the resolver choose compatible versions for everything else. `uv.lock` still records one exact version of each package. *(00:33:16)*

## 7. Running a script with the project environment ([30.1 The project](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv.html#the-project))

*00:33:35–00:35:01*

- **Q:** Your project folder has `pyproject.toml`, `uv.lock` and `hello.py`. In order, what do you run to set up the environment and run the script?
    - **A:** Run `uv sync`, then `uv run hello.py`. `uv run` runs Python in the project's environment, where cowsay is installed. *(00:34:15)*

- **Q:** `hello.py` contains `import cowsay` and `cowsay.cow("hello, moo.")`. What does `uv run hello.py` print?
    - **A:** An ASCII-art cow with a speech bubble that says "hello, moo." *(00:34:20)*

- **Q:** `uv run hello.py` works on your laptop, but your `Dockerfile` only installs `uv`. Can a classmate get your working environment from the image you build?
    - **A:** No. Every setup step must also be written into the `Dockerfile`. If a step isn't in the `Dockerfile`, the image can't be built with it, and if the image can't be built you can't share it. *(00:34:45)*

## 8. Copying the environment files and `uv sync --locked` ([30.2 A `Dockerfile` for a uv project](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv.html#a-dockerfile-for-a-uv-project))

*00:35:01–00:39:25*

- **Q:** After `WORKDIR /workspace`, you need the image to know your project's Python version and packages. Which `COPY` line do you write, and where do the files land?
    - **A:** Write `COPY pyproject.toml uv.lock .python-version ./`. They land in `/workspace`, because `./` means the working directory set by `WORKDIR`. *(00:35:09)*

- **Q:** Your project needs PyTorch, which is almost never compatible with the newest Python. How do you make sure the image installs a Python it supports?
    - **A:** Set the version in `.python-version` and copy that file into the image. `uv` installs the Python version that file names, and the Python version decides which package versions can be installed. *(00:35:59)*

- **Q:** You maintain a package and want to check it against an upcoming Python release candidate before it comes out. Which file do you change?
    - **A:** `.python-version`. Point it at the release candidate to build an environment with the coming Python version, and check that your package still works when Python updates. *(00:37:22)*

- **Q:** You edit `pyproject.toml` but `uv.lock` no longer matches it, and your `Dockerfile` ends with `RUN uv sync --locked`. What happens when you build, and is that what you want?
    - **A:** The build stops with an error at the `uv sync --locked` step. That is what you want. `--locked` requires `pyproject.toml` and `uv.lock` to be in sync, so a mismatch fails loudly instead of quietly building something you didn't expect. *(00:38:55)*

## 9. Building the image and layer caching ([29.1.3 Layer caching](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#layer-caching))

*00:39:25–00:44:33*

- **Q:** You need to run `docker build --tag 2026-11-24-docker .` again, a command you typed a few minutes ago. What is the quickest way?
    - **A:** Press the up arrow to bring back a command you have already typed, instead of retyping it. *(00:39:29)*

- **Q:** Inside the new container, `ls` in `/workspace` shows only `pyproject.toml` and `uv.lock`. Where are `.python-version` and `.venv`?
    - **A:** They are there, but hidden, because their names start with a dot. `ls -a` lists `.python-version`, `.venv`, `pyproject.toml` and `uv.lock`. *(00:41:06)*

- **Q:** You add `COPY hello.py ./` as the last line of the `Dockerfile` and rebuild. Which steps do you expect to run again?
    - **A:** Only the new `COPY hello.py ./` step. The steps above it, including `RUN uv sync --locked`, show `CACHED` because they haven't changed, so the build finishes in under a second. *(00:43:49)*

- **Q:** Your `Dockerfile` copies your code before a slow package install, and each typo fix in a script takes many minutes to rebuild. What is wrong, and what do you change?
    - **A:** Changing a layer reruns it and every layer below it, so each code edit triggers the slow install again. Move the slow, rarely changing install steps to the top and copy your code at the end. Then a typo fix only reruns the fast `COPY`. *(00:42:40)*

- **Q:** You are new to Docker and your `Dockerfile` has many short lines rather than a few combined ones. Do you need to merge them?
    - **A:** No. Combining steps into fewer instructions saves a little disk space, but it doesn't change the outcome, so more lines are fine when you are starting out. *(00:41:59)*

- **Q:** A teammate wants your exact environment. What two ways can you give it to them?
    - **A:** Give them the `Dockerfile` to build with `docker build`. Or publish the image so they can download it with `docker pull`, and they don't have to build anything. *(00:44:16)*

## 10. Why not bake your code into the image ([30.4 Run the project in a container](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv.html#run-the-project-in-a-container))

*00:49:36–00:53:26*

- **Q:** Your group edits EDA files many times a day, and you consider copying the whole project into the image. What problems should you predict?
    - **A:** The code is snapshotted into the image. Anyone opening the container has to ask when the code was copied, and by which teammate. Every change also means commit and push *and* rebuild the image so it holds the right version of each file. That doesn't scale for work that is still changing. *(00:50:47)*

- **Q:** You delete the `COPY hello.py ./` line from the `Dockerfile`. Do you need to rebuild?
    - **A:** Yes. Removing a line is a change to the image too. Until you rebuild, the old image still contains `hello.py`. *(00:53:16)*

- **Q:** Now that code stays out of the image, you want to drop `COPY pyproject.toml uv.lock .python-version ./` as well. Should you?
    - **A:** No. The image can't install the environment without those three files, so they must still be copied in. *(00:52:30)*

- **Q:** You are switching between your laptop's terminal and a container's shell, and a command behaves unexpectedly. What should you check first?
    - **A:** Check the terminal prompt. It tells you which machine you are typing into, for example your laptop's prompt versus `root@…:/workspace` in the container. *(00:52:53)*

## 11. Mounting the project folder with `-v` ([28.1.2 Mounting volumes to containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#mounting-volumes-to-containers))

*00:53:26–00:59:33*

- **Q:** From your project folder, you want a shell in `2026-11-24-docker` with that folder available at `/workspace`. What do you run?
    - **A:** Run `docker run --rm -it -v "$(pwd):/workspace" 2026-11-24-docker bash`. `-v` mounts a folder, and `$(pwd)` substitutes your current directory, which then appears at `/workspace` in the container. *(00:57:13)*

- **Q:** With that container open, you add the line "i eat baby food." to `my_secrets.txt` on your laptop. What does `cat my_secrets.txt` show inside the container?
    - **A:** Both lines, including the new one, straight away. A mount works like a shared drive: the laptop and the container are working on the same file, not on a synced copy. *(00:58:53)*

- **Q:** You try to put the folder mount into the `Dockerfile` so it happens at build time. Will that work?
    - **A:** No. Mounting happens at `docker run`. The build process can only copy files into the image. *(00:56:06)*

- **Q:** Instead of mounting, you consider installing Git in the container and cloning your repository there. What problem will you run into?
    - **A:** The container needs its own SSH key or personal access token before it can push and pull. Each rebuilt container would make a new key that you'd have to register again. A mount avoids all of that, because Git keeps running on your laptop. *(00:54:52)*

- **Q:** You use Windows and the mount command doesn't work as written. What should you try?
    - **A:** You may need a leading slash, as in `/$(pwd)`. The textbook shows the exact form for each shell. *(00:56:34)*

- **Q:** You change a file from inside the container, but Positron on your laptop still shows the old contents. What do you do?
    - **A:** Refresh the file in Positron. The file on disk did change, but Positron sometimes doesn't notice that a file was updated on disk. *(00:55:51)*

## 12. Keeping the image's environment in `/opt/venv` ([30.5 Why the packages go in `/opt/venv`](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv.html#why-the-packages-go-in-optvenv))

*00:59:33–01:06:53*

- **Q:** In a container started with `-v "$(pwd):/workspace"`, `uv run hello.py` prints `Ignoring existing virtual environment linked to non-existent Python interpreter` pointing at a `macos-aarch64` Python, then `Removed virtual environment at: .venv`. What went wrong, and how do you fix it?
    - **A:** The mount replaced the image's `/workspace` with your laptop's folder, including your Mac's `.venv`. The Linux container couldn't use it, so `uv` deleted it and rebuilt `.venv`, which changes the folder on your own computer. Add `ENV UV_PROJECT_ENVIRONMENT=/opt/venv` to the `Dockerfile` before `RUN uv sync --locked`, then rebuild, so the image keeps its Linux environment outside the mounted folder. *(01:04:01)*

- **Q:** You add `ENV UV_PROJECT_ENVIRONMENT=/opt/venv` above the `COPY pyproject.toml …` line. Does its exact position matter, and what will the rebuild do?
    - **A:** Any position works as long as it comes before `uv sync`. Every step below the new line reruns, including `RUN uv sync --locked`, which is what you want, because the packages now get installed into `/opt/venv`. *(01:05:33)*

- **Q:** You want to confirm which Python the container uses. `uv which python` gives `error: unrecognized subcommand 'which'`. What do you run instead, and what should it print?
    - **A:** Run `uv run which python`. It should print `/opt/venv/bin/python`, which shows that `uv` ignores the mounted `.venv` and uses the image's own environment. *(01:06:20)*

- **Q:** In the container you type `python` and get `bash: python: command not found`. How do you run Python?
    - **A:** Go through `uv`, for example `uv run hello.py`. Python exists only inside the project environment, and `uv` knows where to find it. *(01:00:15)*

- **Q:** One teammate is on Windows with an AMD64 chip and another on an ARM64 Mac. Cowsay works from a mounted `.venv`, but you add pandas. What should you expect without `/opt/venv`, and with it?
    - **A:** Without it, packages with compiled code, like pandas, are where the laptop's mounted environment is likely to break inside the Linux container. With `UV_PROJECT_ENVIRONMENT=/opt/venv`, the image's packages were installed for Linux at build time and are used whichever laptop the project folder comes from. *(01:04:46)*

## 13. Docker Compose ([33 Containers: Docker Compose](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-docker-compose.html))

*01:06:53–01:14:06*

- **Q:** Your `docker run` command keeps growing, and soon it will need a `-p` port for JupyterLab or RStudio. Editing pasted commands is painful. What do you switch to?
    - **A:** A `docker-compose.yml` file that records the build and run options. A file can be version controlled and its changes tracked, so you run short commands instead of copying and pasting long ones. *(01:11:28)*

- **Q:** Write the `docker-compose.yml` that replaces building `2026-11-24-docker` and running it with `-v "$(pwd):/workspace"`.
    - **A:** Use `services:`, then a service such as `analysis-env:` containing `build: .`, `image: 2026-11-24-docker` and `volumes:` with `- .:/workspace`. `build: .` uses the `Dockerfile` in this folder, `image:` names the image like `--tag` does, and `volumes:` replaces `-v`. *(01:10:25)*

- **Q:** With `docker-compose.yml` in place, which commands build the image and then start the container in the background?
    - **A:** Run `docker compose build`, then `docker compose up --detach` (or `-d`). Detaching starts the container and gives you your prompt back while it runs in the background. *(01:11:59)*

- **Q:** You type `docker compose up --detatch` and get `unknown flag: --detatch`. What is wrong?
    - **A:** The flag is misspelled. It is `--detach`, or the short form `-d`. *(01:12:47)*

- **Q:** `docker compose up` prints `analysis-env-1 exited with code 0`, `docker compose ps` lists nothing, and `docker compose exec analysis-env bash` says `service "analysis-env" is not running`. What does that tell you?
    - **A:** The container started and exited right away, so nothing is running for `exec` to connect to. Using the image name instead of the service name gives the same "not running" result. This demo was left unresolved, to be fixed next class. *(01:13:50)*

- **Q:** You later need an RStudio container, which serves on port 8787 inside the container. What do you add to the service in `docker-compose.yml`?
    - **A:** A `ports:` entry that maps a port on your computer to 8787 in the container, in the form `<your port>:8787`. *(01:10:21)*

## 14. This week's milestone: a Dockerfile for your analysis

*01:14:06–01:17:04*

- **Q:** Your group's `Dockerfile` is done and you want to check it the way it will be graded. In order, what do you do?
    - **A:** Build the image from your repository. Run a container with the needed project folders mounted. Inside it, run `uv run quarto render` on your report. If the report renders, the image reproduces your analysis's compute environment. *(01:15:01)*

- **Q:** Your analysis uses a geospatial Python package that depends on system tools. The `uv sync` setup alone isn't enough in the image. What do you add?
    - **A:** Add `RUN` lines that install the needed system tools from Ubuntu. Geospatial packages are built on top of such system libraries, so what you install depends on your tool stack. *(01:16:16)*

- **Q:** Inside your container, `nano my_secrets.txt` and `vi my_secrets.txt` both give `command not found`. What are your options?
    - **A:** `ubuntu:24.04` ships without a text editor. Edit the file on your laptop, where a mounted folder shows the change in the container immediately. Or add a `RUN` line to install an editor in the image, as long as you know why you are adding it. *(01:15:41)*

---

- prompt: prompt-recall-3-apply.md @ 65eb21c
- prompt-hash: 49276171f719
- model: claude-opus-5-5 (requested: opus)
- backend: claude
- inputs: transcript-plaud.md, terminal.txt, materials.md, notes-class-main--claude-opus-5-5.md
- generated: 2026-11-24
- notes-input: notes-class-main--claude-opus-5-5.md @ 0caf0d47e007, links and section references removed, diagrams removed
