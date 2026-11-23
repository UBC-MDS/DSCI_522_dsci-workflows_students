# Git branches, pull requests and rebasing to fix conflicts: review questions, tier 4 — Analyze

Date: 2026-11-17

Instructor: Daniel Chen

*Tier 4 of 5: Analyze. Take each one apart yourself before you read the answer; tiers 1 to 3 cover the facts, reasons and steps it relies on.*

## 1. Git recap: setting up the demo repository

*00:04:07–00:06:49*

- **Q:** Break down the review cycle Daniel ran on `README.md` in `2026-11-17-git`: `git status`, `git diff`, `git add README.md`, `git commit -m "intro and review"`, `git push origin main`. What does each step contribute, and which is the only one that touches GitHub?
  **A:** `git status` reported that `README.md` was modified but not staged. `git diff` showed the actual lines added: the review sentence and the Git branches link. `git add` staged the file, and `git commit` recorded it as commit `145ff16` in the local history only. `git push origin main` is the only step that reached GitHub; it moved the remote from `1360d7f` to `145ff16`. The log then showed `HEAD -> main` and `origin/main` on the same commit. *(00:06:13)*

## 2. Why branches: escaping the 521 push/pull friction

*00:06:49–00:09:43*

- **Q:** Separate the phases of a group project as Daniel described them. Where does the 521 "pull before you can push" friction come from, which phase can't avoid it, and how do branches change the later phase?
  **A:** The friction arises when two people push to the same place: even without a conflict, one of them has to pull first before pushing again. Early in a project, the work is blocked on one or two people setting up the basics, so that friction will exist somewhere no matter what. Later, each person owns a self-contained part. On their own branch, they can push and pull from Tuesday to Friday without caring what others do. Coordination is then moved to a review point, such as Friday, when the group reviews and merges the work. *(00:08:46)*

## 3. Review: the local–remote picture

*00:09:46–00:11:47*

- **Q:** Take the 521 local–remote diagram apart. Which of `clone`, commit, `push` and `pull` happen on your computer and which move work between your computer and GitHub? Which side counts for grading, and how do teammates fit in?
  **A:** A commit happens only on your computer. `clone` is a one-time command that brings the repository down. `push` sends your commits up to the remote, and `pull` brings down commits that teammates pushed. Each teammate's computer coordinates with that same GitHub remote. The remote is "the thing that matters": it is what gets graded and published. Work that exists only on your laptop "effectively doesn't really exist" for grading or project purposes. *(00:11:19)*

## 4. What a branch is: `main`, `HEAD` and `origin/main` ([8 Git branches](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html))

*00:12:03–00:17:54*

- **Q:** Distinguish the three labels in `git log --oneline --graph --decorate --all`: `HEAD`, `main` (or a branch name such as `b1`), and `origin/main`. What does each represent, and what makes each one move?
  **A:** `HEAD` marks where you are. It is attached to a branch, and a commit moves whichever branch `HEAD` is attached to. `main` is the default branch. A branch like `b1` is a name you choose, and it moves instead of `main` when `HEAD` is on it; the `git add`/`git commit` workflow itself is unchanged. `origin/main` is what your computer thinks the state of GitHub is. It does not move when you commit, so if you commit on `main` without pushing, local `main` gets ahead of `origin/main`. *(00:13:30)*

## 5. Creating and switching branches ([8.1 Creating a branch using the command line](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#creating-a-branch-using-the-command-line))

*00:17:54–00:26:29*

- **Q:** Trace `dan-b1` through three snapshots of `git log --oneline --graph --decorate --all`: right after `git switch -c dan-b1`, after `git commit -m "define swtich -c"`, and after `git switch main`. What moves at each step, and what stays put?
  **A:** After `git switch -c dan-b1`, no new commit existed. `HEAD -> dan-b1` sat on `145ff16` alongside `main` and `origin/main`, so only a word had changed. After the commit, `HEAD -> dan-b1` moved to the new commit `4a14a64`, while `main` and `origin/main` stayed on `145ff16`. After `git switch main`, `HEAD` moved back to `main` and `README.md` on disk returned to `main`'s version. `dan-b1` stayed on `4a14a64`, which is why the branch you left "never moved anywhere". *(00:22:58)*

## 6. `git checkout` and `git branch` versus `git switch` ([8.1.3 Useful command line Git branching commands](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#useful-command-line-git-branching-commands))

*00:26:40–00:28:26*

- **Q:** Set `git switch -c <name>`, `git checkout -b <name>` and `git branch <name>` side by side. What does each create and move, and what did the failed `git switch -b dan-delete` in class reveal about mixing them up?
  **A:** `git switch -c` creates a branch and moves `HEAD` to it. `git checkout -b` is the older command that does the same thing; `checkout` also does much of what `restore` and `revert` now do. `git branch <name>` only creates the branch without moving you, so you still need `switch` or `checkout` afterwards. In class, `git switch -b dan-delete` failed with ``error: unknown switch `b'``, because `-b` belongs to `checkout`. The fix was `git switch -c dan-delete`. *(00:28:13)*

## 7. Pushing a branch and viewing it on GitHub ([8.2 Useful things you can do with branches on GitHub](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#useful-things-you-can-do-with-branches-on-github))

*00:28:31–00:33:40*

- **Q:** Break down how the `dan-b1` commit reached GitHub. Why did the bare `git push` on `main` send nothing? What changed in the log after `git push origin dan-b1`, and where on GitHub did the work show up and not show up?
  **A:** On `main`, a bare `git push` printed `Everything up-to-date`, because the new commit lived on `dan-b1` and not on `main`. After `git switch dan-b1`, running `git push origin dan-b1` created the new branch on GitHub; the last word names what you push. The log then showed `origin/dan-b1` beside `dan-b1`, while `origin/main` had not moved. On GitHub the repository's main view still showed only `main`'s content. The work was visible only through the branch dropdown at the top left or the branches list. *(00:30:36)*

## 8. Opening a pull request ([9.1 Creating a pull request](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/github-pull-requests.html#creating-a-pull-request))

*00:33:40–00:41:16*

- **Q:** Break the "Compare & pull request" page down into its parts: the branch line at the top, the title and description, and the file list at the bottom. What should you check in each, and which check can cost points?
  **A:** The top line should name your branch and the branch it merges into, which is `main` in this course. That will not always be true in 524 or with forks. The title and description are a report of what changed and why, and later changes belong in an edit to that first comment. The file list shows every change relative to `main`. If a file you worked on is missing, you probably forgot to add, commit or push it. The file list is also your "second line of defence" against files that don't belong, such as `.ipynb_checkpoints`, `.DS_Store` or Word backup files. Points are taken off for those even when the instructions don't say so explicitly, which is why `.gitignore` still matters. *(00:38:44)*

## 9. Code review and updating a pull request ([10 Code review on GitHub](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/github-code-review.html))

*00:41:16–00:45:41*

- **Q:** Trace the second commit on pull request #1, from the local edit to GitHub. What did Daniel run, how did the pull request change, and what happens to a review comment on a line you then edit?
  **A:** On `dan-b1`, he added the `git log --oneline --graph --decorate --all` line to `README.md`. He then ran `git add README.md`, `git commit -m "show you the long git log command"` (commit `b90e441`) and `git push origin dan-b1`. The push moved the remote branch from `4a14a64` to `b90e441`. The pull request is tied to the branch, so #1 showed the second commit, sometimes only after a page refresh, without closing it or opening a new one. A comment on a line you changed may be auto-collapsed as outdated, because it no longer applies. *(00:44:43)*

## 10. AI reviewers and draft pull requests ([9.2 Draft pull requests](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/github-pull-requests.html#draft-pull-requests))

*00:52:11–00:55:41*

- **Q:** Set a draft pull request and an open pull request side by side. How do they look, what can be done with the merge button, what does each signal to teammates and agents, and how do you move between them?
  **A:** "Convert to draft" at the top right turns an open pull request into a draft. A draft shows a grey bar instead of a green one, and its merge button is greyed out, so nobody can accidentally merge it. Daniel believes this also stops an agent from merging everything that's green. A draft signals "you can look, but it's not ready". Daniel has kept drafts open for three or four months on long work. At the bottom of the page, "Ready for review" turns the draft back into an open pull request with green merge buttons. *(00:54:30)*

## 11. Merging and deleting the branch on GitHub ([8.2 Useful things you can do with branches on GitHub](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#useful-things-you-can-do-with-branches-on-github))

*00:55:41–00:59:07*

- **Q:** Separate what merging #1 and then clicking "Delete branch" removed on GitHub from what it kept. What happened to the counters, the branch list and `main`'s history?
  **A:** Merging closed #1, so the open pull request counter went down by one. Deleting the branch took the branch count from two to one, which keeps the dropdown from growing into a giant list. Only the branch label was removed. `main`'s history now holds `dan-b1`'s two commits plus a merge commit, "Merge pull request #1 from chendaniely/dan-b1". You can still find the pull request's commits and undo the feature later, so "nothing's really lost". *(00:58:10)*

## 12. Syncing and cleaning up locally after a merge ([8.1.3 Useful command line Git branching commands](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#useful-command-line-git-branching-commands))

*00:59:07–01:03:51*

- **Q:** Break down the local cleanup after #1 was merged and `dan-b1` was deleted on GitHub: `git pull origin main`, `git branch -a`, `git fetch --prune`, `git branch -d dan-b1`. What does each one change or reveal on your computer?
  **A:** Local `main` doesn't update itself. `git pull origin main` fast-forwarded it from `145ff16` to `3851b00`, adding the 6 merged lines to `README.md`. `git branch -a` revealed that the computer still knew about the local `dan-b1` and `remotes/origin/dan-b1`. `git fetch --prune` syncs history without changing your files (`git pull` is fetch plus merge). It also removed the stale reference, printing `[deleted] (none) -> origin/dan-b1`. Finally, `git branch -d dan-b1` deleted the local label (`was b90e441`), while the commits stayed in the log. *(01:02:22)*

- **Q:** Examine the one-character difference between `git branch -d` and `git branch -D` at the end of this cleanup. When does each one succeed, and what is at stake afterwards if you use the wrong one?
  **A:** Lowercase `-d` deletes a local branch only if it has been merged, as `dan-b1` had been. For an unmerged experiment, it refuses, because deleting it would lose work. Capital `-D` force-deletes the branch regardless, so it can throw away commits you are still working on. Daniel warned that it is a very small change, and that ChatGPT may hand you the capital `-D` "force delete". That is why he said to use lowercase `-d` for now. *(01:03:21)*

## 13. Setting up two conflicting pull requests ([8.3 What happens when my feature branch falls behind main?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#what-happens-when-my-feature-branch-falls-behind-main))

*01:04:00–01:10:00*

- **Q:** Deduce how `dan-fetch` and `dan-delete` were set up to conflict. Where did each start, what did each change, which step was the key to the setup, and why didn't GitHub warn about the conflict at first?
  **A:** After `git pull origin main`, both branches started from the same `main` commit, `3851b00`. `dan-fetch` added the `fetch --prune` definition (commit `157c3cd`, pull request #2). Daniel then switched back to `main`, so that line wasn't in the file, and `dan-delete` added the `-d`/`-D` definitions at the same spot in `README.md` (commit `cb810d5`, pull request #3). The key was not merging #2 right away. The log showed two lines leaving one commit. On GitHub, each pull request on its own looked mergeable into `main`, even though both edited the same line. *(01:09:28)*

## 14. When a merge creates the conflict: resolving on GitHub

*01:10:00–01:12:44*

- **Q:** Trace how merging #2 caused the conflict on #3. Then break "fixing it" into what it means for report prose and what it means for code.
  **A:** Merging one pull request changes `main`. Every other pull request into `main` is then rechecked, so #3, which had looked green, showed a conflict. A simple conflict can be fixed in GitHub's web editor by finding the `<<<<<<<`, `=======` and `>>>>>>>` markers. For report prose, the remaining text must be English that makes sense. For code, removing the markers isn't enough: the code must run from top to bottom again. A conflict on line 13 can affect line 50, for example through a renamed variable, and that is still your problem. *(01:11:39)*

## 15. Resolving the conflict locally with rebase ([8.3.2 Using rebase](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#using-rebase))

*01:12:44–01:20:42*

- **Q:** Break down Daniel's local fix for `dan-delete` into its steps. What did each command do or print, and how does the trigger for the conflict differ from the one you met in 521?
  **A:** `git switch main` and `git pull origin main` brought in the merge of #2, fast-forwarding `main` to `3167d10`. `git switch dan-delete` and `git rebase main` then replayed `cb810d5` on top of that `main` and stopped with `CONFLICT (content): Merge conflict in README.md`. In 521, `git pull origin main` triggered the conflict; here it is the replay. Daniel fixed the markers in his editor by keeping both definitions. `git status` then guided him: `git add README.md` marked the conflict resolved, and `git rebase --continue` finished with "Successfully rebased". `git rebase --abort` was available as the escape hatch. *(01:17:08)*

- **Q:** Examine why the rebased `dan-delete` could not be pushed normally. What changed in its history, what did the log and the push output show, and what does the forced update leave behind on GitHub?
  **A:** Before the rebase, the branch's commit was `cb810d5`, whose parent was `3851b00`. After the rebase, it was a new commit, `0e16503`, sitting on `3167d10`. The log still showed `origin/dan-delete` on the old `cb810d5`. Because the history had changed, a simple push won't work: Daniel had to run `git push --force-with-lease origin dan-delete`, which printed `+ cb810d5...0e16503 dan-delete -> dan-delete (forced update)`. You can't get around force-pushing after a rebase, and GitHub records that the force push happened. As Daniel put it, "you've mangled history", which matters in compliance settings. *(01:19:47)*

---

- prompt: prompt-recall-4-analyze.md @ 8bcc190
- prompt-hash: ccb0e5a939c5
- model: claude-opus-5-5 (requested: opus)
- backend: claude
- inputs: transcript-plaud.md, terminal.txt, materials.md, notes-class-main--claude-opus-5-5.md
- generated: 2026-11-20
- notes-input: notes-class-main--claude-opus-5-5.md @ d979d4ea6828, links and section references removed
