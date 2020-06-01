## Lab 4 - Managing your environment

#### Goal

In this lab you will get to practice using tools to manage your computing environment,
including `packrat`, `conda` or `virtualenv`, and `Docker`, as well as working with
branches in Git. The aim is that you will become familiar with these tools, and form opinions about their usefulness, as well as their limitations.

#### Submission Instructions:
<!-- rubric={mechanics:1} -->

<span id="rubric">
		<font size=5><img src="https://github.com/UBC-MDS/public/blob/master/rubric/icon/num_1.png?raw=true"/ alt="1"></font>
		<font size=5><a href="https://github.com/UBC-MDS/public/blob/master/rubric/rubric_mech.md"><img src="https://github.com/UBC-MDS/public/blob/master/rubric/icon/mech.png?raw=true" alt="[Mechanics]" " width=32/></a></font>

</span>
<!-- end of rubric snippet -->

- You should have a well organized lab repo/directory structure, where:
  - all code files (`.R`, `.py`, `.Rmd`, `.ipynb`, `Dockerfile`) live in the `src` directory,
  except for the driver scripts (Shell script and Makefile which call your
  analysis scripts).
  - all rendered documents live in the `results` directory
  - all data used belong in the `data` directory
  - answers to written questions should be in a `.md` file in the `doc` directory

- In the main `README.md` file in the lab/assignment repo, you must make it clear where all files are for all assignments, as well as explain anything the we need to know to understand your homework submission.

- In the main `README.md` file you should also specify the links to the Github repos
used/modified as part of the assignment, as well as to your docker image on Dockerhub.

*note - You will need to use R and Python code from previous assignments in this class or others*

### Exercise 1 - Managing pacakge dependencies within R and Python
<!-- rubric={reasoning:2,mechanics:3} -->

<span id="rubric">
		<font size=5><img src="https://github.com/UBC-MDS/public/blob/master/rubric/icon/num_3.png?raw=true"/ alt="3"></font>
		<font size=5><a href="https://github.com/UBC-MDS/public/blob/master/rubric/rubric_mech.md"><img src="https://github.com/UBC-MDS/public/blob/master/rubric/icon/mech.png?raw=true" alt="[Mechanics]" " width=32/></a></font>
&nbsp;		<font size=5><img src="https://github.com/UBC-MDS/public/blob/master/rubric/icon/num_2.png?raw=true"/ alt="2"></font>
		<font size=5><a href="https://github.com/UBC-MDS/public/blob/master/rubric/rubric_reasoning.md"><img src="https://github.com/UBC-MDS/public/blob/master/rubric/icon/reasoning.png?raw=true" alt="[Reasoning]" " width=32/></a></font>

</span>
<!-- end of rubric snippet -->

- Find your partner on [this list](https://github.ubc.ca/ubc-mds-2016/DSCI_522_dsci-workflows_students/blob/master/lab4_partners.md).
- Each person should:
  - Fork a previous repository (or two repositories) from previous MDS lab(s) from the `ubc-mds-2016` organization to your Github.ubc.ca account. For this assignment you will
  need to have some R code, and some Python code that you can further develop. If you make this repository private, you **MUST** add the TA, Instructor and your partner as contributors to this forked repo.
  - Modify some of the R code in your forked repo to use *at least* one additional library that your partner does not have installed.
  - Modify some of the Python code in your forked repo to use *at least* one additional library that your partner does not have installed.
  - Modify the `README`'s of the forked repository (or two repositories) to make it explicit
  what the code depends on, and how it should be run. Follow your instructions and verify that you can run your own code by following them.
  - In the main `README.md` file for you lab repo, you should specify the links to the/these forked and modified Github repo(s).

- Partner # 1 should use `packrat` to manage the R packages for their forked repo containing the modified R code.
- Partner # 2  should use either `conda` or `virtualenv` to manage the Python packages for their forked repo containing the modified Python code.

  - Each person should then:
    - Download your partners R and Python code, refer to the `README` and run both their R and Python code.

- In ~ half a page, discuss the experience you had trying to get your partner's code to run. Also comment on whether it mattered if they used a package manager? This should be answered in
a `.md` file in the `doc` directory of your lab's repo.

### Exercise 2a - Write your own `Dockerfile`, and create your own Docker image that you host on Docker Hub
<!-- rubric={code:2,reasoning:2,mechanics:3} -->

<span id="rubric">
		<font size=5><img src="https://github.com/UBC-MDS/public/blob/master/rubric/icon/num_2.png?raw=true"/ alt="2"></font>
		<font size=5><a href="https://github.com/UBC-MDS/public/blob/master/rubric/rubric_code.md"><img src="https://github.com/UBC-MDS/public/blob/master/rubric/icon/code.png?raw=true" alt="[Code]" " width=32/></a></font>
&nbsp;		<font size=5><img src="https://github.com/UBC-MDS/public/blob/master/rubric/icon/num_3.png?raw=true"/ alt="3"></font>
		<font size=5><a href="https://github.com/UBC-MDS/public/blob/master/rubric/rubric_mech.md"><img src="https://github.com/UBC-MDS/public/blob/master/rubric/icon/mech.png?raw=true" alt="[Mechanics]" " width=32/></a></font>
&nbsp;		<font size=5><img src="https://github.com/UBC-MDS/public/blob/master/rubric/icon/num_2.png?raw=true"/ alt="2"></font>
		<font size=5><a href="https://github.com/UBC-MDS/public/blob/master/rubric/rubric_reasoning.md"><img src="https://github.com/UBC-MDS/public/blob/master/rubric/icon/reasoning.png?raw=true" alt="[Reasoning]" " width=32/></a></font>

</span>
<!-- end of rubric snippet -->

- Fork your DSCI 522 Lab 3 repository from the `ubc-mds-2016` organization to your Github.ubc.ca account. If you make this repository private, you **MUST** add the TA and Instructor as contributors to this forked repo. Add a link to this forked repo in your lab's main `README`.

- Write a `Dockerfile` for your automated `make` pipeline you created in DSCI 522's Lab # 3. Your `Dockerfile` should install all necessary dependencies. The `Dockerfile` should be included in root directory of the forked DSCI 522 Lab 3 repository.  

- Use that `Dockerfile` to create a Docker image that can run your automated pipeline.

- Test out the Docker image - could it run your automated pipeline? If not modify that `Dockerfile` and try again.

- To demonstrate you were successfully able to do all of this, include an `.md` file in the `doc` directory in your homework submission that shows the commands you used to get your `Dockerfile` to create a Docker image, and the command to get your Docker image to successfully run you data analysis pipeline, and the resultant output.

- Once you have a Docker image that let's you run your automated pipeline, create a [Docker Hub](https://hub.docker.com/) account and put that Docker image on Docker Hub (include a link to this Docker image in both the forked DSCI 522 Lab 3 repository's `README` and the current (Lab 4) lab's `README`).

- In ~ half a page, discuss the experience you had getting Docker working with your project. Also discuss whether or not this made your more (or less) confident of the reproducibility of you data analysis pipeline.

### Exercise 2b - Docker Hub Automated Build (optional)
<!-- rubric={mechanics:1} -->

<span id="rubric">
		<font size=5><img src="https://github.com/UBC-MDS/public/blob/master/rubric/icon/num_1.png?raw=true"/ alt="1"></font>
		<font size=5><a href="https://github.com/UBC-MDS/public/blob/master/rubric/rubric_mech.md"><img src="https://github.com/UBC-MDS/public/blob/master/rubric/icon/mech.png?raw=true" alt="[Mechanics]" " width=32/></a></font>

</span>
<!-- end of rubric snippet -->

- Use a Docker Hub Automated Build to build your Docker image from your Dockerfile: https://docs.docker.com/docker-hub/builds/.
- If you do this successfully, Docker Hub marks images built this way as "Trusted Build".

### Exercise 3 - Branching with Git (optional)
<!-- rubric={reasoning:1,mechanics:1} -->

<span id="rubric">
		<font size=5><img src="https://github.com/UBC-MDS/public/blob/master/rubric/icon/num_1.png?raw=true"/ alt="1"></font>
		<font size=5><a href="https://github.com/UBC-MDS/public/blob/master/rubric/rubric_mech.md"><img src="https://github.com/UBC-MDS/public/blob/master/rubric/icon/mech.png?raw=true" alt="[Mechanics]" " width=32/></a></font>
&nbsp;		<font size=5><img src="https://github.com/UBC-MDS/public/blob/master/rubric/icon/num_1.png?raw=true"/ alt="1"></font>
		<font size=5><a href="https://github.com/UBC-MDS/public/blob/master/rubric/rubric_reasoning.md"><img src="https://github.com/UBC-MDS/public/blob/master/rubric/icon/reasoning.png?raw=true" alt="[Reasoning]" " width=32/></a></font>

</span>
<!-- end of rubric snippet -->

- Create a new branch in your lab's repo called `new_feature`.

- Add & commit a file (any file) to the `new_feature` branch. Push this change to the `new_feature` branch on Github.

- Locally, merge the `new_feature` branch with `master`, and then push the changes to `master` on Github.

- Delete the `new_feature` branch both locally and remotely.

- Prove that you did the above by saving the output of both `git branch -v` and `git reflog` to a `.md` file in the `doc` directory of your lab's repo (include the command calls to 	`git branch` and `reflog` in this file too).

- In ~ half a page, tell us what Git tool(s) you used to complete this exercise (command line, Sourcetree, Git Kraken, *etc.*) and discuss why branching might be a useful workflow in a data science project. Specifically, mention problems you have encountered (or you could imagine encountering) working with Git that branching could help solve.
