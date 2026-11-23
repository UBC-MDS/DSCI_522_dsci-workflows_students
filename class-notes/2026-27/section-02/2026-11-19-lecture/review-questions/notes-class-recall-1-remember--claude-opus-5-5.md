# Git issues and pull requests, then Docker containers: review questions, tier 1 — Remember

Date: 2026-11-19

Instructor: Daniel Chen

*Tier 1 of 5: Remember. Answer each question before you read its answer; tiers 2 to 5 build on these.*

## 1. Opening: pull the Docker images and start the branch exercise ([Download the images before you start](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#download-the-images-before-you-start))

*00:00:14–00:01:41*

- **Q:** How many Docker commands were posted in Slack for students to run at the start of class, and roughly how long did they take?
  **A:** Three Docker commands, which take about ten minutes to finish. *(00:00:18)*

- **Q:** List the three images the instructor pulled with `docker pull` before class.
  **A:** `rocker/r-ver:4.3.2`, `rocker/rstudio:4.4.2` and `quay.io/jupyter/datascience-notebook:2025-03-14`. *(00:00:18)*

- **Q:** Name the application that must be running before you run Docker commands, and state what an error saying Docker can't be found tells you.
  **A:** Docker Desktop. An error that Docker can't be found means Docker still needs to be installed, and if Docker Desktop is installed but off, the commands will tell you to turn it on. *(00:00:33)*

- **Q:** List the three steps of the warm-up Git exercise at the start of class.
  **A:** Make a branch, create a pull request, and merge it. *(00:00:43)*

- **Q:** According to the instructor, in which courses will you keep working with pull requests and issues?
  **A:** In all of your project-based courses from now on. *(00:00:57)*

## 2. Project advice: keep the analysis simple

*00:01:41–00:05:57*

- **Q:** State what the instructor called the biggest tip for the group project.
  **A:** Do not make your analysis difficult. If a straight-line model fits, fit the straight-line model. *(00:01:56)*

- **Q:** Quote the instructor's warning about choosing an ambitious model, such as a neural net, for the project.
  **A:** "You're going to have a very bad time in about two weeks if you do that." *(00:02:16)*

- **Q:** How much machine learning code did the instructor say you will see in this course's lectures?
  **A:** Almost none, because this is not a model-fitting course. *(00:02:28)*

- **Q:** List the kinds of code the project still needs, even when it is kept simple.
  **A:** Code that downloads the data, possibly cleaning code, EDA code, modelling code, and figures and tables. *(00:02:41)*

- **Q:** State what the instructor said about model accuracy and correctness in the project.
  **A:** The results don't matter, so 60% accuracy is fine, but the work must be technically correct data science and machine learning. *(00:03:08)*

- **Q:** Name the example the instructor gave of an analysis that is simply wrong.
  **A:** Fitting logistic regression when you are trying to predict a numeric outcome. *(00:05:24)*

- **Q:** Name the two simple models the instructor said are fine to use and will not be penalized.
  **A:** Linear regression and logistic regression. *(00:05:12)*

- **Q:** State what the instructor advised if you want to turn the project into a portfolio piece.
  **A:** Don't do it in this assignment. Do it separately, in parallel, if you really want to. *(00:03:27)*

- **Q:** Which lab session did the instructor say was happening that day?
  **A:** Lab session three. *(00:03:47)*

- **Q:** State the topics of this week's and next week's project work.
  **A:** This week is getting everything onto Git, and next week is containers. *(00:04:49)*

- **Q:** How many weeks is the same project built on?
  **A:** Three or four weeks. *(00:05:37)*

## 3. Git review: working on a branch

*00:06:16–00:09:50*

- **Q:** Name the demo repository the instructor cloned for the Git review.
  **A:** `2026-11-19-docker`, cloned with `git clone git@github.com:chendaniely/2026-11-19-docker.git`. *(00:06:20)*

- **Q:** Quote the line the instructor added to `README.md` in the `2026-11-19-docker` demo repository.
  **A:** "today we will talk about containers". *(00:07:39)*

- **Q:** Which branch did `git status` report the instructor was on after he edited `README.md`?
  **A:** `main`, with `README.md` modified and not yet committed. *(00:07:44)*

- **Q:** Where did the instructor say to look if you have already made commits on `main` by mistake?
  **A:** A cheat sheet in the textbook, which has a set of commands to move those commits around. *(00:07:44)*

- **Q:** State the habit the instructor said to build in a branch workflow before running `git add` and `git commit`.
  **A:** Check which branch you are on right before you run `git add`, and definitely before you run `git commit`. *(00:08:08)*

- **Q:** State what the instructor said to do with `main` when you are actively collaborating, before you start making changes.
  **A:** Pull `main` so everything is up to date, so you aren't making changes to something out of date. *(00:08:27)*

- **Q:** Name the command the instructor used to create and switch to the new branch `today`.
  **A:** `git switch -c today`. *(00:08:57)*

- **Q:** Name the command the instructor ran to see his changes to `README.md` before staging them.
  **A:** `git diff`. *(00:09:25)*

- **Q:** Quote the commit message the instructor used on the `today` branch.
  **A:** "today we are talking about containers". *(00:09:25)*

- **Q:** Name the command that pushed the `today` branch to GitHub.
  **A:** `git push origin today`. *(00:09:44)*

## 4. GitHub issues as a project board

*00:09:50–00:16:17*

- **Q:** What did the instructor say GitHub issues are for?
  **A:** Tracking what is happening in your project. They act as a very simple project board. *(00:10:08)*

- **Q:** Which later MDS course did the instructor say will cover issues in more depth?
  **A:** DSCI 524. *(00:10:08)*

- **Q:** What did the instructor say you should document as issues in a group project?
  **A:** Who is responsible for what. *(00:10:28)*

- **Q:** State how the MDS team uses the issue board of one of its internal repositories.
  **A:** To keep meeting notes. Action items from the meeting are then created as separate issues that spawn from the notes issue. *(00:10:49)*

- **Q:** Name the topics of issue #1 and issue #2 in the `2026-11-19-docker` demo repository.
  **A:** Issue #1 asked what today's topic is ("what are we doing today?"), and issue #2 was "edit the readme with today's topic". *(00:11:37)*

- **Q:** State how GitHub numbers issues and pull requests in a repository.
  **A:** They share one numbering sequence. If you create an issue and then a pull request, the pull request gets the next number. *(00:12:07)*

- **Q:** What do you type in an issue or pull request to refer to another item, and what kind of link does it create?
  **A:** A hash followed by the number, such as `#1`. It creates a two-way reference, so the other item links back automatically. *(00:13:34)*

- **Q:** What did the instructor name as one of the reasons GitHub, as opposed to Git, became so popular?
  **A:** Issues and pull requests that link to each other automatically, so you can track everything as a project management system. *(00:13:47)*

- **Q:** What does the instructor ask a coding agent to do when he has a random idea while working?
  **A:** File an issue for it, so he doesn't have to tab over to a browser and lose track. *(00:13:24)*

- **Q:** How many issues does the lab ask for, and how many pull requests may deal with them?
  **A:** Three issues, and it's okay if one pull request deals with all three. *(00:14:23)*

- **Q:** Who do you typically assign to your own pull request, and where do teammates go?
  **A:** You assign yourself, because it is your pull request. Teammates go in the separate reviewer section. *(00:14:47)*

- **Q:** Who did the instructor assign as a reviewer on the demo pull request?
  **A:** Copilot. *(00:15:14)*

## 5. Pull request descriptions, checkboxes and closing keywords

*00:16:17–00:22:18*

- **Q:** Which comment of an issue or pull request did the instructor say must be kept up to date?
  **A:** The first comment. People reading it want to know what is happening and why the thing exists, not read the whole conversation. *(00:16:56)*

- **Q:** Who did the instructor say can typically edit other people's comments on an issue?
  **A:** You, as the project owner. *(00:16:51)*

- **Q:** Name the Markdown feature the instructor used in a pull request to track items still to do.
  **A:** Checkboxes, written with Markdown checkbox notation such as `- [ ] item`. *(00:17:49)*

- **Q:** Besides checkboxes, which pull request button did the instructor mention for showing that work isn't finished?
  **A:** The draft button. *(00:17:49)*

- **Q:** Name the two pull request keywords the instructor said he knows for referring to issues.
  **A:** `closes` and `fixes`. *(00:18:33)*

- **Q:** Is the closing-keyword behaviour a Git feature or a GitHub feature?
  **A:** A GitHub feature, not a feature of the Git version control system. *(00:18:54)*

- **Q:** What happens when a pull request whose description says `fixes #2` is merged?
  **A:** GitHub automatically closes issue #2. *(00:19:30)*

- **Q:** Which closing keyword does the instructor almost always use?
  **A:** `fixes`. *(00:19:55)*

- **Q:** Besides the pull request description, where else did the instructor say you can write a closing keyword, and what is the drawback?
  **A:** In a commit message, but it is harder to see there. *(00:19:55)*

- **Q:** Quote the first line of the description of pull request #3 in the `2026-11-19-docker` demo repository.
  **A:** "this is the fix for #2". *(00:14:14)*

- **Q:** Name the title of the pull request that merged the `today` branch in the `2026-11-19-docker` demo repository, and give its number.
  **A:** Pull request #3, "today we are talking about containers". *(00:22:53)*

- **Q:** Will you be graded on having all your issues closed by the end of the course?
  **A:** No. Open issues for stretch goals or longer-term ideas are fine. *(00:21:50)*

## 6. Cleaning up after a merge

*00:22:18–00:25:19*

- **Q:** Name the two commands the instructor ran to bring local `main` up to date after the pull request was merged.
  **A:** `git switch main`, then `git pull origin main`. *(00:22:25)*

- **Q:** Name the two places on GitHub where you can delete a merged branch.
  **A:** The delete-branch button on the pull request after merging, or the trash can next to the branch in the branches view. *(00:22:53)*

- **Q:** Is deleting merged branches required in this course?
  **A:** No. You can keep them as a record if you want to. *(00:23:16)*

- **Q:** Name the command the instructor used to view the commit graph with all branches.
  **A:** `git log --oneline --graph --all`. *(00:23:56)*

- **Q:** Quote the message of the top commit in the `git log --oneline --graph --all` output after `main` was pulled.
  **A:** "Merge pull request #3 from chendaniely/today" (commit `d25ddfa`). *(00:23:56)*

- **Q:** Name the command that removed the local reference to the `today` branch that had been deleted on GitHub.
  **A:** `git fetch --prune`, which reported `origin/today` as `[deleted]`. *(00:24:30)*

- **Q:** Name the command that deleted the local `today` branch, and quote what it printed.
  **A:** `git branch -d today`, which printed "Deleted branch today (was 3c6d82a)." *(00:24:30)*

- **Q:** What hash did the instructor say you would have to type instead of the branch name if you deleted the `today` branch?
  **A:** `3c6d82a`, as in "git switch three c six d eighty two a" instead of `git switch today`. *(00:25:05)*

## 7. Why data science workflows need stable environments ([27.1 Documenting and loading dependencies](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#documenting-and-loading-dependencies))

*00:25:29–00:30:13*

- **Q:** What is the title of DSCI 522, as stated in class?
  **A:** Data Science Workflows. *(00:25:48)*

- **Q:** Name the three Python plotting libraries the instructor listed as examples of different project package choices.
  **A:** Altair, Plotly and Matplotlib. *(00:27:06)*

- **Q:** State the rule the instructor gave for a project's package list.
  **A:** Keep it to the bare minimum you need, instead of installing everything. *(00:27:38)*

- **Q:** List the two problems the instructor named with installing far more packages than you use.
  **A:** It wastes disk space. Packages also have different update cycles, so updating everything can leave you unable to install it all. *(00:28:04)*

- **Q:** Name the two kinds of chips the instructor said Windows machines now come with.
  **A:** ARM and Intel. *(00:28:53)*

- **Q:** Quote the phrase the instructor said doesn't really work when a teammate can't run your code.
  **A:** "This works on my machine." *(00:29:39)*

- **Q:** State the two things the instructor said the course's tooling is about.
  **A:** Creating a stable computing environment, and building modular data science pipelines. *(00:29:55)*

## 8. What a container is ([27.2 What is a container?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#what-is-a-container))

*00:30:13–00:34:28*

- **Q:** Which two tools from DSCI 521 did the instructor say already handle keeping packages consistent?
  **A:** `uv` and `renv`. *(00:30:13)*

- **Q:** What does a `uv` lock file let someone else do, according to the instructor?
  **A:** At least install the same Python packages. *(00:30:40)*

- **Q:** Define a container in the instructor's words.
  **A:** A virtual computer built from scratch and given to everyone, so you all do your work on the same computer even on different physical machines. *(00:31:49)*

- **Q:** Name the workflow the instructor said containers make possible across a laptop and a bigger machine.
  **A:** Doing prototype work locally, then running on a bigger machine that has access to all the data, with exactly the same compute environment. *(00:32:15)*

- **Q:** State the cost of using a container that the instructor mentioned.
  **A:** A performance hit, because there is an extra layer on top. *(00:32:34)*

- **Q:** What happens if you mess up a container used as a sandbox?
  **A:** You restart it and get a new sandbox. *(00:33:05)*

- **Q:** Besides Docker, name the container tools the instructor listed.
  **A:** LXC, LXD and Podman. He added that Amazon probably has its own. *(00:34:01)*

- **Q:** What did the instructor say a cloud provider such as Google gives you when you get an "instance"?
  **A:** A container on one of their servers, not an actual machine. Pretty much all cloud compute runs on some version of containers. *(00:33:30)*

## 9. Containers versus virtual machines ([27.3 Contrasting containers with virtual machines](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#contrasting-containers-with-virtual-machines))

*00:34:31–00:36:40*

- **Q:** Define a virtual machine as the instructor described it.
  **A:** A full-blown operating system, such as all of Windows, that you log into with all its buttons and graphical interface. *(00:34:48)*

- **Q:** What does a container typically not have, compared with a virtual machine?
  **A:** A graphical interface. It holds only the bare minimum set of things you install. *(00:35:00)*

- **Q:** How much disk space did the instructor say a Windows virtual machine takes, and how large are the containers used in class?
  **A:** A Windows virtual machine takes about 50 to 80 GB. The containers used in class are less than two gigabytes, or even less than one. *(00:36:16)*

- **Q:** List the three resources in which the instructor said containers are lighter than virtual machines.
  **A:** Disk space, memory usage and compute usage. *(00:36:32)*

- **Q:** What does the instructor still use virtual machines for?
  **A:** Testing the MDS installation instructions, where he has to pretend to be on a Windows machine. *(00:36:01)*

## 10. Pulling and running a container: R 4.3.2 beside local R ([28.1.1 Launch and run containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#launch-and-run-containers))

*00:36:40–00:45:01*

- **Q:** Name the command the instructor used to download the R 4.3.2 container image.
  **A:** `docker pull rocker/r-ver:4.3.2`. *(00:36:55)*

- **Q:** What is `rocker`, and what is installed in its `r-ver` machines?
  **A:** An organization that builds container machines, and these only have R installed. *(00:37:22)*

- **Q:** Which version of R did `R --version` report on the instructor's laptop?
  **A:** R 4.6.2. *(00:37:32)*

- **Q:** What did `docker pull rocker/r-ver:4.3.2` print when the image was already on the laptop?
  **A:** A `Digest: sha256:...` hash and "Status: Image is up to date for rocker/r-ver:4.3.2". *(00:39:47)*

- **Q:** Name the industry the instructor gave as a real use case for keeping an old R version for years.
  **A:** Pharmaceutical companies, for clinical trials research, where the regulator wants your code and the full compute environment. *(00:37:58)*

- **Q:** How often does R release an update, according to the instructor?
  **A:** Every six months. *(00:38:10)*

- **Q:** What example did the instructor give of a system tool, rather than a package, that a container can pin?
  **A:** Git. A container with a Git version from 2019 would prevent anyone from running `git switch`. *(00:39:02)*

- **Q:** Which Git command did the instructor say `docker pull` resembles?
  **A:** `git pull`, because both pull something onto your computer. *(00:40:33)*

- **Q:** Name the command that started R 4.3.2 in a container in class.
  **A:** `docker run --rm -it rocker/r-ver:4.3.2`. *(00:40:38)*

- **Q:** What does the `--rm` flag of `docker run` do?
  **A:** It deletes the container when you turn it off. Otherwise you have to delete it manually. *(00:40:55)*

- **Q:** State what a double dash and a single dash mean in front of a command-line flag.
  **A:** A double dash marks a flag that is multiple letters long. A single dash marks single-letter flags, which can be chained together. *(00:41:20)*

- **Q:** State what each letter in `ls -alh` stands for, as given in class.
  **A:** `a` for all, `l` for list, and `h` for human-readable sizes. *(00:41:20)*

- **Q:** What do the `-i` and `-t` in `docker run -it` stand for?
  **A:** `-i` is interactive, and `-t` stands for TTY, which gives you a terminal you can interact with. *(00:41:48)*

- **Q:** What does `docker run` do if the image you name is not on your computer yet?
  **A:** It downloads the image first. *(00:42:16)*

- **Q:** What do you type to start R in a terminal?
  **A:** A capital letter `R`. *(00:42:38)*

- **Q:** Quote the error that `library(tidyverse)` gave inside the `rocker/r-ver:4.3.2` container.
  **A:** "there is no package called ‘tidyverse’". *(00:43:49)*

## 11. Know which machine you are typing on

*00:45:01–00:46:44*

- **Q:** What did the instructor call the main visual cue for knowing which machine you are typing on?
  **A:** Your terminal prompt. *(00:45:04)*

- **Q:** Where was the remote computer whose terminal the instructor showed in class?
  **A:** In his closet at home. *(00:45:48)*

- **Q:** What warning did the instructor give about working in containers and on remote machines?
  **A:** Sometimes you are given nothing but a blinking cursor, so you must know where you are typing and check you're on the machine you think you are. *(00:46:08)*

- **Q:** Which command did the instructor recall from DSCI 521 for checking which machine you're on, and what does it report?
  **A:** `whoami`, which reports the username on that computer. *(00:46:08)*

## 12. Why so many data science tools run in a browser

*00:46:44–00:49:11*

- **Q:** Name the framework the instructor said shows up constantly in how applications are built.
  **A:** Electron, an application that runs in a browser: they made the browser the application. *(00:47:39)*

- **Q:** For what kind of machine did the instructor say Jupyter Lab was designed?
  **A:** A remote container that can have far more cores and memory than your laptop, while keeping the same browser interface. *(00:48:04)*

- **Q:** How did the instructor describe VS Code?
  **A:** As essentially a giant browser application, which can also run in a container or in a browser. *(00:48:33)*

- **Q:** Which GitHub button gives you VS Code in a browser?
  **A:** The Codespaces button. *(00:48:49)*

## 13. Running RStudio in a container and mapping ports ([28.1.3 Mapping ports to containers with web apps](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#mapping-ports-to-containers-with-web-apps))

*00:54:10–00:58:59*

- **Q:** Name the image the instructor used to run RStudio in a container.
  **A:** `rocker/rstudio:4.4.2`. *(00:55:06)*

- **Q:** What warning did the instructor give about running containers without `--rm`?
  **A:** Each running container takes up RAM, so you can end up with five computers running and a computer that stops working. *(00:55:24)*

- **Q:** Which port does RStudio use inside the container?
  **A:** `8787`. *(00:55:56)*

- **Q:** How did the instructor describe the port numbers that tools choose?
  **A:** As very arbitrary: you can pick whatever you want, and 8787 is just the number RStudio picked. *(00:56:19)*

- **Q:** In `-p 8787:8787`, which number is the port on your computer and which is the port in the container?
  **A:** The left number is the port on your local computer, and the right number is the port inside the container. *(00:57:05)*

- **Q:** How did the instructor say you can run two RStudio containers at the same time?
  **A:** Map each one to a different port on your machine. *(00:56:38)*

- **Q:** Name the full command that started RStudio in a container in class, before a password was set.
  **A:** `docker run --rm -p 8787:8787 rocker/rstudio:4.4.2`. *(00:57:42)*

- **Q:** What address did the instructor type in the browser to reach RStudio running in the container?
  **A:** `localhost:8787`. *(00:57:51)*

- **Q:** What did the RStudio container's startup output print about passwords?
  **A:** A generated password ("The password is set to ooph3Aef2Ohcahcu"), followed by a note that you can set your own with the `PASSWORD` environment variable. *(00:57:51)*

- **Q:** What username logs in to the `rocker/rstudio` container?
  **A:** `rstudio`. *(00:58:29)*

- **Q:** Which R versions ran in RStudio desktop on the laptop and in the `rocker/rstudio:4.4.2` container?
  **A:** The desktop ran R 4.6.2 and the container ran R 4.4.2, which also differs from the 4.3.2 `r-ver` container. *(00:58:51)*

## 14. Passing environment variables into a container ([27.2 What is a container?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#what-is-a-container))

*00:59:20–01:02:53*

- **Q:** Which `docker run` flag passes an environment variable into a container?
  **A:** `-e`. *(01:00:05)*

- **Q:** Name the environment variable that sets the login password in the `rocker/rstudio` container.
  **A:** `PASSWORD`, in all caps. *(01:00:05)*

- **Q:** Name the full command the instructor used to run RStudio with a password he chose.
  **A:** `docker run --rm -p 8787:8787 -e PASSWORD="apassword" rocker/rstudio:4.4.2`. *(01:00:39)*

- **Q:** Do all containers accept the same environment variables?
  **A:** No. It depends on how the container was set up, and not every container has these. *(00:59:45)*

- **Q:** Who did the instructor say can reach the RStudio running on his `8787` port?
  **A:** Only someone with access to his physical machine. If you can't log into his machine, `8787` is not available to you. *(01:00:16)*

- **Q:** For which later MDS course and kind of app did the instructor say you can hand people a container to run?
  **A:** DSCI 532, where you put your dashboard code in a container that anyone with Docker can run and open at its port. *(01:01:47)*

## 15. Starting from a base image and working inside it ([28.1.4 Changing the containers default command](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#changing-the-containers-default-command))

*01:03:00–01:08:19*

- **Q:** What must you still choose first when you build your own container?
  **A:** A starting machine, which can be someone else's container, such as the `rocker/r-ver` image that already has R installed. *(01:03:51)*

- **Q:** Name the command that opened a shell, instead of R, in the R 4.6.2 container.
  **A:** `docker run --rm -it rocker/r-ver:4.6.2 bash`. *(01:04:44)*

- **Q:** What does the `rocker/r-ver` container run by default when it starts, without a command after the image name?
  **A:** R: the R prompt comes up. *(01:05:20)*

- **Q:** What did the prompt look like inside the `rocker/r-ver:4.6.2` container started with `bash`?
  **A:** `root@` followed by the container's ID and `:/#`, for example `root@95765251a970:/#`. *(01:04:53)*

- **Q:** What did the instructor say you should do with install steps that work when tried by hand in a container?
  **A:** Start documenting them, so you have the instructions for building the machine from scratch. *(01:05:48)*

- **Q:** What does the R package `cowsay` do?
  **A:** It draws ASCII art of a cow saying some text. *(01:06:08)*

- **Q:** Why did the instructor not install tidyverse in the demo container?
  **A:** Because it is a super long install. *(01:06:03)*

- **Q:** Name the two dependencies that `install.packages("cowsay")` also installed in the container.
  **A:** `crayon` and `rlang`. *(01:06:15)*

- **Q:** Name the R call that drew the cow saying hello inside the container.
  **A:** `cowsay::say('hello')`. *(01:06:41)*

- **Q:** What happened to `library(cowsay)` after the instructor exited the container and started it again?
  **A:** It failed with "there is no package called ‘cowsay’": the package was gone. *(01:07:04)*

- **Q:** Does a container keep a saved state between runs?
  **A:** No. When you turn it back on, it resets to how it was set up. *(01:08:11)*

- **Q:** How long did the instructor say tidyverse can take to install on a Linux machine that isn't set up right?
  **A:** About 15 minutes, which is painful when the project itself runs in 30 seconds. *(01:08:19)*

## 16. Running R from the command line with `Rscript -e` ([29.1.2 Build your first image](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#build-your-first-image))

*01:08:19–01:10:18*

- **Q:** What did the instructor say saving an install step comes down to?
  **A:** Whether you know the terminal command you need to write to make it happen. *(01:08:54)*

- **Q:** Name the command that lets R run code from the terminal.
  **A:** `Rscript`. *(01:09:23)*

- **Q:** What does the `-e` in `Rscript -e` stand for?
  **A:** Expression: you are giving it an R expression to run. *(01:09:27)*

- **Q:** Name the command that installed `cowsay` from the container's shell.
  **A:** `Rscript -e "install.packages('cowsay')"`. *(01:09:47)*

- **Q:** Which quotes go on the outside and which on the inside in `Rscript -e "install.packages('cowsay')"`?
  **A:** Double quotes on the outside and single quotes on the inside. *(01:09:41)*

## 17. The `Dockerfile`: `FROM`, `RUN`, `CMD` ([29.2 `Dockerfile` command summary](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#dockerfile-command-summary))

*01:10:18–01:15:01*

- **Q:** Name the special file that holds the instructions for setting up a container, and state its naming convention.
  **A:** `Dockerfile`, which begins with a capital D. *(01:10:22)*

- **Q:** Which instruction is normally the first line of a `Dockerfile`, and what does it name?
  **A:** `FROM`, in all caps, which names the starting-point machine. *(01:11:17)*

- **Q:** Quote the `FROM` line of the `Dockerfile` written in class.
  **A:** `FROM rocker/r-ver:4.6.2`. *(01:11:30)*

- **Q:** What did the instructor say about starting from an even smaller base image?
  **A:** There are bare-minimum Linux containers, but then you have to install every single thing by hand. *(01:11:49)*

- **Q:** What does the `RUN` instruction in a `Dockerfile` hold?
  **A:** The bash commands the container runs during the build process. *(01:12:44)*

- **Q:** Quote the `RUN` line of the `Dockerfile` written in class.
  **A:** `RUN Rscript -e "install.packages('cowsay')"`. *(01:12:52)*

- **Q:** Which `Dockerfile` instruction did the instructor say is pretty rare, compared with `CMD`?
  **A:** `ENTRYPOINT`. *(01:13:36)*

- **Q:** How is a `CMD` instruction written, compared with a normal bash command?
  **A:** As a list of terms instead of words separated by spaces. *(01:13:40)*

- **Q:** What does `CMD` set in a `Dockerfile`?
  **A:** The default last thing the machine runs when it starts, which you can override by giving another command such as `bash`. *(01:14:05)*

- **Q:** Quote the message the class's `CMD` line makes the cow say.
  **A:** "Hello from my first image!" *(01:13:52)*

- **Q:** For a Python project, what did the instructor say the `Dockerfile` would do to install packages?
  **A:** Install `uv`, copy in the lock files with a copy command, and run `uv sync`. *(01:14:15)*

- **Q:** Name the tool, besides your language and packages, that your project container will have to install next week.
  **A:** Quarto, which is not installed on the machine. *(01:14:40)*

## 18. Building and running your own image ([29.1.2 Build your first image](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#build-your-first-image))

*01:15:01–01:18:44*

- **Q:** Name the command the class used to build its first image.
  **A:** `docker build --tag hello-cowsay .`. *(01:15:11)*

- **Q:** What does the `.` at the end of `docker build --tag hello-cowsay .` mean?
  **A:** The current directory, where Docker should look for the `Dockerfile`. *(01:15:38)*

- **Q:** Which file does `docker build` look for by default?
  **A:** A file named exactly `Dockerfile`, with a capital D. *(01:15:38)*

- **Q:** From which directory are milestone commands assumed to be run?
  **A:** The root of the repository, so commands can be copy-pasted without changing directories. *(01:16:11)*

- **Q:** What full image name did the `docker build --tag hello-cowsay .` output say it was naming the image?
  **A:** `docker.io/library/hello-cowsay:latest`. *(01:16:39)*

- **Q:** Which command lists every image on your computer?
  **A:** `docker images`. *(01:17:01)*

- **Q:** How much disk usage did `docker images` report for `hello-cowsay:latest`?
  **A:** 1.45GB. *(01:17:01)*

- **Q:** Name the command that ran the new image, and state what it printed.
  **A:** `docker run --rm -it hello-cowsay`, which printed an ASCII cow saying "Hello from my first image!" *(01:17:14)*

- **Q:** Name the command that opened a shell inside the `hello-cowsay` image.
  **A:** `docker run --rm -it hello-cowsay bash`. *(01:17:28)*

- **Q:** What happened when the instructor ran `library(cowsay)` in R inside the `hello-cowsay` image?
  **A:** It loaded, because the build had installed the package. *(01:17:52)*

- **Q:** List the kinds of instructions the instructor said fill the middle of a typical `Dockerfile`.
  **A:** Many `RUN` and copy commands, and port commands where relevant, such as opening `8787`. *(01:18:07)*

## 19. Pinning versions, and what comes next

*01:18:44–01:20:39*

- **Q:** Do you need to build containers for this week's lab assignment?
  **A:** No, this week's lab doesn't need it. You need it for next week. *(01:18:48)*

- **Q:** What did the instructor say goes in the placeholder section of a project `Dockerfile`?
  **A:** Your `renv` setup, which installs, snapshots and loads the packages, or the equivalent for Python. *(01:19:02)*

- **Q:** What failure did the instructor recall from another of his classes a few weeks earlier?
  **A:** He restarted a container without hard-pinned versions, something had updated the day before, and nothing worked. *(01:19:55)*

- **Q:** How long does a pinned version stay the same in a `Dockerfile`?
  **A:** Until you update that install line yourself. *(01:20:27)*

- **Q:** What container topic did the instructor say comes next week?
  **A:** More on containers, including how to string multiple containers together. *(01:20:39)*

---

- prompt: prompt-recall-1-remember.md @ 8bcc190
- prompt-hash: cbbf92455214
- model: claude-opus-5-5 (requested: opus)
- backend: claude
- inputs: transcript-plaud.md, history.txt, terminal.txt, materials.md, notes-class-main--claude-opus-5-5.md
- generated: 2026-11-20
- notes-input: notes-class-main--claude-opus-5-5.md @ 1c708a29f65f, links and section references removed
