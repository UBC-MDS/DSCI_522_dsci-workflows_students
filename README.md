# DSCI 522: Data Science Workflows

## Introduction

Data-rich projects can quickly grow out-of-hand
and become irreproducible in the absence of deliberate effort at organization,
tool choice, and process.
This course will teach basic principles of sound data scientific workflows
and will develop skills implementing them
in appropriate state-of-the-art systems and languages (e.g., Python and R).

**Course syllabus**:
This page

**Course notes/book**:
[https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science)

**Slack Channel**: [https://ubc-mds.slack.com/messages/522_dsci-workflows](https://ubc-mds.slack.com/messages/522_dsci-workflows)

## Learning Outcomes

By the end of the course, students are expected to be able to:

- map a data analysis question to appropriate analysis
- use a Git/GitHub to collaboratively work on a data analysis project
- manage project software and environment dependencies
  using virtual environments and containers
- write scripts and analysis pipelines for non-interactive data analysis
- run literate coding documents non-interactively
- automate data science workflows

## Teaching Team

At your service!

|      Position      |          Name          |      Slack Handle      |
| :----------------: | :--------------------: | :--------------------: |
|     Instructor     |      Daniel Chen       | `@Daniel (Instructor)` |
|     Instructor     |    Sky Kehan Sheng     |         `@Sky`         |
| Teaching Assistant |                        |                        |
| Teaching Assistant |                        |                        |
| Teaching Assistant |                        |                        |
| Teaching Assistant |                        |                        |
| Teaching Assistant |                        |                        |
| Teaching Assistant |                        |                        |
| Teaching Assistant |                        |                        |
| Teaching Assistant |                        |                        |

## Deliverables

This is a **project-based course**.
You will work in randomly assigned groups of three (or four, if needed)
for the project milestones.
There are also individual weekly assignments that act as stepping stones
to the project milestones.
Finally, because collaboration is so important in data science,
we will be using a team work multiplier to adjust individual grades.
A combination of peer evaluation
and GitHub history will be used to evaluate this.

:::{.callout-warning}

## Lab attendance is mandatory

Students are expected to attend 100% of their scheduled lab hours and attendance will be taken at the beginning of each lab session.
Students must make formal requests for academic concession in the event that they cannot attend a lab session by filling out this [academic concession form](https://github.com/UBC-MDS/UBC-MDS.github.io/blob/master/img/Template%20-%20In-Term%20Academic%20Concessions%20Self%20Declaration.pdf?raw=1) and sending it to the course instructor.
Applying for academic concession does not promise the granting of academic concession.
Each application will be evaluated in the context of UBC’s Academic concession policy.
Students missing more than **20% of the total scheduled lab hours** for a course without having received an academic concession will receive a possible maximum course grade of 50% and an “F” standing for the course on the transcript.
For all other policies, please see the general MDS policies.

:::

| Assessment                                                                                   | Weight                    | Deadline                |
| -------------------------------------------------------------------------------------------- | ------------------------- | ----------------------- |
| iClicker                                                                                     | 2%                        | Every lecture           |
| Pre-lecture quizzes                                                                          | 2%                        | Every lecture           |
| Individual assignment 1 - version control workflows                                          | 2%                        | 2025-11-22 18:00 PT     |
| Milestone 1 - Setup project on GitHub, draft of analysis in a notebook & virtual environment | 20%                       | 2025-11-22 18:00 PT     |
| Individual assignment 2 - container workflows                                                | 2%                        | 2025-11-29 18:00 PT     |
| Milestone 2 - Modularize code into functions, test code & container                          | 20%                       | 2025-11-29 18:00 PT     |
| Individual assignment 3 - Quarto practice                                                    | 2%                        | 2025-12-07 11:59 PT     |
| Milestone 3 - Move code into scripts and polish report                                       | 20%                       | 2025-12-07 11:59 PT     |
| Peer Review                                                                                  | 5%                        | 2025-12-11 18:00 PT     |
| Individual assignment 4 - Pipeline practice                                                  | 2%                        | 2025-12-13 18:00 PT     |
| Milestone 4 - Data analysis pipeline and revise project in response to feedback              | 20%                       | 2025-12-13 18:00 PT     |
| Team work reflection                                                                         | 3%                        | 2025-12-14 18:00 PT\*\* |
| Team work multiplier                                                                         | final grade \* multiplier | NA                      |

## Schedule

<table class="striped">
  <tr>
    <th>Lecture</th>
    <th>Topic</th>
    <th>Required Notes/Readings</th>
    <th>Additional Resources</th>
    <th></th>
  </tr>
  <tr>
    <td>1</td>
    <td>Reproducibility & trustworthy workflows intro, git branches</td>
    <td>
      <ul>
        <li>[How do reproducible and trustworthy workflows impact data science?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/010-intro-to-ds-workflows.html)</li>
        <li>[Version control (for transparency and collaboration) II](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/050-version-control-2.html)</li>
        <li>[conda-lock](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/090-conda-lock.html)</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>
          Stating and Refining the Question from [The Art of Data Science](https://leanpub.com/artofdatascience)
        </li>
      </ul>
    </td>
    <td></td>
  </tr>
  <tr>
    <td>2</td>
    <td>Introduction to containerization</td>
    <td>
      <ul>
        <li>[Introduction to containerization](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/100-containerization-1.html)</li>
        <li>[Using and running containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/110-containerization-2.html)</li>
      </ul>
    </td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>3</td>
    <td>Customizing, versioning and sharing containers</td>
    <td>
      <ul>
        <li>[Customizing and building containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/120-containerization-3.html)
        </li>
      </ul>
    </td>
    <td>
      <ul>
        <li>[Ten simple rules for writing Dockerfiles for reproducible data science](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008316)
        </li>
      </ul>
    </td>
    <td></td>
  </tr>
  <tr>
    <td>4</td>
    <td>Data validation</td>
    <td>
      <ul>
        <li>
          [Data validation](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/130-data-validation.html)
        </li>
      </ul>
    </td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>5</td>
    <td>Scripts</td>
    <td>
      <ul>
        <li>
        [Non-interactive scripts](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/150-scripts.html)
        </li>
        </ul>
      </td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>6</td>
    <td>Advanced reproducible reports</td>
    <td>
      <ul>
        <li>
          [Reproducible reports](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/160-reproducible-reports.html)
        </li>
      </ul>
    </td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>7</td>
    <td>Data analysis pipelines</td>
    <td>
      <ul>
        <li>[Introduction to Data analysis pipelines](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/170-pipelines-scripts.html)</li>
        <li>[Data analysis pipelines with GNU Make](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/180-pipelines-make.html)</li>
      </ul>
    </td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>8</td>
    <td>Testing for data analysis</td>
    <td>
      <ul>
        <li>[Introduction to testing code for data science](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/140-intro-to-testing-code.html)</li>
        <li>[Python testing example](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/141-python-testing-example.html) or [R testing example](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/142-R-testing-example.html)</li>
        <li>[Observability of unit outputs in data science](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/147-testing-images.html)</li>
      </ul>
    </td>
    <td></td>
    <td></td>
  </tr>
</table>

## Textbooks

- [Reproducible and Trustworthy workflows for data science](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/README.html)
  by Tiffany Timbers et al
  (this is where our course notes are, plus additional gems)
- [Art of Data Science](https://leanpub.com/artofdatascience)
  by Roger Peng & Elizabeth Matsui
  (a companion guide for graduate students doing research projects
  in data science - highly recommended reading!)

## Class Schedule & office hours

See [calendar](https://ubc-mds.github.io/calendar/).

## Policies

- Please see the general and genAI use policies in [MDS policies](https://ubc-mds.github.io/policies/).
- Please review [General Lab Instructions](https://ubc-mds.github.io/resources_pages/general_lab_instructions/)
- Check the [MDS Rubrics](https://github.com/UBC-MDS/public/tree/master/rubric) for grading criteria.

## License

Software licensed under the [MIT License](https://spdx.org/licenses/MIT.html),
non-software content licensed under the
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) License](https://creativecommons.org/licenses/by-nc-sa/4.0/).
See the [license file](LICENSE.md) for more information.
