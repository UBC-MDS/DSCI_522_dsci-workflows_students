# Milestone 3 - Building an automated data analysis pipeline

### Overall project summary

In this course you will work in assigned teams of three or four (see group assignments in Canvas) to answer a statistical question using a publicly available data set that will allow you to answer that question. To answer this question, you will perform a complete data analysis, from data import to communication of results, while placing significant emphasis on reproducibility and transparency. To complete the analysis you will write 4-5 R and/or Python scripts, create a reproducible report (in Jupyter or R Markdown), as well as automate your data analysis workflow using GNU Make. Software and environment dependencies are to be made shippable and shareable via containerization with Docker.

An example final project can be seen here: [https://github.com/ttimbers/breast_cancer_predictor](https://github.com/ttimbers/breast_cancer_predictor)

An example project in milestone3 could be seen here: [https://github.com/ttimbers/breast_cancer_predictor/tree/v3.0](https://github.com/ttimbers/breast_cancer_predictor/tree/v3.0)
#### Goal

Here you will take the data analysis scripts that you built previously and use the build/automation tool Make to create a fully automated data analysis pipeline. 
Additionally, you will review and address feedback received on your project from the TAs and your peers (this will happen in the lab session) to iterate over it and make it better.

#### Submission Instructions:

- Be sure to follow the [general lab instructions](https://ubc-mds.github.io/resources_pages/general_lab_instructions/) that are relevant, while also following the specific instructions described in the [expectations](#expectations) section below.

 *Note - It is a good idea to improve your work based on any feedback you received from the TAs as soon as you get it.*

## Automating the data-analysis pipeline using Make
rubric={mechanics:20,accuracy:20,quality:17}   

Write another script, a Makefile (literally called `Makefile`), to act as a driver script to rule them all. This script should run the others in sequence, hard coding in the appropriate arguments.
This script should:
  - live in the project's root directory and be named `Makefile`
  - be well documented (using the project README and comments inside the Makefile to explain what it does and how to use it)
  - have a `all:` target so that you can easily run the entire analysis from top to bottom by running `make all` at the command line
  - have a `clean:` target so that you can easily "undo" your analysis by running `make clean` at the command line


## Expectations
rubric={mechanics:15}  
  - **Everyone should contribute equally to all aspects of the project (e.g., code, writing, project management). This should be evidenced by a roughly equal number of commits, pull request reviews and participation in communication via GitHub issues.** Thus, by the time you finish your final project, we expect to see 20+ commits in your `git log`. Make your commit messages meaningful!
  - Create another release for your project repo (0.2.0) and submit both the URL of the release and URL of the repository to Canvas.
  - You should still have a well organized lab repo/directory structure.
  - The Makefile must be well documented. This means comments throughout, readable code and a brief summary at the top of each file that answers who wrote it, when it was written and what it does.
  - Your question, analysis and visualization should still make sense. Again, it doesn't have to be complicated, but you should tell a story and have a narrative. Specifically, this should come through in your README and Rmd file.
  - You should use proper grammar and full sentences in your README and report. Point form may occur, but should
  be less than 10% of your written documents.
