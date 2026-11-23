# Git branches, pull requests and rebasing to fix conflicts: review questions, tier 2 — Understand

Date: 2026-11-17

Instructor: Daniel Chen

*Tier 2 of 5: Understand. Explain each answer in your own words before you read it; tier 1 (Remember) covers the facts, tiers 3 to 5 put them to use.*

## 1. Course logistics: lab groups, attendance and interview week

*00:00:01–00:04:04*

- **Q:** Why did the instructor insist that every student submit a correct GitHub username?
  **A:** The usernames build a main list of students that fills the GitHub username column of the lab sections repository. That list is metadata used "under the hood" everywhere else in the program, so a wrong username causes problems beyond this course. *(00:02:01)*

- **Q:** Explain why lab attendance is mandatory in DSCI 522 this year.
  **A:** The course is built around a group project. During lab the TAs go around and talk to every single group, so you need to be there when a TA reaches your group. *(00:02:19)*

- **Q:** Why can the seven-minute interview-week conversation cover anything in your group's code base, not only Git?
  **A:** You are expected to know the code base you work in, "especially in the world of AI." As at work, anything in the repository is fair game, so you should know what it does. The interview does not affect your grade. *(00:03:15)*

## 2. Why branches: escaping the 521 push/pull friction ([8 Git branches](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html))

*00:06:49–00:09:43*

- **Q:** In the 521 shared slide-deck exercise, what friction did students hit even when there was no merge conflict?
  **A:** When you finished your part and tried to push, you often couldn't, because someone else had pushed first. You had to pull before you could push again. Any time two people work on the same thing at the same time, that friction appears, whether or not there is a conflict. *(00:07:06)*

- **Q:** Why will the push/pull friction from 521 still show up somewhere in every group project?
  **A:** Not every project can start with four parallel pieces of work. Early on, the whole group is blocked on one or two people getting the basics in place, so for a while everyone works on the same shared state. *(00:07:50)*

- **Q:** How do parallel streams of work on branches let a teammate work from Tuesday to Friday without worrying about what others are doing?
  **A:** Each person works on a branch, "in your own little world," and can push and pull it freely until the work is done. If the work is self-contained, other people's pushes don't matter. The group then reviews and coordinates everyone's work at one point, for example on Friday. *(00:08:46)*

## 3. Review: the local–remote picture

*00:09:46–00:11:47*

- **Q:** Why did the instructor say that work existing only on your laptop "effectively doesn't really exist"?
  **A:** The GitHub remote is what gets graded and published. Work that isn't pushed can't be graded or used by the project, just as a product at work isn't shipped if its code is only on your computer. *(00:10:53)*

- **Q:** How does adding teammates change the local–remote picture?
  **A:** You still coordinate your computer with the GitHub remote, but each of your teammates must coordinate their own computer with that same remote. That makes a lot of coordination work, and the remote is the shared point that matters. *(00:10:38)*

- **Q:** Compare the roles of `clone`, `push` and `pull` in the local–remote diagram.
  **A:** `clone` is a one-time command that brings the repository down to your computer. `push` sends your local commits up to GitHub. `pull` brings down commits that teammates pushed, so you can coordinate their work onto your computer. *(00:11:33)*

## 4. What a branch is: `main`, `HEAD` and `origin/main` ([8 Git branches](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html))

*00:12:03–00:17:54*

- **Q:** What is the difference between `main` and `origin/main` in the output of `git log --oneline --graph --decorate --all`?
  **A:** `main` is your local branch, and it moves forward each time you commit while `HEAD` is attached to it. `origin/main` is what your computer *thinks* the state of GitHub is. If you commit on `main` without pushing, local `main` gets ahead of `origin/main`. *(00:13:39)*

- **Q:** How does committing on a branch differ from committing on `main`?
  **A:** The workflow is the same: `git add`, then `git commit`. The difference is which name moves forward. On a branch, your commits advance a name you chose, such as `b1`, instead of advancing `main`. *(00:14:25)*

- **Q:** Why should `main` be treated as the stable, "production" version of the project?
  **A:** A project has other moving pieces that should move at a steady rate. You don't want an experiment that breaks on your computer to then break on all your teammates' computers. On `main`, the code should at least work, even if the project isn't finished. *(00:15:24)*

- **Q:** Give the class's example of what belongs on `main` and what stays on a branch during a data analysis.
  **A:** The cleaned dataset sits on `main`, and everyone bases their work on it. Exploratory data analysis, with plots still in progress, is not ready yet, so it stays on that person's branch. *(00:15:49)*

- **Q:** Why does the instructor use branches even in repositories where he is the only contributor?
  **A:** Branches section off work, so he can test and build things without `main` changing before he has reviewed everything. For example, he made textbook edits on branches while another instructor was teaching from the textbook, so pages wouldn't move around mid-lecture. He merged them only after reviewing and testing them. *(00:16:37)*

- **Q:** Explain why abandoning a failed idea is easier on a branch than undoing it on `main`.
  **A:** On a branch, you can say "that was a bad idea," go back to `main`, and you are at your starting point; deleting a branch is easy. If you had written one commit that did twenty different things, you would have to dig through history and copy out the relevant parts. `git reset` and `git revert` from 521 also work, but branches make this easier. *(00:17:22)*

## 5. Creating and switching branches ([8.1 Creating a branch using the command line](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#creating-a-branch-using-the-command-line))

*00:17:54–00:26:29*

- **Q:** Why run `git pull origin main` before `git switch -c` when your work builds on coordinated work?
  **A:** It syncs your starting point with everything your teammates have pushed. The instructor has created branches on one computer and then realized he had already done half the work on another laptop. Syncing first would have saved him that time. *(00:18:39)*

- **Q:** What does `git switch` actually do to the repository?
  **A:** It moves `HEAD` around the repository. You can tell which branch you are on because `HEAD` points to it in the log. `git switch -c <name>` creates a new branch and moves `HEAD` to it. *(00:19:51)*

- **Q:** Why does the instructor start his branch names with his own name, as in `dan-b1`?
  **A:** In a group repository, the name tells others whom to talk to if something on that branch looks weird. *(00:20:31)*

- **Q:** Interpret the log right after `git switch -c dan-b1`, which showed `145ff16 (HEAD -> dan-b1, origin/main, origin/HEAD, main)`.
  **A:** Nothing changed except a word. No new commit was made, so `main`, the remote references and the new `dan-b1` all point to the same commit. The only difference is that `HEAD` is now attached to `dan-b1` instead of `main`. *(00:21:15)*

- **Q:** After committing on `dan-b1`, why is `dan-b1` one commit ahead of both `main` and `origin/main`?
  **A:** Whichever branch `HEAD` is attached to gets dragged along when you commit. This time that was `dan-b1`, not `main`. `origin/main` would be behind in either case, because nothing had been pushed or synced with GitHub. *(00:23:21)*

- **Q:** What happens to the files on disk after `git switch main` from `dan-b1`, and why is that useful?
  **A:** The files return to the state they have at `main`, and the branch you left stays where it was. This lets you move between parallel states of the project, for example to try a feature or to look at a teammate's work on your own computer. *(00:25:46)*

- **Q:** Why does the instructor always type `--all` in `git log --oneline --graph --decorate --all`?
  **A:** Without the `--all` flag, the log may not show your other branch names, only the history of where you are. *(00:25:38)*

- **Q:** How does the graph in the Git tab of VS Code or Positron relate to the terminal log?
  **A:** It shows the same picture: `origin/main`, local `main` and the `dan-b1` commit. Knowing the commands and how to draw the history helps you read that graph view. *(00:24:09)*

## 6. `git checkout` and `git branch` versus `git switch` ([8.1.3 Useful command line Git branching commands](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#useful-command-line-git-branching-commands))

*00:26:40–00:28:26*

- **Q:** How is the older `git checkout` related to `git switch` and to the restore and revert commands from 521?
  **A:** `checkout` used to do what `switch` does, moving `HEAD` around, but it also did much of what the restore and revert commands do. The newer commands were carved out of `checkout`, and `checkout` still has all of those behaviours. *(00:27:09)*

- **Q:** Why should you ask an AI tool for the `switch` version when it tells you to run `git checkout`?
  **A:** `checkout` can do many different things. If you don't know what a suggested command will do, and you are worried about losing work in your codebase, you should think about the commands you type rather than run whatever works. *(00:27:48)*

- **Q:** How does `git branch <name>` differ from `git switch -c <name>` and `git checkout -b <name>`?
  **A:** `git switch -c` and its older equivalent `git checkout -b` both create the branch and move you onto it. `git branch` only creates the branch without moving you, so you still have to switch or check out afterwards. *(00:28:13)*

## 7. Pushing a branch and viewing it on GitHub ([8.2 Useful things you can do with branches on GitHub](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#useful-things-you-can-do-with-branches-on-github))

*00:28:31–00:33:40*

- **Q:** How did the class plan to get the `dan-b1` commits onto `main`, rather than merging on the laptop?
  **A:** The easiest way is not to merge on your local computer, but through a review process, using a pull request (or merge request). That means pushing the branch to GitHub first, because `push` is the only command that links local work to the remote. *(00:29:22)*

- **Q:** Why did a bare `git push` while on `main` print `Everything up-to-date` instead of sending `dan-b1`?
  **A:** With branches, *where* you push and *what* you push now matter; you are no longer pushing only `main`. Being on `main`, which had nothing new, a bare push didn't send the new branch. You have to switch to the branch you want to push and name it. *(00:29:50)*

- **Q:** Explain why the last word changes in `git push origin dan-b1` compared with the `git push origin main` you typed for ten weeks.
  **A:** The last word names the branch you are pushing. Otherwise the behaviour is the same: you send your local work for that branch up to GitHub. *(00:30:44)*

- **Q:** Interpret the log after `git push origin dan-b1`, where `origin/dan-b1` appears next to `dan-b1` but `origin/main` hasn't moved.
  **A:** GitHub now has a branch called `dan-b1` at the same commit as your local `dan-b1`. Pushing a branch doesn't change `main` at all. *(00:31:27)*

- **Q:** Why is it useful to view a pushed branch with the branch dropdown on GitHub before it is merged?
  **A:** You can confirm that your local work actually exists on GitHub. In a group, you can also read a teammate's code, such as how they made a figure, without running it and before it is reviewed or merged into `main`. *(00:32:36)*

## 8. Opening a pull request ([9.1 Creating a pull request](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/github-pull-requests.html#creating-a-pull-request))

*00:33:40–00:41:16*

- **Q:** Why does the instructor open a pull request right away, even after one small commit?
  **A:** The "Compare & pull request" pop-up seems to disappear after a day or so. Starting the pull request immediately means he doesn't risk losing it, and the pull request can still be marked as in progress. If the pop-up is gone, you can reach the same page from the Branches tab through "New pull request". *(00:35:15)*

- **Q:** Why should you check the line at the top of a new pull request that names the two branches?
  **A:** It says which branch is being merged into which. In this course that is your branch into `main`, but in DSCI 524 the target won't always be `main`. With forks of open-source projects, you must also make sure your code goes to the right place. *(00:36:20)*

- **Q:** Explain why the file list at the bottom of a pull request is a "second line of defence".
  **A:** After reviewing on your own computer, you can review on GitHub every change from `main`. First, check that all the files you worked on are there; if not, you probably forgot to add, commit or push. Second, check that files that don't belong, such as `.ipynb_checkpoints`, `.DS_Store` or Word backup files, aren't there, because points are taken off for them even if the instructions don't mention them. *(00:39:42)*

- **Q:** How does a pull request's title differ from its description, and when might the two be the same?
  **A:** The pull request is a report: the title names the change, and the description explains what is happening in the branch. For simple changes, like most group-project work, the two may be almost the same. Pull requests written by AI agents can "read like a novel." *(00:37:42)*

- **Q:** Why edit a pull request's first comment instead of adding "now I'm also doing…" comments as the work grows?
  **A:** The very first message is what people are going to read. All your changes should be defined and explained there, which is why GitHub lets you edit it. *(00:41:03)*

- **Q:** What changes once you click "Create Pull Request"?
  **A:** The pull request appears under the Pull requests tab. Anyone with access to the repository can see the branch and its changes, review them, and discuss them in the conversation. *(00:40:01)*

## 9. Code review and updating a pull request ([10 Code review on GitHub](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/github-code-review.html))

*00:41:16–00:45:41*

- **Q:** What does "code review" mean in terms of the Files changed tab?
  **A:** You look at the diff between the original code and the code being added or removed. You can comment on a line using the `+` that appears when you hover over it, as in "why are you using switch and not checkout?" Those comments are tracked in the main Conversation tab. *(00:41:34)*

- **Q:** Explain the rule of thumb for who fixes problems found in a code review.
  **A:** If it's your pull request, fixing it is your job. The reviewer's job is to say "rewrite this" or "this doesn't look right," not to fix your code. *(00:42:17)*

- **Q:** How do you change the code in an open pull request without closing it and opening a new one?
  **A:** Go back to the branch the pull request is working from, then add, commit and push to that same branch. The pull request is tied to the branch, so it updates. In class, committing "show you the long git log command" and running `git push origin dan-b1` made a second commit appear in pull request #1, sometimes only after a page refresh. *(00:44:43)*

- **Q:** Why might a reviewer's comment collapse as "outdated" after you push a new commit?
  **A:** If you changed the line the comment was attached to, that comment probably isn't relevant anymore. GitHub collapses it so you don't end up looking at too much stuff. The comment isn't necessarily deleted. *(00:45:02)*

## 10. AI reviewers and draft pull requests ([9.2 Draft pull requests](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/github-pull-requests.html#draft-pull-requests))

*00:52:11–00:55:41*

- **Q:** How should you treat comments from a Copilot review on your pull request?
  **A:** Requesting one isn't a bad thing, because more eyes on something is never really a bad idea. But you don't have to keep every comment the LLM makes: you can push back on it, reject it or accept it. *(00:53:05)*

- **Q:** What does "Convert to draft" communicate, and what does the grey bar mean?
  **A:** It turns an open pull request into a draft. The grey bar instead of a green one is the visual cue that people can look, but the work isn't ready yet. You use it to tell yourself and others that this isn't ready. *(00:54:12)*

- **Q:** Why does greying out the merge button on a draft pull request matter?
  **A:** Nobody can accidentally merge something that explicitly says it isn't working or isn't ready. The instructor believes this also stops an agent from just merging everything that's green. This is why he has kept drafts open for three or four months on long pieces of work. *(00:55:03)*

- **Q:** How do you turn a draft pull request back into one that can be merged?
  **A:** At the bottom, where it says the pull request is a work in progress, click "Ready for review." It becomes an open pull request again, with green merge buttons. *(00:55:28)*

## 11. Merging and deleting the branch on GitHub ([8.2 Useful things you can do with branches on GitHub](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#useful-things-you-can-do-with-branches-on-github))

*00:55:41–00:59:07*

- **Q:** Why does the instructor delete a branch on GitHub after its pull request is merged?
  **A:** A project creates many branches and pull requests over its lifetime. Without cleanup, the branch dropdown becomes a giant list, which he finds annoying. You don't need to keep the branch name, because the commits are still there. *(00:56:08)*

- **Q:** Why is no work lost when you delete `dan-b1` after merging pull request #1?
  **A:** Deleting the branch removes only the marker. `main`'s history still contains the branch's two commits plus a separate merge commit. You can find the commits related to the pull request and undo the feature later if you need to. *(00:58:38)*

- **Q:** Why might a team *not* delete merged branches?
  **A:** Where law or compliance requires it, you can't delete anything, and the branch list just gets long. Otherwise, your team's workflow decides, but at least clean up your own work if it doesn't affect other people. *(00:57:34)*

## 12. Syncing and cleaning up locally after a merge ([8.1.3 Useful command line Git branching commands](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#useful-command-line-git-branching-commands))

*00:59:07–01:03:51*

- **Q:** Why do merge conflicts still happen when each person works on their own branch?
  **A:** Even if you tell people which part you're working on, other people or agents sometimes can't help fixing a typo in your part. If you fix the same typo, there is still a conflict. This is why individual assignment 1 has you practise merge conflicts again. *(00:59:39)*

- **Q:** Why do you need `git pull origin main` after a pull request is merged on GitHub?
  **A:** Local `main` doesn't update itself. Pulling syncs it with GitHub. In class, the pull added new lines to `README.md`, which were the merged pull request's changes. *(01:00:17)*

- **Q:** How does `git fetch` differ from `git pull`?
  **A:** `git pull` does two things: it fetches, and then it merges on top. `git fetch` only coordinates the history with `origin`, so you run it alone when you don't want the files on your computer to change. *(01:01:52)*

- **Q:** Interpret what `git fetch --prune` did in class when it printed `[deleted] (none) -> origin/dan-b1`.
  **A:** The `dan-b1` branch had been deleted on GitHub. The prune removed the matching `origin/dan-b1` marker on the local computer. After that, the reference no longer appeared in the big `git log` command. *(01:02:22)*

- **Q:** Why should you use lowercase `git branch -d` rather than capital `-D`, and why is the capital version dangerous?
  **A:** Lowercase `-d` deletes a local branch only if it has been merged. Git makes it harder to delete work, because deleting an unmerged branch in theory loses that work. Capital `-D` force-deletes even unmerged branches, and it's only a one-character difference. Be very careful when copying commands from ChatGPT, which might give you `-D` and delete commits you're still working on. *(01:03:21)*

## 13. Setting up two conflicting pull requests ([8.3 What happens when my feature branch falls behind main?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#what-happens-when-my-feature-branch-falls-behind-main))

*01:04:00–01:10:00*

- **Q:** What makes the `dan-fetch` and `dan-delete` branches conflict?
  **A:** A merge conflict happens when two changes are made to the same line of the same file. Both branches added text at the same place in `README.md`. *(01:04:00)*

- **Q:** Why must you avoid merging the first pull request, `dan-fetch`, straight away when you practise conflicts on your own?
  **A:** Holding it open lets you create a second, conflicting set of changes from the same starting point. This stands in for what happens when two people each open a pull request and one of them conflicts with the other. *(01:06:07)*

- **Q:** Why wasn't the `git fetch --prune` line in `README.md` when the instructor started `dan-delete`?
  **A:** He switched to `main` before creating `dan-delete`, and that line had only been committed on `dan-fetch`. Both branches are therefore based on `main` without each other's changes. *(01:07:20)*

- **Q:** Interpret the `git log --oneline --graph --all --decorate` output in which two lines leave commit `3851b00`.
  **A:** Both branches start from the same `main` commit and then split. The graph literally shows two parallel pieces of work: `dan-fetch` with `157c3cd` and `dan-delete` with `cb810d5`. *(01:09:00)*

- **Q:** Why doesn't GitHub warn you about the coming conflict while both pull requests are still open?
  **A:** Each pull request is compared only with `main`, and on its own each one can be merged into `main`. Nothing in either pull request shows that they edit the same line, and it isn't obvious that they share the same starting point. *(01:09:53)*

## 14. When a merge creates the conflict: resolving on GitHub

*01:10:00–01:12:44*

- **Q:** How did pull request #3 go from mergeable to conflicting?
  **A:** When one pull request is merged, `main` changes. Every pull request that merges into `main` is then rechecked. After #2 was merged, #3 could no longer merge cleanly, and GitHub showed the conflict page. *(01:10:31)*

- **Q:** Compare what "fixing" a conflict means for report prose and for code in this course.
  **A:** For report writing, whatever is left must be English that makes sense. For code, it isn't enough to remove the `<<<<<<<`, `=======` and `>>>>>>>` markers: the code must work from top to bottom again. *(01:11:21)*

- **Q:** Why can resolving a conflict on line 13 still leave the code broken?
  **A:** The conflict only tells you which line has competing changes. Your resolution can affect code elsewhere, for example if you change a variable name that is used on line 50. Making that code work again is still your problem. *(01:11:39)*

- **Q:** When did the instructor suggest the GitHub web editor, and when fixing the conflict locally?
  **A:** The web editor is fine for simple conflicts like the one in `README.md`. He showed the local fix because the commands are more involved. *(01:12:33)*

## 15. Resolving the conflict locally with rebase ([8.3.2 Using rebase](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#using-rebase))

*01:12:44–01:20:42*

- **Q:** What does `git rebase main` do to the `dan-delete` branch?
  **A:** It replays your branch's commits on top of the existing changes on `main`. That replay is where the conflict surfaces on your computer, so you can fix it there. The instructor noted that there are many ways to fix conflicts and that people will have opinions; rebase is the one he uses. *(01:14:31)*

- **Q:** Why must you run `git switch main` and `git pull origin main` before rebasing `dan-delete`?
  **A:** The merged `dan-fetch` commit was on GitHub's `main` but not on your computer. Syncing `main` brings that commit down, so there is something to replay your branch on top of. *(01:13:42)*

- **Q:** Explain what had to change about `dan-delete`'s history, in terms of the commit IDs from class.
  **A:** `dan-delete`'s previous commit was `3851b00`. It needed to be one that contains `157c3cd`, the fetch commit merged into `main`. Rebasing gives the branch that new parent. *(01:16:00)*

- **Q:** How does triggering a conflict with `git rebase main` differ from week 3 of 521?
  **A:** Fixing the conflict is the same skill: open the file and resolve the markers. In 521 the conflict was triggered by `git pull origin main`. Here it is triggered by replaying your commits over another branch. *(01:17:56)*

- **Q:** How does `git status` guide you through a rebase that stopped on a conflict?
  **A:** It tells you to use `git add` to mark the file as resolved. Once all conflicts are fixed, it tells you to run `git rebase --continue`, which asks you to confirm the commit message. If you're scared that something got messed up, you can abort to get back to where you started. *(01:18:44)*

- **Q:** Why did the instructor have to force-push, with `git push --force-with-lease origin dan-delete`, after the rebase, and why should this be done with care?
  **A:** The rebase changed the branch's history: the commit's previous commit is no longer the old version of `main`. A simple push is no longer possible, so you can't avoid force-pushing. GitHub records that a force push happened, and since you've "mangled history," that matters in compliance settings. *(01:20:21)*

---

- prompt: prompt-recall-2-understand.md @ 8bcc190
- prompt-hash: d3d1585a5f4d
- model: claude-opus-5-5 (requested: opus)
- backend: claude
- inputs: transcript-plaud.md, terminal.txt, materials.md, notes-class-main--claude-opus-5-5.md
- generated: 2026-11-20
- notes-input: notes-class-main--claude-opus-5-5.md @ d979d4ea6828, links and section references removed
