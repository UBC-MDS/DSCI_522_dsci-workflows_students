# Git branches, pull requests and rebasing to fix conflicts: review questions, tier 1 — Remember

Date: 2026-11-17

Instructor: Daniel Chen

*Tier 1 of 5: Remember. Answer each question before you read its answer; tiers 2 to 5 build on these.*

## 1. Course logistics: lab groups, attendance and interview week

*00:00:01–00:04:04*

- **Q:** Where do you look up your DSCI 522 group, and which column tells you who is in it?
    - **A:** In the lab sections repository on UBC's GitHub. Find your lab section, then the group number column: everyone with the same number is your group. *(00:01:24)*

- **Q:** State what the GitHub usernames collected from students are used to build.
    - **A:** A main list of every student's GitHub username, a piece of metadata used everywhere else in the program. *(00:02:01)*

- **Q:** State the rule for attending lab this year, and what the TAs do during lab.
    - **A:** Lab attendance is mandatory, because this is a group project. The TAs go around and talk to every group, and you should be there when a TA comes to yours. *(00:02:19)*

- **Q:** How long is the interview week conversation, and what is it modelled on?
    - **A:** About seven minutes, run like a technical interview. *(00:02:50)*

- **Q:** Name the two things the interview week conversation covers.
    - **A:** How much you know about what you are doing with Git, and your group's actual code base. Anything in your code base is fair game, "especially in the world of AI". *(00:03:15)*

- **Q:** Does the interview week conversation affect your grade?
    - **A:** No. You get a grade, but it does not affect your course grade. *(00:03:02)*

- **Q:** What happens if the TAs don't reach everyone in their scheduled interview week?
    - **A:** It moves by plus or minus a week. You might be called and you might not, and some students need the full seven minutes while others don't. *(00:03:29)*

- **Q:** What did the instructor say this interview format might become next year?
    - **A:** It "might actually be the exam next year." *(00:03:48)*

## 2. Git recap: setting up the demo repository

*00:04:07–00:06:49*

- **Q:** Name the demo repository created and cloned in class.
    - **A:** `chendaniely/2026-11-17-git`, named for the day. It was cloned with `git clone git@github.com:chendaniely/2026-11-17-git.git`. *(00:05:18)*

- **Q:** What did the instructor initialise the demo repository `2026-11-17-git` with, instead of leaving it empty?
    - **A:** A README. He noted you could also add a Python option and a license if you want. *(00:05:06)*

- **Q:** What change did the instructor make to `README.md` in `2026-11-17-git` before the first commit?
    - **A:** He added a line saying the class will review 521 Git basics and then go into branches, plus a link to the textbook's Git branches chapter. *(00:05:57)*

- **Q:** What did `git status` report after the first edit to `README.md` in `2026-11-17-git`?
    - **A:** That `README.md` was modified, with `Changes not staged for commit`. *(00:06:13)*

- **Q:** What was the commit message of the first commit in the demo repository `2026-11-17-git`?
    - **A:** `intro and review`. *(00:06:32)*

## 3. Why branches: escaping the 521 push/pull friction ([8 Git branches](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html))

*00:06:49–00:09:43*

- **Q:** Which DSCI 521 exercise, and in which week, did the instructor recall to illustrate push/pull friction?
    - **A:** The shared slide deck exercise in week 3 of 521. *(00:06:54)*

- **Q:** State the annoyance from the 521 slide-deck exercise that happened even when there was no conflict.
    - **A:** You couldn't push because someone else had pushed first, so you had to pull before you could push again. *(00:07:06)*

- **Q:** What kind of work did the instructor say you want to reach in a group project, once the basics are in place?
    - **A:** Parallel streams: a part of the project that is just your responsibility, worked on in your own branch. *(00:08:41)*

- **Q:** Recall the example schedule the instructor gave for working on branches and then reviewing.
    - **A:** You work on your own part from Tuesday to Friday, and on Friday the group reviews and coordinates all the work. *(00:08:46)*

## 4. Review: the local–remote picture

*00:09:46–00:11:47*

- **Q:** Name the two places where you do work in Git.
    - **A:** Your computer (local) and the cloud (the GitHub remote). *(00:10:09)*

- **Q:** Which copy of the project did the instructor say is the one that matters, the one graded and published?
    - **A:** The copy on GitHub, the remote. Work that exists only on your local computer "effectively doesn't really exist" for grading or project purposes. *(00:10:53)*

- **Q:** How often do you run `git clone` on a repository?
    - **A:** Once: clone is a one-time command. *(00:11:25)*

- **Q:** Name the command that sends commits to GitHub and the one that brings down commits your teammates pushed.
    - **A:** `push` sends code up; `pull` brings other people's commits down. *(00:11:33)*

## 5. What a branch is: `main`, `HEAD` and `origin/main` ([8 Git branches](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html))

*00:12:03–00:17:54*

- **Q:** What is the `main` branch?
    - **A:** The default branch that you are working on. *(00:12:38)*

- **Q:** What happens to `main` each time you commit while `HEAD` is attached to it?
    - **A:** It increments: it moves forward with each commit. *(00:13:17)*

- **Q:** What does `origin/main` represent in the Git log?
    - **A:** What your computer thinks the state of `main` on GitHub (the remote) is. *(00:13:30)*

- **Q:** Define a branch, as the instructor put it.
    - **A:** A name you give yourself that your commits move forward instead of `main`. You use the same `git add` and `git commit` process as before. *(00:14:06)*

- **Q:** What was the branch called in the instructor's hand-drawn diagram?
    - **A:** `B1` (labelled `b1` in the drawing). *(00:14:06)*

- **Q:** What did the instructor say you can think of the `main` branch as?
    - **A:** The production, final, stable version, where everything should be in working order, or at least the code works. *(00:15:10)*

- **Q:** Recall the example the instructor gave of using branches while working alone.
    - **A:** He did all his edits to the course textbook in a sequence of branches, so the textbook wouldn't move around in the middle of a teaching day. He merged them after lectures were over and he had reviewed and tested everything. *(00:16:37)*

- **Q:** Which two 521 commands did the instructor name as another way to undo work, besides branches?
    - **A:** `git reset` and `git revert`. *(00:17:22)*

## 6. Creating and switching branches ([8.1 Creating a branch using the command line](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#creating-a-branch-using-the-command-line))

*00:17:54–00:26:29*

- **Q:** Which command did the instructor run first to confirm he was on `main` before creating a branch?
    - **A:** `git status`, which showed `On branch main`. *(00:18:03)*

- **Q:** Which command did the instructor run to sync up before branching, when the work builds on coordinated work?
    - **A:** `git pull origin main`. *(00:18:39)*

- **Q:** What does `git switch` do?
    - **A:** It moves `HEAD` around the Git repository, switching between branches. *(00:19:46)*

- **Q:** What does the `-c` in `git switch -c` stand for?
    - **A:** Create. *(00:20:09)*

- **Q:** Reproduce the command the instructor used to create the first branch in the demo repository.
    - **A:** `git switch -c dan-b1`. *(00:21:31)*

- **Q:** What does the instructor start his branch names with in shared repositories?
    - **A:** His own name, so others know whom to talk to if something looks weird. *(00:20:31)*

- **Q:** What changed in the `git status` output right after `git switch -c dan-b1`?
    - **A:** Only the branch line: it said `On branch dan-b1` instead of `On branch main`. *(00:21:03)*

- **Q:** Quote the definition of `switch -c` that the instructor added to `README.md` on `dan-b1`.
    - **A:** `` `switch -c <name>`: create and move HEAD to the branch <name> ``. *(00:21:56)*

- **Q:** What was the commit message for the first commit on `dan-b1`, as typed?
    - **A:** `define swtich -c`, with "switch" misspelled. *(00:22:31)*

- **Q:** Where in VS Code or Positron can you see the same branch picture as the terminal log?
    - **A:** In the graph view of the Git tab. *(00:24:09)*

- **Q:** Which command moved `HEAD` from `dan-b1` back to `main`?
    - **A:** `git switch main`. *(00:25:12)*

- **Q:** Which flag must you add to `git log --oneline` to see your other branch names?
    - **A:** `--all`, as in `git log --oneline --graph --decorate --all`. *(00:25:38)*

## 7. `git checkout` and `git branch` versus `git switch` ([8.1.3 Useful command line Git branching commands](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#useful-command-line-git-branching-commands))

*00:26:40–00:28:26*

- **Q:** Will students be tested on using `git checkout` rather than `git switch`?
    - **A:** No. The instructor said `checkout` is fine and he is not going to test you on it. *(00:26:42)*

- **Q:** Name the older command that did what `git switch` does, and roughly when the change happened.
    - **A:** `git checkout`; `switch` came in around 2019. *(00:26:59)*

- **Q:** Which command does the instructor use day to day, and when does he use `switch`?
    - **A:** He uses `git checkout`, and only uses `switch` when teaching. *(00:26:59)*

- **Q:** Besides moving `HEAD`, what else did `git checkout` do that newer commands were split out from?
    - **A:** Much of what `revert` and `restore` do. Those behaviours still exist in `checkout`. *(00:27:09)*

- **Q:** What did the instructor say to do if Copilot or ChatGPT tells you to run `checkout` and you don't know what the command does?
    - **A:** Prompt it to do the same thing with `switch` instead. *(00:27:44)*

- **Q:** State the `checkout` equivalent of `git switch -c <name>`.
    - **A:** `git checkout -b <name>`. *(00:28:10)*

- **Q:** What does `git branch <name>` do, and what does it not do?
    - **A:** It creates the branch but does not move you to it, so you still have to `checkout` or `switch` afterwards. *(00:28:13)*

## 8. Pushing a branch and viewing it on GitHub ([8.2 Useful things you can do with branches on GitHub](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#useful-things-you-can-do-with-branches-on-github))

*00:28:31–00:33:40*

- **Q:** Name the two terms for the review process used to get a branch into `main`.
    - **A:** A pull request, also called a merge request. *(00:28:58)*

- **Q:** What did a bare `git push` print when run on `main` while the new commit was on `dan-b1`?
    - **A:** `Everything up-to-date`. It did not push `dan-b1`. *(00:29:34)*

- **Q:** Reproduce the command the instructor used to send the `dan-b1` branch to GitHub.
    - **A:** `git push origin dan-b1`, run while on `dan-b1`. *(00:30:36)*

- **Q:** What did the output of the first `git push origin dan-b1` print, besides the transfer details?
    - **A:** A link to create a pull request for `dan-b1`: `https://github.com/chendaniely/2026-11-17-git/pull/new/dan-b1`, and `* [new branch] dan-b1 -> dan-b1`. *(00:30:36)*

- **Q:** After pushing `dan-b1`, which new reference appeared in the Git log, and which one did not move?
    - **A:** `origin/dan-b1` appeared next to `dan-b1`, while `origin/main` and `main` stayed where they were. *(00:31:19)*

- **Q:** Where on a GitHub repository page do you switch to view another branch, such as `dan-b1`?
    - **A:** The dropdown in the top left-hand corner that says `main`. *(00:32:21)*

- **Q:** Where on GitHub can you see the list of all a repository's branches?
    - **A:** The branch button next to the branch dropdown. *(00:33:16)*

## 9. Opening a pull request ([9.1 Creating a pull request](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/github-pull-requests.html#creating-a-pull-request))

*00:33:40–00:41:16*

- **Q:** What does the button GitHub shows after you push a branch say?
    - **A:** "Compare and Pull Request" (Compare & pull request). *(00:34:25)*

- **Q:** How long did the instructor say the "Compare & pull request" pop-up lasts, and how do you reach the same page once it's gone?
    - **A:** About a day. Go to the branches tab, find your branch, open its expansion menu and choose "New pull request". *(00:35:00)*

- **Q:** In which later course did the instructor say the merge target will not always be `main`?
    - **A:** DSCI 524. *(00:36:14)*

- **Q:** What title did the instructor give pull request #1 in `2026-11-17-git`?
    - **A:** "Learning about branches and PRs". *(00:37:15)*

- **Q:** What description did the instructor write for pull request #1?
    - **A:** "We are learning about Git switch and creating PRs." *(00:37:21)*

- **Q:** Name the junk files the instructor listed as ones that should not appear in a pull request's changed files.
    - **A:** `.ipynb_checkpoints` from Jupyter, `.DS_Store` on a Mac, and hidden backup files from Microsoft Word. Your `.gitignore` is still really important. *(00:39:23)*

- **Q:** What did the instructor warn happens if files that don't belong appear in your repository?
    - **A:** Points are taken off, even if the instructions don't explicitly say so. *(00:38:44)*

- **Q:** What did the instructor call reviewing the changed-files list on GitHub, after reviewing on your own computer?
    - **A:** The second line of defence. *(00:39:42)*

- **Q:** Which green button finally creates the pull request?
    - **A:** "Create Pull Request". *(00:39:56)*

- **Q:** Where can you find a pull request again after leaving its page?
    - **A:** The Pull Request tab at the top of the repository. *(00:40:15)*

- **Q:** Which comment on a pull request should you edit as the work grows, rather than adding new comments?
    - **A:** The very first comment, because that is what people read. *(00:40:55)*

## 10. Code review and updating a pull request ([10 Code review on GitHub](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/github-code-review.html))

*00:41:16–00:45:41*

- **Q:** Name the pull request tab where code review happens.
    - **A:** Files Changed. *(00:41:16)*

- **Q:** What does the Files Changed tab show you?
    - **A:** The diff between the original file and the new file. *(00:41:22)*

- **Q:** How do you leave a comment on a specific line in the Files Changed tab?
    - **A:** Hover over the line and click the little plus button. *(00:41:34)*

- **Q:** Recall the example review comment the instructor left on pull request #1.
    - **A:** Asking why switch is used and not checkout. *(00:41:34)*

- **Q:** Whose job is it to fix the code in a pull request after review?
    - **A:** The author's: the reviewer says what to rewrite, and it is your job, as the person who opened the pull request, to fix it. *(00:42:17)*

- **Q:** How do you update an open pull request with new changes?
    - **A:** Go back to the same branch on your computer, then add, commit and push. You don't close the pull request and create a new one. *(00:43:15)*

- **Q:** Which command did the instructor add to `README.md` on `dan-b1` to update pull request #1?
    - **A:** `git log --oneline --graph --decorate --all`. *(00:43:36)*

- **Q:** What was the commit message of the second commit on `dan-b1`?
    - **A:** `show you the long git log command`. *(00:44:12)*

- **Q:** What does GitHub do to a review comment on a line you later change?
    - **A:** It may auto-collapse it and mark it as outdated. *(00:45:02)*

## 11. AI reviewers and draft pull requests ([9.2 Draft pull requests](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/github-pull-requests.html#draft-pull-requests))

*00:52:11–00:55:41*

- **Q:** Name the AI tool GitHub lets you request a review from.
    - **A:** Copilot. *(00:52:30)*

- **Q:** List the three things you can do with an LLM reviewer's comment.
    - **A:** Push back on it, reject it, or accept it. You don't have to keep every comment. *(00:53:01)*

- **Q:** Which button turns an open pull request into a draft, and where is it?
    - **A:** "Convert to Draft", in the top right corner. *(00:53:52)*

- **Q:** What colour bar does a draft pull request show instead of green?
    - **A:** Gray. *(00:54:04)*

- **Q:** What happens to the merge button on a draft pull request?
    - **A:** It is grayed out, so no one can accidentally merge it. *(00:54:30)*

- **Q:** How long has the instructor kept draft pull requests open?
    - **A:** Three or four months. *(00:55:00)*

- **Q:** What did the instructor believe a draft pull request also stops an AI agent from doing?
    - **A:** Merging everything that's green. *(00:55:03)*

- **Q:** Which button turns a draft back into an open pull request, and where is it?
    - **A:** "Ready for review", at the bottom of the pull request where it says it is a work in progress. *(00:55:28)*

## 12. Merging and deleting the branch on GitHub ([8.2 Useful things you can do with branches on GitHub](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#useful-things-you-can-do-with-branches-on-github))

*00:55:41–00:59:07*

- **Q:** What does the instructor do on GitHub after a pull request is merged?
    - **A:** He deletes the branch on GitHub, so the branch list doesn't become a giant list. *(00:56:08)*

- **Q:** When did the instructor say you should not delete branches?
    - **A:** When there is a legal or compliance requirement: some places don't allow it. *(00:57:00)*

- **Q:** After merging pull request #1 and deleting its branch, what happened to the pull request counter and the branch count?
    - **A:** The pull request counter went down by one, and the branch count went from two to one. *(00:57:42)*

- **Q:** Quote the merge commit message that appeared in `main`'s history after pull request #1 was merged.
    - **A:** `Merge pull request #1 from chendaniely/dan-b1`. *(00:58:10)*

- **Q:** Does deleting the branch delete its commits?
    - **A:** No. The commits are still in history; only the branch marker is gone. *(00:58:19)*

## 13. Syncing and cleaning up locally after a merge ([8.1.3 Useful command line Git branching commands](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#useful-command-line-git-branching-commands))

*00:59:07–01:03:51*

- **Q:** Which individual assignment did the instructor say has you review merge conflicts again?
    - **A:** Individual assignment one. *(00:59:07)*

- **Q:** Which command did the instructor run on `main` to sync it after pull request #1 was merged?
    - **A:** `git pull origin main`. *(01:00:27)*

- **Q:** What did `git pull origin main` report changed after pull request #1 was merged?
    - **A:** A fast-forward adding new lines to `README.md` (6 insertions), which were the merged pull request's changes. *(01:00:41)*

- **Q:** Which command lists all the branches your computer knows of, including remote ones?
    - **A:** `git branch -a`. *(01:01:06)*

- **Q:** In `git branch -a` output, what marks the branch you are on?
    - **A:** A star (`*`) next to it. *(01:01:11)*

- **Q:** What does `git fetch --prune` remove?
    - **A:** Local references to branches that were deleted on GitHub. *(01:01:30)*

- **Q:** What did `git fetch --prune` print in class?
    - **A:** `- [deleted] (none) -> origin/dan-b1`. *(01:01:30)*

- **Q:** Name the two commands `git pull` runs.
    - **A:** `fetch`, then `merge` on top. *(01:01:52)*

- **Q:** When should you run `git fetch` alone instead of `git pull`?
    - **A:** When you don't want the files on your computer to change. *(01:01:52)*

- **Q:** Which command deletes a local branch only if it has been merged?
    - **A:** `git branch -d <branch>`, with a lowercase `d`. In class: `git branch -d dan-b1`. *(01:02:54)*

- **Q:** What does `git branch -D` (capital `D`) do, and what did the instructor warn about it?
    - **A:** It force-deletes a branch even if it hasn't been merged, which can delete the commits you're working on. Be very careful copying commands from ChatGPT, which might give you capital `-D`. *(01:03:21)*

## 14. Setting up two conflicting pull requests

*01:04:00–01:10:00*

- **Q:** Define what causes a merge conflict, as stated in class.
    - **A:** The same change to the same line of the same file. *(01:04:00)*

- **Q:** Name the two branches the instructor created to produce a conflict.
    - **A:** `dan-fetch` and `dan-delete`, both created from `main`. *(01:04:35)*

- **Q:** What was the commit message on `dan-fetch`, and which pull request did it become?
    - **A:** `define fetch --prune`; it became pull request #2. *(01:05:32)*

- **Q:** What did the instructor say is the key to practising merge conflicts on your own with two branches?
    - **A:** Not merging the first pull request immediately. *(01:06:07)*

- **Q:** What error did `git switch -b dan-delete` give?
    - **A:** ``error: unknown switch `b'``. The working command was `git switch -c dan-delete`. *(01:06:40)*

- **Q:** What was the commit message on `dan-delete`, and which pull request did it become?
    - **A:** `branch -d and -D`; it became pull request #3. *(01:07:51)*

- **Q:** What does `git log --oneline --graph --all --decorate` show for `dan-fetch` and `dan-delete`?
    - **A:** Two lines coming out of the same `main` commit: two parallel pieces of work. *(01:08:53)*

- **Q:** Which line of `README.md` did the instructor say had two conflicting sets of changes?
    - **A:** Line thirteen. *(01:09:28)*

- **Q:** What does a GitHub pull request page tell you about an upcoming conflict before another pull request is merged?
    - **A:** Nothing: it just says you can merge into `main`. *(01:09:48)*

## 15. When a merge creates the conflict: resolving on GitHub

*01:10:00–01:12:44*

- **Q:** What does GitHub do to every other pull request targeting `main` when one is merged?
    - **A:** It rechecks each one to see whether it can still be merged. *(01:10:19)*

- **Q:** Where on GitHub can you resolve a simple conflict?
    - **A:** In the web editor. *(01:10:54)*

- **Q:** Name the conflict markers you look for when fixing a conflict.
    - **A:** The "less, equal, greater" markers: `<<<<<<<`, `=======`, `>>>>>>>`. *(01:10:59)*

- **Q:** State what "fixed" means for report writing after a conflict.
    - **A:** Whatever is left is English that makes sense. *(01:11:09)*

- **Q:** State what "fixed" means for code after a conflict, and the warning that came with it.
    - **A:** Your code must work from top to bottom again, not just have the markers removed. A conflict on line 13 can break code elsewhere, such as a variable used on line 50, and that is still your problem. *(01:11:39)*

## 16. Resolving the conflict locally with rebase ([8.3.2 Using rebase](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#using-rebase))

*01:12:44–01:20:42*

- **Q:** Name the command the instructor uses to fix conflicts on his own computer.
    - **A:** `rebase`. He said people who know Git will have opinions, and there are many ways to do it. *(01:14:04)*

- **Q:** State what `git rebase main` does to your branch's commits.
    - **A:** It replays the commits in your branch on top of the `main` branch. *(01:17:14)*

- **Q:** List the two commands the instructor ran first to sync `main` before rebasing.
    - **A:** `git switch main`, then `git pull origin main`. *(01:16:25)*

- **Q:** Reproduce the two commands that started the rebase of `dan-delete`.
    - **A:** `git switch dan-delete`, then `git rebase main`. *(01:17:08)*

- **Q:** What did `git rebase main` print when it stopped on `dan-delete`?
    - **A:** `CONFLICT (content): Merge conflict in README.md` and `error: could not apply cb810d5... branch -d and -D`. *(01:17:21)*

- **Q:** How did the instructor resolve the conflict in `README.md`?
    - **A:** He kept both definitions and cleaned up some whitespace. *(01:17:46)*

- **Q:** In DSCI 521, which command triggered merge conflicts, compared with `git rebase main` here?
    - **A:** `git pull origin main`. *(01:17:56)*

- **Q:** Which option lets you back out of a rebase if something goes wrong?
    - **A:** Abort: `git rebase --abort`. *(01:18:20)*

- **Q:** Which command marks a conflicted file as resolved during a rebase?
    - **A:** `git add`; in class, `git add README.md`. *(01:18:32)*

- **Q:** Which command finishes the rebase once all conflicts are fixed?
    - **A:** `git rebase --continue`, which asks you to confirm the commit message. *(01:18:44)*

- **Q:** Reproduce the push command that finally updated `dan-delete` on GitHub after the rebase.
    - **A:** `git push --force-with-lease origin dan-delete`. *(01:19:47)*

- **Q:** What error came from the first try at force-pushing `dan-delete`?
    - **A:** ``error: unknown option `force-with-leasse'``, a typo for `--force-with-lease`. *(01:19:34)*

- **Q:** What did the instructor warn about the force push after a rebase?
    - **A:** You can't avoid force pushing, because the history has changed. GitHub records that a force push happened: "you've mangled history", which is somewhat of a compliance issue. *(01:20:21)*

- **Q:** What did the successful force push to `dan-delete` print at the end?
    - **A:** `+ cb810d5...0e16503 dan-delete -> dan-delete (forced update)`. *(01:19:47)*

---

- prompt: prompt-recall-1-remember.md @ 65eb21c
- prompt-hash: e448f8420cdb
- model: claude-opus-5-5 (requested: opus)
- backend: claude
- inputs: transcript-plaud.md, terminal.txt, materials.md, notes-class-main--claude-opus-5-5.md
- generated: 2026-11-23
- notes-input: notes-class-main--claude-opus-5-5.md @ d979d4ea6828, links and section references removed, diagrams removed
