# DSCI 522: Data Science Workflows

Student and assignment materials for UBC MDS's DSCI 522: Data Science Workflows course.

The syllabus and every assignment are on the course website:
<https://ubc-mds.github.io/DSCI_522_dsci-workflows_students/>

The course notes are in the textbook,
[Reproducible and Trustworthy Workflows for Data Science](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/).

## Building the site

The site is a Quarto website: `index.qmd` is the syllabus,
and `assignments/` holds one page per assignment.
`slides/` holds the Section 001 lecture and lab slides (the "Section 1 Slides" tab):
each `lec_NN.qmd` / `lab_NN.qmd` page embeds a deck from `slides/slides/`,
and the header comment in `_quarto.yml` explains how to release one.
GitHub Actions renders it and publishes it to GitHub Pages on every push to `main`.
To preview it locally, run `make preview`; `make help` lists the other targets.

## License

Software licensed under the [MIT License](https://spdx.org/licenses/MIT.html),
non-software content licensed under the
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) License](https://creativecommons.org/licenses/by-nc-sa/4.0/).
See the [license file](LICENSE.md) for more information.