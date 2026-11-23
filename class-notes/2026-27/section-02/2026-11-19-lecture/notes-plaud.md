> Date Time: 2026-11-19 09:29:55
>
> Location: [Insert Location]
>
> Instructor: Daniel Chen

## Summary

The lectures combine project guidance, Git and GitHub workflows, and a practical introduction to Docker. Students are encouraged to keep their data analysis and models simple while using technically appropriate methods. GitHub branches, issues, and pull requests are presented as tools for collaborating, organizing work, and connecting tasks.

The Docker material explains how containers provide stable, shareable computing environments that include more than project package versions: they can also specify tools, system components, and setup instructions. The lectures cover pulling and running images, using interactive terminals and browser-based applications, mapping ports, passing environment variables, and building customized images with a Dockerfile. Containers support reproducible work across computers and over time, while interactive changes disappear unless they are included in the image’s build instructions.

## Knowledge Points

### 1. Project scope and data analysis

- **Keep the analysis simple and technically correct**
  - This is not primarily a model-fitting course, so avoid unnecessary complexity. If a straight-line model fits the task, use one rather than adding a neural network just for complexity.
  - Simple linear or logistic regression is acceptable, but the method must match the outcome. For example, logistic regression is not appropriate for predicting a numeric outcome.
  - Model performance is not the main focus. A model that is 60% accurate is not automatically a problem if the data science and machine-learning techniques are technically correct.
  - Do not turn the assignment into a portfolio project. Students who want a portfolio project can work on one separately.
- **Complete the requested components without overbuilding**
  - The work may include code to download data, data cleaning, exploratory data analysis (EDA), modeling, figures, tables, and a report. Keep these components straightforward and follow the assignment’s instructions for the requested report detail.
  - The project is developed over approximately three or four weeks. Students should begin with a machine-learning project even though the lectures contain relatively little machine-learning code.
  - The lecture described the week of November 19, 2026, as focused on getting everything on Git, and the following week, November 26, 2026, as focused on containers. Individual assignments provide short practice for the main assignment; a later assignment includes a very simple data analysis.

### 2. Git and GitHub workflows

- **Use branches to make changes**
  - The practical exercise is to create or use a repository, bring it onto the local computer, edit a file, and open a pull request. The example adds “Today we will talk about containers” to the README.
  - Check the active branch with `git status` before staging or committing, especially to avoid making changes directly on `main`. If work has already been committed on `main`, the textbook includes a cheat sheet with commands for moving it.
  - The demonstrated workflow is to create a branch with `git switch -c today`, check the branch and working tree with `git status`, review changes with `git diff`, stage the README with `git add README.md`, commit with a descriptive message, and push the `today` branch.
  - In an active collaboration, pull the latest `main` branch before beginning work so that changes are based on an up-to-date version.
- **Use GitHub issues to plan and track work**
  - Issues can record tasks, ideas, plans, meeting notes, and responsibilities. Meeting action items can be recorded in notes and split into issues assigned to individuals.
  - Issues are also useful for longer-term ideas or stretch goals that are not part of the immediate assignment.
  - Students are expected to create three issues to practice using the project-board system. Not every issue needs to be closed by the end of class.
- **Connect issues and pull requests**
  - Issues and pull requests share one numbering sequence. Referencing an item by number, such as `#2`, creates a link that can be navigated in both directions.
  - A pull request can address one or several issues; the relationship is not necessarily one issue, one branch, and one pull request.
  - GitHub recognizes closing keywords in pull-request text. For example, `fixes #2` links a pull request to issue 2 and automatically closes the issue when the pull request is merged. The instructor also mentioned `closes`, while recommending `fixes` as the keyword they regularly use.
  - Issues may remain open for future exploration or stretch goals. The course does not require every issue to be closed.
- **Maintain useful pull-request information**
  - Issues and pull requests can be assigned to people. Pull requests can also have reviewers, such as a teammate asked to inspect the work.
  - The main pull-request description should explain what the change does and include relevant issue references. Keep it current so readers can understand the work without reconstructing it from later discussion.
  - Markdown checkboxes can track remaining tasks. A draft pull request can indicate that work is not yet ready.
- **Update and optionally clean up branches after merging**
  - After a pull request is merged, check the state with `git status`, switch to `main` using `git switch main`, and pull the latest changes.
  - GitHub offers an option to delete the remote branch after merging, or it can be deleted from the branches view. This cleanup is optional; teams may have different workflows, and retaining branches can provide convenient references to past work.
  - Deleting a remote branch does not automatically remove its local reference. Use `git fetch --prune` to remove references to remote branches that no longer exist, then optionally remove a local branch with `git branch -d <branch-name>`. This does not erase the merged history.
  - Keeping a local branch name can be more convenient than navigating to a commit hash. Cleanup may help when many branches make Git output difficult to follow.

### 3. Why containers are useful

- **Projects need tailored, minimal environments**
  - Projects may last weeks, months, or years and may use different languages and tools. Students can choose R or Python, and visualization tools might include Altair, Plotly, or Matplotlib.
  - Package lists should include only what the project needs. Unused packages waste disk space, and installing many packages can lead to compatibility problems as packages update on different schedules.
  - In real-world projects, users need to adapt the environment to the project rather than rely on one standard package set.
- **Reproducibility across people, computers, and time**
  - A project that runs on one person’s machine may fail on another’s because collaborators use different operating systems, hardware, or processor architectures, such as ARM or Intel.
  - UV and “RM,” as referenced in the lecture, help keep required packages consistent. Lock files record package versions, but do not necessarily include all the instructions, tools, or system components needed to reproduce the environment on another computer.
  - Containers provide a broader, shareable environment. They can also support modular pipelines so collaborators can use different parts of an analysis, not just its final report.
  - Containers bridge local development and remote computing environments that may have more memory, processor cores, or access to project data.
- **Containers compared with virtual machines**
  - A container is a stripped-down computing environment containing the software and tools needed for a task. It typically does not include a full graphical operating system.
  - A virtual machine typically runs a full operating system, such as Windows, with a graphical interface. Containers are generally lighter and more resource-efficient, though they still add a layer and can incur a performance cost.
  - The lecture contrasted virtual-machine installations that might use 50 or 80 GB with class containers that may be under 2 GB or even under 1 GB. Virtual machines remain useful for some purposes, such as testing an MDS installation in Windows.
  - Containers can act as sandboxes: if an environment is damaged, it can be restarted or replaced. They are also useful for experimenting with operating systems or command-line tools without changing the local computer.
  - Docker is the container tool used in class. LXC, LXD, and Podman were mentioned as alternatives. Cloud computing commonly uses containers or similar environments rather than providing unrestricted access to a physical machine.
- **Pinning tools and preserving long-running analyses**
  - Docker can preserve specific tool versions, not just project package versions. For example, a Docker image can provide R 4.3.2 even if the host has a different version, allowing multiple R versions to be used without installing each directly on the computer.
  - The lecture also noted that system-tool versions affect available commands: a container with a 2019 version of Git, for example, would not support `git switch`.
  - Stable environments can be important for long-running or regulated research. A clinical-trial analysis may span several years while R updates about every six months. Repeatedly changing or revalidating the environment may be undesirable.
  - For a drug submission to the relevant Canadian regulator, described in the lecture as the Canadian equivalent of the FDA, submitted materials may need to include code and the computing environment so the work can be reproduced.
  - Lock files preserve package versions; containers can additionally preserve the tool itself and potentially system-level tools.

### 4. Docker commands and running containers

- **Pulling and running images**
  - `docker pull <image>` downloads a container image to the local computer. Image names resemble a username and repository, such as images provided by Docker for R. Docker may report that an image is already up to date and can identify a specific image version with a hash.
  - The word `pull` is similar to `git pull`: both retrieve something onto the computer.
  - `docker run <image>` starts a container. If the image is not available locally, Docker downloads it. Additional flags can determine how the container runs.
  - Docker Desktop must be open before running the class commands. If Docker cannot be found, install Docker; if it is installed but not running, the commands will prompt the user to start it.
  - The instructor directed students to find three Docker commands in Slack and run them; the setup was expected to take about ten minutes.
- **Flags, terminals, and host-versus-container behavior**
  - Double-dash options introduce longer flags. In the example, `--rm` removes a container when it stops. Without it, the container may need to be removed manually.
  - Single-dash flags are typically single-letter options and can be combined. For example, `ls -a -l -h` shows all files, lists them, and uses human-readable sizes.
  - `-i` enables interactive input and `-t` allocates a TTY; they are often used together for an interactive terminal. `docker run --rm -it <image>` is a demonstrated pattern.
  - A container behaves like a separate computer on the same physical hardware. An R container with R 4.3.2 runs that version rather than the host’s version. Typing `R` in a separate host terminal starts the host’s version, if installed and available on its path. Windows may require different path handling.
  - The R container initially did not have `tidyverse`, so `library(tidyverse)` failed there even though it worked in the host’s R environment. This demonstrates that the host and container have separate software and packages.
  - Check the terminal prompt or other interface cues to determine which machine is active. Commands such as `who am I?` can help identify the current username. Confirm the active environment before running commands, especially on remote systems.
  - Running containers use memory and other resources. Shut down containers that are no longer needed; several running containers can make a computer unresponsive.

### 5. Browser-based applications, ports, and environment variables

- **Accessing applications through a browser**
  - Applications such as RStudio and Jupyter Lab can run inside containers and be accessed through a browser. The browser provides a familiar interface while computation runs in a separately configured environment, locally or remotely.
  - Jupyter Lab was described as commonly running at `localhost:8` in the lecture. VS Code and GitHub Codespaces were also mentioned as examples of familiar interfaces connected to separate computing environments.
  - The instructor demonstrated `rocker/rstudio:4.2`, accessing its browser-based RStudio through `localhost:8787`. This was separate from RStudio installed on the host.
- **Mapping ports**
  - Docker’s `-p` option maps a host port to a port inside the container. Mapping host port `8787` to container port `8787` allows a browser to connect through `localhost:8787`.
  - Port numbers are selected by the application and are not inherently special. RStudio and Jupyter Lab use different ports; other tools use others.
  - Multiple instances can run concurrently if they use different host ports. The lecture gave an alternate host-port example transcribed as `61.11`; users must connect through whichever host port they map.
- **Passing environment variables and sharing applications**
  - Docker’s `-e` option passes environment variables into a container. In the RStudio example, `PASSWORD` was set to a chosen password. The available variables and default username depend on how the image was configured and documented.
  - A containerized dashboard or other application can be shared through a port, allowing end users to run it without separately installing all its dependencies. Users still need Docker but can run the prepared application with the relevant `docker run` options.
  - The lecture noted that containerized browser-based applications may be useful when a graphical interface is desired, though students may not need to install Jupyter Lab independently for the current course.

### 6. Building a customized container

- **Interactive changes are temporary**
  - The instructor demonstrated installing the R package `cowsay`, which provides ASCII-art output, and loading it with `library(cowsay)`.
  - Packages installed interactively are not retained when a container is stopped and restarted. A fresh start returns the container to its configured state unless the setup instructions preserve the changes.
  - This reset behavior is useful for experimentation, but manually reinstalling dependencies every time is inconvenient. The instructor contrasted a potentially 15-minute `tidyverse` installation on an improperly configured Linux machine with an analysis that may take only 30 seconds.
- **Dockerfile instructions**
  - A `Dockerfile` (capital **D**) contains instructions for setting up an environment. Existing R and RStudio images already have their own setup instructions.
  - `FROM` specifies the base image and is typically the first Docker instruction. The example `FROM rocker/r-ver:4.6.2` starts from an image with R 4.6.2 installed.
  - Smaller, minimal Linux images are possible but require more components to be installed manually. A somewhat larger base image can be a reasonable choice.
  - `RUN` executes shell or Bash commands while the image is being built. `Rscript -e` can run an R expression from the terminal. The instructor demonstrated using it to install `cowsay`; the shell example used double quotes outside and single quotes inside.
  - `CMD` specifies the default behavior when the image runs without an overriding command. The example printed “hello from my first image.” `ENTRYPOINT` is another instruction, described as less common and suited to specific cases.
  - Dockerfiles can also use instructions such as `COPY` and multiple `RUN` steps. For a Python environment, for example, files such as lock files could be copied in and `uv sync` run to install packages. Depending on the image, port instructions may also be needed; port `8787` was given as an example.
- **Building and testing an image**
  - `docker build` creates an image from a Dockerfile. The `-t` option assigns a name or tag. The example command was `docker build -t hello-cowsay .`; the final `.` tells Docker to look in the current directory for the file named `Dockerfile`.
  - A full path can be supplied, but commands are commonly run from the project root, consistent with course working-directory conventions.
  - `docker images` lists images available locally. `docker run --rm hello-cowsay` runs the image. Adding `bash` opens a terminal inside the container for testing or investigation.
  - The instructor also demonstrated `docker run --rm -it` with an R image intended to use R 4.6.2, opening a shell rather than launching R automatically. From the shell, users can test setup steps and start R by typing `R`.
  - The general workflow is to start from a base image, add the commands and files needed to configure it, and build the result. Testing setup steps interactively first can help before documenting them in the Dockerfile.
- **Version pinning and upcoming setup**
  - Specifying versions in a Dockerfile keeps tools and packages consistent until the setup instructions are deliberately changed. The lecture gave a “Cordova” example: a project using version 1.11 could instead select version 1.10 and continue using it while the instruction remains unchanged.
  - Pinning helps prevent unexpected updates from breaking a project. The instructor described another project where a tool updated shortly before work, causing the project to stop working because versions had not been pinned.
  - In the next class, students will set up a container for the language they use (R or Python), install Quarto and project packages, and configure the environment so the analysis can run locally and inside the container. Copy-and-paste setup instructions will be provided. The lecture also mentioned an “RM setup” placeholder for installing, snapshotting, and loading packages.
  - Container material will continue in the next class, including connecting multiple containers. No container work is required for this week’s lab assignment.

### 7. Brief event discussion

A participant mentioned a tentative event scheduled for Saturday, November 21, and Sunday, November 22, 2026, and considered attending or filling a slot at the last minute. The discussion referred to image recognition and an idea of reproducing published medical research before attempting a more complex version, with the goal of experimenting with tools and seeing what produced results. Attendance plans and event details were not confirmed.

## Questions

- [Insert Question/Confusion]

## Assignments

- [ ] 1. Run the Docker setup commands provided in Slack with Docker Desktop open; install Docker if it is not available.
- [ ] 2. Complete the Git practice exercise: create or use a repository, create a branch, edit the README, check the branch and changes, commit, push, open a pull request, and merge it.
- [ ] 3. For the class project, create three GitHub issues to practice tracking work, responsibilities, and ideas. Link relevant issues to pull requests and use closing keywords such as `fixes` when appropriate.
- [ ] 4. Follow the assignment steps and build the project over approximately three or four weeks. Keep the analysis and model simple, use technically correct methods, and include the requested code, figures, tables, and report details.
- [ ] 5. After merging a pull request, switch to `main` and pull the latest changes. Optionally delete the merged remote branch and clean up local references with `git fetch --prune` and `git branch -d <branch-name>`.
- [ ] 6. Practice running containers with the demonstrated Docker options. Check the terminal prompt or other cues to confirm whether commands are running on the host or inside a container.
- [ ] 7. If using a browser-based application, map its container port to a host port and access it through `localhost`. Use different host ports for concurrent instances.
- [ ] 8. When developing a custom container, test setup steps interactively from a terminal, then document them in a Dockerfile so the environment can be rebuilt.
- [ ] 9. For next week, prepare to build a container for the project’s language (R or Python), install Quarto and project packages, and configure the environment to run the analysis locally and in the container. Follow the provided setup instructions. No container work is required for this week’s lab assignment.
