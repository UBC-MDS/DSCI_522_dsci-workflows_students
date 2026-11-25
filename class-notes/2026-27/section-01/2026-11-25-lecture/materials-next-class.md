# Not reached in class: 2026-11-25 lecture, section 01 (next class)

Sections of this lecture's readings the class didn't reach, as published on 2026-11-25,
each heading linked to its published section. No script sends this file to a model: a
model given readings the class didn't reach can teach them as class content.

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

#### [29.1.3 Layer caching](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#layer-caching)

Docker saves each step’s result as a layer, and reuses a layer when nothing in its step, or in the steps above it, has changed. To see this, change only the message on the `CMD` line of the `Dockerfile`:

``` dockerfile
CMD ["Rscript", "-e", "cowsay::say('Moo! Only my message changed.')"]
```

Then build again:

*Terminal*

``` bash
docker build --tag hello-cowsay .
```

*Output*

``` out
[+] Building 0.2s (6/6) FINISHED                                               docker:desktop-linux
 => [internal] load build definition from Dockerfile                                           0.0s
 => => transferring dockerfile: 179B                                                           0.0s
 => [internal] load metadata for docker.io/rocker/r-ver:4.6.2                                  0.0s
 => [internal] load .dockerignore                                                              0.0s
 => => transferring context: 2B                                                                0.0s
 => [1/2] FROM docker.io/rocker/r-ver:4.6.2@sha256:8739c76d2d9316698a7145b032601f1e82249fdee3  0.0s
 => => resolve docker.io/rocker/r-ver:4.6.2@sha256:8739c76d2d9316698a7145b032601f1e82249fdee3  0.0s
 => CACHED [2/2] RUN Rscript -e "install.packages('cowsay')"                                   0.0s
 => exporting to image                                                                         0.1s
 => => exporting layers                                                                        0.0s
 => => exporting manifest sha256:f2d1c5ab15c8048a1863f62aa572f3bc2c971015fe8a2c04c5a4f1123137  0.0s
 => => exporting config sha256:0146dc6311dfcf1595b66373383e7f7bc1b4f0deae336219d9487b03da6d38  0.0s
 => => exporting attestation manifest sha256:bc8aca2ce37900fcdcd01fda5fed9286c997df019e23c971  0.0s
 => => exporting manifest list sha256:168f3c35f574628804baaf63e71be4164a7d1534ca35229a6827c7c  0.0s
 => => naming to docker.io/library/hello-cowsay:latest                                         0.0s
 => => unpacking to docker.io/library/hello-cowsay:latest                                      0.0s
```

The `RUN` step says `CACHED`. Docker reused the layer with cowsay installed and only changed the default command:

*Terminal*

``` bash
docker run --rm hello-cowsay
```

*Output*

``` out
 _______________________________ 
< Moo! Only my message changed. >
 ------------------------------- 
      \
       \

        ^__^ 
        (oo)\ ________ 
        (__)\         )\ /\ 
             ||------w|
             ||      ||
```

Installing one package took a few seconds, but installing many packages, or packages that R compiles from source, can take many minutes, and the cache skips all of it. This is why a `Dockerfile` puts the steps that change least often, such as installing software, near the top, and the steps that change most often near the bottom. A change to one step rebuilds that step and every step below it.

`docker image ls` lists the image, and `docker history` lists its layers, newest first (`head -5` keeps the first five lines):

*Terminal*

``` bash
docker image ls hello-cowsay
```

*Output*

``` out
IMAGE                 ID             DISK USAGE   CONTENT SIZE   EXTRA
hello-cowsay:latest   168f3c35f574       1.45GB          390MB        
```

*Terminal*

``` bash
docker history hello-cowsay | head -5
```

*Output*

``` out
IMAGE          CREATED          CREATED BY                                      SIZE      COMMENT
168f3c35f574   17 seconds ago   CMD ["Rscript" "-e" "cowsay::say('Moo! Only …   0B        buildkit.dockerfile.v0
<missing>      17 seconds ago   RUN /bin/sh -c Rscript -e "install.packages(…   4.17MB    buildkit.dockerfile.v0
<missing>      11 days ago      COPY scripts /rocker_scripts # buildkit         168kB     buildkit.dockerfile.v0
<missing>      11 days ago      CMD ["R"]                                       0B        buildkit.dockerfile.v0
```

The top two rows are the layers our `Dockerfile` added. The `RUN` layer holds the 4.17MB of R packages, and it shows that Docker ran the command with `/bin/sh -c`. The `CMD` layer adds no files, only the default command, so its size is 0B. The rows below come from `rocker/r-ver:4.6.2`, including its `CMD ["R"]`, which our `CMD` replaces.

**More information**

Docker runs `RUN` commands with the shell `/bin/sh`, not Bash, unless the `Dockerfile` picks another shell with the `SHELL` instruction (see Docker’s [`Dockerfile` reference](https://docs.docker.com/reference/dockerfile/)). For commands like these, the two shells behave the same.

#### [29.1.4 Guidelines for `RUN` commands](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#guidelines-for-run-commands)

Each `RUN` command creates a new layer in the Docker image. Each layer in a Docker image takes more disk space. As a consequence, we want to minimize the number of layers where reasonably possible. How can we do this?

Install everything that can be installed by a tool (e.g., `apt-get`, or `install.packages()` in R) at once (i.e., when installing 5 programs via `apt-get`, do not call `apt-get` five times; instead do: `apt-get install tool1 tool2 tool3 tool4 tool5`, and in R, `install.packages(c("pkg1", "pkg2"))`). However, doing this can lead to long lines. In response, we can break a single command across lines in the shell by using the `\` character. For example, to reduce the long line below, which uses `apt-get` to install the programs Git, Tiny Nano, Less, and wget:

*Terminal*

``` bash
apt-get install --yes git nano-tiny less wget
```

We can use `\` after each program to break the long command across lines and make the command more readable (especially if there were even more programs to install). Similarly, we indent the lines after `\` to increase readability:

*Terminal*

``` bash
apt-get install --yes \
    git \
    nano-tiny \
    less \
    wget
```

We can also group together related commands that depend upon each other. When doing this, we need to be careful, though, as sometimes we don’t want to run a command if the command that was run immediately before it failed. We can specify this in the shell using `&&`. For example, if we want to not run `apt-get` installation commands if `apt-get update` failed, we can write:

*Terminal*

``` bash
apt-get update && \
    apt-get install --yes git
```

#### [29.2.1 `CMD` or `ENTRYPOINT`?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#cmd-or-entrypoint)

Both set what a container runs when it starts. They differ in what `docker run` can replace. A command after the image name in `docker run` replaces `CMD`. For example, this runs `R --version` in the `hello-cowsay` image in place of its cowsay message (`head -1` keeps the first line):

*Terminal*

``` bash
docker run --rm hello-cowsay R --version | head -1
```

*Output*

``` out
R version 4.6.2 (2026-10-29) -- "Diversified Portfolio"
```

`ENTRYPOINT` is not replaced this way. Anything after the image name is passed to it as arguments, and replaces only `CMD`. With both, `ENTRYPOINT` holds the part that always runs, and `CMD` holds the default arguments. For example, this `Dockerfile`, in a folder of its own, always runs `Rscript -e`, with cowsay R code as the default:

``` dockerfile
FROM rocker/r-ver:4.6.2

RUN Rscript -e "install.packages('cowsay')"

ENTRYPOINT ["Rscript", "-e"]
CMD ["cowsay::say('Hello from my first image!')"]
```

*Terminal*

``` bash
docker build --tag cowsay-entrypoint .
docker run --rm cowsay-entrypoint
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

Passing different R code replaces the default, but still runs it with `Rscript -e`:

*Terminal*

``` bash
docker run --rm cowsay-entrypoint "cowsay::say('Only the R code changed.')"
```

*Output*

``` out
 __________________________ 
< Only the R code changed. >
 -------------------------- 
      \
       \

        ^__^ 
        (oo)\ ________ 
        (__)\         )\ /\ 
             ||------w|
             ||      ||
```

The images in this book, `rocker/r-ver` among them, set only `CMD`, so that a command such as `bash` after the image name replaces it, as in step 3 of the workflow.

### [41.5 Flagging every row](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/data-validation-python-pointblank.html#flagging-every-row)

`get_row_flags()` returns every row of the data, with a column for each step that is `True` where the row failed that step, the number of steps the row failed, and the fraction of steps it passed:

``` python
values.get_row_flags()  # every row, with the checks it failed
```

|  | species | island | bill_length_mm | bill_depth_mm | flipper_length_mm | body_mass_g | sex | year | pb_failed_1\_ | pb_failed_2\_ | pb_failed_3\_ | pb_failed_4\_ | pb_failed_5\_ | pb_n_failed\_ | pb_row_score\_ |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| 0 | Adelie | Torgersen | 39.1 | 18.7 | 181.0 | 3750.0 | male | 2007 | False | False | False | True | False | 1 | 0.8 |
| 1 | Adelie | Torgersen | 39.5 | 17.4 | 186.0 | 3800.0 | female | 2007 | False | False | False | False | False | 0 | 1.0 |
| 2 | Adelie | Torgersen | 40.3 | 18.0 | 195.0 | 3250.0 | female | 2007 | False | False | False | False | False | 0 | 1.0 |
| 3 | Adelie | Torgersen | NaN | NaN | NaN | NaN | NaN | 2007 | False | False | False | False | False | 0 | 1.0 |
| 4 | Adelie | Torgersen | 36.7 | 19.3 | 193.0 | 3450.0 | female | 2007 | False | False | False | False | False | 0 | 1.0 |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |
| 339 | Chinstrap | Dream | 55.8 | 19.8 | 207.0 | 4000.0 | male | 2009 | False | False | False | False | False | 0 | 1.0 |
| 340 | Chinstrap | Dream | 43.5 | 18.1 | 202.0 | 3400.0 | female | 2009 | False | False | False | False | False | 0 | 1.0 |
| 341 | Chinstrap | Dream | 49.6 | 18.2 | 193.0 | 3775.0 | male | 2009 | False | False | False | False | False | 0 | 1.0 |
| 342 | Chinstrap | Dream | 50.8 | 19.0 | 210.0 | 4100.0 | male | 2009 | False | False | False | False | False | 0 | 1.0 |
| 343 | Chinstrap | Dream | 50.2 | 18.7 | 198.0 | 3775.0 | female | 2009 | False | False | False | False | False | 0 | 1.0 |

344 rows × 15 columns
