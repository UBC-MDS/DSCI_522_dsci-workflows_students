# Docker Compose and Data Validation with pointblank

Date: 2026-11-25

Instructor: Daniel Chen

## Summary

Daniel Chen taught this section 01 lecture in place of its usual instructor. The session opened with a hands-on review. Each student created a GitHub repository and copied the `Dockerfile`, `pyproject.toml` and `.python-version` from the reference repository ([`chendaniely/docker-uv-renv`](https://github.com/chendaniely/docker-uv-renv)). They then generated `uv.lock` with `uv sync`, built an image, and got a bash prompt inside the container. While doing this, Daniel walked through the `Dockerfile` line by line. He explained the choice of base image and why `apt-get` installs system software. He showed how uv is copied in from its own image, what `WORKDIR` does, and why the Python packages are installed into `/opt/venv` instead of the project's `.venv`. He also covered why `uv sync --locked` acts as a safety check. He then reviewed `docker run` flags, especially mounting the project folder with `-v`, and explained why mounting beats copying files into the image while you are actively working.

The new material was **Docker Compose**. A `docker-compose.yml` file records everything a long `docker run` command would contain: image, build instructions, ports, volumes and environment variables. You then run short commands instead: `docker compose build`, `up --detach`, `exec`, `run --rm` and `down`. Daniel showed how this is the way your milestone containers will be checked: `docker compose run --rm analysis-env <command>` asks a fresh container to run your analysis. He also connected Positron to the running container over SSH as a stand-in for remote and cloud computing. He pointed out that many self-hosted open-source tools ship as compose files, so this is a skill that goes well beyond MDS.

The last part introduced **data validation** with the `pointblank` package on the Palmer penguins data. Topics were the missing-values table, a `Validate` object with warning/error/critical thresholds, value checks, `interrogate()`, and splitting the data into passing and failing rows so teammates can work in parallel. Data validation, and breaking analysis code into smaller pieces, is the focus of next week's work.

## Knowledge Points

### 1. Setting up the session repository

- **Keep all repositories in one folder**: Daniel keeps every Git repository under a single `git` folder (e.g. `~/git/`). This makes it obvious that everything inside is a repository, and gives him a safe place to clone into.
  - From 521: **never nest Git repositories** inside one another. A dedicated clone folder helps avoid this.
- **Create the repo on GitHub first**, with a README, so you track your work from the start and aren't cloning an empty repository. The class demo repo is [`chendaniely/2026-11-25-docker-validate`](https://github.com/chendaniely/2026-11-25-docker-validate).
- **Open the right folder in your editor**: open Positron (or VS Code) in the cloned project folder, not its parent `git` folder.
- **Template repo as foundation, not as something to copy blindly**: the reference repository is a good technical foundation for the milestones. You remain responsible for understanding every file.
  - Daniel's rule: *if there's a commit with your name on it, it's fair game for a question about it.* With AI-assisted coding, getting the work done is a given. What you're assessed and interviewed on is whether you understand it.

### 2. Reading the `Dockerfile` ([textbook ch. 29](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html))

- **`FROM rocker/r-ver:4.6.2`**: the base image is Ubuntu with R pre-installed. It works for Python projects but takes more storage.
  - Think of the people downstream of you, including graders who must download your image. Pick a base image that is as small as you can manage while still covering what you need. At the extreme, some images are barely an operating system and you install everything yourself. In Daniel's own section, Python projects started from an Ubuntu image.
- **`RUN`**: runs a bash command inside the image while it builds. The image is Linux, which is why MDS teaches you Bash.
- **`apt-get`**: Ubuntu's way of installing system software. The demo installs things like `git` and a text editor (`nano`) so you can look around inside the container.
  - Python packages often need system software installed here first. Examples are C compilers for PyTorch-style work and non-Python libraries for geospatial packages.
- **Installing Quarto**: the reference file downloads the Quarto `.deb` file, installs it with `apt-get`, then deletes the download. This is the command-line equivalent of downloading an installer and double-clicking it. Daniel deleted this section for class to save time.
  - **For your milestones, the container must be able to run your report, so it needs Quarto.**
- **Installing uv with `COPY --from=ghcr.io/astral-sh/uv:0.13.7 /uv /uvx /usr/local/bin/`**: `COPY` can copy files from your computer, and also from another image. The uv documentation recommends this approach. An alternative is starting from a pre-built uv image.
  - Docker's purpose is full control over every piece of software, including the tool version. `pyproject.toml` does not track the uv version, so the image pins it (`0.13.7`).
  - If you swap in a pre-built uv image and something breaks, find out where uv is installed in that image.
- **Python outside MDS**: other projects' instructions may not be uv-compatible. You may see `requirements.txt` files, which is not how uv works. MDS teaches one way on purpose, rather than five ways to install the same software.
- **`WORKDIR /workspace`**: Docker's version of `cd`. When you enter the container you land in `/workspace` instead of the root of the operating system. This keeps you among your project files, where something like `rm *` won't hit system folders.
  - If the folder doesn't exist, Docker creates it: effectively `mkdir` plus `cd`.
- **R parts removed**: no one in the class uses R, so the R/renv section was deleted. It follows a very similar process.
- **`CMD ["/usr/sbin/sshd", "-D"]`**: starts the SSH server and keeps it in the foreground, so the container keeps running. This is needed later to connect Positron to the container.
  - **Linux laptops need one extra line**, the commented-out `StrictModes no` line in the reference `Dockerfile`.

### 3. Why packages go in `/opt/venv` (`UV_PROJECT_ENVIRONMENT`)

- **`.venv` is machine-specific**: `uv sync` creates a `.venv` folder containing packages built for *your* operating system and CPU.
  - The class has Windows, macOS and possibly Linux, on Intel or ARM chips. That makes up to six kinds of computer. Docker exists so code runs on someone else's machine, not only yours.
- **The problem**: when you mount the project folder into the container, your laptop's `.venv` is mounted too. It doesn't match the container's Linux operating system.
- **The official fix**: tell uv to put the environment somewhere else inside the container.
  - `ENV UV_PROJECT_ENVIRONMENT=/opt/venv` sets an environment variable that uv reads whenever it runs.
  - `uv sync` in the image then installs Linux-appropriate packages, as specified by the lock file, into `/opt/venv`.
  - The mounted `.venv` is simply ignored in the container but still works on your laptop.
- **Environment variables**: just as your Python code has variables, tools have their own settings. These are called environment (or system/global) variables. Many tools store configuration in hidden folders in your home directory (e.g. a config folder) so they can adapt to each person's computer.
- **Why not set this in `pyproject.toml`?** You probably could, but then uv would also install into `/opt/venv` on your own laptop. You want Docker to behave slightly differently from your computer, which is why settings live in different places. Try to understand *why* each is where it is.
- **`RUN echo "UV_PROJECT_ENVIRONMENT=$UV_PROJECT_ENVIRONMENT" >> /etc/environment`**: SSH logins don't read `ENV`, so the variable is also written to a file.
  - `echo` prints exactly what you give it; `>>` **appends** to the end of a file.
- **`COPY pyproject.toml uv.lock .python-version ./`, then `RUN uv sync --locked`**: `--locked` stops the build if `uv.lock` doesn't match `pyproject.toml`. You could leave it out, but it's a guard that ensures you get what you expect.

### 4. The uv project files

- **`pyproject.toml` version `2026.11.13`**: uses *date versioning* instead of semantic versioning (more in DSCI 524). It records the date the course's hard-pinned package versions were finalized (November 13).
- **`[tool.uv]` `add-bounds = "exact"`**: makes `uv add` write `==` (an exact pin) instead of `>=`.
- **`.python-version`** (contains `3.14`): tells uv which Python version to download and use for the project.
  - Different projects can use different Python versions, not only different package versions. For example, a decade-old project might still be on Python 2, and you don't want your whole computer on unmaintained Python. PyTorch also tends to lag behind the newest Python. Sometimes parts of a project effectively run in separate environments, and that's okay.
- **Generating `uv.lock`**: with only `pyproject.toml`, running `uv sync` resolves and installs the packages (from cache if already downloaded) and writes `uv.lock`.

### 5. Building and running with plain Docker

- **`docker build --tag <name> .`**: the `.` is the current working directory. By default Docker looks there for a file named `Dockerfile`; you can point it at another one. The output walks through each step: base image, copy uv, `WORKDIR`, environment, copy files, `uv sync`.
- **`docker run` flags**:
  - `--rm`: remove the container when you exit it.
  - `-it` is `-i` (interactive) plus `-t` (tty, a terminal prompt). Single-dash flags are one character and can be chained. Double-dash flags are multi-character names.
  - A command after the image name (e.g. `bash`) is what runs when the container starts.
- **Knowing which computer you're on**: the prompt changes to `root@<container id>:/workspace#`. `pwd` shows `/workspace`, a folder that doesn't exist on your laptop, and the user is `root`. Working on several computers through terminal windows is the same skill as cloud computing; read the prompt to know where you are.
- **`python` doesn't exist in the container; use `uv run python`**: Python is managed through uv. Pre-built Python images may have a system Python, but your uv-installed packages won't be visible to it. These are two different Pythons.

### 6. Mounting volumes with `-v` instead of copying files

- **`-v "$(pwd):/workspace"`**: puts everything in your current folder into `/workspace` in the container. It is written with `$(pwd)` rather than `.` so it works on both Windows and Mac.
  - You can pass several `-v` flags. This is common with databases, which store data in several folders.
- **Why mount instead of `COPY`-ing the project in?**
  - `COPY` happens at *build* time. With an analysis changing every minute, you'd have to rebuild constantly. Put only the *software* in the image and mount the *files*.
  - Changes on one side appear immediately on the other. A file made with `touch hello.py` inside the container showed up straight away on the laptop.
  - You can keep doing `git add`/`git commit`/`git push` on your own computer. A container is a brand-new machine every time it starts, so you'd otherwise have to set up Git credentials repeatedly.
  - **Security: don't bake credentials into an image.** Your SSH key is effectively your account password. Anyone who pulls an image containing it could use it.
  - Exception: when submitting a final, fixed version (e.g. for compliance), copying files into the image makes sense.
- ⚠️ **Editing the same file on both sides**: it behaves like a network share drive. If the file is open in your editor and changed from the other side, saving can prompt you to overwrite. **If you choose overwrite, you lose the other side's changes.** It's essentially a Git conflict without Git, where whoever saves first wins. Use your IDE's **Revert File** command to refresh a file before editing it.
- **Containers reset on restart**: nothing done inside persists unless it's in a mounted folder. This makes the container a safe sandbox. You can try installing difficult software, and if it fails, restart and try again.
  - ⚠️ You can even see what `rm -rf /` does in a container, and a restart brings it back. **Never run that on your actual computer.**

### 7. Docker Compose ([textbook ch. 33](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-docker-compose.html))

- **Why**: `docker run` commands get long fast, with ports, volumes and environment variables (e.g. `-e` to turn off RStudio's login page). Long commands are hard to document beyond the README and painful to edit, since you can't click to a spot in the terminal. Pasting them is error-prone because of line breaks and missing `\`. A file is documented, easy to change, and works well with version control.
- **`docker-compose.yml`** (from the reference repo):
  ```yaml
  services:
    analysis-env:
      build: .
      image: docker-uv-renv
      ports:
        - "2222:22"
      volumes:
        - .:/workspace
        - ~/.ssh/id_ed25519.pub:/root/.ssh/authorized_keys:ro
  ```
  - `services:` lists the containers to run.
  - `analysis-env` is the **service name**. You could run several services off the same image (e.g. `analysis-env2`), but they need different names.
  - `build: .` plus `image: docker-uv-renv` is the equivalent of `docker build --tag docker-uv-renv .`, used if the image doesn't exist yet.
  - `volumes:` mounts the project at `/workspace`, plus your SSH public key. The key is only in the container while it runs, never stored in the image.
- **Ports `"HOST:CONTAINER"`**: the second number is the port inside the container. The first is the port you use on your laptop.
  - Familiar examples: RStudio on 8787, SSH on 22. If you've run two JupyterLabs at once, the second moved to 8889 automatically.
  - Port 22 is used for real secure connections on your computer, so the demo maps it to 2222 to avoid clashing.
  - The two numbers may or may not match. When following someone else's instructions, check the first number, or you'll be "looking at the wrong spot."
- **Commands** (run from the folder containing the compose file):
  - `docker compose build`: builds the image, like `docker build --tag ...`.
  - `docker compose up --detach`: starts every service in the background and gives your terminal back. The container is named `<project folder>-analysis-env-1`.
  - `docker ps -a`: lists containers (`-a` includes stopped ones), with ID, image, command, ports and name.
  - `docker compose exec analysis-env bash`: runs a command in the running container. **Use the service name from the compose file, not the full container name.**
  - `docker compose down`: stops and removes the containers and their network.
- **Turn containers off when done**: each container is effectively another computer using your RAM. Leaving several running steadily eats your memory.
- **How your work is checked**: `docker compose run --rm analysis-env <command>` starts a fresh container, runs the command, and removes the container afterwards.
  - For example, rendering your Quarto report in the container (`uv run quarto render`) checks that your analysis builds in the environment you specified. You built a machine, and this is how you test it by sending it commands.
- **Beyond MDS**: many self-hosted tools ship compose files, including Ollama, n8n (automation), Jellyfin (media server) and Actual Budget (personal finance, served on port 5006). Running old laptops with Linux and containers is good practice for this skill.

### 8. Connecting Positron/VS Code to the container over SSH

- VS Code can open a Docker container directly through Microsoft's extensions. Forks such as Positron or Cursor can't use Microsoft's extension store, so they connect with **Remote SSH** instead.
- Start the container with `docker compose up --detach`, then connect to `root@localhost` on port `2222`.
  - `root` is the container's user. Otherwise your laptop username is used, which doesn't exist in the container.
- Once connected, open the `/workspace` folder. The editor's terminal shows `root@...`, so every command runs *inside* the container while you keep your IDE's graphical tools.
- **Two workflows**: work locally with the folder mounted and test in the container, or work directly in the container. Daniel usually works locally and runs a final command in the container. If your machine is short on RAM, don't keep Docker running the whole time.
- This is the same as cloud computing. Daniel used it with a 128 GB RAM remote machine for roughly 100 GB datasets. The connection isn't tested in your milestone, so experiment and find the way you like to work.

### 9. Data validation with pointblank ([textbook ch. 41](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/data-validation-python-pointblank.html), [pointblank docs](https://posit-dev.github.io/pointblank/))

- **Why validate**: before modelling, check that the data contains what you assume it does. Examples from Daniel:
  - No pregnant men in a health dataset, or flag those rows.
  - An upper bound on BMI.
  - Survey codebooks that record missing values as `99`.
  - Missingness should look random; if it isn't, find out why.
- **Packages**: `pandera` and `pointblank` were both suggested and added. Only pointblank, written at Posit, was demonstrated. `palmerpenguins` provides the dataset (`load_penguins()`).
- **`pb.missing_vals_tbl(data=penguins)`**: a report of missing values per column, with rows split into ten sections (about 34 rows each). In the penguins data, missing values cluster near the start, perhaps from difficulty getting squirming penguins onto the scale. Judging it is subjective.
- **`pb.Validate(...)`**: you build a validation "agent", chain checks onto it, then ask it to report back.
  - `thresholds=(0.01, 0.05, 0.10)`: warning, error and critical levels, reached when 1%, 5% and 10% of rows fail a step.
  - `.col_vals_in_set(columns="species", set=[...])`: only these values are allowed. This catches problems like inconsistent capitalization in human-entered data.
  - `.col_vals_between(columns="bill_length_mm", left=30, right=60, na_pass=True)`: values must be in a range. Daniel believes this is inclusive by default, and there's an option for non-inclusive.
  - `.rows_distinct()`: no duplicate rows, e.g. from several people coding the same record.
  - `.interrogate()`: actually runs all the checks.
- **Reading the report**: displaying the object gives a table of pass/fail rates per step, colored by the threshold reached. In the demo the species set listed only `"Adelie"` and `"Chinstrap"`. Gentoo rows then fail that step, which shows how failures and warnings appear.
- **Check missingness separately**: Daniel strongly recommends validating missing values (per column, then per row) as a separate validation from value checks.
- **Validate in several places**: checks aren't one block. Run them after cleaning, right before modelling, and at whichever points your assumptions matter. This is also a natural way to divide work among teammates.
- **Splitting passing and failing rows**:
  - `values.get_sundered_data(type="pass")` gives the rows that passed every step.
  - `values.get_sundered_data(type="fail")` gives the rows that failed.
  - Data is never 100% clean. Hand the passing rows downstream so the next person can build the pipeline and modelling, while you keep cleaning the failed rows.
  - Both are data frames, so you can save them as CSV files for others to pick up.

## Commands from class

### Clone the session repository and open it

```bash
cd ~/git
git clone git@github.com:chendaniely/2026-11-25-docker-validate.git
cd 2026-11-25-docker-validate
positron .                # open the project folder itself in Positron
ls                        # Dockerfile  pyproject.toml  README.md
```

The `Dockerfile`, `pyproject.toml` and `.python-version` were copied in from the reference repository. `.python-version` is hidden, so plain `ls` doesn't show it.

### Generate `uv.lock`

```bash
uv sync                   # creates .venv and writes uv.lock from pyproject.toml
ls                        # uv.lock now present
```

### Build the image and get a shell in it

```bash
docker build --tag docker-uv-renv .
docker run --rm -it docker-uv-renv bash
```

Inside the container:

```bash
pwd                       # /workspace  (set by WORKDIR)
whoami                    # root
python                    # bash: python: command not found
uv run python             # Python from uv's environment in /opt/venv
exit                      # leave the container (--rm removes it)
```

### Mount the project folder into the container

```bash
docker run --rm -v "$(pwd):/workspace" -it docker-uv-renv bash
```

Inside the container:

```bash
ls                        # your project files, via the mount
touch hello.py            # create a file in the container...
exit
```

Back on the laptop:

```bash
ls                        # ...and hello.py is here too
```

### Docker Compose: build, start, inspect, enter, stop

After adding `docker-compose.yml` from the reference repository:

```bash
docker compose build                       # same as docker build --tag docker-uv-renv .
docker compose up --detach                 # start in the background
docker ps -a                               # list containers
docker compose exec analysis-env bash      # shell in the running container (service name!)
exit                                       # back to the laptop; container keeps running
docker compose down                        # stop and remove container + network
```

The line `docker ps -a` printed for the running container:

```
CONTAINER ID   IMAGE            COMMAND               CREATED          STATUS          PORTS                                     NAMES
5e67a11e10f2   docker-uv-renv   "/usr/sbin/sshd -D"   16 seconds ago   Up 16 seconds   0.0.0.0:2222->22/tcp, [::]:2222->22/tcp   2026-11-25-docker-validate-analysis-env-1
```

### Run a one-off command in a fresh container

```bash
docker compose run --rm analysis-env uv run python    # removed when the command finishes
```

### Start the container again for Positron's Remote SSH

```bash
docker compose up --detach     # then connect Positron to root@localhost, port 2222
```

### Add the data validation packages

```bash
uv add pandera pointblank      # failed, see below
uv sync                        # after adding pandera, palmerpenguins, pointblank to pyproject.toml by hand
```

The final `uv sync` installed 77 packages, including `pandera==0.36.0`, `palmerpenguins==0.1.6` and `pointblank==1.3.0`. The validation code itself is in [`validation.py`](https://github.com/chendaniely/2026-11-25-docker-validate/blob/main/validation.py) in the demo repository.

### What went wrong live

- **Opened Positron in the wrong folder**: `positron .` was first run in the parent `git` folder. Fixed by `cd 2026-11-25-docker-validate` and running `positron .` again.
- **Forgot the image name in `docker run`**: `docker run --rm -v "$(pwd):/workspace" -it bash` made Docker treat `bash` as the *image*. It started pulling it from Docker Hub:
  ```
  Unable to find image 'bash:latest' locally
  latest: Pulling from library/bash
  ```
  Stopped with Ctrl-C and re-run with the image before the command: `... -it docker-uv-renv bash`.
- **`python` not found**, twice. `python` at the container prompt gave `bash: python: command not found`. `docker compose run --rm analysis-env python` failed with:
  ```
  exec: "python": executable file not found in $PATH
  ```
  Fix both ways: `uv run python`. Python lives in uv's environment, not on the system path.
- **Leaving Python vs leaving bash**: `exit()` quits the Python interpreter. At the bash prompt, `quit` gave `command not found`; `exit` is the bash command.
- **`docker compose exec` with the container name**: `docker compose exec 2026-11-25-docker-validate-analysis-env-1 bash` gave `service "2026-11-25-docker-validate-analysis-env-1" is not running`. Compose commands take the **service name** from the file: `docker compose exec analysis-env bash`.
- **Running `docker compose down` inside the container**: gave `bash: docker: command not found`, because the container is a different computer without Docker. Fixed by typing `exit`, then running `docker compose down` on the laptop.
- **`uv add` refused to add packages**: `uv add pandera pointblank` (and then `uv add pandera` alone) printed:
  ```
  error: Project is missing a `[project]` table; add a `[project]` table to use
         production dependencies, or run `uv add --dev` instead
  ```
  The same missing table explains the earlier `warning: No requires-python value found in the workspace` from `uv sync`. Daniel worked around it by adding `pandera`, `palmerpenguins` and `pointblank` to the dependencies in `pyproject.toml` by hand and running `uv sync`. The committed `pyproject.toml` has a `[project]` table with those three packages. Takeaway: you can always edit `pyproject.toml` directly and `uv sync` to update the lock file.

## Questions

- **Q:** At the start, a student asked where the reference GitHub repository they were supposed to copy the files from was.
  **A:** The link was shared in Slack: <https://github.com/chendaniely/docker-uv-renv>. Copy the `Dockerfile`, `pyproject.toml` and `.python-version`, but try generating `uv.lock` yourself with `uv sync` rather than copying it.

## Assignments

- [ ] Next week's work, the week of 2026-11-30: add data validation checks to your project at the right points (after cleaning, before modelling), and break your analysis code into smaller pieces. No due date was given in class.
- [ ] For the milestones: make sure your container can render your report. It needs Quarto installed, and you should check it with `docker compose run --rm analysis-env ...`.

---

- prompt: prompt-notes-original.md @ 979670b
- prompt-hash: f78026c179ce
- model: claude-opus-5-5 (requested: opus)
- backend: claude
- inputs: transcript-plaud.md, terminal.txt, materials.md
- generated: 2026-11-25
