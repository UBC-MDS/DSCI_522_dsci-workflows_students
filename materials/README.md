# DSCI 522: Data Science Workflows

## Introduction
Data-rich projects can quickly grow out-of-hand and become irreproducible in the absence of deliberate effort at organization, tool choice, and process. This course will teach basic principles of sound data scientific workflows and will develop skills implementing them in appropriate state-of-the-art systems and languages (e.g., Python and R).

__Course website__: https://pages.github.ubc.ca/MDS-2022-23/DSCI_522_dsci-workflows_students

__Course webpage__: https://github.ubc.ca/MDS-2022-23/DSCI_522_dsci-workflows_students

__Slack Channel__: https://ubc-mds.slack.com/messages/522_dsci-workflows

## Learning Outcomes

By the end of the course, students are expected to be able to:

1. Map a data analysis question to appropriate analysis.
1. Write R, Python and shell scripts for non-interactive data analysis.
1. Run literate coding documents (Jupyter notebooks and R Markdown documents) non-interactively.
1. Use a Git/GitHub to collaboratively work on a data analysis project.
1. Automate data science workflows (using e.g., Make).
1. Manage project software and environment dependencies (using e.g., Docker)

## Teaching Team

At your service!

| Position           | Name    | Slack Handle | GHE Handle | 
| :----------------: | :-----: | :----------: | :--------: | 
| Lecture and Lab Instructor | Florencia D'Andrea | `@Florencia`   | `@fdandrea` |
| Teaching Assistant | Daniel Ramandi | `@Daniel (TA)` | `@dani014` |
| Teaching Assistant | Aditi Nagaraj Nallan | `@Aditi Nallan (TA)`   | `@aditi48n` |
| Teaching Assistant | Mohamad Amin Mohamadi | `@Amin` | `@lemohama` | 
| Teaching Assistant | Eric Lee | `@Eric` | `@elee0920` |
| Teaching Assistant | Keng Man Glenn Chang | `@Glenn Chang (TA)` | `@glenn03` |
| Teaching Assistant | Abdul Muntakim Rafi | `@Rafi` | `@rafi11` |


## Deliverables

This is a __project-based course__. You will work in randomly assigned groups of three (or four, if needed) for the project milestones. There are also individual weekly assignments that act as stepping stones to the project milestones. Finally, because collaboration is so important in data science, 1/5 of your final grade will be devoted to how good of a team member you were. A combination of peer evaluation and GitHub history will be used to evaluate this. 

| Assessment       | Weight  | Deadline        | 
|------------------|---------|------------------|
| Milestone 1 - Proposal and data download script | 20%     | 2022-11-19 18:00 PT | 
| Milestone 2 -  Working analysis scripts and report draft | 20%     | 2022-11-26 18:00 PT |
| Milestone 3 - Data analysis pipeline with Make | 20%     | 2022-12-03 18:00 PT | 
| Milestone 4 - Final project submission (with ultimate reproducibility) | 20%     | 2022-12-10 18:00 PT     | 
| Individual assignment 1 | 2%     | 2022-11-19 18:00 PT |
| Individual assignment 2 | 2%     | 2022-11-26 18:00 PT |
| Peer Review | 10%     | 2022-12-03 18:00 PT |
| Individual assignment 4 | 2%     | 2022-12-10 18:00 PT |
| Team work |  4% | 2022-12-14 18:00 PT** |
| Team work multiplier |  final grade * multiplier | NA |
## Schedule

| Lecture|   Topic  | Required Readings | Additional Readings |
|--------|---------|------------|-----------------------------|
| 1 | Introduction to Data Science Workflows | <ul><li>[Art of Data Science Chapters 1 - 3](https://leanpub.com/artofdatascience)</li><li>[Best Practices for Scientific Computing](http://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001745)</li></ul> |<ul><li>[Hilary Parker's Opinionated Analysis Development paper](https://peerj.com/preprints/3210/)</li><li>[A Quick Guide to Organizing Computational Biology Projects](http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000424)</li></ul> |
| 2 |  Scaling up: read-eval-print-loop (REPL) processes versus non-interactive scripts | <ul><li>[Art of Data Science Chapters 4](https://leanpub.com/artofdatascience)</li></ul> | <ul><li>[`docopt` python documentation](http://docopt.org/)</li><li>[Docopt, beautiful command-line options for R talk slides](https://www.slideshare.net/EdwindeJonge1/docopt-user2014)</li></ul>|
| 3 |  Scaling up cont'd: using literate coding documents (Jupyter notebooks and R Markdown documents) non-interactively| <ul><li>[Art of Data Science Chapter 5 - 6](https://leanpub.com/artofdatascience)</li></ul> | <ul><li>[R Markdown Cheatsheet](https://www.rstudio.com/wp-content/uploads/2015/02/rmarkdown-cheatsheet.pdf)</li><li>[`bookdown`](https://bookdown.org/yihui/bookdown/)</li><li>[Jupyter book](https://jupyterbook.org/intro.html)</li><li>[jupyter nbconvert](http://nbconvert.readthedocs.io/en/latest/usage.html)</li><li>[Using Python and R in harmony - the reticulate cheat sheet](https://raw.githubusercontent.com/rstudio/cheatsheets/main/reticulate.pdf)</li></ul> |
| 4 |  Data Analysis pipelines and shell scripting | <ul><li>[Art of Data Science Chapter 7 - 8](https://leanpub.com/artofdatascience)</li></ul>|  |
| 5 | Automated workflows; introduction to the build/automation tool Make | <ul><li>[Art of Data Science Chapters 9](https://leanpub.com/artofdatascience)</li></ul> | <ul><li>[STAT 545 - Chapter 36: Automating data-analysis pipelines](https://stat545.com/automating-pipeline.html)</li><li>[Software Carpentry Make lesson](http://swcarpentry.github.io/make-novice/)</li><li>[Make reference sheet](http://swcarpentry.github.io/make-novice/reference)<li>[How to do Reproducible Computational  Analysis](https://www.youtube.com/watch?v=SRItP6PSu4U&feature=youtu.be)</li></ul> |
| 6 | Environment management: containerization with Docker part I| <ul><li>[Art of Data Science Chapter 10](https://leanpub.com/artofdatascience)</li></ul> | <ul><li>[What is a Container](https://www.docker.com/resources/what-container)</li><li>[An Introduction to Rocker: Docker Containers for R](https://arxiv.org/pdf/1710.03675.pdf)</li></ul> |
| 7 |  Environment management: containerization with Docker part II | | <ul><li>[Docker cheat sheet](https://github.com/wsargent/docker-cheat-sheet)</li><li>[Docker docs](https://docs.docker.com/engine/reference/commandline/build/)</li></ul>|
| 8 | Environment management: containerization with Docker part III & Reproducibility wrap-up | | |

## Textbooks:
- [Art of Data Science](https://leanpub.com/artofdatascience) by Roger Peng & Elizabeth Matsui  (very cheap or even free!)
    - Note there are two packages, you only need to get the textbook ("The Book" package), you do not need to get the lecture videos!

## Related fun?
- [Not so standard deviations](http://nssdeviations.com/) podcast with co-hosts: Roger Peng of the Johns Hopkins Bloomberg School of Public Health and Hilary Parker of Stitch Fix.
- [Simply Statistics](https://simplystatistics.org/):
A statistics blog by Rafa Irizarry, Roger Peng, and Jeff Leek

## Class Schedule & office hours

See [calendar](https://ubc-mds.github.io/calendar/).

## Policies

Please see the general [MDS policies](https://ubc-mds.github.io/policies/).

### Where to find help?

If you are struggling eith any situation, please, be free to contact me in a direct message via Slack. I will reply as soon as possible.

## Working during the COVID-19 global pandemic

We are working together on this course during this transition period between hybrid to in-person teaching and learning. Everyone is struggling to some extent. If you tell me you are having trouble, I am not going to judge you or think less of you. I hope you will extend me the same grace! Let's try to be open with each other and help each other. 

Here are some ground rules:

- If you are unable to submit a deliverable on time, please reach out **before** the deliverable is due.
- If you need extra support, the teaching team is here to work with you. Our goal is to help each of you succeed in the course.
- If you are struggling with the material, getting back to in-person teaching and learning, or anything else, please reach out. I will try to find time and listen to you empathetically.
- If I am unable to help you, I might know someone who can. UBC has some [great student support resources](https://students.ubc.ca/support).

### [Covid Safety at UBC](https://srs.ubc.ca/covid-19/ubc-campus-rules-guidance-documents/#COVID-19%20Campus%20Rules)

Please read [Covid Campus Rules](https://srs.ubc.ca/covid-19/ubc-campus-rules-guidance-documents/#COVID-19%20Campus%20Rules).  

**Masks:** This class is going to be in person. UBC no longer requires students, faculty and staff to wear non-medical masks, but continues to recommend that masks be worn in indoor public spaces. 

**Your personal health:**
If you are ill or believe you have COVID-19 symptoms or been exposed to SARS-CoV-2 use the [Thrive Health](https://bc.thrive.health/covid19/en) self-assessment tool for guidance, or download the [BC COVID-19 Support App](https://welcome.thrive.health/bc-covid19-app) for iOS or Android device and follow the instructions provided. Follow the advice from [Public Health](https://www2.gov.bc.ca/gov/content/covid-19/info/restrictions).

Stay home if you have recently tested positive for COVID-19 or are required to quarantine. You can check [this website](http://www.bccdc.ca/health-info/diseases-conditions/covid-19/self-isolation#Who) to find out if you should self-isolate or self-monitor. If you are unable to submit a deliverable on time or unable to appear for an in-person quiz, check out [MDS policies](https://ubc-mds.github.io/policies/) on academic concession and remote quiz requests. 

---

Authors: Tiffany A. Timbers, Firas Moovsi, Florencia D'Andrea

## License: 
Software licensed under the [MIT License](https://spdx.org/licenses/MIT.html), non-software content licensed under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) License](https://creativecommons.org/licenses/by-nc-sa/4.0/). See the [license file](LICENSE.md) for more information.



