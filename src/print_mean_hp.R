# author: Tiffany Timbers
# date: 2020-11-17

# This script calculates the mean horsepower of the cars from the built-in
# R data frame `mtcars`. This script takes no arguments.
#
# Usage: Rscript print_mean_hp.R

mean_hp <- mean(mtcars$hp)
print(mean_hp)
