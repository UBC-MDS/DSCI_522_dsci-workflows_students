# DSCI 522: Data Science Workflows

## Introduction
Data-rich projects can quickly grow out-of-hand and become irreproducible in the absence of deliberate effort at organization, tool choice, and process. This course will teach basic principles of sound data scientific workflows and will develop skills implementing them in appropriate state-of-the-art systems and languages (e.g., Python and R).

## DSCI 522 Slack channel
https://ubc-mds.slack.com/messages/522_dsci-workflows/details/

## Learning Outcomes

By the end of the course, students are expected to be able to:

1. Analyze data interactively using read-eval-print-loop (REPL) processes; write scripts for non-interactive use; use tools and work styles to create fluidity between these two modes (e.g., RStudio IDE, iPython).
2. Perform dynamic reporting functions such as integrating narrative, code, data, numerical results, and visual results;  create reproducible reports and workflows (e.g., R Markdown, Project Jupyter).
3. Manage projects by designing workflows for self-documentation, reproducibility, and collaboration; organize files with appropriate naming conventions; manage paths and dependencies.
4. Use version control software (e.g., Git) including distributed version control and remote servers (e.g., GitHub).
5. Automate data science workflows (using e.g., Make).

## Schedule

| Lecture|      Date| Day |  Topic  | Reading(s) |
|--------|----------|-----|---------|------------|
|   1   | 2016-09-27 | Tue | Project and file management 101 + Version control via RStudio | <ul><li>[Good Enough Practices in Scientific Computing](https://swcarpentry.github.io/good-enough-practices-in-scientific-computing/)</li><li>[R workspace and working directory](http://stat545.com/block002_hello-r-workspace-wd-project.html#workspace-and-working-directory)</li><li>[RStudio Projects](http://stat545.com/block002_hello-r-workspace-wd-project.html#rstudio-projects)</li><li>[Happy Git with R Chapters 13, 16-18](http://happygitwithr.com/)</li></ul> | projects](http://stat545.com/block002_hello-r-workspace-wd-project.html#workspace-and-working-directory)
| 2     | 2016-09-29 | Thu | Scaling up: read-eval-print-loop (REPL) processes versus non-interactive scripts | <ul><li>[Command line arguments in R (the basics)](https://www.vscentrum.be/cluster-doc/software/r-cla-in-scripts)</li><li>[Software Carpentry lesson: Command line arguments with R](http://swcarpentry.github.io/r-novice-inflammation/05-cmdline/)</li><li>[Command line arguments with Python](https://docs.python.org/3.5/howto/argparse.html)</li></ul> |
|   3   | 2016-10-04  | Tue | Scaling up cont'd: Create reproducible reports and workflows in R | <ul><li>[Intro to R Markdown](https://rstudio-pubs-static.s3.amazonaws.com/105639_5c0a8f83c268447d8e9ea334e37e3ce1.html#rmarkdown-time)<li>[R Markdown Cheatsheet](https://www.rstudio.com/wp-content/uploads/2015/02/rmarkdown-cheatsheet.pdf)</li><li>[knitr::spin](http://deanattali.com/2015/03/24/knitrs-best-hidden-gem-spin/)</li><li>[ezknitr](https://github.com/ropenscilabs/ezknitr/blob/master/README.md)<li>[Use other languages in knitr](http://yihui.name/knitr/demo/engines/)</li></ul> |
| 4     | 2016-10-06 | Thu | Scaling up cont'd: Create reproducible reports and workflows in Python | <ul><li>[jupyter nbconvert](http://nbconvert.readthedocs.io/en/latest/usage.html)<li>[Pweave example gallery](http://mpastell.com/pweave/examples/)</li></ul> |
|   5   | 2016-10-11 | Tue | Automated workflows; introduction to build/automation tool (Guest lecture: Shaun Jackman) <ul><li> [Slides](http://sjackman.ca/makefile-slides/)</li><li>[Makefile example](http://sjackman.ca/makefile-example/)</li></ul> | <ul><li>[Software Carpentry Make lesson](http://swcarpentry.github.io/make-novice/)</li><li>[How to do Reproducible Computational  Analysis](https://www.youtube.com/watch?v=SRItP6PSu4U&feature=youtu.be)</li></ul> |
|   6   | 2016-10-18 | Tue | Environment management (package dependencies, managing versions) | <ul><li>[`packrat`](https://rstudio.github.io/packrat/walkthrough.html)</li><li>[virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/)</li><li>[conda's YAML file](http://conda.pydata.org/docs/using/envs.html)</li></ul> |
|7	| 2016-10-20 | Thu | Environment management: containerization with Docker | <ul><li>[R Docker tutorial](http://ropenscilabs.github.io/r-docker-tutorial/)</li></ul> |
|8      | 2016-10-13 | Thu | Project and file management 102 + more version control (branching) | <ul><li>[branching in Git](http://rogerdudler.github.io/git-guide/#branching)</li></ul> |

Time: 9:30am-10:50am

## Labs

| Week  | Lab topic   | Lab Due Date | Peer Review Due Date |
|-------|-------------|----------|--------------------------|
| [1](labs/lab1.md) | Project organization and management + writing scripts with arguments | 2016-10-04 | NA |
| [2](labs/lab2.md) | Creating reports with R Markdown, Pweave and Jupyter notebook | 2016-10-11 | NA |
| [3](labs/lab3.md) | Project management, collaboration and automation | 2016-10-18 | 2016-10-21 (2:00 pm)|
| [4](labs/lab4.md) | Managing your environment | 2016-10-25 | NA |

notes:
- all labs and peer review(s) are due at 2:00 pm
- for labs with peer review, peer review is worth 15% of the lab grade

## Quizzes
|     | Time | Date | Location |
|-----|------|------|----------|
| 1 | 14:00 - 14:30 | 2016-10-11 | ESB 1042 |
| 2 | 15:00 - 15:30 | 2016-10-26 | ESB 1042 |


## Prerequisites
* DSCI 511 (Programming for Data Science)
* DSCI 521 (Computing Platforms for Data Science)


## Lecture Learning Objectives:
1. Project and file management 101 + Version control via RStudio

	By the end of the lecture, students are expected to be able to:
	- Create a well-organized data analysis project directory structure
	- Write appropriate documentation (*e.g.,* README.md)
	- Set-up an R project
	- Set-up a project with distributed version control and remote servers (*e.g.,* GitHub) through RStudio

2. Scaling up: read-eval-print-loop (REPL) processes versus non-interactive scripts

	By the end of the lecture, students are expected to be able to:
	- Explain when it is optimal to work in a read-eval-print-loop (REPL) framework and when it is optimal to shift to using non-interactive scripts
	- Be able to create simple scripts in Python and R that can take input and be run from the command line

3. Scaling up cont'd: Create reproducible reports and workflows in R Markdown and R Notebook

	By the end of the lecture, students are expected to be able to:
	- Describe situations where they would choose to write a script versus a R Markdown report
	- Use R Markdown to create reports that runs simple analysis, the displays code outputs as stdout, tables and figures
	- Describe the situations when they would want to use R Markdown outputs of html_document, pdf_document, and github_document
	- Run R Markdown files from the command line
	- Write scripts that are documented so that reports can be generated from them (via `knitr::spin`)
	- Use ezknitr to manage where documents are rendered to

4. Scaling up cont'd: Create reproducible reports and workflows in Python's Pweave & Jupyter notebook

	By the end of the lecture, students are expected to be able to:
	- Write scripts in Python that are documented so that reports can be generated from them (via `Pweave`) to various outputs (e.g., html, pdf, Markdown)
	- Create reports in the Jupyter notebook
	- Working with/running Jupyter notebooks non-interactively (batch, scheduling, and reports)

6. Automated workflows; introduction to build/automation tool

	By the end of the lecture, students are expected to be able to:
	- Write a simple automated analysis pipeline using Make
	- Generate graph of dependencies from GNU-Make

7. Environment management (package dependencies, managing versions)

	By the end of the lecture, students are expected to be able to:
	- Write code where they wrap something in another language inside of Python or R
	- Correctly document analysis dependencies and load them in a logical place in the script/report
	- Use language specific tools to manage package dependencies (packrat (R), conda's yaml file, virtualenv)

8. Environment management: containerization with Docker

	By the end of the lecture, students are expected to be able to:
	- Use pre-existing Docker images to perform read-eval-print-loop (REPL) analysis in a reproducible environment
	- Batch run analysis scripts and reports in a Docker container
	- Write dockerfiles to modify pre-existing containers
	- Share containers on Docker Hub

5. Project and file management 102 + more version control

	By the end of the lecture, students are expected to be able to:
	- Why, Where and What to document
	- Organize files with appropriate naming conventions
	- More version control: introduction to branches
