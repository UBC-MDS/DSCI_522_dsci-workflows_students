# DSCI 522 - LAB 1
## Mathew Fournier / 27-SEP-2016


# EXERCISE 1
## Data Analysis Projects (3 Items)

* [Million Mutation Projects](https://github.com/ttimbers/Million-Mutation-Project-dye-filling-SKAT)
  * This repo contains the data and code to accompany the analysis of Million Mutation Project strains dye-filling phenotypes reported in *Timbers et al., bioRxiv, 2015*.  This includes a number of R scripts, as well as helper scripts (perl, bash, make) and a docker container.  The associated paper is not included --data and code only.

* [RdRp 454 amplicons Jericho and SOG](https://github.com/jooolia/RdRp_454_amplicons_Jericho_and_SOG)
  * this repo contains the code used to analyze pyrosequencing data and generate figures for the manuscript *High termporal and spatial diversity in marine RNA viruses implies that they have an important role in mortality and structuring plankton communities*.  The source data is hosted in not included in the version control and is hosted [here](https://www.ncbi.nlm.nih.gov/bioproject/?term=PRJNA267690).

* [Pleistocene Aged Stone Artefacts from Jerimalia-East Timor]([https://github.com/benmarwick/Pleistocene-aged-stone-artefacts-from-Jerimalai--East-Timor])
  * Text, data, and code to accompany the analysis of stone artefacts reported in Marwck et al.  This contains all the data, code, and text associated with the publication. Marwick, B, C. Clarkson, S. O'Connor & S. Collins 2016 "Pleistocene-aged stone artefacts from Jerimalai, East Timor: Long term conservatism in early modern human technology in island Southeast Asia" Journal of Human Evolution.  The associated paper source is include, as well as instructions for obtaining the analysis code as an R package, and a docker container.

## Data Science Tools (3 Items)

* [d3 - data driven documents](https://github.com/d3)
  * The root directory for the source for the popular D3 visualization framework by M. Bostock.  This root is an aggregation of individually version controlled modules (d3 (core), d3-array, d3-force, d3-scale).  Each repository contains the source, build tools, API reference, and tests for each module functionality.

* [topojson](https://github.com/mbostock/topojson)
  * This repo contains an extension to the GeoJSON format that allows for topology-preserving shape simplifications, automatic map colouring, cartograms, and up to 80% reduction in size compared to GeoJSON equivalents.  Note:  These are common 'web' formats for use in interactive visualization on maps.  Source code, API reference, and tests are included.

* [ggplot2](https://github.com/hadley/ggplot2)
  * This repo contains the ggplot2 plotting system in R, based on the grammar of graphics.  It vastly improves the look and efficiency of the base graphics plotting in R and forms part of the tidyverse style of data analysis in R.

## Discussion

The data analysis projects generally at least separate out *data* from *scripts*.  They may also include a docker container (so that the environment can be more easily recreated) to simplify dependency issues by downstream users looking to recreate the analyses.  They also contain an overall controlling script, which can be a bash script in the case of RdRp or may be a more formal build tool (e.g. `make`) that processes the scripts, R files, etc. in the correct order to generate the final analyses.  They all include a `README.md` file explaining the project, the dependencies, the build process, the paper they are associated with, and other relevant links.

The data tool projects generally contain a `src` directory (sometimes named `R`) containing the source files, and some form of `tests` directory containing the unit tests used as part of the software development.  The root directory typically contains a `README.md` explaining the project and the API usage, the license that the API is using, file or file(s) indicating the build dependencies (and versions), and build tool instructions.

### Similarities

* They both contain `README.md` explaining the general overview, and linking to metadata such as results or API references
* They both contain some form of `build` tool/script and dependency list
* They generally both contain a license that indicates what use terms
* They both try to use a directory structure to separate out different components of the project (data, code, scripts, metadata)

### Differences

* The tools generally contain unit tests, while the projects are provided more on an `as-is` basis with generally no inclination of how rigorous a code review has been undertaken.  Only one of the projects listed as 'example' projects contained any form of unit testing.
* The code projects are generally more modularly structured following software design principles whereas the data projects appear to be a little haphazard/spaghetti code.  For example, the `scripts` directories of the data projects can be enormous and contain scripts in several languages with no indication of what is doing what.
  * I think this is telling for the difference between 'programmer' and 'researcher who also programs' in regards to the ultimate product.  The researcher is more interested in the results, and is likely less savvy with software design principles.  That is, the data science tools are expected to be used by other people, where the audience for reproducing the data is likely significantly smaller and more willing to deal with a messy build/use process.
