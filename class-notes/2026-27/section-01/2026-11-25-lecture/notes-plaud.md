[](plaud://image?type=summaryCard&id=c_01a214439a1870078c80db6d930e7c41)

[](plaud://highlight-card?title=Highlight%20Summary&detail=Detail)

**A lab lecture led by Daniel Chen** covered container setup, reproducible workflows and data checks.

## Project setup — build from a template, not a full clone

The class began with a review of the starter files and a demonstration of creating a project repository. The reference repository provides a foundation, but students should understand and take responsibility for the code they use.

- **Repository**: Create a GitHub repository, add a README, and clone it to the computer. Daniel keeps Git repositories in a dedicated `Git` folder to avoid scattering projects and nesting repositories.
- **Starter files**: Copy the `.py` file and `pyproject.toml` from the reference repository. Students can copy `uv.lock`, but Daniel recommended generating it with `uv` when possible. The template is intended as the technical foundation for course milestones; students should not copy it blindly.
- **Editor**: Use Positron, VS Code or another editor that can view and edit the project files.
- **Accountability**: Students should understand their work, including code written with AI assistance. Daniel said he may ask about any commit carrying a student’s name.

## Dockerfile — control the software and Python environment

The Dockerfile builds the container’s software environment. Daniel walked through the reference file and explained why its base image, installed tools, working directory and Python environment matter.

- **Base image**: The example starts from an Ubuntu image with R already installed. That image will work for Python work, but it takes more storage and can make downloads longer for people using the container. Choose an image that is small enough for the work required; more minimal images may require installing more components.
- **System software**: Docker `RUN` commands execute Bash commands in the container, typically a Linux environment. `apt-get` installs software on Ubuntu. The Dockerfile is where system tools such as Git, an editor, Quarto, compilers or other dependencies can be installed.
- **Quarto and project needs**: The reference includes commands to download and install Quarto, but Daniel removed that section during the demonstration to save time and space. Students’ milestone containers need the software required to run their reports.
- **Python and UV**: MDS uses UV to manage Python. Instructions found elsewhere may use different approaches, such as `requirements.txt`, and may not work if copied directly into a UV project. The container must have Python and UV available. UV can be installed by copying files from a UV container or by starting from a prebuilt UV image.
- **Version control for tools**: A project’s `pyproject.toml` does not track the UV version. Docker helps control the installed tools as well as package versions. A prebuilt UV image can replace the UV-installation step, but users may need to locate UV inside that image.
- **Working directory**: The Dockerfile sets the directory opened when the container starts. This takes users to project files instead of the operating system’s root folders; Docker creates the directory if it does not exist.
- **Separate virtual environments**: A `.venv` created on a computer may not match the container’s operating system or CPU architecture. The class may include Windows, Mac and Linux machines, as well as different CPU architectures. The Dockerfile directs UV to install packages in a separate location inside the container so UV installs the versions suited to Linux. The mounted local `.venv` is then ignored in the container.
- **Environment variables and SSH**: Tools can use environment variables stored in system or user configuration locations. The Dockerfile sets one for UV, and an SSH connection may require writing the variable to a file because SSH does not read it directly. The file also includes commands and settings for later connecting an editor to the container.
- **Dependency consistency**: Running `uv sync --locked` checks that `pyproject.toml` and `uv.lock` agree; the build fails if they do not. Daniel described the flag as a guard that helps ensure the requested dependencies match the lock file.
- **Python version**: The `.python.version` file tells UV which Python version to download for the project. This lets separate projects use different Python versions, including legacy projects, without requiring the whole computer to use an older version. Daniel noted that some large packages, such as PyTorch, can lag behind other software because their dependencies also need updates.
- **Build and run**: `docker build -t` builds an image from the current directory, represented by `.`; by default Docker looks there for a file named `Dockerfile`. `docker run --rm -it` starts the chosen image interactively and removes the container when it exits. The `-i` and `-t` flags provide interactive terminal access.

## Docker volumes — share project files without copying credentials into the image

Mounting a local folder into the container lets students edit the same files on either side without rebuilding the image for each change. It also keeps Git credentials on the host computer.

- **Live file sharing**: The `-v` flag mounts the current project folder into the container’s workspace. Changes made on the host or in the container appear on the other side. Multiple folders can be mounted with additional `-v` flags.
- **Why not copy files into the image?** Files copied during a Docker build reflect the state at build time. When project files change frequently, mounting them avoids rebuilding the container just to update those files.
- **Git credentials**: A container behaves like a separate computer and may need its own Git setup. Daniel recommended doing Git operations on the host while sharing project files through the mount. In the Compose example, an SSH key is mounted only while the container runs, rather than stored permanently in the image.
- **Container resets**: Changes to the container’s system files and installed software disappear when it is closed and rebuilt or restarted from the image. Mounted project files persist on the host. This makes the container useful as a sandbox for trying installations or other changes.
- **Editing the same file**: Changes made in one editor may not refresh an already-open copy in another. Daniel recommended using an IDE’s revert or refresh option before editing. Otherwise, saving an older copy can overwrite newer changes.
- **Submission case**: Copying files into an image can make sense when a final, fixed version must be submitted for compliance. During active development, a volume avoids repeated rebuilds.

## Docker Compose — keep container settings in a file

Docker Compose moves long `docker run` commands and their flags into a version-controlled YAML file. The file specifies how to build and run containers, including their images, ports, volumes and environment variables.

- **Services and images**: The example defines a service named `analysis-m` based on the image built from the Dockerfile. Multiple services can use the same image with different names. Compose can also specify how to build the image if it does not yet exist.
- **Ports**: A port mapping connects a port on the computer to one inside the container. In the lecture example, the local port is `2` and the container port is `22`. The first number is where to connect on the computer; the second is the container’s port. The RStudio example uses `8787`, and Jupyter may use `8888` for one instance and `8889` for another. Port numbers can match or differ, so users should check which local port the instructions use.
- **Compose commands**: In the folder containing the Compose file, `docker compose build` builds the image and `docker compose up -d` starts the specified containers in the background. `docker compose exec` runs a command, such as Bash, in a running service; `docker compose run --rm` can run a command and remove its container when finished. `docker compose down` stops the containers described in the file.
- **Resource use**: Containers use computer memory. Daniel advised stopping containers that are no longer needed, especially when several are running.
- **Why use a file**: The Compose file makes configuration easier to document, track in version control and change than a long command pasted into a terminal. It also avoids the difficulty of editing long commands in some terminals.
- **Running commands through UV**: Calling ordinary `python` inside the example container failed because Python was managed through UV. Students should use `uv run python` to access the interpreter and packages installed through that project’s UV environment. Running ordinary Python may access a different installation without those packages.
- **Testing reports**: A report can be rendered in the container with a command such as `uv run quarto`, using the project’s file. This checks whether the analysis works in the custom environment rather than only on the host computer.

## Remote editor access — work in the container or test it separately

The container can be used through a terminal, or an editor can connect to it over SSH. Daniel presented both approaches as ways to work with a separate machine.

- **Editor connection**: VS Code has a Remote SSH feature. Daniel said Positron and other VS Code forks do not have access to Microsoft’s extension store, so their connection setup differs. The example connects as `root` to `localhost` on the mapped port.
- **Two workflows**: Students can work locally and run a final test in the container, or connect the editor directly to the container and run commands there. In either case, the mounted workspace makes project files available.
- **Cloud computing**: Docker provides a small-scale example of connecting to another machine. Daniel described using Positron over a remote connection to work on a machine with 128 gigabytes of RAM for datasets that required about 100 gigabytes of RAM. He said students would not be assessed on making an editor connection, and those with limited resources should avoid running Docker unnecessarily.
- **Broader use**: Daniel said Compose is used beyond coursework to run services such as N8N, Jellyfin and Actual Budget. He demonstrated an Actual Budget configuration with services, an image, a port, environment variables and possible volumes.

## Data validation — check assumptions before modeling

Daniel introduced Point Blank and demonstrated checks on the Palmer Penguins dataset. He emphasized that validation can happen at different stages of an analysis, rather than in one block of code.

- **Setup**: The examples use Point Blank, a package written by Rich from Posit, and the Palmer Penguins dataset. Daniel had trouble adding packages with `uv add` during the demonstration. He said packages can also be added manually to the TOML file, followed by `uv sync`.
- **Missing values**: Point Blank’s missing-values table reports missingness across the dataset, and a visual view shows where gaps occur. In the example, missingness appeared more often near the beginning of the data. Daniel suggested it might reflect the collection order, or that penguins were harder to weigh at first, but did not establish a cause.
- **Thresholds**: Checks can flag missingness at selected levels, such as 1%, 5% or 10%. A small amount might be left unflagged, while a higher threshold could trigger a warning.
- **Allowed values**: A check can require the species column to contain only the three expected values. This can catch inconsistent entries, including differences in capitalization, or serve as a final check after cleaning.
- **Ranges and missingness**: A between-check can require values in a column to fall between 30 and 60; Daniel thought the example included both endpoints and noted that non-inclusive bounds are also possible. Similar checks can flag implausible values, such as a measurement outside an expected range. Missingness checks can be handled separately, by column or by row.
- **Duplicate rows**: A check can test whether each row is distinct, which can help identify duplicate records such as repeated sensor readings or entries coded by multiple people.
- **Running checks**: The checks are defined first and run with `interrogate`. Point Blank then produces a table showing which checks passed or failed and displaying results using the specified thresholds. Daniel demonstrated that a check limited to two species values would flag other values in the dataset.
- **Separate passing and failing data**: Point Blank can produce separate data frames for rows that pass and fail. A downstream teammate can use the passing data while cleaning continues on the failures. Those data frames can also be saved as CSV files.
- **Where validation fits**: Checks can run after cleaning or immediately before modeling, and different parts of an analysis can validate data at different points. Daniel said the next week’s work would focus largely on data validation and breaking code into smaller pieces. [](plaud://source?type=summary&fileId=f_01a21440bf197f5894081dddd06aac5d&start_time=4848760&end_time=4859720&displayLabel=1&transcriptType=polish)
