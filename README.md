# DSCI 522 Section 001 Lab Slides

Author: Sky Sheng

This repository contains the lab slides for DSCI 522, reproducible and trustworthy data science workflow, Section 001, for 2026W1. The instructor for this section is Sky Sheng.

## View Slides Online

The slides are hosted on GitHub Pages:

- [http://www.skysheng.io/DSCI_522-001-slides/](http://www.skysheng.io/DSCI_522-001-slides/)

## Local Development

The site is a [Quarto](https://quarto.org/docs/download/) website in `website/`. Slide decks are in `website/slides/`, and each lecture or lab has a page (`lec_NN.qmd`, `lab_NN.qmd`) that embeds its deck. To preview locally:

```bash
cd website
quarto preview
```

Pushing to `main` renders `website/` and publishes it to GitHub Pages with the GitHub Actions workflow in `.github/workflows/publish_website.yml`. The header comment in `website/_quarto.yml` explains how to release a lecture.

## License

This work is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.