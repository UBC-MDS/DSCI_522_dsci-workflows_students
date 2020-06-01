# Milestone 3 - Building an automated data analysis pipeline
rubric={mechanics:5,accuracy:3,quality:3,reasoning:1,writing:1,viz:1}

#### Goal

Here you will take the data analysis scripts that you built previously and use the build/automation tool Make to create a fully automated data analysis pipeline. Additionally, you will review and address feedback received on your project from the TAs and your peers (this will happen in the lab session) to iterate over it and make it better.

#### Submission Instructions:
<!-- rubric={mechanics:2} -->

- Be sure to follow the [general lab instructions](https://ubc-mds.github.io/resources_pages/general_lab_instructions/) that are relevant, while also following the specific instructions described in the [expectations](#expectations) section below.


## Automating the data-analysis pipeline using Make

Write a sixth script, a Makefile (literally called `Makefile`), to act as a driver script to rule them all. This script should run the others in sequence, hard coding in the appropriate arguments.
This script should:
  - live in the project's root directory and be named `Makefile`
  - be well documented (using the project README and comments inside the Makefile to explain what it does and how to use it)
  - have a `all:` target so that you can easily run the entire analysis from top to bottom by running `make all` at the command line
  - have a `clean:` target so that you can easily "undo" your analysis by running `make clean` at the command line

## Make your project even better

In lab you will separate from your partner and meet with individuals of 2 other groups. You will spend ~ 15 minutes introducing your project and walking them through your code/report. Then you will listen silently as you receive feedback from each person (5 min each). After the feedback session you will meet-up with your partner and discuss the feedback you each received and decide how you might move forward improving your project. You should open an issue or two to document the feedback you plan to address. Close that issue once you have addressed it.

## Expectations
  - You should be committing to git every time you work on this project. Thus, by the time you finish your final project, we expect to see 20+ commits in your git log. Make your commit messages meaningful!
  - This is an extension of Milestone 1, so keep working in the public repo you set up for that. You do however, still need to resubmit the URL to your project in your `milestone2` repo's `README.md` file so we can easily find it when we're marking.
  - Create another release for your project repo (with an appropriate name) and submit that URL in your `milestone2` repo's `README.md` file so we know where to find it.
  - You should still have a well organized lab repo/directory structure.
  - The Makefile must be well documented. This means comments throughout, readable code and a brief summary at the top of each file that answers who wrote it, when it was written and what it does.
  - Your question, analysis and visualization should still make sense. Again, it doesn't have to be complicated, but you should tell a story and have a narrative. Specifically, this should come through in your README and Rmd file.
  - You should use proper grammar and full sentences in your README and report. Point form may occur, but should
  be less than 10% of your written documents.
