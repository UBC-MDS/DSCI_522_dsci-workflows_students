library(tidyverse)
library(infer)

L01 <- read_csv("L01.csv", col_names = FALSE)
L02 <- read_csv("L02.csv", col_names = FALSE)
L03 <- read_csv("L03.csv", col_names = FALSE)

V <- rep(1:11, each=2)

set.seed(001) # just to make it reproducible
L01$group <- c(sample(V), 11)
L01$section <- 1

set.seed(002) # just to make it reproducible
L02$group <- c(sample(V), 11)
L02$section <- 2

set.seed(003) # just to make it reproducible
L03$group <- c(sample(V), 11)
L03$section <- 3

groups <- bind_rows(L01, L02, L03)
groups <- rename(groups, name = X1)

groups <- groups %>% arrange(section, group)
write_csv(groups, "teams.csv")
