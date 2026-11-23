# Git issues and pull requests, then an introduction to Docker containers: review questions, tier 2 — Understand

Date: 2026-11-19

Instructor: Daniel Chen

*Tier 2 of 5: Understand. Explain each answer in your own words before you read it; tier 1 (Remember) covers the facts, tiers 3 to 5 put them to use.*

## 1. Opening: pull the Docker images and start the branch exercise

*00:00:14–00:01:41*

- **Q:** Why were students asked to run the three `docker pull` commands from Slack at the very start of class, before anything else?
  **A:** The downloads take about ten minutes. Starting them at the beginning meant they would finish while the class was checking everything else, so nobody would wait for them later. *(00:00:18)*

- **Q:** Docker can fail in two ways at the start: with an error that it "can't find Docker", or by asking you to turn it on. What does each one mean?
  **A:** An error that Docker can't be found means Docker isn't installed, so you need to install the Docker application. If Docker is installed but Docker Desktop isn't running, the commands tell you to turn it on. That is why you open Docker Desktop before running them. *(00:00:33)*

- **Q:** Why did the warm-up exercise practise making a branch, opening a pull request and merging it, together with issues?
  **A:** Branches, pull requests and issues are part of how students will work on all their project-based courses from now on. The exercise gets them practising that workflow right away. *(00:00:57)*

## 2. Project advice: keep the analysis simple

*00:01:41–00:05:57*

- **Q:** Why did the instructor say to keep the group project's analysis simple, for example a straight-line model rather than a neural net?
  **A:** This is not a model-fitting course. The course title is about workflows, and there is almost no machine learning code in the lectures. The report is not the point of the class, and there is a lot more to do, so an ambitious model means "a very bad time in about two weeks." *(00:02:16)*

- **Q:** What is the difference between a model that is "simple" and one that is "incorrect", in terms of how the project is judged?
  **A:** A simple model is fine: the results don't matter, so 60% accuracy is acceptable, and linear or logistic regression won't be penalised. The techniques must still be technically correct data science. Fitting logistic regression to predict a numeric outcome, for example, is just wrong. *(00:03:08, 00:05:24)*

- **Q:** Why did the instructor advise against turning this group project into a portfolio piece?
  **A:** A lot is happening in this class, and you don't want to deal with a complicated report at the same time. If you really want a portfolio project, build it separately, in parallel. *(00:03:27)*

- **Q:** Explain why the project needs a machine learning analysis even though the lectures show almost no machine learning code.
  **A:** The class teaches the workflow around an analysis, not the modelling. You still need a machine learning project to start with, because that analysis is what you build the workflow on over three or four weeks. *(00:05:37, 00:05:43)*

## 3. Git review: working on a branch

*00:06:16–00:09:50*

- **Q:** The instructor edited `README.md` while still on `main`. Why could he fix this just by running `git switch -c today`?
  **A:** He had only edited the file and had not committed anything yet, so he could still create the new branch. After `git switch -c today`, `git status` showed "On branch today" with the same modified `README.md`, ready to commit there. *(00:08:57, 00:09:17)*

- **Q:** Why should you look at which branch you are on right before `git add`, and especially before `git commit`?
  **A:** From now on the course assumes a branch workflow, so commits belong on a branch, not on `main`. Once you have committed on `main`, you need extra commands to move the work around; the textbook has a cheat sheet for this. Checking first avoids the problem. *(00:07:44, 00:08:08)*

- **Q:** Why pull `main` before starting new work when you are actively collaborating?
  **A:** It keeps your copy up to date, so you aren't making changes to something that is out of date. With several people working on several branches, this is something you now have to pay attention to. *(00:08:27, 00:08:41)*

- **Q:** What did the `git diff` output on the `today` branch show before staging?
  **A:** It showed the uncommitted change to `README.md`: the lines starting with `+` were the new blank line and the added line "- today we will talk about containers". That is the change he then staged with `git add README.md` and committed. *(00:09:25)*

## 4. GitHub issues as a project board

*00:09:50–00:16:17*

- **Q:** What are GitHub issues for, beyond reporting bugs?
  **A:** They track what is happening in a project, as a simple project board, including who is responsible for what. MDS uses one internal repository's issues for meeting notes. Action items assigned to people are then spawned as separate issues from the notes issue. *(00:10:08, 00:10:28, 00:10:49)*

- **Q:** Why do issues and pull requests in the demo repository `2026-11-19-docker` share one numbering sequence, so that after issues #1 and #2 the pull request was #3?
  **A:** Because they share one counter, any issue or pull request can refer to any other item just by its number. *(00:12:07, 00:12:20)*

- **Q:** What does it mean that a `#` reference is "two-way", as when issue #2 said "meeting from #1"?
  **A:** Writing `#1` in issue #2 links to issue #1, and issue #1 automatically shows a reference back to #2. Everything links to everything else without extra work. The instructor called this one of the reasons GitHub, rather than just Git, became so popular as a project management system. *(00:13:34, 00:13:47)*

- **Q:** Why does the instructor sometimes ask a coding agent to file an issue for a passing idea instead of opening GitHub himself?
  **A:** Switching to a browser risks ending up on a site he doesn't need and losing track of his work. Asking the agent to file the issue records the idea without breaking his focus. *(00:13:06, 00:13:24)*

- **Q:** What is the difference between being an assignee and being a reviewer on a pull request?
  **A:** Assigning yourself claims the pull request as your responsibility. A reviewer is a teammate asked to look over your work. Some projects block changes until someone has actually reviewed them. In the demo, the instructor added Copilot as a reviewer. *(00:14:47, 00:15:14)*

- **Q:** Why is it acceptable for one pull request to deal with all three issues the lab asks for?
  **A:** One issue, one branch and one pull request is only one extreme, and it isn't always how work happens. The lab asks for issues so you gain experience with the project board system, not to force a one-to-one match. *(00:14:23)*

## 5. Pull request descriptions, checkboxes and closing keywords

*00:16:17–00:22:18*

- **Q:** Why did the instructor edit the first comment of the pull request instead of adding new comments as the work changed?
  **A:** People coming to an issue or pull request want to know what is happening and why it exists, and they won't read the whole conversation. The first comment should hold all the references and any big decisions. It is editable because the work evolves, and project owners can usually edit others' comments too. *(00:16:40, 00:16:56)*

- **Q:** How do Markdown checkboxes in a pull request description compare with marking the pull request as a draft?
  **A:** Both show teammates that the work isn't done yet. Checkboxes such as `- [ ] item 2` also let you track your own remaining to-dos as you fix things. They show what is still unchecked even if you never use the draft button. *(00:17:49, 00:18:21)*

- **Q:** How does writing `fixes #2` in pull request #3's description close issue #2?
  **A:** `fixes` (and `closes`) followed by an issue number is a special pattern that GitHub recognises. When that pull request is merged, the issues it says it fixes are closed automatically. This is a GitHub feature, not a feature of Git itself. *(00:18:33, 00:18:54, 00:19:30)*

- **Q:** Why write closing keywords in the pull request message rather than in a commit message?
  **A:** They also work in a commit message, but they are harder to see there. Putting them in the pull request message makes it visible which issues the work deals with. *(00:19:55)*

- **Q:** Why does auto-closing issues help with project management?
  **A:** As pull requests merge, the issues tab gets smaller, so you don't have to think about finished items again or click close on each one. The instructor works this way on the textbook: file an issue, do the work, write "fixes" in the pull request, then take the next item from the issues list. *(00:20:12, 00:20:28, 00:21:02)*

- **Q:** Why is it fine to leave stretch-goal issues open at the end of the course?
  **A:** Closing all your issues is not what the course grades. Issues are a place to keep longer-term ideas and things to explore, so creating them is good practice even if they stay open. *(00:21:50)*

## 6. Cleaning up after a merge

*00:22:18–00:25:19*

- **Q:** What is the difference between what `git fetch --prune` and `git branch -d today` each removed?
  **A:** `git fetch --prune` removed the local reference to the branch that had been deleted on GitHub, `origin/today`. `git branch -d today` then deleted the local `today` branch. Both only clean up references. *(00:24:30)*

- **Q:** After both cleanup commands, what did `git log --oneline --graph --all` still show, and what had been lost?
  **A:** Commit `3c6d82a` and the merge commit were still in the graph, so you could still tell a merge had happened. Only the branch labels were gone: the quick shortcut reference to that commit. *(00:24:30)*

- **Q:** Why do some people prefer not to delete merged branches?
  **A:** Deleting a branch loses the convenient reference to that point in history. With the branch kept, you can type `git switch today` instead of `git switch 3c6d82a`. *(00:24:05, 00:25:05)*

- **Q:** Why might you clean up branch references anyway?
  **A:** Leftover references can leave you in weird Git states where the graph has too many colours and labels to see what is happening. Cleaning up makes the history readable again. *(00:24:05)*

- **Q:** Why is deleting branches optional in this course?
  **A:** You may want to keep branches as a record. Teams and companies handle Git very differently, even within one company. The course shows one way, and others are modifications of it. *(00:23:16, 00:23:22)*

## 7. Why data science workflows need stable environments ([27.1 Documenting and loading dependencies](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#documenting-and-loading-dependencies))

*00:25:29–00:30:13*

- **Q:** How does working on a project differ from earlier MDS homework when it comes to packages?
  **A:** In homework, the instructors gave you the package file. In projects, each group chooses its own tools, such as R or Python, or Altair, Plotly or Matplotlib, so you must adapt the environment to your project. That is also how it works at a company. *(00:25:52, 00:27:06, 00:27:38)*

- **Q:** Why keep a project's package list to the bare minimum instead of installing everything?
  **A:** Installing packages you don't use wastes disk space. Packages also have different update cycles, so updating a big environment in one go can make things incompatible. You can end up unable to install everything. *(00:27:38, 00:28:04)*

- **Q:** Explain the two kinds of stability a long-running group project needs.
  **A:** You need your own environment to stay stable over days, weeks, months or even years. It also has to work for someone else, because "this works on my machine" doesn't help a teammate who can't run your code. *(00:28:20, 00:28:34, 00:29:39)*

- **Q:** Why is reproducing an environment on a teammate's computer harder than copying it to "just another Mac"?
  **A:** The teammate may be on Windows, and the CPU chips differ between machines, so software is installed differently. Even two Windows machines can differ, because Windows now runs on both ARM and Intel chips. *(00:28:53)*

- **Q:** Why does the course care about modular pipelines, not just a finished report?
  **A:** Other people may need different parts of your analysis, not only the report. The pipeline has to be built so those parts can be used separately. *(00:29:55)*

## 8. What a container is ([27.2 What is a container?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#what-is-a-container))

*00:30:13–00:34:28*

- **Q:** If you can hand a teammate a `uv` lock file, what problem is still left over?
  **A:** The lock file lets them install the Python packages, but their computer may be set up differently. They may not use `uv` at all, and installing it might mess up other things on their computer. *(00:30:40, 00:31:06, 00:31:17)*

- **Q:** Explain the idea of a container in the instructor's "here's my computer" terms.
  **A:** Instead of giving you his physical computer, he builds a virtual computer from scratch and gives you that. You do your work on that virtual computer instead of directly on your own. Everyone is effectively sharing the same computer while sitting at different physical machines. *(00:31:17, 00:31:49, 00:31:56)*

- **Q:** Why are containers useful when you prototype on a laptop but run the full analysis on a bigger machine?
  **A:** The bigger machine may be the one with access to all the data. A container makes the compute environment exactly the same on your machine and on that machine, and on any number of other machines. *(00:32:06, 00:32:15)*

- **Q:** What is the cost of a container, and why might it be worth paying on a remote machine?
  **A:** There is a performance hit, because a container adds an extra layer. However, you often can't install things directly on a shared remote machine, or the admins don't trust what you'd install. A container gives you a sandbox to play in instead. *(00:32:34)*

- **Q:** Why is a container a good place to learn by "mucking around" with an operating system?
  **A:** If you break the sandbox, you restart it and get a new one. Blowing up a container costs nothing, unlike blowing up your own computer. *(00:33:05, 00:33:13)*

- **Q:** How do containers relate to the "instances" you get from cloud providers?
  **A:** Containers are almost like instances. A provider such as Google usually gives you a container on one of its servers, not bare access to a machine. Pretty much all cloud compute runs on some version of containers. *(00:33:30)*

- **Q:** How does a container deal with two versions of software that can't be installed side by side?
  **A:** A container is a little machine with everything it needs installed inside it. Each version can live in its own container, separate from your computer. *(00:34:03)*

## 9. Containers versus virtual machines ([27.3 Contrasting containers with virtual machines](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#contrasting-containers-with-virtual-machines))

*00:34:31–00:36:40*

- **Q:** What is the main difference between a virtual machine and a container?
  **A:** A virtual machine is a full-blown operating system, such as all of Windows, with the graphical interface and all the buttons to click. A container is stripped down: it typically has no graphical interface and contains only the bare minimum you install. *(00:34:48, 00:35:00, 00:35:33)*

- **Q:** Why are containers more performant than virtual machines?
  **A:** A container has less in it and no visual parts, so it uses fewer resources. A Windows virtual machine can take 50–80 GB. Some containers used in class are under one or two gigabytes and still run a full computational stack, using less disk, memory and compute. *(00:35:33, 00:36:16, 00:36:32)*

- **Q:** How does the container's lack of a graphical interface explain why DSCI 521 pushed you to type commands in the terminal?
  **A:** In a container, and in many other places, the terminal may be the only interface you have. You can't double-click through folders, so you have to type commands such as `cd` to get around. *(00:35:00)*

- **Q:** Why does the instructor still use virtual machines?
  **A:** When testing the MDS installation instructions, he has to pretend to be on a Windows machine. That needs a whole different operating system, which is what a virtual machine provides. *(00:36:01)*

## 10. Pulling and running a container: R 4.3.2 beside local R ([28.1.1 Launch and run containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#launch-and-run-containers))

*00:36:40–00:45:01*

- **Q:** Explain what each part of the image name `rocker/r-ver:4.3.2` means.
  **A:** The name looks like a GitHub username and repository because it works similarly. `rocker` is the organisation, which makes machines that have only R installed. The tag after the colon picks the version, here a machine with R 4.3.2. *(00:37:05, 00:37:22, 00:37:26)*

- **Q:** Why would anyone want R 4.3.2 in a container when `R --version` on the laptop shows R 4.6.2?
  **A:** Some work needs an older, fixed version, as in pharmaceutical clinical trials research that runs for years while R updates every six months. You don't want to redo or check your work every six months. Regulators may also require your code and the full compute environment, so you hand over the container that ran the analysis. *(00:37:54, 00:38:10, 00:38:23)*

- **Q:** How does what a container pins differ from what a `uv` or `renv` lock file pins?
  **A:** Lock files track package versions only. A container goes one level deeper and fixes the tools on the system as well, such as the version of R itself or of Git. For example, a container with a 2019 Git would prevent anyone from running `git switch`. *(00:38:46, 00:39:02)*

- **Q:** What does the output "Status: Image is up to date" with a `Digest: sha256:...` line mean after `docker pull rocker/r-ver:4.3.2`?
  **A:** The image was already downloaded and no newer version exists, so nothing new was pulled. The hash identifies the exact version of the image you have. *(00:39:47, 00:39:51)*

- **Q:** Why does `docker pull` sound so much like `git pull`?
  **A:** Tools in the data science and compute stack borrow words from one another. Both commands pull something onto your computer. *(00:40:22, 00:40:33)*

- **Q:** What does `--rm` do in `docker run --rm -it rocker/r-ver:4.3.2`, and what does its double dash tell you?
  **A:** Two dashes mark a flag that is several letters long. `--rm` deletes the container automatically when you turn it off; otherwise you would have to delete it by hand. *(00:40:55)*

- **Q:** Explain `-it` in `docker run --rm -it rocker/r-ver:4.3.2`.
  **A:** It is two single-letter flags chained together, the same way `ls -alh` chains three. `-i` (interactive) lets you type into the container, and `-t` (TTY) gives you an actual terminal to interact with. *(00:41:20, 00:41:48)*

- **Q:** Why did `library(tidyverse)` fail inside the `rocker/r-ver:4.3.2` container but load in a local terminal on the same laptop?
  **A:** The container has only R in it; nobody had told it to install tidyverse. The laptop has tidyverse installed. The two terminals behave like two different machines because the container effectively is a different machine. *(00:43:49, 00:44:09)*

- **Q:** How is running a Docker container like connecting to a cloud machine?
  **A:** In both cases you are connected to another machine, through pretty much the same interface. With Docker, that other machine just happens to run on the same hardware you're typing on. *(00:44:31)*

## 11. Know which machine you are typing on

*00:45:01–00:46:44*

- **Q:** Why does paying attention to your terminal prompt matter once you use containers and remote systems?
  **A:** The prompt is often your only visual cue about which machine you are on. After quitting the container, the laptop's own prompt came back, which showed he was on his actual computer again. *(00:45:04)*

- **Q:** What did the instructor's terminal on a computer in his closet at home show about remote work?
  **A:** Commands typed there ran on that other computer. The only visual cue was the hostname he had given it, a Game of Thrones sword name. Sometimes you get nothing but a blinking cursor, so these cues are what tell you where you are. *(00:45:45, 00:45:48, 00:46:08)*

- **Q:** Explain why a command like `whoami` exists, as discussed in DSCI 521.
  **A:** It reports the username on that computer. That is another way to check that you are on the machine you think you're working on. *(00:46:08, 00:46:29)*

## 12. Why so many data science tools run in a browser

*00:46:44–00:49:11*

- **Q:** Why are so many applications built on Electron as "browser-first" apps?
  **A:** Electron makes a browser into the application. An app built that way can run in a container, or on another machine, and be opened in a browser. *(00:47:39)*

- **Q:** Why do you open Jupyter Lab at a `localhost` address instead of double-clicking an app?
  **A:** Jupyter Lab was made to run on a remote container that can have many more cores and much more memory than your laptop, while keeping the same interface. Building it as a browser app means you just connect your browser to wherever it is running. *(00:48:04, 00:48:33)*

- **Q:** What does GitHub's Codespaces button show about running tools in a browser?
  **A:** It opens VS Code in a browser on another machine whose whole compute environment someone has set up. You get the same interface while working on the same versions of all the software. *(00:48:49, 00:49:00, 00:49:07)*

## 13. Running RStudio in a container and mapping ports ([28.1.3 Mapping ports to containers with web apps](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#mapping-ports-to-containers-with-web-apps))

*00:54:10–00:58:59*

- **Q:** Why keep `--rm` when running `rocker/rstudio:4.4.2`, especially while practising with several containers?
  **A:** `--rm` shuts the machine down and cleans it up when you exit; otherwise it keeps running. Every running container takes up RAM. Leave several running and your computer stops working well, because you've turned on "five computers" that each use resources. *(00:55:06, 00:55:17, 00:55:24)*

- **Q:** Why does running RStudio in a container need a port at all?
  **A:** As with Jupyter Lab, the application is running somewhere else, inside the container. You have to connect your browser on your machine to the place where it is running, and the port is that connection point. *(00:55:41, 00:55:56)*

- **Q:** In `docker run --rm -p 8787:8787 rocker/rstudio:4.4.2`, what do the numbers on each side of the colon mean?
  **A:** The left number is the port on your local computer. The right number is the port inside the container, where RStudio is running. `-p 8787:8787` takes the container's 8787 and puts it on the Mac's 8787. *(00:56:38, 00:57:05)*

- **Q:** How can you run two RStudio containers at the same time if both listen on 8787?
  **A:** The container side stays 8787, but you redirect each container to a different port on your machine. Things can run side by side as long as they use different local ports, which you specify with `-p`. *(00:56:38, 00:57:29)*

- **Q:** Why does RStudio Server use 8787 when Jupyter Lab uses a different number?
  **A:** The numbers are arbitrary. Each tool's developers picked one, and you could pick whatever you want. *(00:55:56, 00:56:19)*

- **Q:** What did comparing RStudio at `localhost:8787` with the desktop RStudio show?
  **A:** The desktop RStudio runs the laptop's R 4.6.2. The browser RStudio runs R 4.4.2 inside the container, which also differs from the R 4.3.2 in the earlier `r-ver` container. You can treat them as completely different machines: one terminal-only, one an application running in a browser. *(00:58:41, 00:58:51, 00:58:59)*

## 14. Passing environment variables into a container

*00:59:20–01:02:53*

- **Q:** Why did the instructor rerun RStudio with `-e PASSWORD="apassword"`?
  **A:** Without it, the container generates a password that is very annoying to remember. The start-up output itself says you can set your own by setting the `PASSWORD` environment variable. Passing `-e` with the same `docker run` command sets that variable, and the container used it as the login password. *(00:59:45, 01:00:05, 01:00:39)*

- **Q:** Why can't you assume every container understands a variable like `PASSWORD`?
  **A:** Whether a container reads certain variables depends on how whoever built it set it up. Containers behave differently depending on how they were built. *(01:00:05, 01:01:08)*

- **Q:** Why was it acceptable for the instructor to show his RStudio password on screen?
  **A:** The container's port is only reachable through his physical machine. If you can't log into his laptop, port 8787 on it isn't available to you. *(01:00:16, 01:00:28)*

- **Q:** Explain the benefit of putting a dashboard (as in DSCI 532) into a container.
  **A:** You've done all the installation, so the end user doesn't have to install `renv`, restore a snapshot or go through the setup at all. If they have Docker, they `docker run` it with some flags and open the port. You've essentially given them a computer you built from scratch. *(01:01:47, 01:02:20)*

## 15. Starting from a base image and working inside it ([29.1.1 Workflow for building a Dockerfile](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#workflow-for-building-a-dockerfile))

*01:03:00–01:08:19*

- **Q:** Why start your own container from `rocker/r-ver:4.6.2` instead of a completely blank machine?
  **A:** Whoever designed that image has already installed R and probably the system pieces a brand-new computer needs for R to work. Those are like the Xcode or compiler tools students installed on their own laptops. Starting there lets you skip steps. *(01:04:00, 01:04:29)*

- **Q:** What does adding `bash` to the end of `docker run --rm -it rocker/r-ver:4.6.2 bash` change?
  **A:** It tells the container not to start its default program, R, and to give you a terminal instead. The prompt changes to the container's own, and you can do anything there. You can still type `R` to start R. *(01:04:53, 01:05:20)*

- **Q:** Why try install steps interactively in a shell before writing them down?
  **A:** You go through the steps first, and once they work you document them. You end up with instructions for building the machine from scratch that you know succeed. *(01:05:43, 01:05:48)*

- **Q:** Why did `library(cowsay)` fail after the instructor exited the container and started it again, right after installing the package?
  **A:** A container has no saved state. Each time it starts, it resets back to how its image was set up. Anything installed by hand in the previous session was gone. *(01:07:10, 01:08:11)*

- **Q:** Why is a container a safe place to run destructive commands, like the "delete the computer" command warned about in DSCI 521?
  **A:** The damage only happens inside the container. Once you turn it off and on again, it is as if you never ran the command. That makes containers a good place to try packages and learn Linux without messing up your own computer. *(01:07:25, 01:07:37)*

- **Q:** Why is the reset also a problem when sharing an analysis?
  **A:** Users would have to follow your README install steps every time they load the container. Installing tidyverse on Linux can take 15 minutes, and spending that before every 30-second analysis is really painful. *(01:08:19)*

## 16. Running R from the command line with `Rscript -e` ([29.1.2 Build your first image](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#build-your-first-image))

*01:08:19–01:10:18*

- **Q:** Why did the instructor need a terminal command for installing `cowsay` rather than `install.packages()` typed inside R?
  **A:** Saving the setup comes down to knowing the terminal command that makes it happen. He needed R to execute the install from the command line, not to open an interactive R session where he types it. *(01:08:54, 01:08:59)*

- **Q:** Explain each part of `Rscript -e "install.packages('cowsay')"`.
  **A:** `Rscript` is how R runs commands from the terminal. `-e` means "here is an R expression", and the expression is the `install.packages` call. The quoting matters: double quotes on the outside and single quotes inside. *(01:09:23, 01:09:27, 01:09:41)*

- **Q:** After `Rscript -e "install.packages('cowsay')"` worked, why was `cowsay` missing again in the next container?
  **A:** The install happened only in that running container, and exiting threw it away. Knowing the command isn't enough: the information has to be saved somewhere, which is what the `Dockerfile` is for. *(01:10:01, 01:10:13, 01:10:18)*

## 17. The `Dockerfile`: `FROM`, `RUN`, `CMD` ([29.2 `Dockerfile` command summary](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#dockerfile-command-summary))

*01:10:18–01:15:01*

- **Q:** What is a `Dockerfile`, and how does it explain why the RStudio container works as soon as you run it?
  **A:** A `Dockerfile`, named with a capital D by convention, holds the instructions for installing and setting up a computer. The RStudio image has its own `Dockerfile` that installs RStudio and opens the ports. That is why RStudio is ready when you load the container. *(01:10:22, 01:10:41, 01:10:45)*

- **Q:** What does the `FROM rocker/r-ver:4.6.2` line do, and why is a fairly large base image acceptable?
  **A:** `FROM` names the starting-point machine, here one with R 4.6.2 already installed. You could start from a bare-minimum Linux and install everything by hand. Disk space is relatively cheap compared with other costs, so a beefier starting machine is fine. *(01:11:25, 01:11:30, 01:12:02, 01:12:15)*

- **Q:** What is the difference between `RUN` and `CMD` in the class's `Dockerfile`?
  **A:** `RUN` holds the bash commands the container executes while it is being built, here installing `cowsay` with `Rscript`. `CMD` is the last thing, the default the machine runs when you turn it on: printing "Hello from my first image!". *(01:12:44, 01:13:52, 01:14:05)*

- **Q:** How does `CMD` relate to adding `bash` at the end of `docker run`?
  **A:** `CMD` is only the default behaviour, used when you don't say something like `bash`. Naming a command when you run the container overrides it. *(01:13:52, 01:14:05)*

- **Q:** How is `CMD ["Rscript", "-e", "cowsay::say('Hello from my first image!')"]` written differently from the same command typed in a shell?
  **A:** It looks like a bash command, but instead of separating terms with spaces it writes them as a list. *(01:13:40)*

- **Q:** Explain how the middle of a `Dockerfile` would differ for a Python project.
  **A:** In place of the `Rscript` install, you'd run the command that installs `uv` and use a copy command to bring in your lock files. Then you'd run `uv sync`. The packages are then installed in the container, so the machine has your compute environment ready. *(01:14:15)*

## 18. Building and running your own image ([29.4.3 3. How do I build an image locally on my laptop?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#how-do-i-build-an-image-locally-on-my-laptop))

*01:15:01–01:18:44*

- **Q:** Explain each part of `docker build --tag hello-cowsay .`.
  **A:** `--tag` gives the new machine the name `hello-cowsay`. The `.` tells Docker where to look for the `Dockerfile`: the current directory. It may be the first time a lone dot is something you must type. By default, `docker build` looks there for a file named exactly `Dockerfile`. *(01:15:11, 01:15:38)*

- **Q:** Why does the course assume `docker build` and other project commands are run from the repository root?
  **A:** Then every command in the instructions can just be copy-pasted. Nobody has to worry about changing directories in the middle of something. Milestone instructions make the same assumption. *(01:16:11, 01:16:29)*

- **Q:** What is the difference between `docker run --rm -it hello-cowsay` and `docker run --rm -it hello-cowsay bash`?
  **A:** Without `bash`, the container runs its `CMD` and prints the cow saying "Hello from my first image!". With `bash`, the default is overridden and you get a terminal inside the machine instead. *(01:17:14, 01:17:28, 01:17:30)*

- **Q:** Why does `library(cowsay)` work inside `hello-cowsay` when it kept failing in containers from `rocker/r-ver:4.6.2`?
  **A:** The install instructions are now in the `Dockerfile`, and the machine was built from them. Every container started from `hello-cowsay` therefore begins with `cowsay` installed, instead of resetting to a machine without it. *(01:17:52)*

- **Q:** Why is shell access to your own image useful?
  **A:** When code works on your machine but not in the container, you can play inside the container directly to find out why. *(01:17:30)*

- **Q:** Why does writing a `Dockerfile` depend so much on knowing bash?
  **A:** Apart from the starting point, the middle of a `Dockerfile` is all commands, such as `RUN` and copy commands. You have to give it the exact shell commands it needs to install whatever you need. *(01:18:07)*

## 19. Pinning versions, and what comes next

*01:18:44–01:20:39*

- **Q:** Why should a project container pin the versions of its tools?
  **A:** Things updating without you being explicit, and without you knowing an update happened, is very annoying. Pinning in Docker means a version doesn't change until you change that line. You control what gets updated and when. *(01:19:35, 01:19:46, 01:20:27)*

- **Q:** What went wrong when the instructor restarted a container in another class, and what does it show?
  **A:** He hadn't hard-pinned any versions, and something had updated the day before, so nothing worked. On a real job you'd spend hours fixing the broken update instead of doing the actual work. That is the reason to pin. *(01:19:55)*

- **Q:** How does a `Dockerfile` keep a project on the same versions a year from now?
  **A:** The `FROM` line fixes the version of R. The install lines can name specific versions of other tools, even an older Quarto than the latest. As long as you don't change those install commands, a year later you are still on the same versions. *(01:18:53, 01:19:14, 01:19:35)*

---

- prompt: prompt-recall-2-understand.md @ 8bcc190
- prompt-hash: d3d1585a5f4d
- model: claude-opus-5-5 (requested: opus)
- backend: claude
- inputs: transcript-plaud.md, history.txt, terminal.txt, materials.md, notes-class-main--claude-opus-5-5.md
- generated: 2026-11-20
- notes-input: notes-class-main--claude-opus-5-5.md @ 1c708a29f65f, links and section references removed
