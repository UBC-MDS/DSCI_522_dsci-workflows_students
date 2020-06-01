# DSCI 522
## Lecture 4 - Data Analysis pipelines
### 2017-11-27

# Learning Objectives
## By the end of the lecture, students should be able to:
By the end of the lecture, students are expected to be able to:

- Create a data analysis pipeline using R, Python and the Unix shell to run multiple scripts
- Hand Draw manual dependency diagrams

## Building a Data Analysis pipeline using a Shell script tutorial
adapted from [Software Carpentry](http://software-carpentry.org/)

To illustrate how to make a data analysis pipeline using a shell script to drive other scripts, we will work through
an example together. Here are some set-up instructions so that we can do this together:


### Set-up instructions

Clone [data_analysis_pipeline_eg](https://github.ubc.ca/timberst/data_analysis_pipeline_eg)

Change into the `data_analysis_pipeline_eg` directory:

### Let's do some analysis!

Suppose we have a script, `wordcount.py`, that reads in a text file,
counts the words in this text file, and outputs a data file:

~~~
$ python wordcount.py books/isles.txt isles.dat
~~~

If we view the first 5 rows of the data file using `head`,

~~~
$ head -5 isles.dat
~~~

we can see that the file consists of one row per word. Each row shows the word itself,
the number of occurrences of that word, and the number of occurrences as a percentage of
the total number of words in the text file.

~~~
the 3822 6.7371760973
of 2460 4.33632998414
and 1723 3.03719372466
to 1479 2.60708619778
a 1308 2.30565838181
~~~

 As another example:

~~~
$ python wordcount.py books/abyss.txt abyss.dat
$ head -5 abyss.dat
~~~

~~~
the 4044 6.35449402891
and 2807 4.41074795726
of 1907 2.99654305468
a 1594 2.50471401634
to 1515 2.38057825267
~~~

## Let's get started!

Suppose we have a script, `wordcount.py`, that reads in a text file,
counts the words in this text file, and outputs a data file:

~~~
$ python wordcount.py books/isles.txt isles.dat
~~~

If we view the first 5 rows of the data file using `head`,

~~~
$ head -5 isles.dat
~~~

we can see that the file consists of one row per word. Each row shows the word itself,
the number of occurrences of that word, and the number of occurrences as a percentage of
the total number of words in the text file.

~~~
the 3822 6.7371760973
of 2460 4.33632998414
and 1723 3.03719372466
to 1479 2.60708619778
a 1308 2.30565838181
~~~

 As another example:

~~~
$ python wordcount.py books/abyss.txt abyss.dat
$ head -5 abyss.dat
~~~

~~~
the 4044 6.35449402891
and 2807 4.41074795726
of 1907 2.99654305468
a 1594 2.50471401634
to 1515 2.38057825267
~~~

Suppose we also have a script, `plotcount.py`, that reads in a data
file and plots the 10 most frequently occurring words:

~~~
$ python plotcount.py isles.dat show
~~~

Close the window to exit the plot.

`plotcount.py` can also save the plot as an image (e.g. a PDF):

~~~
$ python plotcount.py isles.dat isles.pdf
~~~

Together these scripts implement a data analysis pipeline:

1. Read a data file.
2. Perform an analysis on this data file.
3. Write the analysis results to a new file.
4. Plot a graph of the analysis results.
5. Save the graph as an image, so we can put it in a paper.

To document how we'd like the analysis to be run, so we (and others) have a record and
can replicate it, we will build a shell script called `run_all.sh`:

```
# run_all.sh
# Tiffany Timbers, Nov 2017
#
# This driver script completes the textual analysis of
# 3 novels and creates figures on the 10 most frequently
# occuring words from each of the 3 novels. This script
# takes no arguments.
#
# Usage: bash run_all.sh

# perform wordcout on novels
python src/wordcount.py data/isles.txt results/isles.dat
python src/wordcount.py data/abyss.txt results/abyss.dat
python src/wordcount.py data/last.txt results/last.dat
python src/wordcount.py data/sierra.txt results/sierra.dat

# create plots
python src/plotcount.py results/isles.dat results/figures/isles.pdf
python src/plotcount.py results/abyss.dat results/figures/abyss.pdf
python src/plotcount.py results/last.dat results/figures/last.pdf
python src/plotcount.py results/sierra.dat results/figures/sierra.pdf

# make report
Rscript -e 'ezknitr::ezknit("src/count_report.Rmd", out_dir = "doc")'
```
