# Building a Python analysis image with uv, volume mounts and Docker Compose: review questions, tier 2 — Understand

Date: 2026-11-24

Instructor: Daniel Chen

*Tier 2 of 5: Understand. Explain each answer in your own words before you read it; tier 1 (Remember) covers the facts, tiers 3 to 5 put them to use.*

## 1. Letting Claude Code build the repository

*00:07:21–00:11:24*

- **Q:** Why did the instructor say that knowing Docker vocabulary still matters when a coding agent writes the `Dockerfile` for you?
    - **A:** The prompt has to contain the right words, such as "Dockerfile", "image" and the exact image name. Those words steer the agent toward the correct answer. Someone who had never heard of Docker would not know which words to use, and would struggle to get a useful result. *(00:08:06)*

- **Q:** Explain why Claude Code created a `README.md` and a `Makefile` in `2026-11-24-docker` when the prompt never asked for them.
    - **A:** The instructor had set up his computer so that the agent uses his usual defaults, and he normally asks for those files. He pointed out that this is a benefit of coding agents: once you have templates you like, the agent can apply them for you. *(00:11:24)*

- **Q:** Summarize what the shell commands visible in the agent's run show it was doing before and after it wrote the `Dockerfile`.
    - **A:** First it explored the machine. It ran `ls`, checked that `docker` and `gh` exist, and ran a Docker command to learn what kind of computer it was on. Then it ran `mkdir` to make the folder and wrote a `Dockerfile` starting from Rocker. Finally it built the image and ran a script in the container to test it. *(00:09:26)*

- **Q:** Why did the agent put the repository under `~/temp` instead of the instructor's usual Git folder?
    - **A:** The instructor had started Claude in a different folder. His guess was that the agent therefore treated the project as temporary. For a class demo the location did not matter. *(00:10:11)*

## 2. The default command: `CMD ["R"]` ([29.2.1 `CMD` or `ENTRYPOINT`?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#cmd-or-entrypoint))

*00:11:24–00:12:41*

- **Q:** The exercise only needed `FROM rocker/r-ver:4.6.2`. Why did Claude Code also add `CMD ["R"]`?
    - **A:** Claude reasoned that someone who picks an R container probably wants to do R things with it. So it made R the program that starts by default. *(00:11:44)*

- **Q:** What is the difference between the `FROM` line and the `CMD ["R"]` line in the warm-up `Dockerfile`?
    - **A:** `FROM rocker/r-ver:4.6.2` names the image you build on, and it was all the task required. `CMD ["R"]` only says what runs when you start the container without giving it any other input. It is a default, and you can always pass other parameters to start something that is not R. *(00:12:01)*

- **Q:** Explain the instructor's double-click analogy for `CMD`.
    - **A:** If the image were a file and you double-clicked it, `CMD` decides what opens. In this image, R opens by default. *(00:12:28)*

## 3. Listing and building images ([27.7 Image vs container?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#image-vs-container))

*00:12:42–00:16:40*

- **Q:** Why does `docker build --tag 2026-11-24-docker .` need the trailing `.`, and why is forgetting it a common mistake?
    - **A:** By default, `docker build` looks for a file named `Dockerfile`, but you still have to tell it where to look. The `.` means "where I currently am". It works like a function argument with no default: you can't leave it empty. The `.` is easy to miss because it looks like a full stop, but it is a location. *(00:14:57)*

- **Q:** What is the `--tag` value in `docker build --tag 2026-11-24-docker .` for, and what happens when you reuse an existing image's name?
    - **A:** The tag is the name you give the image, and it can be anything you like, even `pizza`. The instructor reused the name Claude had already built, `2026-11-24-docker`, so the build rebuilt and replaced that image. The `latest` that `docker images` shows is simply the tag Docker uses by default. *(00:14:03)*

- **Q:** Why did the rebuild of the R image finish almost instantly, and when would its `FROM` step take much longer?
    - **A:** The `rocker/r-ver:4.6.2` image had already been downloaded in the previous class, so nothing new had to happen. If you change to an R version you haven't downloaded yet, the `FROM` step has to pull that image first. That can take seconds or minutes, depending on your internet speed. *(00:16:15)*

## 4. Running a container, overriding `CMD`, and throwaway containers ([28.2.2 Docker `run` commands](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#docker-run-commands))

*00:16:40–00:20:07*

- **Q:** Explain what `--rm` and `-it` each do in `docker run --rm -it 2026-11-24-docker`.
    - **A:** `--rm` deletes the container when you exit, so it isn't left running on your computer. `-it` gives you terminal access and passes what you type through to the container. The image name at the end says which machine to start. *(00:16:53)*

- **Q:** How does `docker run --rm -it 2026-11-24-docker bash` differ from running the same command without `bash`?
    - **A:** Without `bash`, the container runs its default `CMD`, so R starts. Adding `bash` overrides that default and gives you a normal terminal, like Git Bash or the macOS terminal, with that kind of access to the Linux machine. *(00:17:45)*

- **Q:** Interpret what you saw after starting the container with `bash`: `pwd` printed `/` and `/home` was empty. Why didn't the instructor treat this as a problem for the course?
    - **A:** The container starts you at the root of the file system, so you see the system-level folders. There is no user set up in `/home`. In this course everyone uses the container as the same analysis setup, not as a service for the general public, so ownership of the container doesn't really matter. *(00:18:45)*

- **Q:** Why does `--rm` make a container a safe place to try something risky, such as installing PyTorch?
    - **A:** Once the container is closed, any changes you made inside it are gone, and the next start is clean again. The instructor compared it to a version of Git that automatically resets all your changes. If the experiment goes wrong, you restart the container and nothing bad has happened. *(00:19:58)*

## 5. Choosing a base image for a Python project ([29.3 Choosing a base image for your Dockerfile](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#choosing-a-base-image-for-your-dockerfile))

*00:20:07–00:24:22*

- **Q:** Why build the project's packages into the image instead of having each person install them?
    - **A:** The goal is that you can tell someone to pull the container, and once they run it they don't have to set anything up. Everything is already installed, apart from the bigger download. This works even for someone who has never used Python, or who sets things up differently. *(00:21:33)*

- **Q:** Why are you working in Linux inside a container, even on a Mac or Windows laptop?
    - **A:** Docker containers generally run on top of some version of Linux. So once you are inside a container you are in the Linux world, most likely some version of Ubuntu, whatever your own computer runs. *(00:23:33)*

- **Q:** Why did the new `Dockerfile` start `FROM ubuntu:24.04` rather than keep the R image?
    - **A:** The R image has a lot of R software installed that a Python project doesn't need, and the instructor wanted something smaller. He asked students to be respectful of other people's disk space, which has become expensive because of the AI boom. *(00:23:55)*

- **Q:** Compare Ubuntu with a smaller base image such as Alpine, as the instructor described them.
    - **A:** Alpine is even smaller than Ubuntu, but starting there may mean installing more yourself, depending on what you need. Ubuntu is a pretty good starting point for a lot of that software. *(00:24:13)*

- **Q:** Why does the textbook's example container hold both R and Python, when the class demo used only Python?
    - **A:** One project mixing several languages is common and valid. For example, the instructor likes ggplot2 and R's table tools. The class demo used only Python because every group is working on a Python project. *(00:22:42)*

## 6. Installing `uv` with `COPY --from`, and setting `WORKDIR` ([30.2 A `Dockerfile` for a uv project](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv.html#a-dockerfile-for-a-uv-project))

*00:24:22–00:27:42*

- **Q:** Interpret `COPY --from=ghcr.io/astral-sh/uv:0.13.7 /uv /uvx /usr/local/bin/`.
    - **A:** `COPY` can copy from one image into another. Read the image name like a GitHub path: who published it, the repository, then the version number. The line takes the `uv` and `uvx` programs out of that image and puts them in the container's `/usr/local/bin/` folder, which is how uv's own documentation installs uv. *(00:25:14)*

- **Q:** Why does the image need to install `uv` at all?
    - **A:** You are building a machine from scratch, as a virtual copy of your own machine. Everyone installed `uv` at orientation. So if you want to hand someone a reproducible environment, that machine needs `uv` too. *(00:25:46)*

- **Q:** Why add `WORKDIR /workspace` to the `Dockerfile`?
    - **A:** Without it, the container starts at the root of the file system, among operating-system files. If you moved a folder or messed something up there, everything could stop working. `WORKDIR` changes the working directory, so you start in a folder just for the project, and Docker creates the folder if it doesn't exist. *(00:26:27)*

- **Q:** Explain the instructor's point that the working-directory idea "will never go away".
    - **A:** Every command needs to know its starting point in some way. You met that idea in 521 and in reading files in your R and Python classes. Tools call it different things, such as `pwd`, `cd` or `WORKDIR`, but the idea of where you start stays. *(00:26:42)*

## 7. Setting up the `uv` project locally ([22.1 What `uv add` writes by default](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/virtual-environments-python-uv-exact-pins.html#what-uv-add-writes-by-default))

*00:27:42–00:29:58*

- **Q:** Explain how `pyproject.toml`, `uv sync` and `uv.lock` work together to install a package such as `cowsay`.
    - **A:** `pyproject.toml` lists the project and its dependencies. Running `uv sync` creates the `uv.lock` file from it. The lockfile is then what's used to install the packages. *(00:28:03)*

- **Q:** Why does the `uv` setup still have to work on your own computer before it goes into the image?
    - **A:** The image is built from files copied over from your computer. At this point the image only has `uv` installed, and what remains is getting the project's packages into the container. So the project files have to exist and work locally first, and the container then repeats the same process. *(00:28:18)*

- **Q:** Compare the two ways shown for adding `cowsay` as a dependency.
    - **A:** You can type it into the `dependencies` list of `pyproject.toml` by hand. Or, if you want to do everything with commands, you can run `uv add cowsay`. In class, `uv add cowsay` installed `cowsay==6.1` and wrote a `>=` bound for 6.1 into `pyproject.toml`. *(00:29:51)*

## 8. Pinning exact versions in `pyproject.toml` ([22.2 Why an analysis project declares exact versions](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/virtual-environments-python-uv-exact-pins.html#why-an-analysis-project-declares-exact-versions))

*00:29:58–00:33:35*

- **Q:** Why is a `>=` bound such as `cowsay>=6.1` risky in a project that runs for a long time?
    - **A:** It allows any newer version. If cowsay 7.0 comes out next week and you rebuild the container next week, you actually get 7.0. If your analysis relies on behaviour from 6.x, it can break without you changing anything. *(00:31:06)*

- **Q:** What does a change in the first number of a version, such as 6.x to 7.x, usually signal?
    - **A:** It typically means a change that breaks backwards compatibility. Some things that worked in the 6.x version no longer work in 7.x. *(00:30:37)*

- **Q:** Explain how the `[tool.uv]` table with `add-bounds = "exact"` fits into `pyproject.toml`.
    - **A:** `pyproject.toml` is a general Python metadata file that other tools also know how to read. The `[tool.uv]` table holds the settings that control how `uv` itself behaves. Setting `add-bounds = "exact"` there makes future `uv add` commands write `==` instead of `>=`. *(00:31:49)*

- **Q:** Compare the version information in `uv.lock` with the pins you write in `pyproject.toml`.
    - **A:** `uv.lock` always pins one specific version, but it is generated from the TOML file. `pyproject.toml` holds the explicit versions you care about. You pin those with `==` and let the resolver choose compatible versions for everything else. *(00:33:16)*

- **Q:** Why might you sometimes pin a package you never use directly?
    - **A:** A downstream dependency can still update on its own. The instructor has pinned pandas and still had something far downstream update and break pandas. In that case you add the downstream package to `pyproject.toml` and pin it as well. *(00:32:47)*

## 9. Copying the environment files and `uv sync --locked` ([30.7 When `uv.lock` does not match `pyproject.toml`](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv.html#when-uv.lock-does-not-match-pyproject.toml))

*00:35:01–00:39:25*

- **Q:** Why does `COPY pyproject.toml uv.lock .python-version ./` put the files in `/workspace`?
    - **A:** `./` means the current directory. The earlier `WORKDIR /workspace` line has already changed that directory to `/workspace`, so that is where the files land. *(00:35:09)*

- **Q:** Why does the project need a `.python-version` file when `uv.lock` already exists?
    - **A:** `uv.lock` only locks the packages and their dependencies. `.python-version` says which version of Python to install if the environment is built again, because you don't always want the latest one. The Python version also decides which package versions can be installed, since not every package is compatible with the newest Python. *(00:37:05)*

- **Q:** Give the instructor's example of why pinning the Python version matters.
    - **A:** PyTorch is almost never compatible with the latest version of Python. So to get the whole neural-network stack installed, you almost always have to pin an older Python version. *(00:35:59)*

- **Q:** Why is `.python-version` also useful to package authors?
    - **A:** A package author can point it at an upcoming Python release candidate. That creates an environment for checking that the package still works when Python actually updates. The instructor described this as part of an author's responsibility to the people who use the package. *(00:37:22)*

- **Q:** Summarize the role of each of the three files the `Dockerfile` copies.
    - **A:** `.python-version` says which version of Python to use. `uv.lock` says which packages to install and at which versions. `pyproject.toml` is the human-readable file that controls all of that. *(00:37:44)*

- **Q:** Why use `uv sync --locked` in the `Dockerfile` instead of plain `uv sync`?
    - **A:** `--locked` requires `pyproject.toml` and `uv.lock` to be in sync. If one of them is out of date, the build throws an error. That is what you want: the build happens the way you expect, or it fails loudly at that point. *(00:39:14)*

## 10. Building the image and layer caching ([29.1.3 Layer caching](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#layer-caching))

*00:39:25–00:44:33*

- **Q:** Why did the build of the Python image pause at the `RUN uv sync --locked` step?
    - **A:** That step really was running `uv sync --locked` inside the image. It is the same command you run on your own computer when you get a new project or a new homework assignment. Installing Python and the packages takes time. *(00:40:07)*

- **Q:** Why did the instructor use `ls -a` rather than `ls` to check `/workspace` in the new container?
    - **A:** Some of the files are hidden, such as `.python-version` and the `.venv` environment. Plain `ls` showed only `pyproject.toml` and `uv.lock`, while `ls -a` showed the copied files and the virtual environment too. *(00:41:03)*

- **Q:** Why do many `Dockerfile`s squeeze their work into as few instructions as possible, and does a beginner need to?
    - **A:** Each instruction is cached as its own layer, and combining steps saves a little disk space. It is about efficiency and doesn't really affect the outcome. So there is nothing wrong with having more lines while you are starting out, for example to keep environment steps separate from code steps. *(00:41:59)*

- **Q:** Explain why slow, rarely changing steps belong near the top of a `Dockerfile` and frequently changing files near the bottom.
    - **A:** When you change a layer, Docker has to rerun everything below it. If your code were copied before a slow install, fixing a typo in a script could make you wait for a reinstall such as a fifteen-minute tidyverse install. Putting the slow installs first and your code last avoids that. *(00:43:10)*

- **Q:** Interpret why the rebuild after adding `COPY hello.py ./` as the last line was so fast.
    - **A:** The new line came after everything else, so the earlier layers were reused from the cache and `uv sync` didn't have to run again. Only the new copy step ran, and copying a file is very fast. *(00:43:54)*

- **Q:** Compare handing someone your `Dockerfile` with publishing your image.
    - **A:** With the `Dockerfile`, they build the image themselves and end up with exactly your setup. With a published image, they just run `docker pull`, the way they would get any other image. They don't have to deal with the `Dockerfile` or with `docker build` at all. *(00:44:16)*

## 11. Why not bake your code into the image ([30.4 Run the project in a container](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv.html#run-the-project-in-a-container))

*00:49:36–00:53:26*

- **Q:** Why is copying your project code into the image a poor fit for work that is still changing, such as milestone EDA?
    - **A:** All the code is snapshotted into the image at build time. Anyone who opens the container then has to wonder when the code was copied, and which teammate copied it. *(00:50:27)*

- **Q:** Explain why the instructor called "copy everything in and rebuild" not scalable.
    - **A:** Every change would mean committing and pushing as usual, and also remembering to rebuild the image. Only then would the image hold the right version of each file. *(00:50:47)*

- **Q:** When did the instructor consider installing Git in the image and cloning the repository inside the container acceptable?
    - **A:** With only what students knew before this class, it is a valid approach, and he has used it himself. He has done it to build a container that mimics a student's terminal, where he really does want to clone something. He added that better ways exist for an analysis environment. *(00:51:51)*

- **Q:** What does "separate compute from source code" mean for the project's image?
    - **A:** The image only holds the installed software and packages, and the code stays outside it. That is why the `COPY hello.py ./` line was removed. *(00:52:21)*

- **Q:** Why do `pyproject.toml`, `uv.lock` and `.python-version` still have to be copied into the image, even though the code no longer is?
    - **A:** Those files are what actually build the environment. Without them, the image couldn't be built. *(00:52:30)*

- **Q:** Why did removing the `COPY hello.py ./` line still require rebuilding the image?
    - **A:** Deleting something from the `Dockerfile` is also a change to the image. You have to rebuild so that the step no longer runs and the file is no longer in the image. *(00:53:16)*

- **Q:** Why did the instructor stress paying attention to the terminal prompt during this part of the demo?
    - **A:** He was jumping between his laptop and the container. The prompt is how you know which machine you are typing commands into. *(00:52:59)*

## 12. Mounting the project folder with `-v` ([28.1.2 Mounting volumes to containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#mounting-volumes-to-containers))

*00:53:26–00:59:33*

- **Q:** Explain what `-v` (`--volume`) does when you run a container.
    - **A:** It mounts a volume: a folder on your computer appears inside the container. It works like a shared drive, so changes made inside the container are also on your computer. It isn't a Google Drive-style sync. You are literally working on the same file, so you can't clobber your own work. *(00:55:34)*

- **Q:** Interpret `-v "$(pwd):/workspace"` in `docker run --rm -it -v "$(pwd):/workspace" 2026-11-24-docker bash`.
    - **A:** In Bash, the dollar sign pulls in a special variable or command, here `pwd`, so `$(pwd)` is your current working directory. The flag takes that folder and places it at `/workspace` in the container. On Windows you may need an extra slash, which the textbook shows. *(00:57:13)*

- **Q:** Why did the `my_secrets.txt` demo need a second step to show that a mount differs from copying?
    - **A:** At first the file simply appeared in the container, which looked as if the instructor had copied everything in. Then he added a line ("i eat baby food.") on his laptop, and `cat` in the container showed the new line straight away. That proved the container was live-updating from the shared folder. *(00:58:53)*

- **Q:** Why is mounting the folder better than installing Git inside the container?
    - **A:** Git in a container needs its own SSH key or personal access token to push and pull. Every time the container is built, you would create a new key and have to register it again. Mounting avoids all of that, because Git keeps running on your laptop, where 521 already solved the problem. *(00:55:24)*

- **Q:** Why is the folder mounted at `docker run` rather than set up during `docker build`?
    - **A:** During the build, all you can do is copy. Only when the container runs can you say "take this folder and sync it in this other location". *(00:56:13)*

- **Q:** With the project mounted, why is it still worth running `uv run hello.py` (for your milestone, `uv run quarto render`) inside the container?
    - **A:** Your changes still show up inside the container, so you can check that the code runs the way the container is set up. That gives you tests that your work runs on your local machine and in the container. *(00:59:06)*

- **Q:** Why might Positron show an old version of a file that was changed through the mount?
    - **A:** Positron sometimes doesn't notice that a file was updated on disk, so you have to refresh it. That is an editor problem, separate from the mount itself, which is a live sync. *(00:55:59)*

## 13. Keeping the image's environment in `/opt/venv` ([30.5 Why the packages go in `/opt/venv`](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv.html#why-the-packages-go-in-optvenv))

*00:59:33–01:06:53*

- **Q:** Explain what the `.venv` folder holds, and why `python` gave `command not found` in the container while `uv run` worked.
    - **A:** `.venv` holds the actual Python binary and the packages for the project. Plain `python` doesn't exist on the container's system. `uv` knows to look in the project's environment folder, so Python is reached through `uv run`. *(01:00:15)*

- **Q:** Why does a mounted `.venv` become a problem when you work in a group?
    - **A:** Teammates can be on different operating systems (Windows, macOS, Linux) and different CPU architectures (AMD64 and ARM64), which gives up to six different kinds of computer. The image was built under Linux, but the mount covered `/workspace` with your laptop's `.venv`. The instructor compared it to copying a program from your Mac onto Windows and hoping it works. *(01:02:40)*

- **Q:** If `uv.lock` records packages for every operating system, why doesn't your laptop's `.venv` work everywhere?
    - **A:** The lockfile has the information for all the other operating systems, but `uv sync` only installs for the system it is running on. A Mac has no reason to install the Windows versions, and sometimes they aren't even compatible. *(01:01:42)*

- **Q:** Which kinds of packages are most likely to break when an environment moves between systems?
    - **A:** Anything that "runs fast" in Python, or that is compiled or has some C code. pandas is likely to be a problem, while cowsay is too simple to show it. *(01:02:33)*

- **Q:** Interpret the output of `uv run hello.py` in the mounted container before the `ENV` line was added: "Ignoring existing virtual environment linked to non-existent Python interpreter" and then "Removed virtual environment at: .venv".
    - **A:** `uv` found the Mac's `.venv` through the mount and saw that it pointed to a macOS Python that doesn't exist in the container. It then deleted that `.venv` and created a new Linux one. Treat this as a warning: the mount is the same folder as on your laptop, so the container replaced your own computer's environment. *(00:59:06)*

- **Q:** How does `ENV UV_PROJECT_ENVIRONMENT=/opt/venv` fix the mounted-`.venv` problem?
    - **A:** It tells `uv` where to save the environment and where to look for it. The environment then lives in `/opt/venv` instead of `.venv`, so `uv` ignores the mounted local `.venv`. The packages in `/opt/venv` were installed with the Linux dependencies at build time, so the image works whichever computer the project folder comes from. *(01:04:46)*

- **Q:** Why must the `ENV` line come before `RUN uv sync --locked`, and why did the next build rerun `uv sync`?
    - **A:** The variable has to be set when `uv sync` runs, so that the environment is created in `/opt/venv`. Apart from that, its position doesn't matter. Adding the line was a change higher up in the `Dockerfile`, so every step below it, including `uv sync --locked`, had to run again. *(01:05:33)*

- **Q:** What does `uv run which python` printing `/opt/venv/bin/python` in the mounted container show?
    - **A:** It shows that `uv` now uses the image's own environment in `/opt/venv` and no longer looks in `.venv`. The Linux container runs its Linux stack, your laptop keeps its own environment, and the container stays portable across operating systems. *(01:06:37)*

## 14. Docker Compose ([33.1 Docker Compose to launch containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-docker-compose.html#docker-compose-to-launch-containers))

*01:06:53–01:14:06*

- **Q:** Why did the instructor bring in a `docker-compose.yml` file?
    - **A:** The `docker run` command keeps getting longer: `--rm`, `-it`, `-v`, and a `-p` port for tools like JupyterLab or RStudio. A pasted command is hard to edit because you can't click into it and have to arrow across. A file can be version controlled, its changes are tracked, and you run short commands instead of copying and pasting. *(01:11:46)*

- **Q:** What is Docker Compose mainly designed for, and why is it still useful with one container?
    - **A:** It runs several containers at the same time. For example, a dashboard and the database it reads from are kept separate, because some people only care about the database. With one container it is a little overkill, but it still records all the run settings in a file. *(01:09:04)*

- **Q:** Interpret each line of the class's `docker-compose.yml`: `services:`, `analysis-env:`, `build: .`, `image: 2026-11-24-docker` and `volumes: - .:/workspace`.
    - **A:** `services:` lists the containers, and `analysis-env` is just the name of this one (it could be `pizza`). `build: .` builds from the `Dockerfile` in the current folder, and `image:` names the resulting image. `volumes:` mounts the current folder at `/workspace`, like `-v`. *(01:10:25)*

- **Q:** How does `docker compose build` differ from the `docker build` and `docker run` commands used earlier in the session?
    - **A:** Before, you typed `docker build` and then a long `docker run` with all its flags. `docker compose build` reads the compose file and builds whatever it specifies. The file acts as all the flags of the `docker run` command. *(01:11:09)*

- **Q:** What does `--detach` (`-d`) do in `docker compose up --detach`?
    - **A:** It turns the container on and runs it in the background, so the container keeps running while you get your terminal back. The instructor noted it isn't very useful for this particular container. *(01:12:14)*

- **Q:** What was the live `docker compose up` demo meant to show, and what happened instead?
    - **A:** Compose should have read the file as the flags of the earlier `docker run` command and started that container. Instead the terminal showed `analysis-env-1 exited with code 0`, and `docker compose ps` listed nothing running. The instructor did not resolve this in class and said he would fix the demo for next class. *(01:13:50)*

## 15. This week's milestone: a Dockerfile for your analysis

*01:14:06–01:17:04*

- **Q:** Explain how the TAs will check your milestone `Dockerfile`, and what that check proves.
    - **A:** The TAs take your repository, build a container from it, and try to run the analysis in that container, for example `uv run quarto render` on your report. That checks the goal of the course: a reproducible compute environment, where a file or image holds everything that needs to be installed. *(01:15:09)*

- **Q:** Why might you add extra `RUN` lines for a text editor to your image?
    - **A:** The image from class had no text editor, which is why the instructor couldn't edit a file inside the container. An editor lets you quickly change or look at files in the container. It is optional, and you should know why you add each extra line. *(01:15:41)*

- **Q:** Give the instructor's example of why some projects need system tools installed from Ubuntu.
    - **A:** Some Python packages need system tools underneath them. Geospatial analysis is the example: its packages are built on system libraries that you may have to install in the image. What you need depends on the tool stack your project uses. *(01:16:16)*

## 16. Docker Compose outside the course

*01:17:04–01:20:07*

- **Q:** Why does knowing Docker Compose help you use open-source tools outside MDS?
    - **A:** Many open-source tools already ship a Compose file. Someone else has set up the machine and the software, so you don't have to work out how to install it. If you know your way around Docker, you run `docker compose up` and the tool runs. *(01:19:44)*

- **Q:** Interpret the parts of the Actual Budget Compose file shown in class.
    - **A:** Under `services` there is one container, called `actual server`. It comes from a published image and has ports, environment variables, volumes, and a health check that keeps the server alive. `docker compose up -d` downloads the image and runs the software, and you then connect to that port to use your own personal finance app. *(01:18:29)*

- **Q:** How do tools such as Jellyfin, n8n or a recipe manager run once you start them with Compose, and where can they run?
    - **A:** They are web applications that run on a port and are used in a browser, just like RStudio. They can run on any machine you choose, from an old laptop in a closet to a cloud machine you pay for monthly. This is why containers are a useful skill beyond compute environments. *(01:19:34)*

---

- prompt: prompt-recall-2-understand.md @ 65eb21c
- prompt-hash: 17df43f38e78
- model: claude-opus-5-5 (requested: opus)
- backend: claude
- inputs: transcript-plaud.md, terminal.txt, materials.md, notes-class-main--claude-opus-5-5.md
- generated: 2026-11-24
- notes-input: notes-class-main--claude-opus-5-5.md @ 0caf0d47e007, links and section references removed
