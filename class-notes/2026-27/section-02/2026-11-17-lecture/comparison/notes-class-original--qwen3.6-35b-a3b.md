# Git Branches, Pull Requests, and Conflict Resolution

Date Time: 2026-11-17 09:30:00

Instructor: Daniel Chen

## Summary

The session reviewed foundational Git commands and introduced the branching and pull request workflows essential for collaborative data science projects. The instructor explained that while `main` represents the stable, integrated codebase, developers should use parallel branches to safely explore, test, and build new features without disrupting others. By committing changes to a dedicated branch and pushing it to GitHub, team members can initiate a review process through pull requests, allowing for structured code feedback before integration.

A significant portion of the lecture focused on the mechanics of GitHub pull requests, including how to create draft pull requests to signal incomplete work, navigate the "Files changed" tab for code review, and update a PR by pushing new commits to the same branch. The instructor emphasized that merging a pull request integrates the work into `main` and that the branch itself should be deleted afterward to keep the repository clean. The session concluded with a live demonstration of resolving merge conflicts locally using `git rebase`, highlighting how to replay commits on top of an updated remote branch, manually fix conflict markers, and safely force-push the rewritten history.

## Knowledge Points

### 1. Git Branches and HEAD

- **Branch**: A movable pointer to a commit. Creating a branch allows you to work in an isolated environment so that commits on `main` remain stable and ready for review.
- **HEAD**: The reference that points to your current working directory and active branch. Moving branches is fundamentally about moving the `HEAD` pointer.
- **`main` vs `origin/main`**: `main` tracks your local default branch. `origin/main` tracks what your local computer believes the remote GitHub repository's state is. They only stay synchronized when you push and pull.
- **Diagram reference**: `![Git local vs remote and branch structure](git1.png)` (Illustrates `clone`, `origin`, `main`, and branch `b1` with local laptop on the left and remote cloud on the right).

### 2. Creating and Switching Branches

- **`git switch -c <branch_name>`**: Creates a new branch and immediately switches `HEAD` to it. This is the modern, purpose-built replacement for older `checkout` workflows.
- **Branch naming conventions**: In group projects, it is standard to prefix branch names with your GitHub username (e.g., `dan-b1`) so teammates can identify ownership and know who to contact if issues arise.
- **Legacy commands**: `git checkout` historically handled branch switching but also performed revert/restore actions, which caused significant confusion. Modern Git splits these responsibilities into `git switch` and `git restore`. If AI tools or tutorials suggest `checkout` for branching, prompt them to use `switch` instead.

### 3. Pushing Branches and Pull Requests

- **`git push origin <branch_name>`**: Sends your local branch commits to the remote repository. GitHub typically displays a yellow banner prompting you to compare and create a pull request.
- **Draft Pull Requests**: Use the dropdown next to "Create pull request" to open a draft. This grays out the merge button, signaling to the team that the work is incomplete or in progress, and prevents accidental merges.
- **Code Review**: The "Files changed" tab shows the diff between the target branch and your branch. Reviewers add inline comments using the `+` button. The author is responsible for fixing flagged issues by pushing new commits to the same branch, which automatically updates the pull request without needing to close or recreate it.

### 4. Merging, Cleanup, and Local Sync

- **Merging**: When a PR is approved, clicking "Merge pull request" integrates the commits into `main` on GitHub and adds a merge commit to the history. The original branch commits remain in history and can be referenced later.
- **Remote cleanup**: Delete merged branches on GitHub via the repository's branches dropdown to prevent clutter.
- **`git fetch --prune`**: Synchronizes local tracking references with the remote. The `--prune` flag removes local references to branches that have been deleted on GitHub.
- **`git branch -d <branch_name>`**: Deletes a local branch that has already been merged. Git protects against accidental data loss by refusing to delete unmerged branches with lowercase `d`. Use uppercase `D` (`-D`) only when you are certain you want to permanently discard unmerged work.

### 5. Resolving Merge Conflicts with Rebase

- **Merge conflicts**: Occur when two branches modify the same lines in the same file. In a group project, even if you work on separate files, someone might edit a shared configuration or typo, causing conflicts when merging.
- **`git rebase main`**: Replays your local branch commits on top of the updated `main` branch. If conflicts arise, Git pauses and requires you to manually resolve them in your text editor.
- **Resolving workflow**: Open the conflicted file, remove conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`), keep the necessary code, run `git add <file>`, then execute `git rebase --continue` to proceed. The author must ensure the entire file works end-to-end after resolution, not just the conflicted lines.
- **Force pushing**: After a rebase, the commit history has been rewritten. You cannot use a standard `git push`; you must use `git push --force-with-lease` to update the remote branch. Be extremely careful with force pushes, as they overwrite remote history and can delete teammates' work if misused.
- **Diagram reference**: `![Rebase workflow showing conflict resolution](git2.png)` (Illustrates parallel branches, pull requests, and how rebase replays commits onto an updated main branch).

## Commands from class

### Review and initial setup

```bash
git clone git@github.com:chendaniely/2026-11-17-git.git       # Clone the demo repository
git status                                                    # Verify current branch and working tree state
git diff                                                      # Inspect unstaged changes before committing
git add README.md                                             # Stage changes
git commit -m "intro and review"                              # Commit changes locally
git push origin main                                          # Push local changes to the remote main branch
git log --oneline --graph --decorate --all                    # Visualize commit history and branch pointers
```

### Creating and switching branches

```bash
git switch -c dan-b1                                          # Create a new branch and switch to it
git log --oneline --graph --decorate --all                    # Verify HEAD now points to the new branch
git switch main                                               # Switch back to the main branch
```

### Pushing branches and creating pull requests

```bash
git switch dan-b1                                             # Switch to the branch you want to push
git push origin dan-b1                                        # Push the branch to GitHub
git push origin dan-fetch                                     # Push a second branch for demonstration
git push origin dan-delete                                    # Push a third branch to simulate parallel PRs
```

### Merging and local cleanup

```bash
git switch main                                               # Ensure you are on main before pulling
git pull origin main                                          # Sync local main with the remote after a PR merge
git fetch --prune                                             # Update remote refs and delete local tracking of deleted remote branches
git branch -a                                                 # List all local and remote branches
git branch -d dan-b1                                          # Delete the local branch that was already merged
git pull origin main                                          # Sync again after cleanup
```

### Resolving conflicts via rebase

```bash
git switch dan-delete                                         # Switch to the branch experiencing the conflict
git rebase main                                               # Replay commits onto the updated main; stops at conflict
git add README.md                                             # Mark the conflict as resolved after editing the file
git rebase --continue                                         # Apply the remaining commits
git push --force-with-lease origin dan-delete                 # Force update the remote branch with rewritten history
```

### What went wrong live

- **`git pull main`**: The instructor attempted `git pull main` without specifying the remote, resulting in a `fatal: 'main' does not appear to be a git repository` error. Fixed by running `git pull origin main`.
- **`git switch -b dan-delete`**: The instructor used the `-b` flag, which belongs to legacy `git checkout` commands. Git returned an `unknown switch 'b'` error. Fixed by using the modern `git switch -c dan-delete`.
- **`git push --force-with-leasse`**: A typo in the `--force-with-lease` flag caused an error. Fixed by correcting the spelling to `--force-with-lease`.

---

- prompt: prompt-notes.md @ uncommitted
- prompt-hash: f78026c179ce
- model: qwen3.6-35b-a3b (requested: qwen3.6-35b-a3b)
- backend: local (llama-swap)
- inputs: transcript-plaud.md, terminal.txt, materials.md
- generated: 2026-11-17
