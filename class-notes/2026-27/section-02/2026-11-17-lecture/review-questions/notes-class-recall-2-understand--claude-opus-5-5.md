# Git branches, pull requests and rebasing: review questions, tier 2 — Understand

Date: 2026-11-17

Instructor: Daniel Chen

*Tier 2 of 5: Understand. Explain each answer in your own words before you read it; tier 1 (Remember) covers the facts, tiers 3 to 5 put them to use.*

## 1. Course logistics: lab groups, attendance and interview week

*00:00:01–00:04:04*

- **Q:** Explain why the instructor insisted that everyone submit their GitHub username correctly.
    - **A:** The usernames build a main list of everyone's GitHub accounts. That list is the source of the username column in the lab sections repository, and it is "a piece of metadata that is used everywhere else under the hood" in the rest of the program. That is why getting it right is super important. *(00:01:50)*

- **Q:** Why is lab attendance mandatory in DSCI 522?
    - **A:** The course is built around a group project. During lab the TAs go around and talk to every single group, and you should be there when a TA comes to your group. *(00:02:19)*

- **Q:** Why can anything in your group's code base come up in your interview-week conversation?
    - **A:** You are expected to know the code base you work in, as you would at work. This matters "especially in the world of AI": if something is in your code base, it is fair game to be talked about. *(00:03:15)*

- **Q:** How should you approach the seven-minute interview, given how it is graded?
    - **A:** Treat it like a technical interview about your Git work and your project. It's okay not to know things, because the course is trying the format out. You will get a grade, but it won't affect your mark. *(00:02:55)*

## 2. Why branches: escaping the 521 push/pull friction ([8 Git branches](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html))

*00:06:49–00:09:43*

- **Q:** Explain the friction from the 521 shared slide-deck exercise that branches are meant to remove.
    - **A:** Even when there was no conflict, you often couldn't push your finished part, because someone else had already pushed. There was always the annoying step in the middle of pulling first before you could push again. *(00:07:06)*

- **Q:** Why will some of that push/pull friction exist in every project, even when the team uses branches?
    - **A:** Not every project can start with four parallel pieces of work. Early on, the group has to get the basics down first, and everyone is bound or stuck by one or two people. *(00:07:40)*

- **Q:** Why do you want to reach the phase of a project where each part is one person's responsibility?
    - **A:** If two people work on the same thing at the same time, they keep running into the friction of "I want to add something, but I can't", conflict or not. Separate responsibilities let the team work in parallel streams instead. *(00:08:19)*

- **Q:** How do parallel streams on branches change how a week of group work can run?
    - **A:** Each person is "in your own little world" on their own branch and can push and pull until they're done, without caring what others are doing. For example, you could work on your part from Tuesday to Friday, and then on Friday the group reviews and coordinates everyone's work. *(00:08:46)*

## 3. Review: the local–remote picture

*00:09:46–00:11:47*

- **Q:** Why is the GitHub remote "the thing that matters" rather than your local repository?
    - **A:** The remote is what gets graded and what gets published. Work that exists only on your local computer effectively doesn't exist for grading or project purposes. At work, it would be like a product that isn't shipped, because the code isn't anywhere it could be shipped from. *(00:10:53)*

- **Q:** Compare `clone` with `push` and `pull` in the local–remote diagram.
    - **A:** `clone` is a one-time command that brings the repository down to your computer. `push` sends the commits you made locally up to GitHub. `pull` brings down commits that others, such as teammates, have pushed. *(00:11:25)*

- **Q:** Why does working with teammates add so much coordination work?
    - **A:** You don't only have to coordinate your computer with the GitHub remote. Each of your teammates also has to coordinate their own computer with that same remote. *(00:10:35)*

## 4. What a branch is: `main`, `HEAD` and `origin/main` ([8 Git branches](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html))

*00:12:03–00:17:54*

- **Q:** Explain how `HEAD` and `main` relate when you make a commit on the main branch.
    - **A:** When you're on the main branch, `HEAD` is attached to `main`. Every time you run `git add` and `git commit`, `main` increments to the new commit. *(00:13:17)*

- **Q:** What does `origin/main` in the Git log represent, and why can your local `main` be ahead of it?
    - **A:** `origin/main` is what your computer *thinks* the state of GitHub is. If you write commits on `main` without pushing, your local `main` moves forward while `origin/main` stays put, so the local branch is further ahead. *(00:13:30)*

- **Q:** How does committing on a branch differ from committing on `main`?
    - **A:** The process is the same: `git add`, `git commit`, and so on. The only difference is which name moves. Instead of incrementing `main`, each commit moves a branch name you chose yourself, such as `b1`. *(00:14:06)*

- **Q:** Why should you treat `main` as the production version of the project?
    - **A:** `main` is the stable part, where at least the code works even if the project isn't finished. You don't want one person's experiment to break things so that the project "no longer works on all of my teammates' computers". *(00:15:10)*

- **Q:** Give the class's example of what belongs on `main` and what stays on a branch.
    - **A:** The cleaned dataset goes on `main`, and everyone bases their work on that clean part. Exploratory data analysis, with all its plots, isn't ready yet while you're still exploring the data, so it stays on your own branch. *(00:15:24)*

- **Q:** Why use branches even when you are the only person working in a repository?
    - **A:** Branches section off work, so you can test and build things without `main` changing until you've reviewed everything. The instructor made textbook edits in a sequence of branches while another instructor was teaching from it, so pages wouldn't move around mid-lecture. He merged them after reviewing and testing. *(00:16:37)*

- **Q:** Why is it easier to throw away a failed idea on a branch than to undo it from a commit history?
    - **A:** If the idea didn't work, you just come back to `main`, or delete the branch, and you're back at your starting point. Undoing part of a commit that did twenty different things means going through the history and copying out the relevant bits. `git reset` and `git revert` from 521 could do the same job, but branches make it easier. *(00:16:51)*

## 5. Creating and switching branches ([8.1 Creating a branch using the command line](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#creating-a-branch-using-the-command-line))

*00:17:54–00:26:29*

- **Q:** Why run `git pull origin main` before creating a branch for coordinated work?
    - **A:** Pulling makes sure your starting point includes everything everyone has already pushed. The instructor has created branches on one computer and then realised he had already done half the work on another laptop. Syncing first would have saved him that time. *(00:18:09)*

- **Q:** Explain what `git switch` does to the repository, and how the log shows which branch you're on.
    - **A:** `git switch` moves `HEAD` around the repository. You can tell you're on `main` because `HEAD` points to `main` in the log, and `git switch -c <name>` creates a new branch and moves `HEAD` to it. *(00:19:46)*

- **Q:** Why does the instructor start his branch names with his own name in shared repositories?
    - **A:** It tells other people who to talk to: if something weird is going on in that branch, they know which person is responsible for it. *(00:20:31)*

- **Q:** Interpret the log line `145ff16 (HEAD -> dan-b1, origin/main, origin/HEAD, main) intro and review`, shown right after `git switch -c dan-b1`.
    - **A:** No new commit was made. All that happened is that a new branch, `dan-b1`, was created on the same commit as `main` and the remote references, and `HEAD` moved to it. "Nothing really different other than a word has changed." *(00:21:13)*

- **Q:** After committing "define swtich -c" on `dan-b1`, the log shows `dan-b1` one commit ahead of `main` and `origin/main`. Explain why.
    - **A:** Whatever branch `HEAD` is on gets dragged along when you commit, so this time `dan-b1` moved instead of `main`. `origin/main` stays behind because nothing has been pushed or synced with GitHub. *(00:22:58)*

- **Q:** Why is it worth knowing these commands and how to draw them, even if you use VS Code or Positron?
    - **A:** The graph view in the Git tab of VS Code and Positron shows the same thing as the terminal log: `origin/main`, the local `main`, and the commit on `dan-b1`. Knowing the commands and the diagram lets you read what that view is showing. *(00:23:51)*

- **Q:** What happens to `README.md` on disk after `git switch main`, and why is that useful?
    - **A:** The file goes back to its state at the commit where `main` is, and the branch you left doesn't move. Because you can move between parallel states of the project, you can try a new feature on a branch, or look at a teammate's work, without disturbing `main`. *(00:25:46)*

- **Q:** Why does the instructor type `git log --oneline --graph --decorate --all` rather than leave off `--all`?
    - **A:** Without the `--all` flag, the log may not show your other branch names. That's why he always types it out in full. *(00:25:38)*

## 6. `git checkout` and `git branch` versus `git switch` ([8.1.3 Useful command line Git branching commands](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#useful-command-line-git-branching-commands))

*00:26:40–00:28:26*

- **Q:** Explain why `git switch` exists when `git checkout` already moved `HEAD` around.
    - **A:** `checkout` did what `switch` does, moving `HEAD`, but it also did much of what `restore` and `revert` do. The newer commands were carved out of `checkout` around 2019–2020. `checkout` still has all those behaviours, which is why it is fine to use but harder to predict. *(00:27:09)*

- **Q:** Why should you ask an AI assistant for the `switch` version when it tells you to run `checkout`?
    - **A:** `checkout` can do many things. If you don't know what a particular `checkout` command will do and you're worried about losing work, think about the commands you're typing. Asking for the `switch` version gives you a command whose effect you understand. *(00:27:34)*

- **Q:** Compare `git branch <name>` with `git switch -c <name>` and `git checkout -b <name>`.
    - **A:** `git switch -c` and the older `git checkout -b` both create the branch and move you onto it. `git branch` only creates the branch and doesn't move you, so you still have to `checkout` or `switch` afterwards. *(00:28:13)*

## 7. Pushing a branch and viewing it on GitHub ([8.2 Useful things you can do with branches on GitHub](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#useful-things-you-can-do-with-branches-on-github))

*00:28:31–00:33:40*

- **Q:** Why did the instructor get `dan-b1` into `main` through GitHub rather than merging on his own computer?
    - **A:** He called going through a review process the easiest way. Instead of merging locally, you push the branch and merge it through a pull request, also called a merge request. *(00:28:58)*

- **Q:** Running a bare `git push` while on `main` printed `Everything up-to-date` and did not send the new commit. Explain why.
    - **A:** The new commit was on `dan-b1`, not `main`, so there was nothing new on `main` to push. Once you work with branches, *where* you push and *what* you push start to matter, so you first need to be on the branch you want to push. *(00:29:34)*

- **Q:** Explain what each of the last two words does in `git push origin dan-b1`.
    - **A:** `origin` says where you are pushing: the GitHub remote. `dan-b1` says what you are pushing: the branch, in place of the `main` you've typed for ten weeks. Otherwise the behaviour is exactly the same: your local work goes up to GitHub. *(00:30:36)*

- **Q:** Interpret the log after `git push origin dan-b1`: `origin/dan-b1` sits beside `dan-b1`, while `origin/main` is still one commit back.
    - **A:** GitHub now has a branch called `dan-b1` at the same commit as your local `dan-b1`. Pushing a branch doesn't change `main`, either locally or on GitHub. *(00:31:19)*

- **Q:** Why did the pushed work not appear on the repository's GitHub front page, and how can you see it?
    - **A:** The front page shows `main`, and the work was only on `dan-b1`. The dropdown in the top-left corner, labelled `main`, lets you view other branches, such as `dan-b1` and its changes. *(00:32:21)*

- **Q:** Why is it useful to view a teammate's branch on GitHub before it is merged?
    - **A:** You can look at their code, for example to see how they made a figure, without running it, while it is still not combined into `main`. It is also how you check that your own local work actually reached GitHub. *(00:32:36)*

## 8. Opening a pull request ([9.1 Creating a pull request](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/github-pull-requests.html#creating-a-pull-request))

*00:33:40–00:41:16*

- **Q:** Why does the instructor open a pull request right away, even after one small commit?
    - **A:** The "Compare and Pull Request" pop-up seems to disappear after a day or so. Starting the pull request immediately means he doesn't risk losing it, and the pull request can stay "in process" while he works. If the pop-up does vanish, you can reach the same page from the Branches tab with "New pull request". *(00:34:32)*

- **Q:** Why check the line at the top of a new pull request that names the two branches?
    - **A:** It says which branch you are merging and which branch it goes into, and you want to make sure your code is sent to the right place. In this course the target is probably `main`, but in DSCI 524 it won't always be. With forks of open-source projects, this matters too. *(00:36:20)*

- **Q:** Explain how a pull request lets you review your own work, including work an AI produced.
    - **A:** Your first line of review is on your own computer. The pull request page is a second one: it lists every changed file and its diff relative to `main`, so you can check your work, or an AI's work, before anyone merges it. *(00:38:15)*

- **Q:** If a file you worked on is missing from the pull request's changes, what does that most likely mean?
    - **A:** You probably typed something wrong or forgot to add, commit and push it. The pull request shows only what reached the branch on GitHub. *(00:39:37)*

- **Q:** Why must you check the pull request's file list for files that don't belong there?
    - **A:** Files such as `.ipynb_checkpoints`, macOS `.DS_Store` or hidden Word backup files shouldn't be in the repository. If they're in the repository, points are taken off even if the instructions don't explicitly say so. This check is your second line of defence, and your `.gitignore` file still matters. *(00:38:44)*

- **Q:** Why edit the pull request's first comment instead of adding "now I'm also doing…" comments?
    - **A:** The very first message is what people read. As the pull request changes, all your changes should be defined and explained in that first comment, which is why GitHub lets you edit it. *(00:40:48)*

## 9. Code review and updating a pull request ([10 Code review on GitHub](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/github-code-review.html))

*00:41:16–00:45:41*

- **Q:** Explain what "code review" means on GitHub's Files changed tab.
    - **A:** You look at the diff between the original code and the code someone is adding or removing. Hovering over a line shows a `+` button, which lets you comment on that line, for example "why are you using switch and not checkout?" Those comments are also tracked in the main conversation tab. *(00:41:34)*

- **Q:** Compare the jobs of a pull request's author and its reviewer.
    - **A:** The reviewer's job is to point out problems: "rewrite this" or "this doesn't look right". It is the author's job to actually fix their pull request. *(00:42:17)*

- **Q:** How do you update an open pull request such as #1 after a reviewer asks for a change?
    - **A:** You don't close it and open a new one. Go back to the branch the pull request was made from (here `dan-b1`), then add, commit and push to that same branch. The pull request is tied to the branch, so it updates, although sometimes you have to refresh the page. *(00:43:15)*

- **Q:** Why might GitHub collapse a reviewer's comment and mark it outdated?
    - **A:** You changed the line the comment was made on, so that original comment probably isn't relevant anymore. GitHub collapses it so you don't end up looking at too much stuff. *(00:45:02)*

## 10. AI reviewers and draft pull requests ([9.2 Draft pull requests](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/github-pull-requests.html#draft-pull-requests))

*00:52:11–00:55:41*

- **Q:** How should you treat comments from a Copilot review on your pull request?
    - **A:** Requesting one isn't a bad thing, because having more eyes on something is never really a bad idea. You don't have to keep every comment the LLM makes: you can push back on a comment, reject it or accept it. *(00:52:30)*

- **Q:** Why does the instructor convert a pull request he opened early to a draft?
    - **A:** He opens the pull request first and keeps pushing to it, so it needs to say "this isn't ready yet". A draft shows a grey bar instead of a green one, which signals to him and the team that they can look but the work isn't ready. He has kept drafts open for three or four months on long work. *(00:54:12)*

- **Q:** How does a draft pull request prevent accidental merges?
    - **A:** The merge button is greyed out, so no one can accidentally merge work that is explicitly marked as not ready. The instructor believes this also stops an agent from merging everything that's green. *(00:54:30)*

- **Q:** How do you turn a draft back into a pull request that can be merged?
    - **A:** At the bottom of the pull request, where it says the pull request is a work in progress, click "Ready for review". It becomes an open pull request again, with green merge buttons. *(00:55:28)*

## 11. Merging and deleting the branch on GitHub ([8.2 Useful things you can do with branches on GitHub](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#useful-things-you-can-do-with-branches-on-github))

*00:55:41–00:59:07*

- **Q:** Why does the instructor delete a branch on GitHub after its pull request is merged?
    - **A:** A project has many features, branches and pull requests over its lifetime. Without cleanup, the branch dropdown grows into a giant list, and the merged branch name no longer needs tracking. *(00:56:08)*

- **Q:** Explain why deleting `dan-b1` after merging #1 did not lose any work.
    - **A:** Deleting the branch only removes the branch marker. `main`'s history still has the branch's two commits, plus a separate commit saying the pull request was merged. You can still find the commits for a pull request and undo a feature, so "nothing's really lost". *(00:58:10)*

- **Q:** When should you not delete merged branches?
    - **A:** If a law or compliance rule says you can't delete things, don't. Otherwise your team's workflow decides, but at least clean up your own work. *(00:57:00)*

## 12. Syncing and cleaning up locally after a merge ([8.1.3 Useful command line Git branching commands](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#useful-command-line-git-branching-commands))

*00:59:07–01:03:51*

- **Q:** Why do merge conflicts still happen when every teammate works on their own branch?
    - **A:** Even when people agree who works on which part, other people or agents sometimes can't help fixing a typo in your part. If you fix the same typo, there's still a merge conflict. That's why individual assignment 1 has you practise merge conflicts again. *(00:59:39)*

- **Q:** Why did local `main` need `git pull origin main` after #1 was merged on GitHub?
    - **A:** Local `main` doesn't update itself when something is merged on GitHub; you need a synchronization step. The pull fast-forwarded `main` and added the new lines from the merged pull request to `README.md`. *(01:00:17)*

- **Q:** Interpret the output of `git branch -a`.
    - **A:** It lists all the branches your computer knows about. The branches you created locally appear by name, with a star next to the one you're on, and the remote ones appear as entries such as `remotes/origin/dan-b1`. *(01:01:06)*

- **Q:** Compare `git fetch` with `git pull`.
    - **A:** `git pull` does two things: it runs a fetch and then a merge on top. `git fetch` only synchronizes the history with `origin`. You run fetch alone when you don't want the files on your computer to change. *(01:01:52)*

- **Q:** Explain what `--prune` added, and why `origin/dan-b1` disappeared from the log after `git fetch --prune`.
    - **A:** When a branch has been deleted on the remote, the fetch also removes that branch's marker on your computer. The output showed `[deleted] (none) -> origin/dan-b1`, and the log no longer showed that reference. *(01:02:22)*

- **Q:** Why use lowercase `git branch -d` rather than capital `-D` to delete a local branch?
    - **A:** Lowercase `-d` only deletes a branch that has been merged: deleting an unmerged branch could lose work, so Git makes it harder. Capital `-D` force-deletes even unmerged work. It's a one-character difference, so be very careful when copying commands from ChatGPT: it might hand you `-D`, and you could delete the commits you're working on. *(01:03:21)*

## 13. Setting up two conflicting pull requests ([8.3 What happens when my feature branch falls behind main?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#what-happens-when-my-feature-branch-falls-behind-main))

*01:04:00–01:10:00*

- **Q:** Explain what kind of change produces a merge conflict between two branches.
    - **A:** Two different changes to the same line of the same file. The instructor set up `dan-fetch` and `dan-delete` to edit the same spot in `README.md`. *(01:04:00)*

- **Q:** Why did the instructor not merge the `dan-fetch` pull request (#2) right away?
    - **A:** Leaving #2 unmerged is the key to practising conflicts on your own. It stands in for two people opening pull requests where one has conflicting changes. Merging it first would have been just another review, not a conflict. *(01:06:07)*

- **Q:** Why was the fetch line missing from `README.md` on `dan-delete`?
    - **A:** He switched back to `main` before creating `dan-delete`, and the fetch line existed only on `dan-fetch`. Both branches were based on `main`. *(01:07:20)*

- **Q:** Interpret the log graph where `cb810d5` (`dan-delete`) and `157c3cd` (`dan-fetch`) both come out of `3851b00`.
    - **A:** There is literally a split: from the same `main` commit, two lines come out, one per branch. That means two parallel pieces of work are happening. *(01:08:53)*

- **Q:** Why didn't GitHub warn that #2 and #3 would conflict?
    - **A:** Each pull request is judged on its own against `main`, and it isn't obvious they share a starting point. Each one looked fine to merge into `main`, even though both changed line 13. *(01:09:48)*

## 14. When a merge creates the conflict: resolving on GitHub ([8.3 What happens when my feature branch falls behind main?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#what-happens-when-my-feature-branch-falls-behind-main))

*01:10:00–01:12:44*

- **Q:** Explain how #3 went from mergeable to conflicting once #2 was merged.
    - **A:** Merging one pull request changes `main`. Every other pull request that merges into `main` is then rechecked. #3 could no longer be merged cleanly, so it landed on the "you have a conflict" page. *(01:10:08)*

- **Q:** Compare what "fixing" a conflict means for report text and for code.
    - **A:** For report writing, whatever is left must be English that makes sense. For code, removing the conflict markers isn't enough: the code has to work from top to bottom again. *(01:11:21)*

- **Q:** Why might code still be broken after the conflict markers on line 13 are cleaned up?
    - **A:** Git only tells you that line 13 has conflicting changes; your fix can affect code elsewhere. If resolving it renames a variable used on line 50, that is still your problem. Resolving a conflict means the code runs as you expect, not just that the markers are gone. *(01:11:39)*

- **Q:** When does the instructor resolve a conflict in GitHub's web editor, and when on his own computer?
    - **A:** For simple conflicts like this one, the web editor is fine. Resolving on your own computer is a little more involved because it takes more commands, and he showed it for that reason. *(01:12:19)*

## 15. Resolving the conflict locally with rebase ([8.3.2 Using rebase](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#using-rebase))

*01:12:44–01:20:42*

- **Q:** Explain what `git rebase main` does to the `dan-delete` branch.
    - **A:** It replays the branch's commits on top of the updated `main`, so that `dan-delete`'s parent is no longer `3851b00` but the merge that contains `157c3cd`. The replay is where the conflict comes up on your own computer, so you can fix it there. *(01:14:31)*

- **Q:** Why do you sync `main` before running `git rebase main` on your branch?
    - **A:** The conflicting commit was already merged into `main` on GitHub, and your local `main` doesn't have it yet. Step one is to get that commit onto your computer with `git switch main` and `git pull origin main`, so you have something to rebase onto. *(01:13:42)*

- **Q:** Compare how a conflict was triggered in week 3 of 521 with how it is triggered with branches.
    - **A:** Fixing the markers is the same skill as in 521. In 521, `git pull origin main` triggered the conflict. Here the trigger is replaying your branch's commits over another branch with `git rebase main`. *(01:17:56)*

- **Q:** How does `git status` guide you through a rebase that has stopped on a conflict?
    - **A:** After you fix the markers, it tells you to use `git add` to mark the resolution. It then tells you to run `git rebase --continue`, which asks for the commit message. If you're scared that something got messed up, you can abort the rebase. *(01:18:20)*

- **Q:** Interpret the log after `git rebase --continue`, where `0e16503 (HEAD -> dan-delete)` sits on top of `3167d10`, but `origin/dan-delete` still points to `cb810d5`.
    - **A:** The branch is now at the top of the history, after `main`, with the conflict fixed. Its commit has a new hash because it has a new parent. GitHub's copy of the branch is still the old commit on the old base, so local and remote now disagree. *(01:19:14)*

- **Q:** Why could the rebased `dan-delete` branch not be pushed normally?
    - **A:** The rebase changed the branch's history: the commit's parent is now a different commit. A simple push no longer works, so you have to force push to update the branch, here with `git push --force-with-lease origin dan-delete`. You can't get around force pushing after a rebase. *(01:19:47)*

- **Q:** Why is a force push after a rebase something to take seriously?
    - **A:** You've "mangled history", which can be a compliance concern, and GitHub records that a force push happened. Once it's done, the pull request shows the green merge button again. *(01:20:21)*

---

- prompt: prompt-recall-2-understand.md @ 65eb21c
- prompt-hash: 17df43f38e78
- model: claude-opus-5-5 (requested: opus)
- backend: claude
- inputs: transcript-plaud.md, terminal.txt, materials.md, notes-class-main--claude-opus-5-5.md
- generated: 2026-11-23
- notes-input: notes-class-main--claude-opus-5-5.md @ d979d4ea6828, links and section references removed
