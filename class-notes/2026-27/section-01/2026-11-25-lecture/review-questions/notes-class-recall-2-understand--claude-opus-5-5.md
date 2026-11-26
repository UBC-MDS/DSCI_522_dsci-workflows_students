# Docker Compose and data validation with pointblank: review questions, tier 2 — Understand

Date: 2026-11-25

Instructor: Daniel Chen

*Tier 2 of 5: Understand. Explain each answer in your own words before you read it; tier 1 (Remember) covers the facts, tiers 3 to 5 put them to use.*

## 1. Creating and cloning the repository

*00:04:52–00:07:44*

- **Q:** Why did Daniel create the `2026-11-25-docker-validate` repository on GitHub first, rather than starting it locally?
    - **A:** He suggested creating it online so that you are keeping track of your work. He presented this as the way he does it himself. *(00:05:09)*

- **Q:** Why did Daniel add a `README.md` when he created the repository?
    - **A:** He wanted something in the repository from the start, so the class wasn't dealing with an empty repository at the very beginning. *(00:05:24)*

- **Q:** Explain the two reasons Daniel gave for cloning all his repositories into a single `git` folder.
    - **A:** First, it makes clear that everything in that folder and its subfolders is a Git repository, so repositories aren't scattered across the computer. Second, 521 taught that you don't want to nest Git repositories. A folder that holds only repositories is always a safe place to clone into. *(00:06:13)*

- **Q:** Why did Daniel run `positron .` a second time after `cd 2026-11-25-docker-validate`?
    - **A:** His first `positron .` opened the `git` folder rather than the folder he had cloned. With the editor opened in the repository itself, he doesn't have to worry about subfolders. *(00:07:36)*

## 2. Using the template repository responsibly

*00:07:44–00:08:59*

- **Q:** If the base template repository works, why does Daniel still warn against copying it blindly?
    - **A:** A template helps with typing and avoids mistakes. But you should still know your work and be responsible for it, even when things are working. *(00:08:23)*

- **Q:** Explain why understanding your work matters more in a world of AI-assisted coding.
    - **A:** Nobody cares that you can get the work done, because that is a given. What you are tested on, or interviewed on, is whether you understand it. *(00:08:23)*

- **Q:** What does Daniel's rule "a commit with your name on it is fair game" mean for a group project?
    - **A:** He can ask you about any commit that carries your name. So you need to understand everything you commit, including anything you adapted from a template. *(00:08:51)*

## 3. The `Dockerfile`: base image and system software ([29.3 Choosing a base image for your Dockerfile](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#choosing-a-base-image-for-your-dockerfile))

*00:08:59–00:13:18*

- **Q:** The `rocker/r-ver` base image works for Python projects. Why should you still be mindful of using it in a Python-only project?
    - **A:** It is an Ubuntu image with R components pre-installed, so it takes up more storage. Anyone who uses your container, such as the people grading it, faces a longer download. That is something to weigh if you think about the people downstream of you. *(00:09:51)*

- **Q:** Summarize the goal Daniel gave for choosing a base image, and what the extreme version of that goal looks like.
    - **A:** The goal is an image that is small enough, the bare minimum for the work you need. At the extreme, some images are barely an operating system, and you have to install a lot of things from scratch. *(00:10:22)*

- **Q:** What are `RUN` commands in a `Dockerfile`, and how does that explain why MDS has you use Git Bash?
    - **A:** `RUN` commands are essentially Bash commands, the same as you would type in a terminal. They run in whatever operating system the image is based on, which is typically Linux. Git Bash uses pretty much the same kinds of commands. *(00:10:40)*

- **Q:** Why did the reference `Dockerfile` use `apt-get` to install `git` and `nano`?
    - **A:** `apt-get` is Ubuntu's way of installing software. `git` lets you do Git things inside the container. `nano` gives a text editor for seeing what's going on without jumping back and forth. *(00:11:02)*

- **Q:** Why might a Python project still need non-Python system software installed in its `Dockerfile`?
    - **A:** Some Python packages rely on other tools and don't work without them. PyTorch probably needs C compilers or other system software. Geospatial packages may need regular software installed, because not everything is written in Python. *(00:11:51)*

- **Q:** Explain how the Quarto install commands in the reference `Dockerfile` compare to installing software on your laptop.
    - **A:** The commands download the Quarto file, install it with `apt-get`, then delete the downloaded file. That is the same as downloading an installer and double-clicking it. In a container you have to do it through commands, which is why terminal commands matter. *(00:12:30)*

- **Q:** Daniel deleted the Quarto section for the demo. Why does a milestone container still need it?
    - **A:** For your milestones, the container has to run your report. So it needs every piece of software the report requires, including Quarto. *(00:13:10)*

## 4. Installing `uv` and controlling tool versions ([29.2 `Dockerfile` command summary](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#dockerfile-command-summary))

*00:13:18–00:15:30*

- **Q:** Why do Python installation instructions found outside MDS need care?
    - **A:** In MDS you use Python through `uv`. Outside instructions may not be `uv`-compatible, or may not be written so you can copy-paste them. A `requirements.txt` file, for example, is not how `uv` generally works. *(00:13:47)*

- **Q:** Why does the course teach only one way of installing Python packages?
    - **A:** Otherwise the course would be teaching five different ways to install software. Daniel said there is no benefit to teaching five ways to install the same piece of software. *(00:13:47)*

- **Q:** Explain how `COPY --from=ghcr.io/astral-sh/uv:0.13.7 /uv /uvx /usr/local/bin/` puts `uv` into the image.
    - **A:** Docker's `COPY` can copy files from your computer into the container, and it can also copy files from other containers. The `uv` documentation provides an image that already has `uv` installed. This line copies the `uv` and `uvx` files out of that image and into this one. *(00:14:29)*

- **Q:** A virtual environment already controls package versions. Why is Docker still needed?
    - **A:** The whole point of Docker is complete control over every piece of software that gets installed. The tool itself also matters: `pyproject.toml` doesn't track the version of `uv`. Docker controls those other pieces of software. *(00:14:57)*

- **Q:** Compare copying `uv` in with `COPY --from` against starting from a prebuilt `uv` image.
    - **A:** Swapping in one of the many prebuilt `uv` images saves you from doing the copy step. If you run into a problem, though, you may need to find out where `uv` is installed on that particular machine. *(00:15:20)*

## 5. `WORKDIR` and the `.venv` problem ([29.2 `Dockerfile` command summary](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#dockerfile-command-summary))

*00:15:30–00:19:28*

- **Q:** What does `WORKDIR /workspace` do, and why is it useful?
    - **A:** It tells Docker to `cd` into `/workspace` whenever you turn on or enter the container. Without it you typically land in the root of the container, among the operating-system folders. On a project you want to see only your own files. That matters if you ever run something like `rm *`, because you don't want to delete the computer. *(00:16:13)*

- **Q:** How does `WORKDIR` differ from a plain `cd`?
    - **A:** If the folder doesn't exist, Docker creates it. So `WORKDIR` acts like a `mkdir` and a `cd` at the same time. *(00:16:32)*

- **Q:** Why can't the container use the `.venv` folder that `uv sync` created on your laptop?
    - **A:** The `.venv` folder holds all the project's packages, but it is specific to the operating system and computer that created it. The container is another operating system, so that environment doesn't match. *(00:17:19)*

- **Q:** Explain how the variety of students' computers connects to why the course uses Docker.
    - **A:** Students use Windows, macOS and sometimes Linux, on either Intel or ARM chips. That makes six different types of computer to account for. Docker is used because we want our code to run on someone else's machine, not just our own. *(00:17:59)*

- **Q:** How does mounting the project folder cause a `.venv` problem in the container?
    - **A:** Mounting the volume also mounts your laptop's `.venv` folder into the container. That virtual environment won't match the operating system inside the container. *(00:18:25)*

- **Q:** Explain how `ENV UV_PROJECT_ENVIRONMENT=/opt/venv` solves the `.venv` problem.
    - **A:** It tells `uv` to use `/opt/venv`, a system folder, instead of the current folder's `.venv`. This is the official `uv` approach. `RUN uv sync` then installs packages from the lock file into `/opt/venv`. Because the container is Linux, they are the right packages for it, and a mounted `.venv` is simply ignored: it still works on your laptop and does nothing in the container. *(00:19:28)*

## 6. Environment variables, `uv sync --locked`, and the SSH setup ([29.2 `Dockerfile` command summary](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#dockerfile-command-summary))

*00:27:21–00:30:18*

- **Q:** Explain what an environment variable such as `UV_PROJECT_ENVIRONMENT` is, using Daniel's comparison to Python code.
    - **A:** Your Python code has variables, and tools have their own variables too, known as system or environment variables. Setting `UV_PROJECT_ENVIRONMENT` gives `uv` a variable it looks up whenever it runs a command. *(00:27:30)*

- **Q:** Why do so many programs keep settings in a hidden config folder in your home directory?
    - **A:** Programs need to adapt to people's computers and preferences. Many programs you work with store their settings there. The folder is hidden on purpose. *(00:28:07)*

- **Q:** The `Dockerfile` already sets `UV_PROJECT_ENVIRONMENT` with `ENV`. Why does it also run `echo "UV_PROJECT_ENVIRONMENT=..." >> /etc/environment`?
    - **A:** When an editor connects to the container over SSH, the connection doesn't read the environment variable. So the variable also has to be saved to a file, and this line does that. *(00:28:46)*

- **Q:** Interpret the pieces of `echo "..." >> /etc/environment`.
    - **A:** `echo` outputs exactly what you give it. `>>` appends to the end of a file. Together they write one line of text onto the end of `/etc/environment`. *(00:29:00)*

- **Q:** Why does the `Dockerfile` run `uv sync --locked` instead of plain `uv sync`?
    - **A:** `--locked` is an extra check that `pyproject.toml` and `uv.lock` are in sync. If they are not, the command fails, so what you get is what you expect. You could leave it out, but it is a guard you want to put in. *(00:29:15)*

- **Q:** Why does the `Dockerfile` end by making sure the SSH server is running?
    - **A:** Later, Positron or VS Code connects to the container through the SSH program. That connection needs SSH turned on in the container. *(00:29:54)*

## 7. `pyproject.toml` and `.python-version`

*00:30:18–00:33:30*

- **Q:** Why does the reference project use a date such as `2026.11.13` as its version instead of semantic versioning?
    - **A:** Daniel chose date versioning so the course can track how things update over the years. Because many packages are hard-pinned, the date shows what the package versions were when the course was finalized, on November 13. *(00:31:11)*

- **Q:** What does `add-bounds = "exact"` under `[tool.uv]` change?
    - **A:** It makes `uv add` write an exact `==` pin instead of `>=`. It is another `uv` setting, which `uv` looks up in this file. *(00:31:24)*

- **Q:** Why isn't the `/opt/venv` location set in `pyproject.toml` rather than in the `Dockerfile`?
    - **A:** You probably could set it there. But then `uv` would do the same thing on your own machine. You want Docker to behave slightly differently from your computer, which is why settings end up in different places. *(00:31:47)*

- **Q:** Explain what `.python-version` does, and why it is useful to have per project.
    - **A:** It tells `uv` which version of Python to download when it runs Python. Different projects can then use not only different package versions but different Python versions. *(00:32:23)*

- **Q:** Give an example from class of why a project might need a Python version different from the rest of your computer.
    - **A:** Legacy code that has been running for fifteen years might still be on Python 2. You don't want your whole computer on an unmaintained Python. PyTorch is another case: it is so big, with so many dependencies, that it always lags a little behind. *(00:32:53)*

## 8. Generating `uv.lock` and building the image ([29.4 Dockerfile FAQ](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#dockerfile-faq))

*00:33:30–00:35:47*

- **Q:** How did running `uv sync` in a folder with only `pyproject.toml` produce `uv.lock`, and why was it so fast?
    - **A:** `uv sync` installed all the packages listed in `pyproject.toml` and then created the `uv.lock` file. It ran quickly because the packages were already installed, so it worked from the cache. *(00:33:56)*

- **Q:** Why did Daniel check for `uv.lock` before running `docker build`?
    - **A:** The `Dockerfile` copies the project files into the image, including `uv.lock` (`COPY pyproject.toml uv.lock .python-version ./`). With `uv.lock` present, all the files the `Dockerfile` needs were there. *(00:34:16)*

- **Q:** What does the final `.` in `docker build --tag docker-uv-renv .` mean?
    - **A:** The `.` is the current working directory. `docker build` looks there for a file called `Dockerfile` and uses it to build the image. By default it looks for that name, but you can point it at another Dockerfile. *(00:35:06)*

- **Q:** Interpret the step-by-step output of `docker build`.
    - **A:** The output follows the `Dockerfile` in order. It starts from the base image, copies `uv` in, sets the working directory, sets the environment variable, copies the project files, and runs `uv sync`. Once the last step finishes, the image is built. *(00:35:29)*

## 9. Running the container interactively

*00:35:47–00:38:22*

- **Q:** What does `--rm` do in `docker run --rm -it docker-uv-renv bash`?
    - **A:** When you exit the container, `--rm` shuts it down on your computer. *(00:36:02)*

- **Q:** Explain why `-it` has a single dash, while other flags have two.
    - **A:** Double dashes mark a flag whose name has more than one character, and a single dash marks a one-character flag. Single-character flags can be chained together. So `-it` is `-i` for interactive mode plus `-t` for TTY mode, which is essentially a terminal prompt. *(00:36:22)*

- **Q:** After `docker run ... bash`, how can you tell from the terminal that you are on a different computer?
    - **A:** The prompt looks different: it shows the username and the computer name, here `root` and the container's ID. `pwd` shows `/workspace`, a folder that probably doesn't exist on your laptop, and your laptop's username is probably not `root`. Reading the prompt is how you figure out where you are. *(00:37:15)*

- **Q:** How is running a container in your terminal like cloud computing?
    - **A:** In both cases you work on another computer through a terminal window. With cloud computing, the other computer is not on your physical device and you reach it over an internet connection. *(00:37:24)*

- **Q:** Why did typing `python` in the container give `command not found`, while `uv run python` worked?
    - **A:** In this container, Python is reached through `uv`. `uv run python` opens the Python that comes from `uv`, with everything you installed. *(00:37:52)*

## 10. Mounting the project folder with `-v`

*00:38:22–00:42:42*

- **Q:** Explain what `-v "$(pwd):/workspace"` does, and why it isn't written with `.`.
    - **A:** It takes your current working directory and puts all its files into the `workspace` folder in the container. You can't always use `.`, because of differences between Windows and Mac. The command is written to work more generally. *(00:39:18)*

- **Q:** Why would you ever pass more than one `-v` flag?
    - **A:** Each `-v` mounts one folder, so multiple folders need multiple `-v` flags. This happens a lot with databases, which store their information in several different folders. *(00:39:36)*

- **Q:** Why mount your files with `-v` instead of using `COPY` in the `Dockerfile` to put everything into the image?
    - **A:** `COPY` only captures the files as they were at the time of `docker build`. An analysis that changes every minute would need a rebuild every time just to get the files in. So the image holds just the software, and the constantly changing files are mounted later. *(00:40:25)*

- **Q:** Explain the two-way benefit of a `-v` mount.
    - **A:** Changes made on one side are immediately reflected on the other. If you make a small fix while checking something inside the container, it shows up straight away on your computer. *(00:40:44)*

- **Q:** Why is it more practical to run Git on your laptop than inside the container?
    - **A:** The container resets every time you turn it off and on. GitHub sees it as a brand-new machine, so you would have to set up your access token or SSH key again each time. With the folder mounted, your files are on your computer and you can `git add`, `git commit` and `git push` normally. *(00:41:38)*

- **Q:** Why must you never put Git credentials inside the container image itself?
    - **A:** Your SSH key is like the password to your account. Someone could pull your container, find the Git credentials in it, and start messing around with your account. Keeping credentials out of the image is a security reason for mounting rather than copying. *(00:41:50)*

- **Q:** When is copying the project files into the image the right choice?
    - **A:** At the end of a project, when you have to submit the actual version, for example for compliance. Copying the files makes them part of the container itself. While you are actively working, you don't want to keep rebuilding the container. *(00:42:20)*

## 11. Shared files and editing in two places

*00:42:42–00:44:42*

- **Q:** What did running `touch hello.py` inside the mounted container demonstrate?
    - **A:** The empty `hello.py` appeared in the container's folder and in the project folder on the laptop. Both sides reflect each other pretty much immediately. *(00:43:06)*

- **Q:** Explain Daniel's network share drive analogy for a mounted folder.
    - **A:** The laptop and the container are both working on the same files, like two people on a network share drive. *(00:43:15)*

- **Q:** Why is choosing "overwrite" dangerous when the same file is open on both sides?
    - **A:** An open file doesn't reload automatically when it changes on the other side. Saving can then bring up an overwrite prompt, which is effectively a Git conflict without Git. If you overwrite, the other changes are gone. As on a network drive, the order of saves decides whose version survives. *(00:43:59)*

- **Q:** How does an IDE's "revert file" command help when you work on the same files in two places?
    - **A:** Revert file refreshes the file from what is on disk. If you know you work in several places, revert the file before you edit, so you don't save over changes made on the other side. *(00:43:59)*

## 12. The `docker-compose.yml` file ([33.1 Docker Compose to launch containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-docker-compose.html#docker-compose-to-launch-containers))

*00:44:42–00:52:06*

- **Q:** Why does the `docker-compose.yml` file exist, if `docker run` can already do everything?
    - **A:** `docker run` commands quickly get very long. Each port, volume or environment variable (`-e`) adds another flag. Such a command is easy to copy-paste, but apart from maybe the README it is the only documentation, and its flags and parameters are hard to track. Compose puts them in a file. *(00:45:58)*

- **Q:** In the demo file, what is the difference between the service name `analysis-env` and the image name `docker-uv-renv`?
    - **A:** `image: docker-uv-renv` is the image built with `docker build`. `analysis-env` is a name for one container that uses it. The two names are kept separate because several containers can come from the same image, and they can't share a name. *(00:46:42)*

- **Q:** What does `build: .` in the compose file correspond to?
    - **A:** It is essentially the `docker build` command. The `.` means it looks for the `Dockerfile` in this folder. It says how to build the image if it doesn't exist yet. *(00:47:06)*

- **Q:** Interpret the port mapping `"2222:22"` in `docker-compose.yml`.
    - **A:** The second number is the port where the software runs inside the container, here 22 for SSH. The first number is the port you use on your own laptop to reach it. You connect on your computer through the first number. *(00:48:18)*

- **Q:** Why would the port on your computer differ from the one in the container, as with JupyterLab?
    - **A:** Port 22 is a common port used for real things on your computer, so remapping avoids overwriting it by accident. If you run JupyterLab twice, the second copy falls back to 8889 because the first already has the default port. You can also map to a number you simply prefer to type. *(00:49:03)*

- **Q:** Why does Daniel warn you to check the first port number when using someone else's Compose file?
    - **A:** The first number is how you connect on your computer, and other people may or may not keep the same number on both sides. If you just follow instructions while looking at the wrong port, it will seem not to work. *(00:49:43)*

- **Q:** Why is your SSH key mounted through `volumes:` rather than built into the image?
    - **A:** Mounted this way, the key is not permanently in the container. Your secret credential is there only while the container runs. *(00:50:19)*

- **Q:** Explain what happens to changes made inside a container when it restarts, and why that is useful.
    - **A:** It resets to what was built, so deleted files and installed packages are undone. Only files in a mounted volume are saved, because they are on your computer. That makes the container a sandbox: try a tricky PyTorch install, and if it fails, turn the container off and on and try again. *(00:51:32)*

- **Q:** Why does Daniel say a container is the place to try `rm -rf /`, and never your own computer?
    - **A:** `rm -rf /` kills the system it runs on. Never run it on your actual computer. In a container, turning it off and on again resets everything. *(00:51:42)*

## 13. Docker Compose commands ([33.2 Docker Compose commands](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-docker-compose.html#docker-compose-commands))

*00:52:06–00:58:03*

- **Q:** How does `docker compose build` relate to `docker build --tag ...`, and why does Daniel prefer it?
    - **A:** It runs the equivalent `docker build` with the name from the file, using the `Dockerfile` in the current folder. Everything is specified in a file, and Daniel likes that because files play well with version control. *(00:53:25)*

- **Q:** Why is `docker compose up` easier than pasting a long `docker run` command?
    - **A:** It reads the file and runs the `docker run` equivalent for every container listed, so you don't have to remember the flags. Long pasted commands often break: spaces and line breaks vary, or someone forgets a backslash. *(00:53:39)*

- **Q:** What does `--detach` change about `docker compose up --detach`?
    - **A:** It starts the container without giving you a prompt inside it. You get your normal terminal back, and the container keeps running in the background. *(00:54:12)*

- **Q:** Interpret the `docker ps -a` row for the demo container.
    - **A:** It gives the container's unique ID, the image it came from (`docker-uv-renv`), and that it was created 16 seconds ago. It also shows port 2222 on the laptop forwarded to the container's port 22, and the name `2026-11-25-docker-validate-analysis-env-1`. The unique ID is the exact reference, since several containers can run from the same image. *(00:54:52)*

- **Q:** Why did `docker compose exec 2026-11-25-docker-validate-analysis-env-1 bash` fail, while `docker compose exec analysis-env bash` worked?
    - **A:** `docker compose` commands work from the compose file, which refers to the container by its service name, `analysis-env`. The full container name isn't a service in the file, so Compose replied `service "2026-11-25-docker-validate-analysis-env-1" is not running`. *(00:55:59)*

- **Q:** Why is changing a setting easier in `docker-compose.yml` than in a long `docker run` command?
    - **A:** A `docker run` command can be twenty lines long, and the mouse doesn't work in your terminal. To fix line two you have to arrow over to it. In a file it is easier to change things, the setup is documented, and you can try things out more easily. *(00:56:47)*

- **Q:** Why did `docker compose down` give `docker: command not found` the first time Daniel ran it?
    - **A:** He was still inside the container, which is a completely different computer with no `docker` command. He had to `exit` first and run `docker compose down` on his laptop. *(00:57:27)*

- **Q:** Why be diligent about running `docker compose down` when you're finished?
    - **A:** Containers are essentially other computers, and each one takes up RAM. If several are running at once, your computer's free memory keeps getting smaller. *(00:57:38)*

## 14. Running commands non-interactively ([33.3 Running a Docker container non-interactively using the Docker Compose](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-docker-compose.html#running-a-docker-container-non-interactively-using-the-docker-compose))

*00:58:03–01:01:10*

- **Q:** Explain what `docker compose run --rm analysis-env <command>` does, compared with opening `bash` in the container.
    - **A:** It runs the given command in a container for the `analysis-env` service. Then `--rm` turns that container off when the command is done. Where `bash` gave an interactive prompt, you can put any Bash command instead. *(00:58:49)*

- **Q:** Why did `docker compose run --rm analysis-env python` fail with `executable file not found in $PATH`?
    - **A:** In this container, Python runs through `uv`, not as a plain `python` command. The working command was `docker compose run --rm analysis-env uv run python`. *(00:59:15)*

- **Q:** Why might plain `python` cause trouble even in a prebuilt image where it does exist?
    - **A:** A prebuilt Python image probably has Python installed, but your packages were installed with `uv`. Calling normal Python means the packages aren't there, because they are two different installations. *(00:59:22)*

- **Q:** Why does Daniel take care to stay in `uv` mode when teaching MDS?
    - **A:** He has Python installed in about four different ways on his computer. It is very easy to slip out of the self-contained `uv` mode, and then things go horribly wrong. *(00:59:57)*

- **Q:** How does running `uv run quarto render` through the container connect to the course's goal of reproducibility?
    - **A:** You can tell the container to build your analysis directly, which checks that it works in the custom environment you made, not just on your laptop. You made a machine, and sending it commands is how you test it. That is how you make something reproducible. *(01:01:05)*

## 15. Connecting Positron or VS Code to the container over SSH

*01:01:10–01:06:55*

- **Q:** Why does Positron connect to the container through Remote SSH, when VS Code can open a container directly?
    - **A:** Positron and Cursor are forks of VS Code. The Microsoft extensions are Microsoft-only, and forks don't have access to Microsoft's extension store. Remote SSH connects to any machine, including the container running on your computer. *(01:02:35)*

- **Q:** Why does the Remote SSH connection use the username `root`?
    - **A:** The container's prompt showed `root@...`, so `root` is the user in the container. If you leave the username out, the connection uses your own computer's username, which isn't a user in the container. *(01:03:12)*

- **Q:** Why does the connection go to `localhost` and not to some address on the internet?
    - **A:** The container runs on your own computer, on a port. The compose file maps that port as 2222 on the laptop to 22 in the container. The connection goes from Positron to that port on your machine. *(01:03:26)*

- **Q:** Compare the two ways of working that Daniel described: mounting the folder and testing, versus connecting the editor to the container.
    - **A:** With a mount only, you work and run everything on your own computer, then test it separately in the container. When the editor is connected, the folders are mounted, but every command runs in the container. The prompt shows `root@...`, so in theory you only need to run things once. *(01:04:24)*

- **Q:** Why does Daniel usually test locally and run only the last command in the container?
    - **A:** That way, not everything is open and running at the same time. *(01:05:11)*

- **Q:** How is connecting Positron to a container the same as cloud computing?
    - **A:** Cloud computing is connecting to another machine through the internet, often one with more resources than yours. Daniel's datasets used about 100 GB of RAM, so he connected Positron to a 128 GB machine rather than work only in a terminal. Docker stands in for any remote machine. *(01:06:13)*

- **Q:** Why does Daniel say not to keep Docker running if your laptop is resource-constrained?
    - **A:** A running container uses resources such as RAM, and on a constrained machine you want to save as much RAM as you can. The Remote SSH connection isn't tested in milestones, so it is something to explore only if you want to. *(01:06:42)*

## 16. Docker Compose beyond this course ([33 Containers: Docker Compose](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-docker-compose.html))

*01:06:55–01:08:33*

- **Q:** Why does Daniel say Docker Compose isn't a skill that only applies to MDS?
    - **A:** Many open-source tools run their services through Docker Compose files. Examples are Ollama, n8n, Jellyfin and Actual Budget. *(01:07:32)*

- **Q:** Explain how the Actual Budget compose file relates to the course's `docker-compose.yml`.
    - **A:** It has the same kinds of pieces: `services`, an image, a port, environment variables and volumes. The same `docker compose up -d` or `docker compose run` starts it, here as a personal finance app on a local port. *(01:08:04)*

- **Q:** How did Daniel suggest practising Compose outside class?
    - **A:** Install Linux on an old laptop and run everything in containers. He runs a computer in his closet this way. *(01:08:08)*

## 17. Why validate data, and exploring missing values ([41.1 Where are the missing values?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/data-validation-python-pointblank.html#where-are-the-missing-values))

*01:10:16–01:13:41*

- **Q:** Why validate a dataset before fitting models? Give an example from class.
    - **A:** You want to make sure the data actually contains the values you expect. In a health dataset you probably don't expect pregnant men, or you want a check that shows those rows if they exist. A BMI above some upper bound is probably a problem. *(01:12:01)*

- **Q:** Why are `99`s in health survey data a validation concern?
    - **A:** Some surveys code a missing value as `99` instead of leaving it missing. Those are not real values, so they end up in places where they can't be right. The codebook tells you how missing values were coded. *(01:12:15)*

- **Q:** What pattern should missing values have, and what should you do if they don't?
    - **A:** As in your stats classes, missing values should be kind of random. If they aren't, you should do something about it or figure out why. *(01:12:15)*

- **Q:** Interpret the `pb.missing_vals_tbl(data=penguins)` output for the penguins data.
    - **A:** It reports missing values for each column, with the rows broken up into sections. Much of the missingness was near the beginning of the data. Daniel guessed that might be the order the data was collected in, perhaps because penguins squirm on the scale. *(01:13:18)*

- **Q:** Why does Daniel call reading the missing values table subjective?
    - **A:** It gives a visual view of whether the data has holes somewhere. Deciding what those holes mean is a judgment call, not a pass or fail. *(01:13:18)*

## 18. Building a validation with thresholds ([41.2 Checking values](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/data-validation-python-pointblank.html#checking-values))

*01:13:41–01:18:29*

- **Q:** Explain how a pointblank validation works, from `pb.Validate()` to `.interrogate()`.
    - **A:** You create a testing object with `pb.Validate()` and chain on the checks you want, but nothing has run yet. `.interrogate()` then tells pointblank to actually do all of those checks and report back. *(01:17:12)*

- **Q:** What do `thresholds=(0.01, 0.05, 0.10)` mean in `pb.Validate()`?
    - **A:** They set the failure rates, 1%, 5% and 10%, at which pointblank starts flagging a step with warning levels. You decide how much failure you tolerate. For example, 10% missing might deserve a flag, while 1% might be fine to leave alone silently. *(01:14:20)*

- **Q:** Why check the `species` column with `col_vals_in_set()`?
    - **A:** It confirms in code that the column holds only the expected values. Data entered by people may have inconsistent capitalization, for example. If you have assumed only those values occur, this tests that assumption. *(01:15:19)*

- **Q:** What does `col_vals_between(columns="bill_length_mm", left=30, right=60, ...)` check, and why would you use such a check?
    - **A:** It checks that bill length is between 30 and 60, inclusive by default, with an option for non-inclusive bounds. You use it when you don't expect a value below or above some limit, as with BMI. A value outside the range is probably bad, or at least worth checking. *(01:16:25)*

- **Q:** Why add `rows_distinct()` to a validation?
    - **A:** It checks that each row is different, so there are no duplicate rows. Duplicates can arise from sensor readings, or when several people code the same thing. *(01:16:52)*

- **Q:** Why are data checks placed at several points in an analysis, rather than in one block?
    - **A:** The checks depend on what you are doing at that point in the analysis. Two such points are right after data cleaning and right before modelling. Placing checks at different points is also a way to break up work in a team. *(01:17:47)*

- **Q:** Interpret the report table pointblank shows when you display the validation object.
    - **A:** Each check gets an actual pass/fail rate, coloured according to the thresholds it reached. It lets you see visually what passes and what doesn't. Before Daniel edited it, every check on the penguins data passed. *(01:18:20)*

## 19. Failing checks and splitting passing and failing rows ([41.4 Splitting the passing and failing rows](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/data-validation-python-pointblank.html#splitting-the-passing-and-failing-rows))

*01:18:29–01:20:48*

- **Q:** Daniel changed the allowed set to `["Adelie", "Chinstrap"]`. Interpret what the report showed.
    - **A:** He removed one species from the set the check allows. The data clearly still contains values of that species, so the step now failed and the report started throwing warnings. *(01:18:29)*

- **Q:** Summarize how Daniel recommended organizing checks for missing values.
    - **A:** He highly recommended doing missing values as a separate analysis from the value checks. Check missingness per column, then per row. *(01:18:52)*

- **Q:** Why shouldn't downstream work wait until the data is completely clean?
    - **A:** In more complicated projects, and in capstone, data will never be 100% clean. Waiting for it would hold up the rest of the work. *(01:19:20)*

- **Q:** How does splitting a validation into passed and failed data frames with `get_sundered_data()` help a team?
    - **A:** pointblank gives one data frame of rows that passed and another of rows that failed. The passing rows go to the next team member to build the rest of the pipeline, including their own preprocessing. You keep cleaning the failed rows. *(01:19:52)*

- **Q:** What problem does handing a teammate only the passing rows avoid?
    - **A:** If the full data still has problems, their model may not fit: things may be correlated, or it may not converge because of bad data. With the good data they aren't hung up waiting on your cleaning. *(01:20:19)*

- **Q:** Why does it matter that the passed and failed rows are ordinary data frames?
    - **A:** You can save them out as CSV files. Then they are actual datasets that someone else can pick up while the cleaning is still in progress. *(01:20:32)*

---

- prompt: prompt-recall-2-understand.md @ 65eb21c
- prompt-hash: 17df43f38e78
- model: claude-opus-5-5 (requested: opus)
- backend: claude
- inputs: transcript-plaud.md, terminal.txt, materials.md, notes-class-main--claude-opus-5-5.md
- generated: 2026-11-25
- notes-input: notes-class-main--claude-opus-5-5.md @ 06f3ac544b79, links and section references removed
