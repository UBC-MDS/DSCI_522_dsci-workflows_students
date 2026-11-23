# Git branches, pull requests and rebasing to fix conflicts: review questions, tier 3 — Apply

Date: 2026-11-17

Instructor: Daniel Chen

*Tier 3 of 5: Apply. Work each situation through before you read the answer; tiers 1 (Remember) and 2 (Understand) cover the facts and reasons it relies on.*

## 1. Review: the local–remote picture

*00:09:46–00:11:47*

- **Q:** Your part of the group analysis is committed on your laptop but never pushed. The milestone is graded tonight. Predict what the graders see, and say what you must run.
  **A:** They see nothing of your work. Whatever is on GitHub is what gets graded and published, and work that exists only on your local computer "effectively doesn't really exist." You must push the commits to the remote. *(00:10:53)*

- **Q:** You cloned your group's repository yesterday. Today you want to keep working in it. Do you run `git clone` again?
  **A:** No. Clone is a one-time command that brings the repository down to your computer. From then on you sync with `push` and `pull`. *(00:11:25)*

- **Q:** A teammate tells you they just pushed a commit you need. Which direction does the work have to move, and which command moves it?
  **A:** The commit is on the remote and has to come down to your computer, so you `pull` it. `push` only sends your own commits up. *(00:11:47)*

## 2. What a branch is: `main`, `HEAD` and `origin/main` ([8 Git branches](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html))

*00:12:03–00:17:54*

- **Q:** You are on `main`. You make two commits but don't push, then run `git log --oneline --graph --decorate --all`. Predict where `main` and `origin/main` sit.
  **A:** `HEAD -> main` sits two commits ahead of `origin/main`. `origin/main` is what your computer thinks GitHub's state is, and it doesn't move until you sync with GitHub. *(00:13:39)*

- **Q:** You run `git switch -c dan-b1` and then `git add` and `git commit` a change. Which branch label moves forward, and which stays put?
  **A:** `dan-b1` moves forward with `HEAD`, and `main` stays where it was. The add and commit workflow is unchanged. The only difference is that your commits now drag your branch along instead of `main`. *(00:14:25)*

- **Q:** Your group has a cleaned dataset that everyone builds on. You are halfway through exploratory plots that don't work yet. Where should each one live?
  **A:** The cleaned dataset belongs on `main`, which should be the stable version where at least the code works. Your unfinished EDA stays on your own branch until it is ready. *(00:15:24)*

- **Q:** You tried an idea on its own branch, and none of it worked. Choose the easiest way back to your starting point, and say why it beats having made one big commit on `main`.
  **A:** Switch back to `main`, and delete the branch or just leave it behind. Undoing one commit that did twenty things would mean digging through the history and copying back the relevant bits. `git reset` and `git revert` also work, but a branch makes the undo easier. *(00:17:22)*

## 3. Creating and switching branches ([8.1 Creating a branch using the command line](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#creating-a-branch-using-the-command-line))

*00:17:54–00:26:29*

- **Q:** You are about to start your own part of the group project, and teammates have pushed work since you last synced. In order, what do you run before your first commit on a new branch?
  **A:** Run `git status` to confirm you are on `main`, then `git pull origin main`, then `git switch -c <name>`. Pulling first means your branch starts from everything the team has already pushed. Otherwise you may redo work that already exists. *(00:18:39)*

- **Q:** In the demo repository, you run `git switch -c dan-b1` and then `git log --oneline --graph --decorate --all` before editing anything. Predict the output.
  **A:** The top commit shows `HEAD -> dan-b1` alongside `main` and `origin/main`, all on the same commit. No new commit was made. Only the name `HEAD` is attached to has changed, and `git status` now says `On branch dan-b1`. *(00:21:15)*

- **Q:** You run `git log --oneline`, but your branch `dan-b1` doesn't appear. What do you add to the command?
  **A:** Add the `--all` flag, as in `git log --oneline --graph --decorate --all`. Without it, you may not see your other branch names. *(00:25:38)*

- **Q:** You commit a new line to `README.md` on `dan-b1`, then run `git switch main` and open `README.md`. What do you see?
  **A:** The new line is gone. The file shows `main`'s version, because switching moves `HEAD` and your files follow it. `dan-b1` stays where you left it, and switching back brings the line back. *(00:25:46)*

- **Q:** You are creating a branch in a repository you share with others. Choose a naming convention that helps your teammates.
  **A:** Start the branch name with your own name, such as `dan-b1`. Then anyone who finds something odd on that branch knows whom to talk to. *(00:20:31)*

## 4. `git checkout` and `git branch` versus `git switch` ([8.1.3 Useful command line Git branching commands](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#useful-command-line-git-branching-commands))

*00:26:40–00:28:26*

- **Q:** You type `git switch -b dan-delete`. Predict what happens, and fix it.
  **A:** Git fails with ``error: unknown switch `b'``, because `-b` belongs to the older `git checkout -b`. Run `git switch -c dan-delete` instead. *(01:06:40)*

- **Q:** You run `git branch my-feature` and then start editing and committing. Which branch gets the commits?
  **A:** The branch you were already on. `git branch` creates the branch but doesn't move you to it, so you still have to run `git switch my-feature` (or check it out) before committing. *(00:28:13)*

- **Q:** An AI assistant tells you to run a `git checkout` command you don't understand, in a repository where losing work would hurt. What do you do?
  **A:** Ask it for the `git switch` version instead. `checkout` does more than move `HEAD`: it also has the behaviour of the newer restore and revert commands. If you don't know what it will do, think before you type it. *(00:27:44)*

## 5. Pushing a branch and viewing it on GitHub ([8.2 Useful things you can do with branches on GitHub](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#useful-things-you-can-do-with-branches-on-github))

*00:28:31–00:33:40*

- **Q:** You committed on `dan-b1`, switched back to `main`, and ran a bare `git push`. Predict the output, and fix it so your branch reaches GitHub.
  **A:** It prints `Everything up-to-date` and sends nothing, because the new commit is on `dan-b1`, not `main`. Run `git switch dan-b1`, then `git push origin dan-b1`. The last word names the branch you are pushing. *(00:29:34)*

- **Q:** Right after `git push origin dan-b1`, you run `git log --oneline --graph --decorate --all`. Which labels sit on your latest commit, and where is `origin/main`?
  **A:** Your commit shows `HEAD -> dan-b1, origin/dan-b1`, meaning GitHub now has the branch at the same place. `origin/main` hasn't moved and is still one commit behind. *(00:31:19)*

- **Q:** You push your branch and refresh the repository's GitHub page, but your changes aren't there. Where do you look?
  **A:** The page shows `main`. Use the branch dropdown in the top left, which says `main`, to switch the view to your branch. The branch button next to it lists every branch. *(00:32:21)*

- **Q:** A teammate made a great figure on their unmerged branch. You want to read the code without running it. What needs to happen?
  **A:** They push their branch to GitHub, and you select it in the branch dropdown to read the code. You can look at their work even though it isn't merged into `main` or reviewed yet. *(00:32:36)*

## 6. Opening a pull request ([9.1 Creating a pull request](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/github-pull-requests.html#creating-a-pull-request))

*00:33:40–00:41:16*

- **Q:** You pushed a branch two days ago, and the "Compare & pull request" pop-up has gone. How do you open the pull request, and how could you have avoided the problem?
  **A:** Go to the Branches tab, find your branch, open its menu and choose "New pull request". You land on the same page the pop-up would have opened. To avoid the problem, push a small change and start the pull request right away, even before the work is done. *(00:34:32)*

- **Q:** You are opening a pull request from your branch. Before writing anything, what do you check in the line at the top of the page?
  **A:** Check that it names your branch as the one being merged and `main` as the branch it merges into. In this course the target is `main`. In DSCI 524 it won't always be, and with forks you must also check the code is going to the right place. *(00:36:00)*

- **Q:** The changed-files list at the bottom of your new pull request includes `.DS_Store` and `.ipynb_checkpoints`. What do you do before clicking "Create pull request"?
  **A:** Get those files out of the branch and make sure your `.gitignore` keeps them out. Files that don't belong in the repository lose points even if nobody explicitly told you so. The file list is your second line of defence for catching them. *(00:39:16)*

- **Q:** A script you worked on is missing from the pull request's file list. Diagnose it.
  **A:** You probably forgot to add, commit or push it, or you typed something wrong. Commit and push it to the same branch, and it will appear. *(00:39:37)*

- **Q:** Your pull request keeps growing as you add more work. Where do you describe the new changes?
  **A:** Edit the first comment, the pull request's description, rather than adding "now I'm also doing…" comments. The first comment is what people read, so every change should be explained there. *(00:40:55)*

## 7. Code review and updating a pull request ([10 Code review on GitHub](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/github-code-review.html))

*00:41:16–00:45:41*

- **Q:** You are reviewing a teammate's pull request and want to question one line, such as why they used `switch` and not `checkout`. Where do you go, and what do you click?
  **A:** Open the "Files changed" tab, which shows the diff between the original and new code. Hover over the line and click the `+` to leave a comment. The comment is also tracked in the Conversation tab. *(00:41:34)*

- **Q:** A reviewer comments "this doesn't look right" on your pull request from `dan-b1`. Who changes the code, and what do you run? Do you close the pull request?
  **A:** You fix it, because the author of a pull request fixes it, not the reviewer. Don't close the pull request or open a new one. Go back to `dan-b1` locally, then `git add`, `git commit` and `git push origin dan-b1`, and the open pull request updates. *(00:43:15)*

- **Q:** You pushed a new commit to your pull request's branch, but the pull request page doesn't show it. What do you try?
  **A:** Refresh the page. The pull request is tied to the branch and tracks every commit you push, but sometimes it only shows up after a refresh. *(00:45:00)*

- **Q:** You change a line that a reviewer commented on and push. Predict what happens to their comment.
  **A:** It doesn't disappear, but GitHub may collapse it and mark it as outdated. The line it referred to has changed, so the comment probably no longer applies. *(00:45:02)*

## 8. AI reviewers and draft pull requests ([9.2 Draft pull requests](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/github-pull-requests.html#draft-pull-requests))

*00:52:11–00:55:41*

- **Q:** You opened a pull request early and will keep pushing to it for a week. You don't want anyone, or an agent, to merge it by accident. What do you do, and what changes on the page?
  **A:** Click "Convert to draft". The pull request gets a grey bar instead of a green one, and the merge button is greyed out, so it can't be merged by accident. It signals that people can look but the work isn't ready. *(00:54:30)*

- **Q:** Your draft pull request is finished and you want it merged. What do you click?
  **A:** Scroll to the bottom, where it says the pull request is a work in progress, and click "Ready for review". It becomes an open pull request again, with green merge buttons. *(00:55:28)*

- **Q:** You request a Copilot review, and one of its comments seems wrong. Do you have to make the change?
  **A:** No. More eyes on your code is never a bad idea, but you don't have to keep every comment an LLM makes. You can push back, reject it or accept it. *(00:53:01)*

## 9. Merging and deleting the branch on GitHub ([8.2 Useful things you can do with branches on GitHub](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#useful-things-you-can-do-with-branches-on-github))

*00:55:41–00:59:07*

- **Q:** Your project has run for weeks, and the branch dropdown has become a giant list. What should you do each time a pull request is merged?
  **A:** Click "Delete branch" on GitHub right after the merge. The branch count drops (two to one in the demo) and the list stays manageable. At the very least, clean up your own branches. *(00:57:42)*

- **Q:** You merged pull request #1 and deleted `dan-b1` on GitHub. A teammate worries its commits are gone. Predict what `main`'s history shows.
  **A:** The branch's two commits are still there, plus a merge commit, "Merge pull request #1 from chendaniely/dan-b1". Deleting the branch only removes the label, so you can still find those commits and undo the feature later. *(00:58:10)*

- **Q:** You work somewhere with a legal compliance requirement on code history. Do you delete merged branches?
  **A:** No. Where compliance rules apply, you can't delete them, and the branch list just gets long. Otherwise your team's workflow decides. *(00:57:00)*

## 10. Syncing and cleaning up locally after a merge ([8.1.3 Useful command line Git branching commands](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#useful-command-line-git-branching-commands))

*00:59:07–01:03:51*

- **Q:** Pull request #1 was merged on GitHub. You run `git switch main` locally, but `README.md` doesn't have the merged lines. Diagnose it and fix it.
  **A:** Your local `main` doesn't update itself. Run `git pull origin main`, which fast-forwarded `main` in the demo and added the pull request's 6 new lines to `README.md`. *(01:00:17)*

- **Q:** You type `git pull main`. Predict the result, and fix it.
  **A:** It fails with `fatal: 'main' does not appear to be a git repository`, because Git reads the first word as the remote. Run `git pull origin main`. *(01:04:28)*

- **Q:** The branch was deleted on GitHub, but `git branch -a` still lists `remotes/origin/dan-b1`. What do you run?
  **A:** Run `git fetch --prune`. It syncs your history with `origin` and removes references to branches deleted there. It printed `[deleted] (none) -> origin/dan-b1`. *(01:01:30)*

- **Q:** You want your local history to match GitHub, but you don't want any files in your working directory to change. Do you run `git pull` or `git fetch`?
  **A:** Run `git fetch`. `git pull` is a fetch followed by a merge, which changes your files. Fetch alone only coordinates the history. *(01:02:07)*

- **Q:** Your pull request from `dan-b1` was merged and the branch was deleted on GitHub. In order, what do you run locally to finish cleaning up?
  **A:** Run `git switch main`, then `git pull origin main`, then `git fetch --prune`, then `git branch -d dan-b1`. The lowercase `-d` deletes the local branch because it has been merged. *(01:03:21)*

- **Q:** You abandoned an experiment branch that was never merged, and `git branch -d` refuses to delete it. ChatGPT suggests `git branch -D`. What happens if you run it, and what is the risk?
  **A:** Capital `-D` force-deletes the branch even though it is unmerged, and its commits are lost. Lowercase `-d` refused precisely to stop you losing work. It is a one-character difference, so be very careful when copying commands that may hand you `-D`. *(01:03:21)*

## 11. Setting up two conflicting pull requests ([8.3 What happens when my feature branch falls behind main?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#what-happens-when-my-feature-branch-falls-behind-main))

*01:04:00–01:10:00*

- **Q:** You want to practise a merge conflict on your own in a repository. In order, what do you do, and what must you *not* do?
  **A:** Sync `main`, then `git switch -c dan-fetch`, edit a line of `README.md`, commit, push and open a pull request. Then `git switch main`, `git switch -c dan-delete`, change the same line, commit, push and open a second pull request. Don't merge the first pull request right away, or there will be no conflict to practise on. *(01:06:07)*

- **Q:** You committed a line on `dan-fetch`, then ran `git switch main` and `git switch -c dan-delete`. Is that line in `README.md` on `dan-delete`?
  **A:** No. `dan-delete` was created from `main`, which doesn't have the `dan-fetch` commit, so the line is not there. *(01:07:20)*

- **Q:** With `dan-fetch` and `dan-delete` both pushed, you run `git log --oneline --graph --all --decorate`. Predict the shape of the graph.
  **A:** Two lines leave the same `main` commit (`3851b00`): `157c3cd` on `dan-fetch` and `cb810d5` on `dan-delete`. That shows two parallel pieces of work. *(01:08:24)*

## 12. When a merge creates the conflict: resolving on GitHub

*01:10:00–01:12:44*

- **Q:** Pull requests #2 and #3 both target `main`, edit the same line, and both show as mergeable. You merge #2. Predict what happens to #3.
  **A:** Merging #2 changes `main`, so GitHub rechecks every pull request that targets `main`. #3 now shows a conflict. Nothing warned you beforehand, because each pull request looked fine on its own. *(01:10:19)*

- **Q:** The conflict in #3 is simple, and you resolve it in GitHub's web editor. What do you look for, and when is a conflict in report text fixed?
  **A:** Look for the conflict markers, `<<<<<<<`, `=======` and `>>>>>>>`. Fix them so that the remaining report text is English that makes sense. *(01:11:09)*

- **Q:** A conflict hits line 13 of your analysis script. You resolve it by keeping a version that renames a variable, delete the markers, and stop. The old name is still used on line 50. Are you done?
  **A:** No. Fixing a conflict means your code works from top to bottom again, not just that the markers are gone. The broken reference on line 50 is still your problem to fix. *(01:11:39)*

## 13. Resolving the conflict locally with rebase ([8.3.2 Using rebase](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#using-rebase))

*01:12:44–01:20:42*

- **Q:** #2 (`dan-fetch`) was merged, and #3 (`dan-delete`) now conflicts. In order, what do you run to resolve it on your computer and update #3?
  **A:** `git switch main`, `git pull origin main`, `git switch dan-delete`, `git rebase main`. Then fix the markers in `README.md`, `git add README.md`, `git rebase --continue`, and finally `git push --force-with-lease origin dan-delete`. The rebase replays your commit on top of the updated `main`, which is where the conflict surfaces. *(01:17:08)*

- **Q:** You skip pulling `main` and run `git rebase main` on `dan-delete` straight away. Why won't this deal with the conflict GitHub reports?
  **A:** The `dan-fetch` commit was merged on GitHub, but your local `main` doesn't have it yet. The rebase replays onto a `main` without that change. Syncing `main` first is what brings the merged commit to your computer. *(01:13:42)*

- **Q:** `git rebase main` stops with `CONFLICT (content): Merge conflict in README.md`. You have fixed the file and aren't sure what comes next. How do you find out, and what do you run?
  **A:** Run `git status`, which guides you. It tells you to use `git add README.md` to mark the conflict resolved. Once all conflicts are fixed, it tells you to run `git rebase --continue`, which asks you to confirm the commit message. *(01:18:32)*

- **Q:** You are midway through a rebase, the file looks like a mess, and you are scared you have broken something. How do you get back to where you started?
  **A:** Run `git rebase --abort`. It stops the rebase and returns your branch to its state before `git rebase`. *(01:18:20)*

- **Q:** After `git rebase --continue`, the log shows `dan-delete` at a new commit (`0e16503`) on top of `main`, but `origin/dan-delete` still at `cb810d5`. You run a plain push. Predict what happens, and choose the fix.
  **A:** The plain push is rejected, because the rebase changed the branch's history: the commit now has a different parent. Run `git push --force-with-lease origin dan-delete`. GitHub records that a force push happened, so you are rewriting history, which matters in compliance settings. Only do it on your own branch. *(01:19:47)*

- **Q:** You type `git push --force-with-leasse origin dan-delete`. Predict the result, and fix it.
  **A:** Git fails with ``error: unknown option `force-with-leasse'`` and prints its usage text. It is a typo, so re-run it as `git push --force-with-lease origin dan-delete`. *(01:19:34)*

---

- prompt: prompt-recall-3-apply.md @ 8bcc190
- prompt-hash: 068025368bc2
- model: claude-opus-5-5 (requested: opus)
- backend: claude
- inputs: transcript-plaud.md, terminal.txt, materials.md, notes-class-main--claude-opus-5-5.md
- generated: 2026-11-20
- notes-input: notes-class-main--claude-opus-5-5.md @ d979d4ea6828, links and section references removed
