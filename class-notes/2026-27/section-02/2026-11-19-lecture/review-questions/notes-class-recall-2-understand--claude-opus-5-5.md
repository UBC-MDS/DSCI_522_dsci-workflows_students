# Git issues and pull requests, then an introduction to Docker containers: review questions, tier 2 — Understand

Date: 2026-11-19

Instructor: Daniel Chen

*Tier 2 of 5: Understand. Explain each answer in your own words before you read it; tier 1 (Remember) covers the facts, tiers 3 to 5 put them to use.*

## 1. Project advice: keep the analysis simple

*00:01:41–00:05:57*

- **Q:** Explain why the instructor urged students to keep the group project's analysis simple, even if they could build something more ambitious.
    - **A:** An ambitious model, such as a neural net instead of a straight line, means "a very bad time in about two weeks." This is a workflows course, not a model-fitting course, and there is almost no machine learning code in the lectures. The report is not the point of the class, and there is a lot more work to do around it. *(00:02:16)*

- **Q:** Compare how the project treats a model's performance with how it treats its correctness.
    - **A:** Performance doesn't matter: a model that is sixty percent accurate is fine, and a simple linear or logistic regression is not penalised. The techniques must still be correct data science and correct machine learning. Fitting logistic regression to predict a numeric outcome, for example, "is just wrong." *(00:03:08)*

- **Q:** If the lectures show almost no machine learning code, why does the group project still need a machine learning analysis?
    - **A:** You need a machine learning project to start with. The project is the same analysis, built on over three or four weeks: Git this week, then containers next week. The analysis is what the workflow is applied to, even though class never teaches the modelling. *(00:05:43)*

- **Q:** Explain why a student who wants a portfolio piece should build it in parallel rather than in this assignment.
    - **A:** A lot is happening in this class, and the instructor said you definitely don't want to deal with a complicated report at the same time. If you want a portfolio version, do it separately, in parallel. *(00:03:27)*

## 2. Git review: working on a branch

*00:06:16–00:09:50*

- **Q:** The instructor edited `README.md` in the `2026-11-19-docker` repository while still on `main`. Why could he still move that work onto a new branch with `git switch -c today`?
    - **A:** He had only edited the file and had not committed anything yet. He could therefore create the branch at that point: `git status` then showed he was on branch `today` with the same modification. If you have already made commits on `main`, you need the textbook's cheat sheet of commands to move them. *(00:08:57)*

- **Q:** Why should you look at which branch you are on right before `git add`, and definitely before `git commit`?
    - **A:** The course assumes a branch workflow from now on, and the change is supposed to land on a branch, not on `main`. Checking `git status` before you stage and commit catches the mistake while it is still easy to fix. In the demo it showed the instructor was still on `main`. *(00:08:08)*

- **Q:** When you are actively collaborating, why pull the `main` branch before starting new work?
    - **A:** Pulling brings everything up to date, so you aren't working on and changing something that is out of date. With several people actively working on several branches, this is something you now have to pay attention to. *(00:08:27)*

## 3. GitHub issues as a project board

*00:09:50–00:16:17*

- **Q:** Explain why GitHub issues and pull requests share one numbering sequence. In the `2026-11-19-docker` demo, what number did the pull request get, and why?
    - **A:** Issues and pull requests are counted together so that, inside any issue or pull request, you can refer to any other item by its number. In the demo there were two issues first, so the pull request became #3. *(00:12:07)*

- **Q:** What does it mean that a `#` reference on GitHub is a "two-way reference"?
    - **A:** When you write something like "meeting from #1" in issue #2, it links to item 1, and item 1 also shows a link back. Everything links to everything else automatically. The instructor named this kind of issue and pull request tracking as one of the reasons GitHub, and not only Git, became so popular. *(00:13:34)*

- **Q:** How can an issue board serve as a team's meeting notes?
    - **A:** You can keep the meeting notes in one big issue, as MDS does in one of its internal repositories. After the meeting, any action items or to-dos for other people become separate issues spawned from that note. *(00:10:49)*

- **Q:** Why does the instructor sometimes ask a coding agent to file an issue for a passing idea?
    - **A:** Opening a browser tab risks ending up on a site he doesn't need to be on and losing track of what he was doing. Telling the agent to file the issue lets him throw the idea somewhere without breaking focus. Issues are a good place to dump ideas, such as a neural net someone would like to try later. *(00:13:06)*

- **Q:** What is the difference between assigning someone to a pull request and adding them as a reviewer?
    - **A:** You usually assign yourself to your own pull request, which claims it as your responsibility. A reviewer is someone else, such as a teammate, whom you ask to look over your work. In larger projects there are sometimes ways to block changes until someone has actually reviewed them. *(00:14:47)*

- **Q:** Why is it acceptable for one pull request to deal with all three issues the lab asks you to create?
    - **A:** One issue, one branch, one pull request is only one extreme; it isn't always how the work splits up. The lab's goal is for you to get experience with the project board system, not to match issues to pull requests one-for-one. *(00:14:23)*

- **Q:** Compare tracking a team's work in cross-referenced GitHub issues with keeping it in a shared Google Doc.
    - **A:** Issues and pull requests that reference each other keep all the notes and decisions connected to the work itself. You can see this in any large open-source project. The instructor called it a very good way to keep track of what is happening on your team without relying on a document of notes. *(00:15:48)*

## 4. Pull request descriptions, checkboxes and closing keywords

*00:16:17–00:22:18*

- **Q:** Why should the first comment of an issue or pull request be edited to stay up to date?
    - **A:** People coming to it won't read the whole conversation. They want to know what is happening and why the thing exists, and that should already be in the first comment. If a big decision is made later in the discussion, update the opening comment; project owners can usually edit others' comments too. These comments are editable because they evolve over time. *(00:16:56)*

- **Q:** How do Markdown checkboxes in a pull request description help you and your teammates?
    - **A:** They let you track for yourself what still needs doing as you fix things. They also tell teammates at a glance that the pull request isn't done yet, because not every box is checked. That makes them an alternative to marking the pull request as a draft. *(00:17:49)*

- **Q:** Explain how a closing keyword such as `fixes #2` in a pull request description closes an issue.
    - **A:** A sentence containing a keyword like `fixes #2` (or `closes #1`) declares that the pull request resolves that issue. When the pull request is merged, GitHub closes the referenced issue automatically. This is a GitHub feature, not a feature of Git, the version control system. The instructor wasn't sure `closes` had worked in the demo and said he almost always uses `fixes`. *(00:19:30)*

- **Q:** Closing keywords also work in commit messages. Why write them in the pull request description instead?
    - **A:** The instructor said you could put them in a commit message, but they are harder to see there. Writing the keyword in the pull request message makes it visible that this work deals with that issue. *(00:19:55)*

- **Q:** Why do closing keywords make the issues tab more useful as a project management tool?
    - **A:** As work merges, the issues it fixes close themselves, so the issues tab gets smaller and you don't have to think about those items again. You don't have to click "close" on several issues by hand. You just look down the list for the next thing to work on, which is how the instructor works on the textbook. *(00:20:12)*

- **Q:** Why is it fine to leave stretch-goal issues open at the end of the course?
    - **A:** The course does not grade you on closing all your issues. Creating issues for longer-term ideas or things you'd like to explore is good practice with the system, so open ones are fine. *(00:21:50)*

## 5. Cleaning up after a merge

*00:22:18–00:25:19*

- **Q:** After the `today` branch was deleted on GitHub, why did the instructor still run `git fetch --prune` and `git branch -d today` locally?
    - **A:** Deleting the branch on GitHub doesn't remove your local copies of the references, and `git log --oneline --graph --all` still showed them. `git fetch --prune` drops the reference to the branch that was deleted on GitHub (`origin/today`). `git branch -d today` deletes the local branch itself. *(00:24:30)*

- **Q:** When you delete a merged branch, what do you lose and what stays?
    - **A:** The history stays: the commit and the merge are still in the graph, so you can tell something happened there. What you lose is the quick shortcut name pointing to that location. *(00:24:30)*

- **Q:** Why do some people choose not to delete merged branches?
    - **A:** Deleting loses the reference. Keeping the branch name means you can type `git switch today` instead of `git switch 3c6d82a`. *(00:25:05)*

- **Q:** Why does the instructor sometimes clean up branches anyway?
    - **A:** You can end up in very weird Git states where there are so many branch colours and labels on the screen that you can't see what is happening anymore. Removing stale references makes the graph readable again. *(00:24:05)*

- **Q:** Why does the course not require you to delete branches after merging?
    - **A:** Keeping branches as a record is perfectly fine. Teams and companies handle Git very differently, even groups within the same company. The class shows one way, and other workflows are modifications of it. *(00:23:22)*

## 6. Why data science workflows need stable environments ([27.1 Documenting and loading dependencies](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#documenting-and-loading-dependencies))

*00:25:29–00:30:13*

- **Q:** How does setting up a project's environment differ from the homework you have done so far in MDS?
    - **A:** For homework you were given the package file. In a project, each group picks its own language and libraries (Python or R, and Altair, Plotly or Matplotlib), so the package requirements differ. You have to adapt the environment to your own project, just as every project at a company has different requirements. *(00:27:06)*

- **Q:** Why keep a project's package list to the bare minimum instead of installing everything?
    - **A:** Installing packages you don't use wastes disk space. Packages also have different update cycles, so if you later try to update everything in one go, some may be incompatible and you can end up unable to install them all. *(00:28:04)*

- **Q:** Explain why sharing a stable compute environment with a teammate is harder than keeping your own stable.
    - **A:** The teammate may have a different operating system, and even a different CPU chip: Macs and Windows machines differ, and Windows now ships on both ARM and Intel chips. Different architectures mean software gets installed in different ways. Your code has to run on a machine that isn't set up like yours at all. *(00:28:53)*

- **Q:** Why is "it works on my machine" not good enough for a data science project?
    - **A:** It doesn't help a teammate who is trying to do the same analysis and can't run your code. The goal of the course is a compute environment you can share, so everyone runs the code through that same environment. *(00:29:39)*

- **Q:** Why do data science pipelines need to be modular?
    - **A:** Other people might need different parts of your analysis, not just the final report. *(00:29:55)*

## 7. What a container is ([27.2 What is a container?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#what-is-a-container))

*00:30:13–00:34:28*

- **Q:** If you hand a teammate your `uv.lock` file, why might that still not be enough for them to run your analysis?
    - **A:** The lock file only lets them install the Python packages, and their computer may be set up differently from yours. They might not use `uv` at all. Installing it could mess up other things their computer is set up for. *(00:31:17)*

- **Q:** Explain the idea behind a container as the instructor described it.
    - **A:** Instead of handing over your physical computer, you build a virtual computer from scratch and give that to everyone. Everyone then does their work on that virtual computer. You are all effectively sharing the same computer even though you are on different physical machines. *(00:31:49)*

- **Q:** Why are containers useful when you prototype on your laptop but run the full analysis on a bigger machine?
    - **A:** The bigger machine has access to all the data, and the compute environment must be exactly the same on both. A container gives you that same environment on your laptop, on the other machine, and across multiple machines. *(00:32:15)*

- **Q:** Containers carry a performance cost. Why use them anyway on remote machines?
    - **A:** The extra layer causes an unavoidable performance hit. But you often can't install everything directly on a remote machine: other work may be running there, or the administrator doesn't trust you to install what you think you need. A container gives you a sandbox to play in, and if you mess it up, it is restarted and you get a new sandbox. *(00:32:34)*

- **Q:** How do containers relate to the "instances" offered by cloud providers?
    - **A:** Cloud providers such as Google typically don't give you bare access to an actual machine. They give you a container on one of their servers, and you work inside it. Pretty much all cloud compute runs on some version of containers. *(00:33:30)*

- **Q:** How does a container deal with the problem of software versions that cannot coexist on one computer?
    - **A:** A container is a little machine with everything it needs installed inside it. Two versions of the same software can live in separate containers even when they couldn't both be installed together on one machine. *(00:34:03)*

## 8. Containers versus virtual machines ([27.3 Contrasting containers with virtual machines](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#contrasting-containers-with-virtual-machines))

*00:34:31–00:36:40*

- **Q:** What is the main difference between a virtual machine and a container?
    - **A:** A virtual machine is a full-blown operating system, such as all of Windows, with its graphical interface and buttons. A container is a stripped-down version that typically has no graphical interface. It contains only the bare minimum that you install into it. *(00:35:33)*

- **Q:** Explain why containers perform better than virtual machines.
    - **A:** A container has less in it and no visual parts, so it uses fewer resources. A Windows virtual machine can take 50 to 80 GB. The containers used in class are under two gigabytes, or even under one, yet still run a full computational stack, using less disk, memory and compute. *(00:36:16)*

- **Q:** How does the container's lack of a graphical interface explain why DSCI 521 pushed you to work by typing commands in the terminal?
    - **A:** There will be many times, inside a container or on a remote machine, when the terminal is the only interface you have. You can't double-click through folders there. You have to type commands such as `cd` to get around. *(00:35:00)*

- **Q:** If containers are lighter, why does the instructor still use virtual machines?
    - **A:** He uses them to test the MDS installation instructions, where he has to pretend he is on a Windows machine. That situation needs a full operating system. *(00:36:01)*

## 9. Pulling and running a container: R 4.3.2 beside local R ([28.1.1 Launch and run containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#launch-and-run-containers))

*00:36:40–00:45:01*

- **Q:** The instructor's laptop has R 4.6.2. Why might someone need to run R 4.3.2 in a container?
    - **A:** Some work has to stay on one version of R for years. Clinical trials research at a pharmaceutical company can last several years, while R updates every six months, and you don't want to redo or recheck your work each time. Regulators reviewing a drug submission want your code and the whole compute environment so they can reproduce it, so you give them the container that ran the analysis. *(00:38:07)*

- **Q:** How does what a container pins differ from what the `uv` and `renv` lock files pin?
    - **A:** Lock files track only the package versions, not the tools installed on the system. A container goes one level deeper and fixes the tools themselves, such as R or Git. For example, a container with a 2019 version of Git would stop anyone from running `git switch`. *(00:39:02)*

- **Q:** When the instructor ran `docker pull rocker/r-ver:4.3.2` and the output said "Image is up to date," what did that mean?
    - **A:** He already had that image downloaded, and it matched the current version. If a newer version had been published, the pull would have downloaded it. The hash in the output identifies the exact version. *(00:39:51)*

- **Q:** Why is the command called `docker pull`, and what does the similarity to `git pull` tell you?
    - **A:** In both commands you are pulling something onto your computer. Tools in the data science and compute stack overlap and borrow words from one another, so a familiar word often hints at what a command does. *(00:40:33)*

- **Q:** In `docker run --rm -it rocker/r-ver:4.3.2`, what does `--rm` do, and why does it have two dashes?
    - **A:** Two dashes mark a flag whose name is several letters long. `--rm` means that when you turn the container off, the machine itself is deleted automatically. Otherwise you would have to delete it manually. *(00:40:55)*

- **Q:** Explain what `-it` means in `docker run --rm -it rocker/r-ver:4.3.2`, and why it is written as one flag.
    - **A:** Single-dash flags are single letters and can be chained, as in `ls -alh`, so `-it` is really two flags. `-i` is interactive: you will type into it. `-t` gives you an actual terminal (TTY) to interact with. *(00:41:48)*

- **Q:** In class, `library(tidyverse)` failed inside the `rocker/r-ver:4.3.2` container but loaded in a local R session. Why?
    - **A:** The container has only R installed, and nobody told it to install anything else. The local computer has tidyverse installed. The two terminals run on the same laptop, but the container is effectively a totally different machine. *(00:43:54)*

- **Q:** How is working in a Docker container like working on a cloud machine?
    - **A:** In both cases you are connected to another machine through pretty much the same interface. The difference is that the Docker container happens to run on the same hardware you are typing on. *(00:44:31)*

## 10. Know which machine you are typing on

*00:45:01–00:46:44*

- **Q:** Why is it important to read your terminal prompt when you work with containers or remote systems?
    - **A:** The prompt is often the only reference you have to which machine you are on. After quitting the container, the instructor's laptop prompt returned, and that was the visual cue that he was back on his own computer. You should know where you are typing before you type. *(00:45:04)*

- **Q:** The instructor opened a terminal on a computer in his closet at home. What did that example show?
    - **A:** It looks like any other terminal, but the commands run over there. The only visual cue that he was on a different machine was the hostname he had given it. Sometimes you really are given just a blinking cursor. *(00:45:48)*

- **Q:** Explain why a command like `whoami` exists, in terms of knowing which machine you are on.
    - **A:** It reports the username on the computer you are using. That gives you another way to check you are on the machine you think you are working on. *(00:46:08)*

## 11. Why so many data science tools run in a browser

*00:46:44–00:49:11*

- **Q:** Why are so many applications built on Electron, essentially as browsers?
    - **A:** A browser-first application can run inside a container and be opened in a browser. Making the browser the application is why so many tools you install are essentially browser applications. *(00:47:39)*

- **Q:** Explain why you open Jupyter Lab at a `localhost` address in a browser instead of double-clicking an app.
    - **A:** Jupyter Lab was built to run on a remote container that can have many more cores and much more memory than your laptop, while giving you the same application interface. Because it runs in a browser, you just connect your browser to wherever it is running. *(00:48:04)*

- **Q:** What is the point of GitHub's Codespaces button giving you VS Code in a browser?
    - **A:** VS Code is effectively a big browser application, so it can run in a container. Codespaces gives you the same interface on a different machine. That machine's entire compute environment has been set up for you, so you work on the same versions of all the software. *(00:49:00)*

## 12. Running RStudio in a container and mapping ports ([28.1.3 Mapping ports to containers with web apps](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#mapping-ports-to-containers-with-web-apps))

*00:54:10–00:58:59*

- **Q:** If you prefer a Jupyter notebook interface to Quarto, why does running RStudio in a container matter to you?
    - **A:** The project is written in Quarto, but some students are used to working in Jupyter notebooks. The same setup that runs RStudio from a container applies to running Jupyter from one. *(00:54:23)*

- **Q:** Why keep the `--rm` flag when running `rocker/rstudio:4.4.2`?
    - **A:** `--rm` shuts down and deletes the machine when you exit; without it, the container keeps running. Each container takes up RAM. If you have started five containers while practising, your computer stops working because five computers are using its resources. *(00:55:17)*

- **Q:** Explain what `-p 8787:8787` does in `docker run --rm -p 8787:8787 rocker/rstudio:4.4.2`.
    - **A:** RStudio runs on port 8787 inside the container, and you must connect your browser to it, just as with Jupyter Lab's port. `-p` connects a port on your local computer (the left number) to a port in the container (the right number). Here the container's 8787 appears on the Mac's 8787, so `localhost:8787` reaches RStudio in the container. *(00:57:05)*

- **Q:** How can you run two RStudio containers at the same time when both listen on port 8787?
    - **A:** Each container runs on 8787 internally, but you can redirect it to a different port on your own machine. Things running at the same time just use different host ports, which you specify in the left-hand number of `-p`. *(00:56:38)*

- **Q:** Why does RStudio use port 8787, when Jupyter Lab uses a different number?
    - **A:** The numbers are very arbitrary. Each tool's developers picked one, and that is the number they work with. Many tools happen to use numbers starting with eight. *(00:56:19)*

- **Q:** In class, why did the RStudio in the browser and the RStudio desktop app show different versions of R?
    - **A:** They are effectively completely different machines. The browser RStudio runs inside the `rocker/rstudio:4.4.2` container with that container's R. The desktop RStudio uses the R installed on the laptop, 4.6.2. Both differ from the R 4.3.2 in the earlier `r-ver` container. *(00:58:51)*

## 13. Passing environment variables into a container

*00:59:20–01:02:53*

- **Q:** What does `-e PASSWORD="apassword"` do in `docker run --rm -p 8787:8787 -e PASSWORD="apassword" rocker/rstudio:4.4.2`, and why use it?
    - **A:** `-e` passes an environment variable into the container as it runs. The RStudio container reads the variable `PASSWORD` and uses it as the login password. That replaces the hard-to-remember generated password that was printed at start-up. *(01:00:05)*

- **Q:** Why can't you assume that every container accepts a `PASSWORD` environment variable?
    - **A:** Containers behave differently depending on how whoever built them set them up. A container might use certain variables, but not every container has them. *(01:01:08)*

- **Q:** The instructor typed his RStudio password in front of the class. Why wasn't that a security problem?
    - **A:** The only way to reach that container is through his physical machine. Even though it is running on port 8787, if you can't log into his machine, his 8787 is not available to you. *(01:00:28)*

- **Q:** Why would you put a DSCI 532 dashboard into a container?
    - **A:** A dashboard runs in the browser, so someone can load your container, go to its port and see your dashboard. You have already done all the installation. The end user doesn't have to go through the whole install process with `renv`, snapshots and so on. With Docker they just `docker run` with some flags, because you've given them a computer you built from scratch. *(01:02:20)*

## 14. Starting from a base image and working inside it ([29.1.1 Workflow for building a Dockerfile](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#workflow-for-building-a-dockerfile))

*01:03:00–01:08:19*

- **Q:** When building your own container, why start from an existing machine like `rocker/r-ver:4.6.2`?
    - **A:** Whoever designed that image has already installed R, and probably the other things a brand-new computer needs for R to work. Those are like the compiler tools you installed on your own laptop for R. Starting from it lets you skip a few steps. *(01:04:00)*

- **Q:** How did adding `bash` to `docker run --rm -it rocker/r-ver:4.6.2 bash` change what happened compared with running the R container without it?
    - **A:** Without it, the container starts its default program, R, and drops you at the R prompt. With `bash` it skips that default and gives you a terminal on the container, and the prompt changes to show you are on that machine. You can still type `R` there to start R. *(01:05:20)*

- **Q:** Why open a shell in the base image and try your install steps by hand before writing them down?
    - **A:** It lets you go through the steps first and see that they work. Only then do you document them, so you end up with working instructions for building the machine from scratch. *(01:05:43)*

- **Q:** The instructor installed `cowsay` in a running `rocker/r-ver:4.6.2` container. Why did `library(cowsay)` fail after he exited and started it again?
    - **A:** A container has no real save state. When you turn it back on, it resets to how it was set up, so anything installed by hand in the previous session is gone. The instructor called this a benefit "for better or for worse." *(01:07:10)*

- **Q:** Why is a container a good place to try the destructive commands that DSCI 521 warned you about?
    - **A:** Even a command that deletes the whole computer only deletes the container. When you turn it back on, it is as if you never ran the command. That makes containers a safe place to try new packages or learn Linux without messing up your actual computer. *(01:07:37)*

- **Q:** Why is it a poor solution to make users follow README install steps every time they start your container?
    - **A:** It is extremely painful to repeat those instructions on every start. A tidyverse install on a poorly set up Linux machine can take 15 minutes. You would be spending 15 minutes to run a 30-second analysis. *(01:08:19)*

## 15. Running R from the command line with `Rscript -e` ([29.1.2 Build your first image](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#build-your-first-image))

*01:08:19–01:10:18*

- **Q:** Why did the instructor switch from `install.packages()` typed inside R to `Rscript -e "install.packages('cowsay')"`?
    - **A:** Saving the setup comes down to knowing the terminal command that makes it happen. He needed R to execute the install from the command line, not just to open R. `Rscript` is how R runs commands in the terminal. *(01:08:59)*

- **Q:** Explain each part of `Rscript -e "install.packages('cowsay')"`, including the quotes.
    - **A:** `Rscript` runs R from the terminal, and `-e` says "I'm going to give you an R expression." The expression is the install command. Pay attention to the quotes: the expression is wrapped in double quotes, so the package name inside uses single quotes. *(01:09:41)*

- **Q:** After `Rscript -e "install.packages('cowsay')"` worked in the container, why was the problem still not solved?
    - **A:** It showed the terminal command was right, because `library(cowsay)` then loaded. But on exiting and re-entering the container, the package was gone again. The information had to be saved somewhere, which led to the `Dockerfile`. *(01:10:13)*

## 16. The `Dockerfile`: `FROM`, `RUN`, `CMD` ([29.1 Building container images from `Dockerfile`’s](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#building-container-images-from-dockerfiles))

*01:10:18–01:15:01*

- **Q:** What is a `Dockerfile` for, and how does it explain why the `rocker/rstudio` image starts with RStudio ready?
    - **A:** A `Dockerfile`, named with a capital D, holds the instructions for installing and setting up a computer. The RStudio image has its own `Dockerfile`, which installs RStudio and opens the ports. That is why RStudio is there when you load the container. *(01:10:45)*

- **Q:** Explain the role of the `FROM rocker/r-ver:4.6.2` line in the class's `Dockerfile`.
    - **A:** `FROM` is normally the first line, and it states the starting-point machine. Here that is a machine that already has R 4.6.2 installed. Everything after it builds on top of that machine. *(01:11:30)*

- **Q:** You could start from a bare-minimum Linux image and install everything yourself. Why is a beefier base image acceptable?
    - **A:** Disk space is cheaper than other resources, so starting from a bigger machine is fine if that's what you want. The bare-minimum route means installing every single thing by hand. That is a good way to learn Linux on your own time, not a requirement. *(01:12:02)*

- **Q:** What is the difference between `RUN` and `CMD` in a `Dockerfile`?
    - **A:** `RUN` holds the bash commands the container runs during the build, such as the `Rscript -e "install.packages('cowsay')"` line. `CMD` sets what a container from the new image does by default when it starts, here printing "Hello from my first image!". `CMD` is the last thing the machine runs, and you can override it. *(01:14:05)*

- **Q:** How is `CMD ["Rscript", "-e", "cowsay::say('Hello from my first image!')"]` written differently from a shell command, and when does it run?
    - **A:** It looks like a bash command, but it is written as a list instead of terms separated by spaces. It runs by default when the container starts, unless you give another command, such as `bash`, which overrides it. *(01:14:05)*

- **Q:** How would the middle of a `Dockerfile` look for a Python project using `uv`?
    - **A:** The `RUN` lines would install `uv`. A copy command would bring in your lock files, and then you would run `uv sync`. All the packages would then be installed in the container, so the machine itself has your compute environment ready. *(01:14:15)*

## 17. Building and running your own image ([29.1.2 Build your first image](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#build-your-first-image))

*01:15:01–01:18:44*

- **Q:** In `docker build --tag hello-cowsay .`, what does the final `.` mean?
    - **A:** It tells Docker where to look for the `Dockerfile`: right here, in the current directory. By default `docker build` looks for a file named exactly `Dockerfile` with a capital D. The instructor noted this is probably the first time a lone dot is something you have to type. *(01:15:38)*

- **Q:** Why does the course assume commands like `docker build --tag hello-cowsay .` are run from the root of the repository?
    - **A:** You could give `docker build` a full path, but the course assumes every command is run from the project root. That lets commands be copied and pasted without changing directories in the middle of something. Milestone instructions are written on that assumption. *(01:16:11)*

- **Q:** Why did `library(cowsay)` load inside `hello-cowsay` but not in a fresh `rocker/r-ver:4.6.2` container?
    - **A:** The `Dockerfile` gave the instructions for installing `cowsay`, and the image was then built from them. Every container started from `hello-cowsay` therefore begins with the package installed. Nothing was installed by hand. *(01:17:52)*

- **Q:** What is the difference between `docker run --rm -it hello-cowsay` and `docker run --rm -it hello-cowsay bash`, and why is the second useful?
    - **A:** Without `bash`, the container runs its default `CMD` and prints the cow saying hello. With `bash`, you get shell access inside the image instead. That lets you play inside the container directly, for example to work out why code runs on your machine but not in the container. *(01:17:30)*

- **Q:** Why does writing a `Dockerfile` depend on knowing shell commands?
    - **A:** A `Dockerfile` usually has one starting point and a middle full of `RUN` and copy commands. Every one of those lines is a command you must give the machine to install what you need. If you don't know the shell command, you can't write the step. *(01:18:07)*

## 18. Pinning versions, and what comes next

*01:18:44–01:20:39*

- **Q:** How does a container keep the version of Quarto stable for a project?
    - **A:** The install line in the container names a specific version, even an older one. As long as you don't change that install command, a year later you are still on the same version of the tool. *(01:19:35)*

- **Q:** What went wrong when the instructor restarted a container in another class a few weeks earlier, and why?
    - **A:** He had not hard-pinned the versions in the container. Something had updated the day before, and nothing worked. In a real job you would spend hours fixing the update instead of doing the actual work. *(01:19:55)*

- **Q:** Explain why the instructor wants explicit control over when software updates, and how Docker gives it.
    - **A:** Things updating without you being explicit about it, and without you knowing an update happened, is very annoying. It can also break your work. A `Dockerfile` says "here's the version I want," and that version does not change until you edit that line. *(01:20:27)*

---

- prompt: prompt-recall-2-understand.md @ 65eb21c
- prompt-hash: 17df43f38e78
- model: claude-opus-5-5 (requested: opus)
- backend: claude
- inputs: transcript-plaud.md, history.txt, terminal.txt, materials.md, notes-class-main--claude-opus-5-5.md
- generated: 2026-11-23
- notes-input: notes-class-main--claude-opus-5-5.md @ 1c708a29f65f, links and section references removed
