# Git pull requests and an introduction to Docker containers: review questions, tier 5 — Evaluate

Date: 2026-11-19

Instructor: Daniel Chen

*Tier 5 of 5: Evaluate. Decide and justify your verdict before you read the answer; the criteria are the ones given in class.*

## 1. Project advice: keep the analysis simple

*00:01:41–00:05:57*

- **Q:** At the first group meeting, a teammate argues that the project should use a neural net instead of a straight-line model, so the report stands out. Judge the proposal.
  **A:** Reject it. This is a workflows course, not a model-fitting course, so the report is not the point and model performance does not affect your grade. The instructor warned that a complicated model means "a very bad time in about two weeks," when the workflow work arrives. If the straight line fits, fit the straight line model. *(00:02:16)*

- **Q:** To keep the project simple, a group decides to predict a numeric outcome with logistic regression, which they already know well. Is that an acceptable kind of simple?
  **A:** No. Simple models are not penalised, but they must be technically correct. The instructor said that fitting logistic regression to predict a numeric outcome is "just wrong." Simplicity never excuses an incorrect technique. *(00:05:24)*

- **Q:** A student wants the group project to double as a polished portfolio piece, with a more elaborate analysis. Recommend whether to do that inside the assignment.
  **A:** Don't do it inside this assignment. If you really want a portfolio piece, build it separately and in parallel. A lot happens in this course, and you don't want a complicated report on top of it. *(00:03:27)*

## 2. Git review: working on a branch

*00:06:16–00:09:50*

- **Q:** In the `2026-11-19-docker` repository, a teammate edits `README.md` and runs `git add` and `git commit` straight away, without checking the branch or pulling `main` first. Critique this habit for a group project.
  **A:** It falls short of the standard set in class. In a branch workflow you should look at which branch you are on right before `git add`, and definitely before `git commit`. When collaborating actively, you should also pull `main` first, so you are not changing something out of date. The instructor only escaped committing on `main` because nothing was committed yet, which let `git switch -c today` carry the edit onto a new branch. *(00:08:08)*

## 3. GitHub issues as a project board

*00:09:50–00:16:17*

- **Q:** A group creates the three issues the lab requires, then resolves all three in a single pull request. A teammate objects that every issue needs its own branch and pull request. Who is right?
  **A:** The group is right. One issue, one branch, one pull request is only one extreme, and that is not always how work divides. The instructor said explicitly that it is okay for one pull request to deal with all three issues. The point is experience with the project board system. *(00:14:23)*

- **Q:** A group plans to keep its meeting notes and task assignments in a shared Google Doc instead of in GitHub issues. Assess the plan.
  **A:** Issues are the better choice. They record who is responsible for what, and meeting-notes issues can spawn separate action-item issues. Issues and pull requests also cross-reference each other with two-way `#` links. The instructor presented this as a very good way to track what is happening with your team "and you're not relying on a Google Doc of notes." *(00:15:48)*

## 4. Pull request descriptions, checkboxes and closing keywords

*00:16:17–00:22:18*

- **Q:** A team makes a major design decision halfway through a pull request's comment thread but leaves the opening description unchanged, reasoning that the decision is recorded in the conversation. Judge this.
  **A:** Not good enough. The first comment should be kept up to date. People reading the pull request want to know "why does this thing exist?" from the top, and won't read the whole conversation. Comments are editable precisely because pull requests evolve, and project owners can usually edit them. *(00:16:56)*

- **Q:** A teammate puts `fixes #2` only in a commit message, never in the pull request description. Is that the better place for it?
  **A:** It works, but it is the weaker choice. The instructor said you could put the keyword in a commit message, "but it's harder to see." Writing it in the pull request message makes the link visible to the team, and merging still closes the issue automatically. *(00:19:55)*

- **Q:** Before submitting, a group plans to close every open issue, including stretch-goal ideas, because they believe open issues will cost them marks. Is that necessary?
  **A:** No. The course does not grade on whether all your issues are closed by the end. Creating issues for stretch goals and longer-term ideas is encouraged, and the instructor said it is "totally fine" to leave them open. *(00:21:50)*

## 5. Cleaning up after a merge

*00:22:18–00:25:19*

- **Q:** After pull request #3 merges, a teammate insists that the `today` branch must be deleted on GitHub and locally, or the workflow is wrong. Judge the claim.
  **A:** The claim is too strong. In this course, deleting branches is optional, and you may keep them as a record. The merge history stays either way: `git fetch --prune` and `git branch -d today` only remove the shortcut names. Some people keep the branch because `git switch today` is easier than switching to `3c6d82a`. *(00:23:16)*

## 6. Why data science workflows need stable environments

*00:25:29–00:30:13*

- **Q:** To avoid "missing package" errors, a teammate proposes installing every library anyone might want into the project environment. Critique the proposal.
  **A:** Reject it. The package list should be the bare minimum the project needs. Installing everything wastes disk space. Packages also update on different cycles, so a large environment can reach a point where it can no longer all be installed together. *(00:28:04)*

## 7. What a container is ([27.2 What is a container?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#what-is-a-container))

*00:30:13–00:34:28*

- **Q:** A collaborator doesn't use `uv` and doesn't want to install it, because it might disrupt their setup. You plan to send them only your `uv.lock` file. Is that enough?
  **A:** No. A lock file still requires them to install `uv` and to have a similarly set-up computer. The instructor's easier route is a container: a virtual computer you build and hand over, so everyone works on the same computer even on different physical machines. *(00:31:17)*

- **Q:** The admins of a shared remote machine won't let you install Python on it directly. You propose running your work in a container there instead, accepting the extra layer. Defend or reject the proposal.
  **A:** Defend it. There is a performance hit from the extra layer, but a container gives you a sandbox where you can install what you need without touching the machine itself. If you mess it up, you restart it and get a fresh sandbox. *(00:32:34)*

## 8. Containers versus virtual machines ([27.3 Contrasting containers with virtual machines](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#contrasting-containers-with-virtual-machines))

*00:34:31–00:36:40*

- **Q:** To share the project's computing environment, a teammate proposes distributing a full Windows virtual machine instead of a container. Recommend one.
  **A:** Recommend the container. A Windows virtual machine can take 50–80 GB, and it carries a full operating system and graphical interface. The containers used in class are a couple of gigabytes or less, yet still run the full computational stack. They are lighter on disk, memory and compute. *(00:36:16)*

## 9. Pulling and running a container ([28.1.1 Launch and run containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#launch-and-run-containers))

*00:36:40–00:45:01*

- **Q:** For a multi-year clinical trials analysis that must be submitted to a regulator, a team plans to submit only its code and an `renv.lock` file. Assess whether that meets the standard described in class.
  **A:** It does not. Regulators want to reproduce the work with the full compute environment, and R itself updates every six months. Lock files track only the packages, not the version of R or the system tools. Handing over the container that ran the analysis, such as one built on `rocker/r-ver:4.3.2`, pins those as well. *(00:38:46)*

## 10. Know which machine you are typing on

*00:45:01–00:46:44*

- **Q:** A teammate has a container shell and a laptop terminal open side by side, and runs a destructive cleanup command without first checking the prompt. Critique the habit.
  **A:** It is risky. With containers and remote machines, the prompt is often your only visual cue to which machine you are typing on, so check it every time. Commands such as `whoami` exist to confirm you are on the machine you think you are. *(00:45:04)*

## 11. Running RStudio in a container and mapping ports ([28.1.3 Mapping ports to containers with web apps](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#mapping-ports-to-containers-with-web-apps))

*00:54:10–00:58:59*

- **Q:** While practising, a student drops `--rm` from `docker run -p 8787:8787 rocker/rstudio:4.4.2` and starts several containers through the afternoon. Judge the practice.
  **A:** Avoid it. Without `--rm`, containers aren't removed when they stop, and leaving several running means each one keeps taking up RAM. The instructor warned that you end up asking why your computer isn't working, because you turned on five computers. *(00:55:17)*

- **Q:** A student wants two RStudio containers at once and plans to start both with `-p 8787:8787`. Is that plan sound?
  **A:** No. Both containers can listen on 8787 inside, but each needs a different port on your machine. Change the left-hand (host) number of `-p` for the second container. Running things on different host ports is what lets several run at the same time. *(00:56:38)*

## 12. Passing environment variables into a container ([27.2 What is a container?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#what-is-a-container))

*00:59:20–01:02:53*

- **Q:** The instructor ran `docker run --rm -p 8787:8787 -e PASSWORD="apassword" rocker/rstudio:4.4.2` with the password in plain view. Was that acceptable in that setting?
  **A:** Yes, by the criterion given in class. Port 8787 was only reachable on his own machine, so anyone without access to his laptop could not reach the container at all. The visible password therefore didn't expose anything. *(01:00:16)*

- **Q:** For a future dashboard, a team weighs two options: users follow `renv` setup instructions, or users `docker run` a container with the dashboard already installed. Recommend one for end users.
  **A:** The container. The installation is already done inside it, so users skip the whole process of installing `renv` and restoring the snapshot. As long as they have Docker, `docker run` with some flags starts the application. You've given them a computer you built from scratch. *(01:02:20)*

## 13. Starting from a base image and working inside it ([29.1.1 Workflow for building a Dockerfile](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#workflow-for-building-a-dockerfile))

*01:03:00–01:08:19*

- **Q:** A project README tells users to start `rocker/r-ver:4.6.2` and run `install.packages()` for every package each time before running the analysis. Assess this approach.
  **A:** It is poor. A container has no saved state: packages installed by hand disappear when it restarts, so users repeat the installs every time. The instructor called that extremely painful, for example a 15-minute tidyverse install for a 30-second analysis. Those steps belong in a `Dockerfile`. *(01:08:19)*

- **Q:** A student wants to learn Linux by running risky commands, but is afraid of breaking their laptop. Is `docker run --rm -it rocker/r-ver:4.6.2 bash` a reasonable place to try them?
  **A:** Yes. Restarting a container gives a clean machine, as if you had never run the command. That makes containers a safe place to try new packages or muck around with the command line. *(01:07:25)*

## 14. The `Dockerfile`: `FROM`, `RUN`, `CMD` ([29.1.2 Build your first image](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#build-your-first-image))

*01:10:18–01:15:01*

- **Q:** A reviewer rejects a `Dockerfile` that starts `FROM rocker/r-ver:4.6.2`. They argue it should start from a bare-minimum Linux image, with R installed by hand, to keep the image small. Judge the rejection.
  **A:** The rejection is too strict. A bare-minimum start is possible and a good learning exercise, but the instructor said disk space is relatively cheap, so starting from a beefier machine is acceptable. `rocker/r-ver:4.6.2` already has R and the pieces R needs, which skips steps. *(01:12:02)*

## 15. Building and running your own image ([29.4.3 3. How do I build an image locally on my laptop?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#how-do-i-build-an-image-locally-on-my-laptop))

*01:15:01–01:18:44*

- **Q:** A milestone README tells users to `cd` into a subfolder before running `docker build --tag hello-cowsay .`, then `cd` back for the next step. Does that meet the standard set for milestone instructions?
  **A:** No. Instructions should assume every command runs from the root of the repository. That way they can be copy-pasted without changing directories in the middle. `docker build --tag hello-cowsay .` is meant to run from the root, where the `Dockerfile` lives. *(01:16:11)*

## 16. Pinning versions, and what comes next

*01:18:44–01:20:39*

- **Q:** A project `Dockerfile` installs Quarto and the analysis packages without specifying any versions, "so we always get the latest." Would you approve it in a pull request?
  **A:** No. Things that update without you knowing can break everything. The instructor restarted an unpinned container in another class and nothing worked, because something had updated the day before. Hard-pin the versions so they change only when you edit that line. *(01:19:55)*

---

- prompt: prompt-recall-5-evaluate.md @ 8bcc190
- prompt-hash: 91dbb814d755
- model: claude-opus-5-5 (requested: opus)
- backend: claude
- inputs: transcript-plaud.md, history.txt, terminal.txt, materials.md, notes-class-main--claude-opus-5-5.md
- generated: 2026-11-20
- notes-input: notes-class-main--claude-opus-5-5.md @ 1c708a29f65f, links and section references removed
