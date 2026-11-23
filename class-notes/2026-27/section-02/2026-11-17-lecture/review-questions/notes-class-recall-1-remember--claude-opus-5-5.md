# Git branches, pull requests and rebasing: review questions, tier 1 — Remember

Date: 2026-11-17

Instructor: Daniel Chen

*Tier 1 of 5: Remember. Answer each question before you read its answer; tiers 2 to 5 build on these.*

## 1. Course logistics: lab groups, attendance and interview week

*00:00:01–00:04:04*

- **Q:** Where do you look up your DSCI 522 lab group?
  **A:** In the lab sections repository on GitHub. Find your lab section, then the group number column; everyone with the same number is in your group. *(00:00:56)*

- **Q:** What are the GitHub usernames students submitted used for?
  **A:** They build a main list of everyone's GitHub usernames. That list is a piece of metadata used everywhere else in the program. *(00:02:01)*

- **Q:** State the attendance rule for 522 labs.
  **A:** Lab attendance is mandatory. TAs go around and talk to every group, and you should be there when a TA comes to yours. *(00:02:19)*

- **Q:** How long is the interview-week conversation, and what is it modelled on?
  **A:** About seven minutes, run like a technical interview. *(00:02:50)*

- **Q:** What two things does the interview-week conversation cover?
  **A:** How much you know about Git, and your group's actual code base. Anything in the code base is fair game. *(00:03:15)*

- **Q:** Does the interview-week conversation affect your grade?
  **A:** No. You get a grade, but it doesn't affect your course grade. *(00:03:02)*

- **Q:** What did the instructor say this interview format might become next year?
  **A:** The exam. *(00:03:48)*

## 2. Git recap: setting up the demo repository

*00:04:07–00:06:49*

- **Q:** What is the name of the demo repository the instructor created and cloned?
  **A:** `2026-11-17-git`, named for the day's date, under `chendaniely`. *(00:04:51)*

- **Q:** Which file was the demo repository initialized with, instead of starting empty?
  **A:** A README. The instructor noted you could also add a Python `.gitignore` and a license. *(00:05:06)*

- **Q:** What did the instructor add to `README.md` as the first change?
  **A:** A line saying the class will review 521 Git basics and then go into branches, plus a link to the textbook's Git branches chapter. *(00:05:57)*

- **Q:** What commit message did the instructor use for that first commit on `main`?
  **A:** `intro and review`. *(00:06:32)*

## 3. Why branches: escaping the 521 push/pull friction ([8 Git branches](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html))

*00:06:49–00:09:43*

- **Q:** Which DSCI 521 week-3 exercise did the instructor recall as an example of push/pull friction?
  **A:** Creating a shared slide deck together. *(00:06:54)*

- **Q:** What step was always needed in that exercise before you could push, even when there was no conflict?
  **A:** You had to pull first, because someone else had pushed before you. *(00:07:06)*

- **Q:** What kind of work does the instructor want groups to reach in a project?
  **A:** Parallel streams of work, where each person is responsible for their own self-contained part. *(00:08:41)*

- **Q:** In the instructor's example timeline, which day did the group review and coordinate everyone's work?
  **A:** Friday, after each person worked on their own part from Tuesday to Friday. *(00:08:46)*

## 4. Review: the local–remote picture

*00:09:46–00:11:47*

- **Q:** What are the two places your work can live?
  **A:** Your computer (local) and the cloud (the GitHub remote). *(00:10:09)*

- **Q:** Which copy of the work is the one that's graded and published?
  **A:** The copy on the GitHub remote. Work that exists only on your computer effectively doesn't exist for grading or project purposes. *(00:10:53)*

- **Q:** Which Git command did the instructor call a one-time command?
  **A:** `git clone`. *(00:11:25)*

- **Q:** Name the command that sends commits up to GitHub and the one that brings teammates' commits down.
  **A:** `git push` sends commits up, and `git pull` brings commits down. *(00:11:33)*

## 5. What a branch is: `main`, `HEAD` and `origin/main`

*00:12:03–00:17:54*

- **Q:** What is the `main` branch?
  **A:** The default branch you work on. *(00:12:38)*

- **Q:** What happens to the `main` branch each time you commit while `HEAD` is attached to it?
  **A:** `main` moves forward (increments) with each commit. *(00:13:17)*

- **Q:** What does `origin/main` represent?
  **A:** The remote: what your computer thinks the state of `main` on GitHub is. *(00:13:30)*

- **Q:** Define a branch as the instructor described it.
  **A:** A name you choose yourself that moves forward when you commit, instead of `main` moving. The `git add`/`git commit` process stays the same. *(00:13:55)*

- **Q:** What did the instructor say the `main` branch should be treated as?
  **A:** The production or final version: the stable place where at least the code works. *(00:15:10)*

- **Q:** Do you need collaborators to use branches?
  **A:** No. Branches are useful when working alone too, to section off work. *(00:16:05)*

- **Q:** What real project did the instructor say he edited entirely in branches, and why?
  **A:** The course textbook. Another instructor was teaching from it that day, and he didn't want pages moving around mid-lecture. *(00:16:37)*

- **Q:** Which two DSCI 521 commands did the instructor name as another way to undo work, besides using branches?
  **A:** `git reset` and `git revert`. *(00:17:22)*

## 6. Creating and switching branches ([8.1 Creating a branch using the command line](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#creating-a-branch-using-the-command-line))

*00:17:54–00:26:29*

- **Q:** What command did the instructor run first, to confirm he was on `main` before creating a branch?
  **A:** `git status`. *(00:18:03)*

- **Q:** Which command syncs your starting point before you create a branch that builds on coordinated work?
  **A:** `git pull origin main`. *(00:18:39)*

- **Q:** Define `git switch`.
  **A:** The command that moves `HEAD` around the repository, switching between branches. *(00:19:46)*

- **Q:** What does the `-c` flag in `git switch -c <name>` stand for, and what does the command do?
  **A:** `-c` is for create. The command creates a new branch and moves `HEAD` to it. *(00:20:09)*

- **Q:** What name did the instructor give the first branch he created?
  **A:** `dan-b1`. *(00:21:31)*

- **Q:** What does the instructor put at the start of branch names in shared repositories?
  **A:** His own name, so others know whom to talk to about that branch. *(00:20:31)*

- **Q:** What did `git switch -c dan-b1` print?
  **A:** `Switched to a new branch 'dan-b1'`. *(00:20:58)*

- **Q:** After `git switch -c dan-b1`, what did `git status` report?
  **A:** `On branch dan-b1`, with nothing to commit. The only change was the branch name. *(00:21:03)*

- **Q:** What line did the instructor add to `README.md` on `dan-b1`?
  **A:** `` `switch -c <name>`: create and move HEAD to the branch <name> ``. *(00:21:56)*

- **Q:** What commit message did the instructor use for the first commit on `dan-b1`?
  **A:** `define swtich -c`, typed with that spelling. *(00:22:31)*

- **Q:** Which view in VS Code or Positron shows the same branch picture as the terminal log?
  **A:** The graph view in the Git tab. *(00:23:51)*

- **Q:** What command moved `HEAD` from `dan-b1` back to `main`?
  **A:** `git switch main`. *(00:25:12)*

- **Q:** Which flag must you add to `git log --oneline` to see your other branches?
  **A:** `--all`, as in `git log --oneline --graph --decorate --all`. *(00:25:38)*

## 7. `git checkout` and `git branch` versus `git switch` ([8.1.3 Useful command line Git branching commands](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#useful-command-line-git-branching-commands))

*00:26:40–00:28:26*

- **Q:** Will students be tested on using `git checkout` instead of `git switch`?
  **A:** No. The instructor said using `checkout` is fine and he won't test students on it. *(00:26:42)*

- **Q:** Roughly when was `git switch` introduced, replacing part of what `git checkout` did?
  **A:** Around 2019 to 2020. *(00:26:59)*

- **Q:** Which command does the instructor use himself day to day, and when does he use `switch`?
  **A:** He uses `git checkout`. He only uses `switch` when teaching. *(00:26:59)*

- **Q:** Besides moving `HEAD`, what else did `git checkout` do?
  **A:** Much of what `restore` and `revert` do. Those newer commands came out of `checkout`, and `checkout` still has those behaviours. *(00:27:09)*

- **Q:** What should you ask an AI tool to do if it tells you to run a `checkout` command you don't understand?
  **A:** Ask it to do the same thing with `switch` instead. *(00:27:44)*

- **Q:** Name the `git checkout` equivalent of `git switch -c <name>`.
  **A:** `git checkout -b <name>`. *(00:28:10)*

- **Q:** What does `git branch <name>` do, and what doesn't it do?
  **A:** It creates the branch but doesn't move you to it. You still have to `checkout` or `switch` afterwards. *(00:28:13)*

## 8. Pushing a branch and viewing it on GitHub ([8.2 Useful things you can do with branches on GitHub](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#useful-things-you-can-do-with-branches-on-github))

*00:28:31–00:33:40*

- **Q:** What two names did the instructor give for the review process used to get a branch into `main`?
  **A:** A pull request, or a merge request. *(00:28:58)*

- **Q:** Which command is the only one that links your local work to the remote?
  **A:** `git push`. *(00:29:22)*

- **Q:** What did a plain `git push`, run while on `main`, print in class?
  **A:** `Everything up-to-date`. It didn't send `dan-b1`. *(00:29:34)*

- **Q:** What command pushed the `dan-b1` branch to GitHub?
  **A:** `git push origin dan-b1`. *(00:30:36)*

- **Q:** Besides pushing, what did `git push origin dan-b1` print about pull requests?
  **A:** A link to create a pull request for `dan-b1`: `https://github.com/chendaniely/2026-11-17-git/pull/new/dan-b1`. *(00:30:36)*

- **Q:** After pushing `dan-b1`, which new reference appeared in `git log --oneline --graph --decorate --all`?
  **A:** `origin/dan-b1`, at the same commit as `dan-b1`. `origin/main` had not moved. *(00:31:19)*

- **Q:** Where on a GitHub repository page do you switch to view a branch like `dan-b1`?
  **A:** The dropdown in the top left-hand corner, which says `main`. *(00:32:21)*

- **Q:** Which GitHub button lists all of a repository's branches?
  **A:** The branch button next to the branch dropdown. *(00:33:16)*

## 9. Opening a pull request ([9.1 Creating a pull request](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/github-pull-requests.html#creating-a-pull-request))

*00:33:40–00:41:16*

- **Q:** What does the button say on the pop-up GitHub shows after you push a branch?
  **A:** "Compare & pull request". *(00:34:25)*

- **Q:** Roughly how long does that pop-up stay before it disappears?
  **A:** About a day. *(00:34:32)*

- **Q:** If the pop-up has gone, where can you start a pull request for your branch?
  **A:** In the Branches tab: find your branch, open its menu, and choose "New pull request". *(00:35:00)*

- **Q:** In which later course did the instructor say the merge target will not always be `main`?
  **A:** DSCI 524. *(00:36:14)*

- **Q:** What title did the instructor give pull request #1 in the demo repository?
  **A:** "Learning about branches and PRs". *(00:37:15)*

- **Q:** What description did the instructor write for pull request #1?
  **A:** "We are learning about Git switch and creating PRs." *(00:37:21)*

- **Q:** Name two kinds of files the instructor said shouldn't appear in a pull request's changed files.
  **A:** Jupyter's `.ipynb_checkpoints` and the Mac `.DS_Store`. Microsoft Word backup files are another example. Files like these lose points even when the instructions don't explicitly mention them. *(00:39:16)*

- **Q:** If work you expected is missing from a pull request's file list, what did you probably do?
  **A:** Typed something wrong, or forgot to add, commit and push. *(00:39:37)*

- **Q:** Which green button finishes opening the pull request?
  **A:** "Create Pull Request". *(00:39:56)*

- **Q:** Where can you find a pull request again after leaving its page?
  **A:** The Pull Requests tab at the top of the repository. *(00:40:15)*

- **Q:** When a pull request grows, which comment should you edit instead of adding new ones?
  **A:** The very first comment, because that's what people read. *(00:40:55)*

## 10. Code review and updating a pull request ([10 Code review on GitHub](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/github-code-review.html))

*00:41:16–00:45:41*

- **Q:** Which pull request tab is where code review happens?
  **A:** The "Files Changed" tab, which shows the diff between the original and new files. *(00:41:16)*

- **Q:** How do you leave a comment on a specific line in a pull request's diff?
  **A:** Hover over the line and click the little plus (`+`) button. *(00:41:34)*

- **Q:** What was the instructor's example review comment?
  **A:** "Why are you using switch and not checkout?" *(00:41:34)*

- **Q:** In code review, whose job is it to fix the code?
  **A:** The pull request's author. The reviewer's job is to point out problems, not to fix them. *(00:42:17)*

- **Q:** How do you update an open pull request with new changes?
  **A:** Go back to the same branch locally, add, commit and push to it, and the pull request updates. You don't need to close it and open a new one. *(00:43:15)*

- **Q:** What commit message did the instructor use for the second commit on `dan-b1`?
  **A:** `show you the long git log command`. *(00:44:12)*

- **Q:** What does GitHub do to a review comment when you change the line it was on?
  **A:** It may auto-collapse the comment and mark it as outdated. *(00:45:02)*

## 11. AI reviewers and draft pull requests ([9.2 Draft pull requests](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/github-pull-requests.html#draft-pull-requests))

*00:52:11–00:55:41*

- **Q:** Which AI tool can you ask on GitHub to review a pull request?
  **A:** Copilot. You don't have to keep every comment it makes: you can push back, reject or accept. *(00:52:30)*

- **Q:** Which button turns an open pull request into a draft, and where is it?
  **A:** "Convert to Draft", in the top right corner. *(00:53:52)*

- **Q:** What colour bar marks a draft pull request?
  **A:** Gray instead of green. *(00:54:04)*

- **Q:** What happens to the merge button on a draft pull request?
  **A:** It's grayed out, so no one can merge it by accident. *(00:54:30)*

- **Q:** How long has the instructor kept draft pull requests open?
  **A:** Three or four months. *(00:54:56)*

- **Q:** Which button turns a draft back into an open pull request, and where is it?
  **A:** "Ready for review", at the bottom of the pull request where it says the pull request is a work in progress. *(00:55:28)*

## 12. Merging and deleting the branch on GitHub ([8.2 Useful things you can do with branches on GitHub](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#useful-things-you-can-do-with-branches-on-github))

*00:55:41–00:59:07*

- **Q:** What does the instructor do on GitHub right after a pull request is merged?
  **A:** He deletes the branch on GitHub. *(00:56:08)*

- **Q:** When did the instructor say you should not delete branches?
  **A:** When a law or compliance rule requires keeping them. *(00:57:00)*

- **Q:** After merging #1 and clicking delete branch, what happened to the repository's pull request and branch counts?
  **A:** The open pull request count went down by one, and the branch count went from two to one. *(00:57:42)*

- **Q:** What message did the merge commit for pull request #1 have?
  **A:** `Merge pull request #1 from chendaniely/dan-b1`. *(00:58:10)*

- **Q:** Does deleting a merged branch delete its commits?
  **A:** No. The commits remain in history, along with a separate merge commit. *(00:58:19)*

## 13. Syncing and cleaning up locally after a merge ([8.1.3 Useful command line Git branching commands](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#useful-command-line-git-branching-commands))

*00:59:07–01:03:51*

- **Q:** Which individual assignment has students practise merge conflicts again?
  **A:** Individual assignment 1. *(00:59:07)*

- **Q:** What command updated local `main` after pull request #1 was merged on GitHub?
  **A:** `git pull origin main`, run while on `main`. *(01:00:27)*

- **Q:** What did that `git pull origin main` report about `README.md`?
  **A:** A fast-forward that added 6 lines to `README.md` (`6 insertions(+)`). These were the merged pull request's changes. *(01:00:41)*

- **Q:** Which command lists all the branches your computer knows about, including remote ones?
  **A:** `git branch -a`. *(01:01:06)*

- **Q:** In `git branch -a` output, what marks the branch you're on?
  **A:** A star (`*`). *(01:01:11)*

- **Q:** Which command removes local references to branches deleted on GitHub?
  **A:** `git fetch --prune`. *(01:01:30)*

- **Q:** What did `git fetch --prune` print in class?
  **A:** `- [deleted]         (none)     -> origin/dan-b1`. *(01:01:30)*

- **Q:** Which two commands does `git pull` run?
  **A:** `git fetch`, then a merge. *(01:01:52)*

- **Q:** Which command deletes a local branch only if it has been merged?
  **A:** `git branch -d <branch>`, with a lowercase `d`. *(01:02:54)*

- **Q:** What does `git branch -D` (capital `D`) do, and what warning came with it?
  **A:** It force-deletes a branch even if it hasn't been merged, which can delete commits you're still working on. Be very careful copying commands from ChatGPT, which may hand you capital `-D`. *(01:03:21)*

## 14. Setting up two conflicting pull requests

*01:04:00–01:10:00*

- **Q:** What kind of change causes a merge conflict?
  **A:** Two different changes to the same line of the same file. *(01:04:00)*

- **Q:** Name the two branches the instructor created to cause a conflict.
  **A:** `dan-fetch` and `dan-delete`. *(01:04:35)*

- **Q:** What commit message did the instructor use on `dan-fetch`?
  **A:** `define fetch --prune`. *(01:05:36)*

- **Q:** What did the instructor say is the key to practising merge conflicts on your own?
  **A:** Don't merge the first pull request right away. *(01:06:07)*

- **Q:** What error did `git switch -b dan-delete` produce in class?
  **A:** ``error: unknown switch `b'``. The working command was `git switch -c dan-delete`. *(01:06:40)*

- **Q:** What commit message did the instructor use on `dan-delete`?
  **A:** `branch -d and -D`. *(01:07:51)*

- **Q:** Which pull request numbers came from `dan-fetch` and `dan-delete`?
  **A:** #2 (`define fetch --prune`) came from `dan-fetch`, and #3 (`branch -d and -D`) came from `dan-delete`. *(01:09:11)*

- **Q:** What did `git log --oneline --graph --all --decorate` show after both branches were committed?
  **A:** Two lines coming out of the same `main` commit: two parallel pieces of work. *(01:08:19)*

- **Q:** Before either pull request was merged, did GitHub warn that #2 and #3 would conflict?
  **A:** No. Each pull request on its own showed nothing indicating a merge conflict. *(01:09:53)*

## 15. When a merge creates the conflict: resolving on GitHub ([8.3 What happens when my feature branch falls behind main?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#what-happens-when-my-feature-branch-falls-behind-main))

*01:10:00–01:12:44*

- **Q:** What does GitHub do to other pull requests targeting `main` when one of them is merged?
  **A:** It rechecks each one to see whether it can still be merged. *(01:10:19)*

- **Q:** Which GitHub tool can resolve simple conflicts without your local computer?
  **A:** The web editor. *(01:10:54)*

- **Q:** Name the three conflict markers you look for when fixing a conflict.
  **A:** Less-than, equals and greater-than markers: `<<<<<<<`, `=======` and `>>>>>>>`. *(01:10:59)*

- **Q:** State what "fixing" a conflict means for code in this course.
  **A:** Your code must work from top to bottom again, not just have the markers removed. A conflict on line 13 can still break something on line 50. *(01:11:21)*

## 16. Resolving the conflict locally with rebase ([8.3.2 Using rebase](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#using-rebase))

*01:12:44–01:20:42*

- **Q:** Which Git command does the instructor use to fix conflicts on a branch locally?
  **A:** `git rebase`. *(01:14:04)*

- **Q:** Define what a rebase does, in the instructor's words.
  **A:** It replays your branch's commits on top of the existing changes. *(01:14:31)*

- **Q:** What two commands synced `main` before the rebase?
  **A:** `git switch main`, then `git pull origin main`. *(01:16:25)*

- **Q:** What two commands started the rebase of the conflicting branch?
  **A:** `git switch dan-delete`, then `git rebase main`. *(01:17:01)*

- **Q:** What did `git rebase main` print when it hit the conflict?
  **A:** `CONFLICT (content): Merge conflict in README.md`, followed by `error: could not apply cb810d5... branch -d and -D`. *(01:17:14)*

- **Q:** How did the instructor resolve the `README.md` conflict?
  **A:** He kept both definitions and cleaned up some whitespace. *(01:17:46)*

- **Q:** In DSCI 521, which command triggered merge conflicts, compared with the one used here?
  **A:** In 521 it was `git pull origin main`. Here it was `git rebase main`. *(01:17:56)*

- **Q:** Which option gets you out of a rebase if something goes wrong?
  **A:** `git rebase --abort`. *(01:18:20)*

- **Q:** After fixing the conflict markers, which two commands completed the rebase?
  **A:** `git add README.md` to mark the resolution, then `git rebase --continue`. *(01:18:32)*

- **Q:** What exact command pushed the rebased `dan-delete` branch?
  **A:** `git push --force-with-lease origin dan-delete`. *(01:19:34)*

- **Q:** What error came from the first attempt at the force push?
  **A:** ``error: unknown option `force-with-leasse'`` because the option was misspelled. *(01:19:34)*

- **Q:** What did the successful force push print for `dan-delete`?
  **A:** `+ cb810d5...0e16503 dan-delete -> dan-delete (forced update)`. *(01:19:47)*

- **Q:** After a rebase, can you push without forcing, and what does GitHub show afterwards?
  **A:** No. You can't avoid a force push, because the rebase changed the branch's history. GitHub then records that a force push happened. *(01:20:17)*

- **Q:** How did the instructor describe a force push after a rebase, in compliance terms?
  **A:** You've "mangled history". *(01:20:21)*

- **Q:** Which two commands clean up locally after a rebased pull request is merged?
  **A:** `git fetch --prune` and `git branch -d`. *(01:20:35)*

---

- prompt: prompt-recall-1-remember.md @ 8bcc190
- prompt-hash: cbbf92455214
- model: claude-opus-5-5 (requested: opus)
- backend: claude
- inputs: transcript-plaud.md, terminal.txt, materials.md, notes-class-main--claude-opus-5-5.md
- generated: 2026-11-20
- notes-input: notes-class-main--claude-opus-5-5.md @ d979d4ea6828, links and section references removed
