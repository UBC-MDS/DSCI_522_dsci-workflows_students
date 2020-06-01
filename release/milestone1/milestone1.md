# Milestone 1 - A data analysis project with multiple scripts and a final report
rubric={mechanics:5,accuracy:5,quality:5,reasoning:5,writing:1,viz:3}

#### Goal

Here you will build the scripts and write the final report for your data analysis project. The scripts you write will work to load, clean, analyze, visualize and summarize the data in the context of your question. The written report will provide a narrative for your project and present and discuss your findings. In the next milestone, you will turn this collection of scripts and report into an automated data analysis pipeline. At the final project stage you will use Docker to make your project completely reproducible.

#### Submission Instructions:

- Be sure to follow the [general lab instructions](https://ubc-mds.github.io/resources_pages/general_lab_instructions/) that are relevant, while also following the specific instructions described in the [expectations](#expectations) section below.

## Writing an analysis that uses multiple scripts

- Write the following five files (4 R or Python scripts and an R Markdown or Jupyter notebook report) to carry out your planned data analysis. If you would like to have more than 4 scripts, by all means, go ahead. Three scripts are the minimum however.
- The output of the first script must be the input of the second, and so on.
- Something like this:
    1. First script that reads in some data and saves a clean/tidy version of it. This should take
    two arguments:
      - the path to the input file (a URL or a relative local path, such as `data/file.csv`)
      - a path/filename where to write the file to and what to call it (*e.g.,* `data/cleaned_data.csv`)
      - note - choose more descriptive filenames than the ones used here for illustrative purposes
    2. Second script that reads the data from the first script and creates an exploratory visualization that is useful to help the reader/consumer understand that dataset. This should take two arguments:
      - a path/filename pointing to the data
      - a path/filename prefix where to write the figure to and what to call it (*e.g.,* `results/this_eda.png`)
    2. Third script that reads the data from the first script, performs some statistical or machine learning analysis (*e.g.,* creates a summary table) and writes these numerical data to file in CSV or TSV format. This should take two arguments:
      - a path/filename pointing to the data
      - a path/filename where to write the file to and what to call it (*e.g.,* `results/summarized_data.csv`)
    3. Fourth script that reads the output of the first and/or third script, generate some summary/final result table(s) and/or figure(s) and save them to files. This should take two arguments:
      - a path/filename pointing to the data
      - a path/filename prefix where to write the figure(s)/table(s) to and what to call it (*e.g.,* `results/this_analysis`)
    4. Fourth script: an `.Rmd` or `.ipynb` actually, that presents original data, the statistical summaries, and/or the figures in a little report. There should be a written narrative in this document that introduces and justifies your question, introduces the data set, presents the findings/results, and interprets the findings/results in context of the question. Some critique of the analysis is also expected (limitations, assumptions, etc) and a statement of future directions (what would you do next if you had more time to work on this). The report is expected to be 1-2 written pages (excluding figures, tables and references). You are expected to have a reference section and cite 2-3 external sources (data source can be one of these citations).

*note - feel free to re-use R or Python code from previous assignments in this class or others*

## Expectations

### Version control and submission expectations
- You should be committing to git every time you work on this project. Thus, we expect to see 10+ commits in your git log by the time you submit this milestone.
- git commit messages should be meaningful. These will be marked. It's OK if one or two are less meaningful, but most should be.
- Each team member is expected to work in their personal fork of the repository, and then frequently send pull-requests of their work to the upstream repo (the one they forked). The other teammates should review, critique (if necessary) and finally accept their teammate's pull request.
- Use GitHub issues to communicate to their team mate (as opposed to email or Slack)
- You **must** include the URL of your public project's repo in the `README.md` file of your `milestone1`'s repo,  so we know where to find it.
- Create a release on your project repo named v2.0 (or whatever is appropriate for your versioning scheme) and submit that URL in your `milestone1` repo's `README.md` file so we know where to find it.

### Project organization and documentation expectations
- In the main `README.md` file for this project you should explain the project in a short summary (view from 10,000 feet) and also explain how to run your data analysis (which order scripts are run in, what expected inputs are). Your explanation could include a flow chart/dependecy diagram. This should be an evolution of what was submitted at the proposal stage.
- Each script must be well documented. This means comments throughout, readable code and a brief summary at the top of each file that answers who wrote it, when it was written and what it does.
- Your question, analysis and visualization should make sense. It doesn't have to be complicated, but you should tell a story and have a narrative. Specifically, this should come through in your README and final report file.
- You should use proper grammar and full sentences in your README and report. Point form may occur, but should be less than 10% of your written documents.
