[](plaud://image?type=summaryCard&id=c_01a2108943a07323b98b9745b2805e77)

[](plaud://highlight-card?title=Highlight%20Summary&detail=Detail)

**A classroom lecture by instructor Daniel Chen with student questions** covered Docker builds, Python environments, and running analysis inside containers. The central goal is a reproducible compute environment that can be shared without requiring everyone to set it up by hand.

## Course materials and Docker setup

The exercise began with a review: create a GitHub repository containing a Dockerfile that uses the specified image. Daniel also planned to try a similar task with a Cloud Agent. He showed updates to the course website and reviewed Docker startup requirements.

- **Course materials**: The website now includes material from Sky’s class, including her slide decks and summary notes. Transcripts and links remain on the private side; students no longer need the GitHub UBC student repository to find the summaries.
- **Optional notes**: The notes include comparisons between language models and lecture questions organized at different levels of Bloom’s taxonomy, from factual recall to questions that require understanding how things work. Daniel offered them as a possible template for other classes, but said students were not required to read them. The command-history page may be enough for some.
- **Docker Desktop**: Students should make sure Docker Desktop is running before using Docker commands. Without it, commands may fail and prompt them to start Docker.
- **Starting point**: Daniel created a new repository for the class exercise and used Claude to create a Dockerfile. He stressed that effective prompts rely on knowing terms such as “Dockerfile” and naming the intended image; vague instructions like “make a thing” give an agent less to work with.

## Docker image build and run — reviewing the R container

The first build showed how an agent creates an image and how Docker commands work. The generated files and commands were useful to inspect, but Daniel noted that Claude started in a different folder and created the repository in a temporary location rather than the intended one.

- **Generated files**: Claude created a Dockerfile, a README, and a Makefile. Daniel said only the Dockerfile was needed for the exercise, though the other files reflected his usual requests.
- **Agent activity**: The terminal history showed commands such as `ls`, `mkdir`, and Docker and GitHub CLI checks. Claude built the image and ran a script in the container. The demo cost **fifty cents**.
- **Default command**: The Dockerfile’s `CMD` makes R start when the container runs without another command. Users can supply another command to override that default.
- **Build command**: `docker build` uses `-t` or `--tag` to name the image. The name can be chosen by the user. The dot at the end gives Docker the current directory as its build context; Docker looks there for a file named `Dockerfile` by default.
- **Build steps**: Docker runs the instructions in the Dockerfile to make the image. The base image used the R version from the previous class. If that image is not already downloaded, retrieving it can take seconds or minutes, depending on internet speed.
- **Run command**: `docker run --rm -it` starts a container and gives the user terminal access. `--rm` removes the container when it exits. With the default `CMD`, R starts; supplying `bash` instead opens a shell.
- **Container filesystem**: The shell starts at the root of the container, where system files are visible. The class container has no user assigned in the home directory. Daniel described its setup as a shared analysis environment, not a public-facing service.
- **Temporary changes**: Once a container started with `--rm` exits, its changes are discarded. Daniel compared this to a disposable environment for testing software such as PyTorch: if a test goes wrong, users can restart the container.

## Python environment — packages, versions, and project files

The class will focus on Python because students are working on Python projects. Daniel used Ubuntu 24.04 as the base rather than the R image, which carries extra R software. He also noted that a single project can use more than one language; the textbook example supports both R and Python.

- **Base image**: Ubuntu is a common Linux starting point for containers. Alpine is smaller, but may require installing more software. Daniel urged students to keep images small to limit disk use.
- **Installing UV**: The Dockerfile uses `COPY` to take UV and UVX from an existing image and place them in the container’s `/usr/local/bin` directory. Installing UV in the container helps make the environment reproducible for someone who has not configured Python or UV on their own computer.
- **Working directory**: `WORKDIR` sets the container’s starting directory. The example uses `/workspace`, so users do not start at the root of the filesystem. Daniel connected this to the working-directory concept students have used in Python and R.
- **Project files**: The setup uses `pyproject.toml`, `uv.lock`, and `.python-version`. The first holds project metadata and package requirements; the lock file records resolved package versions; `.python-version` specifies the Python version to install.
- **Adding a package**: The example initializes a project with `uv init --bare`, then adds a package either by editing `pyproject.toml` or running `uv add`. The transcript’s package name is unclear, but the example showed it at version **6.1**.
- **Version constraints**: A `>= 6.1` requirement could admit version 7.0 after a rebuild. Daniel said a change in the first version number typically signals a backward-incompatible change, which could break a long-running project. For packages that must remain consistent, he recommended pinning an exact version, such as `== 6.1`.
- **Locking and dependencies**: `uv.lock` pins resolved versions, but it is generated from `pyproject.toml`. The project file should specify versions that matter; the dependency resolver can select compatible versions for the rest. A downstream dependency may still change and cause a problem, so some projects also pin those dependencies.
- **Python version choice**: The Python version can affect which package versions are available. Daniel cited PyTorch as an example that is often not compatible with the newest Python release. Pinning Python can help avoid that issue.
- **Testing new Python releases**: Package authors can use `.python-version` to test release candidates or upcoming Python versions. Daniel said supporting those versions is part of ensuring a package works for its users as Python changes.
- **Example program**: Daniel showed a short Python file that imports the example package and prints an ASCII cow greeting. On a local computer, `uv sync` sets up the environment, and `uv run` runs the file in it.

## Building the Python image — syncing dependencies and using the cache

The Dockerfile needs the project files and installation steps that reproduce the local environment. Daniel showed that Docker can reuse unchanged build layers, which affects how files and commands should be ordered.

- **Copying setup files**: The Dockerfile copies the project files into `/workspace`. The build then runs `uv sync` with a lock-checking option. Daniel said it errors if the project file and lock file are out of sync, rather than silently building from inconsistent inputs.
- **Build result**: The build copied the files, set the working directory, and ran the sync step. When Daniel entered the resulting container, it opened in `/workspace` and showed the copied files and the Python environment.
- **Layers and cache**: Docker caches build layers. Unchanged steps can use their cached versions; a change to one layer requires rebuilding the steps after it. Fewer layers can save disk space, but having more Dockerfile lines is fine, especially when they make the environment and code easier to distinguish.
- **Order of operations**: Daniel recommended placing slow, relatively stable installation steps before files that change often. Then a small code edit need not rerun a long dependency installation.
- **Code change test**: After Daniel copied the example Python file later in the Dockerfile, rebuilding was quick because Docker did not rerun `uv sync`. The file was available in the container, where he ran it with UV.
- **Sharing the setup**: Students can build an image from the Dockerfile. Daniel said a later class would cover publishing an image so others can use `docker pull` rather than build it themselves.

## Live code in a container — mounting the project folder

Copying code into an image snapshots it at build time. Daniel presented a volume mount as a way to keep the software environment in the image while using the current project files from the host computer.

Copying the full project into the image would make active development cumbersome: users would need to track which version was copied, commit and push changes, then rebuild to update the container. Installing Git inside the container is possible, and Daniel has used that approach when he wanted to reproduce a student’s terminal experience. For this class’s purpose, he recommended separating installed software from source code.

- **Volume mount**: The `-v` option mounts a host folder into the running container. Daniel’s example maps the current working directory to `/workspace`.
- **Live changes**: The container and host then use the same files. A change made in one is visible in the other without rebuilding the image. Daniel said this is a shared folder, not a cloud-sync copy.
- **Using Git on the host**: The mount avoids having to set up Git credentials inside a disposable container. Daniel noted that container-based Git use can require SSH keys or access tokens, and that rebuilding containers can make key management cumbersome.
- **Editor refresh**: Positron may not notice that a file changed on disk, so users may need to refresh it. The files themselves remain shared.
- **Testing**: Students can run their analysis locally and in the container. The mounted code lets them test the container setup against current changes without rebuilding it each time.
- **Required build files**: The project and lock files still need to be copied into the image because the image build uses them to install the environment. The source code itself can be mounted at run time.

## Cross-platform dependencies — keep the container’s environment separate

A mounted virtual environment can overwrite the one created in the Linux image. That can cause problems when the host and container use different operating systems or processor architectures.

- **Platform differences**: Daniel described AMD64 and ARM64 as different processor architectures, and Windows and Mac as different operating systems. He counted four combinations across those systems, or six if Linux is included.
- **Lock-file scope**: A UV lock file can contain package information for other systems, but a local `uv sync` installs for the current system. A build inside the container resolves and installs for Linux.
- **Risk from mounting `.venv`**: Mounting the project folder can place the host’s `.venv` over the image’s environment. A virtual environment built for one operating system or architecture may not work on another. Daniel said simple packages may not expose the problem, but packages such as pandas or software that uses compiled code are more likely to.
- **Separate environment path**: The Dockerfile sets UV’s project-environment variable before running `uv sync`, directing the installed environment to `/opt/venv` instead of the project’s `.venv` folder. UV then uses that location, even when the host folder is mounted over `/workspace`.
- **Rebuild after the change**: Moving the setting earlier in the build means Docker must rerun the steps below it. The rebuilt container uses its Linux environment rather than the mounted host environment, making it portable across the systems Daniel described.

## Docker Compose — save run settings in a file

The Docker run command grows as users add mounts and other settings, such as port forwarding for JupyterLab or RStudio. Daniel introduced a Compose YAML file as a version-controlled place to store those settings.

- **Service definition**: The file begins with `services` and defines a container, with a name chosen by the user. It can describe more than one container.
- **Settings**: The class example specifies the build, image, and volume. A service may also specify ports; the example left out extra mounts that the class would cover later.
- **Multiple services**: Compose is useful when an application has separate parts, such as a dashboard and a database, that need to run together but should not be combined into one container.
- **Commands**: `docker compose build` builds from the file. `docker compose up` starts the service, and `docker compose up -d` runs it in the background.
- **Demo status**: The live Compose demo did not work as intended. Daniel said he would fix it for the next class. He explained that Compose was meant to apply the settings that would otherwise go into the Docker run command. [](plaud://source?type=summary&fileId=f_01a210526f8b78b1a1f88f0fe240685f&start_time=4393250&end_time=4444840&displayLabel=1&transcriptType=polish)

## This week’s analysis container — required work and grading

The main assignment is to create a Dockerfile for the analysis environment. The teaching assistants will build the image from each repository and try to run the analysis inside it.

- **Required result**: The container should reproduce the analysis’s compute environment. Students should mount the necessary folders and run `uv run quarto render` on their report.
- **Starting materials**: The analysis should already run locally, and the project should already have a `pyproject.toml`. The task is to make that project run in the container.
- **Optional additions**: Students may install other tools, such as a text editor, if they need them inside the container. Some package stacks may also need system tools from Ubuntu; Daniel gave geospatial analysis as an example.
- **Scope**: The Dockerfile is the main goal for this class. Compose is not required for the assignment; Daniel said he would return to it after fixing the demo.

## Docker Compose beyond class — examples of ready-to-run software

Daniel connected Compose to software people can run outside the course. Many open-source applications provide Compose files that specify how to start their containers.

- **Personal finance**: Actual Budget and Firefly III are personal-finance applications. Daniel showed a Compose file for Actual Budget with a service image, ports, environment variables, volumes, and a health check.
- **Starting an application**: Running `docker compose up -d` can download the image and start the application, which users can then access through its port.
- **Where to run it**: The application could run on a personal computer, an old laptop, or a computer kept at home; users could also pay for a cloud machine.
- **Other examples**: Daniel named Jellyfin for serving movies and other media, n8n for AI automation, and a recipe app that can store recipes from Instagram collections. These applications run in a browser through a port.
- **Broader use**: Compose files are useful beyond the class’s analysis environment. Users who know Docker can often start an application from its Compose file with a simple command.

## Action Items

**@students (students)**

- [ ] Create a Dockerfile that reproduces the analysis environment, mount the required folders, and render the report inside the container [](plaud://source?type=summary&fileId=f_01a210526f8b78b1a1f88f0fe240685f&start_time=4447640&end_time=4509080&displayLabel=2&transcriptType=polish)

**@Daniel Chen (instructor)**

- [ ] Fix the Docker Compose demo for the next class [](plaud://source?type=summary&fileId=f_01a210526f8b78b1a1f88f0fe240685f&start_time=4429240&end_time=4444840&displayLabel=3&transcriptType=polish)
