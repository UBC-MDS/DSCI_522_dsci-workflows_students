# Docker Compose and data validation with pointblank: review questions, tier 3 — Apply

Date: 2026-11-25

Instructor: Daniel Chen

*Tier 3 of 5: Apply. Work each situation through before you read the answer; tiers 1 (Remember) and 2 (Understand) cover the facts and reasons it relies on.*

## 1. Creating and cloning the repository

*00:04:52–00:07:44*

- **Q:** You are about to clone your new project repository, but your terminal is sitting inside another project's folder. Where should you clone instead, and what does this avoid?
    - **A:** Clone into a folder that is not inside any Git repository, such as a dedicated `~/git` folder that holds every repository side by side. Cloning into another project's folder would nest one Git repository inside another, which you never want. A single folder of repositories is always a safe place to clone into. *(00:06:22)*

- **Q:** You run `git clone git@github.com:chendaniely/2026-11-25-docker-validate.git` from `~/git` and then `positron .`. The editor's file explorer shows all of your repositories instead of the new one. What do you run to fix it?
    - **A:** Run `cd 2026-11-25-docker-validate` and then `positron .` again. The first `positron .` opened the editor in `~/git`, the parent folder, not in the folder you cloned. Opening the repository's own folder means you aren't navigating through subfolders. *(00:07:09)*

- **Q:** You want a new demo repository on your computer that isn't empty from the start. In order, what do you do?
    - **A:** First create the repository on GitHub, online, and add a `README.md` so it has some content. Then copy its URL, go to your repositories folder in the terminal, and run `git clone` with that URL. Finally, `cd` into the cloned folder and open your editor there. *(00:05:24)*

## 2. The `Dockerfile`: base image and system software ([29.3 Choosing a base image for your Dockerfile](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#choosing-a-base-image-for-your-dockerfile))

*00:08:59–00:13:18*

- **Q:** Your group's project uses only Python, and the `Dockerfile` you copied starts with `FROM rocker/r-ver:4.6.2`. Will it work, and what should you consider changing?
    - **A:** It will work, because `rocker/r-ver` is an Ubuntu image with R pre-installed on top. However, the R parts take up extra storage, so anyone who uses your image, including the TAs grading it, has a longer download. Choose a smaller base image that has only what you need, such as a plain Ubuntu image. *(00:09:51)*

- **Q:** You add PyTorch or a geospatial package to your project, and it fails inside the container because it needs non-Python system software, such as a C compiler. Where do you fix this?
    - **A:** Install the missing software in the `Dockerfile` with a `RUN apt-get ...` command, then rebuild the image. `apt-get` is Ubuntu's way of installing software. The `Dockerfile` is where system software goes, because some Python packages rely on tools that aren't written in Python. *(00:11:51)*

- **Q:** Your milestone container has to render your Quarto report, but you deleted the Quarto section from the `Dockerfile`. In order, what do the `RUN` commands you put back have to do?
    - **A:** First download the Quarto installer file, then install it with `apt-get`, then delete the downloaded file. This is the terminal version of downloading an installer and double-clicking it. Without these steps, the container can't render your report. *(00:12:30)*

## 3. Installing `uv` and controlling tool versions ([29.2 `Dockerfile` command summary](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#dockerfile-command-summary))

*00:13:18–00:15:30*

- **Q:** You and a teammate have identical `pyproject.toml` and `uv.lock` files, but you could end up running different versions of `uv` itself. What doesn't the project track, and what line in the `Dockerfile` fixes it?
    - **A:** `pyproject.toml` doesn't track the version of `uv`. Pin it in the `Dockerfile` by copying the binaries from a tagged `uv` image: `COPY --from=ghcr.io/astral-sh/uv:0.13.7 /uv /uvx /usr/local/bin/`. Docker exists to control the tools as well as the packages. *(00:14:57)*

- **Q:** A package's documentation tells you to install it from a `requirements.txt` file. How do you proceed in your MDS project?
    - **A:** Don't copy and paste the instructions blindly. Your project manages Python through `uv`, and instructions written for other workflows may not be `uv`-compatible. Add the package to your `uv` project instead. *(00:13:47)*

- **Q:** You want to skip the `COPY --from=ghcr.io/astral-sh/uv:0.13.7 ...` step in your `Dockerfile`. What can you use instead, and what might you have to look up if something breaks?
    - **A:** Start from one of the prebuilt `uv` images, which already have `uv` installed. If you run into a problem, you may need to find out where `uv` is installed on that particular image. *(00:15:20)*

## 4. `WORKDIR` and the `.venv` problem ([29.2 `Dockerfile` command summary](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#dockerfile-command-summary))

*00:15:30–00:19:28*

- **Q:** Your `Dockerfile` contains `WORKDIR /workspace`, and the base image has no `/workspace` folder. Predict what happens at build time, and where you land when you start the container with `bash`.
    - **A:** Docker creates `/workspace` for you, so `WORKDIR` works like `mkdir` and `cd` at once. When the container starts, you land in `/workspace`, among your project files, instead of at the root of the operating system. *(00:16:32)*

- **Q:** You ran `uv sync` on your Mac, which created `.venv`, and you mount the project folder into a container built without an `ENV UV_PROJECT_ENVIRONMENT` line. The Python environment doesn't work inside the container. Why not, and what do you add to the `Dockerfile`?
    - **A:** The mounted `.venv` was built for your laptop's operating system and CPU, not for the container's Linux. Add `ENV UV_PROJECT_ENVIRONMENT=/opt/venv` before `RUN uv sync --locked`. `uv` then installs the Linux packages from `uv.lock` into `/opt/venv`. *(00:18:25)*

- **Q:** Your image sets `UV_PROJECT_ENVIRONMENT=/opt/venv`, and you mount a project folder that contains your laptop's `.venv`. Predict which environment each machine uses.
    - **A:** The container uses `/opt/venv`, which was built for Linux when the image was built. The mounted `.venv` is simply ignored inside the container. Your laptop keeps using its own `.venv`, so the project works in both places. *(00:19:28)*

## 5. Environment variables, `uv sync --locked`, and the SSH setup ([29.2 `Dockerfile` command summary](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#dockerfile-command-summary))

*00:27:21–00:30:18*

- **Q:** Your `Dockerfile` sets `ENV UV_PROJECT_ENVIRONMENT=/opt/venv`, but when your editor connects to the container over SSH, `uv` ignores that location. What line fixes it?
    - **A:** SSH logins don't read `ENV` variables, so save the variable to a file as well: `RUN echo "UV_PROJECT_ENVIRONMENT=$UV_PROJECT_ENVIRONMENT" >> /etc/environment`. `echo` prints exactly what you give it, and `>>` appends that one line to the end of `/etc/environment`. *(00:28:46)*

- **Q:** You edit `pyproject.toml` to add a package but don't update `uv.lock`, then build the image. The `Dockerfile` runs `RUN uv sync --locked`. Predict the result, and say how you fix it.
    - **A:** The build fails, because `--locked` stops when `pyproject.toml` and `uv.lock` are out of sync. This guard checks that what you get is what you expect. To fix it, run `uv sync` on your computer, which updates `uv.lock` from the TOML file, then rebuild. *(00:29:15)*

- **Q:** You are on a Linux laptop and want to connect your editor to the container over SSH. What do you change in the demo `Dockerfile`?
    - **A:** Uncomment the extra line that is there for Linux laptops: `RUN echo "StrictModes no" > /etc/ssh/sshd_config.d/container.conf`. The SSH server wants `root` to own the key file, but on Linux the mounted key file is owned by you. *(00:29:54)*

## 6. `pyproject.toml` and `.python-version`

*00:30:18–00:33:30*

- **Q:** Your `pyproject.toml` has `add-bounds = "exact"` under `[tool.uv]`, and you run `uv add` for a package. Predict how the dependency is written.
    - **A:** `uv add` writes an exact pin with `==`, not a `>=` lower bound. This is a `uv` setting stored in a file, and `uv` reads it whenever you add a package. *(00:31:24)*

- **Q:** You want packages installed into `/opt/venv`, and you consider setting that location in `pyproject.toml` instead of in the `Dockerfile`. What would happen?
    - **A:** You probably could set it there, but your laptop would then install into `/opt/venv` too. The goal is for Docker to behave slightly differently from your own computer. That's why this setting belongs in the `Dockerfile`'s `ENV` line. *(00:31:47)*

- **Q:** One of your projects needs an older version of Python than your others, for example because PyTorch lags behind new Python releases. How do you handle it without changing your whole computer?
    - **A:** Put the version that project needs in its `.python-version` file. `uv` reads that file and downloads that Python version for that project only. Each project can use its own Python version, not just its own package versions. *(00:32:53)*

## 7. Generating `uv.lock` and building the image ([29.4 Dockerfile FAQ](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#dockerfile-faq))

*00:33:30–00:35:47*

- **Q:** Your folder contains `Dockerfile`, `pyproject.toml` and `README.md`, but no `uv.lock`. The `Dockerfile` has the line `COPY pyproject.toml uv.lock .python-version ./`. What do you run before you build?
    - **A:** Run `uv sync`. It installs the packages, creates `.venv` and writes `uv.lock`. All the files the `Dockerfile` copies are then present, so you can build. *(00:34:16)*

- **Q:** Complete the command that builds an image named `docker-uv-renv` from the `Dockerfile` in your current folder, and say what its last character does.
    - **A:** The command is `docker build --tag docker-uv-renv .` (you can write `-t` for `--tag`). The final `.` is the current working directory, where `docker build` looks for a file called `Dockerfile` by default. *(00:35:06)*

- **Q:** You watch `docker build` run the demo `Dockerfile`. In what order do the steps appear?
    - **A:** It starts from the base image, then copies `uv`, sets the working directory, sets the environment variable, copies `pyproject.toml`, `uv.lock` and `.python-version`, and finally runs `uv sync --locked`. *(00:35:29)*

## 8. Running the container interactively

*00:35:47–00:38:22*

- **Q:** Complete a command that gives you a bash prompt inside a new `docker-uv-renv` container and removes the container when you leave.
    - **A:** Run `docker run --rm -it docker-uv-renv bash`. `--rm` removes the container when you exit. `-it` is two single-character flags chained together: `-i` for interactive mode and `-t` for a terminal prompt. `bash` at the end starts Bash. *(00:36:22)*

- **Q:** At the prompt `root@69b50dc7fa19:/workspace#`, you type `python`. Predict the result and give the fix.
    - **A:** You get `bash: python: command not found`, because the container has no plain `python`. Run `uv run python` instead, which starts the project's Python with everything `uv` installed. *(00:37:52)*

- **Q:** You try to leave the container by typing `quit` at its bash prompt. Predict what happens, and what you should type instead.
    - **A:** Bash replies `bash: quit: command not found`, and you stay in the container. Type `exit` to leave. *(00:38:12)*

- **Q:** You have several terminal windows open and aren't sure whether one of them is your laptop or the container. How do you check?
    - **A:** Read the prompt, which shows the username and the computer you are on. In the container it is `root@<container id>:/workspace`. `pwd` shows `/workspace`, a folder that doesn't exist on your laptop, and `whoami` prints `root`. *(00:37:44)*

## 9. Mounting the project folder with `-v`

*00:38:22–00:42:42*

- **Q:** Complete a command that starts an interactive bash prompt in `docker-uv-renv` with your current folder available at `/workspace`.
    - **A:** Run `docker run --rm -v "$(pwd):/workspace" -it docker-uv-renv bash`. `-v` mounts your current working directory into the container's `/workspace` folder. The command is written with `$(pwd)` because `.` alone doesn't always work on both Windows and Mac. *(00:39:09)*

- **Q:** You run `docker run --rm -v "$(pwd):/workspace" -it bash`, and Docker prints `Unable to find image 'bash:latest' locally` and starts downloading. What went wrong, and how do you fix it?
    - **A:** You left out the image name, so Docker treated `bash` as the image and began pulling it from Docker Hub. Press Ctrl-C, then re-run the command with the image name before `bash`: `docker run --rm -v "$(pwd):/workspace" -it docker-uv-renv bash`. *(00:42:44)*

- **Q:** Your analysis files change every few minutes, and you are deciding whether to `COPY` them into the image or mount them. Which do you choose, and why?
    - **A:** Mount them with `-v`. `COPY` captures the files as they were at `docker build` time, so you would have to rebuild for every change. Keep only the software in the image and mount the files. *(00:40:18)*

- **Q:** You are working in the mounted container and want to commit and push your changes. Where do you run the Git commands, and why shouldn't you set up your credentials inside the image?
    - **A:** Run `git add`, `git commit` and `git push` on your laptop, because the mounted files already show up there. The container resets every time it restarts, and GitHub sees it as a new machine each time. Never bake your SSH key into the image: it is effectively the password to your account, and anyone who pulls the image could find it. *(00:41:50)*

- **Q:** Your project is finished, and you have to submit a frozen version for compliance. Should you still mount the files?
    - **A:** No. In this case, `COPY` the files in so they become part of the image itself. Mounting is for active work, so that you don't have to keep rebuilding. *(00:42:20)*

- **Q:** You run a database container that stores its data in several different folders. How do you mount all of them?
    - **A:** Add one `-v` option for each folder. This is common with databases, and it's how you back up their data from the container. *(00:39:36)*

## 10. Shared files and editing in two places

*00:42:42–00:44:42*

- **Q:** Inside a container started with `-v "$(pwd):/workspace"`, you run `touch hello.py` and then `exit`. Predict what `ls` shows on your laptop.
    - **A:** `hello.py` is there, next to the other project files. The mounted folder works like a network share drive: both sides are working on the same files, and changes show up almost immediately. *(00:43:06)*

- **Q:** You have a file open in Positron on your laptop and edit the same file inside the container. Predict what the open editor tab shows.
    - **A:** It still shows the old contents, because the editor doesn't automatically reload a file that changed on the other side. Use the editor's "revert file" command to reload the file from disk before you edit it. *(00:43:44)*

- **Q:** You edited a file in the container, then saved the same file in Positron and chose "overwrite" when prompted. Your container edits are gone. What happened, and how do you avoid it next time?
    - **A:** Overwriting replaced the version on disk, so the other side's changes were lost. It's effectively a Git conflict without Git to help you. As on a network drive, the last save wins. When you know you are working in more than one place, revert the file before editing it. *(00:43:59)*

## 11. The `docker-compose.yml` file ([33.1 Docker Compose to launch containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-docker-compose.html#docker-compose-to-launch-containers))

*00:44:42–00:52:06*

- **Q:** You want your `docker-compose.yml` to do the work of `docker build --tag docker-uv-renv .`. Which two lines under the `analysis-env` service do this?
    - **A:** `build: .` builds from the `Dockerfile` in this folder if the image doesn't exist yet. `image: docker-uv-renv` gives the image its name, like `--tag`. *(00:47:06)*

- **Q:** Your compose file has `ports:` with `"2222:22"`. Which port do you use to reach the container's SSH server from your laptop?
    - **A:** Use port 2222. The first number is the port on your computer and the second, 22, is the port inside the container. Port 22 is used by real services, so remapping it avoids a clash with your own computer. *(00:48:18)*

- **Q:** You follow someone else's compose file, open the service at the port the software normally runs on, and it "doesn't work". What do you check?
    - **A:** Check the first number in the `ports:` mapping, because that is where the service is on your computer. People may remap a port to any number they like. If you are looking at the container's port instead, you are looking in the wrong place. *(00:49:43)*

- **Q:** You want a second container from the `docker-uv-renv` image for another Python project, alongside `analysis-env`. What do you change in the compose file?
    - **A:** Add another service with a different name, such as `analysis-env2`, using the same image. Two services can't have the same name, but they can share the same setup. *(00:46:42)*

- **Q:** The container needs your SSH public key so you can log in to it. How should it get there, and what should you avoid?
    - **A:** Mount it under `volumes:`, for example `~/.ssh/id_ed25519.pub:/root/.ssh/authorized_keys:ro`, so the key is in the container only while the container runs. Don't copy it permanently into the image. *(00:50:19)*

- **Q:** Inside a running container, you install some packages and delete a few system files, then stop it and start it again. Predict what you find.
    - **A:** The container is reset to how it was built: the packages are gone and the deleted files are back. Only changes in mounted folders survive, because those files live on your computer. *(00:50:38)*

- **Q:** You want to try a messy PyTorch install that needs several other installs, and you aren't sure it will work. Where should you experiment, and what must you never do on your own computer?
    - **A:** Experiment inside a container. If the install fails, turn the container off and on again to reset it, and try again. A destructive command such as `rm -rf /` is only safe to try in a container, where restarting restores everything. Never run it on your own computer. *(00:51:42)*

## 12. Docker Compose commands ([33.2 Docker Compose commands](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-docker-compose.html#docker-compose-commands))

*00:52:06–00:58:03*

- **Q:** You are in the folder with `docker-compose.yml`. In order, what do you run to build the image, start the container in the background, open a shell in it, and finally shut it down?
    - **A:** Run `docker compose build`, then `docker compose up --detach`, then `docker compose exec analysis-env bash`. Type `exit` to leave the shell, then run `docker compose down`. Every command reads the compose file in the folder you are in. *(00:53:07)*

- **Q:** You run `docker compose up` and want your normal terminal back while the container keeps running. Which option do you add?
    - **A:** Add `--detach`: `docker compose up --detach`. The container runs in the background, and you get your laptop's prompt back instead of the container's. *(00:54:12)*

- **Q:** You want to confirm the container is running and see its port mapping and name. What do you run, and what do you look for?
    - **A:** Run `docker ps -a`. Look for the row with the image `docker-uv-renv` and status `Up`. That row shows the ports `0.0.0.0:2222->22/tcp` and the name `2026-11-25-docker-validate-analysis-env-1`. *(00:54:52)*

- **Q:** You copy the name from `docker ps -a` and run `docker compose exec 2026-11-25-docker-validate-analysis-env-1 bash`. You get `service "2026-11-25-docker-validate-analysis-env-1" is not running`. Fix it.
    - **A:** `docker compose` commands take the service name from the compose file, not the full container name. Run `docker compose exec analysis-env bash`. *(00:55:59)*

- **Q:** At the prompt `root@5e67a11e10f2:/workspace#`, you type `docker compose down` and get `bash: docker: command not found`. What went wrong, and what do you do?
    - **A:** You are inside the container, which is a different computer with no `docker` command. Type `exit` to get back to your laptop, then run `docker compose down` there. *(00:57:27)*

- **Q:** After a few days of starting containers, your laptop is running low on memory. What is likely happening, and what do you run?
    - **A:** Each running container is effectively another computer using RAM. Run `docker compose down` in each project when you are done, which reads the compose file and turns its containers off. *(00:57:38)*

## 13. Running commands non-interactively ([33.3 Running a Docker container non-interactively using the Docker Compose](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-docker-compose.html#running-a-docker-container-non-interactively-using-the-docker-compose))

*00:58:03–01:01:10*

- **Q:** You want to run one command in a new `analysis-env` container that removes itself when the command finishes. Complete the command.
    - **A:** Run `docker compose run --rm analysis-env <command>`. `--rm` turns the container off and removes it once the command is done. Any Bash command can go where `bash` went before. *(00:58:29)*

- **Q:** `docker compose run --rm analysis-env python` fails with `exec: "python": executable file not found in $PATH`. Fix the command.
    - **A:** Run `docker compose run --rm analysis-env uv run python`. The container runs Python through `uv`, so it has no plain `python` on its `PATH`. *(00:59:15)*

- **Q:** You want to check that your Quarto report builds in the project's container, without opening a shell in it. What do you run?
    - **A:** Run `docker compose run --rm analysis-env uv run quarto render`, naming your report file if you need to. This sends your custom machine a command, which is how you test that the analysis reproduces there. *(01:00:35)*

- **Q:** You switch to a prebuilt Python image. Plain `python` now starts, but your `uv`-installed packages aren't available. Diagnose the problem.
    - **A:** That image's `python` is a separate installation from the one `uv` manages, so the packages you installed with `uv` aren't there. Keep using `uv run python`. Stepping outside the self-contained `uv` setup is when things go horribly wrong. *(00:59:22)*

## 14. Connecting Positron or VS Code to the container over SSH

*01:01:10–01:06:55*

- **Q:** You want Positron, a VS Code fork, to work inside the `analysis-env` container. In order, what do you do?
    - **A:** Start the container in the background with `docker compose up --detach`. Then use Remote SSH to connect as user `root` to `localhost` on port 2222, the laptop side of the `"2222:22"` mapping. Forks like Positron can't use Microsoft's container extension, so they connect over Remote SSH instead. *(01:03:26)*

- **Q:** You set up the Remote SSH connection to `localhost` on port 2222, but you leave out the username. Predict the result.
    - **A:** The connection uses your laptop's username by default, and that user doesn't exist in the container. Give the username `root`, which is the user shown in the container's prompt. *(01:03:12)*

- **Q:** Positron is now connected to the container. Which folder do you open, and how do you confirm your commands run in the container?
    - **A:** Open `/workspace`, where the project folder is mounted. The terminal prompt then shows `root@...`, so every command runs inside the container. *(01:04:39)*

- **Q:** Your dataset needs about 100 GB of RAM, far more than your laptop has, but you don't want to work only in a terminal. How do you apply the same approach?
    - **A:** Connect Positron with Remote SSH to a large remote machine. All your work then runs on that machine, while you keep your editor's tools. The container is a stand-in for any remote machine you connect to over the internet. *(01:05:49)*

- **Q:** Your laptop is short on memory, but you still want to confirm that your analysis runs in the container. How do you organize your work?
    - **A:** Work and test on your laptop, then run only the final command in the container, so that fewer things are running at once. If resources are tight, don't keep Docker running when you don't need it. *(01:06:42)*

## 15. Adding the validation packages

*01:08:33–01:10:16*

- **Q:** You run `uv add pandera pointblank` and get `error: Project is missing a [project] table`. What is a workaround that still gets the packages installed and locked?
    - **A:** Add the packages to `dependencies` in `pyproject.toml` by hand, then run `uv sync`. `uv sync` resolves and installs the packages, and updates `uv.lock` from the TOML file. *(01:09:59)*

- **Q:** You add `pointblank` to `pyproject.toml` by hand, skip `uv sync`, and run `docker compose build`. The `Dockerfile` runs `RUN uv sync --locked`. Predict the result.
    - **A:** The build fails, because `uv.lock` no longer matches `pyproject.toml` and `--locked` refuses to continue. Run `uv sync` first to update the lock file, then build again. *(00:29:15)*

- **Q:** Your validation script uses `import pointblank as pb` and loads its data with `from palmerpenguins import load_penguins`. Which packages must be in your project's dependencies?
    - **A:** Both `pointblank` and `palmerpenguins`, the second to provide the penguins dataset. After adding them, run `uv sync` so they are installed and locked. *(01:10:09)*

## 16. Why validate data, and exploring missing values ([41.1 Where are the missing values?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/data-validation-python-pointblank.html#where-are-the-missing-values))

*01:10:16–01:13:41*

- **Q:** Before you write any rules for the penguins data, you want to see where values are missing. What do you run?
    - **A:** Run `pb.missing_vals_tbl(data=penguins)`. It reports the missing values in each column, with the rows split into sections from the top of the data to the bottom. In the penguins data, much of the missingness falls near the beginning. Reading the table is a judgment call. *(01:12:47)*

- **Q:** You are working with health survey data, and some columns contain the value `99` in places where no real value could be `99`. What do you suspect, and what do you do?
    - **A:** The survey probably coded missing values as `99`. Check the codebook. Then write validation checks so that those values are flagged instead of being treated as real data. *(01:12:15)*

- **Q:** The missing-values table shows the missingness clustered in one part of your data, not scattered across it. What should you do?
    - **A:** Investigate the cause. Missing values should be roughly random, and if they aren't, you should find out why or do something about it. For example, a cluster could come from the order in which the data was collected. *(01:12:42)*

## 17. Building a validation with thresholds ([41.2 Checking values](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/data-validation-python-pointblank.html#checking-values))

*01:13:41–01:18:29*

- **Q:** Your `pb.Validate()` uses `thresholds=(0.01, 0.05, 0.10)`, and 7% of the rows fail one step. Predict the level that step reaches.
    - **A:** It reaches error. The three numbers are the failure rates for warning (1%), error (5%) and critical (10%), and 7% is past the error level but not the critical one. *(01:14:20)*

- **Q:** You want to confirm that the `species` column holds only `"Adelie"`, `"Chinstrap"` and `"Gentoo"`. Which step do you add to the chain?
    - **A:** Add `.col_vals_in_set(columns="species", set=["Adelie", "Chinstrap", "Gentoo"])`. It tests your assumption that the column contains only those values. This catches problems such as inconsistent capitalization in data typed in by people. *(01:14:56)*

- **Q:** You expect every bill length to be between 30 and 60 mm. Which step do you add?
    - **A:** Add `.col_vals_between(columns="bill_length_mm", left=30, right=60)`. The bounds are inclusive by default, and there is an option for exclusive bounds. The same kind of check works for an upper bound on BMI. *(01:16:07)*

- **Q:** Several people coded the same records, and you are worried about duplicate rows. Which step do you add?
    - **A:** Add `.rows_distinct()`, which checks that every row is different from every other. *(01:16:52)*

- **Q:** You chain several rule steps onto `pb.Validate(data=penguins, ...)` but leave out `.interrogate()`. Predict what happens.
    - **A:** None of the checks run. The chain only describes the steps, and `.interrogate()` is what actually carries them out. Add `.interrogate()` at the end of the chain, then display the object to see the report. *(01:17:12)*

- **Q:** You are deciding where in your project's analysis to put your validation code. Where do the checks go?
    - **A:** Put checks right after data cleaning and again right before modelling. The right checks depend on the stage of the analysis, so you validate in several places rather than in one block. These stages are also a natural way to split the work in your team. *(01:15:31)*

## 18. Failing checks and splitting passing and failing rows ([41.4 Splitting the passing and failing rows](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/data-validation-python-pointblank.html#splitting-the-passing-and-failing-rows))

*01:18:29–01:20:48*

- **Q:** You change the step to `.col_vals_in_set(columns="species", set=["Adelie", "Chinstrap"])` and re-run the validation on the penguins data. Predict the report.
    - **A:** That step fails, because the data clearly contains Gentoo penguins. Its row in the report shows a failure rate and is coloured by the threshold it reached, and warnings start being thrown. *(01:18:29)*

- **Q:** You are about to add missing-value checks to the same chain as your value-range checks. How should you organize them?
    - **A:** Write a separate validation just for missing values, checked per column and then per row. Keep it apart from the value checks, so that a value out of range and a missing value are reported separately. *(01:18:52)*

- **Q:** A teammate is waiting for your data cleaning to finish before they can build the modelling part of the pipeline. How can you unblock them?
    - **A:** After interrogating, split the data with `values.get_sundered_data(type="pass")` and `values.get_sundered_data(type="fail")`. Give the passing rows to your teammate so they can build their part of the pipeline now. Keep cleaning the failing rows yourself, because data will never be 100% clean. *(01:19:36)*

- **Q:** You want someone else to pick up and fix the failing rows from `get_sundered_data(type="fail")`. How do you hand them over?
    - **A:** Save them to a CSV file. The result is an ordinary data frame, so writing it to CSV gives your teammate a real dataset to work from. *(01:20:32)*

---

- prompt: prompt-recall-3-apply.md @ 65eb21c
- prompt-hash: 49276171f719
- model: claude-opus-5-5 (requested: opus)
- backend: claude
- inputs: transcript-plaud.md, terminal.txt, materials.md, notes-class-main--claude-opus-5-5.md
- generated: 2026-11-25
- notes-input: notes-class-main--claude-opus-5-5.md @ 06f3ac544b79, links and section references removed, diagrams removed
