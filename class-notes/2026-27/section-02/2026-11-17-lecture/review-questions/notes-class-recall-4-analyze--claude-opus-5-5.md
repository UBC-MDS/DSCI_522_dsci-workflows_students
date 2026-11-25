# Git branches, pull requests and rebasing to fix conflicts: review questions, tier 4 — Analyze

Date: 2026-11-17

Instructor: Daniel Chen

*Tier 4 of 5: Analyze. Take each one apart yourself before you read the answer; tiers 1 to 3 cover the facts, reasons and steps it relies on.*

## 1. Why branches: escaping the 521 push/pull friction ([8 Git branches](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html))

*00:06:49–00:09:43*

- **Q:** Break down a group project's timeline as the class described it, from the 521 shared slide-deck exercise to a Friday review. Which phase brings back the "pull before you can push" friction, and how do branches change the Tuesday-to-Friday stretch?
    - **A:** Early in a project everyone is blocked on one or two people getting the basics in place. In that phase, work on the shared `main` brings back the 521 friction: you can't push because someone else pushed first, so you have to pull, whether or not there is a conflict. Later each person owns a self-contained part and works on their own branch. On that branch they can push and pull freely without caring what teammates are doing. Coordination moves to a single review point, for example a Friday review where the group goes over everyone's work and merges it. *(00:08:46)*

## 2. Review: the local–remote picture

*00:09:46–00:11:47*

- **Q:** Separate the commands in the 521 review cycle (`clone`, `add`/`commit`, `push`, `pull`) into those that act only on your computer and those that move commits between your laptop and GitHub. Then point out which side counts for grading, and why.
    - **A:** `git add` and `git commit` record work only on your computer. `clone` is a one-time command that brings the repository down from GitHub. `push` sends your commits up, and `pull` brings down commits that teammates pushed. The remote is what gets graded and published. Work that exists only on your laptop "effectively doesn't really exist" for grading or project purposes, like an unshipped product. *(00:11:33)*

## 3. What a branch is: `main`, `HEAD` and `origin/main` ([8 Git branches](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html))

*00:12:03–00:17:54*

- **Q:** Examine the labels in the log line `145ff16 (HEAD -> main, origin/main, origin/HEAD) intro and review` from the demo repository `2026-11-17-git`. What does each of `HEAD`, `main` and `origin/main` mark, what moves each one, and how does a branch change which label your commits drag along?
    - **A:** `HEAD` marks where you are; `HEAD -> main` means you're on `main`. Each `git commit` therefore moves `main` forward. `origin/main` is what your computer thinks the state of `main` on GitHub is. It moves only when you sync, so committing without pushing puts local `main` ahead of `origin/main`. A branch is a name you choose: with `HEAD` attached to it, your commits move that name instead of `main`, and the `git add`/`git commit` workflow itself doesn't change. *(00:13:30)*

## 4. Creating and switching branches ([8.1 Creating a branch using the command line](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#creating-a-branch-using-the-command-line))

*00:17:54–00:26:29*

- **Q:** Trace the `git log --oneline --graph --decorate --all` output through three steps: `git switch -c dan-b1`, then `git commit -m "define swtich -c"`, then `git switch main`. Which labels moved at each step, and which stayed put?
    - **A:** After `git switch -c dan-b1`, the log showed `145ff16 (HEAD -> dan-b1, origin/main, origin/HEAD, main)`. No commit was made; only `HEAD` moved onto a new name at the same commit. After the commit, `4a14a64 (HEAD -> dan-b1)` sat one commit ahead, while `main` and `origin/main` stayed at `145ff16`. After `git switch main`, `HEAD -> main` was back at `145ff16`, and `README.md` returned to `main`'s version. `dan-b1` stayed at `4a14a64`, because the branch you leave never moves. *(00:25:25)*

## 5. `git checkout` and `git branch` versus `git switch` ([8.1.3 Useful command line Git branching commands](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#useful-command-line-git-branching-commands))

*00:26:40–00:28:26*

- **Q:** Distinguish `git switch -c <name>`, `git checkout -b <name>` and `git branch <name>`. For each, say whether it creates a branch, whether it moves `HEAD` to it, and what else the command can do. Then relate this to the failed `git switch -b dan-delete` in the demo.
    - **A:** `git switch -c` creates a branch and moves `HEAD` to it. `git checkout -b` is the older, pre-2019/2020 equivalent. `checkout` also does much of what `restore` and `revert` now do, which is why the class advised asking an AI for the `switch` version when you don't know what a `checkout` command will do. `git branch <name>` only creates the branch, so you still need `switch` or `checkout` to move onto it. Mixing the two flags caused the demo error: `git switch -b dan-delete` failed with ``unknown switch `b'``, because `-b` belongs to `checkout`, and `git switch -c dan-delete` worked. *(00:28:13)*

## 6. Pushing a branch and viewing it on GitHub ([8.2 Useful things you can do with branches on GitHub](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#useful-things-you-can-do-with-branches-on-github))

*00:28:31–00:33:40*

- **Q:** Trace how the commit `4a14a64` got from the laptop to GitHub. Point out why a bare `git push` run on `main` printed `Everything up-to-date`, and which references changed, locally and on GitHub, after `git push origin dan-b1`.
    - **A:** The new commit lived on `dan-b1`, so pushing from `main` had nothing new to send. After `git switch dan-b1` and `git push origin dan-b1`, GitHub reported a `[new branch]` and printed a link to create a pull request. The log then showed `4a14a64 (HEAD -> dan-b1, origin/dan-b1)`, while `origin/main` stayed at `145ff16`. On GitHub, the repository's `main` view still showed only the first change. The pushed work was visible only through the branch dropdown at the top left. *(00:31:19)*

## 7. Opening a pull request ([9.1 Creating a pull request](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/github-pull-requests.html#creating-a-pull-request))

*00:33:40–00:41:16*

- **Q:** Break down the "open a pull request" page for `dan-b1` into the parts you should check before clicking "Create pull request", and say what problem each part catches.
    - **A:** The line at the top should name your branch and its target, `main` in this course. This catches sending code to the wrong branch, which matters in DSCI 524 and with forks. The title and first comment are the report of what changed. Edit that first comment as the pull request grows, because it is what people read. The changed-files list at the bottom is your second line of defence after reviewing locally. A missing file usually means you forgot to add, commit or push, and junk such as `.ipynb_checkpoints`, `.DS_Store` or Word backup files will lose you points even when the instructions don't mention them, so your `.gitignore` still matters. *(00:38:44)*

## 8. Code review and updating a pull request ([10 Code review on GitHub](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/github-code-review.html))

*00:41:16–00:45:41*

- **Q:** Separate the reviewer's job from the author's job in a GitHub code review. Then trace how the author's follow-up change reached pull request #1 without anyone opening a new pull request.
    - **A:** The reviewer reads the diff in the Files changed tab and adds comments with the `+` beside a line. Those comments also appear in the Conversation tab. The author's job is to fix the code. Here the author went back to `dan-b1` locally, ran `git add README.md` and `git commit -m "show you the long git log command"`, then `git push origin dan-b1` (`4a14a64..b90e441`). The pull request is tied to the branch, so the second commit appeared in #1, sometimes only after a refresh. A comment on a line that changed may then collapse as outdated. *(00:43:15)*

## 9. AI reviewers and draft pull requests ([9.2 Draft pull requests](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/github-pull-requests.html#draft-pull-requests))

*00:52:11–00:55:41*

- **Q:** Set a draft pull request and an open pull request side by side. How does each look, what can be done with its merge button, what does it tell the team, and how do you move between the two?
    - **A:** "Convert to Draft" at the top right turns an open pull request into a draft. The draft shows a grey bar instead of a green one, which tells everyone "you can look, but it's not ready." Its merge button is greyed out, so nobody can merge it by accident. Daniel believes this also stops an agent from merging everything that's green. "Ready for review" at the bottom ("this pull request is a work in progress") turns it back into an open pull request with green merge buttons. *(00:54:30)*

## 10. Merging and deleting the branch on GitHub ([8.2 Useful things you can do with branches on GitHub](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#useful-things-you-can-do-with-branches-on-github))

*00:55:41–00:59:07*

- **Q:** After pull request #1 was merged and "Delete branch" was clicked, separate what disappeared from what remained, on GitHub and in the history.
    - **A:** The open pull request count went down by one, and the branch count went from two to one, so the branch dropdown doesn't grow into a giant list. The commits were not deleted. `main`'s history shows the branch's two commits (`4a14a64`, `b90e441`) plus a merge commit, "Merge pull request #1 from chendaniely/dan-b1" (`3851b00`). Because those commits remain, a feature can still be found and undone later. The laptop still held `origin/dan-b1` and `dan-b1` until they were cleaned up locally. *(00:58:19)*

## 11. Syncing and cleaning up locally after a merge ([8.1.3 Useful command line Git branching commands](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#useful-command-line-git-branching-commands))

*00:59:07–01:03:51*

- **Q:** Break down the local cleanup after #1 was merged: `git pull origin main`, `git branch -a`, `git fetch --prune` and `git branch -d dan-b1`. Which of these changed files on disk, and which changed only branch references?
    - **A:** `git pull origin main` fast-forwarded `main` from `145ff16` to `3851b00` and added 6 lines to `README.md`, so it was the only step that changed files. `git branch -a` changed nothing; it showed `dan-b1`, `* main` and the stale `remotes/origin/dan-b1`. `git fetch --prune` synced history without touching files and printed `[deleted] (none) -> origin/dan-b1`. That is the difference from `git pull`, which is a fetch followed by a merge. `git branch -d dan-b1` printed `Deleted branch dan-b1 (was b90e441)`, and the log then showed `b90e441` with no label, so the commit stayed in history. *(01:02:22)*

- **Q:** Distinguish `git branch -d` from `git branch -D`: what does each check before deleting? Then point out where in a branch workflow a pasted `-D` does damage, and what it destroys.
    - **A:** Lowercase `-d` deletes a local branch only if it has been merged. It worked on `dan-b1` because #1 was already in `main`. Capital `-D` force-deletes even an unmerged branch. That bites on a branch you're still working on, or one you abandoned before merging: its commits were never in `main`, so the work is lost. The class warned that this is a one-character difference, and that ChatGPT may hand you `-D` when you copy commands. *(01:03:21)*

## 12. Setting up two conflicting pull requests ([8.3 What happens when my feature branch falls behind main?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#what-happens-when-my-feature-branch-falls-behind-main))

*01:04:00–01:10:00*

- **Q:** Examine the log in which `cb810d5 (dan-delete)` and `157c3cd (dan-fetch)` both leave `3851b00`. Deduce which setup steps made pull requests #2 and #3 conflict, and why neither pull request warned of it on its own.
    - **A:** Both branches were created from the same `main` commit, `3851b00`. `dan-fetch` was pushed as #2 but deliberately not merged, which is what lets you practise a conflict on your own. Switching back to `main` before `git switch -c dan-delete` meant the fetch line wasn't in that branch's `README.md`. Both commits then added text at the same spot in `README.md`, around line 13, which is the condition for a conflict. Each pull request is compared only against the current `main`, so both looked mergeable until one of them changed `main`. *(01:09:28)*

## 13. When a merge creates the conflict: resolving on GitHub ([8.3 What happens when my feature branch falls behind main?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#what-happens-when-my-feature-branch-falls-behind-main))

*01:10:00–01:12:44*

- **Q:** Trace how merging #2 turned #3 into a conflict. Then distinguish what "fixed" means for the report's prose and for code, and point out where a fix that only removes the markers fails.
    - **A:** Merging #2 changed `main`, and GitHub rechecks every pull request targeting `main`, so #3 landed on the conflict page. There you can resolve it in the web editor by finding the `<<<<<<<`, `=======` and `>>>>>>>` markers. For prose, "fixed" means the remaining text is English that makes sense. For code, it means the code runs from top to bottom again. A change made at line 13, such as renaming a variable, can break line 50, and the class warned that this is still your problem even though Git only flagged line 13. *(01:11:39)*

## 14. Resolving the conflict locally with rebase ([8.3.2 Using rebase](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#using-rebase))

*01:12:44–01:20:42*

- **Q:** Follow `dan-delete`'s commit through the rebase by its hashes: what was its parent before and after, what did `origin/dan-delete` point to at each stage, and why did the final push need `--force-with-lease`?
    - **A:** Before, `cb810d5` sat on `3851b00`. `git pull origin main` brought local `main` to `3167d10`, the merge of #2 that contains `157c3cd`. `git rebase main` replayed the commit on top of `3167d10`, and after the conflict was fixed it became the new commit `0e16503`. `origin/dan-delete` still pointed at the old `cb810d5`. Because the branch's history had changed, a plain push could not update it, and `git push --force-with-lease origin dan-delete` printed `+ cb810d5...0e16503 dan-delete -> dan-delete (forced update)`. GitHub records that force push ("you've mangled history"), which matters in compliance settings. *(01:19:47)*

- **Q:** Break down the stop-and-continue sequence of `git rebase main` on `dan-delete`, step by step, as `git status` guided it. Relate it to how the same conflict was triggered in 521.
    - **A:** `git rebase main` stopped with `CONFLICT (content): Merge conflict in README.md`. `git status` then reported a rebase in progress onto `3167d10`, listed `README.md` as `both modified`, and offered `--continue`, `--skip` and `--abort`; `--abort` is the escape hatch if something goes wrong. After the markers were fixed in the editor, keeping both definitions, `git add README.md` marked the file resolved, and `git status` said "all conflicts fixed: run git rebase --continue". `git rebase --continue` confirmed the commit message and finished. Fixing the markers is the same skill as week 3 of 521; only the trigger differs: there it was `git pull origin main`, here it is replaying commits onto another branch. *(01:18:20)*

---

- prompt: prompt-recall-4-analyze.md @ 65eb21c
- prompt-hash: 7dde50dd5ebf
- model: claude-opus-5-5 (requested: opus)
- backend: claude
- inputs: transcript-plaud.md, terminal.txt, materials.md, notes-class-main--claude-opus-5-5.md
- generated: 2026-11-23
- notes-input: notes-class-main--claude-opus-5-5.md @ d979d4ea6828, links and section references removed
