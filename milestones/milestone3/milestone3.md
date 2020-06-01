# Milestone 3 - Building a reproducible and fully automated data analysis pipeline
rubric={mechanics:5,code:5,reasoning:1,writing:1,viz:1}

#### Goal

Here you will take the data analysis scripts that you built previously and use the tools
you have learned about in the lecture (make, packrat, virtualenv, docker, make) to create a reproducible and fully automated data analysis pipeline.

#### Submission Instructions:
<!-- rubric={mechanics:2} -->

- Be sure to follow the [general lab instructions](https://ubc-mds.github.io/resources_pages/general_lab_instructions/) that are relevant, while also following the specific instructions described in the [expectations](#expectations) section below.


## Automating the data-analysis pipeline using Make

Write a fifth script, a Makefile, to act as a driver script to rule them all,
*i.e.* to run the others in sequence, hard coding in the appropriate arguments.
This script should:
  - live in the project's root directory and be named `Makefile`
  - be well documented (explaining what it does and how to use it)
  - have a `clean:` target so that you can easily "undo" your analysis through
  running `make clean` at the command line

## Dependency diagram of the Makefile (optional)
rubric={mechanics:1}

Create a dependency diagram of the Makefile using [`makefile2graph`](https://github.com/lindenb/makefile2graph) and include the image in the `README.md` file in the root of your project.

Make this dependency graph build as part of your automated analysis.

## Make it reproducible to the max

1. If you used R for any code, then use Packrat to manage the package version. If you
used Python, use conda (or virtualenv) to do that. If you used both, use both.

2. Wrap it up in a nice fancy Docker container. To do this, you should:
  - Write your own Dockerfile
  - create your own Docker image that you host on Docker Hub
  - use Docker Hub Automated Build to build your Docker image from your Dockerfile

## Expectations
  - You should be committing to git every time you work on this project. Thus, by the time you finish your final project, we expect to see 20+ commits in your git log. Make your commit messages meaningful!
  - This is an extension of Milestone 1 & 2, so keep working in the public repo you set up for that. You do however, still need to resubmit the URL to your project in your `milestone3` repo's `README.md` file so we can easily find it when we're marking.
  - Create a release on your project repo named v3.0 and submit that URL in your `milestone3` repo's `README.md` file so we know where to find it.
  - You should still have a well organized lab repo/directory structure.
  - In the main `README.md` file for this project you should explain the project in a short summary (view from 10,000 feet) and also explain how to run your data analysis. This should be about how to use Make to run your analysis instead of what to put into each script. A dependency diagram of the Makefile using [`makefile2graph`](https://github.com/lindenb/makefile2graph) could be nice here.
  - Each script (including the Docker and Makefile) must be well documented. This means comments throughout, readable code and a brief summary at the top of each file that answers who wrote it, when it was written and what it does.
  - Your question, analysis and visualization should still make sense. Again, it doesn't have to be complicated, but you should tell a story and have a narrative. Specifically, this should come through in your README and Rmd file.
  - You should use proper grammar and full sentences in your README and report. Point form may occur, but should
  be less than 10% of your written documents.
