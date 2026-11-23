# Git issues and pull requests, then Docker containers: review questions, tier 4 — Analyze

Date: 2026-11-19

Instructor: Daniel Chen

*Tier 4 of 5: Analyze. Take each one apart yourself before you read the answer; tiers 1 to 3 cover the facts, reasons and steps it relies on.*

## 1. Git review: working on a branch

*00:06:16–00:09:50*

- **Q:** In the `2026-11-19-docker` demo repository, the instructor edited `README.md` before he made a branch. Break down the sequence from that edit to `git push origin today`. What did `git status` report at each point, and why did creating the branch late still work?
  **A:** The first `git status` reported `On branch main`, with `README.md` modified but not staged, so the edit existed only in the working directory. Nothing had been committed yet, so `git switch -c today` created the `today` branch and carried the uncommitted edit with it. The second `git status` showed `On branch today` with the same modification. `git diff` then showed the added line, `git add README.md` staged it, `git commit` recorded it on `today` as `3c6d82a`, and `git push origin today` sent the branch to GitHub. Had he already committed on `main`, he would have needed the textbook's cheat sheet to move the commits, which is why he says to look at your branch right before `add`, and definitely before `commit`. *(00:08:57)*

## 2. GitHub issues as a project board

*00:09:50–00:16:17*

- **Q:** The `2026-11-19-docker` repository ended up with issue #1 "what are we doing today?", issue #2 "edit the readme with today's topic" and pull request #3. Relate these three items: why did the pull request get number 3, and how do the references among them link up?
  **A:** Issues and pull requests share one counter, so after two issues the pull request from `today` became #3. Issue #2 points back to #1 with "meeting from #1", the way an action item spawns from a meeting-notes issue. The pull request's description refers to #2 and names both issues. Every `#` reference is two-way: the item referred to automatically shows a link back. As a result, #1 lists #2, and both issues show the pull request that deals with them. *(00:12:07)*

- **Q:** On a GitHub pull request such as #3 in `2026-11-19-docker`, distinguish the assignee role from the reviewer role. Who normally fills each one, and what does each contribute to the project?
  **A:** Being an assignee means claiming the work as your responsibility. You normally assign yourself to your own pull request, and you can also assign people to issues. The reviewer section is separate, and it is where you add a teammate to look over your work. Some larger projects block changes until someone has actually reviewed them. In the demo the instructor added Copilot as the reviewer. *(00:14:47)*

## 3. Pull request descriptions, checkboxes and closing keywords

*00:16:17–00:22:18*

- **Q:** Pull request #3 in `2026-11-19-docker` had a description in three parts: "this is the fix for #2", a checklist (`- [x] item 1`, `- [ ] item 2`), and "closes #1 fixes #2". Separate these parts: what does each do, and which one acts when the pull request is merged?
  **A:** "this is the fix for #2" is a plain reference. It links the pull request and issue #2 both ways but closes nothing. The checklist uses Markdown checkboxes to track what is still to do, which shows teammates that the work isn't finished, much like the draft button does. The last sentence uses closing keywords. When the pull request is merged, GitHub auto-closes the issues named after `closes` or `fixes`, and this is a GitHub feature, not a Git one. In class the instructor wasn't sure `closes` had worked and said he almost always uses `fixes`, but the demo repository lists both #1 and #2 as closed by #3. *(00:19:30)*

- **Q:** Break down the issue-to-merge workflow the instructor uses for the textbook. How does it explain why one pull request can satisfy the lab's three issues?
  **A:** He files an issue, works on it, and writes "fixes #N" in a comment or in the pull request message. When the pull request is merged, the issue closes at the same moment, the issues tab shrinks, and he picks the next item from the list. One refactor of the containers and virtual environments chapters covered two separate issues, moving the old material and writing the new, and a single pull request fixed both. In the same way, one pull request whose message names all three lab issues closes them on merge, so you don't have to close each one by hand. Keywords also work in commit messages, but they are harder to see there. *(00:20:28)*

## 4. Cleaning up after a merge

*00:22:18–00:25:19*

- **Q:** After pull request #3 was merged, the instructor ran `git log --oneline --graph --all` three times while cleaning up. Break down how the labels on commit `3c6d82a` changed after each step, which steps acted on GitHub and which on the laptop, and what stayed the same throughout.
  **A:** `git switch main` and `git pull origin main` fast-forwarded the local `main` to the merge commit `d25ddfa`. At that point `3c6d82a` was labelled `(origin/today, today)`, even though the branch had already been deleted on GitHub with the delete button. `git fetch --prune` reported `[deleted] origin/today` and dropped the stale remote-tracking reference, leaving `(today)`. `git branch -d today` then deleted the local branch, and the commit had no label at all. Throughout, the merge commit and the history stayed in the graph: only the shortcut names disappeared, which is why some people keep branches, since `git switch today` is easier than switching to a hash. *(00:24:30)*

## 5. Why data science workflows need stable environments ([27.1 Documenting and loading dependencies](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#documenting-and-loading-dependencies))

*00:25:29–00:30:13*

- **Q:** The instructor described two stability goals for a project that lasts weeks or years. Separate them: what threatens each one, and why does "it works on my machine" fail?
  **A:** The first goal is keeping your own environment stable over time. Packages update on different cycles, so an environment that installs everything can become impossible to install all at once, which is one reason to keep the package list to the bare minimum. The second goal is reproducing the environment on a teammate's computer, which may run a different operating system or even a different chip. Mac and Windows machines differ, and Windows now ships on both ARM and Intel, so the way software gets installed differs too. Code that runs only on your machine therefore fails as soon as a teammate tries to run the same analysis. *(00:28:53)*

## 6. What a container is ([27.2 What is a container?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#what-is-a-container))

*00:30:13–00:34:28*

- **Q:** Set handing a teammate a `uv.lock` file side by side with handing them a container. Compare what each one carries, what the teammate must already have set up, and where the teammate's code actually runs.
  **A:** A `uv.lock` file records the Python packages, so the teammate can at least install the same package versions. To use it, though, they must install `uv` themselves, which might interfere with how their computer is already set up, and their computer may still differ from yours. A container is a virtual computer built from scratch and handed over whole. The teammate runs their code on that computer instead of directly on their own, so everyone shares the same computer even on different physical machines. *(00:31:17)*

- **Q:** Break down what a container offers in three settings the instructor described: prototyping on your laptop, running on a bigger machine that holds the data, and working on a remote machine whose administrator won't let you install software. What is the cost?
  **A:** The same container gives an identical compute environment on your laptop and on the bigger machine, so work prototyped locally runs unchanged where the data lives. On a remote machine, the administrator can hand you a container as a sandbox instead of letting you install Python directly. If you break the sandbox, you restart it and get a fresh one, which also makes a container a safe place to muck around with an operating system. The cost is a performance hit from the extra layer, which can't be avoided. *(00:32:34)*

## 7. Containers versus virtual machines ([27.3 Contrasting containers with virtual machines](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#contrasting-containers-with-virtual-machines))

*00:34:31–00:36:40*

- **Q:** Set a virtual machine and a container side by side. Compare what each contains, how you interact with it, its size, and what the instructor still uses virtual machines for.
  **A:** A virtual machine is a full-blown operating system, such as all of Windows, with its graphical interface and buttons. A container holds only the bare minimum you install and typically has no graphical interface, so you work in it by typing commands. That makes containers far lighter: a Windows VM takes 50 to 80 GB, while the containers used in class are around a couple of gigabytes or less and still run a full computational stack. They also use less memory and compute. The instructor still uses a VM to test the MDS installation instructions as if he were on Windows. *(00:35:33)*

## 8. Pulling and running a container: R 4.3.2 beside local R ([28.1.1 Launch and run containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#launch-and-run-containers))

*00:36:40–00:45:01*

- **Q:** Break down `docker run --rm -it rocker/r-ver:4.3.2` into its parts. What does each part contribute?
  **A:** `docker run` turns on the machine named at the end, and it downloads the image first if it isn't already on your computer. `--rm` has two dashes because it is a multi-letter flag, and it deletes the container when it stops; otherwise you would have to delete it by hand. `-it` chains two single-letter flags: `-i` for interactive and `-t` for a TTY, a terminal you can type in. `rocker/r-ver:4.3.2` names the image: `rocker` is the organisation, whose `r-ver` images have only R installed, and the tag `4.3.2` picks the R version. *(00:41:48)*

- **Q:** Distinguish the two terminals the instructor had open on his laptop: one running local R, one running `rocker/r-ver:4.3.2`. What did each show for the R version, the platform and `library(tidyverse)`, and what does the contrast demonstrate?
  **A:** Local `R --version` reported R 4.6.2 on `aarch64-apple-darwin23`, the Mac, and there `library(tidyverse)` loaded. The container started R 4.3.2 on `aarch64-unknown-linux-gnu`, and `library(tidyverse)` failed with "there is no package called 'tidyverse'", because the image has only R installed. The two terminals run on the same hardware but behave like two different machines. That is how you can run a second version of R even though your computer has another version installed. *(00:44:09)*

- **Q:** Using the instructor's clinical-trials example, separate what lock files pin from what a container pins, and relate each layer to what a regulator asks for.
  **A:** Lock files such as `uv.lock` and the `renv` lock track only package versions. A container goes one level deeper and fixes the tools on the system: the version of R itself, and even system tools such as Git. A container with a 2019 Git, for example, would stop anyone from using `git switch`. Clinical trials research can run for years while R updates every six months. The regulator wants your code and the full compute environment so they can reproduce your work, and the container that ran the analysis provides both. *(00:39:02)*

## 9. Know which machine you are typing on

*00:45:01–00:46:44*

- **Q:** In the terminal log, separate the prompts that appear: `dan@Heartsbane 2026-11-19-docker %`, `root@95765251a970:/#` and `>`. What does each one tell you about where you are typing, and why did the instructor stress reading them?
  **A:** `dan@Heartsbane 2026-11-19-docker %` is the laptop's own prompt, showing the user, the machine and the current folder, and it returned after each container exited. `root@95765251a970:/#` is a Bash shell inside a container: the user `root`, a container ID, and the folder `/`. `>` is R's own prompt, whether on the laptop or inside a container. With containers and remote machines, the prompt is sometimes the only cue you get, as on the machine in the instructor's closet. Check it, or run `whoami`, before running commands, so you don't run something on the wrong machine. *(00:45:04)*

## 10. Why so many data science tools run in a browser

*00:46:44–00:49:11*

- **Q:** Relate Electron, Jupyter Lab, VS Code and GitHub Codespaces. What design do they share, and what does that design make possible with containers?
  **A:** Electron is essentially a browser packaged as an application, and many applications are built on it. Jupyter Lab opens at a `localhost` address because it was designed to run on a remote machine with more cores and memory while keeping the same interface. VS Code is likewise a large browser application, and the Codespaces button gives you VS Code in a browser on a machine someone else has set up. All of them are browser-first, so the application can run in a container or on another machine while you use it in your local browser, with the same versions of all the software as everyone else. *(00:48:04)*

## 11. Running RStudio in a container and mapping ports ([28.1.3 Mapping ports to containers with web apps](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#mapping-ports-to-containers-with-web-apps))

*00:54:10–00:58:59*

- **Q:** Break down `docker run --rm -p 8787:8787 rocker/rstudio:4.4.2`. How does each part get RStudio into your browser, and what would you change to run a second RStudio at the same time?
  **A:** `--rm` deletes the machine when you exit. Without it, every container you started keeps using RAM, and you end up with "five computers" running and a computer that stops working. `-p` maps ports: the left number is the port on your machine and the right number is the port inside the container, where RStudio Server listens on `8787`. You then open `localhost:8787` in your browser and log in as `rstudio` with the password printed in the start-up output. To run a second copy, keep the container side at `8787` and map it to a different host port on the left. *(00:57:05)*

- **Q:** By the end of the RStudio demo, three versions of R were in play on one laptop. Distinguish them by where each one runs and how you interact with it.
  **A:** The desktop RStudio uses the laptop's installed R 4.6.2. The `rocker/rstudio:4.4.2` container runs its own R inside the container and serves RStudio to the browser at `localhost:8787`. The earlier `rocker/r-ver:4.3.2` container ran R 4.3.2 with only a terminal. The instructor described them as effectively completely different machines: one is terminal-only, and one is an application that runs in a browser. *(00:58:59)*

## 12. Passing environment variables into a container ([27.2 What is a container?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#what-is-a-container))

*00:59:20–01:02:53*

- **Q:** Compare the start-up output of the two `rocker/rstudio:4.4.2` runs, one without `-e` and one with `-e PASSWORD="apassword"`. What differs, what caused the difference, and why was it acceptable to show the password in class?
  **A:** The first run printed "The password is set to ooph3Aef2Ohcahcu", followed by a hint to set the `PASSWORD` environment variable. In the second run, `skipping /var/run/s6/container_environment/PASSWORD` appears among the environment entries, no generated password is printed, and you log in with the password you chose. The difference exists because this image was built to read `PASSWORD`; not every container reads the same variables, since that depends on how its builder set it up. Showing the password was fine because port `8787` is reachable only from the instructor's own machine. *(01:00:39)*

- **Q:** Break down the dashboard handoff the instructor described for DSCI 532. What does the builder do, what does the end user do, and which steps does the user skip?
  **A:** The builder puts the dashboard code into a container and does all of the installation in it. The end user needs only Docker. They run `docker run` with the right flags, then go to the port in their browser to reach the dashboard. They skip the whole installation process, such as setting up `renv` and the snapshot. In effect, the builder has given them a computer built from scratch. *(01:02:20)*

## 13. Starting from a base image and working inside it ([29.1.1 Workflow for building a Dockerfile](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#workflow-for-building-a-dockerfile))

*01:03:00–01:08:19*

- **Q:** The instructor ran `docker run --rm -it rocker/r-ver:4.6.2 bash` three times. Trace what happened to the `cowsay` package across the three sessions, and point out what in the terminal log shows that each session was a new machine.
  **A:** In the first session (`root@95765251a970`), `install.packages("cowsay")` inside R installed it, and `cowsay::say('hello')` drew the cow. After `exit`, the second session (`root@97a536175dca`) started with `library(cowsay)` failing again, and the package was installed once more with `Rscript -e`. The third session (`root@a642984ec391`) failed on `library(cowsay)` once more. A different container ID in each prompt shows a fresh machine each time. A container resets to how its image was built, with no saved state, so following README install steps on every start is painful. *(01:07:10)*

## 14. Running R from the command line with `Rscript -e`

*01:08:19–01:10:18*

- **Q:** Distinguish `install.packages("cowsay")` typed at R's `>` prompt from `Rscript -e "install.packages('cowsay')"` typed at the container's Bash prompt. Where does each run, what does the quoting do, and why did the class need the second form?
  **A:** The first form only works once you have started R interactively. The second runs from the shell: `Rscript` executes R code from the terminal, and `-e` passes it an R expression. The double quotes wrap the whole expression for the shell and the single quotes go around the package name inside it. Both installed `cowsay`, and both installs vanished when the container restarted. The class needed the shell form because saving the setup depends on knowing the terminal command that performs the install. *(01:09:27)*

## 15. The `Dockerfile`: `FROM`, `RUN`, `CMD` ([29.2 `Dockerfile` command summary](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#dockerfile-command-summary))

*01:10:18–01:15:01*

- **Q:** Break down the class's three-line `Dockerfile` (`FROM rocker/r-ver:4.6.2`, `RUN Rscript -e "install.packages('cowsay')"`, `CMD [...]`). What does each line contribute, and when does it take effect?
  **A:** `FROM` names the starting machine. Here it already has R 4.6.2 and the system pieces R needs, which skips steps you would otherwise do by hand. `RUN` holds the shell commands to run while the machine is being built, and here it is the same `Rscript -e` line that was tested by hand. `CMD`, written as a list instead of space-separated words, is what a container from the image runs by default when it starts: it prints "Hello from my first image!". You can override it, for example with `bash`. For a Python project, the middle section would instead install `uv`, `COPY` in the lock files and run `uv sync`. *(01:14:05)*

## 16. Building and running your own image ([29.1.2 Build your first image](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#build-your-first-image))

*01:15:01–01:18:44*

- **Q:** Trace the `hello-cowsay` image from the `Dockerfile` to a container where `library(cowsay)` loads. Which command and which lines of build output correspond to each stage?
  **A:** `docker build --tag hello-cowsay .` names the image with `--tag` and uses `.` to say the file named `Dockerfile` is in the current directory. That is why commands assume you run them from the repository root. The build output lists `[1/2] FROM docker.io/rocker/r-ver:4.6.2` and `[2/2] RUN Rscript -e "install.packages('cowsay')"`, and ends with `naming to docker.io/library/hello-cowsay:latest`. `docker images` then lists `hello-cowsay:latest` among the images on the machine. In `docker run --rm -it hello-cowsay bash`, R loads `cowsay`, because the build installed it into the image itself. *(01:17:52)*

- **Q:** Distinguish `docker run --rm -it hello-cowsay` from `docker run --rm -it hello-cowsay bash`. What does each run, what did each produce, and when is the second one useful?
  **A:** Without a command after the image name, the container runs the `Dockerfile`'s `CMD`, so the cow printed "Hello from my first image!" and the container exited. Adding `bash` replaces that default and drops you at the container's shell, where you can open R and check that `library(cowsay)` loads. Shell access is useful when code works on your machine but not in the container, because you can poke around inside the container directly. *(01:17:30)*

## 17. Pinning versions, and what comes next

*01:18:44–01:20:39*

- **Q:** Break down where each layer of a project's environment gets pinned in a `Dockerfile`, following the instructor's plan for next week's project container. Then relate that plan to the failure he described from another class.
  **A:** The `FROM` line pins the language: `rocker/r-ver:4.6.2` fixes the R version. A section after it holds the `renv` or `uv` setup that installs the packages. Tools such as Quarto get an explicit version in their install line, even an older one, so a year later you are still on the same versions as long as you don't touch that line. In another class a few weeks earlier, the instructor restarted a container that had no hard-pinned versions. Something had updated the day before, nothing worked, and fixing it could cost hours that should have gone to the actual work. Pin every version, and change one only when you mean to. *(01:19:55)*

---

- prompt: prompt-recall-4-analyze.md @ 8bcc190
- prompt-hash: ccb0e5a939c5
- model: claude-opus-5-5 (requested: opus)
- backend: claude
- inputs: transcript-plaud.md, history.txt, terminal.txt, materials.md, notes-class-main--claude-opus-5-5.md
- generated: 2026-11-20
- notes-input: notes-class-main--claude-opus-5-5.md @ 1c708a29f65f, links and section references removed
