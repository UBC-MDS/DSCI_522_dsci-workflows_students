## Individual assignment 4
rubric={correctness:1}

The purpose of this assignment is to ensure that everyone does some self-learning and obtains practice on creating Docker images from `Dockerfile`s. This assignment will be graded for completion. You must attempt all questions to get the grade.

### Submission instructions

You must submit a link to the GitHub.com repository that you create for this assignment 
(it should be named `dockerfile-practice`),
as well as the link to your Docker image on DockerHub.

### Exercise instructions

1. Create a public repository on GitHub.com repo called `dockerfile-practice`

2. Add a `Dockerfile` to it. This Dockerfile should:
    - Be based off of one of the Jupyter docker-stacks images ([link to Jupyter docker-stacks documentation](https://jupyter-docker-stacks.readthedocs.io/en/latest/index.html), [link to repo of Jupyter docker-stacks Dockerfiles](https://github.com/jupyter/docker-stacks))
    - Add at least one new R or Python package to the Dockerfile (ensure that you pin the version of the package you add).

3. Add a GitHub Actions workflow to automatically build the image, push it to DockerHub, and version the image and GitHub repo when changes are pushed to the Dockerfile ([link to a GitHub Actions Workflow you should use for this](https://github.com/ttimbers/dockerfile-practice/blob/main/.github/workflows/publish_docker_image.yml)).
Note 1: When setting up the workflow on GitHub Actions, be sure to click "Skip this and setup a workflow yourself".
Note 2: You will need to add your DockerHub username and password (naming them `DOCKER_USERNAME` and `DOCKER_PASSWORD`, respectively) as GitHub secrets to this repository for this to work.

4. Make sure you make at least one change to the `Dockerfile` once the GitHub Actions have been setup so that you get the image automatically built and pushed to DockerHub at least once.
