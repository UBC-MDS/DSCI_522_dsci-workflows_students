# Git pull requests and an introduction to Docker containers: review questions, tier 3 — Apply

Date: 2026-11-19

Instructor: Daniel Chen

*Tier 3 of 5: Apply. Work each situation through before you read the answer; tiers 1 (Remember) and 2 (Understand) cover the facts and reasons it relies on.*

## 1. Project advice: keep the analysis simple

*00:01:41–00:05:57*

- **Q:** Your group is planning its project and a teammate wants to fit a neural net, though a straight line would describe the data. Which model do you choose, and why?
  **A:** Fit the straight line model. This is a workflows course, not a model fitting course, and an ambitious model will eat the time the workflow work needs. As the warning goes, "You're going to have a very bad time in about two weeks" if you go for the neural net. *(00:02:16)*

- **Q:** Your project's outcome is a numeric quantity, and your group proposes logistic regression because it is simple. Will simplicity save you here?
  **A:** No. Simple models are not penalised, but the technique still has to be correct. Fitting logistic regression to predict a numeric outcome is just wrong, so choose a model that suits a numeric outcome, such as linear regression. *(00:05:24)*

- **Q:** Your simple, correctly fitted model reaches only about 60% accuracy, and you are tempted to keep tuning it before you move on. What should you do?
  **A:** Move on. The results of the model do not matter, as long as the data science and machine learning techniques are technically correct. The time belongs to the workflow parts of the project. *(00:03:08)*

- **Q:** You want the group project to double as a portfolio piece with a more elaborate analysis. How do you handle that?
  **A:** Don't do it in this assignment. If you really want the portfolio version, build it separately and in parallel, because this class has a lot happening and a complicated report would get in the way. *(00:03:27)*

## 2. Git review: working on a branch

*00:06:16–00:09:50*

- **Q:** In the `2026-11-19-docker` repository you have added a line to `README.md`, and `git status` says `On branch main`. You haven't committed anything yet. How do you get this work onto a new branch called `today`?
  **A:** Run `git switch -c today`. Nothing has been committed, so the uncommitted edit comes with you to the new branch. `git status` then shows `On branch today` with `README.md` still modified. *(00:08:57)*

- **Q:** You realise you have already made commits on `main` that should have been on a branch. Where do you turn?
  **A:** The textbook has a cheat sheet with a set of commands for moving those commits onto a branch. Avoid this situation by checking your branch before you commit. *(00:07:44)*

- **Q:** You are on branch `today` with an edited `README.md`. In order, which commands review the change, commit it and send the branch to GitHub?
  **A:** Run `git diff` to review the added line, then `git add README.md`, then `git commit -m "today we are talking about containers"`, then `git push origin today`. The push output gives a link for creating a pull request for `today` on GitHub. *(00:09:25)*

- **Q:** You and your teammates are all actively working on the project, and you are about to start a new change. What do you run first, and why?
  **A:** Pull the main branch with `git pull origin main`, so that everything is up to date. Otherwise you may be making changes to something that is out of date. *(00:08:27)*

- **Q:** You are working in a branch workflow and are about to run `git add`, then `git commit`. What do you check right before each one?
  **A:** Check which branch you are on, for example with `git status`. With several people working on several branches, committing on the wrong branch is the common mistake. Check before `add`, and definitely before `commit`. *(00:08:08)*

## 3. GitHub issues as a project board

*00:09:50–00:16:17*

- **Q:** Your repository has issue #1 and issue #2, and nothing else. You now open a pull request. What number will it get?
  **A:** Number 3. Issues and pull requests share one counter on GitHub; they are not counted separately. *(00:12:07)*

- **Q:** While writing issue #2, you type "meeting from #1". What happens on issue #1?
  **A:** The `#1` becomes a link to issue #1, and issue #1 automatically shows a reference back to issue #2. The reference works in both directions, so related items link to each other without extra work. *(00:13:34)*

- **Q:** Your lab asks for three issues, and one pull request ends up dealing with all three. Do you need to split the work into three branches and three pull requests?
  **A:** No. One issue, one branch, one pull request is only one extreme. It is fine for a single pull request to deal with all three issues; the point is to get experience with the project board. *(00:14:23)*

- **Q:** You open a pull request and want a teammate to look over your work before it is merged. Who goes where in the pull request's sidebar?
  **A:** Assign yourself, since it is your pull request and you are claiming it. Add your teammate in the separate reviewer section. Some projects block changes until someone has actually reviewed the work. *(00:14:47)*

- **Q:** Halfway through a task you have a stray idea, such as trying a neural net later, that you don't want to lose. What do you do with it?
  **A:** File it as an issue. The issues board is a good place to dump ideas and stretch goals. You can even ask a coding agent to file the issue, so you don't have to switch to a browser and lose track. *(00:13:24)*

- **Q:** Your group keeps meeting notes in an issue, and the meeting produces action items for different people. How do you track them?
  **A:** Write the action items in the notes issue, then create a separate issue for each one, spawned out of the notes issue and referencing it. Each issue documents who is responsible for what. *(00:11:14)*

## 4. Pull request descriptions, checkboxes and closing keywords

*00:16:17–00:22:18*

- **Q:** Your pull request #3 resolves issue #2. What do you write so the issue closes itself, and when does it close?
  **A:** Write a sentence such as `fixes #2` in the pull request's description. When the pull request is merged, GitHub closes issue #2 automatically. This is a GitHub feature, not a feature of Git. *(00:19:30)*

- **Q:** One pull request resolves three of your issues. How do you avoid going back and closing each issue by hand?
  **A:** Write the message strategically: put a closing keyword with each issue number, such as `fixes #N`, in the pull request description. Merging the pull request then closes all three, and your issues tab gets smaller without any extra clicks. *(00:21:02)*

- **Q:** You put `fixes #2` in a commit message instead of the pull request description. Will that work, and is it a good choice?
  **A:** It can work in a commit message, but it is harder to see there. Writing it in the pull request message makes it visible to everyone reviewing the work. *(00:19:55)*

- **Q:** You wrote `closes #1 fixes #2` in pull request #3 and you are unsure which keyword to rely on. Which one do you choose?
  **A:** Both `closes` and `fixes` are closing keywords. `fixes` is the one to rely on, because it is the one used almost all the time. The demo repository shows issues #1 and #2 both closed by #3. *(00:19:55)*

- **Q:** Your pull request is open but not finished, and you want teammates to see what is left to do. What can you put in it?
  **A:** Add Markdown checkboxes such as `- [ ] item 1` to the description, and check them off as you go. Unchecked boxes show teammates the work isn't done yet. You can also use these in addition to, or instead of, the draft button. *(00:17:49)*

- **Q:** A big decision is made halfway down the comment thread of your pull request. Where should that decision end up?
  **A:** Edit it into the first comment. Readers want to know what is happening and why the item exists from the top, not by reading the whole conversation. The first comment is editable because it evolves over time. *(00:16:56)*

- **Q:** Your group's project ends with several stretch-goal issues still open. Is that a problem for grading?
  **A:** No. Issues don't all need to be closed by the end; that is not what is graded. Creating issues for longer-term ideas is fine practice. *(00:21:50)*

## 5. Cleaning up after a merge

*00:22:18–00:25:19*

- **Q:** Pull request #3 from `today` has just been merged on GitHub, and locally you are still on `today`. What do you run to bring your local `main` up to date?
  **A:** Run `git switch main`, then `git pull origin main`. The pull fast-forwards `main` to the merge commit made on GitHub. *(00:22:25)*

- **Q:** You want to delete the merged `today` branch on GitHub, but you have already left the pull request page. Where can you delete it?
  **A:** Go to the branches view, find `today` (it shows pull request #3 as merged), and click the trash can. From the pull request page itself, you can use the delete-branch button that appears after merging. *(00:22:53)*

- **Q:** You have deleted `today` on GitHub, but `git log --oneline --graph --all` still shows `(origin/today, today)` next to commit `3c6d82a`. What do you run to drop the remote reference?
  **A:** Run `git fetch --prune`. It removes the `origin/today` reference to the branch that no longer exists on GitHub, so afterwards the commit is labelled `(today)` only. *(00:24:30)*

- **Q:** After `git fetch --prune`, commit `3c6d82a` is still labelled `(today)`. How do you remove that label, and what does the graph look like afterwards?
  **A:** Run `git branch -d today` to delete the local branch. The graph still shows `3c6d82a` and the merge commit `d25ddfa`, but `3c6d82a` has no label. You lose only the shortcut name, not the history. *(00:24:30)*

- **Q:** You expect to return to a merged branch's commit often and would rather not type its hash. What do you do?
  **A:** Keep the branch instead of deleting it, so that `git switch today` works instead of switching to `3c6d82a`. Deleting branches is optional in this course, and you may keep them as a record. *(00:25:05)*

## 6. What a container is ([27.2 What is a container?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#what-is-a-container))

*00:30:13–00:34:28*

- **Q:** You give a collaborator your `uv.lock` file, but they don't use `uv` and worry that installing it will disturb how their computer is set up. What do you give them instead?
  **A:** Give them a container: a virtual computer built from scratch with everything installed. They do their work on that virtual computer, so everyone effectively shares the same computer, even on different physical machines. *(00:31:17)*

- **Q:** You prototype on your laptop, but the full analysis must run on a bigger machine that holds all the data. How do you make sure both machines have exactly the same compute environment?
  **A:** Run the analysis in the same container on both machines. Expect a small performance hit from the extra layer; there is no way around that. *(00:32:15)*

- **Q:** The administrators of a remote server won't let you install Python on it directly. How can you still run your analysis there?
  **A:** Use a container. The administrators can give you a sandbox to play in without you installing software on the machine itself. If you mess it up, it is restarted and you get a fresh sandbox. *(00:32:34)*

## 7. Containers versus virtual machines ([27.3 Contrasting containers with virtual machines](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#contrasting-containers-with-virtual-machines))

*00:34:31–00:36:40*

- **Q:** You need to share your analysis environment with your group, and you are choosing between a virtual machine and a container. Which do you pick?
  **A:** A container. A Windows virtual machine can take 50–80 GB, while a container can run a full computational stack in less than two gigabytes. Containers are lighter on disk, memory and compute. *(00:36:16)*

- **Q:** On your Mac, you need to check that installation instructions work for Windows users, including the Windows graphical interface. Which tool fits?
  **A:** A virtual machine. It runs a full-blown operating system such as Windows, with all its buttons and windows, so you can test as if you were on a Windows machine. *(00:36:01)*

- **Q:** You open a shell in a container and want to browse its folders. How do you get around?
  **A:** Type commands such as `cd` and `ls`. A container is stripped down and typically has no graphical interface, so you can't double-click through a folder structure. *(00:35:00)*

## 8. Pulling and running a container: R 4.3.2 beside local R ([28.1.1 Launch and run containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#launch-and-run-containers))

*00:36:40–00:45:01*

- **Q:** You already downloaded `rocker/r-ver:4.3.2` before class and run `docker pull rocker/r-ver:4.3.2` again. What do you expect to see?
  **A:** Docker checks the registry, prints a `Digest: sha256:...` line, and reports `Status: Image is up to date for rocker/r-ver:4.3.2`. If a newer version had been published, the pull would download it. *(00:39:51)*

- **Q:** `R --version` on your laptop reports R 4.6.2. You run `docker run --rm -it rocker/r-ver:4.3.2`. Which R do you get?
  **A:** R 4.3.2 starts, running inside the container, not the R on your laptop. You can have both versions at once, because the container is effectively a different machine. *(00:42:38)*

- **Q:** Inside the `rocker/r-ver:4.3.2` container, you run `library(tidyverse)`, which works fine in R on your laptop. What happens?
  **A:** It fails with `there is no package called 'tidyverse'`. The image has only R installed, and nothing has told it to install tidyverse. *(00:43:49)*

- **Q:** You run `docker run` with an image name you have never pulled. What does Docker do?
  **A:** It downloads the image first and then runs it. Pulling ahead of time just saves waiting at the moment you run it. *(00:42:16)*

- **Q:** You start a container with `docker run -it rocker/r-ver:4.3.2`, leaving out `--rm`. What happens to the container when you quit?
  **A:** It isn't deleted, so you have to delete it manually. With `--rm`, the container is removed automatically when it stops. *(00:40:55)*

- **Q:** You want to type commands at R's prompt inside the container. Which flags make that possible, and what does each one do?
  **A:** Use `-it`, which is two single-letter flags chained together. `-i` makes the session interactive, so what you type goes in, and `-t` gives you a terminal (TTY) to interact with. *(00:41:48)*

- **Q:** Your multi-year clinical trial analysis must be reproducible for a regulator, while R updates every six months. Your `renv` lock file pins the packages. What else do you hand over?
  **A:** The container that ran the full analysis, which fixes the version of R itself. Lock files only track packages, not the tools installed on the system. *(00:38:46)*

- **Q:** You want everyone on a project to use an old version of Git, so that nobody can run `git switch`. How could you enforce that?
  **A:** Give everyone a container with that version of Git installed, for example one from 2019. A container pins system tools like Git, not only the packages that a lock file covers. *(00:39:02)*

## 9. Know which machine you are typing on

*00:45:01–00:46:44*

- **Q:** You type `q()` in R inside a container, and the prompt now reads `dan@Heartsbane 2026-11-19-docker %`. Where are your next commands going to run?
  **A:** On your own laptop. The prompt is back to your computer's own prompt, and that prompt is your visual cue for which machine you are on. *(00:45:04)*

- **Q:** Your prompt reads `root@95765251a970:/#`. Are you on your laptop?
  **A:** No. You are in a shell inside a container, whose prompt shows the `root` user and the container's ID. The prompt changes when you enter the container, which tells you where you are typing. *(01:05:20)*

- **Q:** You connect to a remote machine and are given little more than a blinking cursor. How do you confirm you are on the machine you think you are?
  **A:** Read the prompt for the machine's name and run `whoami`, which reports your username on that computer. Check before running commands, because sometimes these are the only cues you have. *(00:46:08)*

## 10. Running RStudio in a container and mapping ports ([28.1.3 Mapping ports to containers with web apps](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#mapping-ports-to-containers-with-web-apps))

*00:54:10–00:58:59*

- **Q:** You want RStudio Server from `rocker/rstudio:4.4.2` in your browser. What do you run, and how do you log in?
  **A:** Run `docker run --rm -p 8787:8787 rocker/rstudio:4.4.2`, then go to `localhost:8787`. The username is `rstudio`, and the password is the generated one printed in the start-up output. *(00:57:42)*

- **Q:** One RStudio container is already using port 8787 on your laptop, and you want to start a second one. What do you change in the `-p` flag?
  **A:** Change the left number, which is the port on your machine, and keep the right number at `8787`, the port inside the container. Both containers then run side by side on different host ports. *(00:56:38)*

- **Q:** You have been starting containers all afternoon and your laptop has become sluggish. What is the likely cause, and how do you prevent it?
  **A:** Each running container takes up RAM, so you may have "five computers" running at once. Use `--rm` so a container shuts down and is deleted when you exit it, and stop the ones you don't need. *(00:55:17)*

- **Q:** You press Ctrl+C in the terminal running your RStudio container, and it prints `[s6-finish] waiting for services.` without exiting. What do you do?
  **A:** Press Ctrl+C again. After repeated presses the log shows `got 3 SIGTERM/SIGINTs, forcefully exiting`. Because the container was started with `--rm`, it is still cleaned up. *(00:57:51)*

- **Q:** Your desktop RStudio uses R 4.6.2. You log into the RStudio Server from `rocker/rstudio:4.4.2`. Which R version does it run?
  **A:** R 4.4.2, the version installed in that container. It is effectively a different machine from both your laptop and the `rocker/r-ver:4.3.2` container. *(00:58:51)*

## 11. Passing environment variables into a container ([27.2 What is a container?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#what-is-a-container))

*00:59:20–01:02:53*

- **Q:** The generated RStudio password, such as `ooph3Aef2Ohcahcu`, is a pain to retype each time. How do you choose your own?
  **A:** Run `docker run --rm -p 8787:8787 -e PASSWORD="apassword" rocker/rstudio:4.4.2`, then log in at `localhost:8787` as `rstudio` with `apassword`. `-e` passes an environment variable into the container, and this image reads `PASSWORD`. *(01:00:05)*

- **Q:** You pass `-e PASSWORD=...` to a different image, and it has no effect. What went wrong?
  **A:** Environment variables are container-specific: a container uses only the variables it was built to read, and not every container has this one. Check that image's documentation for the variables it supports. *(01:01:08)*

- **Q:** Your `docker run` command shows the RStudio password in plain text on your screen. Is that a security problem?
  **A:** Not in this setting. The container's port is only reachable from your own machine, so someone who can't log into your laptop can't reach `localhost:8787`. *(01:00:28)*

- **Q:** You built a dashboard and want someone to run it without installing your language, `renv` and packages. How do you deliver it?
  **A:** Put the dashboard code in a container. Anyone with Docker can `docker run` it with the right flags and open the port in their browser. They skip the whole installation process because you have given them a computer you built from scratch. *(01:02:20)*

## 12. Starting from a base image and working inside it ([29.1.1 Workflow for building a Dockerfile](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#workflow-for-building-a-dockerfile))

*01:03:00–01:08:19*

- **Q:** You want a shell in `rocker/r-ver:4.6.2` to try install commands, but starting it drops you straight into R. How do you change that?
  **A:** Add `bash` after the image name: `docker run --rm -it rocker/r-ver:4.6.2 bash`. The image's default command, R, is replaced by a shell, and the prompt changes to the container's. You can still type `R` there to start R. *(01:05:20)*

- **Q:** You are choosing a starting machine for your own R container: `rocker/r-ver:4.6.2` or a bare-minimum Linux image. Which saves you work?
  **A:** `rocker/r-ver:4.6.2`. Whoever built it already installed R and the system pieces a new computer needs to run R, much like the compiler tools you installed on your laptop. A bare image means installing every single thing by hand. *(01:04:00)*

- **Q:** Inside a container started with `docker run --rm -it rocker/r-ver:4.6.2 bash`, you run `install.packages("cowsay")` in R and the cow appears. You exit, start the container again the same way, and run `library(cowsay)`. Predict the result.
  **A:** It fails with `there is no package called 'cowsay'`. A container has no saved state: each start resets to how its image was built, so anything installed by hand is gone. *(01:07:10)*

- **Q:** You want to experiment with risky Linux commands without endangering your laptop. Where do you do it?
  **A:** In a container. Even a command that deletes the whole computer only damages the container, and when you turn it back on it is as if you had never run that command. *(01:07:25)*

- **Q:** You are designing a container and aren't sure your install steps will work. In what order do you go?
  **A:** Go through the steps interactively in a shell inside the base image first. Once they work, document them as the instructions for building the machine from scratch. *(01:05:48)*

## 13. Running R from the command line with `Rscript -e` ([29.1.2 Build your first image](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#build-your-first-image))

*01:08:19–01:10:18*

- **Q:** You are at the Bash prompt in a `rocker/r-ver:4.6.2` container and want to install `cowsay` without opening R. What do you type?
  **A:** Type `Rscript -e "install.packages('cowsay')"`. `Rscript` runs R code from the terminal, and `-e` tells it you are giving it an R expression. *(01:09:27)*

- **Q:** You are writing the `Rscript -e` install command and need a quoted package name inside the quoted expression. How do you quote it?
  **A:** Use double quotes on the outside and single quotes on the inside: `"install.packages('cowsay')"`. Pay attention to the quotes, so the inner quotes don't end the outer string. *(01:09:41)*

- **Q:** You install `cowsay` with `Rscript -e` at a container's prompt, confirm `library(cowsay)` works, then exit and start a new container from the same image. Is `cowsay` there?
  **A:** No, it is gone again. Running the install from the shell doesn't change the image, so the command needs to be saved somewhere that rebuilds the machine. *(01:10:01)*

## 14. The `Dockerfile`: `FROM`, `RUN`, `CMD` ([29.2 `Dockerfile` command summary](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#dockerfile-command-summary))

*01:10:18–01:15:01*

- **Q:** You have confirmed that `Rscript -e "install.packages('cowsay')"` works at a container's prompt. How do you make that install permanent?
  **A:** Write it into a file named `Dockerfile` as a `RUN` line: `RUN Rscript -e "install.packages('cowsay')"`. `RUN` holds the bash commands the container runs during the build, so the package is part of every machine built from it. *(01:12:44)*

- **Q:** Write a `Dockerfile` that starts from R 4.6.2, installs `cowsay`, and by default prints a cow saying "Hello from my first image!".
  **A:** `FROM rocker/r-ver:4.6.2` comes first, naming the starting machine. Next is `RUN Rscript -e "install.packages('cowsay')"`, then `CMD ["Rscript", "-e", "cowsay::say('Hello from my first image!')"]`. `CMD` is written as a list rather than space-separated words, and it is the last thing the machine runs. *(01:13:40)*

- **Q:** Your image's `Dockerfile` ends with a `CMD` that prints the cow message. You start it with `docker run --rm -it hello-cowsay bash`. Does the `CMD` run?
  **A:** No. `CMD` is only the default, used when you don't give another command. Adding `bash` overrides it and gives you a shell instead. *(01:14:05)*

- **Q:** Your project is in Python and managed with `uv`. What goes between the `FROM` line and the `CMD` line of its `Dockerfile`?
  **A:** Commands that install `uv`, a `COPY` of your lock files into the image, and a `RUN` of `uv sync`. All the packages are then installed in the container, so the machine has your compute environment ready. *(01:14:15)*

## 15. Building and running your own image ([29.1.2 Build your first image](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#build-your-first-image))

*01:15:01–01:18:44*

- **Q:** You have just written the `Dockerfile` in the root of `2026-11-19-docker`. In order, what do you run to build an image named `hello-cowsay`, confirm it exists, and run it?
  **A:** Run `docker build --tag hello-cowsay .`, then `docker images`, which should list `hello-cowsay:latest`, then `docker run --rm -it hello-cowsay`. *(01:17:01)*

- **Q:** You type `docker build --tag hello-cowsay` and stop. What is missing, and what does it mean?
  **A:** The final `.`, which tells Docker where to look for the file named `Dockerfile`: the current directory. This may be the first time a lone dot is something you actually have to type. *(01:15:38)*

- **Q:** Your project's milestone instructions include `docker build --tag hello-cowsay .`, and a teammate runs it from a subfolder. Where should it be run?
  **A:** From the root of the repository, where the `Dockerfile` lives. The instructions assume every command runs from the root, so commands can be copy-pasted without changing directories. (You can give a full path to a `Dockerfile`, but this command assumes the root.) *(01:16:11)*

- **Q:** You run `docker run --rm -it hello-cowsay` with no extra command. What appears?
  **A:** An ASCII cow saying "Hello from my first image!". With no command given, the container runs the `CMD` line from the `Dockerfile`. *(01:17:14)*

- **Q:** You run `docker run --rm -it hello-cowsay bash`, start `R`, and run `library(cowsay)`. Predict the result, and contrast it with the bare `rocker/r-ver:4.6.2` image.
  **A:** It loads without error, because the `RUN` line installed `cowsay` when the image was built. In a fresh container from the base `rocker/r-ver:4.6.2` image, `library(cowsay)` fails. *(01:17:52)*

- **Q:** You add a new `RUN` line to your `Dockerfile`, then go straight to `docker run --rm -it hello-cowsay`, but the new software isn't there. What did you skip?
  **A:** Rebuilding the image with `docker build --tag hello-cowsay .`. The `Dockerfile` only holds the instructions: you must build the machine from them before turning it on. *(01:17:52)*

## 16. Pinning versions, and what comes next

*01:18:44–01:20:39*

- **Q:** Your project's analysis must still run on the same R version a year from now. Which line of your `Dockerfile` controls that, and how?
  **A:** The `FROM` line, for example `FROM rocker/r-ver:4.6.2`. The tag pins the version of R, so that part of the environment is now stable. *(01:18:53)*

- **Q:** Quarto 1.11 is current, but you want your project's container to stay on Quarto 1.10. How do you arrange that?
  **A:** Install that explicit version in the `Dockerfile`'s install command. As long as you don't change that line, the container stays on the same version a year from now. *(01:19:25)*

- **Q:** You restart a project container whose `Dockerfile` installs software without pinned versions, and suddenly nothing works. What most likely happened, and how do you prevent it?
  **A:** Something upstream updated, perhaps the day before, and the unpinned install pulled in the new version. Hard-pin your versions so nothing changes until you update that line yourself; otherwise you spend hours fixing an update instead of doing the work. *(01:19:55)*

---

- prompt: prompt-recall-3-apply.md @ 8bcc190
- prompt-hash: 068025368bc2
- model: claude-opus-5-5 (requested: opus)
- backend: claude
- inputs: transcript-plaud.md, history.txt, terminal.txt, materials.md, notes-class-main--claude-opus-5-5.md
- generated: 2026-11-20
- notes-input: notes-class-main--claude-opus-5-5.md @ 1c708a29f65f, links and section references removed
