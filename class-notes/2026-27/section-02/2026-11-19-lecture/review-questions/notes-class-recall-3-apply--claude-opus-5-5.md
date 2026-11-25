# Git pull requests and an introduction to Docker containers: review questions, tier 3 — Apply

Date: 2026-11-19

Instructor: Daniel Chen

*Tier 3 of 5: Apply. Work each situation through before you read the answer; tiers 1 (Remember) and 2 (Understand) cover the facts and reasons it relies on.*

## 1. Opening: pull the Docker images and start the branch exercise

*00:00:14–00:01:41*

- **Q:** You paste a `docker pull` command into your terminal and get an error saying Docker can't be found. What do you check, and in what order?
    - **A:** First check that the Docker Desktop application is open, because the Docker commands won't work while it is off. If there is no Docker application to open, you need to install Docker. *(00:00:33)*

- **Q:** You need the three course images, `rocker/r-ver:4.3.2`, `rocker/rstudio:4.4.2` and `quay.io/jupyter/datascience-notebook:2025-03-14`, for an exercise later in the session. When should you start the `docker pull` commands, and why?
    - **A:** Start them right at the beginning, before the exercises. The downloads take around ten minutes, so pulling early means the images are ready when you need them. *(00:00:18)*

- **Q:** You are doing the warm-up exercise in a fresh repository. Put these steps in order: merge the pull request, make a branch, clone the repository, open a pull request, create the repository.
    - **A:** Create the repository, clone it to your computer, make a branch, open a pull request, then merge it. This branch-and-pull-request cycle is the workflow that project-based courses use from now on. *(00:00:43)*

## 2. Project advice: keep the analysis simple

*00:01:41–00:05:57*

- **Q:** Your group's data looks roughly linear, but a teammate wants to use the project to build a neural network. What do you choose, and why?
    - **A:** Fit the simple straight-line model. This is a workflows course, not a modelling course, and an ambitious model means "you're going to have a very bad time in about two weeks." Simple models are not penalised. *(00:02:03)*

- **Q:** Your group's outcome variable is numeric, and a teammate proposes logistic regression because it is simple. Is that acceptable for the project?
    - **A:** No. Simplicity is fine, but the technique must be correct, and fitting logistic regression to predict a numeric outcome is just wrong. Choose a model that suits a numeric outcome, such as linear regression. *(00:05:24)*

- **Q:** Your model reaches only about 60% accuracy, and you want to keep improving it so the project can go in your portfolio. What should you do?
    - **A:** Leave the course project as it is, because the results of the model don't matter as long as the methods are technically correct. If you want a portfolio piece, build it separately, in parallel, and not in this assignment. *(00:03:08)*

## 3. Git review: working on a branch

*00:06:16–00:09:50*

- **Q:** In the demo repository `2026-11-19-docker`, you add a line to `README.md` and then `git status` says `On branch main`. You have not committed anything yet. What do you run to put this work on a branch called `today`?
    - **A:** Run `git switch -c today`. Because nothing has been committed, the uncommitted edit comes with you, and `git status` then reports `On branch today` with `README.md` modified. *(00:08:57)*

- **Q:** You have an edited `README.md` on a new branch called `today`. In order, what do you run to review the change, commit it and send it to GitHub?
    - **A:** Run `git diff` to review the added line, then `git add README.md`, then `git commit -m "today we are talking about containers"`, then `git push origin today`. GitHub then offers a pull request for the `today` branch. *(00:09:25)*

- **Q:** Your group is actively working on several branches at once, and you are about to start a new piece of work. What do you do first, and what do you check before you `git add` and `git commit`?
    - **A:** Pull the `main` branch first (`git pull origin main`), so you aren't changing something that is out of date. Then, right before `git add`, and definitely before `git commit`, check which branch you are on with `git status`. Committing on the wrong branch, or on a stale `main`, is the common mistake. *(00:08:27)*

- **Q:** You realise you have already made commits on `main` that should have gone on a branch. Where do you look for a fix?
    - **A:** Use the cheat sheet in the textbook, which gives a set of commands for moving those commits around. Switching with `git switch -c` alone only carries work you have not committed yet. *(00:07:44)*

## 4. GitHub issues as a project board

*00:09:50–00:16:17*

- **Q:** Your repository has two issues, #1 and #2, and nothing else. You now open a pull request. What number will it get?
    - **A:** It will be #3. Issues and pull requests share one counter on GitHub, so the pull request takes the next number after the issues. *(00:12:07)*

- **Q:** You write "meeting from #1" in the body of issue #2. What will someone see when they open issue #1?
    - **A:** Issue #1 shows a link back to #2. A `#` number creates a two-way reference, so the two items link to each other automatically. *(00:13:34)*

- **Q:** Your group keeps its meeting notes in one issue, and the meeting produces action items for different people. How do you track them?
    - **A:** Write the action items in the notes issue, then create a separate issue for each one, spawned from that note. Assign each issue to the person responsible, so the board shows who is responsible for what. *(00:11:08)*

- **Q:** You open a pull request in your group project and want a teammate to check your work before it goes in. How do you set the pull request up?
    - **A:** Assign yourself, because it is your pull request and that claims it as your responsibility. Add your teammate in the separate reviewer section. Some projects block changes until someone has reviewed them. *(00:14:47)*

- **Q:** Your lab asks for three issues, and one branch ends up resolving all three. Do you need three separate branches and pull requests?
    - **A:** No. It does not have to be one issue, one branch, one pull request; one pull request may deal with all three issues. What matters is getting experience with the issue system. *(00:14:23)*

- **Q:** While coding, you think of a stretch idea for the project ("maybe a neural net later") that nobody will work on now. Where do you record it?
    - **A:** File it as an issue. Issues are a fine place to dump ideas and stretch goals so they aren't lost, even if they are never acted on. *(00:12:37)*

## 5. Pull request descriptions, checkboxes and closing keywords

*00:16:17–00:22:18*

- **Q:** Pull request #3 in the demo repository resolves issue #2. What do you write in the pull request's description so that #2 closes without any extra clicks, and when does it close?
    - **A:** Write a closing keyword with the issue number, such as `fixes #2`. When the pull request is merged, GitHub closes the issue automatically. This is a GitHub feature, not a Git feature. *(00:19:30)*

- **Q:** One pull request in your project resolves issues #4, #5 and #6. How do you avoid closing each issue by hand after the merge?
    - **A:** Write the description strategically, with a keyword for each issue, for example `fixes #4`, `fixes #5` and `fixes #6`. Merging then closes all three, so you don't go back and click close three times. *(00:21:02)*

- **Q:** You could put `fixes #2` in a commit message or in the pull request description. Which do you choose, and why?
    - **A:** Both work, but put it in the pull request description. A keyword in a commit message is harder to see, while one in the description is visible to everyone reading the pull request. *(00:19:55)*

- **Q:** Your pull request is open but two tasks are still unfinished, and you want teammates to see that at a glance. What can you add?
    - **A:** Either mark the pull request as a draft, or add Markdown checkboxes to its description, such as `- [x] item 1` and `- [ ] item 2`. Unchecked boxes show the work isn't done yet. *(00:17:49)*

- **Q:** Partway through a long pull request conversation, your team makes a major decision. Where do you record it?
    - **A:** Edit the first comment of the pull request so it describes the decision. Readers want to know why the pull request exists without reading the whole conversation, and project owners can usually edit other people's comments too. *(00:16:56)*

- **Q:** Your group finishes the project with some stretch-goal issues still open. Will this cost you marks?
    - **A:** No. You are not graded on having every issue closed by the end, so leaving issues open for longer-term ideas is fine. *(00:21:50)*

## 6. Cleaning up after a merge

*00:22:18–00:25:19*

- **Q:** Your pull request from the `today` branch has just been merged on GitHub, and you are still on `today` locally. What do you run to get the merged work into your local `main`?
    - **A:** Run `git switch main`, then `git pull origin main`. The pull fast-forwards your `main` to the merge commit from the pull request. *(00:22:25)*

- **Q:** After a merge, you want to delete the `today` branch on GitHub, but you have navigated away from the pull request page. Where do you go?
    - **A:** Open the branches view, find the `today` branch (it shows pull request #3, merged) and click the trash can. On the pull request page itself, a delete-branch button appears after merging. *(00:22:53)*

- **Q:** You deleted `today` on GitHub, but `git log --oneline --graph --all` still shows `(origin/today, today)` next to commit `3c6d82a`. What do you run to remove both labels, and what remains afterwards?
    - **A:** Run `git fetch --prune` to drop the stale `origin/today` reference, then `git branch -d today` to delete the local branch. The commit and the merge are still in the history; you only lose the shortcut names. *(00:24:30)*

- **Q:** You expect to return to the work on a merged branch later. Why might you keep the branch instead of deleting it?
    - **A:** Keeping it means you can run `git switch today` instead of switching to a commit hash like `3c6d82a`. Deleting branches is optional in this course, and teams differ in how they handle it. *(00:25:05)*

## 7. Why data science workflows need stable environments ([27 Introduction to containerization](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html))

*00:25:29–00:30:13*

- **Q:** To avoid missing-package errors, a teammate proposes installing every package you might possibly use. What problems do you predict?
    - **A:** It wastes disk space on packages you mostly never use. Worse, packages update on different cycles, so updating everything at once can leave you with packages that are incompatible and an environment you cannot install at all. Keep the package list to the bare minimum. *(00:28:04)*

- **Q:** Your code runs on your Mac, and a teammate on an ARM Windows laptop needs to run it. Is "it works on my machine" good enough, and what do you need?
    - **A:** No. Different operating systems and chips install things differently, so you need a computing environment you can share and that runs the same on their machine. That is what the course's tooling, ending with containers, is for. *(00:28:53)*

- **Q:** Your project will run for several months. Besides your teammates' machines, which environment do you also need to keep stable?
    - **A:** Your own, over time. You need packages and tools not to upgrade underneath you during the project, as well as making the environment reproducible for other people. *(00:28:26)*

## 8. What a container is ([27.2 What is a container?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#what-is-a-container))

*00:30:13–00:34:28*

- **Q:** You send a collaborator your `uv.lock` file, but they don't use `uv` and worry that installing it will disturb their setup. What can you give them instead?
    - **A:** A container: a virtual computer you build from scratch with everything installed, so they run your code on it instead of on their own setup. A lock file only pins the packages and still assumes the receiving computer is set up like yours. *(00:31:17)*

- **Q:** You prototype on your laptop, but the full analysis must run on a larger machine that holds all the data. How do you make sure both machines have the same compute environment?
    - **A:** Run the analysis in the same container on both machines. The container carries the whole environment, so it is identical wherever it runs. Expect a small performance cost from the extra layer. *(00:32:15)*

- **Q:** You want to experiment with risky operating-system commands without damaging your laptop. Where do you run them, and what happens if you break things?
    - **A:** Run them in a container. If you blow it up, you just restart it and get a fresh sandbox. *(00:33:13)*

- **Q:** The administrators of a shared remote server won't let you install Python directly on it. How can you still get your environment there?
    - **A:** Ask for a container on the server. It gives you a sandbox to install and play in without touching the machine itself, and if you mess it up, it can be restarted fresh. *(00:32:34)*

## 9. Containers versus virtual machines ([27.3 Contrasting containers with virtual machines](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#contrasting-containers-with-virtual-machines))

*00:34:31–00:36:40*

- **Q:** You need to share a full computational stack for an analysis, and you are worried about disk space and memory. Which do you choose, a container or a virtual machine, and roughly how big will it be?
    - **A:** A container. A Windows virtual machine can take 50–80 GB, while the containers used here are under two gigabytes yet still run a full stack. Containers are also lighter on memory and compute. *(00:36:16)*

- **Q:** You need to test install instructions exactly as a Windows user would see them, clicking through the Windows interface. Which do you choose, a container or a virtual machine?
    - **A:** A virtual machine. It installs a full operating system with its graphical interface, which is why one is still used to test the MDS install instructions as if on Windows. A container typically has no graphical interface. *(00:36:01)*

- **Q:** You start a container and expect to double-click through folders. What will you actually get, and what skill does it rely on?
    - **A:** You will get only a terminal, because containers usually have no graphical interface. You have to type commands, such as `cd`, to move around, which is why typing shell commands matters so much. *(00:35:00)*

## 10. Pulling and running a container: R 4.3.2 beside local R ([28.1.1 Launch and run containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#launch-and-run-containers))

*00:36:40–00:45:01*

- **Q:** You already pulled `rocker/r-ver:4.3.2` before class, and you run `docker pull rocker/r-ver:4.3.2` again. What do you expect to see?
    - **A:** A short output with a `Digest: sha256:...` hash and `Status: Image is up to date for rocker/r-ver:4.3.2`. Nothing is downloaded again unless a newer version of the image has been published. *(00:39:51)*

- **Q:** `R --version` on your laptop reports R 4.6.2. You run `docker run --rm -it rocker/r-ver:4.3.2`. Which R version starts, and why?
    - **A:** R 4.3.2 starts, because the container has its own R installed, separate from your laptop's. This is how you can have two versions of R on one computer. *(00:42:38)*

- **Q:** Inside `docker run --rm -it rocker/r-ver:4.3.2` you type `library(tidyverse)`, and it works fine in R on your laptop. What happens in the container, and why?
    - **A:** It fails with `there is no package called 'tidyverse'`. The image contains only R, and the container behaves like a separate machine that doesn't see your laptop's packages. *(00:43:54)*

- **Q:** You leave `--rm` out of `docker run -it rocker/r-ver:4.3.2`. What happens to the container when you quit?
    - **A:** It is not deleted automatically, so you have to delete it by hand later. With `--rm`, the container is removed as soon as it stops. *(00:40:55)*

- **Q:** Your `docker run` command needs both interactive input and a terminal. How do you write those two single-letter flags, and what does each do?
    - **A:** Write them chained together as `-it`, the same way `ls -alh` chains flags. `-i` makes the session interactive, so what you type reaches the program, and `-t` gives you a terminal (TTY) to interact with. *(00:41:48)*

- **Q:** You run `docker run --rm -it` with an image you never pulled. What will Docker do?
    - **A:** It downloads the image first and then runs it. `docker run` pulls an image that isn't already on your machine; pulling ahead of time just saves waiting. *(00:42:16)*

- **Q:** Your clinical-trials analysis must stay reproducible for years, R releases a new version about every six months, and a regulator will ask for your full compute environment. What do you hand over?
    - **A:** The container that ran the analysis. It pins the version of R itself, not just the packages that a `uv` or `renv` lock file tracks, so the analysis can be reproduced without your laptop. *(00:38:46)*

- **Q:** You want everyone on a project to use a specific system tool version, for example an older Git that lacks `git switch`. Can a lock file enforce that? What can?
    - **A:** No: lock files only track packages, not tools installed on the system. A container can, because it ships with the tool installed. A container with a 2019 Git would mean nobody could run `git switch`. *(00:39:02)*

## 11. Know which machine you are typing on

*00:45:01–00:46:44*

- **Q:** You quit R with `q()` in `docker run --rm -it rocker/r-ver:4.3.2`. How do you confirm you're back on your own computer before running the next command?
    - **A:** Look at the prompt. Your laptop's usual prompt, such as `dan@Heartsbane ...`, returns once you've left the container. When working with containers or remote systems, the prompt is often your only visual cue. *(00:45:04)*

- **Q:** You connect to a remote machine and get only a blinking cursor. How can you check you are on the machine you think you are?
    - **A:** Check the hostname in the prompt, and run `whoami`, which reports the username on that computer. Both tell you whose machine your commands are running on. *(00:46:08)*

## 12. Running RStudio in a container and mapping ports ([28.1.3 Mapping ports to containers with web apps](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#mapping-ports-to-containers-with-web-apps))

*00:54:10–00:58:59*

- **Q:** You want to use RStudio Server from `rocker/rstudio:4.4.2` in your browser at `localhost:8787`. What `docker run` command do you use?
    - **A:** Run `docker run --rm -p 8787:8787 rocker/rstudio:4.4.2`, then open `localhost:8787` in your browser. In `-p host:container`, the left number is the port on your computer and the right is the port inside the container, where RStudio listens on 8787. *(00:57:05)*

- **Q:** You already have one RStudio container on `localhost:8787` and want to run a second at the same time. How do you change the `-p` flag?
    - **A:** Keep the container side at 8787 and map it to a different port on your computer, for example `-p 8788:8787`, then browse to that port. Several things can run at once as long as each uses a different host port. *(00:56:38)*

- **Q:** You open `localhost:8787` and RStudio asks you to sign in, but you never set a password. Where do you find the login details?
    - **A:** The username is `rstudio`, and the password is printed in the container's start-up output, as `The password is set to ...`. *(00:58:29)*

- **Q:** Your laptop has slowed to a crawl after an afternoon of starting containers without `--rm`. What is the likely cause, and how do you prevent it?
    - **A:** Each container uses RAM, so you probably have several machines still running. Add `--rm` so each container shuts down and is cleaned up when you exit it. *(00:55:24)*

- **Q:** You run RStudio from `rocker/rstudio:4.4.2` while your desktop RStudio uses your laptop's R 4.6.2. Which R version does the browser RStudio show?
    - **A:** It shows the R installed in the container, 4.4.2, not your laptop's 4.6.2. The container is effectively a separate machine with its own R. *(00:58:51)*

## 13. Passing environment variables into a container ([27.2 What is a container?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#what-is-a-container))

*00:59:20–01:02:53*

- **Q:** The generated RStudio password is too hard to remember. How do you modify `docker run --rm -p 8787:8787 rocker/rstudio:4.4.2` so you can log in with `apassword`?
    - **A:** Add an environment variable with `-e`: `docker run --rm -p 8787:8787 -e PASSWORD="apassword" rocker/rstudio:4.4.2`. The image reads `PASSWORD`, sees that you set one, and uses it for the login. *(01:00:05)*

- **Q:** You try `-e PASSWORD=...` with a different image, and nothing changes. What is the likely reason?
    - **A:** Not every container uses the same variables; it depends on how whoever built the image set it up. `PASSWORD` works for `rocker/rstudio` because that image reads it. Check the image's documentation for the variables it supports. *(00:59:45)*

- **Q:** You typed your RStudio container password in plain view on your own laptop. Can someone else use it to reach your RStudio?
    - **A:** Not in this setup. Port 8787 is only available on your own machine, so someone would first need access to your physical computer. *(01:00:28)*

- **Q:** You build a dashboard and want a user to run it without installing your language, packages or `renv` snapshot. What do you give them, and what must they have?
    - **A:** Give them a container with the dashboard and everything it needs installed. They only need Docker: they `docker run` it with the right flags and visit the port in their browser. *(01:02:20)*

## 14. Starting from a base image and working inside it ([28.1.4 Changing the containers default command](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#changing-the-containers-default-command))

*01:03:00–01:08:19*

- **Q:** `rocker/r-ver:4.6.2` opens R by default, but you want a shell inside it to try install commands. What do you run, and how do you know it worked?
    - **A:** Run `docker run --rm -it rocker/r-ver:4.6.2 bash`. Adding `bash` replaces the default command, and the prompt changes to the container's, such as `root@95765251a970:/#`. You can still type `R` there to start R. *(01:04:53)*

- **Q:** Inside `docker run --rm -it rocker/r-ver:4.6.2 bash` you run `install.packages("cowsay")` in R, and `cowsay::say('hello')` works. You `exit`, run the same command again and type `library(cowsay)`. What happens, and why?
    - **A:** It fails with `there is no package called 'cowsay'`. A container has no saved state: each time it starts, it resets to how its image was built, so anything installed by hand is gone. *(01:07:10)*

- **Q:** You need a custom R machine. Why choose `rocker/r-ver:4.6.2` as the starting point instead of a bare Linux image?
    - **A:** The image builders have already installed R and the system pieces R needs, the equivalent of the compiler tools you installed on your laptop. Starting from it skips those steps. *(01:04:00)*

- **Q:** You are designing a container and are not sure which install commands will work. How do you proceed?
    - **A:** Start a shell in the base image, go through the install steps interactively, and once they work, write them down as the instructions for building the machine. *(01:05:48)*

## 15. Running R from the command line with `Rscript -e`

*01:08:19–01:10:18*

- **Q:** At a container's Bash prompt you want to install `cowsay` without opening R, in a form you can later put in a build file. What do you type?
    - **A:** `Rscript -e "install.packages('cowsay')"`. `Rscript` runs R from the shell, and `-e` means "here is an R expression". Build steps have to be terminal commands, so this is the form you need. *(01:09:27)*

- **Q:** You write `Rscript -e "install.packages("cowsay")"` and it breaks. What do you fix?
    - **A:** Fix the quoting: the inner quotes must differ from the outer ones. Use double quotes outside and single quotes inside: `Rscript -e "install.packages('cowsay')"`. *(01:09:41)*

- **Q:** You install `cowsay` with `Rscript -e` at a container's prompt, and `library(cowsay)` now works there. You exit and start the container again. Will `cowsay` still be there?
    - **A:** No. Exiting and re-entering loses it again, because installs made in a running container are not saved. The working command has to be recorded somewhere the image is built from. *(01:10:01)*

## 16. The `Dockerfile`: `FROM`, `RUN`, `CMD` ([29.2 `Dockerfile` command summary](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#dockerfile-command-summary))

*01:10:18–01:15:01*

- **Q:** You want an image based on R 4.6.2 with `cowsay` installed, which by default prints a cow saying "Hello from my first image!". Write the three-line `Dockerfile`.
    - **A:** `FROM rocker/r-ver:4.6.2`, then `RUN Rscript -e "install.packages('cowsay')"`, then `CMD ["Rscript", "-e", "cowsay::say('Hello from my first image!')"]`. `FROM` picks the starting machine, `RUN` runs the shell command during the build, and `CMD` sets the default command. *(01:13:52)*

- **Q:** You are writing a `Dockerfile` from scratch. What do you name the file, and what goes on its first line?
    - **A:** Name it `Dockerfile` with a capital D, which is the convention Docker looks for. Make the first line `FROM` (in caps), followed by the base image. Only metadata such as a maintainer or name comes before it. *(01:11:10)*

- **Q:** Your image ends with `CMD ["Rscript", "-e", "cowsay::say('Hello from my first image!')"]`, but you start it with `bash` after the image name. Which runs, the cow or a shell?
    - **A:** A shell. `CMD` is only the default command, and giving another command such as `bash` overrides it. *(01:13:52)*

- **Q:** Your project is in Python, not R. What goes in the middle section of its `Dockerfile` so the container has your packages?
    - **A:** `RUN` commands that install `uv`, a `COPY` command that copies in your lock files, and a `RUN uv sync`. The packages are then installed in the image, so the machine has your compute environment ready. *(01:14:15)*

## 17. Building and running your own image ([29.1.2 Build your first image](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#build-your-first-image))

*01:15:01–01:18:44*

- **Q:** Your `Dockerfile` is in the root of your project, and you are in that folder. What do you run to build an image named `hello-cowsay`?
    - **A:** `docker build --tag hello-cowsay .`. `--tag` names the image, and the `.` tells Docker to look in the current directory, where it expects a file named exactly `Dockerfile`. *(01:15:38)*

- **Q:** You write build instructions in your project README. Which directory should every command assume, and why?
    - **A:** The root of the repository. Then `docker build --tag ... .` and the other commands can be copy-pasted without anyone changing directories in the middle. You could give the full path to a `Dockerfile` instead, but the root convention is what you'll see everywhere. *(01:16:11)*

- **Q:** You just ran `docker build --tag hello-cowsay .`. How do you confirm the image exists, and what do you run to see its default behaviour?
    - **A:** Run `docker images`, which lists every image on your machine, including `hello-cowsay:latest`. Then run `docker run --rm -it hello-cowsay`, which runs the `CMD` and prints the cow saying "Hello from my first image!". *(01:17:01)*

- **Q:** Your code works on your laptop but not in your container. How do you get inside the `hello-cowsay` image to investigate, and what should `library(cowsay)` do there?
    - **A:** Run `docker run --rm -it hello-cowsay bash` to get a shell inside the container, then start `R`. `library(cowsay)` loads, because the `RUN` line installed it when the image was built. *(01:17:30)*

- **Q:** Put these steps in order to get a package permanently into a container: build the image, write the working command as a `RUN` line, test the install interactively in the base image, run the new image.
    - **A:** Test the install interactively in the base image, write the working command as a `RUN` line, build with `docker build`, then run the new image. Only after the build does every container from the image start with the package installed. *(01:17:52)*

## 18. Pinning versions, and what comes next

*01:18:44–01:20:39*

- **Q:** You restart a project container that installs its tools without pinned versions, and today nothing works, though it did yesterday. What most likely happened, and how do you prevent it?
    - **A:** Something updated upstream the day before, and your container picked up the new version. Pin explicit versions in the `Dockerfile`, so tools change only when you edit that line. Otherwise you can spend hours fixing an update instead of doing the actual work. *(01:19:55)*

- **Q:** Your project uses Quarto, and you want a year from now to get exactly the same Quarto version. What do you do in your `Dockerfile`?
    - **A:** Install a specific Quarto version, even an older one such as 1.10, in its install command. As long as you don't change that line, rebuilding gives the same version. *(01:19:25)*

- **Q:** Which line of your project `Dockerfile` keeps the R version stable, and what goes after it to keep the packages stable?
    - **A:** The `FROM` line pins the R version, for example `FROM rocker/r-ver:4.6.2`. After it, a section holds your `renv` or `uv` setup, which installs the locked package versions. *(01:19:02)*

---

- prompt: prompt-recall-3-apply.md @ 65eb21c
- prompt-hash: 49276171f719
- model: claude-opus-5-5 (requested: opus)
- backend: claude
- inputs: transcript-plaud.md, history.txt, terminal.txt, materials.md, notes-class-main--claude-opus-5-5.md
- generated: 2026-11-23
- notes-input: notes-class-main--claude-opus-5-5.md @ 1c708a29f65f, links and section references removed, diagrams removed
