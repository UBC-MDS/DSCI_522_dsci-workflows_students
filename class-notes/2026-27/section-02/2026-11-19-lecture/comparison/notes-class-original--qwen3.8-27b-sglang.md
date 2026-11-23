# Git Pull Request Review and Intro to Docker Containers

Date Time: 2026-11-19

Instructor: Daniel Chen

## Summary

The session opened with a Git branch-workflow review in the demo repository [2026-11-19-docker](https://github.com/chendaniely/2026-11-19-docker). The instructor cloned it, noticed the `README.md` edit was sitting on `main`, created the `today` branch with `git switch -c` before committing, committed "today we are talking about containers", and pushed. The GitHub side was then walked through live: issues #1 ("what are we doing today?") and #2 ("edit the readme with today's topic"), and [pull request #3](https://github.com/chendaniely/2026-11-19-docker/pull/3), whose description ends with `closes #1 fixes #2` so the issues auto-close when the PR merges. After merging, the branch was deleted on GitHub and the stale references were cleaned up locally with `git fetch --prune` and `git branch -d today`, leaving the merge commit visible in `git log --oneline --graph --all`.

Daniel Chen also gave group-project advice: keep the analysis short and technically correct. Fit the straight line if that's what you have; do not reach for a neural net — "you're going to have a very bad time in about two weeks." Model accuracy is not graded; correctness is. The same project is built on for three or four weeks, with this week's milestone being getting everything on Git and next week's being containers; the very short individual assignments exist to make sure students can do the main assignment.

The main topic was containers ([textbook chapter 27](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html)). The motivating problem is "it works on my machine": lock files pin package versions, but containers go one level deeper and pin the tools and operating-system user space themselves. That was demonstrated by running `rocker/r-ver:4.3.2` next to the host's R 4.6.2 — the container ran R 4.3.2 and failed on `library(tidyverse)` while the host succeeded. The `rocker/rstudio:4.4.2` image was then run as a web app on port 8787, first with the auto-generated password printed to the terminal, then with `-e PASSWORD="apassword"`; the `-p host:container` mapping is what allows multiple instances of the same app at once.

The class ended by building its first image ([chapter 29](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html)): the R package `cowsay` was installed in a live container, the install was shown to vanish when the container restarted, and the working command `Rscript -e "install.packages('cowsay')"` was captured in a `Dockerfile` with `FROM`, `RUN`, and `CMD`. `docker build --tag hello-cowsay .` produced the image, and `docker run` executed the cowsay message by default. The closing warning was about version pinning — Quarto is at 1.11; pin 1.10 if you want to stay put — and Docker Compose (chapter 33) is flagged for next class; it was not covered today.

## Knowledge Points

### 1. Branch, issue, and pull-request workflow (Git review)

- **Before you commit, check your branch**: run `git status` right before `git add` and definitely before `git commit`, and habitually `git pull origin main` first so you're not branching from an out-of-date `main`. If you accidentally commit on `main`, the textbook has a set of recovery commands.
- **`git switch -c <name>`**: create and switch to a new branch; uncommitted working-tree changes come along with you (the demo edited `README.md` on `main`, then created `today` before committing).
- **Pushing offers the PR**: `git push origin today` prints a GitHub URL (`.../pull/new/today`) that opens the pull-request form.
- **Issues and pull requests share one numbering sequence**: in the demo repo, issues [#1](https://github.com/chendaniely/2026-11-19-docker/issues/1) and [#2](https://github.com/chendaniely/2026-11-19-docker/issues/2) were followed by [PR #3](https://github.com/chendaniely/2026-11-19-docker/pull/3). You can reference any item by number (e.g. "meeting from #1") and the reference is two-way — both items link to each other.
- **`closes` / `fixes` keywords**: a sentence in the PR description that ends with `closes #1 fixes #2` makes GitHub auto-close those issues when the PR is merged. This is a GitHub service feature, not a Git feature. One PR may deal with several issues (the lab task required three issues); referencing the same issue multiple times is fine.
- **Descriptions are editable and Markdown**: keep the first comment of an issue or PR as the source of truth and edit it as decisions evolve; use checkboxes (`- [ ] item 2`) to track to-dos; assignees claim responsibility ("this is my responsibility, I'm claiming it") while reviewers are requested separately — the instructor assigned Copilot as a reviewer.
- **Issues as meeting notes**: record meeting notes on the issue board, then spawn action items out as separate issues. The instructor also files issues from an AI agent mid-work ("I just had this idea, can you file the issue?") instead of tabbing away to a browser.
- **Cleanup after merging**: delete the remote branch on GitHub (the "delete branch" button in the PR, or the trash can in the branches view), then `git fetch --prune` to drop the `origin/today` tracking ref and `git branch -d today` (lowercase `-d`) to drop the local ref. The merge commit remains visible in `git log --oneline --graph --all`. Deletion is not required in this class — keeping branches as a record is fine — and different teams use different Git conventions, so this is one valid workflow, not the only one.

### 2. Project scoping (the MDS group project)

- **Do not make your analysis difficult**: this was the biggest tip of the session. If the model is a straight line, fit the straight line; do not say "it's my time to shine" and build a neural net — "you're going to have a very bad time in about two weeks." This is not a model-fitting course; you will almost never see machine-learning code in the lectures.
- **Accuracy is not graded; correctness is**: a 60%-accurate model is acceptable, but the technique must be right — "you shouldn't be fitting logistic regression when you're trying to predict a numeric outcome. That's just wrong."
- **Don't turn it into a portfolio project**: if you want a showcase project, do it in parallel, not inside this assignment.
- **Scope still includes**: code that downloads the data, some cleaning, some EDA, modeling code, and figures/tables — just keep each part very simple. R or Python is fine, and per-project package choices (Altair, Plotly, Matplotlib, ...) are expected; the instructor no longer provides one package list.
- **Milestone sequence**: the same project is built on for three or four weeks. This week: getting everything on Git. Next week: containers. Follow the steps in the assignment in the [student repository](https://github.com/UBC-MDS/DSCI_522_dsci-workflows_students).

### 3. Why containers exist

- **The goal of the class**: create a compute environment you can share with other people and run all of your code through — because "this works on my machine" doesn't work when a teammate can't run your code.
- **Lock files vs. containers**: `uv` and `renv` lock files track *package* versions; containers go one level deeper and pin the tools themselves — the version of R, even the version of Git (joke: ship a 2019-era Git in the container and teammates can't run `git switch`).
- **Real-world example**: multi-year clinical-trial research needs a fixed R version even though R ships updates every six months; drug regulators ask for your code *and* your compute environment so they can reproduce the analysis. You hand over the container that ran the analysis, not your MacBook.
- **Hardware diversity**: Mac vs Windows, ARM vs Intel chips — install paths differ, so a shared container is the same on all of them.
- **Containers vs. virtual machines**: a VM installs a full OS (a Windows install is a 50–80 GB affair; the VM itself can take ~80 GB) with a GUI. A container is a stripped-down OS user-space with only what you install — the rocker images here are under 1–2 GB — so containers are lighter on disk, memory, and compute. They are *less* isolated than VMs, and there is a performance hit from the extra layer that there's no way around.
- **Ephemeral by design**: a running container has no save state; turn it off and it resets to the image. That's a feature for experimenting: "if you blow it up, then you just restart it" — containers are a safe place to practice destructive commands and OS mucking-around. Remote machines also hand you containers as sandboxes when you can't (or aren't trusted to) install software directly.
- **Ecosystem**: Docker is the tool in this course; LXC, LXD, podman, and cloud providers' own options also exist. Cloud compute generally runs on containers — you get a container on a server, not bare access to a machine.

### 4. Pulling and running images

- **Docker Desktop must be open** on macOS/Windows before any Docker command; a "can't find Docker" error means the app isn't running.
- **`docker pull <registry>/<user>/<image>:<tag>`**: downloads an image from a registry without running it (Docker Hub by default; `quay.io` when the name says so). The `rocker` organization publishes images that only have R installed (`rocker/r-ver`), plus R+RStudio (`rocker/rstudio`).
- **The three class images** (pulled from the commands posted in Slack; ~13 GB of disk space, ~3 GB to download in total): `rocker/r-ver:4.3.2`, `rocker/rstudio:4.4.2`, and `quay.io/jupyter/datascience-notebook:2025-03-14` (the largest, ~9 GB). Pulling them before class avoids waiting ~20 minutes mid-lecture; `docker run` will also pull a missing image on the fly.
- **`docker run --rm -it <image>`**: `--rm` deletes the container when it stops, so stopped containers don't pile up and eat RAM; `-i` (`--interactive`) passes your typing in, and `-t` (TTY) gives you a terminal to interact with — "you don't have to know what that is, but you'll see it everywhere."
- **The image's default command runs automatically**: `rocker/r-ver`'s `Dockerfile` sets `CMD ["R"]`, so the run command dropped straight into an R session — R 4.3.2 (2023-10-31) "Eye Holes" on Linux, versus the host's R 4.6.2, proven by running `R --version` first.
- **Proof it's a different machine**: `library(tidyverse)` failed inside the fresh container with `Error in library(tidyverse) : there is no package called 'tidyverse'` while the same command works on the host. Pay attention to where you're typing — the prompt changes when you're inside a container or on a remote machine (the instructor's "machine in the closet" example), and `whoami`-style commands from DSCI 521 help confirm which machine you're on. `q()` quits R and exits the container.

### 5. Web apps in containers: ports and environment variables

- **Browser-first applications**: RStudio Server, JupyterLab, and VS Code are built as web apps so the same interface can run on a remote machine with more cores and memory — JupyterLab lives at `localhost:8888` for the same reason, and GitHub's Codespaces button is VS Code in a browser. Electron apps follow the same "the browser is the application" pattern.
- **Port mapping with `-p`**: `-p <host_port>:<container_port>` forwards a port on your computer to the app's port inside the container. RStudio listens on 8787 inside the image, so `docker run --rm -p 8787:8787 rocker/rstudio:4.4.2` puts it at <http://localhost:8787>. To run a *second* RStudio at the same time, map a different host port to the same container port. These port numbers are arbitrary conventions (Jupyter's is 8888); the container-side port is documented per image.
- **Authentication**: the first run prints a random password to the terminal (`The password is set to ...`). Set your own with an environment variable: `-e PASSWORD="apassword"` (multiple `-e` flags allowed). Sign in at <http://localhost:8787> with username `rstudio`.
- **Stopping it**: the web app runs in the foreground, so `Ctrl+C` in that terminal stops the container.
- **Security note confirmed in class**: even with the port number known, the app is only reachable from the host machine — without access to the physical machine, port 8787 is not available to you.
- **DSCI 532 preview**: a dashboard can be shipped as a container; the end user only needs Docker, not your whole install process.

### 6. Building your own image: the `Dockerfile`

- **The problem it solves**: packages installed in a running container disappear when it restarts (demonstrated live with `cowsay`), and teammates shouldn't have to follow your README's install steps every time — tidyverse on a bare Linux machine can be a 15-minute install for a 30-second script.
- **`Rscript -e "<R expression>"`**: runs R non-interactively from the shell — `Rscript -e "install.packages('cowsay')"` — which is the form a `RUN` line needs. Mind the nested quotes: double on the outside, single on the inside.
- **`Dockerfile`** (capital D, no extension, lives in the project root): the plain-text build recipe, version-controlled in Git alongside your analysis code.
  - `FROM <base>`: the starting machine. `rocker/r-ver:4.6.2` already has R 4.6.2 plus the system packages R needs; you could start from a bare-minimum Linux image and install everything by hand.
  - `RUN <bash command>`: shell commands executed during the build.
  - `CMD [...]`: the default command a container runs when it starts (JSON-list form); it replaces the base image's own `CMD ["R"]`. `ENTRYPOINT` exists but is "pretty rare".
  - The file the class wrote, committed to `main` in the [demo repository's Dockerfile](https://github.com/chendaniely/2026-11-19-docker/blob/main/Dockerfile):

    ```dockerfile
    FROM rocker/r-ver:4.6.2

    RUN Rscript -e "install.packages('cowsay')"

    CMD ["Rscript", "-e", "cowsay::say('Hello from my first image!')"]
    ```
- **Recommended workflow**: try the install commands interactively first — `docker run --rm -it rocker/r-ver:4.6.2 bash` gives you the container's shell instead of R (a command after the image name replaces the default `CMD`) — verify they work, then write them into the `Dockerfile`; add every couple of lines and rebuild while you go.
- **`docker build --tag hello-cowsay .`**: `--tag` names the image (no version given → `latest`); `.` means "the `Dockerfile` in the current directory" — the first time a dot is something you actually type. Docker by default looks for a file named exactly `Dockerfile`; you can also point it at a full path to another file. Assume all commands run from the project root — that's what milestone-one instructions will say. The build prints each step, and unchanged steps show as `CACHED` (the class's build reused the already-run install layer).
- **`docker images`**: lists local images with their disk usage — `hello-cowsay:latest` came out at 1.45 GB on disk.
- **Running the result**: `docker run --rm -it hello-cowsay` executed the `CMD` — the ASCII-art "Hello from my first image!" — while `docker run --rm -it hello-cowsay bash` opened a shell where `library(cowsay)` now works because the install is baked into the image.
- **Pin your versions (flagged as a real pain point)**: pin the base-image tag and any tool versions — Quarto is at 1.11; the instructor suggested building on 1.10 if you want to stay there. Anecdote: a container restarted without hard version pins picked up an upstream update the day before and "nothing worked" — hours spent fixing the update instead of doing the work.
- **Coming up**: next week's milestone builds an image that installs R or Python, Quarto, and your packages (materials sketch `COPY`-ing lock files plus `uv sync` / `renv` restore in the image); Docker Compose ([chapter 33](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-docker-compose.html)) is next class, not covered today.

## Commands from class

### Pull the class images (Slack assignment, done before class)

```bash
docker pull rocker/r-ver:4.3.2
docker pull rocker/rstudio:4.4.2
docker pull quay.io/jupyter/datascience-notebook:2025-03-14   # largest of the three, ~9 GB
```

Start Docker Desktop first. The instructor posted these in Slack so they'd be done in ~10 minutes before class; by the time they were re-run in the demo repo the output reported `Status: Image is up to date`.

### Get the demo repository and check where things stand

```bash
cd ~/git
git clone git@github.com:chendaniely/2026-11-19-docker.git
cd 2026-11-19-docker
git status            # on main; README.md modified, not staged
git pull origin main  # habit: sync main before branching off it
```

### Create the branch, commit, and push

```bash
git switch -c today                                   # branch 'today' from main; edits come along
git diff                                              # new line in README.md
git add README.md
git commit -m "today we are talking about containers"
git push origin today
```

The push output pointed at the PR form (`https://github.com/chendaniely/2026-11-19-docker/pull/new/today`). The instructor then created issues #1 and #2 in the GitHub UI and opened [PR #3](https://github.com/chendaniely/2026-11-19-docker/pull/3) with the description `this is the fix for #2 ... - [x] item 1 / - [ ] item 2 / closes #1 fixes #2`.

### After the merge: sync `main` and clean up branch references

```bash
git switch main
git pull origin main                   # fast-forward to the merge commit
git log --oneline --graph --all        # still shows the origin/today reference
git fetch --prune                      # drop remote-tracking refs for branches deleted on GitHub
git branch -d today                    # delete the local branch (already merged)
```

The branch was first deleted on GitHub (trash-can button in the branches view). After `git fetch --prune` (`- [deleted] ... -> origin/today`) and `git branch -d`, the history looked like:

```
*   d25ddfa (HEAD -> main, origin/main, origin/HEAD) Merge pull request #3 from chendaniely/today
|\
| * 3c6d82a today we are talking about containers
|/
* deb10c5 Initial commit
```

The merge commit and the original commit remain; only the quick shortcut reference (`git switch today`) is gone.

### Compare the host's R with a container's R

```bash
R --version                                  # host: R version 4.6.2 (2026-10-29)
docker run --rm -it rocker/r-ver:4.3.2       # --rm deletes on exit; -it = interactive + TTY
```

R 4.3.2 started directly inside the container. Inside:

```
> library(tidyverse)
Error in library(tidyverse) : there is no package called 'tidyverse'
> q()
```

The same `library(tidyverse)` worked in the host's R — the container only has R in it.

### Run RStudio as a web app

```bash
docker run --rm -p 8787:8787 rocker/rstudio:4.4.2
docker run --rm -p 8787:8787 -e PASSWORD="apassword" rocker/rstudio:4.4.2
```

The first run generated and printed a password:

```
The password is set to ooph3Aef2Ohcahcu
If you want to set your own password, set the PASSWORD environment variable. e.g. run with:
docker run -e PASSWORD=<YOUR_PASS> -p 8787:8787 rocker/rstudio
```

Then open <http://localhost:8787> in a browser and sign in as user `rstudio` — with the printed password, or `apassword` on the second run. The local RStudio (R 4.6.2) and the containerized one (R 4.4.2) are different machines. Stop the foreground app with `Ctrl+C`.

### Show that changes don't persist in a running container

```bash
docker run --rm -it rocker/r-ver:4.6.2 bash    # trailing 'bash' replaces the default R command
# at the container's prompt:
R
library(cowsay)                                 # error: there is no package called 'cowsay'
install.packages("cowsay")                      # installs with deps crayon, rlang
library(cowsay)
cowsay::say('hello')
exit
# restart the same image:
docker run --rm -it rocker/r-ver:4.6.2 bash
R
library(cowsay)                                 # gone again — the container reset to the image
Rscript -e "install.packages('cowsay')"         # non-interactive form, ready for the Dockerfile
```

```
 _______
< hello >
 -------
      \
       \
```

### Build and run the `hello-cowsay` image

The `Dockerfile` in the current directory (see Knowledge Point 6):

```dockerfile
FROM rocker/r-ver:4.6.2

RUN Rscript -e "install.packages('cowsay')"

CMD ["Rscript", "-e", "cowsay::say('Hello from my first image!')"]
```

```bash
docker build --tag hello-cowsay .      # build from ./Dockerfile; 'RUN' step reported CACHED
docker images                          # hello-cowsay:latest, 1.45 GB on disk
docker run --rm -it hello-cowsay       # runs the CMD: the cowsay message
docker run --rm -it hello-cowsay bash  # shell in the built image; library(cowsay) works
```

```
 ____________________________
< Hello from my first image! >
 ----------------------------
```

### What went wrong live

- **Stopping the RStudio web app**: it runs in the foreground, so it takes `Ctrl+C` in that terminal to kill it — the log shows repeated `^C` and then `got 3 SIGTERM/SIGINTs, forcefully exiting` before the container actually died.
- **Stray keystroke inside the container**: typing `n` at the container's bash prompt gave `bash: n: command not found` — a harmless typo, no effect on the container.
- **`library(tidyverse)` / `library(cowsay)` errors**: not bugs — new containers contain only what the image was built with. This was the deliberate demonstration that motivated the `RUN` line: installs made in a live container are lost on restart.

## Questions

- **Q:** Wasn't that an individual assignment? (asking about today's Lab session 3)
  **A:** Yes — the individual assignments are deliberately very short, to make sure you know how to do the main assignment. This week's milestone is getting everything on Git, next week's is containers; follow the steps in the assignment, and keep the underlying data analysis very simple.

- **Q:** Does it matter that the container's password is sitting in plain text in the terminal — can anyone else reach the app on port 8787?
  **A:** No. The only way to have access to that container is to have access to the physical machine; even knowing the port is useless if you can't log into that machine, so 8787 is not available to you from elsewhere (confirmed by a student during the question).

## Assignments

- [ ] Pull the three class images now (commands shared in Slack): `docker pull rocker/r-ver:4.3.2`, `docker pull rocker/rstudio:4.4.2`, `docker pull quay.io/jupyter/datascience-notebook:2025-03-14` — needed for next week's containers milestone; ~10 minutes.
- [ ] Lab 3 in-class practice (2026-11-19): edit `README.md` on a branch, create three issues, open a pull request that `closes`/`fixes` them, merge, then delete the branch and prune references.
- [ ] This week's individual assignment: getting everything on Git — follow the steps in the assignment page of the [student repository](https://github.com/UBC-MDS/DSCI_522_dsci-workflows_students); due this week (no specific due date was stated in class).
- [ ] Next week's milestone: containers — build an image that installs R or Python, Quarto, and your packages, with versions pinned ([chapters 28–29](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html)); Docker Compose ([chapter 33](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-docker-compose.html)) is previewed for next class.

---

- prompt: prompt-notes-original.md @ 979670b
- prompt-hash: f78026c179ce
- model: qwen3.8-27b-sglang (requested: qwen3.8-27b-sglang)
- backend: local (SGLang)
- inputs: transcript-plaud.md, history.txt, terminal.txt, materials.md
- generated: 2026-11-19
