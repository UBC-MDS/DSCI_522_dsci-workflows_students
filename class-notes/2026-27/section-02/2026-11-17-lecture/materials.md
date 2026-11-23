# Course materials: 2026-11-17 lecture

What this lecture worked from: the class's demo repository, the diagrams drawn in class,
and textbook sections from *Reproducible and Trustworthy Workflows for Data Science*
(<https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/>),
as published on 2026-11-17. Each textbook heading links to its published section.

## Demo repository

The repository the instructor cloned and worked in during class:
<https://github.com/chendaniely/2026-11-17-git>. Its pull requests, as GitHub lists them
on 2026-11-17, all merged into `main`:

- [#1 Learning about branches and PRs](https://github.com/chendaniely/2026-11-17-git/pull/1), from branch `dan-b1`
- [#2 define fetch --prune](https://github.com/chendaniely/2026-11-17-git/pull/2), from branch `dan-fetch`
- [#3 branch -d and -D](https://github.com/chendaniely/2026-11-17-git/pull/3), from branch `dan-delete`

## Diagrams drawn in class

The instructor drew these by hand during the lecture. Each is an image in this session's
folder. In both, the left side is the instructor's laptop (the local repository) and the
right side is `origin`, drawn as a cloud; commits are circles joined by arrows.

### `git1.png`

The set of diagrams for the Git review, and for branches and merging pull requests.
Labels in the drawing: `clone`, `origin`, `main`, `b1`.

### `git2.png`

The diagram for several branches and pull requests at once, with a conflict, and the
visual of how a rebase works. Label in the drawing: `rebase`.

## [8 Git branches](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html)

### [Learning Objectives](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#learning-objectives)

1.  Describe what branches are in Git and explain why they are useful for collaboration.
2.  Use Git to create new branches, switch between branches, and merge branches locally.
3.  Bring a branch that has fallen behind the default branch up to date, using merge or rebase.

Branches allow you to have a playground for developing and testing new additions to your code, as well as fixes. This playground lets your explore, experiment and test in a safe place - away from others that might be using or depending on the current version of your code. This is perhaps more obviously useful if your project is deployed and has users (e.g., a data visualization dashboard, an R or Python package, a phone app, etc), but this can also be useful for code that make up a data analyses. As, in addition to the reasons stated above for branching, branching also lets you organize units of work into smaller, more manageable chunks that are easier for collaborators to check over and review.

Once the new code additions or fixes have been finalized in their branch playground, they can be merged back to the main code-base. Several branch playgrounds can co-exist, one for each new code addition or fix being worked on. This allows for parallelization of work!

We can use a construction of a house as a metaphor for this kind of development. First, you need to build the foundation. Since everything depends on the foundation being built, this would be developed on the main branch. When the foundation is finished, the construction of other parts of the house that don’t depend on each other could take place in parallel, e.g. some contributors might start working on the walls and others on the floor. When either of these features is finished, it can be added back to the house (merged into main). When depicted graphically, this process would look something like this (each dot is a commit).

![](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/img/branches-house-analogy.png)

A more realistic Git branching example for a data analysis project might look something like this:

![](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/img/git-branch-diagrams.png)

### [8.1 Creating a branch using the command line](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#creating-a-branch-using-the-command-line)

In the terminal, and in the working directory of the project in which you wish to create a branch, use `git switch` with the `-c` flag and specify the branch name. This create a new branch and immediately switch to it. For example, to create a branch named `patch-docs` (a good branch name if we were planning on working on a fix in the project’s documentation), we would type:

``` bash
git switch -c patch-docs
```

To ask Git what branches now exist and to see where we are, we can use the `branch` command with the `-v` flag (for “verbose”, meaning tell us everything!):

``` bash
git branch -v
```

And we should see something like the output shown below, which lists the branch names in the first column, the SHA of the last commit on each branch in the second column, and the commit message associated with the last commit in the third column:

``` sh
  main       f756bbb initial
* patch-docs f756bbb initial
```

As you work here on this new branch, you can commit your changes to version control locally, and even push your changes to the remote repository. All the changes however will live only on that branch until you do something to move them to another branch. When you want to start discussing your changes with your collaborators to start the process of bringing these changes into the main branch (main code-base) you typically create what is called a pull request. A pull request is a like an asking your collaborators “is it OK to merge my code?” Usually there will be some discussion and a few more revisions to the code, but eventually they will give you the thumbs up when everything looks good and the code can then be merged. We will discuss this more in [Pull requests](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/github-pull-requests.html).

#### [8.1.1 Switching to branches that already exist](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#switching-to-branches-that-already-exist)

After you have been working on your new brain for some time, you will eventually want to get back to the project’s default branch, or some other branch. To do this, we use `git switch <branch_name>`. Note that we do not use the `-c` flag this time, as we are not creating a new branch.

#### [8.1.2 Getting remote branches you did not create locally](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#getting-remote-branches-you-did-not-create-locally)

If your collaborator creates a branch that you want to run or test locally, but it only exists on the remote repository you have to tell Git to fetch (go get it) for you first, before you can switch to it. You can specify which branch you specifically want to grab, but for simplicity it is often easy to ask Git to fetch all of them for you, using the `fetch` command with the `--all` flag:

``` bash
git fetch --all
```

#### [8.1.3 Useful command line Git branching commands](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#useful-command-line-git-branching-commands)

Below is a table of the most commonly used Git commands for branching. This table includes the commands we presented above as well as the a few other useful ones.

| Description | Command |
|----|----|
| list all local branches | `git branch -v` |
| create a new branch & immediately switch to it | `git switch -c <branch_name>` or `git checkout -b <branch_name>` |
| switch to a branch | `git switch <branch_name>` or `git checkout <branch_name>` |
| fetches all changes to all branches | `git fetch --all` |
| retrieve a branch you don’t have locally on your laptop from GitHub | `git checkout --track origin/<branch_name` |
| merge changes from another branch | `git merge <branch_name>` |
| delete a local branch | `git branch -d <branch_name>` |
| push changes to a remote branch | `git push origin <branch_name>` |

**Exercise**

1.  Make your own copy of [this GitHub repository](https://github.com/ttimbers/sqrt) by clicking the green “Use this template” button. And then clone your copy of the repository to your computer.

2.  Create a new branch named `better_error_msg` in the local repository using Git.

3.  On that branch, fix the `sqrt.py` so that if you run this script with a negative number as an argument you do not get an difficult to understand error, but instead throw a helpful exception informing the user that the number should be positive. Fix to add to `sqrt.py`:

``` python
if number < 0:
  raise Exception("n should not a positive number")
```

4.  Add and commit those changes.

5.  Switch back to the `main` branch and look at the `sqrt.py` file - do you see the change there?

6.  Switch back to the `better_error_msg` branch - do you see the change there?

7.  Push your change to the remote GitHub repository, and see where you can find it there!

**Note**

Note: if you use the Git command line tool and get an error message like the one shown below, this is because you did not state the remote (usually it is `origin`). Try pushing again using `git push origin <branch_name>`

``` sh
fatal: The current branch better_error_msg has no upstream branch.
To push the current branch and set the remote as upstream, use
    git push --set-upstream origin better_error_msg
To have this happen automatically for branches without a tracking
upstream, see 'push.autoSetupRemote' in 'git help config'.
```

### [8.2 Useful things you can do with branches on GitHub](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#useful-things-you-can-do-with-branches-on-github)

Create a new branch:

![](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/img/create_branch.png)

Source: <https://github.com/UBC-DSCI/introduction-to-datascience>

View all branches and their status:

![](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/img/view_branches.png)

Source: <https://github.com/UBC-DSCI/introduction-to-datascience>

And delete remote branches:

![](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/img/delete_branches.png)

Source: <https://github.com/UBC-DSCI/introduction-to-datascience/branches>

### [8.3 What happens when my feature branch falls behind main?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#what-happens-when-my-feature-branch-falls-behind-main)

There are a few ways you can fix this problem.

#### [8.3.1 Using merge](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#using-merge)

> How to catch up a branch that has fallen behind the `main` branch using the command line:
>
> - run `git pull origin main` to pull any changes from the remote version of main that we might not have
> - run `git switch <branch>` to make sure we are on the branch we want to catch up
> - run `git merge main` to merge the changes
> - run `git push origin <branch>` to push our updated branch to the remote

#### [8.3.2 Using rebase](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#using-rebase)

1.  Make sure everything is committed in your new branch
2.  Move to the main branch: `git switch main`
3.  Make sure the main branch is up to date: `git pull origin main`
4.  Move back over to your branch: `git switch <branch>`
5.  Update the changes from main: `git rebase main`

## [9 Pull requests](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/github-pull-requests.html)

### [Learning Objectives](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/github-pull-requests.html#learning-objectives)

1.  Use GitHub pull requests to bring new changes into the project’s default branch.
2.  Close a pull request without merging it.
3.  Open a draft pull request to share work in progress, and mark it ready for review.

### [9.1 Creating a pull request](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/github-pull-requests.html#creating-a-pull-request)

To create a pull request, you first need to ensure all the local changes you made on the new branch are also available on the remote repository (i.e., you need to push them). Once that has happened you need to go to the remote GitHub repository, as pull requests are created from there.

GitHub often tries to be helpful when a change is pushed to a new branch that doesn’t yet exist on the default branch by showing you a yellow banner listing any recently pushed branches.

![](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/img/create-pr.png)

To create a pull request, you click the green button “Compare & pull request”. In the new page, add a message to describe the changes you have made, scroll down to review the changed files, and the click the green button that reads “Create pull request”. If you are working together in a team, you could also designate certain team members to review your work and assign relevant labels, via the right hand side panel.

The next step is for a collaborator to review your work and merge it in if they approve it (see [Code review on GitHub](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/github-code-review.html)).

**Exercise**

1.  Use the green “Compare & pull request” button on the yellow banner to open a pull request.

2.  Go to the “Pull requests” tab on the remote GitHub repository and explore the “Conversation” and “Files changed” sub-tabs there.

### [9.2 Draft pull requests](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/github-pull-requests.html#draft-pull-requests)

Sometimes you want to open a pull request before the work is finished, to show your teammates where you are heading, to ask for early feedback, or to see whether your changes pass the project’s automated checks. Instead of adding “WIP” (work in progress) to the title, open the pull request as a **draft**. On the page where you write the pull request’s description, use the drop-down arrow beside the green “Create pull request” button, select “Create draft pull request”, and then click “Draft pull request”.

A draft pull request cannot be merged, and it tells your teammates that it is not ready for review yet. When the work is ready, click “Ready for review” in the merge box at the bottom of the pull request’s “Conversation” tab. If you need to go back to working on it, click “Convert to draft” under “Reviewers” in the right-hand sidebar.

### [9.3 How do you not accept a pull request?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/github-pull-requests.html#how-do-you-not-accept-a-pull-request)

In some cases, it might not make sense to merge a pull request. To close a pull request that should not be merged, scroll to the bottom of the pull request page, and look for a gray “Closes pull request” button. This will end move the pull request to the closed pull requests section (similar to closed issues) and does not merge the changes.

![](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/img/close-pr.png)

## [10 Code review on GitHub](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/github-code-review.html)

### [Learning Objectives](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/github-code-review.html#learning-objectives)

1.  Use GitHub’s pull requests tool to perform code reviews, with in-line comments and suggested changes.
2.  Accept suggested changes from a code review and merge the pull request.

We very often need to have a conversation to get pull requests into good shape before merging the changes into the `main` branch. GitHub has a very nice tool we can utilize to do this: GitHub code reviews. This tool allows us to add inline comments to proposed changes, as well as inline suggested changes that can be accepted with a click of a button. These features increase review efficiency and effectiveness!

- In the project, you are expected to read and review each other’s code BEFORE accepting a pull request.

- Do not expect all (or even most) pull requests to be perfect in their first submission.

- Pull requests are opened, reviewed and merged by people. You may use AI tools to help check the code in a pull request, but a person reviews it and decides whether to merge it. Write down how your project uses AI tools in its [AI policy](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/filenames-project-organization.html#ai-policy).

![](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/img/code-review-suggest-change.png)

**Exercise**

**Demo: do a code review**

I am going to demo a code review of a pull request. I have set-up a template GitHub repository for you so that you can easily generate a pull request for you to review if you want to try this later.

**Steps:**

1.  Click the green “Use this template” button in [this repository](https://github.com/ttimbers/review-my-pull-request) to obtain a copy of it for yourself (do not fork it).

2.  Go to Repository Settings \> Actions \> General and change two settings:

    - Under “Actions permissions”, select “Allow all actions and reusable workflows”.
    - Under “Workflow permissions”, select “Read and write permissions”, and tick “Allow GitHub Actions to create and approve pull requests”. A repository made from a template does not keep this box ticked, so you need to tick it yourself.

    Click the “Save” button under each section you change. When you are done, the page should look like this:

    ![GitHub's Settings, Actions, General page for a repository. Under Actions permissions, Allow all actions and reusable workflows is selected. Under Workflow permissions, Read and write permissions is selected and Allow GitHub Actions to create and approve pull requests is ticked.](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/img/gha-actions-settings-page.png)

    Here are the two “Workflow permissions” settings up close:

    ![The Workflow permissions section, with red arrows pointing to the selected Read and write permissions option and the ticked Allow GitHub Actions to create and approve pull requests checkbox.](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/img/gha-general-settings.png)

    If you skip this step, the workflow in the next step fails with an error like `remote: Permission to <user>/<repo>.git denied to github-actions[bot]` and `The requested URL returned error: 403`. Changing these settings fixes it.

3.  Click on the Actions tab, and then click on the workflow `.github/workflows/pr.yml`. You then should see a **“Run workflow”** button with a drop down menu, from that menu select **“Run workflow”**.

4.  Click on the Pull Requests tab of your copy of the repository, click on the pull request titled “Report most accomplished pilots”, and then click on “Files Changed”. Next click on the `star-wars.Rmd` file. Review the file and observe the following problems with the R Markdown report that was submitted via the pull request:

    - Reasoning of the sentence on line 15
    - Incompatibility with the sentence on line 15 with the code in the code chunk named `table-of-most-accomplished-pilots`
    - Incorrect code in code chunk named `table-of-most-accomplished-pilots` (unnested `film` instead of `starships`) leads to naming the wrong pilot as the most accomplished pilot on line 19
    - Incorrect code in code chunk named `table-of-most-accomplished-pilots` (unnested `film` instead of `starships`) leads to the use of the wrong character’s picture in the image that is sourced in the code chunk named `top-pilot` (it should be a picture of Obi-Wan Kenobi, you could use this URL for example: <https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/ewan-mcgregor-obi-wan-1570898048.jpg>).

5.  Add comments and suggested changes using the `+` sign beside the line numbers (the first time you do this will trigger the start of your code review. Need help? See [GitHub’s how to on reviewing proposed changes in a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/reviewing-proposed-changes-in-a-pull-request).

6.  After you have made all the comments and suggested changes, then add a general comment for the code review, select “Request Changes” and submit your code review.

**Exercise**

**Demo: Accept suggested changes from a code review**

**Steps:**

1.  To accept the code changes that you provided as suggestions, revisit the Pull Requests tab of your copy of the repository and clicking on the pull request titled “Report most accomplished pilots”. Scroll through the pull request comments and find the code suggestions. Then click on the “Commit suggestion button” for each suggestion.

2.  Click on the “Show all reviewers” link beside the red “Changes requested”” text. Then click on the `...` beside the reviewer and click “Approve changes”.

3.  Finally click on the green buttons (“Merge Pull Request” & “Confirm merge”) to merge the pull request.

**Activity**

**Discussion**

If I didn’t tell you what to review, could you really have done a good job reviewing the code only on GitHub?

*Hint: if I didn’t tell you that the top pilot was Obi-Wan Kenobi, how would you have known that?*
