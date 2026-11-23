# DSCI 522: Git branches, pull requests, and merge conflicts

Date Time: 2026-11-17 09:30:09

Instructor: Daniel Chen

## Summary

The lecture opened with practical expectations for DSCI 522: this is the first major project-based course, and students work in fixed lab-section groups. The instructor explained the lab sections repository, where students can find their lab section, group number, and GitHub usernames; those usernames are metadata used across the program. Lab attendance is mandatory because TAs will talk to every group during lab. The course also includes an “interview week” in which students may have a roughly seven-minute, ungraded technical conversation about their Git workflow and their group project code base.

After that, the session reviewed the Git basics from DSCI 521 and moved into the branch-and-pull-request workflow that the group project will use. The instructor worked in a live demo repository, created a commit on `main`, created a new branch with `git switch -c`, committed work on that branch, pushed the branch to `origin`, and opened a GitHub pull request. The pull request was used to review the changed files, add another commit to the same branch, observe the pull request update, merge the branch into `main`, and clean up the local and remote branches.

The final part showed how merge conflicts appear when two branches edit the same lines and one branch is merged first. The instructor demonstrated resolving the conflict locally by rebasing the second branch onto `main`, editing the conflicted file, staging the resolution, continuing the rebase, and force pushing the rewritten branch with `git push --force-with-lease origin dan-delete`. The overall result was a concrete workflow: branch for isolated work, push the branch, use pull requests for review, merge when ready, sync `main`, delete branches, and recover from merge conflicts.

## Knowledge Points

### 1. Group project, lab sections, and interview expectations

- **Lab section groups**:
  - DSCI 522 is a project-based course where students work with others in their lab section.
  - The lab sections repository lists lab sections, group numbers, and GitHub usernames.
  - GitHub usernames are important program-wide metadata.
- **Lab attendance**:
  - Lab attendance is mandatory during lab.
  - TAs will talk to every group during lab, so students should be present when the TA reaches their group.
- **Interview week**:
  - Some students have an “interview week” entry.
  - It is a roughly seven-minute, technical-interview-style conversation about the student’s Git knowledge and group project code base.
  - It was described as not affecting the course grade.
  - Students should be prepared to talk about the code base they are working in, because anything in the code base may be discussed.

### 2. Git review: local work, remote work, and branches

- **Local repository vs `origin`**:
  - Work happens in two places: the local computer and the GitHub remote, commonly called `origin`.
  - `git clone` is a one-time command that brings a remote repository to the local machine.
  - `git commit` records local changes.
  - `git push` sends local commits to the remote.
  - `git pull` brings remote commits down to the local repository.
  - The remote repository is what matters for grading and publication: work that exists only on a local computer is effectively not shipped.
- **`main` and `origin/main`**:
  - `main` is the local default branch.
  - `origin/main` is the local Git reference to the remote `main` branch.
  - `HEAD` points to the branch currently checked out.
  - When commits are made, the branch that `HEAD` points to moves forward.
- **Branches**:
  - A branch is a named line of commits.
  - Branches let students work in parallel streams instead of all editing the same default branch at the time.
  - `main` can be treated as the stable, reviewed, “production” place: in this course, at minimum the code should work.
  - Exploratory work, debugging, new features, or unfinished code can live on branches.
  - Branches are useful even for single-person work: they allow isolated experiments and make it easier to discard an entire branch instead of manually undoing individual commits.
  - The class used the command-line Git branch model from the textbook chapter [Git branches](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html).

![Git review and branch/merge diagrams](git1.png)

- **Visualizing branch state**:
  - `git log --oneline --graph --decorate --all` shows commits, branch names, and remote references.
  - The `--all` flag is needed to see other local and remote branch names.
  - The Positron or VS Code Git tab shows a similar graph view of local and remote branches.

### 3. Creating, switching, and naming branches

- **Starting point before branching**:
  - Run `git status` to confirm the current branch.
  - For coordinated project work, first sync the starting branch, usually with `git pull origin main`.
  - This avoids starting a branch from a stale local state, especially when working across multiple computers.
- **Create and switch to a new branch**:
  - `git switch -c <branch-name>` creates a new branch and moves `HEAD` to it.
  - Example from class: `git switch -c dan-b1`.
  - After the command, `git status` shows the new branch name instead of `main`.
- **Switch to an existing branch**:
  - `git switch <branch-name>` moves `HEAD` to that branch.
  - The working files change to the state committed on that branch.
- **Branch naming**:
  - Branch names can be descriptive.
  - In group work, beginning a branch with a person’s name can make it clear who owns that branch.
- **Older and related commands**:
  - `git checkout` is an older command that moved `HEAD`; `git checkout -b <branch>` created and switched to a new branch.
  - `git branch` can create a branch but does not move `HEAD` to it.
  - `git switch -b` is not valid; the live demo produced an error.
  - If using AI-generated commands and unsure about `git checkout`, the instructor suggested asking for the `git switch` version instead.
- **Commits on a branch**:
  - The usual workflow is unchanged: edit files, check `git status`, inspect `git diff`, stage with `git add`, commit with `git commit`, and push when ready.
  - A new commit moves the current branch, not `main`, if the branch is currently checked out.

### 4. Pushing a branch and opening a pull request

- **Push the branch, not just `main`**:
  - Confirm which branch is currently checked out.
  - Use `git push origin <branch-name>`.
  - Example from class: `git push origin dan-b1`.
  - The first push creates the branch on GitHub and prints a URL for creating a pull request.
- **GitHub pull request entry points**:
  - After pushing a new branch, GitHub often shows a pop-up offering to compare and create a pull request.
  - If that pop-up disappears, go to the branch list, find the branch, and choose “New pull request.”
  - The instructor recommended opening the pull request early, even while work is unfinished, so the workflow is already in motion.
- **Pull request details**:
  - Check the source and base branches carefully.
  - In DSCI 522 the base branch is usually `main`, but in later courses the base may not always be `main`.
  - With forks or large open-source projects, the source/base line matters even more.
  - Give the pull request a title and description.
  - For simple project work, the title and description may be similar.
  - For more complex or AI-assisted work, the description may be long.
  - The first comment is important: later updates should often edit the first comment rather than appending disconnected notes.
- **Reviewing the files changed**:
  - The pull request shows the diff between the original and changed files.
  - Check that all intended files and code changes are present.
  - Check that unwanted files are not present, such as temporary checkpoint files, hidden backup files, or files that should be in `.gitignore`.
  - Examples mentioned: `.ipynb_checkpoints` and `.DS_Store`.
- **Live demo repository**:
  - The class worked in <https://github.com/chendaniely/2026-11-17-git>.
  - Pull request [#1 Learning about branches and PRs](https://github.com/chendaniely/2026-11-17-git/pull/1) came from branch `dan-b1`.
  - Pull request [#2 define fetch --prune](https://github.com/chendaniely/2026-11-17-git/pull/2) came from branch `dan-fetch`.
  - Pull request [#3 branch -d and -D](https://github.com/chendaniely/2026-11-17-git/pull/3) came from branch `dan-delete`.
- The pull request process follows the textbook chapter [Pull requests](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/github-pull-requests.html).

### 5. Code review and updating an open pull request

- **What code review looks like**:
  - Code review happens mainly in the “Files changed” tab of a pull request.
  - The reviewer sees the diff between the original file and the proposed file.
  - Inline comments or suggested changes can be added to specific lines.
- **Responsibility for changes**:
  - If it is your pull request, it is your job to make the requested changes.
  - A reviewer can comment, request changes, or explain what is wrong; the author must actually fix the code.
- **Updating a pull request**:
  - There is no need to close the pull request and create a new one for follow-up changes.
  - Switch back to the branch associated with the pull request.
  - Make the change, then `git add`, `git commit`, and `git push origin <branch-name>`.
  - The open pull request updates automatically with the new commits.
- **Outdated comments**:
  - If a line is changed after someone commented on it, GitHub may mark the comment as outdated or collapse it.
- **AI-assisted review**:
  - An AI tool such as Copilot can be asked to review a pull request.
  - Not every AI comment must be accepted; comments can be rejected, accepted, or responded to.
  - More eyes on the code are generally useful, but a person is still responsible for the review process.
- The code review concepts follow the textbook chapter [Code review on GitHub](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/github-code-review.html).

### 6. Draft pull requests

- **Purpose of a draft pull request**:
  - A draft pull request signals that the work is not ready for final review or merging.
  - It is useful for long-running features or when the author wants to start the pull request workflow early.
- **Converting to draft**:
  - Use the “Convert to draft” control on the pull request.
  - The pull request gets a gray visual state instead of the green open state.
  - The merge button is disabled, preventing accidental merging.
- **Returning to review**:
  - Use “Ready for review” to turn a draft back into an open pull request.
  - Draft pull requests can remain open for a long time as a signal that work is in progress.

### 7. Merging, pulling, and deleting branches

- **Merging on GitHub**:
  - After review, the pull request can be merged into the base branch, usually `main`.
  - Merging creates a merge commit in the repository history.
  - Deleting the branch afterward does not delete the commits; they remain in history through `main`.
- **Local `main` does not update automatically**:
  - After a pull request is merged on GitHub, the local `main` branch is still behind.
  - Switch to `main` and run `git pull origin main` to bring the merged work down.
- **Listing branches**:
  - `git branch -a` shows local and remote branches.
  - A star indicates the currently checked-out local branch.
  - Remote branches appear under `remotes/origin/...`.
- **Deleting the remote branch**:
  - After a pull request is merged, the branch can be deleted on GitHub.
  - This keeps the branch list from growing over the lifetime of a project.
  - Some compliance or workflow rules may require keeping branches, but for this class the instructor preferred cleaning up personal work.
- **Pruning remote-tracking branches locally**:
  - `git fetch --prune` synchronizes remote references and removes local references to branches that were deleted on the remote.
  - `git fetch` coordinates history without changing working files.
  - `git pull` is described as doing `git fetch` plus a merge.
- **Deleting a merged local branch**:
  - `git branch -d <branch-name>` deletes a local branch if it has been merged.
  - Use lowercase `d` for the safe case.
  - Capital `D`, as in `git branch -D <branch-name>`, force-deletes the branch and can delete unmerged work.
  - The instructor warned to be careful when copying force-delete commands from AI assistants.

### 8. Merge conflicts, rebase, and force pushing

- **Why merge conflicts happen with branches**:
  - Two branches can be created from `main` and edit the same lines.
  - If one branch is merged into `main` first, the other branch’s pull request may no longer merge cleanly.
  - GitHub rechecks open pull requests after `main` changes; a previously green pull request can later show a conflict.
  - Even when working in branches, conflicts can happen if teammates or agents edit the same region, for example by fixing the same typo.
- **What “fixing” a conflict means**:
  - It is not enough to remove the conflict markers.
  - The report or code must work from top to bottom.
  - A conflict on one line can affect variables or logic used later in the file.
- **Resolving conflicts in the GitHub web editor**:
  - Simple conflicts can be resolved directly on GitHub.
  - The user looks for the conflict markers, edits the file, and commits the resolution.
- **Resolving conflicts locally with rebase**:
  - The instructor’s preferred local method was `git rebase`.
  - The general workflow was:
    1. Make sure the merged work is on local `main`: `git switch main` and `git pull origin main`.
    2. Switch to the conflicting branch: `git switch <branch-name>`.
    3. Replay the branch’s commits onto `main`: `git rebase main`.
    4. Resolve the conflict in the editor.
    5. Stage the resolved file: `git add <file>`.
    6. Continue the rebase: `git rebase --continue`.
    7. Confirm or provide the commit message if Git asks for one.
  - If something goes wrong, `git rebase --abort` returns to the state before the rebase.
- **Why a force push is needed after rebase**:
  - Rebase rewrites the branch’s commit history.
  - A normal `git push origin <branch>` is not enough because the remote branch history no longer matches the local branch history.
  - The demo used `git push --force-with-lease origin <branch-name>`.
  - Force pushing a shared branch can overwrite remote work; use the lease form shown in class and be careful.
- **After force pushing**:
  - GitHub shows that the branch was force updated.
  - The pull request can then be merged normally.
  - After merging, the usual cleanup steps apply: delete remote and local branches as appropriate.
- The rebase-based conflict resolution follows the textbook section on [Git branches](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html).

![Multiple branches, pull requests, conflict, and rebase](git2.png)

## Commands from class

### Clone the demo repository and open it

```bash
cd ~/git
git clone git@github.com:chendaniely/2026-11-17-git.git
cd 2026-11-17-git
positron .
```

The repository was created for the lecture date. The instructor opened it in Positron and made a README change that added a link to the textbook Git branches chapter.

### Review the commit-and-push cycle on `main`

```bash
git status
git diff
git add README.md
git commit -m "intro and review"
git push origin main
git log --oneline --graph --decorate --all
```

This was the DSCI 521 workflow: inspect changes, stage them, commit them, push them, and view the decorated graph log.

### Create and commit on a new branch

```bash
git pull origin main          # sync before branching; already up to date
git switch -c dan-b1          # create branch dan-b1 and move HEAD to it
git status
git log --oneline --graph --decorate --all
git add README.md
git commit -m "define swtich -c"
git log --oneline --graph --decorate --all
```

The commit message contains the live typo `swtich`. The important point was that the new commit moved `dan-b1`, not `main`.

### Push the branch and start a pull request

```bash
git switch main
git push                      # on main: nothing to push
git switch dan-b1
git push origin dan-b1
git log --oneline --graph --decorate --all
```

The first push of the new branch printed a GitHub pull-request URL:

```text
remote:
remote: Create a pull request for 'dan-b1' on GitHub by visiting:
remote:      https://github.com/chendaniely/2026-11-17-git/pull/new/dan-b1
```

This showed how a newly pushed branch can be turned into a pull request.

### Add a second commit to the open pull request

```bash
git add README.md
git commit -m "show you the long git log command"
git push origin dan-b1
```

Because the pull request is tied to the branch, pushing another commit to the same branch updates the open pull request without closing and recreating it.

### Sync `main` after merging the pull request and clean up the branch

```bash
git switch main
git pull origin main
git branch -a
git log --oneline --graph --decorate --all
git fetch --prune
git log --oneline --graph --decorate --all
git branch -d dan-b1
```

After the pull request was merged on GitHub, local `main` still had to be pulled. `git fetch --prune` removed the local reference to `origin/dan-b1` after the remote branch was deleted:

```text
 - [deleted]         (none)     -> origin/dan-b1
```

The merged history looked like this:

```text
*   3851b00 (HEAD -> main, origin/main, origin/HEAD) Merge pull request #1 from chendaniely/dan-b1
|\
| * b90e441 (dan-b1) show you the long git log command
| * 4a14a64 define swtich -c
|/
* 145ff16 intro and review
* 1360d7f Initial commit
```

### Create two branches that will later conflict

```bash
git switch -c dan-fetch
git add README.md
git commit -m "define fetch --prune"
git push origin dan-fetch
git switch main

git switch -c dan-delete
git add README.md
git commit -m "branch -d and -D"
git push origin dan-delete
git log --oneline --graph --all --decorate
```

Both branches were based on `main` and edited the same general area of `README.md`. They produced two open pull requests that could conflict once one of them was merged.

### Sync `main` after one conflicting branch is merged, then rebase the other branch

```bash
git switch main
git pull origin main
git log --oneline --graph --all --decorate
git switch dan-delete
git rebase main
git status
git add README.md
git rebase --continue
git log --oneline --graph --all --decorate
```

The rebase stopped on a conflict:

```text
Auto-merging README.md
CONFLICT (content): Merge conflict in README.md
error: could not apply cb810d5... branch -d and -D
```

The instructor edited the conflict markers in the editor, staged the resolved file, and continued the rebase.

### Force-push the rebased branch

```bash
git push --force-with-lease origin dan-delete
```

Because the rebase rewrote the branch history, the remote branch had to be force updated:

```text
 + cb810d5...0e16503 dan-delete -> dan-delete (forced update)
```

After that, the pull request could be merged normally.

### What went wrong live

- **Typo in branch-creation flag**:
  - `git switch -b dan-delete` failed with `unknown switch 'b'`.
  - Fixed with `git switch -c dan-delete`.
- **Missing remote name in pull**:
  - `git pull main` failed with `fatal: 'main' does not appear to be a git repository`.
  - Fixed with `git pull origin main`.
- **Typo in force-push flag**:
  - `git push --force-with-leasse origin dan-delete` failed with `unknown option`.
  - Fixed with `git push --force-with-lease origin dan-delete`.

## Assignments

- [ ] Individual assignment 1: review merge conflicts. Due date not stated in this lecture; see the [student repository](https://github.com/UBC-MDS/DSCI_522_dsci-workflows_students).

---

- prompt: prompt-notes.md @ uncommitted
- prompt-hash: f78026c179ce
- model: qwen3.8-27b-sglang (requested: qwen3.8-27b-sglang)
- backend: local (SGLang)
- inputs: transcript-plaud.md, terminal.txt, materials.md
- generated: 2026-11-17
