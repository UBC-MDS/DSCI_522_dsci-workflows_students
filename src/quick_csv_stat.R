# author: Tiffany Timbers
# date: 2020-01-15

"This script calculates a specified summary stat for a specified 
variable from a .csv file. This script takes a filename, 
a summary stat and a column name as the arguments.

Usage: quick_csv_stat.R --file_path=<file_path> --statistic=<statistic> --var=<var>
" -> doc

library(tidyverse)
library(testthat)
library(docopt)

opt <- docopt(doc)

main <- function(file_path, statistic, var){

  # read in data
  data <- read.csv(file_path)

  # print out appropriate statistic based on command line args
  if (statistic == 'mean'){
    out <- data %>% 
      select(!!var) %>% 
      pull() %>% 
      mean(na.rm = TRUE)
    print(out)
  } else if (statistic == 'median'){
    out <- data %>% 
      select(!!var) %>% 
      pull() %>% 
      median(na.rm = TRUE)
    print(out)
  } else if (statistic == 'sd'){
    out <- data %>% 
      select(!!var) %>% 
      pull() %>% 
      sd(na.rm = TRUE)
    print(out)
  } else if (statistic == 'se'){
    out <- data %>% 
      select(!!var) %>% 
      pull() %>% 
      sterror(na.rm = TRUE)
    print(out)
  } else {
    print("You should provide an argument for what statistic to get (e.g., mean, median, sd or se)")
  }
}

#' calculate standard error
#'
#' @param x a vector of numeric values
#' @return the standard error of x as a numeric vector of length one
#' @examples
#' sterror(mtcars$hp)
sterror <- function(x) {
  sd(x, na.rm = TRUE) / sqrt(length(x))
}

test_sterror <- function(){
  test_that("sterror should return 0 if vector values are all the same", {
    expect_equal(sterror(c(1, 1, 1)), 0)
  })
}

test_sterror()

main(opt$file_path, opt$statistic, opt$var)
