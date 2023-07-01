# Milestone 1
### Overall project summary

In this course, you will work in assigned teams of three or four (see group assignments on Canvas) to answer a  question using a publicly available dataset. In order to answer this question, you will perform a complete data analysis, from data import to communication of results, while placing significant emphasis on reproducibility and transparency. To complete the analysis you will write 4-5 R and/or Python scripts, create a reproducible report (in Jupyter or R Markdown), as well as automate your data analysis workflow using GNU Make. Software and environment dependencies are to be made shippable and shareable via containerization with Docker.

An example final project can be seen here: [https://github.com/ttimbers/breast_cancer_predictor](https://github.com/ttimbers/breast_cancer_predictor)

### Milestone 1 summary
In this milestone, you will:
- [Milestone 1](#milestone-1)
    - [Overall project summary](#overall-project-summary)
    - [Milestone 1 summary](#milestone-1-summary)
    - [Submission Instructions:](#submission-instructions)
  - [1. Project set-up:](#1-project-set-up)
      - [i. Team work contract](#i-team-work-contract)
      - [ii. Code of Conduct file](#ii-code-of-conduct-file)
      - [Sample Codes of Conduct:](#sample-codes-of-conduct)
      - [iii. Contributing file](#iii-contributing-file)
      - [iv. License file](#iv-license-file)
  - [2. Project proposal](#2-project-proposal)
      - [Identify a data set, research question, & plan of action for analysis to answer that question](#identify-a-data-set-research-question--plan-of-action-for-analysis-to-answer-that-question)
      - [Data set sources](#data-set-sources)
  - [3. A script that downloads and saves the data](#3-a-script-that-downloads-and-saves-the-data)
  - [4. Exploratory data analysis in a literate code document](#4-exploratory-data-analysis-in-a-literate-code-document)
  - [5. Expectations](#5-expectations)

An example project milestone 1 can be seen here: [https://github.com/ttimbers/breast_cancer_predictor/tree/v1.1](https://github.com/ttimbers/breast_cancer_predictor/tree/v1.1)

### Submission Instructions:
- Be sure to follow the [general lab instructions](https://ubc-mds.github.io/resources_pages/general_lab_instructions/) that are relevant, while also following the specific instructions described in the [expectations](#expectations) section below.

## 1. Project set-up:
rubric={mechanics:20}
- In the [UBC-MDS GitHub organization](https://github.com/UBC-MDS) on github.com, set-up a public repository with a reasonable name for your project. We are using github.com and public repos because we will eventually be using some fancy tooling (*e.g.,* GitHub Actions) in this project. For this to work, all your work for this project (including scripts) should be developed and live in this repo (and/or forks of this repo) on GitHub.com.  Additionally, this will help you build a portfolio of your work you can share with others.
- In your Github repository create an appropriate file and directory structure for a data analysis project.
- Make sure you create the following 4 files that are important for collaboration:
  1. [Team work contract](#i-team-work-contract)
  2. [Code of Conduct file](#ii-code-of-conduct-file)
  3. [Contributing file](#iii-contributing-file)
  4. [License file](#iv-license-file)
  
#### i. Team work contract

This document will govern the working relationships on your team, and if done correctly, it should help you manage and resolve any issues that might arise when working in a group.

A team work contract communicates specifically **how** the core group of people who are working together and gives detail about the logisitics of working together and the expectations you have for each other.
Some aspects of the team work contract could be:
- How will work be distributed in a fair and equitable way?
- What are the expected work hours for the project? 
- How often will group meetings occur (you can read this slides abour [effective meetings](https://github.com/joelostblom/effective-meetings/blob/main/Effective%20Meetings.pdf))? 
- Will you have meeting agendas and minutes? If so, what will be the system for rotating through these responsibilities?
- What will be the style of working? 
    - Will you start each day with [stand-ups](https://www.atlassian.com/agile/scrum/standups), or submit a summary of your contributions 4 hours before each meeting? or something else?
- What is the quality of work each team member expects from themselves and each other?
- When are team members not available (e.g., evenings and Sundays because of family obligations). 
- And any other similar things that govern your working relationships.

Use this opportunity to use your prior knowledge/experience to improve your teamwork, communication, leadership, and organizational skills. 
You will need all of these for your capastone projects (and beyond)!

**Note - this document is fairly personal and does NOT need to reside in your public GitHub.com repo. Instead you can prove that you created this by pasting it into the text box for your Canvas homework submission for this milestone.**

#### ii. Code of Conduct file

In an attempt to create a safe, positive, productive, and happy community, many organizations and developers create a code of conduct for their projects.
A code of conduct in a Data Science project informs others of social norms, acceptable behaviour and general etiquette.
It is more outward facing than the team work contract discussed above.
We recommend [Project Include](https://projectinclude.org/writing_cocs) for a comprehensive guide to writing an effective Code of Conduct.

At minimum, we believe that a good/effective code of conduct should include:

- A Statement on diversity and inclusivity
- Details on expected, and unacceptable behaviour
- A list of consequences for unacceptable behaviour
- A procedure for reporting and dealing with unacceptable behaviour

#### Sample Codes of Conduct:

  - [UBC Data Science 100 CoC](https://github.com/UBC-DSCI/dsci-100/blob/master/CODE_OF_CONDUCT.md)
  - [idocde Coc](http://www.idocde.net/pages/35)
  - [Python Community CoC](https://www.python.org/psf/conduct/)
  - [Tidyverse CoC](https://github.com/tidyverse/tidyverse.org/blob/master/CODE_OF_CONDUCT.md)
  - [Pandas CoC](https://github.com/pandas-dev/pandas-governance/blob/master/code-of-conduct.md)
  - [Vox Media CoC](http://code-of-conduct.voxmedia.com/?_ga=1.62865454.308680892.1455143920)
  
**Note - this document should live in the root of your public GitHub.com repo.**

#### iii. Contributing file

It is a good practice to include information about how others can contribute to your project somewhere in your repository.
This is typically done as a separate file in a repo called `CONTRIBUTING.md`.
Here are some examples of this file:
- [Altair](https://github.com/altair-viz/altair/blob/master/CONTRIBUTING.md)
- [dplyr](https://github.com/tidyverse/dplyr/blob/master/.github/CONTRIBUTING.md)
- [Atom editor](https://github.com/atom/atom/blob/master/CONTRIBUTING.md) (very comprehensive)

If you're interested in this, [here's a quick guide](https://help.github.com/en/github/building-a-strong-community/setting-guidelines-for-repository-contributors) to creating this file from GitHub, but in the meantime, you can use the following snippet as a template:

> We welcome all contributions to this project! If you notice a bug, or have a feature request, please open up an issue [here](). If you'd like to contribute a feature or bug fix, you can fork our repo and submit a pull request. We will review pull requests within 7 days. All contributors must abide by our [code of conduct]().

**Note - this document should live in the root of your public GitHub.com repo.**

#### iv. License file

You may have noticed when you create a new repo on GitHub, you're asked to set a license for your project. 
If you do not currently have a preference, we recommend you use the [MIT license](https://choosealicense.com/licenses/mit/) for the project code and a [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0) license](https://creativecommons.org/licenses/by-nc-nd/4.0/) for the project report
You will learn more about licenses in the Workflows and Collaborative Software Development courses later in the program.
If you're curious, [here's a primer](http://swcarpentry.github.io/git-novice/11-licensing/index.html) from Software Carpentry and [a more detailed guide](https://doi.org/10.1371/journal.pcbi.1002598) to licenses.

**Note - this document should live in the root of your public GitHub.com repo.**

## 2. Project proposal
rubric={reasoning:7,mechanics:3}
#### Identify a data set, research question, & plan of action for analysis to answer that question

1. Choose a public data set from the web that you are interested in to carry out a small data analysis. You may also use any data set we have previously worked with in MDS. **Correctly cite where your data set is coming from in your proposal**. 
The data for the project should be publicly available, and clearly licensed to be shared and used openly on the internet.
2. With your data set, identify **one main predictive or inferential research question** that you will attempt to answer with analyses and visualizations (more on this below). Clearly state the research question and any natural sub-questions you need to address, and their type. 
3. Make a plan of how you will analyze the data (report an estimate and confidence intervals? hypothesis test? classification with a decision tree?). Choose something you already learned how to do in another MDS course. 
4. Discuss at least one exploratory data analysis (EDA) table and one exploratory data analysis figure you will create that makes sense for your research question, the data that you have, and the analysis you plan to do.
5. Suggest how you would share the results of your analysis as one or more tables and/or figures.

Your proposal will be written in the `README.md` file. You should include there:
- the project title 
- the list of contributors/authors 
- the project proposal (view from 10,000 feet) with your research question and describing points 1 - 5 listed above.
- the names of the licenses contained in LICENSE.md

**Note - this document should live in the root of your public GitHub.com repo.**

**Note - Remember, if you have a predictive research question, it is essential that you separate your dataset before you do any analysis. To be clear, you should NOT do any analysis - including preliminary EDA - on your test data.**

#### Data set sources
You can find some dataset sources in the [JupyterBook of this course.](https://pages.github.ubc.ca/MDS-2022-23/DSCI_522_dsci-workflows_students/materials/appendices/datasets.html)

*Hint: we suggest you avoid using data sets where authentication is needed to access (e.g., Kaggle) as this adds another layer of complexity when making these projects reproducible.*

**Note - the proposal should be written in the `README.md` file in the root of your public GitHub.com repo.**

## 3. A script that downloads and saves the data
rubric={accuracy:3,mechanics:11}

To prove to us that you can get the data into R or Python, write a script that takes a URL and a local file path as command line arguments which downloads and writes the file to your laptop. Use the {[docopt](https://github.com/docopt/docopt.R)} R or [`docopt`](https://github.com/docopt/docopt) Python package to create the command line argument functionality. 
If it is possible, the script should download the data to your `data/raw` folder. 

**Note - this script should live in an appropriately named sub-directory of your public GitHub.com repo.**

## 4. Exploratory data analysis in a literate code document
rubric={mechanics:13, viz:5, writing:4}

1. Choose a format to submit your exploratory data analysis, either an Rmd file or a Jupyter notebook. The name of the file should be meaningful and in relation to the project (not `analysis.ipynb` or `analysis.Rmd`)
2. This literate document should serve as a pre-cursor to the scripts you will eventually create. Feel free to experiment with different analyses and visualizations in this document. 
Data scientists often use a sandbox to play around in, before final scripts are created for automation. Similarly, it is valuable to try out a few different plots before finally settling on one or two for the final report. To get started, follow the EDA checklist in chapter 4 of [the Art of Data Science](https://leanpub.com/artofdatascience).
The literate document should include title, summary, an introduction briefly describing the dataset and references. You can divide the rest of the sections according to your criteria. The methods you use for the analysis should be mentioned.
3. Create at least **two plots** and **one table**. Add [figure captions properly](https://clauswilke.com/dataviz/figure-titles-captions.html) for the table and for the plot.
4. Add to the README an Usage section explaining how to run your data anaysis so far (download the script and render the literate code document) and the dependencies requiered.

**Note - the EDA should be done in a literate code document (e.g., `.Rmd` or `.ipynb` file). If you choose `.Rmd`, also please include a rendered document that we can easily read on GitHub (e.g., `.md` or `.pdf`). These documents should live in a subdirectory, such as `src` or make one called `eda`. You should point to this file in the README of your public GitHub.com repo.**

## 5. Expectations
rubric={mechanics:18}

- After the repository is set-up, each group member should create a feature branch with a meaningful name, and send pull-requests of their work to the repo. The other team mates should review, critique (if necessary) and finally accept their team mates pull request.
- You should be committing to git and pushing to GitHub.com every time you work on this project.
- git commit messages should be meaningful. These will be marked. It's OK if one or two are less meaningful, but most should be.
- Use GitHub issues to communicate to their team mate (as opposed to email or Slack)
- Your question, analysis and visualization should make sense. It doesn't have to be complicated.
- You should use proper grammar and full sentences in your README. Point form may occur, but should be less than 10% of your written documents.
- You **must** include the URL of your public project's repository in your milestone 1 submission, so we know where to find it.
- Just before you submit the milestone 1, create a release on your project repository on GitHub and name it 0.0.1. Include the URL to this release in your milestone 1 submission on Canvas, so we can easily jump to the state of your repository at the time of submission for grading puroposes, while you continue to work on your project for the next milestone.
