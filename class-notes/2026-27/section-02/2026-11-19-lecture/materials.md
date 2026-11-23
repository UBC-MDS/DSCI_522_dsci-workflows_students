# Course materials: 2026-11-19 lecture

## Links

- Demo repository: <https://github.com/chendaniely/2026-11-19-docker>
  - [`Dockerfile`](https://github.com/chendaniely/2026-11-19-docker/blob/main/Dockerfile)
  - [Issue #1 what are we doing today?](https://github.com/chendaniely/2026-11-19-docker/issues/1)
  - [Issue #2 edit the readme with today's topic](https://github.com/chendaniely/2026-11-19-docker/issues/2)
  - [Pull request #3 today we are talking about containers](https://github.com/chendaniely/2026-11-19-docker/pull/3)
- Textbook, *Reproducible and Trustworthy Workflows for Data Science*:
  <https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/>
  - [27 Introduction to containerization](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html)
  - [28 Using and running containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html)
  - [29 Customizing and building containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html)
- Not reached in class (next class; their text is in `materials-next-class.md`):
  - [27.7 Image vs container?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#image-vs-container)
  - [27.8 What is a container registry?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#what-is-a-container-registry)
  - [28.1.2 Mounting volumes to containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#mounting-volumes-to-containers)
  - [28.1.5 Use a container to execute a script](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#use-a-container-to-execute-a-script)
  - [28.2 Docker command-line commands](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#docker-command-line-commands)
  - [29.1.3 Layer caching](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#layer-caching)
  - [29.1.4 Guidelines for `RUN` commands](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#guidelines-for-run-commands)
  - [29.2.1 `CMD` or `ENTRYPOINT`?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#cmd-or-entrypoint)
  - [29.3 Choosing a base image for your Dockerfile](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#choosing-a-base-image-for-your-dockerfile)
  - [33 Containers: Docker Compose](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-docker-compose.html)

## About these materials

What this lecture worked from: the class's demo repository, and textbook chapters from
*Reproducible and Trustworthy Workflows for Data Science*
(<https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/>),
as published on 2026-11-19. Each textbook heading links to its published section.

The syllabus lists chapters 27, 28 and 33 for this lecture. The class also built a first
image from a Dockerfile (chapter 29). It ran out of time before Docker Compose (chapter
33) and parts of chapters 27-29, which the instructor plans to cover next class. Those
sections are listed under "Not reached in class" above, as links only; their text is in
`materials-next-class.md`, which is not sent to the models.

## Demo repository

The repository the instructor cloned and worked in during class:
<https://github.com/chendaniely/2026-11-19-docker>. As GitHub lists them on 2026-11-19:

- Issue [#1 what are we doing today?](https://github.com/chendaniely/2026-11-19-docker/issues/1),
  which reads "what is today's topic?"; closed by #3.
- Issue [#2 edit the readme with today's topic](https://github.com/chendaniely/2026-11-19-docker/issues/2),
  assigned in its text to the instructor and pointing back to #1 ("meeting from #1"); closed by #3.
- Pull request [#3 today we are talking about containers](https://github.com/chendaniely/2026-11-19-docker/pull/3),
  from branch `today`, merged into `main`. It changes `README.md`, adding the line
  "today we will talk about containers". Its description:

  ```
  this is the fix for #2

  - [x] item 1
  - [ ] item 2

  closes #1 fixes #2
  ```

The `Dockerfile` the class wrote, committed to `main` at the end of class:

```dockerfile
FROM rocker/r-ver:4.6.2

RUN Rscript -e "install.packages('cowsay')"

CMD ["Rscript", "-e", "cowsay::say('Hello from my first image!')"]
```

## [27 Introduction to containerization](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html)

### [Learning Objectives](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#learning-objectives)

1.  Explain what containers are, and why they can be useful for reproducible data analyses
2.  Discuss the advantages and limitations of containerization (e.g., Docker) in the context of reproducible data analyses
3.  Compare and contrast the difference between running software/scripts in a virtual environment, a virtual machine, and a container
4.  Evaluate, choose, and justify an appropriate environment management solution based on the data analysis project’s complexity, expected usage, and longevity

### [Download the images before you start](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#download-the-images-before-you-start)

The exercises in this chapter run three container images, which together take about 13 GB of disk space (about 3 GB to download). Downloading them takes a while, so download (pull) them before you start. Start Docker first (on macOS and Windows, open Docker Desktop), then run:

*Terminal*

``` bash
docker pull rocker/r-ver:4.3.2
docker pull rocker/rstudio:4.4.2
docker pull quay.io/jupyter/datascience-notebook:2025-03-14
```

`docker pull` downloads an image from a container registry without running it. The Jupyter image is the largest of the three, at about 9 GB.

### [27.1 Documenting and loading dependencies](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#documenting-and-loading-dependencies)

You’ve made some beautiful data analysis pipeline/project using Make, R, and/or Python. It runs on your machine, but how easily can you, or someone else, get it working on theirs? The answer usually is, it depends…

What does it depend on?

1.  Do your `README` and your scripts make it blatantly obvious what programming languages and packages are needed to run your data analysis pipeline/project?

2.  Do you also document the version numbers of the programming languages and packages you used? This can have big consequences when it comes to reproducibility… (*e.g.*, the [change to how `sample()` draws random numbers](https://cran.r-project.org/doc/manuals/r-release/NEWS.3.html) in R 3.6.0, in 2019?)

3.  Did you document what other software (beyond the programming languages and packages used) and operating system dependencies are needed to run your data analysis pipeline/project?

*Virtual environments can be tremendously helpful with \#1 & \#2; however, they may or may not be helpful to manage \#3…* ***Enter containerization as a possible solution!***

### [27.2 What is a container?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#what-is-a-container)

Containers are another way to generate (and share!) isolated computational environments. They differ from virtual environments (which we discussed previously) in that they are even more isolated from the computer’s operating system, and they can be used to share many other types of software, applications, and operating system dependencies.

Before we can fully define containers, however, we need to define **virtualization**. Virtualization is a process that allows us to divide the elements of a single computer into several virtual elements. These elements can include computer hardware platforms, storage devices, computer network resources, and even operating system user spaces (e.g., graphical tools, utilities, and programming languages).

Containers virtualize operating system user spaces so that they can isolate the processes they contain, as well as control the processes’ access to computer resources (e.g., CPUs, memory, and disk space). What this means in practice is that an operating system user space can be carved up into multiple containers running the same or different processes in isolation. Below we show the schematic of a container whose virtual user space contains the:

- R programming language, the Bioconductor package manager, and two Bioconductor packages
- Galaxy workflow software and two toolboxes that can be used with it
- Python programming language, IPython interpreter, and Jupyter notebook package

![](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/img/13742_2016_article_135_f7.jpeg)

**Schematic of a container for genomics research.** Source: <https://doi.org/10.1186/s13742-016-0135-4>

**Exercise**

**Running a simple container**

To further illustrate what a container looks like, and feels like, we can use Docker (containerization software) to run one and explore. First we will run a Linux (Debian-flavored) container that has R installed. To run this, type:

*Terminal*

``` bash
docker run --rm -it rocker/r-ver:4.3.2
```

Here is what each part of the command does:

- `docker run` starts a new container from an image. If the image is not on your computer yet, Docker first downloads (pulls) it from a container registry.
- `--rm` deletes the container when it stops, so that stopped containers do not pile up on your computer.
- `-it` is two flags written together. `-i` (`--interactive`) keeps the container’s input open, so that what you type reaches R. `-t` (`--tty`) connects R to a terminal, so that R runs as an interactive session. Without `-t`, R stops with `Fatal error: you must specify '--save', '--no-save' or '--vanilla'`.
- `rocker/r-ver:4.3.2` is the image to run, `rocker/r-ver` from Docker Hub with the tag `4.3.2`, which picks R 4.3.2.

**More information**

R starts because the image’s [`Dockerfile`](https://github.com/rocker-org/rocker-versioned2/blob/R4.3.2/dockerfiles/r-ver_4.3.2.Dockerfile) sets `CMD ["R"]`, the command a container runs when it starts. [Building images](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html) explains `CMD`.

[Running containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html) covers these flags in more detail, and Docker’s [`docker run` reference](https://docs.docker.com/reference/cli/docker/container/run/) lists them all.

When you successfully launch the container, R should have started. Check the version of R - is it the same as your computer’s version of R? Use `getwd()` and `list.files()` to explore the container’s filesystem from R. Does this look like your computer’s filesystem or something else?

Type `q()` to quit R and exit the container.

Compare this version of R that is running in the container to the version of R you have on your computer.

**Exercise**

**Running a container with RStudio as a web app**

Next, try to use Docker to run a container that has the RStudio Server web application installed:

*Terminal*

``` bash
docker run --rm -p 8787:8787 -e PASSWORD="apassword" rocker/rstudio:4.4.2
```

Then open a web browser on your computer and type: <http://localhost:8787>

If it worked, then you should be at an RStudio Sign In page. To sign in, use the following credentials:

- **username:** rstudio
- **password:** apassword

The RStudio Server web app being run by the container should look something like this:

![](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/img/rstudio-container-web-app.png)

Type `Ctrl` + `C` in the terminal where you launched the container to quit R and RStudio and exit the container.

We can pass in multiple environment variables by using multiple `-e` flags. For example, we can set the password for the rstudio user with the `PASSWORD` environment variable, but we can also disable the login screen with the `DISABLE_AUTH=true` variable.

*Terminal*

``` bash
docker run --rm -p 8787:8787 -e PASSWORD="apassword" -e DISABLE_AUTH=true rocker/rstudio:4.4.2
```

Each container will have its own set of environment variables to control its behavior. For the `rocker/rstudio` project, you can find the environment variable documentation here: <https://rocker-project.org/images/versioned/rstudio.html#environment-variables>.

**Exercise**

**Running a container with Jupyter as a web app**

Next, try to use Docker to run a container that has the Jupyter web application installed:

*Terminal*

``` bash
docker run --rm -p 8888:8888 quay.io/jupyter/datascience-notebook:2025-03-14
```

In the terminal, look for a URL that starts with `http://127.0.0.1:8888/lab?token=` (for an example, see the highlighted text in the terminal below). Copy and paste that URL into your browser.

**Important**

Do not forget to copy the `token=` portion of the URL. If you only go to `localhost:8888` or `http://127.0.0.1:8888`, it will ask you for the password/token.

![](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/img/jupyter-container-web-app-launch-url.png)

The Jupyter web application being run by the container should look something like this:

![](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/img/jupyter-container-web-app.png)

Type Ctrl + c in the terminal where you launched the container to quit Jupyter and exit the container.

### [27.3 Contrasting containers with virtual machines](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#contrasting-containers-with-virtual-machines)

Virtual machines are another technology that can be used to generate (and share) isolated computational environments. Virtual machines emulate the functionality of an entire computer on another physical computer. With virtual machines, the virtualization occurs at the layer of software that sits between the computer’s hardware and the operating system(s). This software is called a hypervisor. For example, on a Mac laptop, you could install a program called [Oracle VirtualBox](https://www.virtualbox.org/) to run a virtual machine whose operating system was Windows 8.1, as the screenshot below shows:

![](https://www.virtualbox.org/raw-attachment/wiki/Screenshots/Windows_8.1_on_OSX.png)

**A screenshot of a macOS computer running a Windows virtual machine.** Source: <https://www.virtualbox.org/wiki/Screenshots>

Below, we share an illustration that compares where virtualization happens in containers compared to virtual machines. This difference leads to containers being more lightweight and portable compared to virtual machines, and also less isolated.

![](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/img/container_v_vm.png)

*Source: <https://www.docker.com/resources/what-container>*

**Key take-home:** Containerization software shares the host’s operating system, whereas virtual machines have a completely separate, additional operating system. This can make containers lighter (smaller in terms of size) and more resource- and time-efficient than using a virtual machine.

### [27.4 Contrasting common computational environment virtualization strategies](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#contrasting-common-computational-environment-virtualization-strategies)

| Feature | Virtual environment | Container | Virtual machine |
|----|----|----|----|
| Virtualization level | Application | Operating system user-space | Hardware |
| Isolation | Programming languages, packages | Programming languages, packages, **other software, operating system dependencies, filesystems, networks** | Programming languages, packages, other software, operating system dependencies, filesystems, networks, **operating systems** |
| Size | Extremely lightweight | Lightweight | Heavyweight |

### [27.5 Virtualization strategy advantages and disadvantages for reproducibility](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#virtualization-strategy-advantages-and-disadvantages-for-reproducibility)

Let’s collaboratively generate a list of advantages and disadvantages of each virtualization strategy in the context of reproducibility:

#### [27.5.1 Virtual environment](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#virtual-environment)

A virtual environment, such as a uv or renv project, isolates the packages for one programming language.

##### [Advantages](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#advantages)

- Extremely small size
- Porous (less isolated) - makes it easy to pair the virtualized computational environment with files on your computer
- Specify these with a single text file

##### [Disadvantages](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#disadvantages)

- Not always possible to capture and share operating system dependencies, and other software your analysis depends upon
- Computational environment is not fully isolated, and so missed dependencies can go unnoticed

#### [27.5.2 Containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#containers)

A container isolates an operating system user space, with its programming languages, packages and other software.

##### [Advantages](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#advantages-1)

- Somewhat lightweight in size (manageable for easy sharing - there are tools and software to facilitate this)
- Possible to capture and share operating system dependencies, and other software your analysis depends upon
- Computational environment is fully isolated, and errors will occur if dependencies are missing
- Specify these with a single text file
- Can share volumes and ports (advantage compared to virtual machines)

##### [Disadvantages](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#disadvantages-1)

- Possible security issues - running software on your computer that you may allow to be less isolated (i.e., mount volumes, expose ports)
- Takes some effort to share volumes and ports (disadvantage compared to virtual environments)

#### [27.5.3 Virtual machine](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#virtual-machine)

A virtual machine isolates a whole computer, including its operating system.

##### [Advantages](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#advantages-2)

- High security, because these are much more isolated (filesystem, ports, etc.)
- Can share an entirely different operating system (might not be so useful in the context of reproducibility however…)

##### [Disadvantages](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#disadvantages-2)

- Very big in size, which can make it prohibitive to share them
- Takes great effort to share volumes and ports - which makes it hard to give access to data on your computer

### [27.6 Container usage workflow](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html#container-usage-workflow)

Below is a schematic of a typical container usage workflow from a [blog post](https://blog.octo.com/en/docker-registry-first-steps/) by Arnaud Mazin. The source code for container images is stored in a file called a `Dockerfile`. Like a `pyproject.toml` or an `renv.lock` file, you would typically version control this with Git and store this in your GitHub repository with your analysis code. From the source `Dockerfile` we can build a Docker container image. This image is a binary file, from which we can run one, or more, container instances. Container instances are the computational environment in which you would run your analysis. Containers are usually ephemeral - we create them from the image when we want to run the analysis and then stop and remove/delete them after it has run. Docker images can (and should) be versioned and shared via container registries (which are akin to remote code repositories).

![](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/img/docker-stages.png)

*Source: [OctoTalks](https://blog.octo.com/en/docker-registry-first-steps/)*

## [28 Using and running containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html)

### [Learning Objectives](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#learning-objectives)

1.  Use the containerization software (e.g., Docker command line and Docker Compose) to run the software needed for your analysis
2.  Use port mapping with the containerization software to run web apps to access IDEs (e.g., Jupyter, RStudio, VS Code)
3.  Use volume mounting with the containerization software to allow the container access to local host files (e.g., analysis code and data files)

### [Download the images before you start](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#download-the-images-before-you-start)

The examples in this chapter use three images. You pulled the two `rocker` images in [Introduction to containerization](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html). Start Docker first (on macOS and Windows, open Docker Desktop), then download (pull) any you do not have yet:

*Terminal*

``` bash
docker pull ubuntu:24.04
docker pull rocker/r-ver:4.3.2
docker pull rocker/rstudio:4.4.2
```

### [28.1 Launching containers using Docker at the command line](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#launching-containers-using-docker-at-the-command-line)

Docker has many ways we can run containers (GUI, command line, Docker Compose configuration files). Here we will learn how to use the command-line interface for running container instances from container images. We will then build on this knowledge to move to using Docker Compose configuration files for increased efficiency. We are opting to use command-line and configuration file tools so that we can automate and scale the running of containers. It is also more reproducible.

#### [28.1.1 Launch and run containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#launch-and-run-containers)

Below we demonstrate how to launch and run containers using the [`ubuntu` image](https://hub.docker.com/_/ubuntu) as an example, which is Ubuntu Linux with almost nothing else installed. We will slowly walk through the 4 basic steps needed to run a container:

##### [Step 1 - launch the Docker app (for OSX & Windows only)](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#step-1---launch-the-docker-app-for-osx-windows-only)

On Mac and Windows, Docker runs in a virtual machine managed by the Docker Desktop app. To run a Docker container, you must have this running. To do this, use Launchpad/Finder/Start menu/etc. to find and launch Docker Desktop.

> Note: Docker might already be running. If so, great, but if it’s not, the commands below will not work. So it is always good to check!

##### [Step 2 - get container image from Docker Hub](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#step-2---get-container-image-from-docker-hub)

To run a container instance, you need to have a container image locally. One way to get a container image locally is to pull (i.e., download) one from a container registry like Docker Hub. To do this we use the `docker pull <CONTAINER>` command. You will commonly see the container to pull written as: `container_registry/container_user/container_image:container_image_version_tag`.

If you only see `container_user/container_image:container_image_version_tag`, Docker will assume you are using Docker Hub as the container registry (this is the default). In the previous chapter, we ran the `quay.io/jupyter/datascience-notebook:2025-03-14` container from the `quay.io` registry, and `rocker/rstudio:4.4.2` from Docker Hub.

Sometimes the `container_image_version_tag` is omitted. When this happens, the most recent container is pulled, and it has the version tag `latest`. In data analysis projects, we try to avoid using this strategy because Docker is lazy, and if you already have a `latest` image on your local host machine, `docker run container_user/container_image` will use it without checking whether there is a newer version of the container image on the remote container registry. Only `docker pull` checks the registry for a newer `latest`.

We will now pull the `ubuntu` Docker image, container image version `24.04`, which is hosted on Docker Hub, by running the following in the terminal:

*Terminal*

``` bash
docker pull ubuntu:24.04
```

We can verify that it successfully pulled by typing `docker images ubuntu:24.04`, or `docker images` to list all of your images. When you do that, you should see something like:

*Terminal*

``` bash
docker images ubuntu:24.04
```

*Output*

``` out
IMAGE          ID             DISK USAGE   CONTENT SIZE   EXTRA
ubuntu:24.04   008173c23f95        141MB         30.9MB        
```

**Note**

- You can skip this step and just go on to `docker run ...` as that command will pull the image if you do not have it locally.

- If you ever need to delete a container image from your computer, you can run `docker rmi <IMAGE_ID>` to do so.

##### [Step 3 - launch a container from the image and poke around!](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#step-3---launch-a-container-from-the-image-and-poke-around)

We use `docker run` to launch a container instance from a container image. By default, the container instance will execute its programmed launch behavior and immediately stop. Thus, if we want to use the container in a more interactive way, we need to tell Docker that by adding the `-it` flag to our `docker run` command.

*Terminal*

``` bash
docker run -it ubuntu:24.04
```

If it worked, then your command line prompt should now look something like this, which says that you are the user `root` in the container whose ID starts with `8f04536bf43d`, in its folder `/`:

*Output*

``` out
root@8f04536bf43d:/#
```

You can use standard Bash shell commands like `ls`, `cd`, and `pwd` to explore the container:

*Terminal*

``` bash
pwd
ls
```

*Output*

``` out
/
bin  boot  dev  etc  home  lib  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
```

You can type `exit` to leave when you are done (your prompt will look normal again)!

##### [Step 4 - clean up your container!](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#step-4---clean-up-your-container)

After you close a container, it still “hangs” around… It has stopped running, but the container instance still exists on your computer. You can view the containers on your computer, including the stopped ones, using `docker ps -a`. It may list other containers too:

*Terminal*

``` bash
docker ps -a
```

*Output*

``` out
CONTAINER ID   IMAGE          COMMAND       CREATED          STATUS                     PORTS     NAMES
8f04536bf43d   ubuntu:24.04   "/bin/bash"   15 seconds ago   Exited (0) 3 seconds ago             ecstatic_hoover
```

You can remove the container by typing `docker rm <container_id>`:

*Terminal*

``` bash
docker rm 8f04536bf43d
```

*Output*

``` out
8f04536bf43d
```

After you remove the container, you can prove to yourself that the container is no longer “hanging around” via `docker ps -a`, but that you still have the image installed (which you can see via `docker images`).

> Note: to remove running containers, you will need to first stop them via `docker stop <container_id>`.

##### [That’s a lot of work…](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#thats-a-lot-of-work)

We walked through those steps slowly so that you understand how everything is working. However, it is not the most efficient way to work with Docker container instances when using `docker run`. What we typically do is tell Docker to delete the container upon exit using the `--rm` flag in the run command.

The command below runs a new container instance from the same image. This one command is equivalent to steps 2–4 above!

*Terminal*

``` bash
docker run \
    --rm \
    -it \
    ubuntu:24.04
```

**Note**

We are using `\` above to split a Bash command across lines to make it more readable. You will see that throughout this chapter.

#### [28.1.3 Mapping ports to containers with web apps](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#mapping-ports-to-containers-with-web-apps)

[Docker documentation on Container networking](https://docs.docker.com/config/containers/container-networking/)

If we want to use a graphical user interface (GUI) with our containers, for example to be able to use the computational environment in the container in an integrated development environment (IDE) such as RStudio or JupyterLab, then we need to map the correct port from the container to a port on our computer.

**Note**

In computer science, ports are points where network connections start and end. They can be physical (e.g., USB ports, Ethernet ports) or virtual. In the case of virtual ports, they are really a software-based addressing mechanism that identifies points to connect specific processes or types of network services. When we are discussing ports in the context of containerization, we are referring to virtual ports.

To do this, we use the `-p` flag with `docker run`, specifying the port in the host (your computer) on the left-hand side, and the port in the container on the right-hand side of `:`. For example, to run the `rocker/rstudio` container image we would type `-p 8787:8787` to map the ports as shown in the `docker run` command below:

*Terminal*

``` bash
docker run \
    --rm \
    -p 8787:8787 \
    -e PASSWORD="apassword" \
    rocker/rstudio:4.4.2
```

Then to access the web app, we need to navigate a browser URL to `http://localhost:<HOST_PORT>`. In this case, we would navigate to <http://localhost:8787> to use the RStudio Server web app from the container.

Note that we can only map one port on our computer (the container/Docker host) to a container at any given time. However, our computer (the container/Docker host) has many ports we can choose from to map. So if we wanted to run a second `rocker/rstudio` container, then we could map it to a different port as shown below:

*Terminal*

``` bash
docker run \
    --rm \
    -p 8788:8787 \
    -e PASSWORD="apassword" \
    rocker/rstudio:4.4.2
```

When we do this, to run the app in a browser on our computer, we need to go to <http://localhost:8788> (instead of <http://localhost:8787>) to access this container as we mapped it to the `8788` port on our computer (and not `8787`).

Another important note is that the container port is specific to the container, and the web app installed therein. So we cannot change that without changing the container image and/or the application installed therein. Where do you learn what port is exposed in a container image? The image documentation should specify this. For example, in the [`rocker/rstudio` container image documentation](https://hub.docker.com/r/rocker/rstudio) it states:

![](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/img/rocker-rstudio-port-docs.png)

*Source: <https://hub.docker.com/r/rocker/rstudio>*

#### [28.1.4 Changing the containers default command](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-running.html#changing-the-containers-default-command)

When we launch containers, they execute the command at runtime that was specified in their `Dockerfile`. For example, in the case of the Rocker and Jupyter images, this default behavior is to run a web app. Sometimes the default container behavior is not what we want to do. Instead, we want to do something different, like run the container as a Bash shell to test out some installation commands (common when we are building and customizing our own containers) or use the container to run a script non-interactively (like executing a data analysis pipeline from beginning to end).

To do this, we can append a new command to the end of our `docker run` commands. For example, to open the `rocker/rstudio:4.4.2` image in an interactive Bash shell, we would run:

*Terminal*

``` bash
docker run \
    --rm \
    -it \
    rocker/rstudio:4.4.2 \
    bash
```

Notice the command above does not specify the ports, nor does it set the password. This is because, in this instance, we are not using this container to run it as a web app; we are just running it as a Bash shell (which needs no ports or authentication).

The general form for running things non-interactively is this:

*Terminal*

``` bash
docker run \
    --rm \
    -v PATH_ON_YOUR_COMPUTER:VOLUME_ON_CONTAINER DOCKER_IMAGE PROGRAM_TO_RUN \
    PROGRAM_ARGUMENTS
```

## [29 Customizing and building containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html)

### [Learning Objectives](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#learning-objectives)

1.  Write a container file (e.g., Dockerfile) that can be used to reproducibly build a container image that would contain the needed software and environment dependencies of your data science project
2.  Use manual and automated tools (e.g., Docker, GitHub Actions) to build and share container images
3.  List good container base images for data science projects

### [Download the images before you start](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#download-the-images-before-you-start)

The examples in this chapter build on `rocker/r-ver:4.6.2`, which takes more than a gigabyte of disk space. Start Docker first (on macOS and Windows, open Docker Desktop), then download (pull) it before you start:

*Terminal*

``` bash
docker pull rocker/r-ver:4.6.2
```

### [29.1 Building container images from `Dockerfile`’s](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#building-container-images-from-dockerfiles)

- A `Dockerfile` is a plain-text file that contains commands primarily about what software to install in the Docker image. This is the more trusted and transparent way to build Docker images.

- Once we have created a `Dockerfile`, we can build it into a Docker image.

- Docker images are built in layers, and as such, `Dockerfile`s always start by specifying a base Docker image that the new image is to be built on top of.

- Docker containers are all Linux containers and thus use Linux commands to install software. However, there are different flavors of Linux (e.g., Ubuntu, Debian, CentOS, Red Hat), and thus you need to use the right Linux install commands to match your flavor of container. For this course, we will focus on Ubuntu- or Debian-based images (and that means if we need to install software outside of R and Python packages, we will use `apt-get` as our installation program). However, most of what we’ll be doing for installation is R, Python, and their packages. For those, an image uses the same tools as your laptop, uv for Python and renv for R, which the next chapters put into an image.

**`apt` or `apt-get`?**

Ubuntu has two commands for its package manager. `apt` is designed for people typing at a terminal, and its behavior may change between versions. `apt-get` is the older command, which keeps working the same way, so Ubuntu’s [`apt` manual page](https://manpages.ubuntu.com/manpages/noble/man8/apt.8.html) recommends `apt-get` for scripts. The `RUN` lines in a `Dockerfile` are a script, so this book uses `apt-get` in them. `apt` even prints a warning when a script runs it:

*Output*

``` out
WARNING: apt does not have a stable CLI interface. Use with caution in scripts.
```

At a container’s prompt either command works, but using `apt-get` there too means you can copy the command that worked straight into the `Dockerfile`.

#### [29.1.1 Workflow for building a Dockerfile](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#workflow-for-building-a-dockerfile)

It can take a LOOOOOOOONNNG time to troubleshoot the building of Docker images. Thus, to speed things up and be more efficient, we suggest the workflow below:

1.  Choose a base image to build off (from <https://hub.docker.com/>).

2.  Create a `Dockerfile` named `Dockerfile` and save it in an appropriate project repository. Open that file and type `FROM <BASE_IMAGE>` on the first line. Add any files that need to be accessed at build time via the `COPY` command.

3.  In a terminal, type `docker run --rm -it <BASE_IMAGE> bash` and interactively try the install commands you think will work. Edit and try again until the install command works. The `bash` at the end starts a Bash shell in place of the image’s default command.

4.  Write working install commands in the `Dockerfile`, preceding them with `RUN`, and save the `Dockerfile`.

5.  After adding every 2–3 commands to your `Dockerfile`, try building the Docker image via `docker build --tag <TEMP_IMAGE_NAME> <PATH_TO_DOCKERFILE_DIRECTORY>`.

6.  Once the entire `Dockerfile` works from beginning to end on your laptop, then you can finally move to building remotely (e.g., creating a trusted build on GitHub Actions).

#### [29.1.2 Build your first image](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#build-your-first-image)

Let’s follow the workflow to build a small image with R and the R package [cowsay](https://cran.r-project.org/package=cowsay), which draws an animal saying whatever you give it.

For step 1, the base image is `rocker/r-ver:4.6.2`, Ubuntu Linux with R 4.6.2 installed. For step 2, make a folder for the project and move into it:

*Terminal*

``` bash
mkdir hello-cowsay
cd hello-cowsay
```

In a text editor, create a file in that folder named `Dockerfile`, with no file extension, that has one line:

``` dockerfile
FROM rocker/r-ver:4.6.2
```

For step 3, start a container from the base image with a Bash shell:

*Terminal*

``` bash
docker run --rm -it rocker/r-ver:4.6.2 bash
```

Inside R, you would install the package with `install.packages("cowsay")`. At the container’s Bash prompt, `Rscript -e` runs a line of R code instead, which is the form a `RUN` line needs:

*Terminal*

``` bash
Rscript -e "install.packages('cowsay')"
```

*Output*

``` out
Installing package into ‘/usr/local/lib/R/site-library’
(as ‘lib’ is unspecified)
also installing the dependencies ‘crayon’, ‘rlang’

trying URL 'https://p3m.dev/cran/__linux__/resolute/latest/src/contrib/crayon_1.5.3.tar.gz'
trying URL 'https://p3m.dev/cran/__linux__/resolute/latest/src/contrib/rlang_1.3.0.tar.gz'
trying URL 'https://p3m.dev/cran/__linux__/resolute/latest/src/contrib/cowsay_1.2.2.tar.gz'
* installing *binary* package ‘crayon’ ...
* package ‘crayon’ successfully unpacked and SHA256 sums checked
* DONE (crayon)
* installing *binary* package ‘rlang’ ...
* package ‘rlang’ successfully unpacked and SHA256 sums checked
* DONE (rlang)
* installing *binary* package ‘cowsay’ ...
* package ‘cowsay’ successfully unpacked and SHA256 sums checked
* DONE (cowsay)

The downloaded source packages are in
    ‘/tmp/RtmpAypckK/downloaded_packages’
```

Then try it:

*Terminal*

``` bash
Rscript -e "cowsay::say('Hello')"
```

*Output*

``` out
 _______ 
< Hello >
 ------- 
      \
       \

        ^__^ 
        (oo)\ ________ 
        (__)\         )\ /\ 
             ||------w|
             ||      ||
```

Type `exit` to leave the container.

For step 4, write the commands that worked into the `Dockerfile`:

``` dockerfile
FROM rocker/r-ver:4.6.2

RUN Rscript -e "install.packages('cowsay')"

CMD ["Rscript", "-e", "cowsay::say('Hello from my first image!')"]
```

`RUN` runs the install while the image is built. It is the same command you typed at the container’s Bash prompt, which is one reason this book works at the command line (see [Introduction to the Bash Shell](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/bash-shell.html)). `CMD` sets the command a container from this image runs when it starts. It replaces the base image’s own `CMD ["R"]` (see [Introduction to containerization](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers.html)), so a container runs our line of R code instead of starting R.

**A misspelled package does not stop the build**

`install.packages()` only warns when it cannot find a package, and `Rscript` still finishes with exit status `0`, which tells the shell that the command worked. `echo $?` prints the exit status of the last command:

*Terminal*

``` bash
Rscript -e "install.packages('cowsya')"
echo $?
```

*Output*

``` out
Installing package into ‘/usr/local/lib/R/site-library’
(as ‘lib’ is unspecified)
Warning message:
package ‘cowsya’ is not available for this version of R

A version of this package for your version of R might be available elsewhere,
see the ideas at
https://cran.r-project.org/doc/manuals/r-patched/R-admin.html#Installing-packages 
0
```

So a `RUN` line with a misspelled package builds without an error, into an image without the package. Adding `library()` after the install makes R stop with an error, which stops the build at that step:

*Terminal*

``` bash
Rscript -e "install.packages('cowsya'); library(cowsya)"
echo $?
```

*Output*

``` out
Installing package into ‘/usr/local/lib/R/site-library’
(as ‘lib’ is unspecified)
Warning message:
package ‘cowsya’ is not available for this version of R

A version of this package for your version of R might be available elsewhere,
see the ideas at
https://cran.r-project.org/doc/manuals/r-patched/R-admin.html#Installing-packages 
Error in library(cowsya) : there is no package called ‘cowsya’
Execution halted
1
```

For step 5, build the image from the folder that has the `Dockerfile`:

*Terminal*

``` bash
docker build --tag hello-cowsay .
```

- `--tag hello-cowsay` names the image. You can add a version after a colon, such as `hello-cowsay:0.1`; without one, Docker uses the tag `latest`.
- `.` is the build context, the folder Docker reads the `Dockerfile` and any copied files from, here the current folder.

*Output*

``` out
[+] Building 4.0s (6/6) FINISHED                                               docker:desktop-linux
 => [internal] load build definition from Dockerfile                                           0.0s
 => => transferring dockerfile: 176B                                                           0.0s
 => [internal] load metadata for docker.io/rocker/r-ver:4.6.2                                  0.0s
 => [internal] load .dockerignore                                                              0.0s
 => => transferring context: 2B                                                                0.0s
 => CACHED [1/2] FROM docker.io/rocker/r-ver:4.6.2@sha256:8739c76d2d9316698a7145b032601f1e822  0.0s
 => => resolve docker.io/rocker/r-ver:4.6.2@sha256:8739c76d2d9316698a7145b032601f1e82249fdee3  0.0s
 => [2/2] RUN Rscript -e "install.packages('cowsay')"                                          3.6s
 => exporting to image                                                                         0.2s
 => => exporting layers                                                                        0.1s
 => => exporting manifest sha256:3194becb32301ec3fcd846472866f8501aa5035f582f5149e2714b6d4903  0.0s
 => => exporting config sha256:c6f87af4eb6e98b553b3ee935b571ec906888a174f9322e359e9b96e2b15c1  0.0s
 => => exporting attestation manifest sha256:8b4f5f3c8233fa3a54471ca2fe6f7471a873845c8477c3c6  0.0s
 => => exporting manifest list sha256:9f2606d682dc224d8df0cdb02909dabdbfd7e4218aa98cd8cace121  0.0s
 => => naming to docker.io/library/hello-cowsay:latest                                         0.0s
 => => unpacking to docker.io/library/hello-cowsay:latest                                      0.1s
```

Each `[1/2]` and `[2/2]` is a step of the `Dockerfile`. If you have not pulled `rocker/r-ver:4.6.2` before, the `FROM` step downloads it first.

Run a container from the new image. It needs no `-it`, because our R code prints its message and exits:

*Terminal*

``` bash
docker run --rm hello-cowsay
```

*Output*

``` out
 ____________________________ 
< Hello from my first image! >
 ---------------------------- 
      \
       \

        ^__^ 
        (oo)\ ________ 
        (__)\         )\ /\ 
             ||------w|
             ||      ||
```

### [29.2 `Dockerfile` command summary](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#dockerfile-command-summary)

The most common `Dockerfile` commands I use:

| Command | Description |
|----|----|
| FROM | States which base image the new Docker image should be built on top of |
| RUN | Specifies that a command should be run in a shell |
| ENV | Sets environment variables |
| EXPOSE | Specifies the port the container should listen to at runtime |
| COPY or ADD | Adds files (or URLs in the case of ADD) to a container’s filesystem |
| CMD | Sets the default command a container runs when it starts; a command after the image name in `docker run` replaces it |
| ENTRYPOINT | Sets a command that always runs when a container starts; anything after the image name in `docker run` is passed to it as arguments |
| WORKDIR | Sets the working directory for any `RUN`, `CMD`, `ENTRYPOINT`, COPY and ADD instructions that follow it in the `Dockerfile` |

And more here in the [Dockerfile reference](https://docs.docker.com/reference/dockerfile/).

### [29.4 Dockerfile FAQ](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#dockerfile-faq)

These questions come up when you start writing your own `Dockerfile`.

#### [29.4.1 1. Where does the `Dockerfile` live?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#where-does-the-dockerfile-live)

The `Dockerfile` should live in the root directory of your project.

#### [29.4.2 2. How do I make an image from a `Dockerfile`?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#how-do-i-make-an-image-from-a-dockerfile)

There are 2 ways to do this! I use the first when developing my `Dockerfile` (to test quickly that it works), and then the second when I want a build that others can check, made from the `Dockerfile` in the repository.

1.  Build a Docker image locally on your laptop

2.  Build a Docker image on GitHub Actions (see [Building images for several platforms](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-platforms.html))

#### [29.4.3 3. How do I build an image locally on my laptop?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#how-do-i-build-an-image-locally-on-my-laptop)

From the directory that contains your `Dockerfile` (usually your project root):

*Terminal*

``` bash
docker build --tag IMAGE_NAME:VERSION .
```

**Note**

`--tag` lets you name and version the Docker image. You can call this anything you want. The version number/name comes after the colon.

After I build, I then try to `docker run ...` to test the image locally. If I don’t like it, or it doesn’t work, I delete the image with `docker rmi {IMAGE_NAME}`, edit my Dockerfile, and try to build and run it again.
