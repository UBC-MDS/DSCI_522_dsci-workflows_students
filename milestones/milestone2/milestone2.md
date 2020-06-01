# Milestone 2 - Building a data analysis pipeline
rubric={mechanics:5,code:5,reasoning:1,writing:1,viz:1}

#### Goal

Here you will build the data analysis pipeline that you will use for your final project.
It will consist of multiple scripts which work to ingest, summarize and visualize some
data, as well as report something interesting about the data that you learned by doing this
analysis. In the next milestone (due at the end of the course), you will make this pipeline
reproducible, as well as automate it. These things are not yet required for this milestone however.

#### Submission Instructions:

- Be sure to follow the [general lab instructions](https://ubc-mds.github.io/resources_pages/general_lab_instructions/) that are relevant, while also following the specific instructions described in the [expectations](#expectations) section below.

## Writing an analysis that uses multiple scripts

- Write the following four files (3 R or Python scripts and an R Markdown file) to carry out a small data analysis.
- The output of the first script must be the input of the second, and so on.
- Something like this:
    1. First script that downloads some data and save it locally. This should take
    two arguments:
      - a URL pointing to the data
      - a path/filename where to write the file to and what to call it (*e.g.,* `data/data.csv`)
    2. Second script that reads the data from the first script, performs some analysis (*e.g.,* creates a summary table) and writes these numerical data to file in CSV or TSV format. This should take two arguments:
      - a path/filename pointing to the data
      - a path/filename where to write the file to and what to call it (*e.g.,* `results/summarized_data.csv`)
    3. Third script that reads the output of the second script, generate some figures and save them to files. This should take two arguments:
      - a path/filename pointing to the data
      - a path/filename prefix where to write the figure to and what to call it (*e.g.,* `results/this_analysis`)
    4. Fourth script: an `.Rmd` actually, that presents original data, the statistical summaries, and/or the figures in a little report.

*note - feel free to re-use R or Python code from previous assignments in this class or others*

## Expectations
- You should be committing to git every time you work on this project. Thus, we expect to
see 10+ commits in your git log.
- git commit messages should be meaningful. These will be marked. It's OK if one or two are
less meaningful, but most should be.
- Because we will eventually be using some fancy tooling (e.g., automated builds on Dockerhub) with this project
you will need to put your scripts in a public repo on github.com. You **must** include the URL to your project in your `milestone2` repo's `README.md` file so we know where to find it.
- Create a release on your project repo named v2.0 and submit that URL in your `milestone2` repo's `README.md` file so we know where to find it.
- You should have a well organized lab repo/directory structure, where:
  - all code files (`.R`, `.py`, `.Rmd`, `.ipynb`) live in the `src` directory,
  except for the driver scripts (script which calls your analysis scripts).
  - all rendered documents live in the `results` directory
  - all data used belong in the `data` directory
  - Make your figure names MORE descriptive than the examples I provide above
- In the main `README.md` file for this project you should explain the project in a short summary (view from 10,000 feet) and also explain how to run your data analysis (which order scripts are run in, what expected inputs are). Your explanation could include a flow chart/dependecy diagram.
- Each script must be well documented. This means comments throughout, readable code and a brief summary at
the top of each file that answers who wrote it, when it was written and what it does.
- Your question, analysis and visualization should make sense. It doesn't have to be complicated, but you should tell a story and have a narrative. Specifically, this should come through in your README and Rmd file.
- You should use proper grammar and full sentences in your README and report. Point form may occur, but should
be less than 10% of your written documents.
