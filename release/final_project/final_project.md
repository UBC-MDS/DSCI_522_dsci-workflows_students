# Milestone 3 - Building a reproducible and fully automated data analysis pipeline
rubric={mechanics:5,accuracy:5,quality:3,reasoning:1,writing:1,viz:1}

#### Goal

Here you will agree upon a code of conduct document for your group (and any future open source contributions you might receive) and add it to your project repository. You will also use Docker to make your project reproducible on any machine (that has Docker installed).

#### Submission Instructions:
rubric={mechanics:2}

- Be sure to follow the [general lab instructions](https://ubc-mds.github.io/resources_pages/general_lab_instructions/) that are relevant, while also following the specific instructions described in the [expectations](#expectations) section below.


## Dependency diagram of the Makefile (optional)
rubric={mechanics:1}

Create a dependency diagram of the Makefile using [`makefile2graph`](https://github.com/lindenb/makefile2graph) and include the image in the `README.md` file in the root of your project.

Make this dependency graph build as part of your automated analysis.


## Add a code of conduct document to your repository

*First, apologies, I should have had this requirement as part of the proposal. Hopefully this is better late than never. We will include this as a requirement for all future group projects in MDS.*

Decide and agree upon a code of conduct for contributing to your project. Document this in a file called CONDUCT.md file which should live in each of the project's root directory (this can be identical for both projects). Examples of such a file is (remember to provide attribution if you use any of these as a basis for your own!) the [tidytext code of conduct](https://github.com/juliasilge/tidytext/blob/master/CONDUCT.md)


## Make your project reproducible (to the max) with Docker

Wrap your project up in a nice fancy Docker container. To do this, you should:
  - Write your own Dockerfile (this should include all the software and libraries/packages needed to run your analysis pipeline, but not this project itself)
  - use Docker Hub Automated Build to build your Docker image from your Dockerfile
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
  - This is an extension of Milestone 2, so keep working in the public repo you set up for that. You do however, still need to resubmit the URL to your project in your `final_project` repo's `README.md` file so we can easily find it when we're marking.
  - Create another release for your project repo (with an appropriate name) and submit that URL in your `final_project` repo's `README.md` file so we know where to find it.
  - You should still have a well organized lab repo/directory structure.
  - The Dockerfile must be well documented. This means comments throughout, readable code and a brief summary at the top of each file that answers who wrote it, when it was written and what it does.
  - Your question, analysis and visualization should still make sense. Again, it doesn't have to be complicated, but you should tell a story and have a narrative. Specifically, this should come through in your README and final report file.
  - You should use proper grammar and full sentences in your README and report. Point form may occur, but should
  be less than 10% of your written documents.
