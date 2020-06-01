# Milestone 4 - Building a reproducible and fully automated data analysis pipeline
rubric={mechanics:25,accuracy:30,quality:20,reasoning:5,writing:5,viz:5}

#### Goal

Here you will use Docker to make your project reproducible on any machine that has Docker installed, add a Makefile dependency diagram to your README, and do a final round of iteration on all aspects of your project (code, automation, writing, data visualizations, report) to perfect it for final submission. 

#### Submission Instructions:

- Be sure to follow the [general lab instructions](https://ubc-mds.github.io/resources_pages/general_lab_instructions/) that are relevant, while also following the specific instructions described in the [expectations](#expectations) section below.

- **NEW** Some of you have chosen datasets that take ages to download and to perform analyses that take significant amount of computation resources and time. In your `README`, please **clearly** document that this is the case along with estimated completion times (on your machines is fine). This is so that the TAs are not stuck running these analyses for indeterminate amounts of time. 

## Dependency diagram of the Makefile
rubric={mechanics:10}

Create a dependency diagram of the Makefile using [`makefile2graph`](https://github.com/lindenb/makefile2graph) and include the image in the `README.md` file in the root of your project.

## Make your project reproducible (to the max) with Docker

Wrap your project up in a nice fancy Docker container. To do this, you should:
  - Write your own Dockerfile (this should include all the software and libraries/packages needed to run your analysis pipeline, but not this project itself - i.e., do not `git clone` your project repo inside your Dockerfile). This Dockerfile should live in the root of your project repository.
  - use Docker Hub Automated Build to build your Docker image from your Dockerfile
  - Do NOT include any of your data or code in the docker images!
  - include instructions in the project `README` on how to use your project with and without Docker. I envision that your instructions for using it with Docker should go something like this:

  > To run this analysis using Docker, clone/download this repository, use the command line to navigate to the root of this project on your computer, and then type the following (filling in PATH_ON_YOUR_COMPUTER with the absolute path to the root of this project on your computer).   

  >  ```
  >  docker run --rm -v PATH_ON_YOUR_COMPUTER:/home/data_analysis_eg ttimbers/data_analysis_pipeline_eg make -C '/home/data_analysis_eg' all
  >  ```

  > To clean up the analysis type:

  > ```
  > docker run --rm -v PATH_ON_YOUR_COMPUTER:/home/data_analysis_eg ttimbers/data_analysis_pipeline_eg make -C '/home/data_analysis_eg' clean
  > ```

## Expectations
  - You should be committing to git every time you work on this project. Thus, by the time you finish your final project, we expect to see 20+ commits in your git log. Make your commit messages meaningful!
  - This is an extension of Milestones 1, 2 and 3, so keep working in the public repo you set up for that. You do however, still need to resubmit the URL to your project in your `milestone4` repo's `README.md` file so we can easily find it when we're marking.
  - Create another release for your project repo (with an appropriate name) and submit that URL in your `milestone4` repo's `README.md` file so we know where to find it.
  - You should still have a well organized lab repo/directory structure.
  - The Dockerfile must be well documented. This means comments throughout, readable code and a brief summary at the top of each file that answers who wrote it, when it was written and what it does.
  - Your question, analysis and visualization should still make sense. Again, it doesn't have to be complicated, but you should tell a story and have a narrative. Specifically, this should come through in your README and final report file.
  - You should use proper grammar and full sentences in your README and report. Point form may occur, but should be less than 10% of your written documents.
