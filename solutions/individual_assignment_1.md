
## Individual assignment 1

rubric={correctness:1}

The purpose of this assignment is to ensure that everyone does some
self-learning and obtains practice on using docopt to create command
line arguements in scripts, as well as creating releases on GitHub. This
assignment will be graded for completion. You must attempt all questions
to get the grade.

### Submission instructions

You must also submit a `.html` version of this homework to Canvas. To
programmatically render your notebook to html and submit the assignment
to Canvas, open [submit.ipynb](submit.ipynb) and use the instructions
there.

### Exercise 1

Create a public repository on GitHub.com called `docopt_demo`. Paste the
url below:

> <https://github.com/ttimbers/docopt_demo>

### Exercise 2

**Getting documentation from a {docopt} R script**

In [this
repo](https://github.ubc.ca/MDS-2020-21/DSCI_522_dsci-workflows_students),
in the `src` directory, you will find a script named `demo.R`. Access
the documentation for that script from the command line by running the
script with the `--help` option (and no other options or arguments).
Paste the documentation that was printed out to your terminal below.

>     This script prints out docopt args.
>     Usage: demo.R <arg1> --arg2=<arg2> [--arg3=<arg3>]
>     Options:
>     <arg>             Takes any value (this is a required positional argument)
>     --arg2=<arg2>     Takes any value (this is a required option)
>     [--arg3=<arg3>]   Takes any value (this is an optional option) 

### Exercise 3

**What does `docopt` return in R?**

Run the `demo.R` script giving it appropriate arguments to see what the
`docopt` function in R returns. Try setting and not setting a value for
`arg3`. Describe what you observed below.

For options, you need to include the `--` in the command line call, for
example:

    Rscript src/my_script something --anoption=something more

> When I set the first poistional command line argument (`arg1`) to
> “this” and then the first required optional argument (`arg2`) to “is”
> and ran the script, it printed out a list with 6 elements, the first
> three were the two characters I passed in at the command line, and
> then NULL for `--arg3` as I passed no value for that. They had
> non-syntactic names for these elements. The last 3 elements had the
> same values duplicated, however, they had syntactic names for these
> elements. The type of the object was also printed out (a list). When I
> added “a\_test” for the last optional option (`arg3`) NULL was
> replaced with “a\_test” in the list that was printed out.

### Exercise 4

**Break this script!**

Run the `demo.R` script and find at least 3 different ways to break it
by changing the values or order of the command line arguments at the
command line (do not modify the script). Document how you did this
below.

> 1.  Removing the first positional argument (`arg1`) breaks it
> 2.  Removing the second required argument (`arg2`) breaks it
> 3.  Adding another command line argument (e.g., `--arg4=test`) breaks
>     it

### Exercise 5

**Add a new optional positional argument**

Copy the `demo.R` script into your `docopt_demo` repo, and then edit it
to add a new positional argument that is optional. Also modify the
script so that it prints out the value for this new argument in addition
to the entire `docopt` object and `docopt` object type. Commit this
change and push it to your `docopt_demo` repository. Paste the URL to
this commit below:

> <https://github.com/ttimbers/docopt_demo/commit/ed2d715b36f3ec968a5b9f1e56f107682baa5521#diff-0548e1109a8e781327f4a94d4329ad8a19d6233c79510fe6d97cf5a637cc2d2a>

### Exercise 6

**Add a main function**

Modify the `demo.R` script further so that the three print statements
happen inside a main function. Commit this change and push it to your
`docopt_demo` repository. Paste the URL to this commit below:

> <https://github.com/ttimbers/docopt_demo/commit/dff5994f38801b347b1932308f68bf834e783c47#diff-0548e1109a8e781327f4a94d4329ad8a19d6233c79510fe6d97cf5a637cc2d2a>

### Exercise 7

**What does `docopt` return in Python?**

In [this
repo](https://github.ubc.ca/MDS-2020-21/DSCI_522_dsci-workflows_students),
in the `src` directory, you will find a script named `demo.py`. Run the
`demo.py` script giving it appropriate arguments to see what the
`docopt` function in Python returns. Try setting and not setting a value
for `arg3`. How does this differ from what `docopt` returns in R?
Describe what you observed below.

> Python returns a dictionary with 3 elements instead of a list, where
> the keys are the argument names (including things like `<` and `--`,
> etc) and the values are . Also, when an optional argument is not used,
> it returns None for it instead of NULL.

### Exercise 8

**Add a new optional positional argument**

Copy the `demo.py` script into your `docopt_demo` repo, and then edit it
to add a new positional argument that is optional. Also modify the
script so that it prints out the value for this new argument in addition
to the entire `docopt` object and `docopt` object type. Commit this
change and push it to your `docopt_demo` repository. Paste the URL to
this commit below:

> <https://github.com/ttimbers/docopt_demo/commit/be15dadb64f6d77dab02492a1fbff10b6d9f86cc>

### Exercise 9

Modify the `demo.py` script further so that the three print statements
happen inside a main function. Commit this change and push it to your
`docopt_demo` repository. Paste the URL to this commit below:

> <https://github.com/ttimbers/docopt_demo/commit/81eef76c3a6a53e7a22aa7af31c0051f47f31da5>

### Exercise 10

Create a release in your `docopt_demo` repo called `0.1.0`. Paste the
URL to this release below.

\*Hint: See the [creating a release
docs](https://docs.github.com/en/free-pro-team@latest/github/administering-a-repository/managing-releases-in-a-repository#creating-a-release)
to help complete this exercise.

> <https://github.com/ttimbers/docopt_demo/tree/0.1.0>
