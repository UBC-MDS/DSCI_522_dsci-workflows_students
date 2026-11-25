# Git issues and pull requests, and an introduction to Docker containers: review questions, tier 5 — Evaluate

Date: 2026-11-19

Instructor: Daniel Chen

*Tier 5 of 5: Evaluate. Decide and justify your verdict before you read the answer; the criteria are the ones given in class.*

## 1. Project advice: keep the analysis simple

*00:01:41–00:05:57*

- **Q:** A teammate says the group project is their "time to shine" and proposes a neural net when a straight-line model fits the question. Judge the proposal.
    - **A:** Reject it and fit the straight-line model. This is a workflows course, not a model-fitting course, and the instructor warned "you're going to have a very bad time in about two weeks if you do that." The report is not the point of the class, and the workflow work still has to get done. *(00:02:16)*

- **Q:** A group's model reaches only 60% accuracy. The model itself is logistic regression, and it predicts a numeric outcome. Assess whether the submission meets the course's standard.
    - **A:** It does not, but the accuracy is not the reason. Model results do not matter, but the techniques must be correct data science. Using logistic regression to predict a numeric outcome is "just wrong." *(00:05:24)*

- **Q:** A student wants to turn the group project into a polished portfolio piece with a more elaborate report. Recommend whether to do that in this assignment.
    - **A:** Don't do it in this assignment. If you want a portfolio project, build it in parallel. A lot is happening in this class, and you don't want to be dealing with a complicated report at the same time. *(00:03:27)*

## 2. Git review: working on a branch

*00:06:16–00:09:50*

- **Q:** In the `2026-11-19-docker` repository, the instructor edited `README.md` while still on `main` and had not committed. A student says the edit is now stuck on `main`. Assess running `git switch -c today` at that point.
    - **A:** It is fine. Nothing had been committed yet, so the uncommitted edit moved to the new `today` branch, and `git status` then showed `On branch today` with `README.md` modified. Only commits already made on `main` need the textbook's cheat sheet of commands to move them. *(00:08:57)*

- **Q:** A teammate in an active group project starts editing and committing straight away, without checking which branch they are on or pulling `main`. Critique this habit.
    - **A:** It is risky in a branch workflow with several people and several branches. Look at your branch right before `git add`, and definitely before `git commit`, so commits don't land on the wrong branch. Pull `main` first, so you aren't making changes to something that is out of date. *(00:08:27)*

## 3. GitHub issues as a project board

*00:09:50–00:16:17*

- **Q:** The lab asks for three issues, and a group resolves all three with a single pull request instead of one branch and one pull request per issue. Is that acceptable?
    - **A:** Yes. "One issue, one branch, one pull request" is only one extreme and isn't always the case. The class said explicitly that one pull request may deal with all three issues. The aim is experience with the project-board system. *(00:14:23)*

- **Q:** A group keeps its meeting notes and the to-do list it assigns from them in a shared Google Doc instead of GitHub issues. Recommend whether to switch.
    - **A:** Switch to issues. They record who is responsible for what, and action items can become separate issues spawned from the meeting-notes issue. Because `#` references link both ways automatically, everything stays connected to the pull requests that do the work, "and you're not relying on a Google Doc of notes." *(00:15:48)*

## 4. Pull request descriptions, checkboxes and closing keywords

*00:16:17–00:22:18*

- **Q:** Halfway through a pull request's discussion, the team makes a major decision and records it only in a later comment. Judge whether that is enough.
    - **A:** It is not enough. Update the first comment so it describes the decision. Readers want to know "why does this thing exist?" from the top, and "no one's really going to care about the conversation." The first comment is editable precisely because a pull request evolves. *(00:16:56)*

- **Q:** Pull request #3 in `2026-11-19-docker` resolves issues #1 and #2. A teammate plans to merge it and then close both issues by hand, instead of writing `closes #1 fixes #2` in the description. Which approach is better?
    - **A:** Write the keywords in the pull request description. Merging the pull request then closes the issues automatically, so you don't have to go back and close each one, and the issues tab shrinks as work merges. A commit message also works, but keywords there are harder to see. *(00:21:02)*

- **Q:** A group decides it must close every issue, including stretch-goal ideas, before submitting the milestone. Assess that plan.
    - **A:** It is unnecessary. The course does not grade on whether all issues are closed by the end of class. Issues for longer-term ideas and stretch goals are fine to leave open, and the point is to practise with the system. *(00:21:50)*

## 5. Cleaning up after a merge

*00:22:18–00:25:19*

- **Q:** After pull request #3 is merged, a teammate wants to keep the `today` branch on GitHub as a record. Another insists that branches must always be deleted. Decide between them.
    - **A:** Both are acceptable in this course. You are not required to delete branches, and keeping them as a record is allowed. Teams and companies handle Git differently, and the class's way is only one way. *(00:23:16)*

- **Q:** A student refuses to run `git fetch --prune` and `git branch -d today` because they fear it will erase the merged work from history. Is the fear justified?
    - **A:** No. The `git log --oneline --graph --all` output still shows commit `3c6d82a` and the merge commit. You lose only the shortcut name, so you would switch by hash instead of `git switch today`. Cleaning up is worth it when too many references make the Git state hard to read. *(00:24:30)*

## 6. Why data science workflows need stable environments ([27.1 Documenting and loading dependencies](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#documenting-and-loading-dependencies))

*00:25:29–00:30:13*

- **Q:** To avoid "missing package" errors, a teammate proposes installing every data science package they might ever need into the project environment. Critique the proposal.
    - **A:** Reject it and keep the package list to the bare minimum. Installing packages you don't use wastes disk space. Packages also update on different cycles, so a big environment can end up impossible to install all at once. *(00:28:04)*

- **Q:** A teammate defends their code with "it works on my machine," even though a groupmate on a Windows ARM laptop can't run it. Is that defence acceptable?
    - **A:** No. The goal of the class is a compute environment you can share, so that others can run the same analysis. "It works on my machine" doesn't work when a teammate can't run your code, and teammates may have a different operating system or even a different chip architecture. *(00:29:43)*

## 7. What a container is ([27.2 What is a container?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#what-is-a-container))

*00:30:13–00:34:28*

- **Q:** You send a collaborator your `uv.lock` file, but they don't use `uv` and don't want to install it. Assess whether the lock file alone is enough to share your environment.
    - **A:** It is not enough. A lock file only lets someone with the right tools install your packages. Installing `uv` might mess up other things on their machine, and their computer may be set up differently. A container gives everyone the same virtual computer, so all of you work on the same machine despite different hardware. *(00:31:17)*

- **Q:** A student wants to learn Linux by experimenting with system commands, but is worried about breaking their laptop. Recommend where they should do it.
    - **A:** Do it in a container. A container is a sandbox: if you mess it up, you restart it and get a fresh one. The cost is a performance hit from the extra layer, which is acceptable for experimenting. *(00:33:13)*

## 8. Containers versus virtual machines ([27.3 Contrasting containers with virtual machines](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#contrasting-containers-with-virtual-machines))

*00:34:31–00:36:40*

- **Q:** A group plans to share its analysis environment as a full Windows virtual machine instead of a container. Judge the plan.
    - **A:** A container is the better choice. A Windows VM can take 50–80 GB because it carries the full operating system and graphical interface. The containers used in class are a couple of gigabytes or less and still run a full computational stack, so they use less disk, memory and compute. VMs still have uses, such as testing the MDS install on Windows. *(00:36:16)*

## 9. Pulling and running a container: R 4.3.2 beside local R ([28.1.1 Launch and run containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#launch-and-run-containers))

*00:36:40–00:45:01*

- **Q:** A pharmaceutical team running a multi-year clinical trial analysis plans to rely on `renv.lock` alone for its regulatory submission. Assess the plan.
    - **A:** It is insufficient. R updates every six months, and the regulator needs to reproduce the full compute environment, not only the package versions. Lock files track packages but not the tool itself, such as the version of R. Handing over the container that ran the analysis pins R and the other system tools too. *(00:38:46)*

## 10. Know which machine you are typing on

*00:45:01–00:46:44*

- **Q:** After working in a container and on a remote machine, a student is faced with a bare blinking cursor and runs a destructive command without checking anything. Critique this.
    - **A:** It is dangerous. With containers and remote systems, your prompt is sometimes the only cue to where you are typing. Check the prompt, or run `whoami` to see the username, before running anything, so the command doesn't run on the wrong machine. *(00:46:08)*

## 11. Running RStudio in a container and mapping ports ([28.1.3 Mapping ports to containers with web apps](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#mapping-ports-to-containers-with-web-apps))

*00:54:10–00:58:59*

- **Q:** While practising, a student leaves `--rm` off their `docker run` commands and starts several containers through the day. Judge this practice.
    - **A:** It is a mistake. Each running container takes up RAM, so you end up with "five computers" running and a laptop that stops working well. `--rm` shuts down and deletes the machine when you exit. *(00:55:24)*

- **Q:** A student wants two RStudio containers at once and gives both `-p 8787:8787`. Assess the plan.
    - **A:** It won't work as written. Inside each container RStudio runs on 8787, but each must be mapped to a different port on your machine, with the host port on the left of the `:`. Multiple things can run at the same time only because they use different host ports. *(00:56:38)*

## 12. Passing environment variables into a container ([27.2 What is a container?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#what-is-a-container))

*00:59:20–01:02:53*

- **Q:** The instructor ran `docker run --rm -p 8787:8787 -e PASSWORD="apassword" rocker/rstudio:4.4.2` with the password visible on screen. Was that acceptable?
    - **A:** Yes, in that context. The container's port 8787 is only reachable from the instructor's physical machine, so someone who can't log into that machine can't reach the RStudio login. *(01:00:16)*

- **Q:** For a dashboard project, a group debates two options: shipping install instructions (install `renv`, restore the snapshot, and so on) or shipping a container that users start with `docker run`. Recommend one.
    - **A:** Ship the container. You have done all the installation already, so the end user only needs Docker and a `docker run` command with some flags, then visits the port. In effect you give them a computer you built from scratch, although the instructor acknowledged that installing Docker is itself a pretty big lift. *(01:02:20)*

## 13. Starting from a base image and working inside it ([28.1.4 Changing the containers default command](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#changing-the-containers-default-command))

*01:03:00–01:08:19*

- **Q:** A group's README tells users to start `rocker/r-ver:4.6.2` and install the needed packages by hand each time before running the analysis. Judge the approach.
    - **A:** It is a poor approach. A container has no saved state: `cowsay`, installed by hand, was gone after a restart. Making users repeat installs every time is painful, for example a 15-minute tidyverse install to run a 30-second analysis. The steps belong in the image's build instructions. *(01:08:19)*

- **Q:** A student writes a whole `Dockerfile` from memory without testing any command first. Another opens `docker run --rm -it rocker/r-ver:4.6.2 bash`, tries each install, and writes it down only once it works. Which workflow is better?
    - **A:** The second is better. Going through the steps interactively first, then documenting those that work, gives you instructions for building the machine from scratch that you know succeed. The `bash` at the end of the command gives a shell instead of the default R prompt, so you can do exactly this. *(01:05:48)*

## 14. The `Dockerfile`: `FROM`, `RUN`, `CMD` ([29.1 Building container images from `Dockerfile`’s](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#building-container-images-from-dockerfiles))

*01:10:18–01:15:01*

- **Q:** One teammate wants the `Dockerfile` to start `FROM rocker/r-ver:4.6.2`. Another insists on a bare-minimum Linux base with every tool installed by hand, for performance. Decide.
    - **A:** `rocker/r-ver:4.6.2` is a reasonable choice. It already has R and the system pieces R needs, which saves steps. Disk space is relatively cheap, so a beefier base image is acceptable. Building from bare Linux is possible and teaches you a lot, but the instructor suggested it as a learning project for a break, not as a project requirement. *(01:12:15)*

## 15. Building and running your own image ([29.1.2 Build your first image](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#build-your-first-image))

*01:15:01–01:18:44*

- **Q:** A group's milestone instructions say "`cd docker/` and then run `docker build --tag hello-cowsay .`", with other commands run from other folders. Critique the instructions.
    - **A:** They fall short of the class's convention. Commands are assumed to run from the root of the repository, which is why `docker build --tag hello-cowsay .` uses `.` to mean "the `Dockerfile` right here". Instructions should be copy-pasteable without changing directories partway through. *(01:16:29)*

## 16. Pinning versions, and what comes next ([29 Customizing and building containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html))

*01:18:44–01:20:39*

- **Q:** A pull request adds a Quarto install to the project `Dockerfile` without specifying a version, "so we always get the latest." Would you approve it?
    - **A:** No. Ask for an explicit version. The instructor restarted a container without hard-pinned versions, something had updated the day before, and nothing worked, so hours went into fixing the update instead of the real work. With a pinned install line, you stay on the same versions a year from now and change them only when you decide to. *(01:19:55)*

---

- prompt: prompt-recall-5-evaluate.md @ 65eb21c
- prompt-hash: 6b82591e2f8e
- model: claude-opus-5-5 (requested: opus)
- backend: claude
- inputs: transcript-plaud.md, history.txt, terminal.txt, materials.md, notes-class-main--claude-opus-5-5.md
- generated: 2026-11-23
- notes-input: notes-class-main--claude-opus-5-5.md @ 1c708a29f65f, links and section references removed, diagrams removed
