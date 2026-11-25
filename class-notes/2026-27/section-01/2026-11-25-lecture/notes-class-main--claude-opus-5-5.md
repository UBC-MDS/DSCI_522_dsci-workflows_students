# Docker Compose and Data Validation with pointblank

Date: 2026-11-25

Instructor: Daniel Chen

## Summary

Daniel Chen taught this section in place of its usual instructor. He started with a hands-on review. Students created a GitHub repository and copied in the `Dockerfile` and `pyproject.toml` from a reference repository. They generated `uv.lock`, built an image and got a Bash prompt inside it. He then walked through the `Dockerfile` line by line:

- why the base image matters;
- how `RUN apt-get` installs system software;
- how uv is copied in from its own image;
- what `WORKDIR` does;
- why `UV_PROJECT_ENVIRONMENT=/opt/venv` keeps the container's Python packages away from your laptop's `.venv` when the project folder is mounted.

A short movement break, run by a guest, interrupted the review. After it, he built and ran the image, mounted the project folder with `-v`, and showed a file created inside the container appearing straight away on the laptop.

The new material was **Docker Compose**. Long `docker run` commands are hard to edit and poorly documented. A `docker-compose.yml` file records the image, how to build it, the port mapping and the volumes, and it can be version controlled. The class used these commands:

- `docker compose build` to build the image;
- `docker compose up --detach` to start the container in the background;
- `docker compose exec` to get a shell in the running container;
- `docker compose down` to stop it;
- `docker compose run --rm` to send one command to a fresh container, which is how a milestone's analysis can be checked inside its own environment.

He also showed Positron connecting to the running container over SSH as a stand-in for cloud computing. He pointed out that many self-hosted tools ship as Compose files.

The last part introduced **data validation with pointblank** on the Palmer penguins data:

- a table of where the missing values are;
- a `Validate` object with warning, error and critical thresholds;
- rules for allowed values, numeric ranges and duplicate rows, run with `interrogate()`;
- splitting the data into passing and failing rows, so teammates can keep working while cleaning continues.

This sets up next week's work: data validation checks, and breaking analysis code into smaller pieces.

## Key takeaways

- Choose the smallest base image that does the job, because everyone who uses your container has to download it.
- Setting `UV_PROJECT_ENVIRONMENT=/opt/venv` in the `Dockerfile` installs the container's packages outside the project folder, so a mounted laptop `.venv` built for another operating system is ignored.
- Mount your project with `-v` (or a Compose `volumes:` entry) while you are actively working; copy files into the image only for a final, frozen version.
- A `docker-compose.yml` records everything a long `docker run` needs, so `docker compose up --detach`, `exec`, `run --rm` and `down` replace commands you would otherwise retype.
- Inside the MDS containers Python is reached through uv: `uv run python`, not `python`.
- pointblank chains rules onto `pb.Validate(...)` and only checks them when you call `.interrogate()`, reporting pass/fail rates against your thresholds.
- Validate values and missingness separately, and at several points in your pipeline, not in one block at the end.

## Knowledge Points

### 1. Review exercise and session setup

*00:00:00–00:04:52*

- **Different teaching style**: Daniel does not teach from slides. Every command and every line of code is typed live, so students can follow along.
- **The review task**, done in the first few minutes:
  - create a GitHub repository and clone it;
  - copy the `.py` file and `pyproject.toml` from the reference repository (<https://github.com/chendaniely/docker-uv-renv>), whose link was also posted in Slack;
  - generate `uv.lock` yourself rather than copying it;
  - build the container from the `Dockerfile`;
  - get a Bash prompt out of it.
- **Don't clone the whole reference repository**: it holds much more than the class needed. The point was to bring files over one at a time and understand each one.
- **Generating the lock file is part of the review**: you can copy `uv.lock` over, but you should know how to create it from `pyproject.toml`.

### 2. Creating and cloning the repository

*00:04:52–00:08:59*

- **Create the repository on GitHub first**: this keeps track of your work from the start. Daniel added a `README.md` so the repository was not empty, then cloned the new `2026-11-25-docker-validate` repository with its SSH URL.
- **Keep every repository in one `~/git` folder**: everything in that folder is a Git repository, so nothing is scattered across the computer. It is also a known-safe place to clone into.

> [!WARNING]
>
> Don't nest Git repositories inside one another (from DSCI 521). Cloning into a dedicated `~/git` folder is a simple habit that avoids it.

- **Open the repository folder in your editor, not its parent**: Daniel used Positron (VS Code works too). He first opened it in `~/git` by mistake, then moved into the cloned folder so he wasn't dealing with subfolders.
- **The base template repo is the technical foundation for your milestones**: it shows an example report and most of the pieces the course covers.

> [!WARNING]
>
> Don't blindly copy the template. You are responsible for the work you submit. "No one cares that you can get the work done … it's whether you understand." In Daniel's class, any commit with your name on it is fair game for a question.

### 3. The `Dockerfile`: base image and system software ([29.3 Choosing a base image for your Dockerfile](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#choosing-a-base-image-for-your-dockerfile))

*00:08:59–00:13:18*

- **`Dockerfile`**: the file used to build container images. Its `FROM` line names the starting image. The reference uses `rocker/r-ver:4.6.2`, which is Ubuntu with R pre-installed.
- **Base image size matters**: an R image works for Python projects but takes more storage. Anyone downstream has a longer download, including the TAs grading your milestone.
  - Your Python projects will probably start from a different base. Daniel's own class used an Ubuntu image.
  - The aim is something "small enough, bare minimum" for your work. At the extreme, some images are barely an operating system and you install everything yourself.
- **`RUN`**: runs Bash commands in the image's operating system, which is usually Linux. That is why MDS uses Git Bash.
- **`apt-get`**: Ubuntu's way of installing software. The reference installs tools such as `git` and a text editor (`nano`) so you can work inside the container.
- **System dependencies go here**: some Python packages only work once other software is installed. Examples are PyTorch needing C compilers, and geospatial packages needing non-Python tools.
- **Installing Quarto**: the reference downloads the Quarto `.deb` file, installs it with `apt-get`, then deletes the file. This is the command-line equivalent of downloading an installer and double-clicking it.
  - Daniel deleted that section for today. **Your milestone container must be able to render your report, so it needs Quarto.**

### 4. Installing uv into the image ([29.2 `Dockerfile` command summary](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#dockerfile-command-summary))

*00:13:18–00:15:30*

- **MDS installs Python through uv**: outside MDS, install instructions may not be written for uv. You will often see a `requirements.txt`, which isn't how uv works. MDS teaches one way rather than five.
- **`COPY --from`**: `COPY` brings files from your computer into the image, and it can also copy from another image.
  - uv's documentation offers a pre-built image containing uv.
  - The `Dockerfile` copies the binaries out of it with `COPY --from=ghcr.io/astral-sh/uv:0.13.7 /uv /uvx /usr/local/bin/`.
- **Docker controls the tools, not just the packages**: a virtual environment pins package versions, but `pyproject.toml` does not record which version of uv you used. Pinning the uv image version in the `Dockerfile` does.
- **Alternative**: start from one of the existing pre-built uv images instead, which saves this step. If something breaks, find out where uv is installed on that image.

### 5. `WORKDIR` and keeping the virtual environment out of the mount

*00:15:30–00:19:39*

- **`WORKDIR /workspace`**: Docker's way of saying "`cd` here when you enter the container".
  - Without it you land in the container's root and see operating-system folders instead of your project.
  - If the folder doesn't exist, Docker creates it, so it acts like `mkdir` plus `cd`.
- **Why a project folder is safer**: being in your project means a convenient `rm *` deletes project files, not the operating system.
- **`.venv` is tied to one machine**: `uv sync` creates `.venv` with packages built for your operating system and CPU.
  - There are three operating systems (Windows, macOS, Linux) and two chip types (Intel/AMD and ARM).
  - That makes six kinds of computer to account for, which is the reason Docker is used at all: code should run on someone else's machine.
- **The problem with mounting**: mounting your project folder also mounts your laptop's `.venv`, which doesn't match the container's Linux system.
- **The official fix**: tell uv to keep its environment somewhere else. `UV_PROJECT_ENVIRONMENT=/opt/venv` makes uv install into `/opt/venv`, and the lock file makes those Linux packages match exactly. Later, when you mount the folder, the laptop's `.venv` is simply ignored inside the container.

### 6. Environment variables and the rest of the `Dockerfile` ([29.2 `Dockerfile` command summary](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#dockerfile-command-summary))

*00:27:21–00:30:18*

- **Environment variables**: tools have variables just as your Python code does. They are also called system or global environment variables. `ENV UV_PROJECT_ENVIRONMENT=/opt/venv` sets one that uv reads whenever it runs.
  - Many programs keep settings in hidden folders in your home directory, such as a config folder, so they can adapt to each computer.
- **Saving the variable for SSH logins**: SSH connections don't see `ENV`. The `Dockerfile` therefore appends the variable to `/etc/environment`:
  - `echo` prints exactly what you give it;
  - `>>` appends it to the end of a file.
- **`uv sync --locked`**: fails if `pyproject.toml` and `uv.lock` are out of sync. You could leave it out, but it is a guard that confirms "what I want is what I expect".
- **R parts removed**: nobody in the section uses R, so the R install and `renv` restore steps were deleted. They follow a very similar process.
- **Linux laptops need one extra line**: a commented-out `StrictModes no` setting for the SSH server, needed later when connecting an editor.
- **Last line**: starts the SSH server (`sshd`) so an editor can connect to the container.

### 7. `pyproject.toml` and `.python-version`

*00:30:18–00:33:30*

- **Date versioning**: the reference's `version = "2026.11.13"` uses date versioning rather than semantic versioning (more in DSCI 524). It records when the hard-pinned package versions were finalized, 2026-11-13.
- **`[tool.uv]` with `add-bounds = "exact"`**: makes `uv add` write `==` instead of `>=`. It is another setting uv looks up.
- **Settings live in many places, on purpose**: you could probably tell uv in `pyproject.toml` to install into `/opt/venv`, but then it would do that on your laptop too.
  - Docker needs to behave slightly differently from your computer, which is why the setting lives in the `Dockerfile`.
  - Try to understand why each setting is where it is.
- **`.python-version`**: tells uv which Python version to download (`3.14` here). Different projects can use different versions of Python, not just of packages. Examples:
  - legacy code still on Python 2, which you don't want for your whole computer;
  - PyTorch, which lags behind new Python releases.

### 8. Building the image and running it ([29.1 Building container images from `Dockerfile`'s](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#building-container-images-from-dockerfiles))

*00:33:30–00:38:15*

- **`uv sync` creates `uv.lock`**: with only `pyproject.toml` present, `uv sync` installs the packages (from cache, so quickly) and writes the lock file. Every file the `Dockerfile` copies now exists.
- **`docker build --tag docker-uv-renv .`**: `--tag` (`-t`) names the image. The `.` is the current directory, where Docker looks for a file called `Dockerfile` by default; you can point to another one. The build output lists each step: base image, copy uv, `WORKDIR`, environment, copy files, `uv sync --locked`.
- **`docker run --rm -it docker-uv-renv bash`**:
  - `--rm` removes the container when you exit.
  - `-it` is `-i` (interactive) plus `-t` (a terminal). Single dashes take one-character flags, which can be chained; double dashes take longer names.
  - `bash` asks for a Bash prompt.
- **You are on another computer**: the prompt changes to `root@<id>:/workspace`. `pwd` shows `/workspace` and `whoami` shows `root`. This is the same idea as cloud computing: learn to read the prompt to know where you are.
- **`python` is not there; `uv run python` is**: plain `python` gives `command not found`, because Python in this image comes through uv. Leave with `exit`.

### 9. Mounting the project folder with `-v`

*00:38:15–00:44:42*

- **`-v "$(pwd):/workspace"`**: puts everything in your current folder into `/workspace` in the container.
  - `$(pwd)` is used because `.` doesn't work everywhere (a Windows/Mac difference).
  - You can repeat `-v` for several folders, which is common with databases that store data in several places.
- **Why mount instead of `COPY`**: `COPY` captures files only at build time, so you'd rebuild after every change. Put just the software in the image and mount the files, which change constantly.
- **Changes show up both ways**: Daniel ran `touch hello.py` inside the container, and `hello.py` appeared on his laptop at once. Think of it as a network share drive.
- **Git stays on your laptop**: with the folder mounted, you `git add`, `commit` and `push` from your own computer. To GitHub a container is a new machine needing its own credentials, and it resets every time it restarts.

> [!WARNING]
>
> Don't put Git credentials or your SSH key into the container image. Your SSH key is like the password to your account, and anyone who pulls your image could read them.

- **When copying is right**: at the end of a project, for example when you must submit a frozen version for compliance, copy the files in so they are part of the image.

> [!WARNING]
>
> Editing the same file both in the container and on your laptop can lose work. Your editor does not refresh an open file. If you save over changes made on the other side, choosing "overwrite" throws them away: it is like a Git conflict without Git. Use your editor's "revert file" before editing a file you know changed elsewhere.

### 10. Why Docker Compose, and reading `docker-compose.yml` ([33.1 Docker Compose to launch containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-docker-compose.html#docker-compose-to-launch-containers))

*00:44:42–00:52:06*

- **The problem**: `docker run` commands grow quickly. Examples are extra `-e` environment variables, such as one that disables RStudio's login page. A long command is easy to share but documented almost nowhere, and its flags are hard to track.
- **`docker-compose.yml`** records the run in a file:
  - `services:` lists the containers to run;
  - `analysis-env:` names this one, and the same image can back several services such as `analysis-env2`;
  - `build: .` is the `docker build .` part;
  - `image: docker-uv-renv` is the `--tag`.
- **`ports:` as `"2222:22"`**:
  - The second number is the port inside the container (22 is the SSH port). The first is the port on your laptop.
  - RStudio uses 8787. A second Jupyter Lab on the same machine moves to 8889.
  - You can remap freely, but always check the first number, since that's where you connect. Files from other people may not keep the same number.
  - Port 22 is used for real things on your computer, so you don't want to take it over by accident.
- **`volumes:`**:
  - `.:/workspace` mounts the project;
  - a second entry mounts your SSH public key into the container, read-only, only while it runs, so it is never permanently in the image.
- **Containers reset**: nothing you do inside is saved except in mounted folders. That makes a container a safe sandbox for trying hard installs like PyTorch: if it breaks, restart it.

> [!WARNING]
>
> `rm -rf /` destroys a system. A container is the place to see what it does, because restarting resets it. Never run it on your actual computer.

### 11. Docker Compose commands ([33.2 Docker Compose commands](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-docker-compose.html#docker-compose-commands))

*00:52:06–00:58:03*

- **Run from the folder with the compose file**: every `docker compose` command reads that one file. Daniel likes settings "specified in a file because it plays well with version control".
- **`docker compose build`**: equivalent to `docker build --tag ...` with the settings from the file. In class it reused cached layers.
- **`docker compose up --detach`**: does the `docker run` for every service. `--detach` runs it in the background and gives your terminal back. No more pasting long commands with missing `\` line breaks.
- **`docker ps -a`**: lists containers, including old stopped ones. It shows a unique ID and a name built from the folder and service (`2026-11-25-docker-validate-analysis-env-1`), plus the port forward `0.0.0.0:2222->22/tcp`.
- **`docker compose exec analysis-env bash`**: runs a command in the running container. Use the **service name** from the file, not the full container name.
- **`docker compose down`**: stops and removes the containers listed in the file. Run it on your laptop, not inside the container.

> [!WARNING]
>
> Turn containers off when you're done. Each one is effectively another computer using your RAM, and several running at once will eat your memory.

### 12. Running commands in the container non-interactively ([33.3 Running a Docker container non-interactively using the Docker Compose](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-docker-compose.html#running-a-docker-container-non-interactively-using-the-docker-compose))

*00:58:03–01:01:10*

- **`docker compose run --rm analysis-env <command>`**: starts a fresh container for the service, runs the command, and removes the container when it finishes. This is one of the ways your work is graded, and how you should document running it.
- **`python` fails, `uv run python` works**: `docker compose run --rm analysis-env python` errored with `executable file not found in $PATH`. Python here is uv's.
  - Be careful with pre-built Python images. Plain `python` may exist there without your uv-installed packages, because they are two different things.
  - Daniel has Python installed four ways on his own machine and has to stay in uv mode deliberately.
- **Rendering your report**: the same pattern, `uv run quarto render` with your file, checks that your laptop's analysis builds in the custom environment.
- **Reproducibility in practice**: "You made a machine. This is how you can go and test this machine by sending it commands."

### 13. Connecting Positron or VS Code to the container over SSH

*01:01:10–01:06:55*

- **Remote SSH**: with the container running (`docker compose up --detach`), an editor can connect to it as if it were any machine on the internet.
  - VS Code has a Remote SSH feature.
  - Forks such as Positron or Cursor can't use Microsoft's extension store, so they connect this way.
- **Connection details**:
  - user `root`, the name shown in the container's prompt; otherwise your laptop username is used, which doesn't exist in the container;
  - host `localhost`;
  - port `2222`, the laptop side of the port mapping.
- **Inside the container from the editor**: open the `/workspace` folder (knowing paths matters here). The terminal prompt becomes `root@...`, so every command runs in the container while you keep the editor's graphical tools.
- **Two ways to work**:
  - work and test locally, then run a final command in the container (Daniel's usual way, so not everything runs at once);
  - work directly inside the container.
- **This is cloud computing**: over the summer Daniel used a 128 GB RAM machine for ~100 GB datasets by connecting Positron to it remotely. Milestones won't test this; experiment if you like, but skip running Docker alongside if you're short on RAM.

### 14. Docker Compose beyond MDS

*01:06:55–01:08:33*

- **A widely used format**: many open-source and self-hosted tools publish a Compose file. Examples:
  - Ollama;
  - n8n, an automation/AI service;
  - Jellyfin, for hosting your own movies.
- **Example: Actual Budget**, a personal finance app. Its Compose file has the same parts you just learned: `services`, an `image`, `ports`, environment variables and `volumes`. You start it with `docker compose up -d`.
- **Daniel's home setup**: a computer in his closet runs a whole set of services this way.
- **How to practise**: install Linux on an old laptop and run everything in containers. This skill goes well beyond this course.

### 15. Setting up packages for data validation

*01:08:33–01:10:16*

- **Back on the laptop**: the validation demo was run locally, not in the container.
- **Packages needed**:
  - `pandera` and `pointblank`, two of the suggested validation packages;
  - `palmerpenguins`, for a dataset.
- **`uv add` failed**: `uv add pandera pointblank` errored, complaining about a missing `[project]` table.
- **The fallback**: list the packages by hand under `dependencies` in `pyproject.toml`, then run `uv sync`. It resolves, installs and writes the lock file from the TOML.
- **Only pointblank was demonstrated**: there wasn't time for both packages.

### 16. Why validate data, and finding missing values ([41.1 Where are the missing values?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/data-validation-python-pointblank.html#where-are-the-missing-values))

*01:10:16–01:13:41*

- **pointblank**: a validation package from Rich at Posit, which builds a lot of open-source data tools. Load it with `import pointblank as pb` and the data with `penguins = load_penguins()`.
- **Why validate**: before fitting models, check the data holds the values you assume.
  - In health data you don't expect pregnant men, or you want to see what happens if a row has one.
  - BMI may have a plausible upper bound.
- **Watch for coded missing values**: health surveys often code missing as `99`, which are not real values. Check your codebook. Missingness should be roughly random; if it isn't, investigate.
- **`pb.missing_vals_tbl(data=penguins)`**: a report of missing values per column, split into sections of rows. In the penguins data most missingness sits near the start. Reading it is subjective; it shows where the holes are.

### 17. Writing validation rules ([41.2 Checking values](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/data-validation-python-pointblank.html#checking-values))

*01:13:41–01:18:29*

- **`pb.Validate(...)`**: you build a validation object, chain rules onto it, and then ask it to report back. Its arguments are `data=penguins`, a `label`, and `thresholds=(0.01, 0.05, 0.10)` for warning, error and critical. For example, 1% missing might be ignored while 10% gets flagged.
- **`.col_vals_in_set(columns="species", set=[...])`**: only the listed species are allowed. This catches human-entered values with inconsistent capitalisation, and tests any assumption you made.
- **`.col_vals_between(columns="bill_length_mm", left=30, right=60, na_pass=True)`**: values must fall in a range. Daniel believed the bounds are inclusive, with an option for exclusive. The same idea works for BMI or any "too small / too large" check.
- **`.rows_distinct()`**: checks for duplicate rows, for example when several people code the same sensor reading or person.
- **`.interrogate()`**: actually runs all the chained checks. Displaying the object shows a table with each step's pass/fail rate, coloured by threshold. In class every step passed.
- **Validate in several places**: check right after cleaning and right before modelling. Checks are not one block, and different checkpoints are a natural way to split work among teammates.

### 18. Failing checks, missingness and splitting the data ([41.4 Splitting the passing and failing rows](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/data-validation-python-pointblank.html#splitting-the-passing-and-failing-rows))

*01:18:29–01:20:48*

- **A failing check**: removing `"Gentoo"` from the allowed set made the species step fail, with warnings raised by the thresholds.
- **Missingness as a separate validation**: Daniel recommended checking missing values per column and per row, separately from checking the values themselves.
- **Splitting the data**: pointblank can give a data frame of rows that passed and another of rows that failed:
  - `values.get_sundered_data(type="pass")` for the passing rows;
  - `values.get_sundered_data(type="fail")` for the failing rows;
  - `pb.preview(data=failed)` for a quick look.
- **Why the split helps teams**: data is never 100% clean.
  - Pass the good rows downstream so teammates can build preprocessing and models now.
  - Keep cleaning the failed rows yourself, so nobody is held up by models that won't converge on bad data.
  - Both are data frames, so you can save them as CSV files for someone else to pick up.
- **Next week**: mostly data validation, plus breaking code into smaller pieces.

## Not reached in class

- [29.1.2 Build your first image](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#build-your-first-image)
- [29.1.3 Layer caching](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#layer-caching)
- [29.1.4 Guidelines for `RUN` commands](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#guidelines-for-run-commands)
- [29.2.1 `CMD` or `ENTRYPOINT`?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#cmd-or-entrypoint)
- [41.5 Flagging every row](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/data-validation-python-pointblank.html#flagging-every-row)

## Commands from class

### Cloning the demo repository and opening it

```bash
cd ~/git
git clone git@github.com:chendaniely/2026-11-25-docker-validate.git
cd 2026-11-25-docker-validate
positron .                 # open the editor in the repository folder
```

The demo repository is <https://github.com/chendaniely/2026-11-25-docker-validate>. After this, `Dockerfile` and `pyproject.toml` were copied in from the reference repository.

### Generating the lock file

```bash
ls                         # Dockerfile  pyproject.toml  README.md
uv sync                    # creates .venv and writes uv.lock
ls                         # uv.lock now exists
```

### Building the image and getting a shell in it

```bash
docker build --tag docker-uv-renv .        # . = folder containing the Dockerfile
docker run --rm -it docker-uv-renv bash    # interactive Bash prompt, removed on exit
pwd                        # /workspace (from WORKDIR)
whoami                     # root
python                     # bash: python: command not found
uv run python              # Python from uv's environment in /opt/venv
exit
```

### Mounting the project folder

```bash
docker run --rm -v "$(pwd):/workspace" -it docker-uv-renv bash
touch hello.py             # inside the container
ls                         # hello.py is there...
exit
ls                         # ...and on the laptop too
```

### Docker Compose: build, start, use, stop

```bash
docker compose build                     # builds image docker-uv-renv from the file
docker compose up --detach               # starts analysis-env in the background
docker ps -a                             # list containers and their port mappings
docker compose exec analysis-env bash    # shell in the running container (service name)
exit
docker compose down                      # stop and remove the container and network
```

`docker ps -a` showed the running container with its forwarded port:

```
CONTAINER ID   IMAGE            COMMAND               ...   PORTS                                     NAMES
5e67a11e10f2   docker-uv-renv   "/usr/sbin/sshd -D"   ...   0.0.0.0:2222->22/tcp, [::]:2222->22/tcp   2026-11-25-docker-validate-analysis-env-1
```

### Running a command in a fresh container

```bash
docker compose run --rm analysis-env python          # fails: python not in $PATH
docker compose run --rm analysis-env uv run python   # works
docker compose up --detach                           # start again, for the Positron SSH connection
```

### Adding the data validation packages

```bash
uv add pandera pointblank   # failed (see below)
# added pandera, palmerpenguins and pointblank to dependencies in pyproject.toml by hand
uv sync                     # resolved and installed them, updating uv.lock
```

The validation code itself is in the demo repository's [`validation.py`](https://github.com/chendaniely/2026-11-25-docker-validate/blob/main/validation.py).

### What went wrong live

- **Editor opened in the wrong folder**: `positron .` was first run in `~/git`, not the clone. Fixed with `cd 2026-11-25-docker-validate` and `positron .` again.
- **Forgot the image name in `docker run`**: `docker run --rm -v "$(pwd):/workspace" -it bash` treated `bash` as the image, so Docker started downloading the official Bash image:
  ```
  Unable to find image 'bash:latest' locally
  latest: Pulling from library/bash
  ```
  Stopped with Ctrl-C and re-run with `docker-uv-renv` before `bash`.
- **`quit` in Bash**: `bash: quit: command not found`. `exit()` leaves Python; `exit` leaves the container shell.
- **`docker compose exec` with the container name**: using the full name from `docker ps` failed:
  ```
  service "2026-11-25-docker-validate-analysis-env-1" is not running
  ```
  `exec` wants the service name from `docker-compose.yml`, so `docker compose exec analysis-env bash` worked.
- **`docker compose down` inside the container**: `bash: docker: command not found`, because the container is a different computer. `exit` first, then run `docker compose down` on the laptop.
- **`python` in `docker compose run`**:
  ```
  exec: "python": executable file not found in $PATH
  ```
  Fixed with `uv run python`.
- **`uv add` refused**:
  ```
  error: Project is missing a `[project]` table; add a `[project]` table to use
         production dependencies, or run `uv add --dev` instead
  ```
  Daniel didn't track down why during class. Earlier `uv sync` runs had also warned `No requires-python value found in the workspace`. He added the packages to `pyproject.toml` by hand and ran `uv sync`, which installed them.

## Assignments

- [ ] Next week's work, from the [student repository](https://github.com/UBC-MDS/DSCI_522_dsci-workflows_students): add data validation checks to your project, placed at the points in your analysis where they belong (after cleaning, before modelling), and break your code into smaller pieces. No due date was given in class.
- [ ] Milestone reminder: your project's container must be able to install everything needed to render your report, Quarto included.

---

- prompt: prompt-notes.md @ 76ca356
- prompt-hash: a00c660964b7
- model: claude-opus-5-5 (requested: opus)
- backend: claude
- inputs: transcript-plaud.md, terminal.txt, materials.md
- generated: 2026-11-25
