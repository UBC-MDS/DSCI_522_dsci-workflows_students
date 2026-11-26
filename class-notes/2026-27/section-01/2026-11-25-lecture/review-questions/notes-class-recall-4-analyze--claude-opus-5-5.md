# Docker Compose and data validation with pointblank: review questions, tier 4 — Analyze

Date: 2026-11-25

Instructor: Daniel Chen

*Tier 4 of 5: Analyze. Take each one apart yourself before you read the answer; tiers 1 to 3 cover the facts, reasons and steps it relies on.*

## 1. The `Dockerfile`: base image and system software ([29.1 Building container images from `Dockerfile`’s](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#building-container-images-from-dockerfiles))

*00:08:59–00:13:18*

- **Q:** Break down the Quarto section of the reference `Dockerfile`, which was deleted in class, into its steps. Relate each step to what you would do to install software by hand on a laptop.
    - **A:** First, a command downloads a file, the Quarto installer. This is like downloading an installer from a website. Second, `apt-get` installs that file, which takes the place of double-clicking the installer. Third, the downloaded file is deleted, as you would delete an installer after using it. The work is the same as a manual install, but each step has to be a terminal command in a `RUN` line. That is why terminal commands matter for building containers. *(00:12:30)*

## 2. Installing `uv` and controlling tool versions ([29.2 `Dockerfile` command summary](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#dockerfile-command-summary))

*00:13:18–00:15:30*

- **Q:** Separate the software in the demo image by which file pins it. Name what `pyproject.toml` and `uv.lock` control, what `.python-version` controls, and what only the `Dockerfile` controls.
    - **A:** `pyproject.toml` and `uv.lock` control the versions of the Python packages, which is what a virtual environment manages. `.python-version` (`3.14`) tells `uv` which version of Python to download. `pyproject.toml` does not track the version of `uv` itself. The `Dockerfile` fixes `uv` with `COPY --from=ghcr.io/astral-sh/uv:0.13.7`, and it fixes the operating system and R with the `rocker/r-ver:4.6.2` base image. Controlling these tools, beyond the packages, is the reason the class gave for using Docker on top of a virtual environment. *(00:14:57)*

## 3. `WORKDIR` and the `.venv` problem ([29.2 `Dockerfile` command summary](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#dockerfile-command-summary))

*00:15:30–00:19:28*

- **Q:** Follow the `.venv` folder from running `uv sync` on your laptop to mounting the project folder into the container. Point out where the problem appears and how `ENV UV_PROJECT_ENVIRONMENT=/opt/venv` removes it.
    - **A:** Running `uv sync` on the laptop creates `.venv`, which holds packages built for the laptop's operating system and CPU. With three operating systems and two CPU architectures, the class counted six kinds of computer. Mounting the project folder also mounts that `.venv` into the container, whose Linux system it doesn't match. With `UV_PROJECT_ENVIRONMENT=/opt/venv` set, `uv sync` inside the image installs Linux packages into `/opt/venv`, based on `uv.lock`. Any `uv` command in the container looks there, so the mounted `.venv` is ignored. It still works on the laptop and does nothing in the container. *(00:18:25)*

## 4. Environment variables, `uv sync --locked`, and the SSH setup ([29.2 `Dockerfile` command summary](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#dockerfile-command-summary))

*00:27:21–00:30:18*

- **Q:** The demo `Dockerfile` sets `UV_PROJECT_ENVIRONMENT` twice: once with `ENV`, and once with `RUN echo "UV_PROJECT_ENVIRONMENT=$UV_PROJECT_ENVIRONMENT" >> /etc/environment`. Distinguish which kind of session each line serves, and break the second line into its parts.
    - **A:** The `ENV` line sets an environment variable that `uv` looks up whenever it runs a command in the container. A login over SSH, such as an editor connecting to the container, doesn't read `ENV`, so the variable also has to be saved to a file. In the second line, `echo` prints exactly the text it is given. `>>` appends that text to the end of `/etc/environment`, writing it as one line, and SSH logins read that file. *(00:28:41)*

## 5. `pyproject.toml` and `.python-version`

*00:30:18–00:33:30*

- **Q:** Separate the `uv` settings in the demo project by the file each one lives in. Point out why the `/opt/venv` setting is in the `Dockerfile` and not in `pyproject.toml`.
    - **A:** `add-bounds = "exact"` under `[tool.uv]` in `pyproject.toml` makes `uv add` write `==` instead of `>=`. `.python-version` holds the Python version that `uv` downloads, so different projects can run different versions of Python. `UV_PROJECT_ENVIRONMENT=/opt/venv` is set in the `Dockerfile`. You could probably put it in `pyproject.toml`, but then your own machine would install into `/opt/venv` too. Docker needs to behave slightly differently from your computer, so the settings are spread across files, and you should understand why each one sits where it does. *(00:31:47)*

## 6. Generating `uv.lock` and building the image ([29.4 Dockerfile FAQ](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#dockerfile-faq))

*00:33:30–00:35:47*

- **Q:** Trace the demo from a folder with only `Dockerfile`, `pyproject.toml` and `README.md` to a built image called `docker-uv-renv`. Which command creates each file the build needs, and which build step uses it?
    - **A:** Running `uv sync` on the laptop installed the packages, from cache, and wrote `uv.lock`; the next `ls` showed it. In `docker build --tag docker-uv-renv .`, the `.` is the current directory, where `docker build` looks for a file named `Dockerfile` by default. The build output then runs the steps in order:
        - start from the base image;
        - copy in `uv`;
        - `WORKDIR /workspace`, which creates the folder and moves into it;
        - set the environment variable;
        - `COPY pyproject.toml uv.lock .python-version ./`;
        - `RUN uv sync --locked`.

      The copy step needs `uv.lock` to be present. The `--locked` flag makes the last step fail if `pyproject.toml` and `uv.lock` disagree. *(00:35:29)*

## 7. Running the container interactively ([29.1.1 Workflow for building a Dockerfile](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#workflow-for-building-a-dockerfile))

*00:35:47–00:38:22*

- **Q:** Break `docker run --rm -it docker-uv-renv bash` into its parts. Then point out the evidence in the session that followed that the prompt belonged to a different computer.
    - **A:** `--rm` removes the container when you exit. `-it` is two single-character flags chained together: `-i` for interactive mode and `-t` for a TTY, a terminal prompt. `docker-uv-renv` is the image, and `bash` asks for a Bash prompt when the container starts. Inside, the prompt changed to `root@69b50dc7fa19:/workspace#`. `pwd` printed `/workspace`, a folder your laptop probably doesn't have, and `whoami` printed `root`. Reading the username and hostname in the prompt is how you tell which machine you are on. *(00:37:15)*

## 8. Mounting the project folder with `-v`

*00:38:22–00:42:42*

- **Q:** Set mounting the project with `-v "$(pwd):/workspace"` beside copying it into the image with `COPY`. Compare them on when the files are captured, whether you must rebuild, which way changes flow, Git and credentials, and when each is the right choice.
    - **A:** `COPY` captures the files as they were at `docker build`, so an analysis that changes every minute would need a rebuild for each change. `-v` mounts the current folder at run time, and changes on either side appear on the other immediately. With a mount, you keep using `git add`, `git commit` and `git push` on your laptop. The alternative is setting up Git credentials in a container that resets on every restart and that GitHub sees as a new machine. Baking credentials into an image would let anyone who pulls it find your SSH key, which is the password to your account. `COPY` is right for a final frozen version, for example for compliance; while you are actively working, mount. *(00:41:50)*

- **Q:** The command `docker run --rm -v "$(pwd):/workspace" -it bash` printed `Unable to find image 'bash:latest' locally` and started pulling. Trace that output back to the part of the command that caused it, and give the corrected command.
    - **A:** The image name `docker-uv-renv` was missing from the command. `docker run` takes the first argument after the flags as the image, so it read `bash` as the image name. It didn't find `bash:latest` locally and began downloading it from Docker Hub. After Ctrl-C, the corrected command was `docker run --rm -v "$(pwd):/workspace" -it docker-uv-renv bash`. In that command `docker-uv-renv` is the image and `bash` is again the command to run inside it. *(00:42:49)*

## 9. Shared files and editing in two places

*00:42:42–00:44:42*

- **Q:** Trace how edits are lost when the same file is open on both sides of a mounted folder. Point out the step where the loss happens and what prevents it.
    - **A:** The `touch hello.py` demo showed that a file created in the container appears on the laptop straight away, as on a network share drive. An editor that already has the file open doesn't reload it when the other side changes it. When you save, the editor asks whether to overwrite. Choosing overwrite is where the other side's changes disappear, because the last save wins. Daniel called it a Git conflict without being a Git conflict, with no Git to help you recover. Running the IDE's "revert file" command before you edit reloads the file from disk and avoids this. *(00:43:59)*

## 10. The `docker-compose.yml` file ([33.1 Docker Compose to launch containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-docker-compose.html#docker-compose-to-launch-containers))

*00:44:42–00:52:06*

- **Q:** Break the demo `docker-compose.yml` into its parts, and relate each to the `docker build` or `docker run` command it replaces.
    - **A:**
        - `services:` lists the containers to run; this file has one, named `analysis-env`.
        - `build: .` is the `docker build` with a `.`: if the image doesn't exist, it is built from the `Dockerfile` in this folder.
        - `image: docker-uv-renv` is the name given with `--tag`.
        - `ports: "2222:22"` maps a port on your computer to a port in the container.
        - `volumes:` plays the role of the `-v` flags. It mounts `.` at `/workspace`, and mounts your SSH public key as the container's `authorized_keys`.

      The service name can differ from the image name, so `analysis-env`, `analysis-env2` and so on could all run from one image. *(00:47:06)*

- **Q:** Break the port mapping `"2222:22"` into its two numbers and relate each to a machine. Then point out where a wrong reading goes wrong when you use someone else's Compose file.
    - **A:** The second number, `22`, is the port the software listens on inside the container; 22 is the SSH port. The first number, `2222`, is the port you connect to on your own computer. Port 22 is used for real things there, so the demo remaps it rather than risk overwriting it. `docker ps -a` later showed the same mapping as `0.0.0.0:2222->22/tcp`. If you follow someone's instructions but look at the container's number instead of the first number, it "doesn't work" only because you're looking at the wrong spot. *(00:49:13)*

- **Q:** Separate what survives a container restart from what is reset. Point out how the two `volumes:` entries and the `rm -rf /` warning fit that split.
    - **A:** Anything done inside the container is undone when it is turned off and on again: deleted files, installed packages, even a broken system. Only mounted folders keep their changes, so `.:/workspace` is how your work outlives the container. The SSH key mount puts your secret credential in the container only while it runs, never permanently in the image. The reset is what makes the container a sandbox for trying a difficult PyTorch install. It is also the only place to try `rm -rf /`, which kills the system it runs on. Never run that on your own computer. *(00:51:02)*

## 11. Docker Compose commands ([33.2 Docker Compose commands](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-docker-compose.html#docker-compose-commands))

*00:52:06–00:58:03*

- **Q:** Separate the names in the `docker ps -a` line for the running demo container: `5e67a11e10f2`, `docker-uv-renv` and `2026-11-25-docker-validate-analysis-env-1`. Then deduce why `docker compose exec 2026-11-25-docker-validate-analysis-env-1 bash` failed while `docker compose exec analysis-env bash` worked.
    - **A:** `5e67a11e10f2` is the container's unique ID, which matters because several containers can run from the same image. `docker-uv-renv` is the image built by `docker compose build`. `2026-11-25-docker-validate-analysis-env-1` is the container's name on your computer. `docker compose` commands refer to the service name from the file, `analysis-env`, not the container's name. Given the full name, Compose answered `service "2026-11-25-docker-validate-analysis-env-1" is not running`. *(00:55:59)*

- **Q:** Break the Compose lifecycle in class into `docker compose build`, `up --detach`, `exec` and `down`. Distinguish what each does, and on which machine `down` must run, as the `bash: docker: command not found` error showed.
    - **A:** `docker compose build` does the work of `docker build --tag docker-uv-renv .`; the layers were cached, so it was instant. `docker compose up --detach` runs the `docker run` equivalent for every service in the file and returns your terminal while the container runs in the background. `docker compose exec analysis-env bash` opens a shell in that running container. `docker compose down` stops and removes the containers from the file. Typed at the container's prompt, it failed because the container is a different computer with no `docker` command. After `exit`, it worked on the laptop. *(00:57:27)*

## 12. Running commands non-interactively ([33.3 Running a Docker container non-interactively using the Docker Compose](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-docker-compose.html#running-a-docker-container-non-interactively-using-the-docker-compose))

*00:58:03–01:01:10*

- **Q:** Break `docker compose run --rm analysis-env uv run python` into its parts. Then trace why the same command ending in plain `python` failed with `exec: "python": executable file not found in $PATH`.
    - **A:** `docker compose run` starts a container for a service and runs the command you give it. `--rm` turns the container off when the command finishes. `analysis-env` is the service from the compose file. Everything after the service name is any Bash command, where earlier you used `bash`. The image has no plain `python` on its path, because Python was installed and is run through `uv`. `uv run python` therefore starts the project's Python, with the packages installed from `uv.lock`. *(00:59:15)*

- **Q:** Distinguish `docker compose exec analysis-env bash` from `docker compose run --rm analysis-env <command>`: which container each uses, and what each is for in the class workflow.
    - **A:** `exec` runs a command, such as `bash`, in the container that `docker compose up --detach` already started; that container keeps running in the background. `run --rm` starts a container for the service, runs one command, and removes the container when the command finishes. Daniel said `run --rm` is one of the ways the TAs grade projects and how students should document running theirs. Sending a command such as `uv run quarto` with your file to the container tests that your analysis builds in the environment you made. *(00:58:29)*

## 13. Connecting Positron or VS Code to the container over SSH

*01:01:10–01:06:55*

- **Q:** Break down everything in the demo `Dockerfile` and `docker-compose.yml` that has to be in place for Positron to connect to `root@localhost` on port 2222. Name what each piece contributes.
    - **A:**
        - `openssh-server`, installed with `apt-get`, provides the SSH program.
        - The last `Dockerfile` line, `CMD ["/usr/sbin/sshd", "-D"]`, makes sure the SSH server is running; `docker ps -a` showed it as the container's command.
        - `"2222:22"` exposes the container's port 22 on port 2222 of your computer.
        - The volume `~/.ssh/id_ed25519.pub:/root/.ssh/authorized_keys:ro` provides your key while the container runs.
        - The username is `root`, seen in the prompt. Without it, the connection uses your laptop's username, which doesn't exist in the container.
        - The `/etc/environment` line lets SSH logins still find `/opt/venv`.

      *(01:03:12)*

- **Q:** Set the two ways of working with the container side by side: mounting the folder and testing locally, versus connecting the editor directly. Compare where commands run, how often you run them, and what Daniel does himself.
    - **A:** With the folder mounted, you work and run everything on your laptop, then test separately in the container. With a direct Remote SSH connection, the folders are already mounted, but every command runs in the container, so in theory you only run it once. In that mode the editor opens `/workspace` and its terminal shows `root@...`. Daniel usually tests locally and runs only the last command in the container, so that fewer things are open and running at once. A direct connection is the same move he made to a 128 GB RAM machine for roughly 100 GB datasets, which is cloud computing. *(01:04:10)*

## 14. Adding the validation packages

*01:08:33–01:10:16*

- **Q:** Follow `pandera`, `palmerpenguins` and `pointblank` from the failed `uv add` to an installed environment. Point out which files changed at each step and what the final `uv sync` reported.
    - **A:** `uv add pandera pointblank`, then `uv add pandera` alone, both failed with ``error: Project is missing a `[project]` table``, so no file changed. The cause wasn't worked out in class. The workaround was to add the three packages by hand to `dependencies` in `pyproject.toml`. `uv sync` then created the lock file from the TOML file. It reported `Resolved 79 packages`, installed 77 into the laptop's environment, and listed `palmerpenguins==0.1.6`, `pandera==0.36.0` and `pointblank==1.3.0`. *(00:10:04)*

## 15. Building a validation with thresholds ([41.2 Checking values](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/data-validation-python-pointblank.html#checking-values))

*01:13:41–01:18:29*

- **Q:** Break the `values = (pb.Validate(...)...interrogate())` chain in `validation.py` into its parts. Name what each contributes before the report can be read.
    - **A:**
        - `pb.Validate()` creates the testing object from the data (`penguins`), a label (`"Penguin measurements"`) and `thresholds=(0.01, 0.05, 0.10)`. The thresholds are the failure rates at which a step is flagged as a warning, an error or critical.
        - Each chained method, `col_vals_in_set()`, `col_vals_between()` and `rows_distinct()`, adds one check.
        - `.interrogate()` is what actually runs the checks.

      Displaying `values` gives a table with each step's pass/fail rate, coloured by the threshold it reached. *(01:17:12)*

- **Q:** Relate each check in the class's `pb.Validate()` chain to the kind of data problem Daniel said it catches.
    - **A:** `col_vals_in_set(columns="species", ...)` tests that a column has only the expected values. It catches human-entered data with inconsistent capitalization. `col_vals_between(columns="bill_length_mm", left=30, right=60, ...)` flags values outside a plausible range. That is the same idea as an upper bound on BMI, or the `99` codes in health surveys that stand in for missing values. `rows_distinct()` catches duplicate rows, for example when several people code the same record or sensor readings repeat. These checks can sit at different points of the analysis, such as after cleaning and before modelling, which is also a way to split the work. *(01:16:23)*

## 16. Failing checks and splitting passing and failing rows ([41.4 Splitting the passing and failing rows](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/data-validation-python-pointblank.html#splitting-the-passing-and-failing-rows))

*01:18:29–01:20:48*

- **Q:** Trace the change in the validation report after `"Gentoo"` was removed from the allowed `species` set, back to the edit and the data.
    - **A:** Before the edit, every step passed: the species values were in the set, the bill lengths were in range, and the rows were distinct. Removing `"Gentoo"` left only `"Adelie"` and `"Chinstrap"` in the `col_vals_in_set()` step. The penguins data clearly still has Gentoo rows, so those rows now fail that step. The report then shows warnings for that step, coloured by the threshold its failure rate reached. *(01:18:29)*

- **Q:** Break down the team workflow that `get_sundered_data()` enables. Name what each data frame is for and who works on it.
    - **A:** After `interrogate()`, `values.get_sundered_data(type="pass")` gives a data frame of the rows that passed. `type="fail"` gives a separate data frame of the rows that failed. The passing rows go to the next teammate, who builds the rest of the pipeline and preprocessing now. They don't get stuck on models that won't converge because of bad data. The person doing data cleaning keeps working on the failing rows, because data is never 100% clean. Both are ordinary data frames, so they can be saved as CSV files that someone else can pick up. *(01:20:07)*

---

- prompt: prompt-recall-4-analyze.md @ 65eb21c
- prompt-hash: 7dde50dd5ebf
- model: claude-opus-5-5 (requested: opus)
- backend: claude
- inputs: transcript-plaud.md, terminal.txt, materials.md, notes-class-main--claude-opus-5-5.md
- generated: 2026-11-25
- notes-input: notes-class-main--claude-opus-5-5.md @ 06f3ac544b79, links and section references removed
