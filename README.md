# DSCI 522: Data Science Workflows

## Introduction
Data-rich projects can quickly grow out-of-hand and become irreproducible in the absence of deliberate effort at organization, tool choice, and process. This course will teach basic principles of sound data scientific workflows and will develop skills implementing them in appropriate state-of-the-art systems and languages (e.g., Python and R).

__Course webpage__: https://github.ubc.ca/MDS-2018-19/DSCI_522_dsci-workflows_students

__Slack Channel__: https://ubc-mds.slack.com/messages/522_dsci-workflows

## Learning Outcomes

By the end of the course, students are expected to be able to:

0. Map a data analysis question to appropriate analysis.
1. Write R, Python and shell scripts for non-interactive data analysis.
2. Run literate coding documents (Jupyter notebooks and R Markdown documents) non-interactively.
4. Use a Git/GitHub forking-pull request collaboration approach to collaboratively work on a data analysis project.
5. Automate data science workflows (using e.g., Make).
6. Manage project software and environment dependencies (using e.g., Docker)

## Teaching Team

| Position | Name  | Slack Handle | GHE Handle | Office Hour | Lab Section |
| :------: | :---: | :----------: | :--------: | :----------:|:--------:|
| Lecture & Lab Instructor| Tiffany Timbers | `@tiffany` |  `@timberst` | Fridays at 1:00 - 2:00 in ESB 3152 | all |
| Teaching Assistant | 	Ali Mirza | `@Ali Mirza` | `@amirza17` | Tuesdays 1:00 - 2:00 in ESB 3173 | L01 |
| Teaching Assistant | Ozum Kafaee | `@ozum`  | `@ozum` | Thursdays 3:30 - 4:30 in ESB 3174| L03 |
| Teaching Assistant | Eric Fu | `@eric-f` | `@ericfu` | Wednesdays 12:30 - 1:30 in ESB 1043  | L02 |

*note - Attendance at office hours is optional* 

## Project deadlines

This is an __project-based course__. You will work in randomly assigned groups of two. You'll be evaluated as follows:

| Assessment       | Weight  | Deadline        | Location |
|------------------|---------|------------------|----------|
| Proposal | 10%     | 2018-11-17 @ 18:00 | Submit to Github |
| Milestone 1 -  working analysis scripts and report draft | 20%     | 2018-11-24 @ 18:00 | Submit to Github |
| Milestone 2 - data analysis pipeline with Make | 20%     | 2018-12-01 @ 18:00 | Submit to Github |
| Final project - reproducibility with Docker | 40%     | 2018-12-08 @ 18:00     | Submit to Github |
| Team work |  10% | **2018-12-11 @ 18:00** | Submit to Github |

## Schedule


| Lecture|   Topic  | Readings |
|--------|---------|------------|
| 1 | [Introduction to Data Science Workflows](lectures/01_lecture-intro-to-ds-workflows.ipynb) | <ul><li>[Art of Data Science Chapters 1 - 3](https://leanpub.com/artofdatascience)</li><li>[Best Practices for Scientific Computing](http://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001745)</li><li>[A Quick Guide to Organizing Computational Biology Projects](http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000424)</li></ul> |
| 2 |  [Scaling up: read-eval-print-loop (REPL) processes versus non-interactive scripts](lectures/02_lecture-intro-to-scripts.ipynb) | <ul><li>[Art of Data Science Chapters 4](https://leanpub.com/artofdatascience)</li><li>[Software Carpentry lesson: Command line arguments with R](http://swcarpentry.github.io/r-novice-inflammation/05-cmdline/)</li><li>[Command line arguments with Python](https://docs.python.org/3.5/howto/argparse.html)</li></ul>  |
| 3 |  [Scaling up cont'd: using literate coding documents (Jupyter notebooks and R Markdown documents) non-interactively.](lectures/03_lecture-notebooks-at-command-line.ipynb) | <ul><li>[Art of Data Science Chapter 5](https://leanpub.com/artofdatascience)</li><li>[R Markdown Cheatsheet](https://www.rstudio.com/wp-content/uploads/2015/02/rmarkdown-cheatsheet.pdf)</li><li>[jupyter nbconvert](http://nbconvert.readthedocs.io/en/latest/usage.html)</li></ul> |
| 4 |  [Data Analysis pipelines and shell scripting](lectures/04_lecture-shell-driver-scripts.md) | <ul><li>[Art of Data Science Chapter 6 - 8](https://leanpub.com/artofdatascience)</li></ul>|
| 5 | [Automated workflows; introduction to the build/automation tool Make](lectures/05_lecture-make-driver-script.md) | <ul><li>[Art of Data Science Chapters 9](https://leanpub.com/artofdatascience)</li><li>[Software Carpentry Make lesson](http://swcarpentry.github.io/make-novice/)</li><li>[Make reference sheet](http://swcarpentry.github.io/make-novice/reference)<li>[How to do Reproducible Computational  Analysis](https://www.youtube.com/watch?v=SRItP6PSu4U&feature=youtu.be)</li></ul> |
| 6 | [Environment management: containerization with Docker part I](lectures/06_lecture-intro-to-docker.ipynb) | <ul><li>[Art of Data Science Chapter 10](https://leanpub.com/artofdatascience)</li><li>[What is a Container](https://www.docker.com/resources/what-container)</li><li>[An Introduction to Rocker: Docker Containers for R](https://arxiv.org/pdf/1710.03675.pdf)</li></ul> |
| 7 |  [Environment management: containerization with Docker part II](lectures/07_lecture_writing_dockerfiles.ipynb) | <ul><li>[Docker cheat sheet](https://github.com/wsargent/docker-cheat-sheet)</li><li>[Docker docs](https://docs.docker.com/engine/reference/commandline/build/)</li></ul>|
| 8 | [Conda (another way to manage your environment) and reproducibility wrap-up](lectures/08_lecture_conda_and_repro_wrap_up.ipynb) | |

## Textbooks:
- [Art of Data Science](https://leanpub.com/artofdatascience) by Roger Peng & Elizabeth Matsui  (very cheap or even free!)

## Related fun?
- [Not so standard deviations](http://nssdeviations.com/) podcast with co-hosts: Roger Peng of the Johns Hopkins Bloomberg School of Public Health and Hilary Parker of Stitch Fix.
- [Simply Statistics](https://simplystatistics.org/):
A statistics blog by Rafa Irizarry, Roger Peng, and Jeff Leek
