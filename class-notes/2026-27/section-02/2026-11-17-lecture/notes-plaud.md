> Date Time: 2026-11-17 09:30:29  
>
> Location: [Insert Location]  
>
> Instructor: Daniel Chen

## Summary

The lectures introduce the group-project workflow for course 522 and review how Git supports collaboration through branches and pull requests (PRs). Students are expected to coordinate through the course GitHub repository, attend mandatory labs, understand their project code, and review teammates’ contributions. The Git workflow progresses from creating and switching between branches to pushing branch work to GitHub, opening and updating PRs, reviewing changes, merging approved work into `main`, and cleaning up branches. The lectures also cover merge conflicts, including how to resolve them locally with a rebase and update the remote branch afterward.

## Knowledge Points

### 1. Course 522 project coordination and expectations

* **Find your group in the course GitHub repository**
  - Locate your lab section in the GitHub lab-sections repository and use the group-number column to identify your group and teammates.
  - Group information is built from a main list of students’ GitHub usernames. Because this information is used elsewhere in the course setup, ensure your username is accurate.
* **Attend labs and coordinate group work**
  - Lab attendance is mandatory. Teaching assistants will visit every group, and students should be present when a TA meets with their group.
  - The first week of a project may involve coordination overhead. Work may not immediately divide into four independent streams, and some tasks may depend on one or two people. Aim to divide work into parallel, self-contained responsibilities as the project develops.
  - Shared work can create friction when teammates edit the same files or when one person pushes before another. Pulling teammates’ changes and coordinating contributions are part of the workflow. Well-separated work lets people make progress without being blocked by each other, then review and coordinate their work with the group.
* **Prepare for technical interviews**
  - An “interview week” column in the group information indicates when a student may be selected for an approximately seven-minute technical interview during lab. Interviews cover Git knowledge and the group-project codebase.
  - The interviews are intended to assess how well students understand their work; students are not expected to know everything. Students receive a grade, but it does not affect their course grade.
  - The schedule may shift by about a week if necessary. Some interviews may take the full seven minutes, while others may be shorter. The instructor mentioned that this format might become an exam format in a future year, but only as a possibility.

### 2. Git fundamentals and branches

* **Local and remote repositories**
  - Work takes place on a student’s computer and in the shared remote repository. Cloning brings the repository to a computer; commits record local changes; pushing sends commits to the remote; and pulling brings down work that teammates have committed and pushed.
  - The shared GitHub remote is the authoritative version for grading and publication. Code that exists only on a local computer is unavailable for grading or delivery.
  - In the course 521 shared-slide-deck exercise, students sometimes had to pull teammates’ changes before pushing their own. Similar friction can occur when people work on the same project area. Separating work into self-contained streams helps reduce these coordination issues.
* **Basic repository workflow**
  - The reviewed workflow includes creating a GitHub repository, bringing it to a computer, editing the README, checking the repository with `git status`, reviewing changes, staging files with `git add`, and committing them. The demonstration also added a link to the Git branches chapter.
  - A repository could be initialized with a README, a Python-related option, and a license. The demonstrated commit message was “Intro and review.”
  - These steps recap material practiced in course 521 over approximately the preceding ten weeks.
* **What branches are for**
  - `main` is the default branch and represents the stable, production-like version of a project. Its contents should work or be finished, although course work does not necessarily have to be fully finished to appear there.
  - Branches let people develop, test, or explore work separately from the shared main line. For example, cleaned data could remain in `main` as a common starting point while exploratory analysis and plots are developed on a separate branch.
  - Branches make it easier to set aside or abandon unsuccessful work without disentangling changes from the main project history. The instructor contrasted this with using `reset` or `revert`, which were covered in course 521.
  - Branches also support peer review: work can be developed separately, reviewed and tested, and then merged into the shared project. The instructor’s textbook example used branches for changes made during a class, avoiding disruptive updates while teaching was underway.
* **Branch references and `HEAD`**
  - `HEAD` points to the currently checked-out branch. When working on `main`, commits advance the local `main` reference; when working on another branch, commits advance that branch instead.
  - `origin/main` represents the remote state of `main` on GitHub as understood by the local computer. If commits are made locally on `main` but not pushed, local `main` moves ahead of `origin/main`.
  - Creating and switching to a branch does not create a commit or change project files. It changes the branch that `HEAD` points to. The existing `main` branch and remote references remain in place.
  - A local branch is not automatically synchronized with GitHub. The lecture example remained one commit behind the remote because nothing had been pushed, fetched, or synchronized.

### 3. Creating, using, and switching branches

* **Create a branch and switch to it**
  - Use `git switch -c <branch-name>` to create a branch and move `HEAD` to it. The `-c` option means create. Examples included `B1` and the local branch `Dan-B1`.
  - In group repositories, the instructor sometimes begins branch names with their own name so teammates know whom to contact about the work.
  - After switching, `git status` reports the new branch. Before creating a branch, check that you are on `main` and start from an up-to-date base when the work depends on coordinated project changes. Starting from outdated work can cause duplicated effort.
* **Continue the usual edit-and-commit workflow**
  - Branching does not change the normal workflow: edit a file, use `git status` to see what changed, and use `git diff` to review the changes.
  - If satisfied, stage the file—for example, with `git add README.md`—and commit it with a message. One example commit message was `define switch -c`.
  - The branch that is checked out is the one that advances when a commit is made.
* **Inspect branches and move between them**
  - Use `git switch <branch-name>` to move to an existing branch, such as `main`. Switching away does not move the branch being left; the working files change to match the branch that is now checked out.
  - A log view can show where `main`, remote references, and local branches point. The instructor noted that the `--all` option is needed to show branch names that might otherwise be absent. The demonstrated one-line log command was `git log --oneline --graph --decorate --all`.
  - VS Code and Positron display branch and commit relationships in a graph, corresponding to the relationships shown in the terminal. The example showed three commits, `origin/main`, local `main` at the same point, and a later commit on `Dan-B1`.
  - Branches are inexpensive to create and can be left in place if an experiment is unsuccessful. Switch back to `main` to continue other work, or create another branch. Successful work can later be merged into the main line.
* **Related Git commands**
  - `git checkout` was commonly used to switch branches before the newer `git switch` command. The instructor placed the transition to newer commands around 2019–2020, while noting uncertainty about the exact year.
  - The older branch-creation command is `git checkout -b <branch-name>`, equivalent to `git switch -c <branch-name>`. `checkout` also covered behaviors now associated with `revert` and `restore`, which remain available through `checkout`.
  - Tools such as GitHub Copilot or ChatGPT may suggest `checkout` commands. Understand a suggested command before running it, especially when work could be at risk; if unsure, ask for an equivalent using `switch`.
  - `git branch <branch-name>` creates a branch without switching to it. Use `git switch <branch-name>` or `git checkout <branch-name>` afterward to begin working on it.

### 4. Pushing branches and using pull requests

* **Push the branch containing your work**
  - Check which branch is active and switch to the branch you intend to share, for example, with `git switch dan-b1`. Switching changes the working files to the state committed on that branch.
  - Push the feature branch rather than `main`. The example was `git push origin dan-b1`: `origin` is the remote, and the branch name specifies what is being pushed.
  - After pushing, the log can show an `origin` reference for the feature branch at the same commit as the local branch, while `main` remains unchanged. On GitHub, use the branch selector to view the branch and confirm it is available for teammates to inspect. A branch being visible does not mean it has been reviewed or approved.
  - Branch lists can grow as projects add contributors, features, and projects. Branches can be deleted when they are no longer needed.
* **Create and configure a PR**
  - After pushing a branch, GitHub may show a **Compare and Pull Request** button. If the prompt disappears, find the branch under the repository’s branches tab and select **New pull request**.
  - The instructor recommends opening a PR early, even while work is in progress, so review can happen as changes are made. The initial prompt may disappear after roughly a day, but the branch menu remains another route.
  - Verify the base branch that will receive the changes and the source branch being compared. In this class, the destination is generally `main`; other courses or projects may differ. For forks or large open-source projects, confirm the intended repository and branch.
  - Write a clear title and description that briefly report what the branch changes. One example title was “Learning about branches and PRs,” with a description about `git switch` and creating PRs. Keep the original description current by editing it as the work changes, rather than adding disconnected updates that reviewers may miss.
* **Review changes and collaborate through the PR**
  - The PR displays changes between the feature branch and the base branch, including affected files, code, and commits. Check that all intended work is present; missing changes may not have been added, committed, or pushed.
  - Check for unnecessary files, such as temporary checkpoint files, Microsoft Word backup or fallback files, Jupyter Notebook `.ipynb_checkpoints`, and macOS `.DS_Store` files. Keep `.gitignore` appropriate; unwanted repository files can cost points in the class.
  - People with repository access can review the PR and discuss it in the conversation. The **Files Changed** tab shows a diff, and reviewers can comment on specific lines. Code review means examining that diff and commenting on the changes.
  - The PR author is responsible for making requested code changes; the reviewer identifies concerns or suggests changes. Review can happen locally or on GitHub. GitHub Copilot can also be asked to review work, but its suggestions can be considered, challenged, rejected, or acted on.
  - To address feedback or add work, return to the PR’s source branch, make changes, then add, commit, and push to that same branch. The existing PR updates with the new commits; there is no need to close it or create another one.
  - The example added a line about viewing Git history with `git log --oneline --graph --decorate --all`, staged the README with `git add README`, committed it, and pushed it. The instructor recommended pushing regularly, even about every 10 minutes, so work remains available for review. Refresh the PR page to see updates. If a changed line had a review comment, GitHub may collapse the comment and mark it outdated.
* **Use draft PRs for unfinished work**
  - An open PR can be converted to a draft with **Convert to Draft**. A draft displays a gray status bar rather than a green one, signals that the work is not ready to merge, and disables the merge control.
  - Drafts can remain open for extended work; the instructor mentioned drafts lasting three or four months. Draft status communicates the work’s state to the team and may discourage an agent from merging work automatically.

### 5. Merging pull requests and cleaning up branches

* **Review and merge completed work**
  - Change a draft PR to **Ready for review** when it is ready. Once the PR has been reviewed and its checks are green, merge it into the target branch, such as `main`.
  - The intended workflow is to develop work on a feature branch, review it through a PR, and merge approved commits into `main`. A merged PR is closed. The changes should then be present on `main`, and the commit history can confirm the branch commits and, depending on the merge method, a separate merge commit.
* **Synchronize local work after a merge**
  - Switching to local `main` does not automatically update it with changes merged on GitHub. Switch to `main` and run `git pull origin main` to bring the remote changes onto the local computer.
  - `git branch -a` lists branches known locally, including remote-tracking branches; an asterisk marks the current branch.
  - `git fetch --prune` updates the local view of remote history and removes remote-tracking references for branches deleted on GitHub. Use `git fetch` alone when you want to update your knowledge of remote history without changing local files.
  - `git pull` combines fetching with merging fetched changes into the current branch.
* **Delete branches carefully**
  - Deleting a branch after its work is merged can keep a long-running project’s branch list manageable. Deleting the branch marker does not delete the commits or remove the work from history; relevant commits remain available if the feature later needs to be undone.
  - Branch deletion depends on the team’s workflow and any compliance or record-retention requirements. Do not delete work that must be retained.
  - After pruning, use `git branch -d <branch-name>` to delete a merged local branch. Lowercase `-d` refuses to delete a branch Git believes contains unmerged work.
  - Uppercase `-D` force-deletes a branch even if it has not been merged. Use it cautiously, since it can remove a branch containing work you still need.
  - A branch can also be deleted on GitHub after merging, removing it from the remote branch list.

### 6. Merge conflicts and local rebase workflow

* **Understand how conflicts arise**
  - A merge conflict can occur when two branches based on the same starting point make different changes to the same line in the same file. The demonstration used two branches and PRs with conflicting edits around lines 12–14, including line 13.
  - When one PR is merged, `main` changes. GitHub then checks whether other open PRs can still be merged. A later PR may conflict even if it initially appeared mergeable and had green checks.
  - Conflicts can still occur when work is divided among contributors; another person or an agent might make a small edit in the same area, such as correcting a typo.
  - Resolve conflict markers (`<<<<<<<`, `=======`, and `>>>>>>>`) by choosing the correct final content and removing the markers. For report writing, the result should read as sensible English; for code, it must work from top to bottom. A conflict can have implications elsewhere in the file, such as a variable name used on another line, so check the broader result.
* **Resolve simple conflicts on GitHub or locally**
  - Simple conflicts can be resolved in GitHub’s web editor. More complex conflicts can be handled locally.
  - In the local rebase demonstration, one PR had already been merged into `main`, while another branch, named `DanDelete` in the example, remained open.
  - Update local `main` first with `git switch main` and `git pull origin main`. Then switch to the still-open branch, for example with `git switch dan-delete`, and run `git rebase main`. Rebase replays the branch’s commits on top of the updated `main`, bringing the conflict into the local working files.
  - Open the conflicted file, remove the markers, choose the correct content, and check the result. The example retained both definitions and cleaned up whitespace.
  - Use `git status` to inspect the repository state and Git’s suggested next steps. Stage the resolved file, for example with `git add README.md`, and run `git rebase --continue`. Git also provides an abort option if the rebase needs to be abandoned.
  - After the rebase completes, the branch’s commit appears at the top of the updated history with the conflict resolved.
* **Force-push a rebased branch**
  - Rebasing rewrites branch history by replaying commits onto a different base, so a normal push is not sufficient to update the remote branch.
  - Use a force push, such as `git push --force origin dan-delete`, to update the remote branch and its PR. GitHub indicates that a force push occurred.
  - Once updated, the PR can be merged if its checks and review allow it. Then synchronize and clean up branches as appropriate, while observing team and compliance requirements.

### 7. Course application

The group project will use branches and PRs over the coming weeks. Students should expect to create branches, open PRs, review and merge completed work, synchronize local `main`, and clean up branches where appropriate. Individual Assignment 1 includes another review of merge-conflict resolution. Students should be prepared to resolve conflicts and verify that the final report text or code works.

## Questions

- [Insert Question/Confusion]

## Assignments

- [ ] 1. Locate the course GitHub lab-sections repository, verify your lab section and group number, and ensure your GitHub username is accurate.
- [ ] 2. Attend mandatory lab sessions and be available when a TA visits your group.
- [ ] 3. Prepare to explain your Git practices and project codebase; review your group’s work in case you are selected for a technical interview.
- [ ] 4. Before coordinated project work, check that you are on `main` and synchronize relevant changes from the shared repository.
- [ ] 5. Practice creating a branch with `git switch -c <branch-name>`, checking the current branch with `git status`, and inspecting branch references with `git log --all`.
- [ ] 6. On a branch, practice reviewing changes with `git diff`, staging with `git add`, and committing with `git commit`; then switch to `main` and observe how the checked-out branch determines the file state.
- [ ] 7. When encountering commands such as `git checkout` in instructions or generated suggestions, understand what they do before running them; use `git switch` where appropriate.
- [ ] 8. For group-project work, push the branch containing your changes and create a PR targeting the correct base branch. Write a clear title and description, and use draft status if the work is not ready to merge.
- [ ] 9. Review PR diffs to confirm intended changes are present and unnecessary files are excluded. Check that `.gitignore` covers temporary or system-generated files.
- [ ] 10. Address review feedback by committing and pushing changes to the same branch so the existing PR updates.
- [ ] 11. Review merge-conflict resolution for Individual Assignment 1, including identifying conflict markers and ensuring the final text or code works.
- [ ] 12. When appropriate for the team workflow and compliance requirements, synchronize local `main`, prune stale remote references, and delete merged local and remote branches.
