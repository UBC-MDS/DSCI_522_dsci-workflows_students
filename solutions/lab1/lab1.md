## Lab 1 - Project organization and management

**Goal** - In this lab you will explore and reflect on how popular data science and data science tools projects are managed by seasoned developers. The goal is is to learn from the mistakes and wins of others, to make your project organization and management as effective as possible.

**Submission Instructions:**
<!-- rubric={mechanics:1} -->

- Exercise 1 should be submitted as a `.md` document (separate from the repo's main `README.md` file) within the lab/assignment repo. *How you create this `.md` document is up to you (you can use Atom, Jupyter, RStudio, or any other editor capable of exporting Markdown files).*

- For exercise 2, you should:
    - create a separate **public** Github repo on https://github.com/ and develop your script and documentation in there
    - this repo should contain the script and a `README.md`

- In the main `README.md` file in the lab/assignment repo, you must link to the `.md` file which contains exercises 1 as well as the repo containing your script for exercise 2.

### Exercise 1 - Identify public repositories in hosted version control for data analysis projects and data science tools
<!-- rubric={reasoning:4,writing:1} -->

- Search or browse hosted version control (*e.g.,* Github and/or Bitbucket) and identify 3 public repositories for data analysis projects and three public repositories for data science tools. You can choose from the list of repositories below, **or** you can find others **you are interested in**:

  - Data analysis project Github repositories:
    - [Pleistocene-aged stone artefacts from Jerimalai, East Timor: Long term conservatism in early modern human technology in island Southeast Asia](https://github.com/benmarwick/Pleistocene-aged-stone-artefacts-from-Jerimalai--East-Timor) by Ben Marwick *et al.*
    - [WorldBank GDP data sets and evaluation](https://github.com/bici-sancta/gdp_worldbank) by Bici Sancta
    - [High temporal and spatial diversity in marine RNA viruses implies that they have an important role in mortality and structuring plankton communities](https://github.com/jooolia/RdRp_454_amplicons_Jericho_and_SOG) by Julia Gustavsen *et al.*
    - [The Horse Transcriptome project](https://github.com/drtamermansour/horse_trans) by Tamer Mansour
    - [Historical horse population in Canada](https://github.com/ttimbers/equine_numbers_value_canada) by Tiffany Timbers

  - Data science tool Github repositories:
    - [`geoparser`](https://github.com/ropenscilabs/geoparser)
    - [`screed`](https://github.com/dib-lab/screed)
    - [`AutoQC`](https://github.com/BillMills/AutoQC)
    - [`rpanama`](https://github.com/dgrtwo/rpanama)
    - [`southafricastats`](https://github.com/juliasilge/southafricastats)
    - [`dplyr`](https://github.com/hadley/dplyr)
    - [`pandas`](https://github.com/pydata/pandas)
    - [`packrat`](https://github.com/rstudio/packrat)
    - [`conda`](https://github.com/conda/conda)
    - [`virtualenv`](https://github.com/pypa/virtualenv)
    - [Docker](https://github.com/docker/docker)

- As proof of your search and research, identify these repositories with their URLs and write a brief summary paragraph to describe each project (this can be very high level).

- In about three quarters (3/4) of a page, reflect on the following:
  - How are data **analysis project repositories** generally organized? What is the folder structure and what content is included in these folders
  - How are data science **tool repositories** generally organized? What is the folder structure and content is included in these folders?
  - What similarities do you observe between data analysis project and data science tool repositories?
  - What differences do you observe between data analysis project and data science tool repositories?

### Exercise 2 - Cookie cutter project template generators
<!-- rubric={code:3,mechanics:2} -->

A cookie cutter project template generator is a tool which generates a project file and directory structure template so that you don't have to do this from scratch every time. They are great time savers, and also help remind you to create all the little bits, such as `README.md`'s and `LICENSE.md`'s that might otherwise get overlooked.

- Do a web search (*e.g.,* Google, Github) to find 2 cookie cutter project template generators that could work for a data analysis project
- Write a script using the shell, python or R which will create your own cookie cutter project template generator
- You should be using version control as you develop this script:
  - A new, public Github repository should be created (also mentioned in submission instructions) for this on [github.com](https://github.com/).
  - This repository should contain the script and a `README.md` file.
- Don't forget to document it! The script **and** the `README.md` file should clearly document:
  - what the script does
  - if has command line arguments (or none)
  - who wrote it
  - when it was created

Note: Take idea of the format from your sample project you found above
