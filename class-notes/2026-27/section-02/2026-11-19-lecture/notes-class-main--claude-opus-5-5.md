# Git issues and pull requests, then an introduction to Docker containers

Date: 2026-11-19

Instructor: Daniel Chen

## Summary

The session opened with a hands-on Git review. In a fresh demo repository, the instructor made a branch called `today`, edited `README.md`, pushed the branch and opened a pull request. He then introduced GitHub issues as a lightweight project board. Issues and pull requests share one numbering sequence and cross-reference each other with `#` numbers. The keywords `closes` and `fixes` in a pull request description close the linked issues automatically when the pull request is merged. He finished the review by cleaning up after a merge: switching back to `main`, pulling, deleting the branch on GitHub, then removing the stale references locally with `git fetch --prune` and `git branch -d`. Before the Git review he gave strong advice about the group project: keep the analysis simple, because this is a workflows course and not a modelling course.

The rest of the lecture introduced containers. The motivation was a project that lasts weeks or years and runs on teammates' machines with different operating systems and chip architectures. Lock files from `uv` and `renv` pin packages but not the language or system tools themselves. A container is a "virtual computer" you build from scratch and hand to everyone. It is much lighter than a virtual machine because it has no graphical interface or full operating system.

The class then used containers live. They pulled and ran `rocker/r-ver:4.3.2`, which gives R 4.3.2 next to the instructor's local R 4.6.2. They ran RStudio Server in `rocker/rstudio:4.4.2`, mapping port `8787` with `-p` and setting a password with `-e PASSWORD=...`. They opened a Bash shell inside `rocker/r-ver:4.6.2`. Packages installed by hand in a running container vanished when it restarted. That motivated the `Dockerfile`, which records the build steps.

The class wrote a three-line `Dockerfile` using `FROM`, `RUN` and `CMD`, built it with `docker build --tag hello-cowsay .`, and ran the resulting image. The image printed a cow saying "Hello from my first image!" and had the `cowsay` package installed permanently. Students leave able to run other people's containers and to build a first image of their own. Next week builds a project container with Quarto and the project's packages, and covers how to string several containers together.

## Key takeaways

- Keep the group project's analysis simple, because a correct straight-line model is far better than an ambitious model that eats the time this workflows course needs.
- Check which branch you are on before you `git add` and `git commit`, and pull `main` before starting new work.
- Writing `fixes #2` (or `closes #1`) in a pull request's description closes those issues automatically when the pull request is merged.
- A container is a virtual computer you build from scratch and share, so it pins the language version and system tools as well as the packages that `uv`/`renv` lock files cover.
- `docker run --rm -it <image>` starts an interactive container that is deleted when it stops, `-p host:container` maps a web app's port to your machine, and `-e` passes environment variables.
- Anything you install by hand in a running container is lost when it restarts, so write each working command into a `Dockerfile` as a `RUN` line.
- A `Dockerfile` starts `FROM` a base image, adds `RUN` steps, and ends with a default `CMD`; you build it from the project root with `docker build --tag <name> .`.

## Knowledge Points

### 1. Opening: pull the Docker images and start the branch exercise

*00:00:14–00:01:41*

- **Image downloads first**: three `docker pull` commands were posted in Slack. Students were asked to start them at the beginning of class because they take about ten minutes.
- **Docker Desktop must be running**: if the commands fail with an error that Docker can't be found, open the Docker Desktop application first. The commands refuse to run while it is off.
- **Warm-up exercise**: create a repository, clone it, make a branch, open a pull request and merge it.
- **Why it matters**: working with pull requests and issues is how all project-based courses in the program run from now on.

### 2. Project advice: keep the analysis simple

*00:01:41–00:05:57*

- **The biggest tip**: do not make your analysis difficult. If a straight line fits, fit the straight line model. Don't treat the project as your "time to shine" with a neural net.
- **This is not a modelling course**: the course is about workflows, and there is almost no machine learning code in the lectures. The report is not the point of the class.
- **What the project still needs**: code that downloads the data, possibly cleaning code, EDA code, modelling code, and figures and tables. All of it should stay very simple.
- **Correctness still counts**: model performance doesn't matter (60% accuracy is fine), but the techniques must be correct data science. Fitting logistic regression to predict a numeric outcome, for example, is simply wrong.
- **Portfolio ambitions**: if you want a portfolio piece, build it separately and in parallel, not in this assignment.
- **Schedule**: this week's work is getting everything onto Git, and next week is containers. It is the same project, built up over three or four weeks.

> [!WARNING]
>
> Don't pick a complicated model for the group project: "You're going to have a very bad time in about two weeks if you do that." Simple models are not penalised, but incorrect techniques are.

### 3. Git review: working on a branch

*00:06:16–00:09:50*

- **Setup**: the instructor cloned the demo repository [`2026-11-19-docker`](https://github.com/chendaniely/2026-11-19-docker) and added the line "today we will talk about containers" to `README.md`.
- **Caught on `main`**: `git status` showed he was still on branch `main`. He had not committed yet, so he could create the branch now with `git switch -c today`. Uncommitted edits travel with you to the new branch.
- **If you already committed on `main`**: there is a cheat sheet in the textbook with commands to move those commits onto a branch.
- **Branch habit**: in a branch workflow, which the course assumes from now on, look at which branch you're on right before `git add`, and definitely before `git commit`.
- **Stay up to date**: when actively collaborating, pull `main` first so you aren't making changes to something out of date.
- **The sequence**: `git diff` to review the change, `git add README.md`, `git commit -m "today we are talking about containers"`, then `git push origin today`.

> [!WARNING]
>
> With several people working on several branches, committing on the wrong branch, or on top of a stale `main`, is the common mistake. Check `git status` before you add and commit, and pull `main` before you start.

### 4. GitHub issues as a project board

*00:09:50–00:16:17*

- **What issues are for**: tracking what is happening in a project, as a simple project board. The course practises them now, and DSCI 524 covers them further.
- **Who does what**: document who is responsible for what as issues.
  - The MDS team uses an internal repository's issues for meeting notes.
  - Action items from a meeting become separate issues spawned from the notes issue.
- **Demo issues**:
  - [Issue #1 what are we doing today?](https://github.com/chendaniely/2026-11-19-docker/issues/1) asked "what is today's topic?".
  - [Issue #2 edit the readme with today's topic](https://github.com/chendaniely/2026-11-19-docker/issues/2) referred back with "meeting from #1".
- **Shared numbering**: issues and pull requests use one counter. After two issues, the next pull request is number 3.
- **Two-way references**: typing `#1` in an issue or pull request links to item 1, and item 1 automatically shows a link back. This automatic linking is a big part of why GitHub became popular, beyond Git itself.
- **Idea dump**: issues are a fine place for stray ideas such as "maybe a neural net later" or stretch goals.
  - The instructor sometimes asks a coding agent to file an issue for a passing thought, so he doesn't have to switch to a browser and lose focus.
- **Assignees and reviewers**: you can assign people to issues and to pull requests.
  - You normally assign yourself to your own pull request, which claims it as your responsibility.
  - Teammates go in the separate reviewer section. Some projects block merging until someone has reviewed.
  - In the demo the instructor added Copilot as a reviewer.
- **One pull request, many issues**: it doesn't have to be one issue, one branch, one pull request. The lab asks for three issues, and one pull request may deal with all three.

### 5. Pull request descriptions, checkboxes and closing keywords

*00:16:17–00:22:18*

- **Keep the first comment current**: edit the opening comment as decisions are made. Readers want to know "why does this exist?" from the top, not by reading the whole conversation. Project owners can usually edit others' comments too.
- **Markdown checkboxes**: `- [ ] item` lists track what is still to do. They show teammates the work isn't finished, as an alternative or complement to marking the pull request as a draft.
- **Closing keywords**: a sentence with `closes #1` or `fixes #2` in a pull request makes merging that pull request auto-close those issues. This is a GitHub feature, not a Git feature.
- **The demo pull request**: [#3 today we are talking about containers](https://github.com/chendaniely/2026-11-19-docker/pull/3) had this description:

  ```
  this is the fix for #2

  - [x] item 1
  - [ ] item 2

  closes #1 fixes #2
  ```

- **Did `closes` work?** In class the instructor wasn't sure `closes` had taken effect. He usually uses `fixes`. The demo repository shows both #1 and #2 closed by #3.
- **Commit messages work too**: keywords also work in commit messages, but they are harder to see there.
- **The payoff**: the issues tab shrinks as work merges. The instructor's textbook workflow is to file an issue, work, write "fixes #N" in the pull request, then pick the next issue from the list.
  - One textbook refactor of the containers and virtual environments chapters fixed several issues in a single pull request.
- **Grading**: you won't be graded on closing all your issues. Open stretch-goal issues are fine.

### 6. Cleaning up after a merge

*00:22:18–00:25:19*

- **Update local `main`**: `git switch main`, then `git pull origin main`, which fast-forwarded to the merge commit.
- **Delete the remote branch**: after merging, click the delete-branch button on the pull request. Alternatively, go to the branches view, find the merged branch (it shows pull request #3, merged) and click the trash can.
- **Optional in this course**: you don't have to delete branches, and you may keep them as a record. Teams and companies differ a lot in how they use Git; this is one way, and others are variations on it.
- **Remove stale references locally**:
  - `git fetch --prune` drops the `origin/today` reference to the branch deleted on GitHub.
  - `git branch -d today` deletes the local branch.
- **The history stays**: the merge commit and its parent are still in the graph. You only lose the shortcut name. That is why some people keep branches: `git switch today` is easier than switching to `3c6d82a`.

### 7. Why data science workflows need stable environments ([27.1 Documenting and loading dependencies](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#documenting-and-loading-dependencies))

*00:25:29–00:30:13*

- **What changes now**: until now, assignments came with a ready-made package list. Projects last longer than a homework assignment and involve other people.
- **Each project differs**: groups choose their own language and libraries, such as Python or R, and Altair, Plotly or Matplotlib. You adapt the environment to the project, as you would at a company.
- **Bare-minimum package lists**: don't install everything.
  - It wastes disk space.
  - Packages update on different cycles, so a big environment can become impossible to install all at once.
- **Two stability goals**:
  - Keep your own environment stable over days, weeks, months or years.
  - Make it reproducible on a teammate's machine that may run a different OS, or even a different chip. Macs and Windows machines differ, and Windows itself now ships on both ARM and Intel.
- **"It works on my machine" isn't enough**: the course's tooling is about stable computing environments and modular pipelines that others can run.

### 8. What a container is ([27.2 What is a container?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#what-is-a-container))

*00:30:13–00:34:28*

- **Where `uv`/`renv` stop**: DSCI 521 covered `uv` and `renv`, which keep package versions consistent. A `uv.lock` file lets someone install your Python packages, but they still need `uv` installed and a similarly set-up computer.
- **The container idea**: "here's my computer". You build a virtual computer from scratch, give it to everyone, and everyone runs their code on it, even on different physical machines. See [27.4 Contrasting common computational environment virtualization strategies](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#contrasting-common-computational-environment-virtualization-strategies) and [27.5 Virtualization strategy advantages and disadvantages for reproducibility](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#virtualization-strategy-advantages-and-disadvantages-for-reproducibility).
- **Prototype locally, run big**: the same environment can run on your laptop and on a larger machine that holds all the data.
- **Cost**: there is a performance hit from the extra layer.
- **Sandboxing**: remote machines' admins may not let you install software directly, but they can hand you a container to play in. If you break it, you restart it and get a fresh sandbox. It is the safe place to muck around with an operating system.
- **Tools**: the course uses Docker. LXC, LXD and Podman are alternatives, and cloud providers have their own.

### 9. Containers versus virtual machines ([27.3 Contrasting containers with virtual machines](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#contrasting-containers-with-virtual-machines))

*00:34:31–00:36:40*

- **Virtual machine**: a full-blown operating system, such as all of Windows, with its graphical interface and buttons.
- **Container**: a stripped-down version with typically no graphical interface. It holds only the bare minimum you install. This is why DSCI 521 pushed typing commands, since sometimes the terminal is the only interface you get.
- **Size and performance**: a Windows VM can take 50–80 GB. The containers used in class are a couple of GB or less yet run a full computational stack. They are lighter on disk, memory and compute.
- **VMs still have uses**: the instructor uses one to test the MDS install instructions as if on Windows.

### 10. Pulling and running a container: R 4.3.2 beside local R ([28.1.1 Launch and run containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#launch-and-run-containers))

*00:36:40–00:45:01*

- **`docker pull rocker/r-ver:4.3.2`**: downloads an image. The name looks like a GitHub user/repo because it works similarly. `rocker` is the organisation, and these images have only R installed. The tag `4.3.2` picks the R version. If the image is already present, the output says "Image is up to date" and shows a digest hash.
- **Two R versions at once**: `R --version` on the laptop shows R 4.6.2, and the container gives R 4.3.2.
- **Real-world case**: in pharmaceutical work, clinical trials research runs for years while R updates every six months. Regulators can ask for your code *and* the full compute environment, so you hand over the container that ran the analysis.
- **Beyond lock files**: lock files pin packages; containers pin the tools themselves, such as R or Git. A container with an old Git could even prevent anyone from using `git switch`.
- **Similar names across tools**: `docker pull` echoes `git pull` because tools borrow each other's vocabulary.
- **`docker run` flags**:
  - `--rm`: a double dash marks a multi-letter flag. When the container stops, it is deleted automatically; otherwise you delete it by hand.
  - `-it`: single-letter flags can be chained, as in `ls -alh`. `-i` is interactive and `-t` allocates a terminal (TTY). You'll see `-it` everywhere.
  - The image name comes last. `docker run` also downloads the image if it isn't present.
- **Isolation shown**: in the container, `library(tidyverse)` fails because the image has only R. In a local terminal, tidyverse loads fine. Two terminals on one laptop behave like two different machines.

### 11. Know which machine you are typing on

*00:45:01–00:46:44*

- **Read your prompt**: after quitting the container, the laptop's own prompt returns. The prompt is often your only visual cue.
- **Same idea remotely**: the instructor opened a terminal on a machine in his closet at home. The only clue was the hostname he'd given it.
- **Why `whoami` exists**: it reports the username on that computer, which is another way to confirm you're on the machine you think you are.
- **Applies everywhere**: the same habit matters in containers and on remote cloud systems.

> [!WARNING]
>
> With containers and remote machines you are sometimes given nothing but a blinking cursor. Check your prompt (or `whoami`) before running commands, so you don't run something on the wrong machine.

### 12. Why so many data science tools run in a browser

*00:46:44–00:49:11*

- **Applications as browsers**: many desktop apps are built on Electron, which is essentially a browser packaged as an app.
- **Why**: a browser-first application can run inside a container or on a remote machine while you view it in your local browser.
- **Jupyter Lab**: you open it at a `localhost` address because it was designed to run on remote machines with more cores and memory but the same interface.
- **VS Code**: it is effectively a big browser app. GitHub's Codespaces button gives you VS Code in a browser, running on a machine whose whole compute environment someone has set up.

### 13. Running RStudio in a container and mapping ports ([28.1.3 Mapping ports to containers with web apps](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#mapping-ports-to-containers-with-web-apps))

*00:54:10–00:58:59*

- **Jupyter users too**: projects are written in Quarto, but the same setup applies if you prefer a Jupyter interface.
- **Keep `--rm`**: each running container uses RAM. Without it you can end up with "five computers" running and a laptop that grinds to a halt.
- **Ports**: like Jupyter Lab on `8888`, RStudio Server listens on `8787` inside the container. The numbers are arbitrary choices by the tool's developers.
- **`-p host:container`**: the left number is the port on your machine and the right is the port in the container. `-p 8787:8787` puts the container's 8787 on the laptop's 8787. To run RStudio twice, map the second container to a different host port.
- **Open it**: go to `localhost:8787` in the browser. The username is `rstudio`, and the start-up output prints a generated password.
- **Different machines again**: this RStudio runs R 4.4.2 in the container. The desktop RStudio runs the laptop's R 4.6.2, and the earlier `r-ver` container ran R 4.3.2.

> [!WARNING]
>
> Running containers without `--rm`, or leaving several running, keeps using your computer's RAM. Use `--rm` so a container is cleaned up when you exit.

### 14. Passing environment variables into a container

*00:59:20–01:02:53*

- **`-e NAME=value`**: passes an environment variable into the container. `rocker/rstudio` reads `PASSWORD`, so `-e PASSWORD="apassword"` replaces the hard-to-remember generated password (see the RStudio exercise in [27.2 What is a container?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#what-is-a-container)).
- **Container-specific**: not every container supports the same variables. It depends on how the image was built, so check its documentation.
- **Showing the password is fine here**: the port is only reachable from the instructor's own machine. If you can't log into his laptop, his `8787` isn't available to you.
- **Looking ahead to DSCI 532**: a dashboard runs in a browser. Put the dashboard code in a container and anyone with Docker can `docker run` it and visit the port. They skip the whole install process (`renv`, snapshots and so on) because you've given them a computer you built from scratch.

### 15. Starting from a base image and working inside it ([29.1.1 Workflow for building a Dockerfile](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#workflow-for-building-a-dockerfile))

*01:03:00–01:08:19*

- **Start from someone else's machine**: when building your own container you still pick a starting machine. `rocker/r-ver:4.6.2` already has R plus the system pieces R needs, the equivalent of the compiler tools students installed on their laptops. That saves steps.
- **Override the default command**: `docker run --rm -it rocker/r-ver:4.6.2 bash` gives a shell instead of R. The prompt changes to the container's (`root@<id>:/#`), and you can still type `R` to start R (see [28.1.4 Changing the containers default command](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#changing-the-containers-default-command)).
- **Try first, then document**: test install steps interactively, and once they work, write them down as the build instructions.
- **Demo**: `install.packages("cowsay")` in the container's R, then `cowsay::say('hello')` drew an ASCII cow. The instructor used `cowsay` instead of tidyverse because tidyverse takes far too long to install.
- **No saved state**: after exiting and starting the container again, `library(cowsay)` failed with "there is no package called 'cowsay'". A container resets to how its image was built every time.
- **A good place to experiment**: even destructive commands from DSCI 521 are safe in a container, because restarting gives a clean machine.
- **The problem this creates**: making users follow README install steps inside a container every time is painful, for example a 15-minute tidyverse install for a 30-second analysis.

### 16. Running R from the command line with `Rscript -e` ([29.1.2 Build your first image](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#build-your-first-image))

*01:08:19–01:10:18*

- **The key question**: do you know the terminal command that makes the install happen? Build steps have to be shell commands.
- **`Rscript`**: runs R code from the shell. `-e` means "here is an R expression".
- **The command**: `Rscript -e "install.packages('cowsay')"`. Note the quoting: double quotes outside and single quotes inside.
- **Confirmed, then lost**: R in that container could `library(cowsay)` afterwards. Exiting and re-entering lost it again, so the information has to be saved somewhere.

### 17. The `Dockerfile`: `FROM`, `RUN`, `CMD` ([29.2 `Dockerfile` command summary](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#dockerfile-command-summary))

*01:10:18–01:15:01*

- **`Dockerfile`**: a special file named with a capital D. It holds the instructions for installing and setting up the computer. The `rocker` images have their own `Dockerfile`s, which is how RStudio comes installed with its port open. See also [27.6 Container usage workflow](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#container-usage-workflow).
- **`FROM`** (all caps): normally the first line. It names the starting machine, here `rocker/r-ver:4.6.2`.
  - You could start from a bare-minimum Linux and install everything yourself. That is a good learning project for a break.
  - Disk space is relatively cheap, so a beefier base image is acceptable.
- **`RUN`**: the shell commands the image runs during the build, here the same `Rscript -e` line tested by hand.
- **`CMD`**: what a container from the image runs by default.
  - It is written as a list instead of space-separated words.
  - It runs only if you don't give another command such as `bash`, which overrides it.
  - `ENTRYPOINT` also exists, but the instructor called it rare.
- **The class's file** ([`Dockerfile`](https://github.com/chendaniely/2026-11-19-docker/blob/main/Dockerfile)):

  ```dockerfile
  FROM rocker/r-ver:4.6.2

  RUN Rscript -e "install.packages('cowsay')"

  CMD ["Rscript", "-e", "cowsay::say('Hello from my first image!')"]
  ```

- **For a Python project**: the `RUN` section would install `uv`, `COPY` in the lock files and run `uv sync`. Next week, project containers also install the language and Quarto.

### 18. Building and running your own image ([29.1 Building container images from `Dockerfile`'s](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#building-container-images-from-dockerfiles))

*01:15:01–01:18:44*

- **`docker build --tag hello-cowsay .`**: `--tag` names the image.
  - The `.` is the directory to build from, the current one. It may be the first time a lone `.` is something you must type.
  - Docker looks for a file named exactly `Dockerfile` there.
- **Run from the project root**: you can point `docker build` at another path. Milestone instructions assume every command runs from the repository root, so commands can be copy-pasted without changing directories (see [29.4 Dockerfile FAQ](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#dockerfile-faq)).
- **`docker images`**: lists every image on your machine, including the new `hello-cowsay`.
- **Run it**: `docker run --rm -it hello-cowsay` prints the cow message from `CMD`.
- **Shell access**: `docker run --rm -it hello-cowsay bash` gives a shell inside the image, which is useful when something "works on my machine but not in the container". There, `library(cowsay)` now loads, because the build installed it.
- **Typical shape**: one `FROM`, a middle section of many `RUN` and `COPY` lines (and port instructions where relevant), and a `CMD`. Writing it all depends on knowing shell commands.

### 19. Pinning versions, and what comes next

*01:18:44–01:20:39*

- **Next week**: this week's lab doesn't need any of this. Next week's work does.
- **Pin the language**: the `FROM` line pins the R version. A placeholder section would then hold the `renv` or `uv` setup that installs the packages.
- **Pin the tools**: you can choose a specific, even older, Quarto version. A year later you are still on the same versions, as long as you don't touch that install line.
- **A real failure**: in another class a few weeks earlier, the instructor restarted a container without hard-pinned versions. Something had updated the day before, and nothing worked. Hours of fixing an update instead of doing the real work is why you control what updates and when.
- **Coming up**: more on building containers, and stringing several containers together.

> [!WARNING]
>
> If you don't pin versions in your container, an upstream update can break everything overnight, as it did in the instructor's other class. Install explicit versions and change them only when you mean to.

## Not reached in class

- [27.7 Image vs container?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#image-vs-container)
- [27.8 What is a container registry?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#what-is-a-container-registry)
- [28.1.2 Mounting volumes to containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#mounting-volumes-to-containers)
- [28.1.5 Use a container to execute a script](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#use-a-container-to-execute-a-script)
- [28.2 Docker command-line commands](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#docker-command-line-commands)
- [29.1.3 Layer caching](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#layer-caching)
- [29.1.4 Guidelines for `RUN` commands](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#guidelines-for-run-commands)
- [29.2.1 `CMD` or `ENTRYPOINT`?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#cmd-or-entrypoint)
- [29.3 Choosing a base image for your Dockerfile](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#choosing-a-base-image-for-your-dockerfile)
- [33 Containers: Docker Compose](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-docker-compose.html)

## Commands from class

### Pull the images before class

```bash
docker pull rocker/r-ver:4.3.2
docker pull rocker/rstudio:4.4.2
docker pull quay.io/jupyter/datascience-notebook:2025-03-14
```

These are the three commands from Slack. Docker Desktop must be running first.

### Clone the demo repository and make a branch

```bash
cd ~/git
git clone git@github.com:chendaniely/2026-11-19-docker.git
cd 2026-11-19-docker
positron .                       # open in the editor; README.md edited here
git status                       # still on main, README.md modified
git pull origin main             # make sure main is up to date
git switch -c today              # uncommitted edit moves to the new branch
git status
git diff                         # review the added line
git add README.md
git commit -m "today we are talking about containers"
git push origin today
```

On GitHub the instructor opened issues #1 and #2, then the pull request that fixes both: [#3](https://github.com/chendaniely/2026-11-19-docker/pull/3).

### Clean up after merging

```bash
git switch main
git pull origin main             # fast-forwards to the merge commit
git log --oneline --graph --all
git fetch --prune                # drop origin/today, deleted on GitHub
git log --oneline --graph --all
git branch -d today              # delete the local branch
git log --oneline --graph --all
```

The three `git log` runs show the references disappearing while the history stays:

```
*   d25ddfa (HEAD -> main, origin/main, origin/HEAD) Merge pull request #3 from chendaniely/today
|\  
| * 3c6d82a (origin/today, today) today we are talking about containers
|/  
* deb10c5 Initial commit
```

After `git fetch --prune` the commit is labelled `(today)` only. After `git branch -d today` it has no label at all:

```
| * 3c6d82a today we are talking about containers
```

### Run R 4.3.2 in a container

```bash
R --version                              # local R: 4.6.2
docker pull rocker/r-ver:4.3.2
docker run --rm -it rocker/r-ver:4.3.2   # opens R 4.3.2; library(tidyverse) fails; q() to quit
```

### Run RStudio Server in a container

```bash
docker pull rocker/rstudio:4.4.2
docker run --rm -p 8787:8787 rocker/rstudio:4.4.2                          # visit localhost:8787, user rstudio
docker run --rm -p 8787:8787 -e PASSWORD="apassword" rocker/rstudio:4.4.2  # choose your own password
```

Without `-e PASSWORD`, the start-up output tells you the generated password and how to set your own:

```
The password is set to ooph3Aef2Ohcahcu
If you want to set your own password, set the PASSWORD environment variable. e.g. run with:
docker run -e PASSWORD=<YOUR_PASS> -p 8787:8787 rocker/rstudio
```

### Try installs interactively in the base image

```bash
docker run --rm -it rocker/r-ver:4.6.2 bash
# in R: install.packages("cowsay"); library(cowsay); cowsay::say('hello')
# exit, then start again:
docker run --rm -it rocker/r-ver:4.6.2 bash
# in R: library(cowsay) -> error, the package is gone
Rscript -e "install.packages('cowsay')"   # the shell form of the install, for a RUN line
docker run --rm -it rocker/r-ver:4.6.2 bash
# in R: library(cowsay) -> error again after the restart
```

### Build and run your own image

```bash
docker build --tag hello-cowsay .        # from the folder holding the Dockerfile
docker images                            # hello-cowsay:latest now listed
docker run --rm -it hello-cowsay         # runs the CMD: the cow says hello
docker run --rm -it hello-cowsay bash    # shell instead; library(cowsay) now works in R
```

An excerpt from `docker images`, showing how the sizes compare:

```
IMAGE                    ID             DISK USAGE   CONTENT SIZE
hello-cowsay:latest      abd88b403482       1.45GB          390MB
rocker/r-ver:4.3.2       4e32addfc4da       1.11GB          313MB
rocker/r-ver:4.6.2       8739c76d2d93       1.85GB          795MB
rocker/rstudio:4.4.2     6bfc87fb66d0       3.16GB          734MB
```

### What went wrong live

- **Edited on `main` before branching**: `git status` showed `On branch main` with `README.md` modified. Nothing had been committed yet, so `git switch -c today` carried the change onto the new branch and the rest of the workflow went ahead normally.
- **RStudio container wouldn't stop on one Ctrl+C**: the log shows the container waiting on `[s6-finish] waiting for services.`. More Ctrl+C presses ended it with `got 3 SIGTERM/SIGINTs, forcefully exiting`. Because of `--rm`, the forced exit still cleaned the container up.

## Questions

- **Q:** A student asked about this week's individual lab assignment and how much analysis it needs. **A:** The individual assignments are meant to be short, to make sure you know how to do the main assignment. This week is about getting everything onto Git, and next week is containers. The project is one analysis built on for three or four weeks. It must be as detailed as the assignment asks, and simple models such as linear or logistic regression are not penalised, but they must be used correctly.
- **Q:** (question inaudible) A student apparently asked why the project needs machine learning when the course has no modelling. **A:** You won't see machine learning code in class, but you need a machine learning project as the analysis that the workflow tools are applied to.
- **Q:** A student asked what an "instance" is, as in a cloud compute instance. **A:** Containers are almost like instances. Cloud providers such as Google don't give you an actual machine; they give you a container on one of their servers. Pretty much all cloud compute runs on some form of containers rather than bare access to hardware.

## Assignments

- [ ] Lab 3, this week's project work: get the group project onto Git with a branch-and-pull-request workflow, and create at least three issues, using `fixes #N` where a pull request resolves them. Details are on the assignment page in the [student repository](https://github.com/UBC-MDS/DSCI_522_dsci-workflows_students).

---

- prompt: prompt-notes.md @ 8bcc190
- prompt-hash: a00c660964b7
- model: claude-opus-5-5 (requested: opus)
- backend: claude
- inputs: transcript-plaud.md, history.txt, terminal.txt, materials.md
- generated: 2026-11-20
