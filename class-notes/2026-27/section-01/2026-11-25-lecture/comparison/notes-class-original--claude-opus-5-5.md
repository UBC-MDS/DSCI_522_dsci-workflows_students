# Docker Compose and Data Validation with pointblank

Date: 2026-11-25

Instructor: Daniel Chen

## Summary

Daniel Chen taught this section 01 lecture in place of the usual instructor. The first half reviewed building a container. The class created a new GitHub repository and cloned it. They copied in the `Dockerfile` and `pyproject.toml` from the reference repository ([chendaniely/docker-uv-renv](https://github.com/chendaniely/docker-uv-renv)), generated `uv.lock` with `uv sync`, built the image with `docker build`, and got a Bash prompt with `docker run`. The instructor walked through the `Dockerfile` line by line. He covered why the base image matters, how `RUN apt-get` installs system software, how `uv` is copied in at a pinned version, what `WORKDIR` does, and why `UV_PROJECT_ENVIRONMENT=/opt/venv` stops the host's `.venv` folder from clashing with the container's Linux environment. He then explained why you mount your project folder with `-v` instead of `COPY`ing it into the image. A mount is a live two-way sync. It also means your Git credentials never get baked into the image. A Move U crew member interrupted the review with a short movement break.

The new material was **Docker Compose**. A long `docker run` command with ports, volumes and environment variables is hard to edit and is documented only in a README. A `docker-compose.yml` file holds all of those settings in one version-controlled file. The class used it to build the image (`docker compose build`) and start the container in the background (`docker compose up --detach`). They also opened a shell in the running container (`docker compose exec analysis-env bash`), stopped it (`docker compose down`), and ran a one-off command (`docker compose run --rm analysis-env uv run python`). That last pattern is how the teaching team checks that a project's analysis runs in its container. The instructor also showed how to connect Positron or VS Code to the running container over SSH (port 2222), and why that is the same skill as working on a remote cloud machine.

The last part of the session introduced **data validation** with the `pointblank` package on the Palmer penguins data. The examples were a missing-values report, a `Validate` object with warning, error and critical thresholds, and value checks. Running `interrogate()` produces a pass/fail report. Splitting the data into passing and failing rows lets a teammate keep building the pipeline while you clean the bad rows. This leads directly into next week's work: writing data checks and breaking the analysis code into smaller pieces.

## Knowledge Points

### 1. Setting up the project repository

- **Where to keep repositories**: the instructor keeps every Git repository under one `~/git` folder. That makes it clear that everything there is a repository, and it gives a safe place to clone into without nesting one Git repository inside another (a 521 rule).
- **Create the repo on GitHub first**, with a `README.md`, so it is not empty, then `git clone` it. Open your editor in the *cloned* folder, not its parent. The instructor opened Positron in `~/git` by mistake and had to reopen it in the right folder.
- **Using the template repository**: the reference repository is the technical foundation for the milestones. **Don't copy it blindly.** You are responsible for everything in your project. If there is a commit with your name on it, it is fair game for a question in an interview or an exam.

### 2. Reading the `Dockerfile` ([textbook ch. 29](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html))

- **`FROM rocker/r-ver:4.6.2`**: the base image. It is Ubuntu with R preinstalled. It works for Python projects but is larger than necessary, so anyone pulling your image (including graders) waits longer for the download.
  - For a Python-only project, consider a smaller base such as plain `ubuntu`. The goal is the smallest image that has what you need. At the extreme, some images are barely an operating system, and you install everything yourself.
- **`RUN`**: runs a Bash command inside the image's operating system, which is usually Linux. This is why MDS uses Git Bash.
  - `apt-get` is Ubuntu's installer. The demo installs tools like `git` and `nano` (a text editor for looking around inside the container) and `openssh-server` (needed later to connect an editor to the container).
  - This is where system-level software goes when Python packages depend on it. Examples are C compilers for PyTorch and system libraries for geospatial packages.
- **Installing Quarto**: the reference `Dockerfile` downloads the Quarto `.deb` file, installs it with `apt-get`, then deletes the download. This is the terminal version of downloading an installer and double-clicking it. The section was deleted for today. **For your milestones the container must be able to render your report, so it needs Quarto.**
- **Installing Python through `uv`**: in MDS, Python is managed by `uv`. Instructions you find elsewhere (for example a `requirements.txt` file) may not be `uv`-compatible, so don't paste them blindly.
  - `COPY --from=ghcr.io/astral-sh/uv:0.13.7 /uv /uvx /usr/local/bin/` copies the `uv` binary out of uv's own prebuilt image. `COPY` can copy from your computer or from another image.
  - The point is version control of the *tool itself*. `pyproject.toml` pins package versions but not the `uv` version. Docker lets you pin everything.
  - You can instead start from a prebuilt `uv` image. If something breaks, check where `uv` is installed in that image.
- **`WORKDIR /workspace`**: Docker's `cd`. When you enter the container you land here and not at the root of the filesystem among the operating system's folders. If the folder doesn't exist, Docker creates it, so it acts as `mkdir` and `cd` in one step.
- **`ENV UV_PROJECT_ENVIRONMENT=/opt/venv`**: an environment variable that `uv` reads. Like variables in your own code, tools have their own environment (system) variables, and many tools store settings in hidden config folders in your home directory.
  - **Why it's needed**: `uv sync` creates a `.venv` folder that is specific to the operating system and CPU it was built on. Your class's computers span 3 operating systems (macOS, Windows, Linux) and 2 CPU architectures (ARM, Intel), which makes 6 combinations. When you mount your project folder into the container, your host's `.venv` comes along and doesn't match the container's Linux system.
  - Setting this variable tells `uv` inside the container to install packages into `/opt/venv` instead. The mounted `.venv` is then ignored in the container and keeps working on your laptop. This is the official approach, not a hack.
  - You could set this in `pyproject.toml`, but then it would also apply on your own machine. Docker should behave slightly differently from your laptop.
- **`RUN echo "UV_PROJECT_ENVIRONMENT=$UV_PROJECT_ENVIRONMENT" >> /etc/environment`**: SSH logins don't see `ENV` variables, so the variable is also written to a file. `echo` prints its text, and `>>` appends to the end of a file.
- **`COPY pyproject.toml uv.lock .python-version ./`** followed by **`RUN uv sync --locked`**:
  - `--locked` makes the build fail if `uv.lock` doesn't match `pyproject.toml`. It is an extra guard that what you want is what you get.
  - Because the image is Linux, `uv sync` installs the Linux versions of the locked packages.
- **R parts deleted**: no one in the section uses R, so the R install and the `renv` restore step were removed. They follow the same pattern.
- **Linux laptops**: one extra commented-out line, `StrictModes no`, is needed for the SSH connection.
- **`CMD ["/usr/sbin/sshd", "-D"]`**: starts the SSH server so an editor can connect later.

### 3. The `uv` project files

- **`pyproject.toml`** in the demo uses date versioning (`version = "2026.11.13"`) instead of semantic versioning (more in DSCI 524). This tracks when the hard-pinned package versions were frozen for the course.
- **`[tool.uv]` `add-bounds = "exact"`** makes `uv add` write `==` pins instead of `>=`.
- **`.python-version`** (contains `3.14`) tells `uv` which Python version to download. Different projects can use different Python versions, not only different package versions. Examples are legacy code stuck on an old Python, or PyTorch, which lags behind new Python releases.
- **`uv sync`** with only a `pyproject.toml` installs the packages (from cache if already downloaded) and creates `uv.lock`.

### 4. Building and running the image

- **`docker build --tag docker-uv-renv .`**: `--tag` (or `-t`) names the image. The `.` is the current directory. By default Docker looks there for a file called `Dockerfile`, but you can point it at another one. The build output lists each step: base image, `COPY`, `WORKDIR`, `ENV`, `uv sync`.
- **`docker run --rm -it docker-uv-renv bash`**:
  - `--rm` removes the container when you exit.
  - `-it` is `-i` (interactive) plus `-t` (a tty, i.e. a terminal prompt). Single-letter flags take one dash and can be chained. Multi-letter flags take two dashes.
  - `bash` at the end is the command to run, here a Bash prompt.
- **Knowing where you are**: the prompt changes to `root@<container-id>:/workspace`. `pwd` gives `/workspace`, and the user is `root`. It is a different computer. Reading the prompt to work out which machine you are on is a skill you need for cloud computing too.
- **Python inside the container**: plain `python` is not found. Use `uv run python` to get the `uv`-managed Python with your packages.

### 5. Mounting volumes with `-v` instead of `COPY`

- **`-v "$(pwd):/workspace"`** mounts your current folder at `/workspace` in the container. The `$(pwd)` form is written to work on both Mac and Windows, where `.` doesn't always work.
  - Use more `-v` flags to mount more folders. Databases, for example, store data in several folders.
- **Why not `COPY` the project into the image?** `COPY` captures the files at *build* time. Your analysis changes constantly, and you don't want to rebuild the image every time. Put the software in the image and mount the files.
  - If you need a frozen final artifact, for example for compliance, copying the files in is fine.
- **Two-way sync**: changes on either side appear on the other almost immediately, like a network share drive. The class showed this by running `touch hello.py` in the container and seeing the file appear on the laptop.
- **Git stays on your laptop**: because files sync back, you can `git add`/`commit`/`push` from your own machine. The container would otherwise need its own Git setup (token or SSH key) every time it restarts.
  - **Security warning**: don't put credentials such as SSH keys into the image. Anyone who pulls the image could read them and get into your account.
- **⚠️ Editing the same file on both sides**: if a file is open in your editor and changes on the other side, saving can bring up an overwrite prompt. **If you choose overwrite, you lose the other side's changes.** It is effectively a Git conflict without Git, and whoever saves last wins. Use your editor's **revert file** command to reload from disk before editing a file you've been working on elsewhere.
- **Containers reset**: anything not in a mounted folder disappears when the container restarts. This makes the container a safe sandbox. You can try installing something complicated like PyTorch's dependencies, break things, and restart to get a clean system back.
  - **⚠️ The instructor joked that a container is the place to see what `rm -rf /` does. Never run it on your actual computer: it deletes everything.** In a container, it destroys only that container, and a restart restores it.

### 6. Docker Compose ([textbook ch. 33](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-docker-compose.html))

- **Why**: `docker run` commands grow long: ports, several volumes, environment variables (for example `-e DISABLE_AUTH=true` for the RStudio container). They are copy-paste friendly, but:
  - often the only documentation is the README;
  - you can't click to edit the middle of a multi-line command in a terminal;
  - a missing `\` or a stray line break breaks the paste.

  A file fixes all of that and works well with version control.
- **`docker-compose.yml`** from the demo:

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

  - **`services:`** lists the containers to run.
  - **`analysis-env`** is the service name you use in `docker compose` commands. You could run several services from the same image (for example `analysis-env2`), but each needs its own name.
  - **`build: .`** is how to build the image if it doesn't exist (the `docker build .` part). **`image: docker-uv-renv`** is the image name (the `--tag` part).
  - **`ports: "2222:22"`** means `<port on your computer>:<port in the container>`. The SSH server listens on 22 inside. Port 22 is a real, commonly used port on your own machine, so the host side uses 2222.
    - Other familiar ports: RStudio uses 8787. JupyterLab uses 8888, and a second JupyterLab falls back to 8889.
    - **Pay attention to the first number.** That is where you connect on your laptop. Files from other people may remap ports, and "it doesn't work" is often just looking at the wrong port.
  - **`volumes:`** mounts the project folder at `/workspace`. It also mounts your SSH public key read-only (`ro`) so you can log in. The key is present only while the container runs and is never stored in the image.
- **Commands** (run from the folder containing the compose file):
  - `docker compose build` is the `docker build --tag ...` equivalent.
  - `docker compose up --detach` runs every service in the background and gives your prompt back.
  - `docker compose exec analysis-env bash` runs a command in the *running* container. It takes the **service name**, not the long container name Docker shows.
  - `docker compose down` stops and removes the project's containers. It must be run on your computer, not inside the container.
  - `docker compose run --rm analysis-env <command>` starts a fresh container, runs one command, and removes it.
- **Turn containers off when you're done**: each one is effectively another computer using RAM. Many running containers will steadily eat your memory.
- **Almost nothing in Compose can't be done with `docker run`**. Compose just puts the parameters in a file.

### 7. Running your analysis in the container

- **`docker compose run --rm analysis-env uv run python`** gives a Python interpreter running inside the container, from your laptop. Plain `python` fails because Python lives in `uv`.
  - If you use a prebuilt Python image, a system `python` may exist, but packages installed with `uv` won't be visible to it. These are two different Pythons. The instructor has Python installed several ways on his machine and has to be careful to stay in `uv` mode.
- **The same pattern renders your report**: `uv run quarto render` with your file. This is how you, and the graders, check that the analysis builds in the environment you defined. You built a machine, and you test it by sending it commands. This is the point of the course: reproducibility.

### 8. Connecting your editor to the container

- **Remote SSH**: VS Code has a Remote SSH feature for connecting to any machine. Forks of VS Code (Positron, Cursor) can't use Microsoft's extension store, so they connect this way.
  - Connect as user **`root`** (the container's user, not your laptop username), to host **`localhost`**, on port **2222**.
  - The editor window then behaves as if it were inside the container. Open the `/workspace` folder (knowing your paths matters here), and the terminal prompt shows `root@...`.
- **Ways of working**:
  - edit and run locally, then test in the container;
  - or work directly in the container, so commands run there only once.

  The instructor usually works locally and runs the final command in the container.
- **This is cloud computing**: the container stands in for any remote machine. The instructor used Positron's remote connection to work on a 128 GB RAM server because his datasets needed around 100 GB of memory.
- **Not tested in your milestones.** Try it and find what you like. If your laptop is short on resources, don't keep Docker running.
- **Beyond MDS**: many self-hosted open-source tools ship as Compose files. Examples are Ollama, n8n (automation), Jellyfin (media server) and Actual Budget (personal finance; its compose file has services, an image, a port, environment variables and volumes, and it runs on port 5006). Running services in containers on an old Linux laptop is a good way to practise.

### 9. Data validation with pointblank ([textbook ch. 41](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/data-validation-python-pointblank.html))

- **Packages**: `pandera` and `pointblank` (the two suggested tools; only `pointblank` was demonstrated), plus `palmerpenguins` for data. pointblank is written by Rich at Posit ([docs](https://posit-dev.github.io/pointblank/)).
- **Why validate**: check that the data contains what you assume before you model it. Examples from the instructor's experience:
  - impossible combinations (pregnant men in health data);
  - implausible values (a BMI above some upper bound);
  - missing values coded as `99` in survey data (check the codebook);
  - missingness that isn't random, which you should investigate.
- **Missing values report**: `pb.missing_vals_tbl(data=penguins)` shows missingness per column across sections of rows. In penguins, most missing values sit near the start of the data. Reading it is subjective, but it shows where the holes are.
- **A validation** (from the demo's [`validation.py`](https://github.com/chendaniely/2026-11-25-docker-validate/blob/main/validation.py)):

  ```python
  import pointblank as pb
  from palmerpenguins import load_penguins

  penguins = load_penguins()

  values = (
      pb.Validate(
          data=penguins,
          label="Penguin measurements",
          thresholds=(0.01, 0.05, 0.10),  # warning, error, critical
      )
      .col_vals_in_set(columns="species", set=["Adelie", "Chinstrap"])
      .col_vals_between(columns="bill_length_mm", left=30, right=60, na_pass=True)
      .rows_distinct()
      .interrogate()
  )
  values
  ```

  - **Thresholds**: the share of failing rows (1%, 5%, 10%) at which a step is flagged. For example, 1% missing might be fine to ignore, while 10% should be flagged.
  - **`col_vals_in_set`**: the column contains only the allowed values. This catches human-entered data with inconsistent capitalisation.
  - **`col_vals_between`**: values fall in a range. It is inclusive by default, and there is an option for exclusive bounds. Use it for any plausible range, such as BMI.
  - **`rows_distinct`**: no duplicate rows, for example when several people coded the same records.
  - **`interrogate()`** actually runs the checks you have chained up.
  - The **report table** shows the pass/fail rate per step, coloured by the threshold reached. In class, `"Gentoo"` was removed from the allowed species set to show failures and warnings appearing.
- **Validate values and missingness separately**: check missingness per column and per row in its own validation.
- **Validate in several places**: for example after cleaning and right before modelling. Validation code isn't one block, and checks at different stages are a natural way to split work among teammates.
- **Splitting passing and failing rows**:

  ```python
  passed = values.get_sundered_data(type="pass")
  failed = values.get_sundered_data(type="fail")
  ```

  Data is never 100% clean, so don't block your team waiting for it. Give the passing rows to the next person so they can build the pipeline (preprocessing, models that converge). Keep working on the failing rows yourself. Both are data frames, so you can save them as CSV files for others to pick up.

## Commands from class

### Cloning the repository and opening it

```bash
cd ~/git
git clone git@github.com:chendaniely/2026-11-25-docker-validate.git
cd 2026-11-25-docker-validate
positron .                    # open the editor in the cloned repo
```

The class then copied `Dockerfile` and `pyproject.toml` from the reference repository.

### Generating the lock file

```bash
ls                            # Dockerfile  pyproject.toml  README.md
uv sync                       # creates .venv and uv.lock
ls                            # uv.lock now present
```

### Building the image and getting a shell

```bash
docker build --tag docker-uv-renv .
docker run --rm -it docker-uv-renv bash
pwd                           # /workspace  (set by WORKDIR)
whoami                        # root
python                        # fails: bash: python: command not found
uv run python                 # the uv-managed Python 3.14
exit()                        # leave Python
exit                          # leave the container
```

The build output lists the `Dockerfile` steps in order:

```
 => [stage-0 3/7] COPY --from=ghcr.io/astral-sh/uv:0.13.7 /uv /uvx /usr/  0.1s
 => [stage-0 4/7] WORKDIR /workspace                                      0.0s
 => [stage-0 5/7] RUN echo "UV_PROJECT_ENVIRONMENT=/opt/venv" >> /etc/en  0.1s
 => [stage-0 6/7] COPY pyproject.toml uv.lock .python-version ./          0.0s
 => [stage-0 7/7] RUN uv sync --locked                                    0.2s
```

### Mounting the project folder

```bash
docker run --rm -v "$(pwd):/workspace" -it docker-uv-renv bash
touch hello.py                # create a file inside the container
ls                            # hello.py is there
exit
ls                            # ...and it is on the laptop too
```

### Docker Compose: build, start, enter, stop

```bash
docker compose build                       # same as docker build --tag docker-uv-renv .
docker compose up --detach                 # start in the background
docker ps -a                               # list containers, running or not
docker compose exec analysis-env bash      # shell in the running service
exit
docker compose down                        # stop and remove (run on your laptop)
```

`docker compose up --detach` creates a network and a container named after the project folder and the service:

```
 ✔ Network 2026-11-25-docker-validate_default          Created
 ✔ Container 2026-11-25-docker-validate-analysis-env-1 Started
```

In `docker ps -a`, read the image, the command (`sshd -D`), the port mapping, and the name:

```
CONTAINER ID   IMAGE            COMMAND               CREATED          STATUS          PORTS                                     NAMES
5e67a11e10f2   docker-uv-renv   "/usr/sbin/sshd -D"   16 seconds ago   Up 16 seconds   0.0.0.0:2222->22/tcp, [::]:2222->22/tcp   2026-11-25-docker-validate-analysis-env-1
```

### Running one-off commands in the container

```bash
docker compose run --rm analysis-env python          # fails: python not in $PATH
docker compose run --rm analysis-env uv run python   # works
docker compose up --detach                           # started again for the Positron remote SSH demo
```

### Adding the data validation packages

```bash
uv add pandera pointblank     # failed, see below
# added pandera, palmerpenguins and pointblank to dependencies in pyproject.toml by hand
uv sync                       # installs them and updates uv.lock
```

### What went wrong live

- **Editor opened in the wrong folder**: `positron .` was first run in `~/git`, not the cloned repo. Fixed with `cd 2026-11-25-docker-validate` and `positron .` again.
- **`python` not found in the container**: both `python` at the container prompt and `docker compose run --rm analysis-env python` failed:

  ```
  exec: "python": executable file not found in $PATH
  ```

  Python is managed by `uv`, so use `uv run python`.
- **`quit` at a Bash prompt**: `bash: quit: command not found`. `exit` leaves a shell. `exit()` leaves Python.
- **Image name forgotten in `docker run`**: `docker run --rm -v "$(pwd):/workspace" -it bash` made Docker treat `bash` as the *image* name and start pulling it:

  ```
  Unable to find image 'bash:latest' locally
  ```

  Stopped with Ctrl-C and re-run with the image before the command: `... -it docker-uv-renv bash`.
- **`docker compose exec` given the container name**: `docker compose exec 2026-11-25-docker-validate-analysis-env-1 bash` failed:

  ```
  service "2026-11-25-docker-validate-analysis-env-1" is not running
  ```

  `docker compose` commands take the **service name** from `docker-compose.yml`. `docker compose exec analysis-env bash` worked.
- **`docker compose down` typed inside the container**: `bash: docker: command not found`. The container is a different computer without Docker. `exit` first, then run `docker compose down` on the laptop.
- **`uv add` failed**: both `uv add pandera pointblank` and `uv add pandera` errored with:

  ```
  error: Project is missing a `[project]` table; add a `[project]` table to use
         production dependencies, or run `uv add --dev` instead
  ```

  The same `pyproject.toml` had produced `warning: No requires-python value found in the workspace` on every earlier `uv` command, which suggests the copied file lacked its `[project]` header. The workaround in class was to add `pandera`, `palmerpenguins` and `pointblank` to the dependencies list by hand and run `uv sync`, which installed them. The `pyproject.toml` committed to the [demo repository](https://github.com/chendaniely/2026-11-25-docker-validate/blob/main/pyproject.toml) has a `[project]` table with `requires-python = ">=3.14"`.

## Questions

- **Q:** Where is the GitHub repository we're supposed to copy the files from?
  **A:** It's the reference repository ([chendaniely/docker-uv-renv](https://github.com/chendaniely/docker-uv-renv)), and the link was also posted in Slack.

## Assignments

- [ ] Next week's work: write data validation checks for your project and break your analysis code into smaller pieces. No due date was given in class; check the [student repository](https://github.com/UBC-MDS/DSCI_522_dsci-workflows_students).
- [ ] For your milestones: make sure your container installs everything needed to render your report, including Quarto. Check that it runs with `docker compose run --rm <service> ...`.

---

- prompt: prompt-notes-original.md @ 979670b
- prompt-hash: f78026c179ce
- model: claude-opus-5-5 (requested: opus)
- backend: claude
- inputs: transcript-plaud.md, terminal.txt, materials.md
- generated: 2026-11-25
