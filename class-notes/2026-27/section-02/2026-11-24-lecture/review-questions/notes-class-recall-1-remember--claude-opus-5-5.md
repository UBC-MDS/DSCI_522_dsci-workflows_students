# Building a Python analysis image with uv, volume mounts and Docker Compose: review questions, tier 1 — Remember

Date: 2026-11-24

Instructor: Daniel Chen

*Tier 1 of 5: Remember. Answer each question before you read its answer; tiers 2 to 5 build on these.*

## 1. Warm-up exercise: a Dockerfile from a given image

*00:00:00–00:04:30*

- **Q:** What did the first exercise of the day ask students to create?
    - **A:** A GitHub repository with a `Dockerfile` that uses a particular given image. It was review from the previous class. *(00:00:00)*

- **Q:** According to the instructor, how much of a file did the warm-up solution need?
    - **A:** Essentially one line in one file, in a new repository. *(00:04:19)*

- **Q:** What did the instructor do with the same warm-up task while students worked on it?
    - **A:** He gave it to a coding agent (Claude) to see what it would produce. *(00:00:17)*

- **Q:** What base image did the warm-up `Dockerfile` in the demo repository `2026-11-24-docker` build from?
    - **A:** `rocker/r-ver:4.6.2`, the same R version the class worked with last class. *(00:15:45)*

- **Q:** What did the instructor say the warm-up exercise was for?
    - **A:** It was a way to set up the rest of the class, which builds on that repository. *(00:04:25)*

## 2. Course website updates and a Docker Desktop reminder

*00:04:30–00:07:21*

- **Q:** Where can students now find the summary lecture notes?
    - **A:** On the course website. You no longer have to look in the GitHub UBC student repo for them. *(00:04:58)*

- **Q:** What format does the other instructor of the course teach from, and where can you find it?
    - **A:** Slide decks. They are linked on the course website. *(00:04:54)*

- **Q:** Which lecture materials stay on the private side, rather than the course website?
    - **A:** The transcript and the link. The site has only the summary. *(00:05:11)*

- **Q:** What did the instructor say you can compare across the summary notes?
    - **A:** Summaries produced by different language models. *(00:05:24)*

- **Q:** The lecture question-and-answer sets are written at different levels of which learning framework?
    - **A:** Bloom's taxonomy. They range from basic factual questions to questions that need you to know what is going on under the hood. *(00:05:48)*

- **Q:** Which page of the course site is for students who only want the commands that were run?
    - **A:** The command history page. *(00:06:40)*

- **Q:** What must be running on your computer before any `docker` command will work?
    - **A:** Docker Desktop. Without it, any Docker command you run will fail. *(00:07:00)*

## 3. Letting Claude Code build the repository

*00:07:21–00:11:24*

- **Q:** What name did the instructor give the new demo repository?
    - **A:** `2026-11-24-docker`. *(00:07:21)*

- **Q:** Which two programs did the coding agent check for on the instructor's computer before it built anything?
    - **A:** `docker` and `gh`. *(00:09:16)*

- **Q:** Which shell command did the coding agent run to make the repository's folder?
    - **A:** `mkdir`. *(00:09:26)*

- **Q:** In which folder did the coding agent create `2026-11-24-docker`?
    - **A:** In the temp folder (`~/temp/2026-11-24-docker`), not in the Git folder the instructor wanted. *(00:08:38)*

- **Q:** Besides the `Dockerfile`, which two files did the coding agent create without being asked in this prompt?
    - **A:** A `README.md` and a `Makefile`. The instructor usually asks for these, so the agent knew to make them. *(00:11:24)*

- **Q:** What did the coding agent do after writing the `Dockerfile`?
    - **A:** It built the container and ran a script in it to test it. *(00:10:37)*

- **Q:** How much did the coding agent's run cost?
    - **A:** Fifty cents. *(00:10:55)*

- **Q:** What did the instructor say you must already know before you can prompt a coding agent to build a Docker image well?
    - **A:** The tooling vocabulary and jargon, such as Dockerfile, image and the exact image name. Without it, you can't steer the agent toward the correct answer. *(00:08:06)*

## 4. The default command: `CMD ["R"]` ([29.2.1 `CMD` or `ENTRYPOINT`?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#cmd-or-entrypoint))

*00:11:24–00:12:41*

- **Q:** Which line did Claude add to the warm-up `Dockerfile`, beyond what the task required?
    - **A:** `CMD ["R"]`. *(00:11:44)*

- **Q:** What does `CMD ["R"]` do when you run the container without any other inputs?
    - **A:** It starts R by default. *(00:12:01)*

- **Q:** What analogy did the instructor use for an image's default command?
    - **A:** If the image were a file and you double-clicked it, the default command decides what opens. Here, R opens. *(00:12:28)*

- **Q:** Can you run something other than R in a container from an image whose default command is R?
    - **A:** Yes. You can always give it other parameters to turn on something other than R. *(00:12:19)*

## 5. Listing and building images ([29 Customizing and building containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html))

*00:12:42–00:16:40*

- **Q:** Which command lists the images on your computer?
    - **A:** `docker images`. *(00:13:03)*

- **Q:** Which tag did the image `2026-11-24-docker` have when Claude built it?
    - **A:** `latest`, the tag Docker uses by default. *(00:13:03)*

- **Q:** Which command did the instructor use to rebuild the `2026-11-24-docker` image by hand?
    - **A:** `docker build --tag 2026-11-24-docker .` *(00:13:56)*

- **Q:** What is the short form of `docker build`'s `--tag` flag?
    - **A:** `-t`. *(00:14:00)*

- **Q:** Does the name you give `docker build --tag` have to be anything in particular?
    - **A:** No. You can give it any name you want, even `pizza`. *(00:14:13)*

- **Q:** Which file does `docker build` look for by default?
    - **A:** A file named `Dockerfile`, with a capital D. *(00:14:46)*

- **Q:** What does the `.` at the end of `docker build --tag 2026-11-24-docker .` stand for?
    - **A:** Your current location, "here": that is where Docker should look for the `Dockerfile`. The instructor warned that it is not a period or full stop, and you can't leave it out. *(00:15:31)*

- **Q:** How long does the `FROM` step of a build take when you haven't downloaded the base image yet?
    - **A:** A couple of seconds or minutes, depending on your internet speed, while Docker pulls it. *(00:16:15)*

- **Q:** Which image did the instructor say you need some version of for this week's milestone?
    - **A:** The R image from last class (`rocker/r-ver`), the image the warm-up `Dockerfile` pulls from. *(00:15:45)*

## 6. Running a container, overriding `CMD`, and throwaway containers ([28.2 Docker command-line commands](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#docker-command-line-commands))

*00:16:40–00:20:07*

- **Q:** What does the `--rm` flag of `docker run` do?
    - **A:** It deletes the container when you exit, so the container isn't left running on your computer. *(00:16:40)*

- **Q:** What does the `-it` flag of `docker run` do?
    - **A:** It gives you terminal access to the container and passes what you type through to that machine. *(00:16:53)*

- **Q:** What started when the instructor ran `docker run --rm -it 2026-11-24-docker` on the warm-up image?
    - **A:** R. The terminal printed R version 4.6.2 because of the `CMD ["R"]` line. *(00:17:17)*

- **Q:** What did the instructor add after the image name to get a shell instead of R?
    - **A:** `bash`, as in `docker run --rm -it 2026-11-24-docker bash`. It overrides the default command. *(00:17:45)*

- **Q:** Where in the file system does a shell in the `rocker/r-ver` container start?
    - **A:** At the root of the computer: `pwd` printed `/`. *(00:18:12)*

- **Q:** What did the instructor find in the container's `/home` directory?
    - **A:** Nothing. No user is assigned in this image. *(00:18:36)*

- **Q:** What happens to the changes you made inside a container started with `--rm` after you exit?
    - **A:** They are gone. When you go back in, any changes have undone themselves. *(00:19:29)*

- **Q:** What did the instructor compare a throwaway container to?
    - **A:** A version of Git that automatically resets all of your changes. *(00:19:29)*

- **Q:** What risky installation did the instructor suggest trying in a container first?
    - **A:** Installing PyTorch. If it goes wrong, you restart the container and nothing bad has happened. *(00:19:50)*

## 7. Choosing a base image for a Python project ([29.3 Choosing a base image for your Dockerfile](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#choosing-a-base-image-for-your-dockerfile))

*00:20:07–00:24:22*

- **Q:** How many students said they were working on an R project?
    - **A:** None. Everyone is on a Python project, so the demo focused on Python. *(00:20:27)*

- **Q:** What did the instructor want someone to be able to do with the finished project image?
    - **A:** Pull the container and run it without setting anything up, apart from the bigger download, because everything is already installed. *(00:21:18)*

- **Q:** Which languages does the Docker container in the textbook's example have?
    - **A:** R and Python, at the same time. *(00:22:26)*

- **Q:** Which R package did the instructor name as a reason he might mix languages in one project?
    - **A:** ggplot2. Projects that mix several languages are common and valid. *(00:22:42)*

- **Q:** Which operating system do Docker containers run on, even on Mac and Windows computers?
    - **A:** Some version of Linux, most likely some version of Ubuntu. *(00:23:16)*

- **Q:** Which base image did the new Python `Dockerfile` start from?
    - **A:** `ubuntu:24.04`. *(00:23:42)*

- **Q:** Why did the instructor say not to keep using the R image as the base for a Python project?
    - **A:** It has a lot of R software installed, and he wanted a smaller image. Disk space is expensive because of the AI boom, so be respectful of other people's. *(00:23:55)*

- **Q:** Which base image did the instructor name as even smaller than Ubuntu?
    - **A:** Alpine. You might have to install more yourself, depending on what you need. *(00:23:55)*

## 8. Installing `uv` with `COPY --from`, and setting `WORKDIR` ([30 Python packages with uv in an image](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv.html))

*00:24:22–00:27:42*

- **Q:** Which `Dockerfile` instruction, new this class, can copy files from one image into another?
    - **A:** `COPY`. *(00:24:38)*

- **Q:** What line did the class use to install `uv` in the image?
    - **A:** `COPY --from=ghcr.io/astral-sh/uv:0.13.7 /uv /uvx /usr/local/bin/` *(00:24:53)*

- **Q:** Which two programs does the `COPY --from=ghcr.io/astral-sh/uv:0.13.7` line copy, and to where?
    - **A:** `uv` and `uvx`, into the container's `/usr/local/bin` folder. *(00:24:53)*

- **Q:** Where did the `COPY --from` line for installing `uv` come from?
    - **A:** Straight out of the textbook and the uv documentation. *(00:24:24)*

- **Q:** When did everyone in the class install `uv` on their own computer?
    - **A:** At orientation. *(00:25:41)*

- **Q:** Which `Dockerfile` instruction changes the container's working directory?
    - **A:** `WORKDIR`, for working directory. *(00:26:42)*

- **Q:** Which working directory did the class set in the Python `Dockerfile`?
    - **A:** `/workspace`, a folder called workspace in the root directory. *(00:27:15)*

- **Q:** What does `WORKDIR /workspace` do if the folder doesn't exist?
    - **A:** It makes the folder. *(00:27:23)*

## 9. Setting up the `uv` project locally ([30 Python packages with uv in an image](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv.html))

*00:27:42–00:29:58*

- **Q:** Which command created the demo project's `pyproject.toml`?
    - **A:** `uv init --bare`. *(00:28:32)*

- **Q:** Which file does `uv sync` create from `pyproject.toml`?
    - **A:** `uv.lock`, which is then used to install the packages. *(00:28:03)*

- **Q:** What Python requirement did `uv init --bare` write into `pyproject.toml`?
    - **A:** Python 3.14 or newer (`requires-python = ">=3.14"`). *(00:29:07)*

- **Q:** Besides typing a dependency into `pyproject.toml` by hand, which command adds cowsay to the project?
    - **A:** `uv add cowsay`. *(00:29:38)*

- **Q:** Which version of cowsay did `uv add cowsay` install?
    - **A:** 6.1 (`cowsay==6.1`). *(00:29:45)*

- **Q:** What did `uv add cowsay` write into `pyproject.toml` by default?
    - **A:** `cowsay>=6.1`, a "greater or equal" bound. *(00:29:51)*

## 10. Pinning exact versions in `pyproject.toml` ([22 uv: pinning exact versions](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/virtual-environments-python-uv-exact-pins.html))

*00:29:58–00:33:35*

- **Q:** With `cowsay>=6.1` in `pyproject.toml`, what happens if cowsay 7.0 comes out next week and you rebuild the container then?
    - **A:** You get 7.0: the package updates. *(00:30:17)*

- **Q:** What does a change in the first number of a package's version typically mean?
    - **A:** A backwards-compatibility-breaking change: things in 6.x may no longer work in 7.x. *(00:30:37)*

- **Q:** Which later MDS course did the instructor say covers version numbers in more depth?
    - **A:** DSCI 524. *(00:30:32)*

- **Q:** What warning did the instructor give about `>=` bounds in a long-running project?
    - **A:** If you use "greater or equal" and the project runs a long time, there is a chance it will break when a new major version comes in. *(00:30:51)*

- **Q:** Which operator pins a package to one exact version in `pyproject.toml`?
    - **A:** `==` ("double equal"), as in `cowsay==6.1`. *(00:31:06)*

- **Q:** Which setting in the demo's `pyproject.toml` makes `uv add` write `==` instead of `>=`?
    - **A:** `add-bounds = "exact"`, in the `[tool.uv]` table. *(00:31:31)*

- **Q:** How did the instructor describe `pyproject.toml`?
    - **A:** A general Python metadata file that other tools know how to read. Its `[tool.uv]` part controls how `uv` behaves. *(00:31:37)*

- **Q:** What does `uv.lock` always record for each package, and which file is it created from?
    - **A:** One specific version. It is created from the `pyproject.toml` file. *(00:32:26)*

- **Q:** What happened to the instructor even after he pinned pandas to a particular version?
    - **A:** Something far downstream updated and broke pandas, so he had to pin and roll back that package too. *(00:32:47)*

## 11. Running a script with the project environment ([30 Python packages with uv in an image](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv.html))

*00:33:35–00:35:01*

- **Q:** What code is in the demo's `hello.py`?
    - **A:** `import cowsay`, then `cowsay.cow("hello, moo.")`. *(00:33:49)*

- **Q:** Which two `uv` commands set up the environment and ran `hello.py` on the laptop?
    - **A:** `uv sync`, then `uv run hello.py`. *(00:34:07)*

- **Q:** What did `uv run hello.py` print?
    - **A:** "hello, moo." in a speech bubble from an ASCII cow picture. *(00:34:20)*

- **Q:** What did the instructor say happens if a setup step isn't in the `Dockerfile`?
    - **A:** He can't build the image, and if he can't build the image, he can't give it to the class. *(00:34:45)*

## 12. Copying the environment files and `uv sync --locked` ([30 Python packages with uv in an image](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv.html))

*00:35:01–00:39:25*

- **Q:** Which `COPY` line brings the project's environment files into the image?
    - **A:** `COPY pyproject.toml uv.lock .python-version ./` *(00:35:09)*

- **Q:** Which folder does `./` refer to in `COPY pyproject.toml uv.lock .python-version ./`?
    - **A:** `/workspace`, because `WORKDIR` already changed to that directory. *(00:35:09)*

- **Q:** What does the `.python-version` file tell `uv`?
    - **A:** Which version of Python to install. *(00:36:38)*

- **Q:** What does the demo's `.python-version` file contain?
    - **A:** `3.14`. *(00:36:30)*

- **Q:** Which package did the instructor name as almost never compatible with the latest version of Python?
    - **A:** PyTorch. You almost always have to pin an older Python to install it. *(00:35:59)*

- **Q:** How can a package author use `.python-version` with upcoming Python releases?
    - **A:** To create an environment with an upcoming release candidate, to make sure the package works when Python updates. *(00:37:05)*

- **Q:** Name the three environment files the `Dockerfile` copies, and what each one is for.
    - **A:** `.python-version` gives the Python version. `uv.lock` gives the packages and their versions. `pyproject.toml` is the human-readable file that controls them. *(00:37:44)*

- **Q:** Which `RUN` instruction installs Python and the packages in the image?
    - **A:** `RUN uv sync --locked`. *(00:38:03)*

- **Q:** What does the `--locked` flag of `uv sync` do?
    - **A:** It requires `pyproject.toml` and `uv.lock` to be in sync. If one is out of date, it throws an error. *(00:38:55)*

## 13. Building the image and layer caching ([29.1.3 Layer caching](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#layer-caching))

*00:39:25–00:44:33*

- **Q:** Which key recalls a command you've already typed in the terminal?
    - **A:** The up arrow. *(00:39:29)*

- **Q:** At which step did the first build of the Python image pause?
    - **A:** The `RUN uv sync --locked` step. *(00:40:07)*

- **Q:** Where did a shell in the new Python container start?
    - **A:** In `/workspace`, because of `WORKDIR`. *(00:40:54)*

- **Q:** What did `ls -a` show in `/workspace` in the Python image?
    - **A:** `.python-version`, `.venv`, `pyproject.toml` and `uv.lock`. *(00:41:03)*

- **Q:** What does Docker do with each instruction in a `Dockerfile` when it builds?
    - **A:** It saves each one as a layer and caches it. An unchanged layer reuses the cached version. *(00:41:35)*

- **Q:** Is it wrong for a beginner's `Dockerfile` to have more lines than it needs?
    - **A:** No. Fewer instructions only save a little space; they don't change the outcome. *(00:41:59)*

- **Q:** What happens to the later steps when you change one layer of a `Dockerfile`?
    - **A:** Docker has to rerun everything downstream of it. *(00:42:33)*

- **Q:** Which R installation did the instructor say can take fifteen minutes?
    - **A:** The tidyverse, depending on how you install it. *(00:43:10)*

- **Q:** Which line did the instructor add to the end of the `Dockerfile` to put the script in the image?
    - **A:** `COPY hello.py ./` *(00:43:33)*

- **Q:** Why was the rebuild after adding `COPY hello.py ./` so fast?
    - **A:** It didn't have to run `uv sync` again, and copying a file is very fast. *(00:43:49)*

- **Q:** Which command will let someone get a published image without building it from the `Dockerfile`?
    - **A:** `docker pull`. *(00:44:16)*

## 14. Why not bake your code into the image

*00:49:36–00:53:26*

- **Q:** What happens to your code if you copy all of it into the image?
    - **A:** It is snapshotted into the container. Anyone opening it has to worry about when the code was copied and which teammate copied it. *(00:50:27)*

- **Q:** Which steps does every code change require if your code is copied into the image?
    - **A:** Git commit and push, then copying everything into the image and rebuilding it so it holds the right version of each file. *(00:50:47)*

- **Q:** What other approach did the instructor call valid with what students knew before this class?
    - **A:** Installing Git in the container and cloning the repository from inside it. *(00:51:21)*

- **Q:** What did the instructor name as the goal for separating the image from the project?
    - **A:** Separating compute from source code: the container holds only the installed software and packages. *(00:52:14)*

- **Q:** Which line did the instructor remove from the `Dockerfile`, and which files did he keep copying?
    - **A:** He removed the line copying `hello.py`. He kept copying the environment files, because the container can't be built without them. *(00:52:21)*

- **Q:** What should you watch to know which machine you are typing commands into?
    - **A:** The terminal prompt. *(00:52:53)*

- **Q:** Does deleting a line from a `Dockerfile` mean you have to rebuild the image?
    - **A:** Yes. Deleting something is a change to the container, so you must rebuild. *(00:53:05)*

## 15. Mounting the project folder with `-v` ([28.1.2 Mounting volumes to containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#mounting-volumes-to-containers))

*00:53:26–00:59:33*

- **Q:** What does the `-v` flag of `docker run` stand for?
    - **A:** `--volume`. *(00:53:48)*

- **Q:** What is the technical term for what `-v` does?
    - **A:** Mounting a volume: a folder from your computer appears in the container when it runs. *(00:54:05)*

- **Q:** What did the instructor compare a mounted folder to?
    - **A:** A shared drive. It is not like a Google Drive sync: you are working on the same file. *(00:55:34)*

- **Q:** Which Git credentials does mounting save you from setting up inside a container?
    - **A:** An SSH key or a personal access token. A key made in the container would be made new every time it rebuilds. *(00:54:52)*

- **Q:** Does mounting a folder happen when you build an image or when you run a container?
    - **A:** When you run it. A build can only copy. *(00:56:06)*

- **Q:** What does `$` do in Bash, as in `$(pwd)`?
    - **A:** It pulls up a special variable or command. `$(pwd)` gives the current working directory. *(00:56:50)*

- **Q:** What command did the instructor use to mount the project folder into the container?
    - **A:** `docker run --rm -it -v "$(pwd):/workspace" 2026-11-24-docker bash` *(00:57:13)*

- **Q:** What might Windows users need to add to the mount path?
    - **A:** A slash. The textbook shows when you need it. *(00:56:34)*

- **Q:** What file did the instructor create on the laptop to test the mount, and what did it say first?
    - **A:** `my_secrets.txt`, containing "i'm afraid of the dark." *(00:57:23)*

- **Q:** What happened when the instructor tried `nano my_secrets.txt` and `vi my_secrets.txt` in the container?
    - **A:** Both failed with `command not found`: the container has no text editor. *(00:58:06)*

- **Q:** What happened in the container when the instructor added "i eat baby food." to `my_secrets.txt` on the laptop?
    - **A:** `cat` in the container showed the new line straight away: the mount updates live. *(00:58:53)*

- **Q:** Which editor did the instructor say sometimes misses that a file changed on disk?
    - **A:** Positron. You may have to tell it to refresh. *(00:55:51)*

## 16. Keeping the image's environment in `/opt/venv` ([30.5 Why the packages go in `/opt/venv`](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv.html#why-the-packages-go-in-optvenv))

*00:59:33–01:06:53*

- **Q:** What does the `.venv` folder contain?
    - **A:** The actual Python binary and the packages installed for the project. *(00:59:52)*

- **Q:** What happened when the instructor ran plain `python` in the container?
    - **A:** `bash: python: command not found`. Python has to be run through `uv`, which knows where to look. *(01:00:08)*

- **Q:** Which two CPU architectures did the instructor name?
    - **A:** AMD64 and ARM64. *(01:00:45)*

- **Q:** How many combinations of operating system and CPU architecture did the instructor count for a team?
    - **A:** Four for Windows and Mac, and six if a teammate is on Linux. *(01:01:08)*

- **Q:** Which file records packages for other operating systems, even though `uv sync` installs only for yours?
    - **A:** `uv.lock`. *(01:01:22)*

- **Q:** Which kinds of packages did the instructor say are where cross-platform problems show up?
    - **A:** Compiled packages with C code, anything that "runs fast" in Python, such as pandas. *(01:02:15)*

- **Q:** What did `uv run hello.py` print about `.venv` when the instructor ran it in the mounted container, before the fix?
    - **A:** That it ignored the existing virtual environment linked to a missing interpreter, then "Removed virtual environment at: .venv" and created a new one. It replaced the laptop's `.venv` in the shared folder. *(00:59:06)*

- **Q:** What warning did the instructor give about running the container with the laptop's `.venv` mounted?
    - **A:** It amounts to copying the versions on your computer onto another operating system and hoping they work. Like opening a Mac file on Windows, that is not how things work. *(01:02:40)*

- **Q:** Which environment variable tells `uv` where to put the project environment?
    - **A:** `UV_PROJECT_ENVIRONMENT`. *(01:04:01)*

- **Q:** What value did the class give `UV_PROJECT_ENVIRONMENT`, and what is the default location it replaces?
    - **A:** `/opt/venv`, in place of the default `.venv`. *(01:04:13)*

- **Q:** Where in the `Dockerfile` must the `ENV UV_PROJECT_ENVIRONMENT=/opt/venv` line go?
    - **A:** The order doesn't matter, as long as it comes before `uv sync`. *(01:03:56)*

- **Q:** What did `uv which python` print in the container?
    - **A:** `error: unrecognized subcommand 'which'`. *(01:06:00)*

- **Q:** What did `uv run which python` print in the mounted container after the fix?
    - **A:** `/opt/venv/bin/python`: it no longer looks in `.venv`. *(01:06:20)*

## 17. Docker Compose ([33 Containers: Docker Compose](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-docker-compose.html))

*01:06:53–01:14:06*

- **Q:** Which `docker run` flag might you need for JupyterLab or RStudio, making the command longer still?
    - **A:** `-p`, to forward a port. *(01:07:09)*

- **Q:** What is the file name of a Docker Compose file, and what format is it in?
    - **A:** `docker-compose.yml`, a YAML file. *(01:08:10)*

- **Q:** What is Docker Compose mainly for, beyond one container?
    - **A:** Running several containers at the same time, as with microservices, such as a dashboard and the database it reads from. *(01:09:04)*

- **Q:** Which key does a compose file begin with?
    - **A:** `services`. *(01:09:31)*

- **Q:** What name did the class's `docker-compose.yml` give its one service?
    - **A:** `analysis-env`. You could call it `pizza` if you wanted. *(01:09:43)*

- **Q:** What does `build: .` in the class's `docker-compose.yml` tell Compose?
    - **A:** To build from the `Dockerfile` in the current location. *(01:09:51)*

- **Q:** Which container port did the instructor give as the example for an RStudio container?
    - **A:** `8787`. *(01:10:15)*

- **Q:** Which entry of the class's `docker-compose.yml` replaces `-v`?
    - **A:** `volumes`, which mounts the current working directory at `/workspace`. *(01:10:25)*

- **Q:** Which command reads `docker-compose.yml` and builds the image?
    - **A:** `docker compose build`. *(01:11:09)*

- **Q:** What advantages did the instructor give for keeping run options in a file instead of a pasted command?
    - **A:** Files can be version controlled, and changes can be tracked. *(01:11:28)*

- **Q:** Which command starts a compose container in the background, and what does `-d` stand for?
    - **A:** `docker compose up -d`; `-d` stands for detach, and you get your prompt back. *(01:11:59)*

- **Q:** What happened when the instructor ran `docker compose up` in class?
    - **A:** It created the network and container, then printed `analysis-env-1 exited with code 0`. A retry with `--detatch` failed with `unknown flag`. *(01:12:32)*

- **Q:** When did the instructor say he would fix the Compose demo?
    - **A:** For next class. *(01:13:50)*

## 18. This week's milestone: a Dockerfile for your analysis

*01:14:06–01:17:04*

- **Q:** What is the main task for this week's milestone?
    - **A:** Create the `Dockerfile` that is the compute environment for your analysis. It is almost copy-paste from the class example. *(01:14:10)*

- **Q:** Which command should render your report inside the container?
    - **A:** `uv run quarto render`, with the needed folders mounted. *(01:14:37)*

- **Q:** How will the TAs grade the milestone's container?
    - **A:** They take your repository, build the container, and try to run the analysis in it. *(01:15:01)*

- **Q:** What optional tool did the instructor suggest you might add to the container with a `RUN` command?
    - **A:** A text editor, since the class's container didn't even have one. *(01:15:41)*

- **Q:** Which kind of analysis did the instructor name as needing system tools from Ubuntu?
    - **A:** Geospatial analysis. *(01:16:03)*

- **Q:** Is Docker Compose required for this week's milestone?
    - **A:** No. The goal is a `Dockerfile`, and the instructor will get Compose working in the future. *(01:16:45)*

## 19. Docker Compose outside the course

*01:17:04–01:20:07*

- **Q:** Which personal finance software did the instructor show with a Docker Compose file, and which similar one did he name?
    - **A:** Actual Budget, and Firefly III. *(01:17:36)*

- **Q:** What is the container called in Actual Budget's compose file?
    - **A:** `actual server`. *(01:18:10)*

- **Q:** What does Actual Budget's compose file specify for its container?
    - **A:** The image, ports, environment variables, volumes and a health check. *(01:18:19)*

- **Q:** Which command downloads and starts software from its compose file?
    - **A:** `docker compose up -d`. *(01:18:29)*

- **Q:** What are Jellyfin and n8n for?
    - **A:** Jellyfin serves movies and media; n8n is AI automation software. *(01:19:03)*

- **Q:** Which other app did the instructor mention that you can run from a compose file?
    - **A:** An app that stores recipes, for example from your Instagram collections. *(01:19:12)*

- **Q:** Where did the instructor say you can run these self-hosted apps?
    - **A:** On any machine: an old laptop in a closet, or a machine you pay for monthly in the cloud. *(01:19:28)*

---

- prompt: prompt-recall-1-remember.md @ 65eb21c
- prompt-hash: e448f8420cdb
- model: claude-opus-5-5 (requested: opus)
- backend: claude
- inputs: transcript-plaud.md, terminal.txt, materials.md, notes-class-main--claude-opus-5-5.md
- generated: 2026-11-24
- notes-input: notes-class-main--claude-opus-5-5.md @ 0caf0d47e007, links and section references removed, diagrams removed
