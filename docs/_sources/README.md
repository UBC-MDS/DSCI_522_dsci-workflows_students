# DSCI 522: Data Science Workflows

## Introduction
Data-rich projects can quickly grow out-of-hand and become irreproducible in the absence of deliberate effort at organization, tool choice, and process. This course will teach basic principles of sound data scientific workflows and will develop skills implementing them in appropriate state-of-the-art systems and languages (e.g., Python and R).

__Course website__: https://pages.github.ubc.ca/MDS-2020-21/DSCI_522_dsci-workflows_students

__Course webpage__: https://github.ubc.ca/MDS-2020-21/DSCI_522_dsci-workflows_students

__Slack Channel__: https://ubc-mds.slack.com/messages/522_dsci-workflows

## Learning Outcomes

By the end of the course, students are expected to be able to:

1. Map a data analysis question to appropriate analysis.
1. Write R, Python and shell scripts for non-interactive data analysis.
1. Run literate coding documents (Jupyter notebooks and R Markdown documents) non-interactively.
1. Use a Git/GitHub forking-pull request collaboration approach to collaboratively work on a data analysis project.
1. Automate data science workflows (using e.g., Make).
1. Manage project software and environment dependencies (using e.g., Docker)

## Teaching Team

At your service!

| Position           | Name    | Slack Handle | GHE Handle | 
| :----------------: | :-----: | :----------: | :--------: | 
| Lecture & Lab Instructor | Tiffany | `@tiffany`   | `@timberst` | 
| Teaching Assistant | Arjun Baghela | @abaghela | @abaghela |
| Teaching Assistant | Jordan Bourak | @Jordan Bourak   | @jnbk |
| Teaching Assistant | 	Analise Hofmann | @(TA) Analise 521 | @ahofmann | 
| Teaching Assistant | Eric Lee | @Eric | @elee0920 |
| Teaching Assistant | Hossameldin Mohammed | @Hossam | @hos40044 |


## Deliverables

This is a __project-based course__. You will work in randomly assigned groups of three (or four, if needed) for the project milestones. There are also individual weekly assignments that act as stepping stones to the project milestones. Finally, because collaboration is so important in data science, 1/5 of your final grade will be devoted to how good of a team member you were. A combination of peer evaluation and GitHub history will be used to evaluate this. 

| Assessment       | Weight  | Deadline        | 
|------------------|---------|------------------|
| Milestone 1 - Proposal and data download scipt | 12%     | 2020-11-21 11:59 PT | 
| Milestone 2 -  Working analysis scripts and report draft | 20%     | 2020-11-28 11:59 PT |
| Milestone 3 - Data analysis pipeline with Make | 20%     | 2020-12-05 @ 11:59 PT | 
| Milestone 4 - Final project submission (with ultimate reproducibility) | 20%     | 2020-12-12 11:59 PT     | 
| Individual assignment 1 | 2%     | 2020-11-21 11:59 PT |
| Individual assignment 2 | 2%     | 2020-11-28 11:59 PT |
| Individual assignment 3 | 2%     | 2020-12-05 11:59 PT |
| Individual assignment 4 | 2%     | **2020-12-11 11:59 PT** |
| Team work |  20% | **2020-12-13 11:59 PT** |

## Schedule

| Lecture|   Topic  | Required Readings | Additional Readings |
|--------|---------|------------|-----------------------------|
| 1 | Introduction to Data Science Workflows | <ul><li>[Art of Data Science Chapters 1 - 3](https://leanpub.com/artofdatascience)</li><li>[Best Practices for Scientific Computing](http://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001745)</li></ul> |<ul><li>[Hilary Parker's Opinionated Analysis Development paper](https://peerj.com/preprints/3210/)</li><li>[A Quick Guide to Organizing Computational Biology Projects](http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000424)</li></ul> |
| 2 |  Scaling up: read-eval-print-loop (REPL) processes versus non-interactive scripts | <ul><li>[Art of Data Science Chapters 4](https://leanpub.com/artofdatascience)</li></ul> | <ul><li>[`docopt` python documentation](http://docopt.org/)</li><li>[Docopt, beautiful command-line options for R talk slides](https://www.slideshare.net/EdwindeJonge1/docopt-user2014)</li></ul>|
| 3 |  Scaling up cont'd: using literate coding documents (Jupyter notebooks and R Markdown documents) non-interactively| <ul><li>[Art of Data Science Chapter 5 - 6](https://leanpub.com/artofdatascience)</li></ul> | <ul><li>[R Markdown Cheatsheet](https://www.rstudio.com/wp-content/uploads/2015/02/rmarkdown-cheatsheet.pdf)</li><li>[jupyter nbconvert](http://nbconvert.readthedocs.io/en/latest/usage.html)</li><li>[Using Python and R in harmony - the reticulate cheat sheet](https://github.com/rstudio/cheatsheets/raw/master/reticulate.pdf)</li></ul> |
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

## Dealing With COVID-19

The [COVID-19 pandemic](https://www.who.int/emergencies/diseases/novel-coronavirus-2019/events-as-they-happen) has affected us all in different ways: it's okay to not be okay, and we all need to support each other during this time. With that said:

- My (virtual) door is always open, please feel free to talk to me about how you're doing and if/how I can help you (and if I can't help you, I can point you in the direction of someone who can);
- You don't ever need to explain yourself; if you need support, need to miss a class, or need extra time for an assignment, just ask;
- UBC has [great student support resources](https://students.ubc.ca/covid19) related to COVID-19 (and otherwise).

Further, teaching/learning an intense graduate course like MDS online is a very new concept to all of us. If you have feedback on how I can improve the teaching experience, don't hesitate to reach out - I'm sure things won't be perfect from the get-go.

Finally, here is an official statement from UBC regarding the online learning experience:

>*During this pandemic, the shift to online learning has greatly altered teaching and studying at UBC, including changes to health and safety considerations. Keep in mind that some UBC courses might cover topics that are censored or considered illegal by non-Canadian governments. This may include, but is not limited to, human rights, representative government, defamation, obscenity, gender or sexuality, and historical or current geopolitical controversies. If you are a student living abroad, you will be subject to the laws of your local jurisdiction, and your local authorities might limit your access to course material or take punitive action against you. UBC is strongly committed to academic freedom, but has no control over foreign authorities (please visit http://www.calendar.ubc.ca/vancouver/index.cfm?tree=3,33,86,0 for an articulation of the values of the University conveyed in the Senate Statement on Academic Freedom). Thus, we recognize that students will have legitimate reason to exercise caution in studying certain subjects. If you have concerns regarding your personal situation, consider postponing taking a course with manifest risks, until you are back on campus or reach out to your academic advisor to find substitute courses. For further information and support, please visit: http://academic.ubc.ca/support-resources/freedom-expression.*
