# Proposal:
## Project set-up & identify the data set and plan of action
rubric={mechanics:3,reasoning:2,writing:1}

#### Goal

Here you will work [in assigned teams of two or three](https://github.ubc.ca/MDS-2018-19/DSCI_522_dsci-workflows_students/blob/master/teams/teams.csv) identify a data set, question and hypothesis that you will use for your final project. For the proposal, you will also set-up a Github repository with an appropriate file and directory structure. In the next two milestones, you will build on this project to create a data analysis pipeline. Your final project will be a reproducible data analysis pipeline (a collection of R/Python scripts with a Jupyter/Rmd report tied together by a Makefile and managed by Docker).

#### Submission Instructions:

- Be sure to follow the [general lab instructions](https://ubc-mds.github.io/resources_pages/general_lab_instructions/) that are relevant, while also following the specific instructions described in the [expectations](#expectations) section below.

## Project set-up
- In the [UBC-MDS GitHub organization](https://github.com/UBC-MDS) on github.com, set-up a public repository with a reasonable name for your project. We are using github.com for public repos because we will eventually be using some fancy tooling (*e.g.,* automated builds on Dockerhub) in this project. You need to put your scripts in a public repo on github.com. Additionally, this will help you build a portfolio of your work you can share with others.
- In your Github repository create an appropriate file and directory structure for a data analysis project (think about what you learned in [lab 4 from DSCI 521](https://github.ubc.ca/MDS-2018-19/DSCI_521_platforms-dsci_students/blob/master/source/lab4/lab4.md) and maybe try out the [ProjectTemplate](http://projecttemplate.net/getting_started.html) R package).
- You **must** include the URL to your project's repo in your `proposal` repo's `README.md` file so we know where to find it.
- Create a release on your project repo named v0.1 and submit that URL in your `proposal` repo's `README.md` file so we know where to find it.

## Identify data set, question, & plan of action for analysis to answer that question

1. Choose a public data set from the web that you are interested in to carry out a small data analysis. You may also use any data set we have previously worked with in MDS. **Prove to us that you can load the data set into R or Python** (this could be demonstrating by writing a script that downloads the data and saves a snippet of it, for example).
2. With that data set, identify a question you would like to ask from it that could be answered by some simple analysis and visualization (more on this below). State what kind of question it is (it should be one of the 6 types discussed in lecture 1).
3. Make a plan of how you will analyze the data (report an estimate and confidence intervals? hypothesis test? classification with a decision tree?). Choose something you know how to do (report an estimate and confidence intervals, a two-group hypothesis), or will learn how to do in the first week of block 3 (ANOVA, classification with a decision tree).
4. Suggest how you might summarize the data to show this as a table or a number, as well as how you might show this as a visualization.

Document these 4 requirements in the project's `README.md` file.

#### Data set sources
- past MDS homework
- [UCI Machine Learning Repository: Data Sets](https://archive.ics.uci.edu/ml/datasets.html)
- [Google Data set search engine](https://toolbox.google.com/datasetsearch)

## Expectations
- You should be committing to git every time you work on this project.
- git commit messages should be meaningful. These will be marked. It's OK if one or two are
less meaningful, but most should be.
- After the repository is set-up, each group member should fork the repository to their personal GitHub.com account and work there, and send pull-requests of their work to the upstream repo (the one they forked). The other team mate should review, critique (if necessary) and finally accept their team mates pull request.
- Use GitHub issues to communicate to their team mate (as opposed to email or Slack)
- Your question, analysis and visualization should make sense. It doesn't have to be complicated.
- You should use proper grammar and full sentences in your README. Point form may occur, but should
be less than 10% of your written documents.
- You **must** include the URL of your public project's repo in the `README.md` file of your `proposal`'s repo,  so we know where to find it.
- Create a release on your project repo named v1.0 and submit that URL in your `proposal` repo's `README.md` file so we know where to find it.
