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

## Teaching Team

| Position | Name  | Slack Handle | GHE Handle | Office Hour |
| :------: | :---: | :----------: | :--------: | :----------:|
| Instructor & Teaching Fellow | Tiffany Timbers | `@tiffany` |  `@timberst` | Thurs 12:30 - 13:30 |
| Teaching Assistant | Gursimran Singh | `@msimar` | `@msimar` | Thurs 16:00 - 17:00 |
| Teaching Assistant | Joseph Khoury | `@joseph`  | `@josephjk` | Mon 13:00 - 14:00 |

*note - see Calendar for office hour location and exact dates*

## Schedule


| Lecture|      Date  | Day |  Topic  | Reading(s) |
|--------|------------|-----|---------|------------|
| 1      | 2017-11-16 | Thu | Introduction to Data Science Workflows and project & file management 101 | <ul><li>[Good Enough Practices in Scientific Computing](https://swcarpentry.github.io/good-enough-practices-in-scientific-computing/)</li><li>[Best Practices for Scientific Computing](http://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001745)</li><li>[A Quick Guide to Organizing Computational Biology Projects](http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000424)</li><li>[Nine simple ways to make it easier to (re)use your data](https://ojs.library.queensu.ca/index.php/IEE/article/view/4608/0)</li></ul> |
| 2      | 2017-11-21 | Tue |  Scaling up: read-eval-print-loop (REPL) processes versus non-interactive scripts | <ul><li>[Software Carpentry lesson: Command line arguments with R](http://swcarpentry.github.io/r-novice-inflammation/05-cmdline/)</li><li>[Command line arguments with Python](https://docs.python.org/3.5/howto/argparse.html)</li></ul>  |
| 3      | 2017-11-23 | Thu |  Scaling up cont'd: Create reproducible reports and workflows in R & Python | <ul><li>[Intro to R Markdown](https://rstudio-pubs-static.s3.amazonaws.com/105639_5c0a8f83c268447d8e9ea334e37e3ce1.html#rmarkdown-time)<li>[R Markdown Cheatsheet](https://www.rstudio.com/wp-content/uploads/2015/02/rmarkdown-cheatsheet.pdf)</li><li>[Use other languages in knitr](http://yihui.name/knitr/demo/engines/)</li><li>[jupyter nbconvert](http://nbconvert.readthedocs.io/en/latest/usage.html)</li></ul> |
| 4      | 2017-11-28 | Tue |  Data Analysis pipelines | |
| 5      | 2017-11-30 | Thu | Automated workflows; introduction to build/automation tools | <ul><li>[Software Carpentry Make lesson](http://swcarpentry.github.io/make-novice/)</li><li>[How to do Reproducible Computational  Analysis](https://www.youtube.com/watch?v=SRItP6PSu4U&feature=youtu.be)</li></ul> |
| 6      | 2017-12-05 | Tue | Environment management (package dependencies, managing versions) | <ul><li>[`packrat`](https://rstudio.github.io/packrat/walkthrough.html)</li><li>[virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/)</li><li>[conda's YAML file](http://conda.pydata.org/docs/using/envs.html)</li></ul> |
| 7      | 2017-12-07 | Thu |  Environment management: containerization with Docker part I | <ul><li>[An Introduction to Rocker: Docker Containers for R](https://arxiv.org/pdf/1710.03675.pdf)</li></ul> |
| 8      | 2017-12-12 | Tue |  Environment management: containerization with Docker part II | |

Time: 9:30am-10:50am

## Assessment
| Deliverable | % grade |
|------------|----------|
| Lab 1           | 25  |
| Milestone 1 | 5 |
| Milestone 2 (project at halfway point) &ast; | 30 |
| Milestone 3 (complete project) | 40 |

&ast; This will be peer reviewed

## Labs

| Week  | Lab topic   | Lab Due Date | Peer Review Due Date |
|-------|-------------|----------|--------------------------|
| [1](labs/lab1/lab1.md) | Data Science workflows, project organization and management exercises | 2017-11-19 | NA |

## Project
| Week  | Milestone   | Due Date | Peer Review Due Date |
|-------|-------------|----------|--------------------------|
| [2](milestones/milestone1/milestone1.md) | 1. Project set-up & identify the dataset, question, hypothesis and plan of action | 2017-12-03 | NA |
| [3](milestones/milestone2/milestone2.md) | 2. Data Analysis pipeline draft | 2017-12-10 | 2017-12-12 |
| [4](milestones/milestone3/milestone3.md) | 3. Fully automated and reproducible Data Analysis pipeline | 2017-12-17 | NA |

## Prerequisites
* DSCI 511 (Programming for Data Science)
* DSCI 521 (Computing Platforms for Data Science)


## Lecture Learning Objectives:
1. Introduction to Data Science Workflows and project & file management 101

	By the end of the lecture, students are expected to be able to:
	- Outline and identify the key components to a Data Science Workflow
	- Explain the importance of using version control (with meaningful commit messages) throughout a project
	- Create a well-organized data analysis project directory structure with good filenames

2. Scaling up: read-eval-print-loop (REPL) processes versus non-interactive scripts

	By the end of the lecture, students are expected to be able to:
	- Explain when it is optimal to work in a read-eval-print-loop (REPL) framework and when it is optimal to shift to using non-interactive scripts
	- Be able to create simple scripts in Python and R that can take input and be executed from the command line

3. Scaling up cont'd: Create reproducible reports and workflows in R & Python

	By the end of the lecture, students are expected to be able to:
	- Describe situations where they would choose to write a script versus a Markdown report
	- Use R Markdown to create reports that runs simple analysis, the displays code outputs as stdout, tables and figures
	- Describe the situations when they would want to use R Markdown outputs of html_document, pdf_document, and github_document
	- Run R Markdown files from the command line
	- Use ezknitr to manage where documents are rendered to
	- Create reports in the Jupyter notebook
	- Working with/running Jupyter notebooks non-interactively (batch, scheduling, and reports)

4. Data Analysis pipelines

	By the end of the lecture, students are expected to be able to:
	- Create a data analysis pipeline using R, Python and the Unix shell to run multiple scripts
	- Hand Draw manual dependency diagrams
	- Write code where they wrap something in another language inside of Python or R

5. Automated workflows; introduction to build/automation tool

	By the end of the lecture, students are expected to be able to:
	- Write a simple automated analysis pipeline using Make

6. Environment management (package dependencies, managing versions)

	By the end of the lecture, students are expected to be able to:
	- Correctly document and manage analysis dependencies, as well as load them in a logical place in the script/report
	- Use language specific tools to manage package dependencies (packrat (R), conda's yaml file, virtualenv)

7. Environment management: containerization with Docker part I

	By the end of the lecture, students are expected to be able to:
	- Use pre-existing Docker images to run software (GUI and command line, e.g., Generate graph of dependencies from GNU-Make)
	- Use pre-existing Docker to perform read-eval-print-loop (REPL) analysis in a reproducible environment

7. Environment management: containerization with Docker part II

	By the end of the lecture, students are expected to be able to:
	- Batch run analysis scripts and reports in a Docker container
	- Write dockerfiles to modify pre-existing containers
	- Share containers on Docker Hub
