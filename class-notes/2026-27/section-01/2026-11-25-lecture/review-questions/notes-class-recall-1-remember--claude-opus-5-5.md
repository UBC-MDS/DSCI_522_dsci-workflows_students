# Docker Compose and Data Validation with pointblank: review questions, tier 1 — Remember

Date: 2026-11-25

Instructor: Daniel Chen

*Tier 1 of 5: Remember. Answer each question before you read its answer; tiers 2 to 5 build on these.*

## 1. Opening review exercise

*00:00:00–00:04:52*

- **Q:** State the instructor's teaching style as he described it at the start of class.
    - **A:** He doesn't teach from a slide deck. The class goes over all the commands and code together, and students can follow along. *(00:00:35)*

- **Q:** Which two files were students told to copy from the reference repository, instead of cloning the whole repository?
    - **A:** The `.py` file and the `pyproject.toml` file. *(00:01:10)*

- **Q:** Name the file students were allowed to copy but were encouraged to generate themselves as part of the review.
    - **A:** The `uv.lock` file. *(00:01:19)*

- **Q:** List the last two steps of the opening review task.
    - **A:** Build the container from the `Dockerfile`, then run it and get a bash prompt out of it. *(00:01:19)*

- **Q:** Where, besides the class's own screen, was the link to the reference repository posted?
    - **A:** In Slack. *(00:02:28)*

## 2. Creating and cloning the repository

*00:04:52–00:07:44*

- **Q:** What file did the instructor add when creating the demo repository on GitHub, and why?
    - **A:** A README file, so the repository had something in it and wasn't empty from the very beginning. *(00:05:24)*

- **Q:** Name the folder where the instructor keeps all his Git repositories.
    - **A:** A folder called `git`. Everything in it and its subfolders is a Git repository. *(00:06:09)*

- **Q:** State the practice from DSCI 521 that keeping all repositories in one `git` folder helps you follow.
    - **A:** Don't nest Git repositories. The `git` folder is always a safe place to clone into. *(00:06:22)*

- **Q:** Reproduce the command the instructor used to clone the demo repository `2026-11-25-docker-validate`.
    - **A:** `git clone git@github.com:chendaniely/2026-11-25-docker-validate.git` *(00:06:53)*

- **Q:** Which editor did the instructor use for the demo, and which editor did he say works just as well?
    - **A:** Positron. VS Code works just as well. *(00:07:03)*

- **Q:** What mistake did the instructor make when he first opened Positron?
    - **A:** He opened it in the `git` folder instead of the cloned repository folder. *(00:07:09)*

## 3. Using the template repository responsibly

*00:07:44–00:08:59*

- **Q:** What is the base template repository linked in Slack meant to be used for?
    - **A:** As the technical foundation for all of your project milestones. It includes an example report and many pieces covered later in the course. *(00:07:51)*

- **Q:** State the instructor's warning about using the template repository.
    - **A:** Don't just blindly copy it. You are still responsible for the work and should understand it. *(00:08:15)*

- **Q:** According to the instructor, what are you actually tested or interviewed on, given that getting the work done is a given?
    - **A:** Whether you understand the work. *(00:08:23)*

- **Q:** In the instructor's class, which commits are "fair game" for questions?
    - **A:** Any commit with your name on it. *(00:08:51)*

## 4. The `Dockerfile`: base image and system software ([29.1 Building container images from `Dockerfile`'s](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#building-container-images-from-dockerfiles))

*00:08:59–00:13:18*

- **Q:** What is a `Dockerfile`?
    - **A:** The file used to build containers. *(00:09:04)*

- **Q:** Name the base image the demo `Dockerfile` started from, and state what it contains.
    - **A:** `rocker/r-ver:4.6.2`, which is an Ubuntu image with R pre-installed. *(00:09:46)*

- **Q:** Which base image did the instructor's own class use for its Python projects?
    - **A:** An Ubuntu image. *(00:09:30)*

- **Q:** State the downside of using the R base image for a Python project.
    - **A:** It takes up more storage space, so anyone using the container, including the graders, has a longer download. *(00:09:57)*

- **Q:** State the main goal when choosing a base image.
    - **A:** Get something small enough, the bare minimum for the work you need. *(00:10:22)*

- **Q:** What are `RUN` commands in a `Dockerfile`?
    - **A:** Bash commands, like the ones you would type in a terminal, run in the container's operating system, which is typically Linux. *(00:10:40)*

- **Q:** What is `apt-get`?
    - **A:** Ubuntu's way of installing software. *(00:11:02)*

- **Q:** Name two kinds of Python work that may need non-Python system software installed in the image.
    - **A:** Neural nets with PyTorch, which may need C compilers, and geospatial packages, which may need regular software installed. *(00:11:42)*

- **Q:** List the three steps the reference `Dockerfile` uses to install Quarto on Linux.
    - **A:** Download the Quarto file, install it with `apt-get`, then delete the downloaded file. *(00:12:30)*

- **Q:** Which piece of software was deleted from the demo `Dockerfile` but is needed in your milestone container, and why is it needed?
    - **A:** Quarto, because the milestone container needs to run your report. *(00:12:57)*

## 5. Installing `uv` and controlling tool versions ([29.2 `Dockerfile` command summary](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#dockerfile-command-summary))

*00:13:18–00:15:30*

- **Q:** Name the file the instructor said you might see outside MDS, but which is not how `uv` generally works.
    - **A:** A `requirements.txt` file. *(00:13:47)*

- **Q:** According to the `uv` documentation, what is one way to get `uv` into your container?
    - **A:** Copy it from the container the `uv` project already built, which has `uv` installed. *(00:14:13)*

- **Q:** What can the Docker `COPY` command copy from, besides your local computer?
    - **A:** Other containers. *(00:14:29)*

- **Q:** Reproduce the `COPY` line in the demo `Dockerfile` that installs `uv`.
    - **A:** `COPY --from=ghcr.io/astral-sh/uv:0.13.7 /uv /uvx /usr/local/bin/` *(00:14:29)*

- **Q:** State the alternative to copying `uv` in that saves you this step.
    - **A:** Start from one of the prebuilt `uv` containers. *(00:14:41)*

- **Q:** Which version does `pyproject.toml` not track, making Docker necessary to control it?
    - **A:** The version of `uv` itself. *(00:14:57)*

## 6. `WORKDIR` and the `.venv` problem ([29.2 `Dockerfile` command summary](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#dockerfile-command-summary))

*00:15:30–00:19:28*

- **Q:** What does `WORKDIR` in a `Dockerfile` do when you start or go into the container?
    - **A:** It is Docker's way of saying `cd` here, so you land in that folder. In the demo, the folder is `/workspace`. *(00:15:30)*

- **Q:** What does `WORKDIR` do if the folder doesn't exist?
    - **A:** Docker creates it, so it works like `mkdir` and `cd` at the same time. *(00:16:32)*

- **Q:** Where do you usually end up when you run a container without a working directory set?
    - **A:** In the root of the container, looking at the operating system folders. *(00:15:57)*

- **Q:** What folder does `uv sync` create as part of making a virtual environment?
    - **A:** A `.venv` folder, which holds all the project's packages. *(00:17:08)*

- **Q:** What is the `.venv` folder specific to?
    - **A:** The operating system and computer that created it. *(00:17:19)*

- **Q:** How many kinds of computer did the instructor count, and from what?
    - **A:** Six: three operating systems times two CPU architectures. *(00:17:59)*

- **Q:** Name the environment variable and value the demo `Dockerfile` sets so `uv` installs packages outside the project's `.venv`.
    - **A:** `UV_PROJECT_ENVIRONMENT=/opt/venv`. *(00:19:13)*

- **Q:** Once that variable is set, what happens to the laptop's `.venv` folder when the project is mounted into the container?
    - **A:** It gets ignored in the container and still works on the local machine. *(00:19:28)*

## 7. Environment variables, `uv sync --locked`, and the SSH setup ([29.2 `Dockerfile` command summary](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#dockerfile-command-summary))

*00:27:21–00:30:18*

- **Q:** List the names the instructor gave for the variables that tools use.
    - **A:** System variables, environment variables, or global environment variables. *(00:27:30)*

- **Q:** Name one common place where programs store their settings on your computer.
    - **A:** A hidden config folder in your home directory. *(00:28:07)*

- **Q:** Why does the demo `Dockerfile` also save the environment variable to a file?
    - **A:** An SSH connection doesn't read environment variables. The `Dockerfile` writes the variable to `/etc/environment`. *(00:28:46)*

- **Q:** What does the Bash command `echo` do?
    - **A:** It outputs exactly what you give it: what you see is what you get. *(00:28:53)*

- **Q:** What does `>>` mean in a Bash command?
    - **A:** Append to the end of a file. *(00:29:00)*

- **Q:** What does the `--locked` flag do in `RUN uv sync --locked`?
    - **A:** It makes the command fail if `pyproject.toml` and `uv.lock` are not in sync, as an extra check. *(00:29:15)*

- **Q:** What does the last command in the demo `Dockerfile` do?
    - **A:** It makes sure the SSH program is turned on, for connecting Positron or VS Code later: `CMD ["/usr/sbin/sshd", "-D"]`. *(00:29:54)*

- **Q:** Which laptops need one extra command in the `Dockerfile` for the SSH connection?
    - **A:** Linux laptops. *(00:29:54)*

## 8. `pyproject.toml` and `.python-version`

*00:30:18–00:33:30*

- **Q:** Name the versioning system used for the reference project's version number, and the one it was contrasted with.
    - **A:** Date versioning, instead of semantic versioning. Students learn more in DSCI 524. *(00:30:54)*

- **Q:** What date does the version in the demo `pyproject.toml` record?
    - **A:** November 13 (`version = "2026.11.13"`), when the course's hard-pinned package versions were finalized. *(00:31:18)*

- **Q:** What does the `[tool.uv]` setting in the demo `pyproject.toml` make `uv add` do?
    - **A:** Write `==` instead of `>=` for the package version. *(00:31:24)*

- **Q:** What does the `.python-version` file contain, and what is it used for?
    - **A:** The Python version (`3.14`), so `uv` knows which version of Python to download. *(00:32:23)*

- **Q:** Name the two examples the instructor gave of projects that may need a different Python version.
    - **A:** Legacy code still on Python 2, and PyTorch, which lags behind new Python releases. *(00:32:53)*

## 9. Generating `uv.lock` and building the image ([29.4 Dockerfile FAQ](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#dockerfile-faq))

*00:33:30–00:35:47*

- **Q:** Which command did the instructor run to generate `uv.lock` from `pyproject.toml`?
    - **A:** `uv sync`. *(00:33:34)*

- **Q:** Why did `uv sync` run so quickly in the demo?
    - **A:** The packages were already installed, so it ran from cache. *(00:33:56)*

- **Q:** Reproduce the command the instructor ran to build the demo image.
    - **A:** `docker build --tag docker-uv-renv .` *(00:34:25)*

- **Q:** What is the short form of `docker build --tag`?
    - **A:** `-t`. *(00:34:25)*

- **Q:** What does the final `.` in `docker build --tag docker-uv-renv .` represent?
    - **A:** The current working directory. *(00:34:53)*

- **Q:** Which file does `docker build` look for by default?
    - **A:** A file called `Dockerfile`. You can point it to another file instead. *(00:35:06)*

- **Q:** List the build steps the instructor read from the `docker build` output, in order.
    - **A:** Start from the base container, copy `uv`, set the working directory, set the environment variable, copy the files, and run `uv sync`. *(00:35:29)*

## 10. Running the container interactively

*00:35:47–00:38:22*

- **Q:** What does `--rm` do in `docker run --rm`?
    - **A:** It removes the container when you exit it. *(00:36:02)*

- **Q:** What do the two flags in `-it` stand for?
    - **A:** `-i` is interactive mode and `-t` is TTY mode, which is essentially a terminal prompt. *(00:36:32)*

- **Q:** State the rule for double-dash and single-dash flags.
    - **A:** A double dash marks a flag with more than one character. A single dash marks a one-character flag, and those can be chained together. *(00:36:14)*

- **Q:** Reproduce the command the instructor used to get a bash prompt in the demo image.
    - **A:** `docker run --rm -it docker-uv-renv bash` *(00:36:56)*

- **Q:** What did `pwd` and `whoami` print inside the container?
    - **A:** `/workspace` and `root`. *(00:36:56)*

- **Q:** What part of the terminal tells you which computer you are on?
    - **A:** The prompt, which shows the username and the computer. *(00:37:44)*

- **Q:** What happened when the instructor typed `python` in the container, and what command worked instead?
    - **A:** It printed `bash: python: command not found`. `uv run python` opened the Python from `uv`. *(00:37:52)*

- **Q:** Which command leaves the container's bash prompt?
    - **A:** `exit`. Typing `quit` gave `command not found`. *(00:38:12)*

## 11. Mounting the project folder with `-v`

*00:38:22–00:42:42*

- **Q:** Reproduce the `docker run` command the instructor used to mount the project folder.
    - **A:** `docker run --rm -v "$(pwd):/workspace" -it docker-uv-renv bash` *(00:38:52)*

- **Q:** What does `-v "$(pwd):/workspace"` do?
    - **A:** It takes all the files in your current working directory and puts them in the `workspace` folder in the container. *(00:39:18)*

- **Q:** How do you mount more than one folder, and when is this common?
    - **A:** Add another `-v`. This is common with databases, which store information in several folders. *(00:39:36)*

- **Q:** When a `Dockerfile` uses `COPY` to put files in the image, at what point are the files copied?
    - **A:** At the time of `docker build`. *(00:40:06)*

- **Q:** How quickly do changes appear on the other side of a `-v` mount?
    - **A:** Immediately, in both directions. *(00:40:29)*

- **Q:** How does GitHub see a container you try to use Git from?
    - **A:** As a brand new machine, which you would have to set up every time because the container resets. *(00:41:38)*

- **Q:** State the instructor's warning about Git credentials and containers.
    - **A:** Don't put credentials in the container. Your SSH key is like the password to your account, and anyone who pulls your container could find it and mess with your account. *(00:41:50)*

- **Q:** When is it appropriate to copy files into the container instead of mounting them?
    - **A:** At the end of a project, for example for compliance, when it is the final version. *(00:42:20)*

## 12. Shared files and editing in two places

*00:42:42–00:44:42*

- **Q:** What command did the instructor run inside the mounted container to show that files are shared?
    - **A:** `touch hello.py`. The file then also appeared on his laptop. *(00:43:02)*

- **Q:** What did the instructor compare a mounted folder to?
    - **A:** A network share drive, where both sides work on the same files. *(00:43:15)*

- **Q:** Name the IDE command that reloads a file that may have been changed elsewhere.
    - **A:** Revert file. *(00:43:44)*

- **Q:** State the warning about saving a file that was changed on the other side of a mount.
    - **A:** If you hit overwrite, you lose the other changes. It is essentially a Git conflict without being a Git conflict. *(00:43:59)*

## 13. The `docker-compose.yml` file ([33.1 Docker Compose to launch containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-docker-compose.html#docker-compose-to-launch-containers))

*00:44:42–00:52:06*

- **Q:** What problem with `docker run` does the Docker Compose YAML file exist to solve?
    - **A:** `docker run` commands can very quickly get very long, with many flags that are hard to track. *(00:45:02)*

- **Q:** Which `docker run` flag sets an environment variable, and what example was given?
    - **A:** `-e`. For example, the RStudio container has a variable that disables the initial login page. *(00:45:24)*

- **Q:** What does the `services:` key at the top of `docker-compose.yml` mean?
    - **A:** It lists the containers you want Docker to run. *(00:46:18)*

- **Q:** Name the service in the demo `docker-compose.yml` and the image it uses.
    - **A:** The service is `analysis-env` and the image is `docker-uv-renv`, the name given in `docker build`. *(00:46:31)*

- **Q:** What does `build: .` in `docker-compose.yml` correspond to?
    - **A:** The `docker build` command, which looks for the `Dockerfile` in the current folder. It is how the image gets built if it doesn't exist. *(00:47:06)*

- **Q:** In the port mapping `"2222:22"`, which number is the port in the container and which is the port on your computer?
    - **A:** The second number (`22`) is the port in the container. The first (`2222`) is the port on your computer. *(00:48:18)*

- **Q:** State the port numbers mentioned for RStudio, SSH and JupyterLab.
    - **A:** RStudio uses 8787 and SSH uses 22. JupyterLab uses 8888, and a second JupyterLab defaults to 8889. *(00:48:45)*

- **Q:** State the instructor's warning about port numbers in other people's Compose files.
    - **A:** Pay attention to the first number, because that is where you connect on your computer. Otherwise you may follow the instructions and find it "doesn't work" because you are looking at the wrong spot. *(00:49:43)*

- **Q:** Besides the project folder, what does the demo file's `volumes:` section mount, and for how long is it in the container?
    - **A:** Your SSH key. It is in the container only while the container runs, not permanently. *(00:50:19)*

- **Q:** What happens to files you delete or packages you install in a container after you turn it off and on again?
    - **A:** The container resets to what was built. Only files in a mounted volume are kept. *(00:50:38)*

- **Q:** State the instructor's warning about `rm -rf /`.
    - **A:** It will kill the system, so try it only in a container, which resets when restarted, and never on your actual computer. *(00:51:42)*

## 14. Docker Compose commands ([33.2 Docker Compose commands](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-docker-compose.html#docker-compose-commands))

*00:52:06–00:58:03*

- **Q:** From which folder do you run `docker compose` commands?
    - **A:** The folder with the compose file. *(00:53:02)*

- **Q:** Which `docker compose` command replaces `docker build -t ...`?
    - **A:** `docker compose build`. *(00:53:07)*

- **Q:** Why does the instructor like having settings specified in a file?
    - **A:** It plays well with version control. *(00:53:25)*

- **Q:** Reproduce the command the instructor used to start the container in the background with Docker Compose.
    - **A:** `docker compose up --detach` *(00:53:39)*

- **Q:** What does `--detach` do in `docker compose up --detach`?
    - **A:** It starts the container without giving you a prompt inside, so it runs in the background and you get your normal computer back. *(00:54:12)*

- **Q:** Name the command the instructor ran to list the containers, and what it showed for the running container.
    - **A:** `docker ps -a`. It showed the unique ID, the image `docker-uv-renv`, port 2222 mapped to the container's port 22, "16 seconds ago" for when it started, and the name `2026-11-25-docker-validate-analysis-env-1`. *(00:54:52)*

- **Q:** What did `docker compose exec 2026-11-25-docker-validate-analysis-env-1 bash` print?
    - **A:** `service "2026-11-25-docker-validate-analysis-env-1" is not running`. *(00:55:48)*

- **Q:** Reproduce the command that worked to open a shell in the running Compose container.
    - **A:** `docker compose exec analysis-env bash` *(00:55:56)*

- **Q:** What happened when the instructor ran `docker compose down` inside the container?
    - **A:** It printed `bash: docker: command not found`, because he was in the container, a completely different computer. He had to exit first. *(00:57:23)*

- **Q:** What does `docker compose down` do?
    - **A:** It reads all the containers from the Docker Compose file and turns them off. *(00:57:33)*

- **Q:** Why should you be diligent about turning containers off?
    - **A:** Containers are essentially other computers that take up RAM, so running many shrinks your free memory. *(00:57:38)*

## 15. Running commands non-interactively ([33.3 Running a Docker container non-interactively using the Docker Compose](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-docker-compose.html#running-a-docker-container-non-interactively-using-the-docker-compose))

*00:58:03–01:01:10*

- **Q:** What did the instructor say the `docker compose run` approach is used for in the course?
    - **A:** It is one of the ways your work is graded, and a way you should document running it. *(00:58:08)*

- **Q:** What does `--rm` do in `docker compose run --rm analysis-env ...`?
    - **A:** It makes the container turn itself off when the command is done. *(00:58:29)*

- **Q:** What error did `docker compose run --rm analysis-env python` produce?
    - **A:** `exec: "python": executable file not found in $PATH`. *(00:59:10)*

- **Q:** Reproduce the command that opened a Python interpreter in the container from the laptop.
    - **A:** `docker compose run --rm analysis-env uv run python` *(01:00:06)*

- **Q:** How many ways does the instructor have Python installed on his own computer?
    - **A:** About four. He has to make sure he stays in the self-contained `uv` mode when teaching. *(00:59:42)*

- **Q:** What command did the instructor suggest running in the container to check that your Quarto report builds?
    - **A:** `uv run quarto render` with your file. *(01:00:35)*

## 16. Connecting Positron or VS Code to the container over SSH

*01:01:10–01:06:55*

- **Q:** Which editor can open a Docker container directly?
    - **A:** VS Code. *(01:01:59)*

- **Q:** Name the VS Code forks the instructor listed.
    - **A:** Positron, Code and Cursor. *(01:02:05)*

- **Q:** What do VS Code forks lack access to?
    - **A:** The Microsoft extension store. *(01:02:35)*

- **Q:** Name the VS Code feature for connecting to another machine.
    - **A:** Remote SSH. *(01:02:43)*

- **Q:** What username do you connect to the container with, and where did the class see it?
    - **A:** `root`, which appeared in the container's prompt as "root at something". *(01:03:06)*

- **Q:** What host and port does Positron connect to for the container?
    - **A:** `localhost`, on the mapped port 2222 from `docker-compose.yml`. *(01:03:26)*

- **Q:** Which folder do you open in Positron once it is connected to the container?
    - **A:** The `workspace` folder inside the container. *(01:04:24)*

- **Q:** How does the instructor usually work with containers?
    - **A:** He tests on his local computer and then runs the last command in the container. *(01:05:11)*

- **Q:** State the size of the machine the instructor connected Positron to over the summer, and why he needed it.
    - **A:** A 128 GB RAM machine, because his datasets needed about a hundred gigabytes of RAM. *(01:05:42)*

- **Q:** Is connecting an editor to the container tested in the milestones?
    - **A:** No. There is no way to test it in the milestone. *(01:06:26)*

## 17. Docker Compose beyond this course

*01:06:55–01:08:33*

- **Q:** Name the open-source tools the instructor said run their services through Docker Compose files.
    - **A:** Ollama, n8n, Jellyfin and Actual Budget. *(01:07:28)*

- **Q:** Match each tool to what it does: n8n, Jellyfin, Actual Budget.
    - **A:** n8n is an AI automation service, Jellyfin hosts your own movies, and Actual Budget is a personal finance application. *(01:07:44)*

- **Q:** List the parts the instructor pointed out in Actual Budget's Docker Compose file.
    - **A:** Services, an image, a port, environment variables and volumes. *(01:07:53)*

- **Q:** What did the instructor suggest for practising this skill?
    - **A:** Install Linux on an old laptop and run everything in containers. *(01:08:08)*

## 18. Adding the validation packages ([41 Data validation: Python (pointblank)](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/data-validation-python-pointblank.html))

*01:08:33–01:10:16*

- **Q:** Did the instructor run the data validation demo in the container or on his laptop?
    - **A:** On his laptop, not in the container. *(01:08:38)*

- **Q:** Reproduce the first command the instructor tried to add the validation packages.
    - **A:** `uv add pandera pointblank` *(01:09:06)*

- **Q:** What error did `uv add pandera` print in the demo repository?
    - **A:** ``error: Project is missing a `[project]` table; add a `[project]` table to use production dependencies, or run `uv add --dev` instead``. *(01:09:30)*

- **Q:** State the workaround when `uv add` didn't work.
    - **A:** Add the packages manually to `pyproject.toml`, then run `uv sync`, which creates the lock file from the TOML file. *(01:09:59)*

- **Q:** Which package was added to get a dataset to work with?
    - **A:** `palmerpenguins`. *(01:10:09)*

- **Q:** What did `uv sync` report after the packages were added by hand?
    - **A:** It resolved 79 packages and installed 77. *(01:10:04)*

## 19. Why validate data, and exploring missing values ([41.1 Where are the missing values?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/data-validation-python-pointblank.html#where-are-the-missing-values))

*01:10:16–01:13:41*

- **Q:** Who wrote pointblank?
    - **A:** Rich, from Posit, which builds a lot of open-source data tools. *(01:10:30)*

- **Q:** Reproduce the import line used for pointblank.
    - **A:** `import pointblank as pb` *(01:10:58)*

- **Q:** How was the penguins dataset loaded?
    - **A:** `penguins = load_penguins()`, with `load_penguins` from `palmerpenguins`. *(01:11:19)*

- **Q:** What example of an unexpected value in a health dataset did the instructor give?
    - **A:** Pregnant men. *(01:11:48)*

- **Q:** In health survey data, what value did the instructor say is often used instead of a missing value?
    - **A:** `99`. *(01:12:15)*

- **Q:** Name the pointblank function that reports the missing values in a dataset.
    - **A:** `pb.missing_vals_tbl()`, called as `pb.missing_vals_tbl(data=penguins)`. *(01:12:47)*

- **Q:** Where in the penguins data did `pb.missing_vals_tbl()` show most of the missingness?
    - **A:** Somewhere near the beginning of the rows. *(01:13:02)*

## 20. Building a validation with thresholds ([41.2 Checking values](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/data-validation-python-pointblank.html#checking-values))

*01:13:41–01:18:29*

- **Q:** State how a pointblank validation works, in the instructor's words.
    - **A:** You create an agent of testing, add the checks, and then tell it to report back. *(01:13:45)*

- **Q:** What threshold values did the class's validation use, and what levels do they set?
    - **A:** `thresholds=(0.01, 0.05, 0.10)`, which set 1%, 5% and 10% failure rates for warning, error and critical. *(01:14:20)*

- **Q:** Which check did the class use to make sure the `species` column contains only expected values?
    - **A:** `col_vals_in_set()`, for example `.col_vals_in_set(columns="species", set=[...])`. *(01:14:56)*

- **Q:** Which method checks that a column's values fall within a range, and what range was used for bill length?
    - **A:** `col_vals_between()`, with 30 to 60 for `bill_length_mm`. It is inclusive by default, and there is a way to flag bounds as not inclusive. *(01:16:07)*

- **Q:** Which check makes sure there are no duplicate rows?
    - **A:** `rows_distinct()`. *(01:16:52)*

- **Q:** Which method actually runs all the checks?
    - **A:** `interrogate()`. *(01:17:12)*

- **Q:** At which points in an analysis did the instructor say to put data checks?
    - **A:** Right after the data cleaning process and right before the modelling process. You check your data in multiple places. *(01:15:31)*

- **Q:** What does displaying the interrogated pointblank object show?
    - **A:** A table saying whether each check passed, with a pass/fail rate and different colours based on the thresholds. *(01:17:58)*

## 21. Failing checks and splitting passing and failing rows ([41.4 Splitting the passing and failing rows](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/data-validation-python-pointblank.html#splitting-the-passing-and-failing-rows))

*01:18:29–01:20:48*

- **Q:** How did the instructor make the `species` check fail on purpose?
    - **A:** He removed `"Gentoo"` from the allowed set, leaving only `"Adelie"` and `"Chinstrap"`, so warnings were thrown. *(01:18:29)*

- **Q:** State the instructor's recommendation about checking missing values.
    - **A:** Do missing values as a separate analysis: check missingness per column and then per row, separately from the value checks. *(01:18:52)*

- **Q:** What two data frames can pointblank give you after a validation?
    - **A:** One of all the rows that passed and one of all the rows that failed. *(01:19:36)*

- **Q:** Reproduce the pointblank method calls that split the data into passing and failing rows.
    - **A:** `values.get_sundered_data(type="pass")` and `values.get_sundered_data(type="fail")`. *(01:19:36)*

- **Q:** Which data frame do you pass on to the next team member, and what do you keep working on?
    - **A:** You pass on the rows that passed, so they can build the rest of the pipeline. You keep cleaning the rows that failed. *(01:19:52)*

- **Q:** What can you do with the passed and failed data frames so someone else can pick them up?
    - **A:** Save them out to CSV files. *(01:20:32)*

- **Q:** What did the instructor say next week's work would mostly be?
    - **A:** Data validation, and breaking your code into smaller pieces. *(01:20:48)*

---

- prompt: prompt-recall-1-remember.md @ 65eb21c
- prompt-hash: e448f8420cdb
- model: claude-opus-5-5 (requested: opus)
- backend: claude
- inputs: transcript-plaud.md, terminal.txt, materials.md, notes-class-main--claude-opus-5-5.md
- generated: 2026-11-25
- notes-input: notes-class-main--claude-opus-5-5.md @ 06f3ac544b79, links and section references removed, diagrams removed
