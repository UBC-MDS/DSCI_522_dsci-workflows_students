# Docker Compose and Data Validation with pointblank

Date: 2026-11-25

Instructor: Daniel Chen

Demo repository: [2026-11-25-docker-validate](https://github.com/chendaniely/2026-11-25-docker-validate)

## Summary

Daniel Chen taught this section in place of its usual instructor, and the session had three parts. It opened with a hands-on review. Students created a GitHub repository, copied in the `Dockerfile` and `pyproject.toml` from the reference repository, generated `uv.lock` themselves, built an image, and got a bash prompt inside the container. Daniel then went through the `Dockerfile` line by line: why the base image matters, what `RUN` and `apt-get` do, how `uv` gets into the image, and what `WORKDIR` does. He also explained why `UV_PROJECT_ENVIRONMENT=/opt/venv` stops the container from tripping over the `.venv` folder from your laptop when the project folder is mounted.

The main new topic was Docker Compose. A `docker run` command picks up flags for ports, volumes and environment variables until it is hard to copy, edit or document. `docker-compose.yml` records all of those settings in a version-controlled file, so the commands shrink to `docker compose build`, `docker compose up --detach`, `docker compose exec`, `docker compose run --rm` and `docker compose down`. Daniel showed the `-v` mount making files appear on both sides instantly, and warned about overwriting edits when the same file is open in two places. He explained why credentials should be mounted at run time and never baked into the image, and showed that the container resets every time it restarts. He ran Python non-interactively in the container and connected Positron to the running container over Remote SSH, which works the same way as connecting to a cloud machine. He finished with examples of self-hosted open-source apps that ship as Compose files.

The last part introduced data validation with pointblank on the Palmer penguins data. This is preparation for next week's project work. The demo used `pb.missing_vals_tbl()`, a `pb.Validate()` chain with thresholds, `col_vals_in_set()`, `col_vals_between()`, `rows_distinct()` and `interrogate()`, and deliberately broke one check to show what a failing report looks like. Daniel also showed splitting data into passing and failing rows, so a team can keep building the pipeline while data cleaning continues.

## Key takeaways

- A `Dockerfile` pins the tools as well as the packages: `pyproject.toml` and `uv.lock` don't record the version of `uv` itself, but `COPY --from=ghcr.io/astral-sh/uv:0.13.7` does.
- Setting `UV_PROJECT_ENVIRONMENT=/opt/venv` in the image keeps the container's Linux virtual environment separate from the `.venv` your laptop creates, so mounting the project folder doesn't break anything.
- Mount your working files with `-v` (or `volumes:`) rather than `COPY`ing them in, because they change constantly, edits show up on both sides immediately, and anything not mounted is lost when the container stops.
- `docker-compose.yml` holds every `docker run` flag in one documented, version-controlled file, and `docker compose build` / `up --detach` / `exec` / `run --rm` / `down` replace the long commands.
- Inside the container, Python is `uv run python`, not `python`; the same goes for `uv run quarto render` when testing that your report builds.
- pointblank validations are a chain of rule steps on `pb.Validate()` with warning/error/critical thresholds, and nothing is checked until `.interrogate()` runs.
- Check values and missingness separately, at several points in the analysis, and split passing and failing rows so teammates downstream aren't blocked by data cleaning.

## Knowledge Points

### 1. Opening review exercise

*00:00:00–00:04:52*

- **Context**: the section's usual instructor was away, so Daniel taught this lecture. He doesn't teach from slides; the class works through the commands and code together, and students can follow along.
- **Review task given at the start**:
  - create a GitHub repository and clone it to your computer;
  - copy the Python file and `pyproject.toml` from the reference repository, without cloning the whole reference repository;
  - generate `uv.lock` yourself if you know how (copying it is allowed, but generating it is part of the review);
  - build the container from the `Dockerfile` and run it to get a bash prompt.
- **Where the reference was**: the link to the reference repository was posted in Slack ([docker-uv-renv](https://github.com/chendaniely/docker-uv-renv)).
- Students had a few minutes to work before Daniel went through the same steps live.

### 2. Creating and cloning the repository

*00:04:52–00:07:44*

- **Create the repository on GitHub first**: Daniel creates repositories online to keep track of his work. He made a public repository and added a `README.md`, so it wasn't empty from the start.
- **Keep all repositories in one folder**: Daniel clones everything into `~/git`, so everything in that folder and its subfolders is a Git repository and nothing is scattered across the computer.
- **A safe place to clone**: the main reason for the `~/git` folder is that you never want to nest one Git repository inside another (from 521), and `~/git` is always a safe place to clone into.

> [!WARNING]
>
> Don't nest Git repositories. Clone into a folder that is not itself inside another repository.

- **Editor**: Daniel used Positron; VS Code works just as well. The goal is simply a way to see and edit your files.
- **Open the right folder**: he first opened Positron in `~/git` instead of the cloned folder. Open the editor in the repository's own folder so you aren't navigating subfolders.

### 3. Using the template repository responsibly

*00:07:44–00:08:59*

- **Base template repository**: the Slack link points to a template meant as the technical foundation for every project milestone. It includes an example report and many pieces the course covers later.
- **Don't copy it blindly**: a template saves typing and typos, but you are still responsible for understanding everything in your work.
- **Why it matters with AI-assisted coding**: nobody is impressed that you got the work done, because that is a given. What you are tested and interviewed on is whether you understand it.
- **Commits are fair game**: in Daniel's class, any commit with your name on it is something he can ask you about.

### 4. The `Dockerfile`: base image and system software ([29.3 Choosing a base image for your Dockerfile](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#choosing-a-base-image-for-your-dockerfile))

*00:08:59–00:13:18*

- **`Dockerfile`**: the file used to build container images. The class copied it from the reference repository.
- **Base image (`FROM`)**: the demo starts from `rocker/r-ver:4.6.2`, which is an Ubuntu image with R pre-installed.
  - It works for Python projects, but the R parts take up extra storage, so anyone using your image (including the TAs grading it) downloads more.
  - Projects that only use Python will probably start from a different base. Daniel's own class used an Ubuntu image.
  - The goal is the smallest image that has what you need. At the extreme, some images are barely an operating system and you install everything yourself.
- **`RUN`**: runs Bash commands inside the image's operating system, which is typically Linux. This is why MDS has you use Git Bash: the commands are the same kind.
- **`apt-get`**: Ubuntu's way of installing software. The demo installs things like `git` and the `nano` text editor, plus `openssh-server` for connecting from an editor later.
- **System software for Python packages**: some Python packages need non-Python software, which gets installed here. Examples are C compilers for PyTorch and system libraries for geospatial packages.
- **Installing Quarto**: the reference `Dockerfile` downloads the Quarto `.deb` file, installs it with `apt-get`, and deletes the downloaded file. This is the terminal equivalent of downloading an installer and double-clicking it. Daniel deleted this section for the demo, but your milestone container needs Quarto so it can render your report.

### 5. Installing `uv` and controlling tool versions ([29.2 `Dockerfile` command summary](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#dockerfile-command-summary))

*00:13:18–00:15:30*

- **MDS uses Python through `uv`**: instructions you find online may not be `uv`-compatible. For example, a `requirements.txt` file is not how `uv` normally works.
  - The course teaches one way of installing packages on purpose; teaching five ways to install the same software has no benefit.
- **`COPY --from`**: `COPY` copies files from your computer into the image, and it can also copy from other images. The `uv` documentation recommends copying the binaries out of its official image: `COPY --from=ghcr.io/astral-sh/uv:0.13.7 /uv /uvx /usr/local/bin/`.
- **Alternative**: start from one of the many prebuilt `uv` images instead, which saves this step.
- **Why Docker pins tools**: virtual environments control package versions, but `pyproject.toml` doesn't track the version of `uv` itself. Docker gives you control over every other piece of software too.
- **If something breaks**: you may need to find out where `uv` is installed on that particular machine.

### 6. `WORKDIR` and the `.venv` problem ([29.2 `Dockerfile` command summary](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#dockerfile-command-summary))

*00:15:30–00:19:28*

- **`WORKDIR /workspace`**: Docker's version of `cd`. When you start or enter the container, you land in `/workspace` rather than at the root of the operating system.
  - You want to see your project files, not the operating-system folders. Being in the right place also matters when you run something like `rm *`.
  - If the folder doesn't exist, Docker creates it, so it works like `mkdir` and `cd` at once.
- **`uv sync` creates `.venv`**: that folder holds all of the project's installed packages, built for the operating system and CPU of the machine that created it.
- **Why that clashes with containers**: three operating systems (Windows, macOS, Linux) and two CPU architectures (Intel and ARM) give six kinds of computer. Docker exists so code runs on someone else's machine, not just yours.
- **The mount problem**: mounting your project folder also mounts your laptop's `.venv` into the container, and that environment doesn't match the container's Linux.
- **The fix, which is the official `uv` approach**: tell `uv` to put the environment elsewhere with `ENV UV_PROJECT_ENVIRONMENT=/opt/venv`.
  - `uv sync` in the image then installs Linux packages into `/opt/venv`, based on `uv.lock`.
  - When you later mount the folder, the mounted `.venv` is simply ignored. It still works on your laptop and does nothing in the container.

### 7. Environment variables, `uv sync --locked`, and the SSH setup ([29.2 `Dockerfile` command summary](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#dockerfile-command-summary))

*00:27:21–00:30:18*

- **Environment variables**: just as your Python code has variables, tools have their own, called system or environment variables. `uv` looks up `UV_PROJECT_ENVIRONMENT` whenever it runs.
- **Where tool settings live**: there are many places on your computer. A common one is a hidden config folder in your home directory, where many programs store their settings.
- **SSH logins don't see `ENV`**: connecting an editor to the container over SSH (theme 16) doesn't read `ENV` variables. The `Dockerfile` therefore also writes the variable to `/etc/environment`:
  - `echo` prints exactly what you give it;
  - `>>` appends it to the end of a file, so the line `RUN echo "UV_PROJECT_ENVIRONMENT=..." >> /etc/environment` writes one line of text to that file.
- **`RUN uv sync --locked`**: use `--locked` in Docker as an extra guard. If `pyproject.toml` and `uv.lock` are out of sync, the build fails instead of quietly re-resolving packages. You could leave it out, but it checks that what you get is what you expect.
- **R sections removed**: nobody in the section uses R, so Daniel deleted the steps that install R packages with `renv` (restoring a snapshot). They follow a very similar process.
- **SSH server**: the last command makes sure the SSH server (`sshd`) is running, which editors need to connect. Linux laptops need one extra line, which is left commented out in the `Dockerfile`.

### 8. `pyproject.toml` and `.python-version`

*00:30:18–00:33:30*

- **Version field**: the reference project uses date-based versioning (`version = "2026.11.13"`) instead of semantic versioning (more in DSCI 524). The date records when the course's hard-pinned package versions were finalized, 2026-11-13.
- **`[tool.uv]` `add-bounds = "exact"`**: makes `uv add` write `==` pins instead of `>=`. This is another `uv` setting stored in a file.
- **Why some settings live in the `Dockerfile` instead**: you probably could set the `/opt/venv` location in `pyproject.toml`, but then your laptop would use it too. Docker needs to behave slightly differently from your computer, which is why settings end up in several places. Try to understand why each one is where it is.
- **`.python-version`**: contains just the Python version (`3.14`) that `uv` should download and use.
  - Different projects can use different Python versions, not just different package versions.
  - Examples: legacy code still on Python 2, or PyTorch, which lags behind new Python releases. You don't want your whole computer stuck on an unmaintained version.

### 9. Generating `uv.lock` and building the image ([29.4 Dockerfile FAQ](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#dockerfile-faq))

*00:33:30–00:35:47*

- **Generate the lock file with `uv sync`**: with only `pyproject.toml` in the folder, `uv sync` installs the packages (quickly, because they were cached) and writes `uv.lock`. All the files the `Dockerfile` copies are then present.
- **`docker build --tag docker-uv-renv .`**: `--tag` (or `-t`) names the image.
- **The final `.`**: the current working directory (from 521). `docker build` looks there for a file named `Dockerfile` by default; you can point it at a different file instead.
- **Reading the build output**: the build goes step by step: start from the base image, copy `uv`, set the working directory, set the environment variable, copy the project files, run `uv sync`.

### 10. Running the container interactively

*00:35:47–00:38:22*

- **`docker run --rm`**: removes the container when you exit.
- **`-it`**: two single-character flags chained together. `-i` is interactive mode and `-t` gives a TTY (a terminal prompt).
  - Double dashes mark long flags with more than one character; a single dash marks one-character flags, which can be combined.
- **`bash` at the end**: run Bash when the container starts, which gives a prompt in `/workspace`.
- **You are on a different computer**: `pwd` shows `/workspace`, a folder that doesn't exist on your laptop, and the prompt shows the user `root`.
  - This is the same idea as cloud computing, except both machines are on your device. Get used to reading the prompt's username and hostname to know where you are.
- **Python is `uv run python`**: `python` alone is not found in the container. You get the project's Python, with everything installed, through `uv run python`. Leave with `exit`.

### 11. Mounting the project folder with `-v`

*00:38:22–00:42:42*

- **`-v "$(pwd):/workspace"`**: mounts your current working directory to `/workspace` in the container. The command is written to work on both Windows and macOS, where `.` alone doesn't always work.
- **Several mounts**: repeat `-v` for each folder. This is common with databases, which store data in several folders.
- **Why not `COPY` everything in?** `COPY` captures the files as they were at build time. An analysis that changes every minute would need a rebuild for every change. Put the software in the image and mount the files.
- **Two-way sync**: changes on either side appear immediately on the other, including small fixes made while checking something inside the container.
- **Git stays on your laptop**: you can keep using `git add`, `git commit` and `git push` normally. A container resets each time it restarts, and GitHub sees it as a brand-new machine, so you would otherwise have to set up credentials again every time.
- **Security**: your SSH key is effectively the password to your account. Don't bake credentials into an image that someone else could pull and inspect.

> [!WARNING]
>
> Never put Git credentials or SSH keys into the image itself. Anyone who pulls your container could find them and use your account.

- **When copying is right**: for a final, frozen version, for example for compliance, copy the files in so they are part of the image. While you are actively working, mount them.

### 12. Shared files and editing in two places

*00:42:42–00:44:42*

- **Demo**: inside the mounted container, `touch hello.py` created a file that appeared straight away in the project folder on the laptop.
- **Think of it as a network share drive**: both sides are working on the same files.
- **Editing the same file in both places**: an open editor doesn't automatically reload a file changed on the other side. When you save, it may ask whether to overwrite.
- **Revert file**: many IDEs have a "revert file" command that reloads the file from disk. If you know you work in several places, revert before editing.

> [!WARNING]
>
> If a file changed on the other side and you choose "overwrite", the other changes are gone. It is effectively a Git conflict without Git to help. As on a network drive, the last save wins.

### 13. The `docker-compose.yml` file ([33.1 Docker Compose to launch containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-docker-compose.html#docker-compose-to-launch-containers))

*00:44:42–00:52:06*

- **Why Compose exists**: `docker run` commands grow quickly. You add ports, volumes and environment variables with `-e`; for example, the RStudio container takes a variable that disables its login page. A command copied from the internet or a README is hard to track and change.
- **Structure of the demo file**:
  - `services:`: the containers to run. This one is named `analysis-env`.
  - `build: .`: the `docker build .` equivalent, which builds from the `Dockerfile` here if the image doesn't exist.
  - `image: docker-uv-renv`: the image name, the same as `--tag`.
  - The service name can differ from the image name, so you could run `analysis-env`, `analysis-env2` and so on from the same image.
- **`ports:` as `"2222:22"`**: the second number is the port inside the container and the first is the port on your computer. Port 22 is the SSH port.
  - Familiar examples: RStudio uses 8787, and JupyterLab uses 8888. A second JupyterLab falls back to 8889.
  - Port 22 is used for real things, so remapping it avoids clashing with your computer.
  - You can map to any port you like, for example a number you find easier to type.

> [!WARNING]
>
> When you use someone else's Compose file, check the first port number. That is where you connect on your own computer. Following the instructions while looking at the wrong port is a common reason it "doesn't work".

- **`volumes:`**: `.:/workspace` mounts the project. Your SSH public key is mounted too, so it is only in the container while the container runs, never stored in the image.
- **Containers reset**: deleting files or installing packages in a container is undone when it restarts. Only mounted folders keep their changes. This makes the container a safe sandbox, for example for trying out a tricky PyTorch install and starting over.

> [!WARNING]
>
> `rm -rf /` destroys the system it runs on. Only experiment with it inside a container, where restarting resets everything; never run it on your own computer.

### 14. Docker Compose commands ([33.2 Docker Compose commands](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-docker-compose.html#docker-compose-commands))

*00:52:06–00:58:03*

- **Run from the folder with the compose file**: every `docker compose` command reads that one file.
- **`docker compose build`**: does the work of `docker build --tag ...`. The layers were cached, so it finished almost instantly. Daniel likes settings in a file because it works well with version control.
- **`docker compose up --detach`**: runs the `docker run` equivalent for every service, with no flags to remember and no long multi-line commands to paste. Those break when a line-continuation backslash is missing. `--detach` runs the container in the background and gives your terminal back.
- **`docker ps -a`**: lists containers with their ID, image, command (`/usr/sbin/sshd -D`), how long ago each was created, port mapping (`0.0.0.0:2222->22/tcp`) and name (`2026-11-25-docker-validate-analysis-env-1`).
- **`docker compose exec analysis-env bash`**: opens a shell in the running container. `docker compose` commands use the **service name** from the file (`analysis-env`), not the full container name.
- **Editing in a file beats editing in a terminal**: a twenty-line `docker run` command is painful to change because you can't click in the terminal, only use the arrow keys. A file is easier to change, documented, and easier to experiment with.
- **`docker compose down`**: stops and removes every container in the file. Run it on your own computer, not from inside the container, which is a different machine with no `docker` command.
- **Turn containers off**: each container is effectively another computer using RAM. Leave several running and your free memory keeps shrinking.

### 15. Running commands non-interactively ([33.3 Running a Docker container non-interactively using the Docker Compose](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-docker-compose.html#running-a-docker-container-non-interactively-using-the-docker-compose))

*00:58:03–01:01:10*

- **Grading and documentation**: this is one of the ways the TAs grade your project, and how you should document running it. `docker run` would also work, but Compose is easier to specify.
- **`docker compose run --rm analysis-env <command>`**: starts a container for the service, runs the command, and removes the container afterwards. Any Bash command can go where `bash` went before.
- **`python` fails, `uv run python` works**: the container has no plain `python` on its `PATH`, because everything goes through `uv`.
  - With a prebuilt Python image, plain `python` may exist but won't have your `uv`-installed packages, because they are two different installations.
  - Daniel has Python installed four different ways on his laptop and has to make sure he stays in self-contained `uv` mode when teaching. Stepping out of it is when things go horribly wrong.

> [!WARNING]
>
> Don't call plain `python` in the project container. Use `uv run python` (and `uv run quarto ...`), or you may end up with a Python that doesn't have your packages.

- **Testing your report**: `uv run quarto render` (with your file) in the container checks that your analysis builds in the custom environment you made. You made a machine; this is how you test it by sending it commands.

### 16. Connecting Positron or VS Code to the container over SSH

*01:01:10–01:06:55*

- **Start it in the background**: `docker compose up --detach`.
- **VS Code vs. forks**: VS Code can open Docker containers directly. Forks such as Positron or Cursor don't have access to Microsoft's extension store, so they connect with **Remote SSH**, which works with any machine.
- **Connection details**: the user is `root` (seen in the container's prompt) and the host is `localhost` on the mapped port 2222. Without the username, the connection uses your laptop's username, which doesn't exist in the container.
- **Working inside**: the editor window then behaves as if it runs inside the container. You open `/workspace`, which is why knowing about paths matters, and the terminal prompt shows `root@...`. All your editor tools work, but every command runs in the container.
- **Two ways of working**:
  - mount the folder, work and test locally, then test again in the container;
  - connect directly, so everything runs once, in the container.
  - Daniel usually tests locally and runs only the final command in the container, so fewer things are running at once.
- **The same as cloud computing**: Daniel connected Positron to a 128 GB RAM server for datasets of about 100 GB rather than working only in a terminal. The container stands in for any remote machine.
- **Not tested in milestones**: explore which way you like to work. If your laptop is short on resources, don't keep Docker running unnecessarily.

### 17. Docker Compose beyond this course

*01:06:55–01:08:33*

- **Common in open-source self-hosted tools**: Ollama, n8n (an AI automation service), Jellyfin (host your own movies), and Actual Budget (a personal finance app) all publish Compose files.
- **The same pieces appear**: Actual Budget's file has `services`, an image, a port, environment variables and volumes.
- **Same commands**: `docker compose up -d` or `docker compose run` starts the service, which for Actual Budget is a web app on a local port.
- **Practising the skill**: install Linux on an old laptop and run things in containers. Daniel runs a computer in his closet this way. The skill is useful well beyond MDS.

### 18. Adding the validation packages

*01:08:33–01:10:16*

- **Validation runs on the laptop**: Daniel did this part outside the container.
- **The packages**: the course suggests a few validation packages; Daniel showed pointblank (and added `pandera`). He also needed `palmerpenguins` for data.
- **`uv add` failed live**: `uv add pandera pointblank` reported that the project was missing a `[project]` table. Daniel didn't know why.
- **Workaround**: add the packages to `dependencies` in `pyproject.toml` by hand, then run `uv sync`. It resolves everything, installs it, and updates the lock file from the TOML file.

### 19. Why validate data, and exploring missing values ([41.1 Where are the missing values?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/data-validation-python-pointblank.html#where-are-the-missing-values))

*01:10:16–01:13:41*

- **pointblank**: a package by Rich from Posit, which builds many open-source data tools. It is imported as `import pointblank as pb`, and the data is loaded with `from palmerpenguins import load_penguins` and `penguins = load_penguins()`.
- **Why validate**: before you fit models, confirm the data contains the values you expect.
  - In a health dataset you probably don't expect pregnant men, or you want a check that shows those rows if they exist.
  - A BMI above some upper bound is probably an error.
  - Survey data often codes missing values as `99`, which are not real values; your codebook tells you.
  - Missing values should be roughly random; if they aren't, find out why.
- **`pb.missing_vals_tbl(data=penguins)`**: reports missing values per column, with the rows split into sections. In the penguins data, much of the missingness is near the start, perhaps because of collection order or penguins squirming on the scale.
- **Subjective**: the table is a visual way to spot holes in the data, and interpreting it is a judgment call.

### 20. Building a validation with thresholds ([41.2 Checking values](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/data-validation-python-pointblank.html#checking-values))

*01:13:41–01:18:29*

- **Create, then interrogate**: you create a validation object with `pb.Validate()`, chain rule steps onto it, and ask it to report back.
- **Thresholds**: `thresholds=(0.01, 0.05, 0.10)` set the failure rates for warning, error and critical. For example, 10% missing might deserve a flag, while 1% might be fine to leave alone.
- **Steps used in class** (from `validation.py`):

  ```python
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
  ```

  - `col_vals_in_set()`: the column contains only the expected values. This catches problems such as inconsistent capitalization in data typed by people.
  - `col_vals_between()`: values fall within a range (30–60 for bill length, inclusive by default, with an option for exclusive bounds). This is the BMI-style plausibility check.
  - `rows_distinct()`: no duplicate rows, for example when several people code the same record or sensor readings repeat.
  - `.interrogate()`: actually runs all the checks.
- **Validate in several places**: checks belong right after data cleaning and right before modelling, and the right checks depend on the stage of the analysis. Checks at different stages are also a natural way to split work in a team. This is next week's work.
- **The report**: displaying the object shows a table with each step's pass/fail rate, coloured by the threshold it reached. Before the edit, every step passed.

### 21. Failing checks and splitting passing and failing rows ([41.4 Splitting the passing and failing rows](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/data-validation-python-pointblank.html#splitting-the-passing-and-failing-rows))

*01:18:29–01:20:48*

- **Breaking a check on purpose**: Daniel removed `"Gentoo"` from the allowed species. The report then showed the step failing, with warnings, because Gentoo values are clearly in the data.
- **Check missingness separately**: Daniel strongly recommended a separate validation for missing values, per column and per row, kept apart from the value checks.
- **Don't wait for perfectly clean data**: in bigger projects such as capstone, data is never 100% clean. Downstream work shouldn't wait for it.
- **Sundered data**: pointblank can give one data frame of rows that passed and another of rows that failed:

  ```python
  passed = values.get_sundered_data(type="pass")  # keep working with these
  failed = values.get_sundered_data(type="fail")  # a teammate fixes these
  ```

  - Hand `passed` to the next teammate so they can build the pipeline and preprocessing now, while you keep cleaning the `failed` rows.
  - This keeps teammates from getting stuck on models that won't converge because of bad data.
  - Both are ordinary data frames, so you can save them as CSV files that someone else can pick up.
- **Next week**: mostly data validation, plus breaking your code into smaller pieces.

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
positron .                          # opened ~/git by mistake
cd 2026-11-25-docker-validate
positron .                          # open the editor in the repository itself
ls                                  # Dockerfile  pyproject.toml  README.md
```

The `Dockerfile` and `pyproject.toml` were then copied in from the reference repository, with the Quarto and R sections of the `Dockerfile` deleted.

### Generating the lock file and building the image

```bash
uv sync                             # creates .venv and writes uv.lock
ls                                  # uv.lock now present
docker build --tag docker-uv-renv . # build from ./Dockerfile
```

The build output shows each `Dockerfile` step in order, ending with the locked sync:

```
 => [stage-0 4/7] WORKDIR /workspace
 => [stage-0 5/7] RUN echo "UV_PROJECT_ENVIRONMENT=/opt/venv" >> /etc/en
 => [stage-0 6/7] COPY pyproject.toml uv.lock .python-version ./
 => [stage-0 7/7] RUN uv sync --locked
```

### Running the container interactively

```bash
docker run --rm -it docker-uv-renv bash
pwd                                 # /workspace
whoami                              # root
python                              # bash: python: command not found
uv run python                       # the project's Python, from uv
exit
```

### Mounting the project folder

```bash
docker run --rm -v "$(pwd):/workspace" -it docker-uv-renv bash
ls
touch hello.py                      # create a file inside the container
exit
ls                                  # hello.py is also on the laptop
```

### Using Docker Compose

```bash
docker compose build                # same as docker build --tag docker-uv-renv .
docker compose up --detach          # start analysis-env in the background
docker ps -a                        # list containers, ports and names
docker compose exec analysis-env bash   # shell in the running container
exit
docker compose down                 # stop and remove the container and network
```

`docker ps -a` showed the running container and its port mapping:

```
IMAGE            COMMAND               STATUS          PORTS                                     NAMES
docker-uv-renv   "/usr/sbin/sshd -D"   Up 16 seconds   0.0.0.0:2222->22/tcp, [::]:2222->22/tcp   2026-11-25-docker-validate-analysis-env-1
```

### Running Python non-interactively

```bash
docker compose run --rm analysis-env python          # fails: no python on PATH
docker compose run --rm analysis-env uv run python   # works
```

### Starting the container for a Remote SSH connection

```bash
docker compose up --detach          # then connect Positron to root@localhost, port 2222
```

### Adding the data validation packages

```bash
uv add pandera pointblank           # failed: missing [project] table
uv add pandera                      # same error
# added pandera, palmerpenguins and pointblank to pyproject.toml by hand
uv sync                             # resolved 79 packages, installed 77
```

The validation code itself is in [`validation.py`](https://github.com/chendaniely/2026-11-25-docker-validate/blob/main/validation.py) in the demo repository.

### What went wrong live

- **Editor opened in the wrong folder**: the first `positron .` ran in `~/git`. Running `cd 2026-11-25-docker-validate` and then `positron .` again opened the repository.
- **`python` not found in the container**: both `python` at the container prompt (`bash: python: command not found`) and `docker compose run --rm analysis-env python` failed:

  ```
  exec: "python": executable file not found in $PATH
  ```

  Running Python through `uv`, as `uv run python`, fixed both.
- **`quit` instead of `exit`**: `bash: quit: command not found` at the container prompt. `exit` leaves the container.
- **Forgot the image name in `docker run`**: `docker run --rm -v "$(pwd):/workspace" -it bash` treated `bash` as the image, printed `Unable to find image 'bash:latest' locally`, and started pulling it from Docker Hub. Pressing Ctrl-C and re-running with `docker-uv-renv bash` fixed it.
- **Wrong name for `docker compose exec`**: `docker compose exec 2026-11-25-docker-validate-analysis-env-1 bash` gave `service "2026-11-25-docker-validate-analysis-env-1" is not running`. Compose wants the service name from the file: `docker compose exec analysis-env bash`.
- **`docker compose down` inside the container**: gave `bash: docker: command not found`, because the container is another machine. Running `exit` first and then `docker compose down` on the laptop fixed it.
- **`uv add` refused**: both attempts printed:

  ```
  error: Project is missing a `[project]` table; add a `[project]` table to use
         production dependencies, or run `uv add --dev` instead
  ```

  The cause wasn't worked out in class. The workaround was to add the packages to `dependencies` in `pyproject.toml` by hand and run `uv sync`.

## Assignments

- [ ] Next week: add data validation checks to your group project (for example with pointblank) and break your code into smaller pieces. No due date was given in class; see the [student repository](https://github.com/UBC-MDS/DSCI_522_dsci-workflows_students) for the milestone.

---

- prompt: prompt-notes.md @ 420acc6
- prompt-hash: 7e4c2b128a1b
- model: claude-opus-5-5 (requested: opus)
- backend: claude
- inputs: transcript-plaud.md, terminal.txt, materials.md
- generated: 2026-11-25
