
# DSCI 522


## Lecture 2 - Scaling up: read-eval-print-loop (REPL) processes versus non-interactive scripts


### 2016-09-29

# Learning Objectives

## By the end of the lecture, students should be able to:

- Explain when it is optimal to work in a read-eval-print-loop (REPL) framework and when it is optimal to shift to using non-interactive scripts
- Be able to create simple scripts in Python and R that can take input and be run from the command line

## Read-eval-print-loop (REPL) framework (*i.e.,* interactive mode) versus Scripts

- Up until now, we have primarily been using R and Python in an Read-eval-print-loop (REPL) framework (*i.e.,* interactive mode)
- Read-eval-print-loop (REPL) framework (*i.e.,* interactive mode) is when we run our code in the console in R/Python, or in cells/chunks in the RStudio/Juptyer notebooks
- Python in an Read-eval-print-loop (REPL) framework (*i.e.,* interactive mode) is very useful for:
    - solving small problems
    - developing code that will be knit/weaved/etc to an analytic report
    - developing code that will be run as a script (i.e., in "batch" mode)

## Reminder - what is a script?

An R/Python script is simply a plain text file containing (almost) the same commands that you would enter into R/Python's console or in cells/chunks in the RStudio/Juptyer notebooks.

## Why write scripts?

- Efficiency!
- Automation!
- Reusable!
- Record of what you have done!

## Scripts in R

Let's start with a small, simple example to demonstrate how we write and run scripts in R (it is very similar in Python and we will get to this later in the lesson).

Our script will be called `print_mean_hp.R`, and it will calculate the mean horsepower of the cars from the built-in R data frame `mtcars`. 

We will develop this script inside RStudio, make sure it works, and then run it from the command line/terminal/Git bash.

##### Our first R script:

```
# print_mean_hp.R
# Tiffany Timbers, Oct 2016
#
# This script calculates the mean horsepower of the cars from the built-in 
# R data frame `mtcars`. This script takes no arguments.
#
# Usage: Rscript print_mean_hp.R

mean_hp <- mean(mtcars$hp)
print(mean_hp)
```

##### Running our first R script

To run our R script, we need to open the command line/terminal/Git bash, and either navigate to the directory that houses the scrit OR point to it when we call it. We will do the former.

Then to run the R script, we use the `Rscript` command, followed by the name/path to the file:

```
Rscript print_mean_hp.R
```

The output should be:

```
[1] 146.6875
```

## A couple notes about scripts

- If you want something to be output to the command line/terminal/Git bash, you **should** explicitly ask for it to be print. *This is not an absolute requirement in R, but it is in Python!*
- From a reproducibility perspective, if we want input from the user, usually we will design the scripts to take command line arguments, and not use keyboard/user prompts.


## Script structure and organization

Although not necessary in R or Python, it is still good practice and advised to organize the code in your script into a main function and other functions. This practice keeps your code readable and organized, and in Python has some additional benefits we will discuss later.

##### Example R script organization:
```
#! /usr/bin/env Rscript 
# documentation comments

# import libraries/packages

# parse/define command line arguments here

# define main function
main <- function(){
    # code for "guts" of script goes here
}

# code for other functions goes here

# call main function
main()
```

##### Example Python script organization:
```
#!/usr/bin/env python 
# documentation comments

# import libraries/packages

# parse/define command line arguments here

# define main function
def main():
    # code for "guts" of script goes here

# code for other functions goes here

# call main function
if __name__ == "__main__":
    main()
```

*You can see that R and Python scripts should have roughly the same style. There is the difference of `if __name__ == "__main__":` in Python scripts, and R does not really have an equivalent. The benefit of some control flow around `main`, as is done in Python, is so that you could import or source the other functions in the script without running the `main` function.*

## R Script development example:

Here we write a script called `quick_titanic_fare_se.R` which reads in the [titanic dataset](https://github.ubc.ca/ubc-mds-2016/datasets/raw/master/data/titanic.csv) and calculates the standard error for the fare (ticket price) variable.

Our script has two functions, a function we defined to calculate the standard error (such a function does not exist in R) and a `main` function which runs the "body" of our code.

```
#! /usr/bin/env Rscript 
# quick_csv_stat.R
# Tiffany Timbers, Oct 2016
#
# This script calculates the standard error for the fare (ticket price) 
# from titanic.csv. This script takes no arguments.
#
# Usage: Rscript quick_csv_stat.R

# define main function
main <- function(){
  
  # read in data
  data <- read.csv('titanic.csv')
  
  # print out mean of variable of interest
  out <- sterror(data[['fare']])
  print(out)
}

# standard error function
sterror <- function(x){
  se <- sd(x, na.rm=TRUE)/sqrt(length(x))
  return(se)
}

# call main function
main()
```

##### Using command line arguments in R
Let's make our script more flexible, and let us specify when we call the script, what variable we want to calculate the standard error for.

To do this, we use the function `commandArgs`. This function will collect the text we enter at the command line when we call the script, and make it available to us when we run the script. 

When we run `commandArgs` it takes the text we entered at the command line and gives it to us as a character vector, and whitespace at the command line is what is used to parse the text into separate items in the vector.

Usually when we use `commandArgs` we provide the argument, `trailingOnly = TRUE` so that `commandArgs`only returns the text after the name of the script (the rest is generally unimportant to us).


```
#! /usr/bin/env Rscript 
# quick_csv_stat.R
# Tiffany Timbers, Oct 2016
#
# This script calculates the standard error for a specified 
# variable from titanic.csv. This script takes a column name
# as the variable argument.
#
# Usage: Rscript quick_csv_stat.R fare


# read in command line arguments
args <- commandArgs(trailingOnly = TRUE)
variable <- args[1]

# define main function
main <- function(){
  
  # read in data
  data <- read.csv('titanic.csv')
  
  # print out mean of variable of interest
  out <- sterror(data[[variable]])
  print(out)
}

# standard error function
sterror <- function(x){
  se <- sd(x, na.rm=TRUE)/sqrt(length(x))
  return(se)
}

# call main function
main()
```

Let's make our script even more flexible, and let us specify that dataset as well (we could then use it more generally on other files, such as the Gapminder `.csv`'s we saw in Block 1).


```
#! /usr/bin/env Rscript 
# quick_csv_stat.R
# Tiffany Timbers, Oct 2016
#
# This script calculates the standard error for a specified 
# variable from a .csv file. This script takes a filename and
# a column name as the variable argument.
#
# Usage: Rscript quick_csv_stat.R titanic.csv fare

# read in command line arguments
args <- commandArgs(trailingOnly = TRUE)
input_file <- args[1]
variable <- args[2]

# define main function
main <- function(){
  
  # read in data
  data <- read.csv(input file)
  
  # print out mean of variable of interest
  out <- sterror(data[[variable]])
  print(out)
}

# standard error function
sterror <- function(x){
  se <- sd(x, na.rm=TRUE)/sqrt(length(x))
  return(se)
}

# call main function
main()
```

Finally, let's make our script VERY flexible, and let is also specify the summary stat we are interested in:

```
#! /usr/bin/env Rscript 
# quick_csv_stat.R
# Tiffany Timbers, Oct 2016
#
# This script calculates a specified summary stat for a specified 
# variable from a .csv file. This script takes a filename, 
# a summary stat and a column name as the variable arguments.
#
# Usage: Rscript quick_csv_stat.R titanic.csv mean fare

# read in command line arguments
args <- commandArgs(trailingOnly = TRUE)
input_file <- args[1]
statistic <- args[2]
variable <- args[3]

main <- function(){ 
  # read in data
  data <- read.csv(input_file)
  
  # print out appropriate statistic based on command line args
  if (statistic == 'mean'){
    out <- mean(data[[variable]], na.rm=TRUE)
    print(out)
  } else if (statistic == 'median'){
    out <- median(data[[variable]], na.rm=TRUE)
    print(out)
  } else if (statistic == 'mode'){
    out <- mode(data[[variable]], na.rm=TRUE)
    print(out)
  } else if (statistic == 'sd'){
    out <- sd(data[[variable]], na.rm=TRUE)
    print(out)
  } else if (statistic == 'se'){
    out <- sterror(data[[variable]])
    print(out)
  } else {
    print("You should provide an argument for what statistic to get (e.g., mean, median, mode, sd or se)")
  }
}

# standard error function
sterror <- function(x){
  se <- sd(x, na.rm=TRUE)/sqrt(length(x))
  return(se)
}

# call main function
main()
```

## Scripts in Python

##### Command line arguements in Python explained

In Python, there is no built-in function for extracting command line arguments, so we need to import a library to do this. We will be using the `argparse` library because it has very nice functionality and flexibility. Another common library you might come across to solve this problem is `Sys`. It works quite fine for positional arguments (as we have been doing), but has limited functionality and flexibility for going beyond this (e.g., making nice option/argument flags, help options, etc).

How to use `argeparse`:

1. `import` the `argeparse` package
2. use the `ArgumentParser()` function to create an object for parsing command line strings into Python objects.
3. Use the `add_argument()` function to store the value of the argument.
4. Use `parse_args()` to make an object from which the stored value of the argument can be retrieved.
5. Use `{argument_object}.{argument_name}` to retrieve the stored value.

For example:

```
# step 1
import argparse

# step 2
parser = argparse.ArgumentParser()

# step 3
parser.add_argument('input_file')
parser.add_argument('statistic')
parser.add_argument('variable')

# step 4
args = parser.parse_args()

# step 5
print(args.input_file)
```

##### Our first Python script

Let's take our VERY flexible R script and recreate it in Python:

```
#!/usr/bin/env python 
# quick_csv_stat.py
# Tiffany Timbers, Oct 2016
#
# This script calculates a specified summary stat for a specified
# variable from a .csv file. This script takes a filename,
# a summary stat and a column name as the variable arguments.
#
# Dependencies: argparse, pandas, numpy
#
# Usage: python quick_csv_stat.py titanic.csv mean fare

# import libraries
import argparse
import pandas as pd
import numpy as np

# read in command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('input_file')
parser.add_argument('statistic')
parser.add_argument('variable')
args = parser.parse_args()

def main():

    # read in data
    data = pd.read_csv(args.input_file)

    if args.statistic == 'mean':
        out = data[args.variable].mean()
        print(out)
    elif args.statistic == 'median':
        out = data[args.variable].median()
        print(out)
    elif args.statistic == 'mode':
        out = data[args.variable].mode()
        print(out)
    elif args.statistic == 'sd':
        out = data[args.variable].std()
        print(out)
    elif args.statistic == 'se':
        out = sterror(data[args.variable])
        print(out)
    else:
        print("You should provide an argument for what statistic to get (e.g., mean, median, mode, sd or se)")

# standard error function
def sterror(x):
    se = x.std()/np.sqrt(x.size)
    return se

# call main function
if __name__ == "__main__":
    main()
```

# Concept map wrap-up

- When to work in a read-eval-print-loop (REPL) framework versus when to use scripts
- Scripts in R
- Scripts in Python
