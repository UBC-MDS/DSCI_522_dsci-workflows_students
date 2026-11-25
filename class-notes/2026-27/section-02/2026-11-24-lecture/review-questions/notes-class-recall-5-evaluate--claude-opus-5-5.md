# Building a Python analysis image with uv, volume mounts and Docker Compose: review questions, tier 5 — Evaluate

Date: 2026-11-24

Instructor: Daniel Chen

*Tier 5 of 5: Evaluate. Decide and justify your verdict before you read the answer; the criteria are the ones given in class.*

## 1. Letting Claude Code build the repository

*00:07:21–00:11:24*

- **Q:** A student who has never used Docker plans to skip the terminology and just ask a coding agent to "go make a container for my project." Judge whether this is a sound plan.
    - **A:** It is not sound. The instructor's point was that you need the vocabulary, such as Dockerfile, image and the exact image name, to put in the prompt. Those words are what steer the agent toward the correct answer. If you don't know the words around what you are building, "that's going to be a problem." *(00:08:06)*

- **Q:** Claude Code reports that it created the `2026-11-24-docker` repository, built the image and tested it. Assess whether you can accept the result without looking at it.
    - **A:** You should not accept it unchecked. In class the agent created the folder under `~/temp` instead of `~/git`. It also added a `README.md`, a `Makefile` and a `CMD ["R"]` line that nobody asked for in the prompt. The instructor had to check where the folder went and what the `Dockerfile` contained before using it. *(00:10:11)*

## 2. Listing and building images ([29 Customizing and building containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html))

*00:12:42–00:16:40*

- **Q:** A teammate's README tells people to build with `docker build --tag 2026-11-24-docker`, with no trailing `.`, arguing that Docker looks for a file called `Dockerfile` by default anyway. Would you approve this README?
    - **A:** No. `docker build` does look for a file named `Dockerfile` by default, but you still have to tell it where to look. It is like a function argument with no default, so you cannot leave it empty. The `.` means "here", the current directory; it is not a full stop, and the class was warned not to forget it. *(00:14:57)*

## 3. Running a container, overriding `CMD`, and throwaway containers ([28 Using and running containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html))

*00:16:40–00:20:07*

- **Q:** You want to try installing PyTorch but worry it might wreck your setup. One teammate says to install it on your laptop and uninstall it if things break. You propose trying it in `docker run --rm -it <image> bash` first. Which plan would you defend?
    - **A:** Trying it in the container is the better plan. With `--rm`, every change inside the container is undone when you exit, like a version of Git that automatically resets your changes. If the install goes wrong, you restart the container and nothing bad has happened to your computer. *(00:19:58)*

## 4. Choosing a base image for a Python project ([29.3 Choosing a base image for your Dockerfile](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#choosing-a-base-image-for-your-dockerfile))

*00:20:07–00:24:22*

- **Q:** A group's project uses only Python, but their `Dockerfile` still says `FROM rocker/r-ver:4.6.2` because "it already builds." A pull request changes it to `FROM ubuntu:24.04`. Would you approve the pull request?
    - **A:** Yes. The R image carries a lot of software installed for R that a Python project does not need. The instructor asked students to keep images small out of respect for other people's disk space, which has become expensive. *(00:23:55)*

- **Q:** A teammate argues that the group should use Alpine instead of `ubuntu:24.04` because a smaller image is always better. Assess this argument.
    - **A:** It is not automatically better. Alpine is even smaller, but it may mean installing more software yourself, depending on what you need. The class treated Ubuntu as a pretty good starting point that balances size against convenience. *(00:24:13)*

## 5. Installing `uv` with `COPY --from`, and setting `WORKDIR` ([30.2 A `Dockerfile` for a uv project](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv.html#a-dockerfile-for-a-uv-project))

*00:24:22–00:27:42*

- **Q:** A `Dockerfile` has no `WORKDIR` line, so every container from it opens at `/`. Its author says that is fine because you can always `cd` yourself. Would you accept it?
    - **A:** It is better to add `WORKDIR /workspace`. Starting at `/` puts you among the operating system's files. If you move a folder or mess something up there, everything can stop working. Setting the working directory lands everyone in a folder just for the project. *(00:26:10)*

## 6. Pinning exact versions in `pyproject.toml` ([22 uv: pinning exact versions](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/virtual-environments-python-uv-exact-pins.html))

*00:29:58–00:33:35*

- **Q:** A group's `pyproject.toml` lists `cowsay>=6.1` for a project that will run all term. A teammate says that is fine because it works today. Is it acceptable?
    - **A:** No. With `>=`, a rebuild next week could pull in cowsay 7.0. A change in the first version number usually breaks backwards compatibility, so behaviour you rely on in 6.x may not work in 7.x. Pin with `cowsay==6.1`, and set `add-bounds = "exact"` under `[tool.uv]` so that `uv add` writes `==` from now on. *(00:31:06)*

- **Q:** To be safe, a teammate proposes listing every transitive dependency in `pyproject.toml` with `==`. Critique the proposal.
    - **A:** It goes beyond what the class set out. `pyproject.toml` holds the explicit versions you care about, and the resolver picks compatible versions for everything else. You add a downstream package only when it actually causes trouble, as the instructor did when a dependency far below pandas updated and broke it. *(00:33:16)*

## 7. Copying the environment files and `uv sync --locked` ([30.2 A `Dockerfile` for a uv project](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv.html#a-dockerfile-for-a-uv-project))

*00:35:01–00:39:25*

- **Q:** A group whose analysis uses PyTorch deletes `.python-version`, arguing that `requires-python = ">=3.14"` in `pyproject.toml` already covers it. Would you approve this change?
    - **A:** No. The Python version decides which package versions can be installed. PyTorch is almost never compatible with the latest Python, so you usually have to pin an older version to get it installed. `.python-version` pins the interpreter the way `uv.lock` pins the packages, so `uv` doesn't simply take the newest Python. *(00:35:59)*

- **Q:** The build stops at `RUN uv sync --locked` because someone edited `pyproject.toml` by hand. A teammate proposes deleting `--locked` so the build goes through. Judge this fix.
    - **A:** Reject it. `--locked` exists to throw an error when `pyproject.toml` and `uv.lock` are out of sync. That is what you want: the build should fail loudly rather than produce something you didn't expect. Bring the two files back in sync instead. *(00:38:55)*

## 8. Building the image and layer caching ([29.1.3 Layer caching](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#layer-caching))

*00:39:25–00:44:33*

- **Q:** A `Dockerfile` puts `COPY hello.py ./` above `RUN uv sync --locked`. Would you approve it in a pull request?
    - **A:** No. Changing a layer reruns every step below it, so each edit to the script would rerun the slow `uv sync`. Put slow, rarely changing installs at the top and fast-changing code at the end. In class, appending `COPY hello.py ./` as the last line rebuilt in under a second because `uv sync` stayed cached. *(00:42:40)*

- **Q:** A reviewer rejects a beginner's `Dockerfile` because it uses several separate lines instead of one combined command. Is that a fair reason to reject it?
    - **A:** No. Combining steps saves a bit of disk space and is more efficient, but it doesn't affect the outcome. The instructor said there is nothing wrong with having more lines when you are starting out with Docker. *(00:41:59)*

## 9. Why not bake your code into the image

*00:49:36–00:53:26*

- **Q:** For the milestone, a group adds `COPY . .` to its `Dockerfile` so the analysis code ships inside the image, and plans to rebuild whenever the code changes. Assess this plan.
    - **A:** It is a poor fit for work that is still changing. The code gets snapshotted into the image, so anyone opening the container has to ask when the code was copied, and by which teammate. Every change then needs a commit, a push and a rebuild, which doesn't scale. The goal is to separate compute from source code: the image holds the software and packages, and the code stays outside it. *(00:51:16)*

## 10. Mounting the project folder with `-v` ([28.1.2 Mounting volumes to containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#mounting-volumes-to-containers))

*00:53:26–00:59:33*

- **Q:** Instead of mounting, a teammate proposes installing Git in the image and cloning the repository from inside each new container. Judge this approach against mounting with `-v "$(pwd):/workspace"`.
    - **A:** Cloning is valid with what you knew before this class, and the instructor has done it, but mounting is better. Git in the container needs its own SSH key or personal access token. Every rebuilt container makes a new key that you would have to register again. Mounting avoids that problem entirely, because you edit the same files your laptop already handles with Git. *(00:54:52)*

- **Q:** A teammate wants the live shared folder set up inside the `Dockerfile`, so nobody has to type `-v` at `docker run`. Assess whether this can work.
    - **A:** It can't. Mounting happens in the run process, not the build process. A build can only copy files, which gives you a snapshot rather than a folder shared with your computer. *(00:56:06)*

## 11. Keeping the image's environment in `/opt/venv` ([30.5 Why the packages go in `/opt/venv`](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-uv.html#why-the-packages-go-in-optvenv))

*00:59:33–01:06:53*

- **Q:** A teammate removes `ENV UV_PROJECT_ENVIRONMENT=/opt/venv` from the `Dockerfile` because `uv run hello.py` still printed the cow in a mounted container on their Mac. Would you approve this change?
    - **A:** No. Without the line, the mount hands the Linux container the laptop's `.venv`, which was built for one operating system and CPU architecture. Teammates may differ in both, and the instructor compared this to copying an Excel file from a Mac to Windows and hoping it runs. In class, `uv` deleted and rebuilt the mounted `.venv`, which changed the folder on the laptop itself. With the `ENV` line, the container uses its own Linux environment in `/opt/venv`. *(01:02:40)*

- **Q:** A `Dockerfile` sets `ENV UV_PROJECT_ENVIRONMENT=/opt/venv` on the line after `RUN uv sync --locked`. Is it correct?
    - **A:** No. The position of the line is flexible only as long as it comes before `uv sync`. Placed after it, `uv sync` has already installed the environment in the default `.venv` location. *(01:03:56)*

## 12. Docker Compose ([33 Containers: Docker Compose](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-docker-compose.html))

*01:06:53–01:14:06*

- **Q:** A team keeps its growing `docker run --rm -it -v "$(pwd):/workspace" ...` command in a chat message for everyone to paste. Someone proposes a `docker-compose.yml` instead, and another says Compose is overkill for one container. Decide which approach the team should adopt.
    - **A:** Adopt the `docker-compose.yml`. Pasted commands are hard to edit because you can't click inside them. A file can be version controlled and its changes tracked, so the team relies on simple commands instead of copy and paste. The instructor granted that Compose is mainly for running several containers and may be a bit of overkill for one, but called it still very useful. *(01:11:28)*

## 13. This week's milestone: a Dockerfile for your analysis

*01:14:06–01:17:04*

- **Q:** A group checks its milestone only by running `uv run quarto render` on their own laptops, and the report renders. Judge whether that shows the milestone is done.
    - **A:** It does not. The TAs take your repository, build the container, and try to run the analysis inside it. The group has to confirm that, with the needed folders mounted, `uv run quarto render` renders the report inside the container. *(01:15:01)*

- **Q:** A teammate adds a long list of extra `RUN` installs to the group's image "just in case." Assess this addition.
    - **A:** Extra tools are allowed, but this justification falls short. Adding a text editor, or system libraries that some packages need (for example for geospatial work), is fine. The instructor's condition was that you know why you add each one. *(01:16:03)*

---

- prompt: prompt-recall-5-evaluate.md @ 65eb21c
- prompt-hash: 6b82591e2f8e
- model: claude-opus-5-5 (requested: opus)
- backend: claude
- inputs: transcript-plaud.md, terminal.txt, materials.md, notes-class-main--claude-opus-5-5.md
- generated: 2026-11-24
- notes-input: notes-class-main--claude-opus-5-5.md @ 0caf0d47e007, links and section references removed, diagrams removed
