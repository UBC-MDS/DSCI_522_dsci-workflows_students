# Git Branches, Pull Requests, Code Review and Resolving Conflicts with Rebase

Date Time: 2026-11-17 09:30:00

Instructor: Daniel Chen

## Summary

This was the first DSCI 522 lecture. It opened with course logistics: how to find your lab group, the rule that lab attendance is mandatory, and a new, ungraded "interview week" in which students talk through their own group project code and Git usage. The rest of the session reviewed the 521 Git basics (clone, add, commit, push, pull) and then moved on to what the group project needs: working in **branches** and bringing work into `main` through **pull requests (PRs)** and **code review** on GitHub.

Dan worked live in a fresh demo repository, [`chendaniely/2026-11-17-git`](https://github.com/chendaniely/2026-11-17-git). He created a branch with `git switch -c`, pushed it with `git push origin <branch>`, and opened a PR on GitHub. He then reviewed it in the "Files changed" tab, updated it by pushing more commits to the same branch, and showed how draft PRs work. After merging the PR, he showed the cleanup steps: delete the branch on GitHub, `git pull origin main`, `git fetch --prune`, and `git branch -d`. He also explained that `git checkout` is the older command that `git switch` partly replaces.

The session ended with a merge conflict between two branches. Both branches started from the same `main` and edited the same line of `README.md`. Once one PR was merged, the other could no longer merge cleanly. Dan fixed it locally with `git rebase main`, resolved the conflict, ran `git rebase --continue`, and pushed with `git push --force-with-lease`, because rebasing rewrites the branch's history. From now on, students are expected to work on the group project in parallel branches with PR review, and to be able to get themselves out of a merge conflict.

## Knowledge Points

### 1. Course logistics: lab groups and interviews

- **Lab groups**: A lab sections repository on UBC's GitHub lists each student by lab section. One column is your group number, and the list is sorted by group.
  - Your GitHub username is collected once and reused as metadata across the rest of the program. That is why it had to be submitted correctly.
- **Lab attendance is mandatory**: Because this is a group project course, TAs visit every group during lab. You must be present when the TA comes to your group.
- **Interview week**: Another column marks your interview week.
  - The interview is a short conversation of about seven minutes, run like a technical interview, about how you use Git and about your group project's code base.
  - You receive a grade, but it does not count toward your course grade. It is a trial run and may become the exam format next year.
  - Anything in your code base is fair game, including code written with AI. You are expected to know the code you work in, just as you would at a job.
  - If the TAs fall behind, your interview may move by about a week either way, and not everyone may be called.

### 2. Why branches

![Git review, branches and merging a pull request](git1.png)

- **Local vs remote**: Work happens in two places, your computer and GitHub (`origin`). With teammates, every person also has to coordinate with the same remote.
  - **What is on GitHub is what counts.** It is what gets graded and published. Work that exists only on your laptop effectively does not exist for the project.
- **`clone`** is a one-time command. **`push`** sends commits up to the remote. **`pull`** brings teammates' commits down.
- **The 521 friction**: In the 521 shared slide-deck exercise, you often could not push because someone else had pushed first, so you had to pull before pushing, even without a conflict. Some of that friction is unavoidable early in a project, because not all work can start in parallel. The goal is to reach the stage where each person owns a separate piece of work.
- **Parallel streams**: With branches, you work in "your own little world". You push and pull your branch freely, then your teammates review it. For example, everyone works Tuesday to Friday and the group reviews and merges on Friday.
- **`main`** is the default branch. Treat it as the stable, "production" version: the code on `main` should work.
  - Exploratory work, such as EDA plots, stays on a branch until it is ready. `main` holds the shared, agreed state, such as the cleaned dataset everyone builds on.
- **Branches are useful even when working alone**: They let you section off work. Dan did all of his textbook edits in branches so the published book would not change in the middle of a teaching day.
  - If an idea fails, switch back to `main` and delete the branch or leave it behind. This is much easier than undoing parts of a commit that did twenty things.
  - You could do the same with `git reset` and `git revert` from 521, but branches make it easier.

### 3. What a branch is: `HEAD`, `main`, `origin/main`

- **Branch**: A name that moves forward as you commit. Normally each commit advances `main`. On a branch, your commits advance the branch name instead (for example `dan-b1`), and `main` stays where it was.
- **`HEAD`**: Marks where you currently are. `HEAD -> main` in the log means you are on `main`. Committing drags along whichever branch `HEAD` is attached to.
- **`origin/main`**: What your computer *thinks* the state of `main` on GitHub is. If you commit without pushing, your local `main` (or branch) is ahead of `origin/main`.
- **Viewing the history**: Use `git log --oneline --graph --decorate --all`.
  - Without `--all`, you will not see your other branch names.
  - The Git graph view in VS Code and Positron shows the same picture. Hovering over it shows where `origin/main`, local `main` and your branch are.

### 4. Creating and moving between branches ([textbook ch. 8](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html))

- **Sync before branching**: Run `git status` to confirm you are on `main`, then `git pull origin main` so your starting point includes everything others have pushed. Dan has wasted time redoing work he had already done on another laptop because he skipped this step.
- **`git switch -c <name>`**: Creates a branch and moves `HEAD` to it. The only visible change is that `git status` now says `On branch <name>`. No commit is made.
- **`git switch <name>`**: Moves `HEAD` to an existing branch. The files in your working directory change to that branch's committed state.
  - This lets you look at a teammate's or an experiment's state locally.
- **Branch names**: Any name works for now; 524 adds more structure. In MDS repositories, Dan starts branch names with his own name so others know who to ask.
- **The add/commit cycle does not change on a branch**: `git status`, `git diff`, `git add`, and `git commit -m` work exactly as before.
- **`git checkout`**: The older command (pre-2019/2020) for moving `HEAD`. It also did file-restoring work that the newer commands from 521 now handle, and it still has all of that behaviour.
  - `git checkout -b <name>` is the old equivalent of `git switch -c <name>`.
  - Dan uses `checkout` himself and only uses `switch` when teaching.
  - ChatGPT and other AI tools may suggest `checkout`. If you do not know exactly what a command does, ask for the `switch` version, especially when you are worried about losing work.
- **`git branch <name>`**: Creates a branch but does **not** move you onto it. You still need `git switch` afterwards.

### 5. Pushing a branch and opening a pull request ([textbook ch. 9](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/github-pull-requests.html))

- **Pushing a branch**: First switch to the branch, then run `git push origin <branch>`.
  - This is why `git push origin main` has had its last word all along: it says *which* branch to push.
  - A plain `git push` from `main` does not push your other branch.
- **Seeing branches on GitHub**: Use the branch dropdown in the top-left, which shows `main` by default, to view any pushed branch's files. Use the branches button next to it to list all branches.
  - This is useful for checking that your work reached GitHub, or for reading a teammate's code before it is merged.
- **Pull request (merge request)**: The review process for bringing a branch into `main`. The easiest way to merge is through this process rather than on your laptop.
- **"Compare & pull request" banner**: GitHub shows it after you push a branch.
  - It disappears after a while, roughly a day.
  - If it is gone, go to the branches tab, open the menu next to your branch, and choose "New pull request".
  - Dan opens the PR right away, even with tiny changes, so the banner never becomes a problem.
- **Check the base and compare branches** at the top of the PR. You should see your branch being merged into `main`.
  - In this course the base is almost always `main`. In 524 it will not always be.
  - With forks of open source projects, check this line carefully so your code goes to the right place.
- **Title and description**: Describe what the branch changes. For small group-project PRs the title and description may be nearly the same. AI-agent-written PRs can come with "a novel".
- **Edit the first comment**: As the PR grows, keep the very first message up to date, because that is what people read. Do not add a trail of "now I'm also doing…" comments.
- **Review your own PR before creating it**: Scroll down to see every changed file.
  - Confirm that all the work you expected is there. If it is missing, you probably forgot to add, commit or push.
  - Confirm that **files that do not belong are absent**, such as `.ipynb_checkpoints`, `.DS_Store`, and Word backup or temporary files. **Points are taken off** for these even if not explicitly stated. Keep your `.gitignore` up to date.
  - This is your "second line of defence" after reviewing on your own computer. It also applies when an AI wrote the code: you can still review the AI's work this way.

### 6. Code review on GitHub ([textbook ch. 10](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/github-code-review.html))

- **Pull requests tab**: Once created, the PR is visible to everyone with access to the repository. The Conversation tab holds the discussion.
- **Files changed tab**: This is what "code review" means: reading the diff between the original and the new code.
  - Hover over a line and click the `+` to leave a comment on that line. For example: "why are you using switch and not checkout?"
- **The PR author fixes the code.** The reviewer's job is to say what needs changing. The author's job is to make the change.
- **Updating a PR**: Do **not** close it and open a new one. Go back to the same branch locally, then add, commit, and push to that branch. The PR updates automatically; you may need to refresh the page.
  - If you change a line that had a comment on it, GitHub collapses that comment as **outdated**.
- **AI review**: You can request a Copilot review. Its comments are suggestions: you can accept them, push back on them, or reject them. More eyes on the code is never a bad idea.
- **Draft pull requests**: Use "Convert to draft" in the top-right of the PR.
  - A draft PR shows a grey bar instead of a green one, and the merge button is greyed out, so nobody can merge it by accident.
  - Dan believes this also stops an agent from merging everything that is green.
  - Dan has kept draft PRs open for three or four months.
  - Click "Ready for review" at the bottom of the Conversation tab to turn it back into an open PR.

### 7. Merging and cleaning up

- **After merging**: The open PR count goes down by one. Clicking "Delete branch" on GitHub removes the branch name.
  - The commits are **not** lost. `main` gains a merge commit (`Merge pull request #1 from chendaniely/dan-b1`) and keeps the branch's commits, so you can still find and undo a feature later.
- **Why delete branches**: Over a project you create many branches. Without cleanup, the branch list becomes long and noisy.
  - Exception: if your workplace has compliance rules, do not delete anything. Follow your team's workflow.
- **Local `main` does not update itself.** Switch to `main` and run `git pull origin main`.
- **`git pull` = `git fetch` + `git merge`.** Run `git fetch` alone when you want to sync history without changing your files.
- **`git branch -a`**: Lists local branches (a `*` marks the current one) and remote-tracking branches (`remotes/origin/...`).
- **`git fetch --prune`**: Removes local `origin/<branch>` references for branches that were deleted on GitHub.
- **`git branch -d <name>`**: Deletes a local branch, but **only if it has been merged**. Git makes it harder to delete work you have not saved elsewhere.
  - ⚠️ **`git branch -D <name>` (capital D) force-deletes, even if the branch is unmerged.** That can permanently lose commits. It is a one-character difference. Be very careful when copying commands from ChatGPT, which may give you `-D`.
  - Use lowercase `-d` for now.

### 8. Merge conflicts between branches, fixed with rebase

![Several branches and pull requests at once, with a conflict, and how a rebase works](git2.png)

- **Branches do not prevent conflicts**: Someone (or an agent) may fix a typo in "your" section. If you fixed the same line, the merge will conflict. This is why Individual Assignment 1 has you practise merge conflicts again.
- **How the conflict appears**: Two PRs branch off the same `main` and edit the same line of the same file.
  - Each PR looks fine on its own. Nothing warns you in advance.
  - Once one PR is merged, `main` changes and GitHub rechecks every other PR targeting `main`. The second PR then reports a conflict.
- **Resolving on the web**: For simple conflicts, use GitHub's web editor. Find the `<<<<<<<`, `=======`, `>>>>>>>` markers and fix the text.
- **"Fixing" means the result works, not just that the markers are gone.**
  - For report prose, the remaining text must read as sensible English.
  - For code, it must run from top to bottom. A conflict on line 13 can break line 50, for example if a variable was renamed. That is still your problem to fix.
- **Resolving locally with rebase** (Dan's preferred way; people have opinions, and there are other approaches):
  1. Sync `main`: `git switch main`, then `git pull origin main`. This brings the already-merged commit onto your computer.
  2. Switch to the conflicting branch and run `git rebase main`. This **replays your branch's commits on top of the updated `main`**, which is where the conflict surfaces.
  3. Edit the file to resolve the conflict. In the demo, Dan kept both definitions and cleaned up whitespace.
  4. Let `git status` guide you: `git add <file>` marks the conflict as resolved, then run `git rebase --continue` and confirm the commit message.
  5. If you get scared or something goes wrong, `git rebase --abort` returns you to where you started.
- **Difference from 521**: In 521, `git pull origin main` triggered the conflict. Here, replaying commits onto another branch triggers it.
- **A rebased branch must be force-pushed.** Rebasing changes the branch's history: the commit's parent is now the new `main`. A normal push is rejected, and there is no way around force pushing.
  - Dan used `git push --force-with-lease`. The help text in the log describes it as "require old value of ref to be at this value": it only overwrites the remote branch if the remote is still where you last saw it.
  - The PR on GitHub then shows that a force push happened. Dan noted this is "somewhat of a compliance thing", because you have rewritten history.
  - After the force push, the PR's merge button works again. Merge it, then clean up as in section 7.

## Commands from class

### Clone the demo repo and review the 521 cycle

```bash
cd ~/git
git clone git@github.com:chendaniely/2026-11-17-git.git   # one-time copy of the remote
cd 2026-11-17-git
positron .                                     # open in Positron to edit README.md
git status
git diff                                       # inspect the README change
git add README.md
git commit -m "intro and review"
git push origin main
git log --oneline --graph --decorate --all     # --all shows every branch
```

### Sync, then create a branch

```bash
git status                     # confirm you are on main
git pull origin main           # start from an up-to-date main
git switch -c dan-b1           # create the branch and move HEAD to it
git status                     # "On branch dan-b1"
git log --oneline --graph --decorate --all
```

Right after creating the branch, the log shows only a new label. Every name points to the same commit:

```
* 145ff16 (HEAD -> dan-b1, origin/main, origin/HEAD, main) intro and review
```

### Commit on the branch, and move between branches

```bash
git diff
git add README.md
git commit -m "define swtich -c"
git log --oneline --graph --decorate --all   # dan-b1 is now one commit ahead of main
git switch main                              # files revert to main's state
git log --oneline --graph --decorate --all
git push                                     # from main: "Everything up-to-date" (does not push dan-b1)
git switch dan-b1
```

### Push the branch and open a PR

```bash
git push origin dan-b1     # last word is the branch name, not main
git log --oneline --graph --decorate --all
```

On the first push of a new branch, GitHub replies with a link for starting the pull request:

```
remote: Create a pull request for 'dan-b1' on GitHub by visiting:
remote:      https://github.com/chendaniely/2026-11-17-git/pull/new/dan-b1
```

This became PR [#1 Learning about branches and PRs](https://github.com/chendaniely/2026-11-17-git/pull/1).

### Update the open PR by pushing to the same branch

```bash
git diff                   # added the git log --oneline --graph --decorate --all line
git add README.md
git commit -m "show you the long git log command"
git push origin dan-b1     # the PR picks up the new commit automatically
```

### After merging PR #1 on GitHub: sync and clean up

```bash
git switch main
git pull origin main       # fast-forwards main to the merge commit
git branch -a              # local and remote-tracking branches
git fetch --prune          # drop origin/dan-b1, which was deleted on GitHub
git log --oneline --graph --decorate --all
git branch -d dan-b1       # lowercase -d: only deletes merged branches
git log --oneline --graph --decorate --all
```

```
 - [deleted]         (none)     -> origin/dan-b1
...
Deleted branch dan-b1 (was b90e441).
```

The merged history keeps the branch's commits under a merge commit:

```
*   3851b00 (HEAD -> main, origin/main, origin/HEAD) Merge pull request #1 from chendaniely/dan-b1
|\  
| * b90e441 show you the long git log command
| * 4a14a64 define swtich -c
|/  
* 145ff16 intro and review
```

### Set up two conflicting branches from the same `main`

```bash
git pull origin main
git switch -c dan-fetch
git status
git add README.md
git commit -m "define fetch --prune"
git push origin dan-fetch          # PR #2
git switch main                    # start the second branch from main, not from dan-fetch
git switch -c dan-delete
git status
git add README.md
git commit -m "branch -d and -D"   # edits the same README line as dan-fetch
git push origin dan-delete         # PR #3
git log --oneline --graph --all --decorate
```

The graph shows the split: two branches coming out of the same commit.

```
* cb810d5 (HEAD -> dan-delete, origin/dan-delete) branch -d and -D
| * 157c3cd (origin/dan-fetch, dan-fetch) define fetch --prune
|/  
*   3851b00 (origin/main, origin/HEAD, main) Merge pull request #1 from chendaniely/dan-b1
```

### Merge PR #2, then fix PR #3's conflict with rebase

```bash
git switch main
git pull origin main               # bring in the merged dan-fetch work
git log --oneline --graph --all --decorate
git switch dan-delete
git rebase main                    # replay dan-delete on top of main -> conflict
git status                         # tells you what to do next
# edit README.md: remove the conflict markers, keep both definitions
git add README.md                  # mark the conflict as resolved
git status                         # "all conflicts fixed: run git rebase --continue"
git rebase --continue
git status
git log --oneline --graph --all --decorate
git push --force-with-lease origin dan-delete   # history changed, so a force push is required
```

The conflict that `git rebase main` stopped on:

```
Auto-merging README.md
CONFLICT (content): Merge conflict in README.md
error: could not apply cb810d5... branch -d and -D
hint: Resolve all conflicts manually, mark them as resolved with
hint: "git add/rm <conflicted_files>", then run "git rebase --continue".
hint: You can instead skip this commit: run "git rebase --skip".
hint: To abort and get back to the state before "git rebase", run "git rebase --abort".
```

After `git rebase --continue`, the rebased commit (`0e16503`) sits on top of `main`. The old `cb810d5` remains only as `origin/dan-delete` until the force push:

```
* 0e16503 (HEAD -> dan-delete) branch -d and -D
*   3167d10 (origin/main, origin/HEAD, main) Merge pull request #2 from chendaniely/dan-fetch
...
 + cb810d5...0e16503 dan-delete -> dan-delete (forced update)
```

This branch became PR [#3 branch -d and -D](https://github.com/chendaniely/2026-11-17-git/pull/3).

### What went wrong live

- **`git pull main`**: Failed with `fatal: 'main' does not appear to be a git repository`. The first argument to `git pull` is the *remote*, so Git treated `main` as a remote name. Fixed with `git pull origin main`.
- **`git switch -b dan-delete`**: Failed with ``error: unknown switch `b'``. Dan mixed up `git checkout -b` with `git switch`. Fixed with `git switch -c dan-delete`.
- **`git push --force-with-leasse origin dan-delete`**: A typo, which failed with ``error: unknown option `force-with-leasse'``. Fixed by spelling it correctly: `git push --force-with-lease origin dan-delete`.

## Questions

- **Q:** A student asked about using `git checkout` instead of `git switch`.
  **A:** That's fine, and it won't be tested. `checkout` was the standard command before about 2019–2020, and Dan still uses it himself. It does more than move `HEAD`, which is why newer commands such as `switch` were split out of it. `git checkout -b` is the equivalent of `git switch -c`. If an AI tool suggests `checkout` and you don't know exactly what it will do, ask for the `switch` version instead, especially when you are worried about losing work.

## Assignments

- [ ] Individual Assignment 1, which includes reviewing merge conflicts again. No due date was given in class; check the [student repository](https://github.com/UBC-MDS/DSCI_522_dsci-workflows_students).
- [ ] Group project: over the next couple of weeks, start working in the branch → pull request → review workflow with your group.

---

- prompt: prompt-notes.md @ uncommitted
- prompt-hash: f78026c179ce
- model: claude-opus-5-5 (requested: opus)
- backend: claude
- inputs: transcript-plaud.md, terminal.txt, materials.md
- generated: 2026-11-17
