# Introduction to Containers with Docker (plus Issues and Pull Request Workflow Review)

Date Time: 2026-11-19

Instructor: Daniel Chen

## Summary

The session opened with project advice, then reviewed the Git workflow students need for this week's lab. In a demo repository (<https://github.com/chendaniely/2026-11-19-docker>), the instructor made an edit and moved it onto a new branch. He committed it, pushed it and opened a pull request. He then showed how GitHub issues and pull requests work together as a lightweight project-management system. Issues and pull requests share one numbering sequence, `#N` creates two-way references between them, and you can assign people and reviewers. Task-list checkboxes track unfinished work. The keywords `fixes #N` and `closes #N` in a pull request close the matching issues automatically when the pull request is merged. After the merge he cleaned up with `git fetch --prune` and `git branch -d`.

The project advice was blunt: **keep your analysis simple**. DSCI 522 is not a modelling course. A linear or logistic regression is fine, as long as it is technically correct. An ambitious model will make the next few weeks very hard.

The main topic was containers. Lock files from `uv` and `renv` pin package versions. They do not pin the language version itself, system tools such as Git, or differences between operating systems and CPU architectures. A container gives everyone the same "virtual computer" to run the analysis in. The instructor compared containers with virtual machines, which are larger, include a full OS and usually a GUI. He then ran other people's images: an R-only `rocker/r-ver:4.3.2` container next to his local R 4.6.2, and RStudio Server in `rocker/rstudio:4.4.2`, reached in a browser through port mapping and an environment variable for the password.

Finally the class built its first image. The instructor showed that anything installed by hand inside a running container disappears when the container stops. That is why the install steps belong in a `Dockerfile` (`FROM`, `RUN`, `CMD`), which `docker build --tag hello-cowsay .` turns into an image. Students won't need a `Dockerfile` for this week's lab, but they will next week. Docker Compose and running several containers together were planned for the next class.

## Knowledge Points

### 1. Project advice: keep the analysis simple

- **The analysis is not the point of the course**: the course is about workflows, not model fitting. You will see almost no machine learning code in lectures.
- **Still required**: code that downloads the data, any cleaning, EDA, modelling code, figures and tables. Keep each part very simple.
- **Correctness still matters**: the score of the model does not matter (60% accuracy is fine), but the methods must be correct. For example, do not fit logistic regression to predict a numeric outcome.
- **Warning**: do not use this project as your portfolio piece. Choosing something complicated such as a neural net will give you "a very bad time in about two weeks". Do a portfolio project in parallel if you want one.
- **Same project throughout**: you build on the same project for three or four weeks. This week is getting everything on Git; next week is containers.
- **Language choice**: R projects are allowed, but class demos will be in Python. Package choices such as Altair, Plotly or Matplotlib may differ between groups, so each project must define its own minimal package list.

### 2. Branch workflow habits

- **Check your branch before `git add`, and definitely before `git commit`**: branch-based work is assumed from now on. Run `git status` and read the "On branch …" line.
- **Pull `main` before starting work**: with several people working on several branches, this avoids building on out-of-date code.
- **Edited files while on `main`?** If you have not committed yet, `git switch -c <branch>` takes your uncommitted changes onto the new branch. If you already committed on `main`, the [textbook](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/) has a cheat sheet of commands to move the commits.

### 3. GitHub issues as project management

- **Issues track what is happening in a project**: you can use them for:
  - assigning responsibility (who is doing what);
  - meeting notes, from which separate action-item issues are created;
  - parking ideas and stretch goals (for example, "it would be nice to try a neural net");
  - asking a coding agent to file an issue for a passing thought, which the instructor does himself.
- **Shared numbering**: issues and pull requests use one counter. In the demo, issues #1 and #2 were followed by pull request #3.
- **`#N` references are two-way**: writing "meeting from #1" in issue #2 also shows a link back on #1. This automatic cross-linking is a GitHub feature, not a Git one, and is a big reason GitHub became popular.
- **Assignees and reviewers**: you usually assign yourself to your own pull request. You can request a teammate (or Copilot, as in the demo) as a reviewer. Some projects block merging until someone has reviewed the work.
- **Keep the first comment up to date**: readers look at the first comment to learn why an issue or pull request exists, not at the whole conversation. Edit it when decisions change. Project owners can edit other people's comments.
- **Task lists**: Markdown checkboxes (`- [ ]`, `- [x]`) in issues and pull requests show what is still unfinished. A **draft** pull request is the other way to signal "not done yet".
- **For this course**: you must create at least three issues. One pull request may handle all three. You are not graded on closing every issue, so feel free to record longer-term ideas as issues.
- Demo artefacts: [Issue #1](https://github.com/chendaniely/2026-11-19-docker/issues/1), [Issue #2](https://github.com/chendaniely/2026-11-19-docker/issues/2), [Pull request #3](https://github.com/chendaniely/2026-11-19-docker/pull/3).

### 4. Closing keywords in pull requests

- **`fixes #N` / `closes #N`**: when a pull request containing these is merged, GitHub closes the referenced issues automatically.
  - The demo PR description was:
    ```
    this is the fix for #2

    - [x] item 1
    - [ ] item 2

    closes #1 fixes #2
    ```
  - In class the instructor briefly wondered whether `closes` worked, saying "`fixes` is the one I almost always use". The demo repository shows both issue #1 and issue #2 were closed by PR #3, so both keywords work.
- **Write the message strategically**: one pull request can close several issues, so you don't have to close each one by hand. The keywords also work in commit messages, but they are harder to see there.
- The instructor uses this for the textbook: he files issues, then lists `fixes #…` in the pull request, so his open-issues tab doubles as a to-do list.

### 5. Cleaning up after a merge

- **Delete the remote branch on GitHub**: use the "Delete branch" button on the merged pull request, or the trash-can icon on the repository's Branches page.
- **Deleting branches is optional in this course**: some people keep branches as a record. Teams and companies differ in how they use Git, so this is one workflow, not the only one.
- **`git fetch --prune`**: removes local references to remote branches that no longer exist (here, `origin/today`).
- **`git branch -d today`**: deletes the local branch label.
- **History is kept**: the merge commit and the branch's commit still show in `git log --oneline --graph --all`. Only the shortcut name disappears, so you would now need the hash (`3c6d82a`) instead of `git switch today`. Clean up when too many branch labels make the graph hard to read.

### 6. Why containers? The problem a stable compute environment solves

([Introduction to containerization](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html))

- **Projects last a long time and involve other people**: you need a stable environment for yourself over days, months or years, and one that also works for teammates.
- **Teammates' machines differ**: Mac vs Windows, and ARM vs Intel chips even among Windows machines. "It works on my machine" is not good enough when a teammate cannot run your code.
- **What virtual environments already cover**: `uv` (Python) and `renv` (R), from 521, pin *package* versions through lock files.
- **What they don't cover**: the language version itself, and system tools.
  - Example: a container with a 2019 version of Git would not have `git switch`.
  - Lock files also assume the other person has `uv` installed. Installing it might disturb their setup.
- **A container is a virtual computer you build from scratch and hand to others**: everyone runs code on "the same computer" even on different hardware.
- **Pharmaceutical example**: clinical trial analyses can run for years, while R releases roughly every six months. Regulators reviewing a drug submission want the code *and* the full compute environment, so you give them the container that ran the analysis.
- **Other uses**:
  - prototyping locally, then running the identical environment on a bigger machine that has the data;
  - giving someone a sandbox on a shared or remote machine without letting them install software directly on it.
- **Containers reset**: if you break one, restart it and you get a fresh one. This makes them a safe place to learn Linux and the command line.
- **Cost**: there is a performance hit from the extra layer, but this is often worth it.
- **Other container tools exist**: LXC, LXD, Podman. Cloud compute mostly runs on containers, so you rarely get bare access to a machine.

### 7. Containers vs virtual machines

- **Virtual machine**: a full operating system, typically with the full graphical interface. A Windows VM is roughly a 50–80 GB install. The instructor still uses VMs, for example to test the MDS install instructions as if on Windows.
- **Container**: only the minimum set of things you install, usually with no GUI. That is one reason 521 pushed typing commands in the terminal. Many containers are under 1–2 GB yet run a full computational stack.
- **Result**: containers use less disk, memory and compute than VMs.

### 8. Pulling and running other people's images

([Using and running containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html))

- **Docker Desktop must be running** before any `docker` command (on Mac and Windows). If you get a "can't find Docker" error, Docker is not installed.
- **`docker pull <image>`**: downloads an image, like `git pull` pulls code. Names look like a GitHub user and repository: `rocker/r-ver:4.3.2` is the `rocker` organisation's R-only image, with the tag `4.3.2` meaning R 4.3.2. If the image is already up to date, Docker says so and shows its digest (hash).
- **`docker run`**: starts (turns on) a machine from an image. It also downloads the image first if you don't have it.
- **`--rm`**: a double-dash, multi-letter flag. It deletes the container when it stops; otherwise you have to delete it by hand.
- **`-it`**: two single-letter flags chained together, the same way `ls -alh` chains `-a`, `-l` and `-h`.
  - `-i`: interactive, so what you type reaches the container.
  - `-t`: gives you a terminal (TTY) to interact with.
- **Demo result**: `rocker/r-ver:4.3.2` opened R 4.3.2, while `R --version` on the host showed R 4.6.2. Two versions of R ran side by side on one laptop.
- **Each container is a separate machine**: `library(tidyverse)` failed in the container ("there is no package called 'tidyverse'") but worked on the host.
- **Know where you are typing**: the prompt is often your only cue to whether you are on your laptop, in a container, or on a remote machine. Inside a container the prompt looks like `root@<id>:/#`. The instructor also showed a terminal on a machine at home, recognisable only by its hostname. Commands like `whoami` help confirm where you are.

### 9. Web applications in containers: ports and environment variables

- **Browser-based apps**: many tools (Electron apps, JupyterLab, VS Code, GitHub Codespaces) run as browser applications. That is why they can run in a container or on a remote machine with the same interface. It is also why JupyterLab opens at a `localhost` address.
- **`-p <host port>:<container port>`**: maps a port inside the container to a port on your computer.
  - RStudio Server listens on 8787, so `-p 8787:8787`, then open `localhost:8787`.
  - JupyterLab uses 8888.
  - These numbers are arbitrary choices by each tool.
  - To run two copies of the same app, map the container's 8787 to a different free port on your computer.
- **RStudio login**: the username is `rstudio`. Without a password set, the container prints a random one at startup, which is hard to remember.
- **`-e VAR=value`**: passes an environment variable into the container, for example `-e PASSWORD="apassword"`. Which variables an image understands depends on how its authors built it, so check its documentation.
- **Is a visible password a problem here?** The port is only reachable from the instructor's own machine, so a simple demo password is acceptable in this context.
- **Warning: every running container uses RAM.** Use `--rm` so containers are removed when they stop. Otherwise you will wonder why your computer is slow and find you have "five computers" running.
- **Looking ahead**: in DSCI 532 you can put a dashboard in a container. Users then only need Docker and one `docker run` command, with no `renv` or `uv` setup of their own.

### 10. Building your own image with a `Dockerfile`

([Customizing and building containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html))

- **Containers don't keep changes**: the instructor installed `cowsay` inside a running `rocker/r-ver:4.6.2` container. After exiting and starting a new container, `library(cowsay)` failed again. Every new container starts fresh from its image.
  - **Good**: this makes containers a safe place for dangerous experiments, including the destructive "delete the computer" command warned about in 521.
  - **Bad**: users should not have to follow README install steps every time. A tidyverse install on Linux can take about 15 minutes for a 30-second analysis.
- **Recommended workflow**:
  1. Start the base image with `bash` instead of its default program.
  2. Try the install commands interactively until they work.
  3. Write the working commands into the `Dockerfile`.
- **Installing from the terminal**: `Rscript -e "install.packages('cowsay')"` runs an R expression from bash. **Watch the quotes**: double quotes outside, single quotes inside.
- **`Dockerfile`**: a file with exactly that name, capital D and no extension, containing the build instructions for the machine. Published images such as RStudio have their own `Dockerfile`.
- **`FROM`**: the starting-point machine. It is the first line, apart from optional metadata.
  - Starting from `rocker/r-ver:4.6.2` skips steps such as installing compilers, which the image authors have already done.
  - Smaller, bare-bones Linux bases exist, but then you install everything yourself.
- **`RUN`**: a shell command executed while the image is being built. Most `Dockerfile`s are mostly `RUN` and `COPY` lines, and sometimes port lines (for example, opening 8787).
  - Knowing the bash command for each install step is essential.
  - For Python, you would `COPY` in your lock files and run `uv sync`.
- **`CMD`**: the default command when the container starts, written as a list (`["Rscript", "-e", "..."]`). Adding a command after the image name in `docker run` (for example `bash`) overrides it.
- **`ENTRYPOINT`**: also exists, but the instructor called it pretty rare.
- The class `Dockerfile` ([in the demo repo](https://github.com/chendaniely/2026-11-19-docker/blob/main/Dockerfile)):
  ```dockerfile
  FROM rocker/r-ver:4.6.2

  RUN Rscript -e "install.packages('cowsay')"

  CMD ["Rscript", "-e", "cowsay::say('Hello from my first image!')"]
  ```
- **`docker build --tag hello-cowsay .`**: `--tag` names the image. The `.` is the current directory, where `docker build` looks for a file named `Dockerfile`.
  - This is "probably the first time a dot is actually something you have to type".
  - Course instructions, including milestone 1, assume you run every command from the repository root, so commands can be copied and pasted without changing directories.
- **`docker images`**: lists the images on your computer. The new `hello-cowsay` image appeared at 1.45 GB.
- **Pin versions**: pin the language and tool versions (R, Python, Quarto) in the `Dockerfile` so nothing updates until you change that line.
  - **Warning**: in another class the instructor restarted a container with no pinned versions. Something had updated the day before and nothing worked. Fixing an unexpected update can take longer than the real work.
- **Next week**: install your language, Quarto (copy-paste install steps will be provided) and your packages in a container, so the analysis runs both locally and in the container.

## Commands from class

### Pull the images ahead of time (the three commands posted in Slack)

```bash
docker pull rocker/r-ver:4.3.2
docker pull rocker/rstudio:4.4.2
docker pull quay.io/jupyter/datascience-notebook:2025-03-14
```

Docker Desktop must be open first. These downloads take a while, so start them before class.

### Clone the demo repository and open it

```bash
cd ~/git
git clone git@github.com:chendaniely/2026-11-19-docker.git
cd 2026-11-19-docker
positron .                       # open the project in the editor
```

### Move an uncommitted edit onto a branch, commit, push

```bash
git status                       # showed "On branch main" with README.md modified
git pull origin main             # make sure main is up to date
git switch -c today              # new branch; the uncommitted change comes along
git status                       # now "On branch today"
git diff                         # review the added line
git add README.md
git commit -m "today we are talking about containers"
git push origin today
```

The push output includes a link to open the pull request on GitHub. Issues #1 and #2 and pull request #3 were created in the browser.

### Sync main after the merge and clean up

```bash
git status
git switch main
git pull origin main             # fast-forwards to the merge commit
git log --oneline --graph --all
git fetch --prune                # drop origin/today, already deleted on GitHub
git log --oneline --graph --all
git branch -d today              # drop the local branch label
git log --oneline --graph --all
```

Running `git log` three times shows the labels disappear while the history stays:

```
*   d25ddfa (HEAD -> main, origin/main, origin/HEAD) Merge pull request #3 from chendaniely/today
|\  
| * 3c6d82a (origin/today, today) today we are talking about containers
|/  
* deb10c5 Initial commit
```

After `git fetch --prune` (` - [deleted] (none) -> origin/today`), the commit shows only `(today)`. After `git branch -d today` (`Deleted branch today (was 3c6d82a).`), it has no label at all:

```
| * 3c6d82a today we are talking about containers
```

### Run an R-only container alongside your local R

```bash
R --version                              # host: R version 4.6.2
docker pull rocker/r-ver:4.3.2           # already up to date
docker run --rm -it rocker/r-ver:4.3.2   # drops you straight into R 4.3.2
```

Inside, `library(tidyverse)` fails because the container only has R:

```
> library(tidyverse)
Error in library(tidyverse) : there is no package called ‘tidyverse’
```

Quit with `q()`.

### Run RStudio Server in a container

```bash
docker pull rocker/rstudio:4.4.2
docker run --rm -p 8787:8787 rocker/rstudio:4.4.2                          # random password printed
docker run --rm -p 8787:8787 -e PASSWORD="apassword" rocker/rstudio:4.4.2  # choose your own
```

Open `localhost:8787` and sign in as `rstudio`. Without `-e PASSWORD`, the startup log tells you what to do:

```
The password is set to ooph3Aef2Ohcahcu
If you want to set your own password, set the PASSWORD environment variable. e.g. run with:
docker run -e PASSWORD=<YOUR_PASS> -p 8787:8787 rocker/rstudio
```

### Try installs interactively in a base image

```bash
docker run --rm -it rocker/r-ver:4.6.2 bash   # bash prompt instead of R
# inside R: install.packages("cowsay"); library(cowsay); cowsay::say('hello')
exit
docker run --rm -it rocker/r-ver:4.6.2 bash   # fresh container: cowsay is gone again
Rscript -e "install.packages('cowsay')"       # the same install as one shell command
exit
docker run --rm -it rocker/r-ver:4.6.2 bash   # gone again -> it needs to go in a Dockerfile
```

### Build and run your own image

```bash
docker build --tag hello-cowsay .        # run from the folder containing the Dockerfile
docker images                            # hello-cowsay:latest is listed
docker run --rm -it hello-cowsay         # runs the CMD: prints the cowsay message
docker run --rm -it hello-cowsay bash    # override CMD; library(cowsay) now works in R
```

The build output shows each `Dockerfile` step:

```
 => [1/2] FROM docker.io/rocker/r-ver:4.6.2@sha256:8739c76d2d93166  0.0s
 => CACHED [2/2] RUN Rscript -e "install.packages('cowsay')"        0.0s
 => => naming to docker.io/library/hello-cowsay:latest              0.0s
```

### What went wrong live

- **Edited `README.md` while still on `main`**: `git status` reported `On branch main` with `README.md` modified, but the exercise asked for a branch. Nothing had been committed yet, so `git switch -c today` moved the uncommitted change onto the new branch. If you have already committed on `main`, use the textbook's cheat sheet instead.
- **Stopping the RStudio container took several Ctrl+C presses**: the first `^C` started the container's shutdown scripts. It then sat at `[s6-finish] waiting for services.` until two more presses forced it: `got 3 SIGTERM/SIGINTs, forcefully exiting`. Because of `--rm`, the container was removed either way.
- **Installed packages vanished between runs**: `cowsay` installed in one `rocker/r-ver:4.6.2` container was missing (`there is no package called ‘cowsay’`) in the next one, twice. This was the intended lesson. The fix was to put the `Rscript -e "install.packages('cowsay')"` line in a `Dockerfile` as a `RUN` step and build an image.

## Questions

- **Q:** A student asked how much analysis the assignment expects, noting that the individual assignments are supposed to be very short.
  **A:** Do a very simple data analysis, as detailed as the assignment's steps ask for. This week is about getting everything on Git; next week is containers. Linear or logistic regression is fine and won't be penalised for simplicity, but it must be done correctly. Don't use logistic regression for a numeric outcome. It is the same project, built on for three or four weeks. Class shows no machine learning code, but you still need a machine learning project to start from.
- **Q:** A student asked what an "instance" is.
  **A:** Containers are essentially instances. Cloud providers such as Google don't give you a physical machine; they give you a container on one of their servers. Nearly all cloud compute runs on some form of container.

## Assignments

- [ ] Before the containers material: open Docker Desktop and pull the three images posted in Slack (`rocker/r-ver:4.3.2`, `rocker/rstudio:4.4.2`, `quay.io/jupyter/datascience-notebook:2025-03-14`).
- [ ] This week's lab: practise the branch → pull request → merge workflow, and create at least three issues for your project. One pull request may close all three, using `fixes #N`. See the assignment pages in the [student repository](https://github.com/UBC-MDS/DSCI_522_dsci-workflows_students).
- [ ] Project: get everything on Git this week, and keep the analysis simple but technically correct.
- [ ] Next week: containerise the project, installing R or Python, Quarto and your packages in a `Dockerfile`. A `Dockerfile` is not needed for this week's lab.

---

- prompt: prompt-notes-original.md @ 979670b
- prompt-hash: f78026c179ce
- model: claude-opus-5-5 (requested: opus)
- backend: claude
- inputs: transcript-plaud.md, history.txt, terminal.txt, materials.md
- generated: 2026-11-19
