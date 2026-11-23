# Docker Containers and Workflow Practices

Date Time: 2026-11-19

Instructor: Daniel Chen

## Summary

The session reviewed essential Git collaboration practices before introducing Docker containers as a solution to environment management and reproducibility. The instructor emphasized keeping project analyses simple and technically correct, focusing on the workflow rather than complex modeling. The lecture explained how containers isolate operating system user spaces to guarantee that code runs identically across different machines and operating systems. The instructor demonstrated pulling and running pre-built R and RStudio images, explaining key flags like `--rm` for cleanup and `-p` for port mapping. The class concluded by walking through the creation of a custom `Dockerfile` to build a persistent image with specific packages, covering the `FROM`, `RUN`, and `CMD` instructions and how Docker's layer caching speeds up repeated builds.

## Knowledge Points

### 1. Git Workflow and Project Management

- **GitHub Issues**: Used for tracking tasks, meeting notes, and ideas. Issues and pull requests share a single sequential numbering system. 
- **Auto-closing with Keywords**: Writing `fixes #N` or `closes #N` in a pull request description automatically closes the corresponding issue when the PR is merged into the target branch.
- **Branch Cleanup**: After merging a pull request, the branch should be deleted on GitHub. Locally, run `git fetch --prune` to remove stale remote-tracking references, then `git branch -d <branch>` to delete the local branch.
- **Keep Analysis Simple**: The course prioritizes reproducible workflows over complex statistical modeling. A technically correct, simple analysis is preferred over an over-engineered one that complicates the pipeline.

### 2. Containerization Fundamentals

- **What is a Container?**: A lightweight, isolated computing environment that virtualizes the operating system user space. Unlike virtual machines, containers share the host OS kernel, lack a graphical interface, and are significantly smaller and faster to start.
- **Solving "Works on My Machine"**: Containers guarantee that everyone uses the exact same versions of programming languages, packages, and system-level dependencies. This eliminates compatibility issues across different host operating systems (macOS, Windows, Linux) and architectures.
- **Ephemeral State**: By default, interactive containers discard all changes upon exit. To persist an environment or installed software, it must be baked into a new container image.

### 3. Running Containers with Docker

- **`docker run`**: Launches a container instance from an image. 
- **`--rm`**: Automatically removes the container instance when it stops, preventing stopped containers from piling up and consuming disk space.
- **`-it`**: Two combined flags. `-i` keeps standard input open (interactive), and `-t` allocates a pseudo-TTY terminal.
- **Port Mapping (`-p`)**: Routes network traffic from the host to the container. Format is `-p <host_port>:<container_port>`. Essential for running web-based IDEs like RStudio or Jupyter inside containers.
- **Environment Variables (`-e`)**: Pass configuration into the container at runtime using `-e KEY="VALUE"`. Commonly used to set passwords or toggle features.

### 4. Building Custom Images with Dockerfiles

- **`Dockerfile`**: A plain-text configuration file that instructs Docker on how to build a container image. It builds in layers, starting from a base image.
- **Key Instructions**:
  - `FROM`: Specifies the base image to build upon (e.g., `rocker/r-ver:4.6.2`).
  - `RUN`: Executes shell commands during the image build process (e.g., installing packages).
  - `CMD`: Sets the default command that runs when a container is launched from the new image.
- **Building and Caching**: Use `docker build --tag <name> .` to build an image from the `Dockerfile` in the current directory. Docker caches each layer; if a `RUN` command hasn't changed, Docker reuses the cached layer, making rebuilds extremely fast.

## Commands from class

### Git branch, PR, and cleanup workflow

```bash
git switch -c today                       # Create and switch to a new feature branch
git add README.md                         # Stage modified files
git commit -m "today we are talking about containers" # Commit changes
git push origin today                     # Push the branch to the remote repository
git switch main                           # Switch back to the main branch
git pull origin main                      # Pull latest changes to main
git fetch --prune                         # Delete local references to branches deleted on the remote
git branch -d today                       # Delete the local branch
```

### Pulling and running base R containers

```bash
docker pull rocker/r-ver:4.3.2            # Download a specific version of the base R image
docker run --rm -it rocker/r-ver:4.3.2    # Run interactively; --rm cleans up after exit
```

The container runs a fresh Linux environment with R 4.3.2 installed. Any R packages installed during this session are lost when you exit because the container instance is ephemeral.

### Running web apps (RStudio) with port mapping

```bash
docker run --rm -p 8787:8787 rocker/rstudio:4.4.2
docker run --rm -p 8787:8787 -e PASSWORD="apassword" rocker/rstudio:4.4.2
```

The `-p 8787:8787` flag maps port 8787 on your computer to port 8787 inside the container, allowing you to access the RStudio web interface via `http://localhost:8787`. The `-e` flag overrides the container's default randomly generated login password.

### Building a custom image

```bash
# Test the installation command inside an interactive bash shell
Rscript -e "install.packages('cowsay')"

# Build the image using the Dockerfile in the current directory
docker build --tag hello-cowsay .

# Run the custom image; it executes the CMD instruction automatically
docker run --rm -it hello-cowsay
```

The `Dockerfile` instructed Docker to `FROM rocker/r-ver:4.6.2`, `RUN` the installation command, and `CMD` to print a message using `cowsay`. The build output shows `CACHED [2/2] RUN ...`, demonstrating how Docker skips rebuilding layers that haven't changed.

## Questions

- **Q:** How can you run two containers simultaneously if they both try to use the same default port?
  **A:** Each container instance needs a unique port on the host machine to avoid conflicts. You can remap the local port using the `-p` flag (e.g., `-p 8788:8787`). This runs the container's service on port 8788 of your local machine while the container itself still listens on 8787 internally.

- **Q:** How do you prevent a container's installed packages from disappearing after you exit the session?
  **A:** Interactive containers are temporary. To persist changes, you must document your setup in a `Dockerfile` and build it into a new image using `docker build`. The new image permanently includes the installed software and will be available whenever you run that image.

## Assignments

- [ ] Milestone 2: Set up your Git repository, create three issues, create a pull request to merge a feature branch into main, and merge it. Due this week, 2026-11-19.
- [ ] Milestone 3: Containerize your project analysis using Docker and a `Dockerfile`. Due next week, 2026-11-26.

---

- prompt: prompt-notes-original.md @ 979670b
- prompt-hash: f78026c179ce
- model: qwen3.6-35b-a3b (requested: qwen3.6-35b-a3b)
- backend: local (llama-swap)
- inputs: transcript-plaud.md, history.txt, terminal.txt, materials.md
- generated: 2026-11-19
