# Git branches, pull requests and rebasing to fix conflicts: review questions, tier 3 — Apply

Date: 2026-11-17

Instructor: Daniel Chen

*Tier 3 of 5: Apply. Work each situation through before you read the answer; tiers 1 (Remember) and 2 (Understand) cover the facts and reasons it relies on.*

## 1. Git recap: setting up the demo repository

*00:04:07–00:06:49*

- **Q:** You have just cloned `2026-11-17-git` and edited `README.md` on `main`. In order, what do you run to check the change, record it and send it to GitHub?
    - **A:** Run `git status` to confirm `README.md` is modified and `git diff` to read the change. Then run `git add README.md`, `git commit -m "intro and review"` and `git push origin main`. This is the same add–commit–push cycle from DSCI 521. *(00:06:32)*

- **Q:** You want to see exactly which lines of `README.md` you changed before you stage it. Which command do you run, and what will it show?
    - **A:** Run `git diff`. It shows the old lines prefixed with `-` and the new lines prefixed with `+`, for example the added line linking the Git branches chapter. Run it before `git add`, while the change is still unstaged. *(00:06:13)*

- **Q:** You have just run `git push origin main` after committing "intro and review". Predict where `HEAD`, `main` and `origin/main` sit in `git log --oneline --graph --decorate --all`.
    - **A:** All three sit on the same commit: `145ff16 (HEAD -> main, origin/main, origin/HEAD) intro and review`. You committed on `main` and then pushed, so your computer's record of GitHub's `main` caught up with your local `main`. *(00:06:38)*

## 2. Why branches: escaping the 521 push/pull friction ([8 Git branches](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html))

*00:06:49–00:09:43*

- **Q:** You and a teammate both commit to `main` on the group project. You try to push and are refused, even though you edited different files. What happened, and how do you avoid this happening all week?
    - **A:** Your teammate pushed first, so you have to pull before you can push again, even without a conflict. To avoid this, each person works on their own branch. You can then push and pull your branch freely without depending on what others are doing. *(00:07:06)*

- **Q:** Your group is in the first week of the project, and nothing exists yet except the plan. Can all four of you start separate branches of independent work straight away?
    - **A:** Usually not. Early in a project, everyone is blocked on one or two people getting the basics in place, so some of the old push/pull friction is unavoidable. Move to parallel branches once each person owns a self-contained part. *(00:07:50)*

- **Q:** You own a self-contained part of the project and plan to work on it from Tuesday to Friday. How do you work during the week, and when does your work meet your teammates' work?
    - **A:** Work on your own branch, pushing as often as you like without caring what others are doing. On Friday the group reviews everyone's branches and merges the work together. *(00:09:19)*

## 3. Review: the local–remote picture

*00:09:46–00:11:47*

- **Q:** Your analysis is committed on your laptop, but you never pushed it before the milestone deadline. Will it be graded?
    - **A:** No. GitHub is what gets graded and published. Work that exists only on your computer "effectively doesn't really exist" for grading or project purposes, so you must `push` it. *(00:10:53)*

- **Q:** You already cloned the group repository last week. Today a teammate pushes a new commit. Do you run `git clone` again to get it?
    - **A:** No. `clone` is a one-time command. To bring down commits your teammates pushed, run `pull`. *(00:11:47)*

- **Q:** You and three teammates each have the project on your own laptop. Choose the place everyone's work must end up in, and the command that sends your commits there.
    - **A:** The GitHub remote is the place that matters; every teammate's computer coordinates with it. You send your commits there with `push`, and teammates' commits come down with `pull`. *(00:11:33)*

## 4. What a branch is: `main`, `HEAD` and `origin/main` ([8 Git branches](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html))

*00:12:03–00:17:54*

- **Q:** You make two commits on `main` and do not push. Predict where `main` and `origin/main` sit in `git log --oneline --graph --decorate --all`.
    - **A:** `main` (with `HEAD` attached) is two commits ahead of `origin/main`. `origin/main` is only what your computer thinks GitHub's `main` is, and it does not move until you sync with GitHub. *(00:13:44)*

- **Q:** You are on a branch named `b1` and run `git add` and `git commit`. Which branch name moves forward, and which stays where it was?
    - **A:** `b1` moves forward to the new commit, and `main` stays put. The `git add`/`git commit` workflow is unchanged; the only difference is that your commits drag along your branch name instead of `main`. *(00:14:25)*

- **Q:** You are doing exploratory data analysis for the group project, and your plots are still rough. The cleaned dataset is finished. What goes on `main`, and where does the EDA live?
    - **A:** `main` holds the cleaned dataset, which everyone builds on. Treat `main` as the stable version, where at least the code works. Your EDA stays on your own branch until it is ready to be reviewed and merged. *(00:15:49)*

- **Q:** You spend an afternoon on a branch trying a new approach, and none of it works. How do you get back to your starting point?
    - **A:** Switch back to `main` and either delete the branch or start a new one. This is much easier than untangling a single commit that did twenty things on `main`. `git reset`/`git revert` would also work, but branches make it simpler. *(00:17:22)*

- **Q:** You are the only person working in a repository, but others read it while you edit, as with a textbook being taught from that day. Should you still use branches?
    - **A:** Yes. Make your edits on branches so the published version does not shift around mid-use. Merge only after you have reviewed and tested everything. Branches section off work even when you work alone. *(00:16:51)*

## 5. Creating and switching branches ([8.1 Creating a branch using the command line](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#creating-a-branch-using-the-command-line))

*00:17:54–00:26:29*

- **Q:** You are about to start a new task in your group project that builds on what your teammates have pushed. In order, what do you run before your first commit?
    - **A:** Run `git status` to confirm you are `On branch main`. Run `git pull origin main` to sync with everything your team has pushed. Then run `git switch -c <name>` to create your branch and move to it. Skipping the pull can mean you redo work that already exists elsewhere. *(00:18:39)*

- **Q:** On `main` at commit `145ff16`, you run `git switch -c dan-b1` and nothing else. Predict the output of `git status` and of `git log --oneline --graph --decorate --all`.
    - **A:** `git status` says `On branch dan-b1` with a clean working tree. The log shows `145ff16 (HEAD -> dan-b1, origin/main, origin/HEAD, main)`. No new commit is made: you only created a branch and attached `HEAD` to it. *(00:21:15)*

- **Q:** On `dan-b1` you commit a new README line ("define swtich -c"). Predict where `dan-b1`, `main` and `origin/main` sit in the log.
    - **A:** `dan-b1` (with `HEAD`) is on the new commit `4a14a64`, one commit ahead. `main` and `origin/main` both stay on `145ff16`. You have not pushed, so GitHub knows nothing about the branch yet. *(00:23:21)*

- **Q:** You committed a new line to `README.md` on `dan-b1`, then ran `git switch main`. You open `README.md`. Is the new line there, and where did `dan-b1` go?
    - **A:** The line is gone, because the files on disk now show `main`'s version. `dan-b1` has not moved. Switch back with `git switch dan-b1` and the line returns. *(00:25:46)*

- **Q:** You run `git log --oneline --graph --decorate`, but your other branches do not appear. What do you add?
    - **A:** Add the `--all` flag: `git log --oneline --graph --decorate --all`. Without it, you may not see the other branch names. *(00:25:38)*

- **Q:** You are creating a branch in a shared group repository. How can you name it so teammates know whom to ask if something on it looks odd?
    - **A:** Start the branch name with your own name, as in `dan-b1`. Teammates then know who is responsible for that work. *(00:20:31)*

## 6. `git checkout` and `git branch` versus `git switch` ([8.1.3 Useful command line Git branching commands](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#useful-command-line-git-branching-commands))

*00:26:40–00:28:26*

- **Q:** ChatGPT tells you to run `git checkout -b my-feature`. What is the `git switch` command that does the same thing?
    - **A:** `git switch -c my-feature`. Both create the branch and move `HEAD` to it; `checkout -b` is the older form. *(00:28:10)*

- **Q:** You run `git branch my-idea` and then immediately commit a change. Which branch does the commit land on?
    - **A:** It lands on the branch you were already on, not `my-idea`. `git branch` only creates the branch and does not move you to it. You still need `git switch my-idea` (or `checkout`) before committing. *(00:28:13)*

- **Q:** An AI assistant hands you a `git checkout` command you don't fully understand, in a codebase where you are worried about losing work. What do you do?
    - **A:** Don't run it blindly; ask for the `switch` version instead. `checkout` does more than move `HEAD`: it also does much of what `restore` and `revert` do. You should know what a command will do before running it on work you care about. *(00:27:44)*

## 7. Pushing a branch and viewing it on GitHub ([8.1 Creating a branch using the command line](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#creating-a-branch-using-the-command-line))

*00:28:31–00:33:40*

- **Q:** Your new commit is on `dan-b1`, but you are on `main`. You run `git push`, and it prints `Everything up-to-date`, but the commit isn't on GitHub. What went wrong, and what fixes it?
    - **A:** The bare `git push` from `main` had nothing new to send, because the commit is on `dan-b1`. Run `git switch dan-b1`, then `git push origin dan-b1`. The last word of the push names the branch you are pushing, not `main`. *(00:30:36)*

- **Q:** You have just run `git push origin dan-b1` for the first time. Predict what changes in `git log --oneline --graph --decorate --all`.
    - **A:** `origin/dan-b1` now appears on the same commit as `dan-b1`. `origin/main` has not moved, because you pushed the branch, not `main`. *(00:31:27)*

- **Q:** You pushed `dan-b1` and refresh the repository's main page on GitHub, but your change isn't in the README. Where do you look to confirm it reached GitHub?
    - **A:** Use the branch dropdown at the top left, which says `main`, and choose `dan-b1`. The main page only shows `main`'s content until the branch is merged. The branch button next to the dropdown lists all branches. *(00:32:29)*

- **Q:** A teammate made a figure you want to learn from, but their work is not merged and you don't want to run it. How do you read their code?
    - **A:** Ask them to push their branch. Then pick that branch in the branch dropdown on GitHub and browse its files, even though it isn't in `main` yet. *(00:32:36)*

- **Q:** Your work on `dan-b1` is finished, and you want it in `main`. Choose between merging it locally and another route.
    - **A:** Push the branch and merge it through a pull request on GitHub rather than on your computer. The review process happens there. *(00:28:58)*

## 8. Opening a pull request ([9.1 Creating a pull request](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/github-pull-requests.html#creating-a-pull-request))

*00:33:40–00:41:16*

- **Q:** You pushed a branch two days ago, and the "Compare & pull request" pop-up on GitHub is gone. How do you open the pull request now?
    - **A:** Go to the Branches tab, find your branch, open its expansion menu and choose "New pull request". You land on the same page the pop-up would have taken you to. *(00:35:00)*

- **Q:** You are starting a task that will take a few days. When do you open its pull request so you don't lose the easy route to it?
    - **A:** Open it right away. Make a small change, push the branch and start the pull request even though the work isn't done. Then keep pushing to the branch, and the pull request updates as you go. *(00:35:15)*

- **Q:** On the "Open a pull request" page, what do you check in the line at the top before writing anything?
    - **A:** Check that it shows the branch you are working on and the branch you are merging into, which is `main` in this course. In other settings the target isn't always `main`, and with forks you must make sure the code is going to the right repository. *(00:36:55)*

- **Q:** Scrolling the changed files at the bottom of your new pull request, you see `.ipynb_checkpoints` and a `.DS_Store`. What do you do before creating it?
    - **A:** Remove them and add them to your `.gitignore`. Files that don't belong in the repository lose points even if the instructions don't explicitly mention them. This file list is your second line of defence for catching them. *(00:39:23)*

- **Q:** A script you know you wrote is missing from your pull request's list of changed files. What probably went wrong?
    - **A:** You probably forgot to add, commit or push it, or you typed something wrong. Run `git add`, `git commit` and `git push origin <branch>` from the same branch, and the file will appear. *(00:39:37)*

- **Q:** Your pull request has grown to cover more work than its original description. How do you update what reviewers read?
    - **A:** Edit the first comment (the description) so it explains all the changes. Don't keep adding "now I'm also doing…" comments. People read the first comment. *(00:41:03)*

## 9. Code review and updating a pull request ([10 Code review on GitHub](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/github-code-review.html))

*00:41:16–00:45:41*

- **Q:** You are reviewing a teammate's pull request and want to ask why a particular line uses `switch` and not `checkout`. Where do you leave the comment?
    - **A:** Open the Files changed tab, hover over that line in the diff, click the `+` and write the comment. It is also tracked in the main Conversation tab. *(00:41:34)*

- **Q:** You review a teammate's pull request and find a line that looks wrong. Do you fix it yourself?
    - **A:** No. As the reviewer, your job is to point it out ("rewrite this", "this doesn't look right"). The author of the pull request is responsible for fixing it. *(00:42:17)*

- **Q:** A reviewer asks you to change your open pull request from `dan-b1`. Do you close it and open a new one? What do you run?
    - **A:** Don't close it. Go back to the same branch locally (`git switch dan-b1`), make the change, then run `git add README.md`, `git commit -m "..."` and `git push origin dan-b1`. The pull request is tied to the branch, so it updates with the new commit. *(00:43:15)*

- **Q:** You pushed a new commit to your pull request's branch, but the commit doesn't show on the pull request page yet. What do you try first?
    - **A:** Refresh the page. The pull request tracks every commit you push to the branch, but sometimes you need a refresh to see it. *(00:45:00)*

- **Q:** You change a line that a reviewer had commented on, then push. Predict what happens to their comment.
    - **A:** It doesn't disappear, but GitHub may collapse it and mark it as outdated, because the line it refers to has changed. *(00:45:02)*

## 10. AI reviewers and draft pull requests ([9.2 Draft pull requests](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/github-pull-requests.html#draft-pull-requests))

*00:52:11–00:55:41*

- **Q:** You request a Copilot review on your pull request, and it leaves several comments. Must you act on all of them?
    - **A:** No. You can accept some, push back on others or reject them. More eyes on your work is never really a bad idea, but an LLM's comments are not orders. *(00:53:01)*

- **Q:** You opened a pull request early and will keep pushing to it for several days. A teammate, or an agent, might merge it because everything looks green. What do you do?
    - **A:** Click "Convert to draft" at the top right. The pull request shows a grey bar instead of green, and the merge button is greyed out, so nobody can merge it by accident. Agents are also less likely to merge it just because it is green. *(00:54:30)*

- **Q:** Your draft pull request is now finished. How do you make it mergeable again?
    - **A:** Scroll to the bottom, where it says the pull request is still a work in progress, and click "Ready for review". It becomes an open pull request with green merge buttons again. *(00:55:28)*

## 11. Merging and deleting the branch on GitHub ([8.2 Useful things you can do with branches on GitHub](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#useful-things-you-can-do-with-branches-on-github))

*00:55:41–00:59:07*

- **Q:** Your pull request from `dan-b1` has just been merged. What do you do on GitHub so the branch dropdown doesn't turn into a giant list over the project?
    - **A:** Click "Delete branch" on the merged pull request. The branch count drops (from two to one in the demo), and only live branches stay in the list. *(00:57:42)*

- **Q:** You hesitate to delete `dan-b1` on GitHub because you fear losing its commits. Predict what `main`'s commit history shows afterwards.
    - **A:** The branch's two commits are still there, plus a merge commit, "Merge pull request #1 from chendaniely/dan-b1". Deleting the branch only removes the label, not the work. *(00:58:19)*

- **Q:** A merged feature later turns out to be a mistake, and its branch was deleted long ago. Where do you go to undo it?
    - **A:** Look in `main`'s history for the commits related to that pull request and its merge commit, and undo from there. Nothing is really lost in this workflow. *(00:58:38)*

- **Q:** Your workplace has legal or compliance rules about keeping records. Do you still delete merged branches?
    - **A:** No. If compliance requires it, don't delete them, even though the branch list gets long. Otherwise follow your team's workflow, and at least clean up your own branches. *(00:57:00)*

## 12. Syncing and cleaning up locally after a merge ([8.1.3 Useful command line Git branching commands](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#useful-command-line-git-branching-commands))

*00:59:07–01:03:51*

- **Q:** Your pull request was merged on GitHub. You run `git switch main` locally, but `README.md` doesn't have the merged lines. What do you run?
    - **A:** Run `git pull origin main`. Local `main` doesn't update itself. The pull brings the merge down (in the demo it fast-forwarded and added 6 lines to `README.md`). *(01:00:27)*

- **Q:** You deleted `dan-b1` on GitHub, but `git branch -a` still lists `remotes/origin/dan-b1`. What removes it?
    - **A:** Run `git fetch --prune`. It syncs history with `origin` and removes local references to branches that were deleted on GitHub. The output shows `[deleted] (none) -> origin/dan-b1`. *(01:01:30)*

- **Q:** You want to bring your local record of GitHub's history up to date without any of your working files changing. Choose between `git pull` and `git fetch`.
    - **A:** Use `git fetch`. `git pull` runs a fetch and then a merge, which changes your files. `fetch` alone only coordinates the history. *(01:02:07)*

- **Q:** You run `git branch -d my-experiment` on an experiment branch that was never merged, and Git refuses. What is going on, and what is the risky alternative?
    - **A:** Lowercase `-d` only deletes merged branches, so Git is protecting work you would otherwise lose. Capital `git branch -D` force-deletes it anyway. It is a one-character difference, so be very careful when an AI hands you `-D`: you could delete commits you are still working on. *(01:03:21)*

- **Q:** Your pull request from `dan-b1` has been merged and the branch deleted on GitHub. In order, what do you run locally to finish cleaning up?
    - **A:** Run `git switch main`, then `git pull origin main`, then `git fetch --prune`, then `git branch -d dan-b1`. Pulling first makes `dan-b1` count as merged, so the lowercase `-d` succeeds. *(01:03:21)*

## 13. Setting up two conflicting pull requests ([8.3 What happens when my feature branch falls behind main?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#what-happens-when-my-feature-branch-falls-behind-main))

*01:04:00–01:10:00*

- **Q:** You want to practise a merge conflict on your own in your demo repository. How do you set it up?
    - **A:** Create two branches from `main` (such as `dan-fetch` and `dan-delete`) that each change the same line of the same file. Push both and open two pull requests. Don't merge the first one straight away: a conflict comes from the same change to the same line of the same file. *(01:06:07)*

- **Q:** You run `git pull main` to sync before branching, and get `fatal: 'main' does not appear to be a git repository`. What fixes it?
    - **A:** Run `git pull origin main`. The first argument has to be the remote (`origin`) and the second the branch. Git read `main` as the name of a repository. *(01:04:28)*

- **Q:** You commit a "fetch --prune" line on `dan-fetch`, then run `git switch main` and `git switch -c dan-delete`. Is the fetch line in `README.md`?
    - **A:** No. `dan-delete` was created from `main`, which doesn't contain the `dan-fetch` commit, so that line isn't in this version of the file. *(01:07:20)*

- **Q:** You type `git switch -b dan-delete` and get ``error: unknown switch `b'``. What do you run instead?
    - **A:** Run `git switch -c dan-delete`. The `-b` flag belongs to `git checkout -b`; `switch` uses `-c` to create a branch. *(01:06:43)*

- **Q:** Both `dan-fetch` and `dan-delete` are pushed, each with its own commit. Predict the shape of `git log --oneline --graph --all --decorate`.
    - **A:** Two lines leave the same `main` commit (`3851b00`): one to `157c3cd` on `dan-fetch` and one to `cb810d5` on `dan-delete`. Those are two parallel pieces of work. *(01:08:19)*

- **Q:** You open both pull requests, #2 and #3, side by side on GitHub. Each says it can be merged into `main`. Will GitHub warn you that they edit the same line?
    - **A:** No. Nothing on either pull request tells you a conflict is coming; each is only checked against the current `main`. You only find out when one of them is merged. *(01:09:53)*

## 14. When a merge creates the conflict: resolving on GitHub ([8.3 What happens when my feature branch falls behind main?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#what-happens-when-my-feature-branch-falls-behind-main))

*01:10:00–01:12:44*

- **Q:** Pull requests #2 and #3 both look green. You merge #2. Predict what happens to #3.
    - **A:** Merging #2 changes `main`, and GitHub rechecks every pull request that merges into `main`. #3 now shows a merge conflict, because both edited the same line. *(01:10:19)*

- **Q:** The conflict on your pull request is a small one in `README.md`. How do you resolve it without leaving GitHub?
    - **A:** Open the web editor from the conflict page and find the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`). Edit the section into its final form and remove the markers. *(01:10:59)*

- **Q:** You resolve a conflict on line 13 of a script by renaming a variable, and the markers are gone. The old name is still used on line 50. Are you done?
    - **A:** No. Fixing a conflict means the code works from top to bottom again, not just that the markers are gone. Update line 50 and run the code; any knock-on breakage from your fix is still your problem. *(01:11:39)*

- **Q:** The conflict is in your group's report prose rather than code. What must be true when you have resolved it?
    - **A:** The text that remains must be English that makes sense, not just text with the markers deleted. *(01:11:09)*

## 15. Resolving the conflict locally with rebase ([8.3.2 Using rebase](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#using-rebase))

*01:12:44–01:20:42*

- **Q:** #2 was merged, and your pull request from `dan-delete` now conflicts. In order, what do you run to fix it on your own computer with rebase?
    - **A:** Run `git switch main` and `git pull origin main` to get the merged commit. Then run `git switch dan-delete` and `git rebase main`, fix the markers in `README.md`, `git add README.md` and `git rebase --continue`. Finally, run `git push --force-with-lease origin dan-delete`. The rebase replays your commit on top of the updated `main`, so the conflict appears locally where you can fix it. *(01:17:08)*

- **Q:** `git rebase main` stops with `CONFLICT (content): Merge conflict in README.md`. What do you do next, and how do you know?
    - **A:** Fix the conflict markers in `README.md` in your editor. `git status` then tells you to run `git add README.md` to mark the conflict resolved. After that, it tells you to run `git rebase --continue`, which asks you to confirm the commit message. *(01:18:44)*

- **Q:** You are midway through a rebase, the conflict looks like a mess, and you are afraid you've broken something. How do you get back to where you started?
    - **A:** Run `git rebase --abort`. It returns your branch to its state before `git rebase main`, and `git status` lists it as an option. *(01:18:20)*

- **Q:** After `git rebase --continue` on `dan-delete`, predict where `dan-delete` and `origin/dan-delete` sit in `git log --oneline --graph --all --decorate`.
    - **A:** `dan-delete` is a new commit, `0e16503`, sitting directly on top of `main` (`3167d10`), with the conflict fixed. `origin/dan-delete` still points at the old commit, `cb810d5`, on the old base. The rebase rewrote your local branch but not GitHub's copy. *(01:19:14)*

- **Q:** After the rebase, you plan to run `git push origin dan-delete`. Will it work? What do you run instead?
    - **A:** A plain push will be rejected, because the rebased commit has a new parent and the branch's history has changed. You have to force-push with `git push --force-with-lease origin dan-delete`. GitHub then records that a force push happened, which is why you rebase only your own branch. *(01:19:47)*

- **Q:** You type `git push --force-with-leasse origin dan-delete` and get ``error: unknown option `force-with-leasse'``. What fixes it?
    - **A:** It's a typo in the flag. Re-run it as `git push --force-with-lease origin dan-delete`, and the output shows `(forced update)`. *(01:19:47)*

- **Q:** Your force push succeeded, and the pull request from `dan-delete` shows a green merge button again. What remains to be done?
    - **A:** Merge the pull request and delete the branch on GitHub. Then clean up locally: `git switch main`, `git pull origin main`, `git fetch --prune` and `git branch -d dan-delete`. *(01:20:35)*

---

- prompt: prompt-recall-3-apply.md @ 65eb21c
- prompt-hash: 49276171f719
- model: claude-opus-5-5 (requested: opus)
- backend: claude
- inputs: transcript-plaud.md, terminal.txt, materials.md, notes-class-main--claude-opus-5-5.md
- generated: 2026-11-23
- notes-input: notes-class-main--claude-opus-5-5.md @ d979d4ea6828, links and section references removed, diagrams removed
