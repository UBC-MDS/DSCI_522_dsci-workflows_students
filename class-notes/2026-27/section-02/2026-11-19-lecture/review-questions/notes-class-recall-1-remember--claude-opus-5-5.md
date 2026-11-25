# Git issues and pull requests, then Docker containers: review questions, tier 1 — Remember

Date: 2026-11-19

Instructor: Daniel Chen

*Tier 1 of 5: Remember. Answer each question before you read its answer; tiers 2 to 5 build on these.*

## 1. Opening: pull the Docker images and start the branch exercise ([Download the images before you start](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#download-the-images-before-you-start))

*00:00:14–00:01:41*

- **Q:** How many Docker commands were posted in Slack for students to run at the start of class, and roughly how long did the instructor say they would take?
    - **A:** Three Docker commands, which should be done in about ten minutes. *(00:00:18)*

- **Q:** Name the three images the start-of-class `docker pull` commands download.
    - **A:** `rocker/r-ver:4.3.2`, `rocker/rstudio:4.4.2` and `quay.io/jupyter/datascience-notebook:2025-03-14`. *(00:00:18)*

- **Q:** What application must be open before you run the class's Docker commands?
    - **A:** Docker Desktop. If it is off, the commands tell you to turn it on. If you get an error that Docker can't be found, you still need to install Docker. *(00:00:33)*

- **Q:** List the three steps of the warm-up Git exercise at the start of class.
    - **A:** Make a branch, create a pull request, and merge it. *(00:00:43)*

- **Q:** State which courses the instructor said will use pull requests and issues from now on.
    - **A:** All of your project-based courses moving forward. *(00:00:57)*

## 2. Project advice: keep the analysis simple

*00:01:41–00:05:57*

- **Q:** What did the instructor call his biggest tip for the group project?
    - **A:** Do not make your analysis difficult. If a straight-line model fits, fit the straight-line model. *(00:01:56)*

- **Q:** Quote the instructor's warning about choosing an ambitious model, such as a neural net, for the project.
    - **A:** "You're going to have a very bad time in about two weeks if you do that." *(00:02:16)*

- **Q:** How much machine learning code did the instructor say students will see in the lectures?
    - **A:** Almost none. The course is not a model-fitting course. *(00:02:28)*

- **Q:** List the kinds of code the instructor said the project still needs, even when kept simple.
    - **A:** Code that downloads the data, possibly cleaning code, EDA code, modelling code, and figures and tables. *(00:02:41)*

- **Q:** State what the instructor said about model accuracy versus correctness.
    - **A:** It doesn't matter if the model is 60% accurate, but it has to be technically correct, using correct data science and machine learning techniques. *(00:03:08)*

- **Q:** What did the instructor say to do if you want the project to become a portfolio piece?
    - **A:** Don't do it in this assignment. Do it in parallel if you really want to. *(00:03:27)*

- **Q:** Name the example of an incorrect technique the instructor gave.
    - **A:** Fitting logistic regression when you're trying to predict a numeric outcome: "That's just wrong." *(00:05:24)*

- **Q:** State the topic of this week's project work and the topic of next week's.
    - **A:** This week is getting everything on Git, and next week is containers. *(00:04:49)*

- **Q:** How long do students build on the same project?
    - **A:** Three or four weeks. *(00:05:37)*

## 3. Git review: working on a branch

*00:06:16–00:09:50*

- **Q:** Name the demo repository the instructor cloned for this class.
    - **A:** `2026-11-19-docker`. *(00:06:20)*

- **Q:** What line did the instructor add to the demo repository's `README.md`?
    - **A:** "today we will talk about containers". *(00:07:39)*

- **Q:** Which branch did `git status` show the instructor was on after he edited `README.md` in the demo repository?
    - **A:** `main`, which is not where he meant to work. *(00:07:44)*

- **Q:** Where did the instructor say to find commands for fixing commits you accidentally made on `main`?
    - **A:** In a cheat sheet in the textbook. *(00:07:44)*

- **Q:** When did the instructor say to check which branch you are on in a branch workflow?
    - **A:** Right before you run `git add`, and definitely before you run `git commit`. Getting this wrong becomes a common problem once you work with several people on several branches. *(00:08:08)*

- **Q:** What did the instructor say to do with `main` before making changes in an active collaborating environment?
    - **A:** Pull `main` so everything is up to date, so you aren't making changes to something out of date. *(00:08:27)*

- **Q:** What command created and switched to the `today` branch in the demo repository?
    - **A:** `git switch -c today`. *(00:08:57)*

- **Q:** What command did the instructor run to see his changes to `README.md` before staging them?
    - **A:** `git diff`. *(00:09:25)*

- **Q:** What commit message did the instructor use for the `README.md` change on the `today` branch?
    - **A:** `"today we are talking about containers"`. *(00:09:25)*

- **Q:** What command pushed the `today` branch to GitHub?
    - **A:** `git push origin today`. *(00:09:44)*

## 4. GitHub issues as a project board

*00:09:50–00:16:17*

- **Q:** What did the instructor say issues are a good way to do?
    - **A:** To track what is happening in your project. He described them as a very simple view of a project board. *(00:10:08)*

- **Q:** Which later MDS course did the instructor say will cover issues in more depth?
    - **A:** DSCI 524. *(00:10:08)*

- **Q:** What did the instructor say you should document as an issue?
    - **A:** Who is responsible for what. *(00:10:28)*

- **Q:** State one way the instructor said MDS uses the issue board of an internal repository.
    - **A:** To keep meeting notes. Action items from the meeting can then be spun out into separate issues. *(00:10:49)*

- **Q:** Name the two issues in the `2026-11-19-docker` demo repository.
    - **A:** Issue #1 "what are we doing today?" and issue #2 "edit the readme with today's topic". *(00:11:37)*

- **Q:** State how GitHub numbers issues and pull requests in the same repository.
    - **A:** They share one numbering sequence. If you create an issue and then a pull request right after, the pull request is number two. *(00:12:07)*

- **Q:** What text did issue #2 in the demo repository use to refer to issue #1?
    - **A:** "meeting from #1". *(00:12:30)*

- **Q:** What happens to the referenced item when you write a `#` number in an issue or pull request?
    - **A:** It becomes a two-way reference: the referenced item automatically shows a link back. *(00:13:34)*

- **Q:** What did the instructor say he sometimes asks a coding agent to do when he has a random thought?
    - **A:** File an issue for it, so he doesn't tab over to a browser and lose track. *(00:13:24)*

- **Q:** According to the instructor, what made GitHub super popular, beyond Git itself?
    - **A:** Issues and pull requests, and tracking everything as a project management system. *(00:13:47)*

- **Q:** How many issues does this course ask you to have, and must each get its own pull request?
    - **A:** Three issues. It's okay if one pull request deals with all three. *(00:14:23)*

- **Q:** Who did the instructor assign as a reviewer on the demo pull request?
    - **A:** Copilot. *(00:15:14)*

- **Q:** Name the two roles you can give people on a pull request.
    - **A:** Assignee, which claims it as your responsibility, and reviewer, for a teammate who looks over your work. *(00:14:47)*

## 5. Pull request descriptions, checkboxes and closing keywords

*00:16:17–00:22:18*

- **Q:** Which comment in an issue or pull request did the instructor say to keep up to date?
    - **A:** The first comment, so readers can see what is happening and why the thing exists without reading the whole conversation. *(00:16:56)*

- **Q:** Whose comments can a project owner typically edit?
    - **A:** Other people's comments. *(00:16:51)*

- **Q:** What Markdown feature did the instructor use in the pull request description to track remaining work?
    - **A:** Checkboxes, such as `- [ ] item`. *(00:17:49)*

- **Q:** Name the pull request button the instructor mentioned as another way to show that work isn't done yet.
    - **A:** The draft button. *(00:17:49)*

- **Q:** Name the two pull request keywords the instructor gave for linking issues.
    - **A:** `closes` and `fixes`. *(00:18:33)*

- **Q:** Is auto-closing issues with keywords a Git feature or a GitHub feature?
    - **A:** A GitHub feature, not a feature of the Git version control system. *(00:18:54)*

- **Q:** What happens to issues named after `fixes` or `closes` in a pull request description when that pull request is merged?
    - **A:** The issues are closed automatically. *(00:19:30)*

- **Q:** Which closing keyword does the instructor almost always use?
    - **A:** `fixes`. *(00:19:55)*

- **Q:** Besides a pull request description, where else did the instructor say you can write a closing keyword?
    - **A:** In a commit message, but it's harder to see there. *(00:19:55)*

- **Q:** Reproduce the closing line of pull request #3's description in the demo repository.
    - **A:** `closes #1 fixes #2`. The description also opened with "this is the fix for #2". *(00:14:14)*

- **Q:** What example did the instructor give of one pull request fixing several issues in his own work?
    - **A:** A refactor of the containers and virtual environments chapters in the textbook. Moving the old material and writing the new material were separate issues, all fixed by one pull request. *(00:21:17)*

- **Q:** State whether students are graded on closing all their issues by the end of the course.
    - **A:** No. Stretch-goal and longer-term issues can stay open. *(00:21:50)*

## 6. Cleaning up after a merge

*00:22:18–00:25:19*

- **Q:** After the demo pull request was merged, what two commands brought local `main` up to date?
    - **A:** `git switch main`, then `git pull origin main`. *(00:22:25)*

- **Q:** Name the two places on GitHub where you can delete a merged branch.
    - **A:** The delete-branch button on the pull request after merging, or the trash can icon in the branches view. *(00:22:53)*

- **Q:** Which pull request number did GitHub's branches view show for the `today` branch?
    - **A:** Pull request number three, marked as merged. *(00:22:53)*

- **Q:** Are students required to delete their branches in this course?
    - **A:** No. You can keep them as a record if you want. *(00:23:16)*

- **Q:** What command did the instructor use to view the branch history as a graph?
    - **A:** `git log --oneline --graph --all`. *(00:23:56)*

- **Q:** What was the merge commit's message in the demo repository's log?
    - **A:** "Merge pull request #3 from chendaniely/today". *(00:23:56)*

- **Q:** What command removed the local reference to the branch that had been deleted on GitHub?
    - **A:** `git fetch --prune`, which dropped `origin/today`. *(00:24:30)*

- **Q:** What command deleted the local `today` branch?
    - **A:** `git branch -d today`. *(00:24:30)*

- **Q:** What hash would you have to type with `git switch` once the `today` name is gone?
    - **A:** `3c6d82a`, which is why some people keep the branch name. *(00:25:05)*

## 7. Why data science workflows need stable environments ([27.1 Documenting and loading dependencies](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#documenting-and-loading-dependencies))

*00:25:29–00:30:13*

- **Q:** What is DSCI 522 called?
    - **A:** Data Science Workflows. *(00:25:48)*

- **Q:** Name the Python plotting libraries the instructor mentioned as different project choices.
    - **A:** Altair, Plotly and Matplotlib. *(00:27:06)*

- **Q:** State the two problems the instructor gave with installing every package instead of a bare-minimum list.
    - **A:** It wastes disk space. Also, packages update on different cycles, so you can end up unable to install everything together. *(00:28:04)*

- **Q:** Name the two kinds of Windows chips the instructor mentioned.
    - **A:** ARM Windows chips and Intel Windows chips. *(00:28:53)*

- **Q:** Quote the phrase the instructor said doesn't really work when teammates can't run your code.
    - **A:** "This works on my machine." *(00:29:39)*

- **Q:** Name the two goals the instructor gave for the course's tooling.
    - **A:** Creating a stable computing environment, and building modular data science pipelines. *(00:29:55)*

## 8. What a container is ([27.2 What is a container?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#what-is-a-container))

*00:30:13–00:34:28*

- **Q:** Which tools did the instructor say handled keeping package versions consistent in DSCI 521?
    - **A:** `uv` and `renv`. *(00:30:13)*

- **Q:** How did the instructor define a container?
    - **A:** A virtual computer built from scratch that you give to others, so everyone does their work on the same computer even on different physical machines. *(00:31:49)*

- **Q:** What cost of containers did the instructor name?
    - **A:** A performance hit, because there is an extra layer on top. *(00:32:34)*

- **Q:** What happens if you mess up a container sandbox?
    - **A:** You restart it and get a new sandbox. *(00:33:05)*

- **Q:** Besides Docker, name the container tools the instructor listed.
    - **A:** LXC, LXD and Podman. He added that Amazon probably has its own. *(00:34:03)*

- **Q:** Asked what an "instance" is, what did the instructor say cloud providers such as Google give you?
    - **A:** A container on one of their servers, not an actual machine. Pretty much all cloud compute runs on some version of containers. *(00:33:30)*

## 9. Containers versus virtual machines ([27.3 Contrasting containers with virtual machines](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#contrasting-containers-with-virtual-machines))

*00:34:31–00:36:40*

- **Q:** How did the instructor define a virtual machine?
    - **A:** A full-blown operating system, such as all of Windows, with the graphical interface and all its buttons. *(00:34:48)*

- **Q:** What does a container typically leave out compared with a virtual machine?
    - **A:** The graphical interface. It holds only the bare minimum you install. *(00:35:00)*

- **Q:** State the size the instructor gave for a Windows virtual machine and for the containers used in class.
    - **A:** A Windows install is about 50 to 80 GB. The containers used in class are under two gigabytes, or even under one. *(00:36:16)*

- **Q:** For what does the instructor still use virtual machines?
    - **A:** Testing the MDS install instructions, because he has to pretend he is on a Windows machine. *(00:36:01)*

## 10. Pulling and running a container: R 4.3.2 beside local R ([28.1.1 Launch and run containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#launch-and-run-containers))

*00:36:40–00:45:01*

- **Q:** What command downloads the R 4.3.2 image used in class?
    - **A:** `docker pull rocker/r-ver:4.3.2`. *(00:37:02)*

- **Q:** In `rocker/r-ver:4.3.2`, what is `rocker`, and what do its `r-ver` machines contain?
    - **A:** `rocker` is the organisation, and these machines have only R installed. *(00:37:22)*

- **Q:** What version of R did `R --version` report on the instructor's laptop?
    - **A:** R 4.6.2. *(00:37:32)*

- **Q:** How often did the instructor say R updates?
    - **A:** Every six months. *(00:38:10)*

- **Q:** In the pharmaceutical example, what do regulators want with a drug submission besides your code?
    - **A:** The whole compute environment, so they can reproduce your work. *(00:38:23)*

- **Q:** What did the instructor say he could do to stop everyone from using `git switch`?
    - **A:** Give them a container with an old version of Git that predates `git switch`. *(00:39:02)*

- **Q:** What status did `docker pull rocker/r-ver:4.3.2` print when the image was already downloaded?
    - **A:** `Status: Image is up to date for rocker/r-ver:4.3.2`, along with a digest hash. *(00:39:47)*

- **Q:** Which Git command did the instructor say `docker pull` sounds like?
    - **A:** `git pull`, because both pull something onto your computer. *(00:40:33)*

- **Q:** What does the `--rm` flag of `docker run` do?
    - **A:** It deletes the container automatically when it is turned off. Otherwise you have to delete it by hand. *(00:40:55)*

- **Q:** What do the `-i` and `-t` in `docker run -it` stand for?
    - **A:** `-i` is interactive, and `-t` is TTY, which gives you a terminal you can interact with. *(00:41:48)*

- **Q:** Which `ls` command did the instructor use to show that single-letter flags can be chained?
    - **A:** `ls -alh`: all, list, and human-readable sizes. *(00:41:20)*

- **Q:** What does `docker run` do if the image is not on your computer yet?
    - **A:** It downloads the image first. *(00:42:16)*

- **Q:** What command ran R 4.3.2 interactively in a container?
    - **A:** `docker run --rm -it rocker/r-ver:4.3.2`. *(00:42:38)*

- **Q:** How do you start R in a terminal?
    - **A:** Type capital `R`. *(00:42:38)*

- **Q:** What error did `library(tidyverse)` give inside the `rocker/r-ver:4.3.2` container?
    - **A:** `there is no package called 'tidyverse'`, because the container has only R in it. *(00:43:49)*

## 11. Know which machine you are typing on

*00:45:01–00:46:44*

- **Q:** What did the instructor say is often your only visual cue for which machine you are typing on?
    - **A:** The terminal prompt. Sometimes you are given nothing but a blinking cursor, so know where you're typing. *(00:45:04)*

- **Q:** Where was the remote computer the instructor connected to from his terminal?
    - **A:** In his closet at home. *(00:45:45)*

- **Q:** Name the command the instructor recalled from DSCI 521 for checking which machine you're on.
    - **A:** `whoami`, which reports the username for that computer. *(00:46:08)*

## 12. Why so many data science tools run in a browser

*00:46:44–00:49:11*

- **Q:** Name the browser that many applications are built on.
    - **A:** Electron. *(00:47:39)*

- **Q:** Why did the instructor say Jupyter Lab is opened through `localhost` in a browser?
    - **A:** It was made to run on remote containers with more cores and memory while giving you the same interface. *(00:48:04)*

- **Q:** What does clicking the Codespaces button on GitHub give you?
    - **A:** VS Code running in a browser. *(00:48:49)*

## 13. Running RStudio in a container and mapping ports ([28.1.3 Mapping ports to containers with web apps](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#mapping-ports-to-containers-with-web-apps))

*00:54:10–00:58:59*

- **Q:** What happens to your computer if you leave several containers running?
    - **A:** Each container takes up RAM, so you can end up with five computers using resources and a computer that stops working well. Use `--rm` so containers shut down when you exit. *(00:55:17)*

- **Q:** Which port does RStudio use inside its container?
    - **A:** `8787`. *(00:55:56)*

- **Q:** What did the instructor say about how port numbers are chosen?
    - **A:** They are very arbitrary: you can pick whatever you want. *(00:56:19)*

- **Q:** In `-p 8787:8787`, which number is the port on your computer and which is the port in the container?
    - **A:** The left number is on your local computer, and the right number is in the container. *(00:57:05)*

- **Q:** How can you run two RStudio containers at the same time?
    - **A:** Map the second container's `8787` to a different port on your machine. *(00:56:38)*

- **Q:** What command started RStudio Server in a container in class?
    - **A:** `docker run --rm -p 8787:8787 rocker/rstudio:4.4.2`. *(00:57:42)*

- **Q:** What address did the instructor open in the browser to reach RStudio in the container?
    - **A:** `localhost:8787`. *(00:57:51)*

- **Q:** What username logs into RStudio in the `rocker/rstudio` container, and where does the password come from?
    - **A:** The username is `rstudio`, and the password is printed in the container's start-up output. *(00:58:29)*

## 14. Passing environment variables into a container

*00:59:20–01:02:53*

- **Q:** Which `docker run` flag passes an environment variable into a container?
    - **A:** `-e`. *(01:00:05)*

- **Q:** Which environment variable sets the password for the `rocker/rstudio` container?
    - **A:** `PASSWORD`, in all caps. *(01:00:05)*

- **Q:** Reproduce the command that ran RStudio with a password chosen by the instructor.
    - **A:** `docker run --rm -p 8787:8787 -e PASSWORD="apassword" rocker/rstudio:4.4.2`. *(01:00:39)*

- **Q:** Does every container use the same environment variables?
    - **A:** No. It depends on how the container was set up, and not every container has this. *(00:59:45)*

- **Q:** Who can reach a container on port `8787` of the instructor's laptop?
    - **A:** Only someone with access to his physical machine. *(01:00:16)*

- **Q:** For which later MDS course did the instructor say you could put your work in a container?
    - **A:** DSCI 532. You put your dashboard in a container, and someone can run it and open its port without doing any installation. *(01:01:47)*

## 15. Starting from a base image and working inside it ([28.1.4 Changing the containers default command](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#changing-the-containers-default-command))

*01:03:00–01:08:19*

- **Q:** What setup step on students' laptops did the instructor say a base image like `rocker/r-ver` may already have done for you?
    - **A:** Installing compiler tools like the Xcode tools that students installed for R. *(01:04:00)*

- **Q:** What command opened a Bash shell, not R, in the R 4.6.2 container?
    - **A:** `docker run --rm -it rocker/r-ver:4.6.2 bash`. *(01:04:44)*

- **Q:** What happens to the prompt after you start a container with `bash`?
    - **A:** It changes to the container's prompt, such as `root@95765251a970:/#`. *(01:05:20)*

- **Q:** At the container's Bash prompt, how do you still get R?
    - **A:** Type `R`. *(01:05:20)*

- **Q:** What does the R package `cowsay` do?
    - **A:** It draws ASCII art: a cow with some text. *(01:06:08)*

- **Q:** What function call made the cow say hello in the container?
    - **A:** `cowsay::say('hello')`. *(01:06:41)*

- **Q:** What did `library(cowsay)` print after the container was exited and started again?
    - **A:** `there is no package called 'cowsay'`. *(01:07:10)*

- **Q:** Does a container keep a saved state between runs?
    - **A:** No. It turns back on as its image was built. *(01:08:11)*

- **Q:** How long did the instructor say installing tidyverse on Linux can take?
    - **A:** About 15 minutes, which is painful for a 30-second analysis. *(01:08:19)*

## 16. Running R from the command line with `Rscript -e` ([29.1.2 Build your first image](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#build-your-first-image))

*01:08:19–01:10:18*

- **Q:** What command runs R code from the terminal?
    - **A:** `Rscript`. *(01:09:23)*

- **Q:** What does the `-e` in `Rscript -e` stand for?
    - **A:** Expression: you are giving it an R expression. *(01:09:27)*

- **Q:** Reproduce the shell command that installed `cowsay` in the container.
    - **A:** `Rscript -e "install.packages('cowsay')"`. *(01:09:47)*

- **Q:** What quoting did the instructor use in `Rscript -e "install.packages('cowsay')"`?
    - **A:** Double quotes on the outside and single quotes on the inside. *(01:09:41)*

- **Q:** What happened to `cowsay` after exiting the container and starting it again?
    - **A:** It was gone. *(01:10:01)*

## 17. The `Dockerfile`: `FROM`, `RUN`, `CMD` ([29.2 `Dockerfile` command summary](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#dockerfile-command-summary))

*01:10:18–01:15:01*

- **Q:** What is a `Dockerfile`, and how is its name written?
    - **A:** The file holding the instructions for installing and setting up the computer. It is named `Dockerfile` with a capital D. *(01:10:22)*

- **Q:** What does the `FROM` line of a `Dockerfile` state?
    - **A:** The starting-point machine. It is in all caps and normally the first line. *(01:11:30)*

- **Q:** Reproduce the `FROM` line of the class's `Dockerfile`.
    - **A:** `FROM rocker/r-ver:4.6.2`. *(01:11:30)*

- **Q:** What does `RUN` do in a `Dockerfile`?
    - **A:** It runs the Bash commands you want during the build. *(01:12:44)*

- **Q:** Reproduce the `RUN` line of the class's `Dockerfile`.
    - **A:** `RUN Rscript -e "install.packages('cowsay')"`. *(01:12:52)*

- **Q:** Which `Dockerfile` keyword did the instructor say is pretty rare?
    - **A:** `ENTRYPOINT`. *(01:13:36)*

- **Q:** How is a `CMD` line written differently from a Bash command?
    - **A:** As a list of terms, not terms separated by spaces. *(01:13:40)*

- **Q:** Reproduce the `CMD` line of the class's `Dockerfile`.
    - **A:** `CMD ["Rscript", "-e", "cowsay::say('Hello from my first image!')"]`. *(01:13:52)*

- **Q:** When does a container run its `CMD`?
    - **A:** By default when it starts, unless you give another command such as `bash`, which overrides it. *(01:14:05)*

- **Q:** For a Python project, what did the instructor say the `Dockerfile` would install, copy and run?
    - **A:** Install `uv`, copy in your lock files with a copy command, and run `uv sync`. *(01:14:15)*

## 18. Building and running your own image ([29.4.3 3. How do I build an image locally on my laptop?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#how-do-i-build-an-image-locally-on-my-laptop))

*01:15:01–01:18:44*

- **Q:** What command built the class's image?
    - **A:** `docker build --tag hello-cowsay .`. *(01:15:06)*

- **Q:** What does `--tag` do in `docker build`?
    - **A:** It gives the image a name, here `hello-cowsay`. *(01:15:24)*

- **Q:** What does the `.` at the end of `docker build --tag hello-cowsay .` mean?
    - **A:** Look in the current directory. *(01:15:38)*

- **Q:** Which file does `docker build` look for by default?
    - **A:** A file named exactly `Dockerfile`, with a capital D. *(01:15:38)*

- **Q:** From which directory do the milestone instructions assume you run every command?
    - **A:** The root of the repository. *(01:16:11)*

- **Q:** What command lists every image on your computer?
    - **A:** `docker images`. *(01:17:01)*

- **Q:** What did `docker run --rm -it hello-cowsay` print?
    - **A:** A cow saying "Hello from my first image!". *(01:17:14)*

- **Q:** What command opened a shell inside the `hello-cowsay` image, and did `library(cowsay)` work there?
    - **A:** `docker run --rm -it hello-cowsay bash`. `library(cowsay)` now loaded, because the build had installed it. *(01:17:30)*

- **Q:** Name the instructions a typical `Dockerfile` has in its middle section, between `FROM` and `CMD`.
    - **A:** Many `RUN` and `COPY` commands, and port commands such as opening `8787` where relevant. *(01:18:07)*

## 19. Pinning versions, and what comes next

*01:18:44–01:20:39*

- **Q:** Is building a container needed for this week's lab assignment?
    - **A:** No. You need it for next week. *(01:18:48)*

- **Q:** What did the instructor say the `FROM rocker/r-ver:4.6.2` line makes stable?
    - **A:** The version of R. *(01:18:53)*

- **Q:** What went wrong when the instructor restarted a container in another class a few weeks earlier?
    - **A:** He hadn't hard-pinned any versions, something had updated the day before, and nothing worked. *(01:19:55)*

- **Q:** Name the container topic the instructor said comes next week.
    - **A:** How to string multiple containers together. *(01:20:39)*

---

- prompt: prompt-recall-1-remember.md @ 65eb21c
- prompt-hash: e448f8420cdb
- model: claude-opus-5-5 (requested: opus)
- backend: claude
- inputs: transcript-plaud.md, history.txt, terminal.txt, materials.md, notes-class-main--claude-opus-5-5.md
- generated: 2026-11-23
- notes-input: notes-class-main--claude-opus-5-5.md @ 1c708a29f65f, links and section references removed, diagrams removed
