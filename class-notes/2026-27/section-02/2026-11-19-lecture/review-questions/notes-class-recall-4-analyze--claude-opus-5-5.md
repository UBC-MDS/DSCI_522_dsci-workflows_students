# Git issues and pull requests, then Docker containers: review questions, tier 4 — Analyze

Date: 2026-11-19

Instructor: Daniel Chen

*Tier 4 of 5: Analyze. Take each one apart yourself before you read the answer; tiers 1 to 3 cover the facts, reasons and steps it relies on.*

## 1. Git review: working on a branch

*00:06:16–00:09:50*

- **Q:** Break down the steps the instructor ran in the `2026-11-19-docker` repository, from editing `README.md` to `git push origin today`. What did each step contribute, and which steps stayed on the laptop and which reached GitHub?
    - **A:** After the edit, `git status` showed he was still `On branch main` with `README.md` modified but not committed, and `git pull origin main` reported `Already up to date`. Because nothing was committed yet, `git switch -c today` could create the branch and carry the uncommitted edit onto it. `git diff` showed the added line "today we will talk about containers". `git add README.md` and `git commit -m "today we are talking about containers"` then recorded commit `3c6d82a` on `today`, and every one of these steps ran only on the laptop. Only `git push origin today` touched GitHub: it created the remote branch and printed the link to open a pull request. *(00:08:57)*

- **Q:** Point out the two places in the branch workflow where the instructor said to stop and check something, and what each check protects later on.
    - **A:** The first check is right before `git add`, and definitely before `git commit`: look at which branch you are on. If you commit on `main` by mistake, you have to move those commits with the cheat-sheet commands from the textbook. In the demo, `git status` caught him on `main` before he had committed, so `git switch -c today` was enough to fix it. The second check comes before you start work: pull `main`, so you are not making changes to something out of date. This matters once several people work on several branches at the same time. *(00:08:08)*

## 2. GitHub issues as a project board

*00:09:50–00:16:17*

- **Q:** Relate issue #1, issue #2 and pull request #3 in the `2026-11-19-docker` repository. What role did each play, why did the pull request get number 3, and how are the three linked?
    - **A:** Issue #1, "what are we doing today?", worked like a meeting or planning note that asked for today's topic. Issue #2, "edit the readme with today's topic", was an action item spawned from it, and its text points back with "meeting from #1". Issues and pull requests share one counter, so the pull request opened after two issues became #3. Writing a `#` number in an issue or pull request creates a two-way reference: the item you name automatically shows a link back. That is how #3's "this is the fix for #2" connects the pull request and the issue. *(00:12:07)*

## 3. Pull request descriptions, checkboxes and closing keywords

*00:16:17–00:22:18*

- **Q:** Break down the description of pull request #3 into its parts. What does each part do on GitHub, and which part acts only when the pull request is merged?
    - **A:** The first line, "this is the fix for #2", is a plain reference: it creates a two-way link but closes nothing. The checkboxes `- [x] item 1` and `- [ ] item 2` are Markdown tasks that track what is still to do. They show teammates the work isn't finished, as an alternative to the draft button. The last line, `closes #1 fixes #2`, uses closing keywords: when the pull request is merged, GitHub closes those issues automatically. This is a GitHub feature, not a Git feature. In class the instructor wasn't sure `closes` had worked, but the repository shows both #1 and #2 closed by #3. *(00:19:30)*

- **Q:** Break down the issue-to-merge cycle the instructor uses for the textbook. What does each stage do to the issues tab, and how does one pull request handle several issues?
    - **A:** He files an issue for a piece of work, does the work, and writes "fixes" followed by the issue number in a comment or the pull request message. When that chapter update is merged, the issue closes at the same moment, so the issues tab shrinks. He then picks the next item from the list without clicking "close" anywhere. Keywords also work in commit messages, but they are harder to see there. A single pull request can name several issues: his refactor of the containers and virtual environment chapters fixed several separate issues at once. *(00:20:28)*

## 4. Cleaning up after a merge

*00:22:18–00:25:19*

- **Q:** Separate the cleanup after merging pull request #3 into the steps done on GitHub and the steps done on the laptop. What does each step update?
    - **A:** On the laptop, `git switch main` and `git pull origin main` brought in the merge commit that GitHub created: the output shows `Updating deb10c5..d25ddfa` and `Fast-forward`. On GitHub, the branch is deleted with the button on the merged pull request, or with the trash can in the branches view, which listed `today` as pull request #3, merged. Deleting the branch on GitHub does not touch the laptop's references. Two more local commands remove them: `git fetch --prune` for the remote-tracking reference and `git branch -d` for the local branch. Deleting branches is optional in this course, and teams differ in how they handle it. *(00:24:30)*

- **Q:** Correlate the three `git log --oneline --graph --all` outputs with the commands run between them. What did each command remove, and what stayed in the history?
    - **A:** The first log shows commit `3c6d82a` labelled `(origin/today, today)` under the merge commit `d25ddfa`. `git fetch --prune` printed `[deleted] (none) -> origin/today`, and the second log labels `3c6d82a` only `(today)`. `git branch -d today` printed `Deleted branch today (was 3c6d82a)`, and the third log shows `3c6d82a` with no label at all. The merge commit and `3c6d82a` are still in the graph, so only the shortcut names are gone. That is why some people keep their branches: `git switch today` is easier than switching to a commit hash. *(00:24:30)*

## 5. Why data science workflows need stable environments ([27.1 Documenting and loading dependencies](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#documenting-and-loading-dependencies))

*00:25:29–00:30:13*

- **Q:** Break down the two stability goals the instructor set out for a project that lasts weeks or longer. What threatens each one?
    - **A:** The first goal is to keep your own environment stable over days, weeks, months or years. Packages update on different cycles, so an install-everything environment can become impossible to install, which is why the package list should be the bare minimum. The second goal is to make the same environment work on a teammate's computer. That computer may run a different operating system or even have a different chip: Mac and Windows differ, and Windows now ships on both ARM and Intel, so things install differently. "It works on my machine" fails the second goal even when the first is met. *(00:28:34)*

## 6. What a container is ([27.2 What is a container?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#what-is-a-container))

*00:30:13–00:34:28*

- **Q:** Set a `uv.lock` file and a container side by side. What does each hand a teammate, and what must the teammate already have or do?
    - **A:** A `uv.lock` file lets a teammate install the same Python packages. They still need `uv` on their own computer, which they might not use, and installing it might mess up other things their computer is set up for. A container hands over a whole computer instead: you build a virtual computer from scratch and give it to them. They then do all their work on that computer instead of directly on their own machine. Everyone effectively shares the same computer even on different physical machines, at the cost of a performance hit from the extra layer. *(00:31:17)*

## 7. Containers versus virtual machines ([27.3 Contrasting containers with virtual machines](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#contrasting-containers-with-virtual-machines))

*00:34:31–00:36:40*

- **Q:** Set a virtual machine and a container side by side. Compare what each contains, the interface you get, the size, and when the instructor still reaches for a virtual machine.
    - **A:** A virtual machine installs a full operating system, such as all of Windows, with its graphical interface and buttons. A container is a stripped-down version that holds only the bare minimum you install and typically has no graphical interface. That is why DSCI 521 pushed typing commands in the terminal. A Windows virtual machine takes something like 50–80 GB. The containers used in class are under a couple of gigabytes, so they are lighter on disk, memory and compute. The instructor still uses a virtual machine to test the MDS install instructions as if he were on Windows. *(00:35:33)*

## 8. Pulling and running a container: R 4.3.2 beside local R ([28.1.1 Launch and run containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#launch-and-run-containers))

*00:36:40–00:45:01*

- **Q:** Break down `docker run --rm -it rocker/r-ver:4.3.2` into its parts. What does each part contribute to what appeared on screen?
    - **A:** `docker run` says which computer to turn on, and it downloads the image first if it isn't on your machine. `--rm` is a multi-letter flag, as its double dash shows: it deletes the container when it is turned off, instead of leaving you to delete it by hand. `-it` chains two single-letter flags: `-i` for interactive, and `-t` for a terminal (TTY) you can type in. `rocker/r-ver:4.3.2` names the image: `rocker` is the organisation, `r-ver` is a machine with only R installed, and the tag `4.3.2` picks the R version. Together they opened an R 4.3.2 prompt. *(00:41:48)*

- **Q:** Distinguish the laptop's R from the container's R using what the two terminals printed. Which details show that they are different machines?
    - **A:** `R --version` on the laptop reported R 4.6.2 "Diversified Portfolio" on `aarch64-apple-darwin23`. R in the container reported 4.3.2 "Eye Holes" on `aarch64-unknown-linux-gnu`, which is a Linux machine. In the container, `library(tidyverse)` failed with "there is no package called 'tidyverse'", because the image has only R. In the laptop's terminal, tidyverse loaded. Two terminals on one laptop behave like two separate computers. *(00:44:09)*

- **Q:** In the instructor's clinical-trials example, separate what a lock file keeps stable from what the container adds.
    - **A:** A trial can run for years while R releases a new version every six months, and the regulator can ask for both the code and the compute environment. A lock file (`renv` or `uv.lock`) pins only the package versions. The container also pins the tools on the system, such as the version of R itself or of Git. The instructor's example: hand people a container with an old Git, and they couldn't run `git switch`. So you hand over the container that ran the full analysis, not your laptop. *(00:39:02)*

## 9. Know which machine you are typing on

*00:45:01–00:46:44*

- **Q:** Point out the cues in the class's terminal output that tell you which machine a command is running on: the laptop, a container, or a remote machine.
    - **A:** On the laptop, the prompt reads `dan@Heartsbane 2026-11-19-docker %`, and it came back after he quit the container. Inside a container started with `bash`, the prompt changes to something like `root@95765251a970:/#`: the user is `root`, then comes the container's ID and the folder `/`. Inside R, the `>` prompt hides which machine you are on, so the R version banner is the clue. On the remote machine in his closet, the only cue was the hostname he had given it, and `whoami` reports the username as another check. The instructor warned that sometimes all you get is a blinking cursor, so read these cues before you type anything. *(00:46:08)*

## 10. Why so many data science tools run in a browser

*00:46:44–00:49:11*

- **Q:** Relate Electron apps, Jupyter Lab and GitHub Codespaces to containers. What design do they share, and what does it let you separate?
    - **A:** All three are browser-first: Electron makes the browser itself the application, and VS Code is essentially a big browser app. Because the interface is a web page, the program can run in a container or on a remote machine while you view it in your local browser. Jupyter Lab opens at a `localhost` address because it was built to run on machines with more cores and memory than your laptop, while keeping the same interface. The Codespaces button gives you VS Code in a browser, running on a machine whose whole compute environment someone else has set up. *(00:48:33)*

## 11. Running RStudio in a container and mapping ports ([28.1.3 Mapping ports to containers with web apps](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#mapping-ports-to-containers-with-web-apps))

*00:54:10–00:58:59*

- **Q:** Break down `docker run --rm -p 8787:8787 rocker/rstudio:4.4.2` and trace how typing `localhost:8787` in the browser reaches RStudio.
    - **A:** `--rm` shuts the machine down and removes it when you exit. The instructor warned that each running container uses RAM, and leaving "five computers" running grinds a laptop to a halt. In `-p 8787:8787`, the left number is the port on your machine and the right number is the port inside the container, where RStudio Server listens. The browser at `localhost:8787` is therefore forwarded into the container. A second RStudio would need a different number on the left. Once connected, you sign in with the username `rstudio` and the password printed in the start-up output. *(00:57:05)*

- **Q:** Relate the three R versions the class saw: in the laptop's RStudio, in the `rocker/rstudio:4.4.2` container, and in the `rocker/r-ver:4.3.2` container. What does each one belong to?
    - **A:** The RStudio desktop app on the laptop runs the laptop's own R 4.6.2. The RStudio in the browser runs R 4.4.2 inside the `rocker/rstudio:4.4.2` container. The earlier `rocker/r-ver:4.3.2` container ran R 4.3.2. Each is effectively a separate machine: the `r-ver` one is terminal-only, and the `rstudio` one is an application you reach through a browser. *(00:58:51)*

## 12. Passing environment variables into a container ([27.2 What is a container?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#what-is-a-container))

*00:59:20–01:02:53*

- **Q:** Differentiate the start-up output of `docker run --rm -p 8787:8787 rocker/rstudio:4.4.2` from the run with `-e PASSWORD="apassword"` added. Which lines changed, and what does that show about how the image uses the variable?
    - **A:** Without `-e`, the `01_set_env` step skipped only `HOME` and `RSTUDIO_VERSION`. The `02_userconf` step then printed `The password is set to ooph3Aef2Ohcahcu`, with instructions for setting `PASSWORD` yourself. With `-e PASSWORD="apassword"`, `01_set_env` also lists `PASSWORD`, and `02_userconf` prints no generated password: the container noticed the password had been set manually. Which variables a container reads depends on how its image was built, so not every container has `PASSWORD`. *(01:00:39)*

- **Q:** Break down the dashboard hand-off the instructor described for DSCI 532. What does the person who builds the container do, and what does the person who uses it do?
    - **A:** The builder puts the dashboard code in a container and does all the installation inside it, such as setting up `renv` and the snapshot. The user only needs Docker. They type `docker run` with some flags and open the dashboard's port in their browser. They skip the whole installation process, because they have been given a computer that was built from scratch. *(01:02:20)*

## 13. Starting from a base image and working inside it ([28.1.4 Changing the containers default command](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#changing-the-containers-default-command))

*01:03:00–01:08:19*

- **Q:** Differentiate `docker run --rm -it rocker/r-ver:4.3.2` from `docker run --rm -it rocker/r-ver:4.6.2 bash`. Which part produces the difference in what starts, and why is the second form useful when you design a container?
    - **A:** The R version comes from the tag, but what starts comes from the word after the image name. Without anything after the image name, the container runs its default and you land at the R prompt. Adding `bash` replaces that default with a shell, so the prompt becomes the container's own (`root@...:/#`), and you can still type `R` to start R. From that shell you can try install steps by hand. Once they work, you document them as the instructions for building the machine from scratch. *(01:05:20)*

- **Q:** Trace the `cowsay` package across the three `docker run --rm -it rocker/r-ver:4.6.2 bash` sessions in the terminal log. Why did it appear and disappear?
    - **A:** In the first container (`root@95765251a970`), `library(cowsay)` failed until `install.packages("cowsay")` ran, and then `cowsay::say('hello')` drew the cow. In the second (`root@97a536175dca`), `library(cowsay)` failed again. After `Rscript -e "install.packages('cowsay')"`, it loaded. In the third (`root@a642984ec391`), it failed once more. Each run is a new container, with a new ID, started from an unchanged image, so it resets to how the image was built: "there's no save state of a container". *(01:07:10)*

## 14. Running R from the command line with `Rscript -e` ([29.1.2 Build your first image](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#build-your-first-image))

*01:08:19–01:10:18*

- **Q:** Break down `Rscript -e "install.packages('cowsay')"`. How does it relate to typing `install.packages("cowsay")` at the R prompt, and to the line that later went into the `Dockerfile`?
    - **A:** `Rscript` runs R from the terminal, and `-e` says that what follows is an R expression. The quoting is double on the outside and single on the inside. It installs exactly what the interactive call did: the log shows `crayon`, `rlang` and `cowsay` installed both ways. The difference is that this is a shell command, and the instructor's point was that saving a setup comes down to knowing the terminal command that makes it happen. That same line became the `Dockerfile`'s `RUN Rscript -e "install.packages('cowsay')"`. *(01:09:27)*

## 15. The `Dockerfile`: `FROM`, `RUN`, `CMD` ([29.2 `Dockerfile` command summary](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#dockerfile-command-summary))

*01:10:18–01:15:01*

- **Q:** Break down the three lines of the class's `Dockerfile`. When does each line take effect, and which step from the earlier hands-on work does it record?
    - **A:** `FROM rocker/r-ver:4.6.2` names the starting machine, which already has R 4.6.2: it records the image the class had been passing to `docker run`. `RUN Rscript -e "install.packages('cowsay')"` runs during the build, and it is the shell command tested by hand in the container. `CMD ["Rscript", "-e", "cowsay::say('Hello from my first image!')"]` is written as a list rather than space-separated words. It is the default a container runs when it starts, and you can override it by giving a command such as `bash`. *(01:13:52)*

- **Q:** Break down how the middle of the `Dockerfile` would change for a Python project, as the instructor sketched it. What does each piece contribute to the finished machine?
    - **A:** A `RUN` step would install `uv`. A copy command would bring the project's lock files into the image. `uv sync` would then install all the packages, so the machine itself carries the compute environment. For next week's project container, the image also needs the language and Quarto installed. Then the analysis runs both on your own computer and in the container. *(01:14:15)*

## 16. Building and running your own image ([29.1.2 Build your first image](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#build-your-first-image))

*01:15:01–01:18:44*

- **Q:** Break down `docker build --tag hello-cowsay .` and relate its parts to the build output in the terminal log.
    - **A:** `--tag hello-cowsay` names the image, and the output ends with `naming to docker.io/library/hello-cowsay:latest`. The `.` tells Docker to look in the current directory for the file named exactly `Dockerfile`, which matches `load build definition from Dockerfile`. The two numbered steps come straight from the file: `[1/2] FROM docker.io/rocker/r-ver:4.6.2` and `[2/2] RUN Rscript -e "install.packages('cowsay')"`. Afterwards, `docker images` lists `hello-cowsay:latest` alongside the images pulled earlier. *(01:16:39)*

- **Q:** Trace `library(cowsay)` from failing in `rocker/r-ver:4.6.2` to loading in `hello-cowsay`. Which steps caused the change, and what did each of the two `docker run` commands on the new image show?
    - **A:** The install was written into the `Dockerfile` as a `RUN` line, and `docker build` ran it once, saving the package into the `hello-cowsay` image instead of into a throwaway container. `docker run --rm -it hello-cowsay` ran the image's `CMD` and printed the cow saying "Hello from my first image!". `docker run --rm -it hello-cowsay bash` replaced that default with a shell, and there R loaded `cowsay` without any install. The instructor summed it up as three things: give the instructions in the `Dockerfile`, build the machine, then turn it on. *(01:17:52)*

## 17. Pinning versions, and what comes next

*01:18:44–01:20:39*

- **Q:** Trace the failure in the instructor's other class back to its cause. Then relate the lines of a project `Dockerfile` that prevent it.
    - **A:** He restarted a container whose versions weren't hard-pinned, something had updated the day before, and nothing worked. On a real job that means hours spent fixing an update instead of doing the actual work. In a project `Dockerfile`, the `FROM` line pins the R version. A placeholder section holds the `renv` or `uv` setup that installs the packages. The tool install lines can name a specific version, even an older Quarto. A year later you are still on those versions, as long as you don't change those lines, so nothing updates without you knowing. *(01:19:55)*

---

- prompt: prompt-recall-4-analyze.md @ 65eb21c
- prompt-hash: 7dde50dd5ebf
- model: claude-opus-5-5 (requested: opus)
- backend: claude
- inputs: transcript-plaud.md, history.txt, terminal.txt, materials.md, notes-class-main--claude-opus-5-5.md
- generated: 2026-11-23
- notes-input: notes-class-main--claude-opus-5-5.md @ 1c708a29f65f, links and section references removed
