# Git branches, pull requests and rebasing to fix conflicts: review questions, tier 5 — Evaluate

Date: 2026-11-17

Instructor: Daniel Chen

*Tier 5 of 5: Evaluate. Decide and justify your verdict before you read the answer; the criteria are the ones given in class.*

## 1. Course logistics: lab groups, attendance and interview week

*00:00:01–00:04:04*

- **Q:** A group member lets an AI agent write their part of the group project and plans to skip reading it, because the seven-minute interview-week conversation does not affect their grade. Judge whether that plan is sound.
    - **A:** It is not sound. The interview covers your group's actual code base, and anything in it is fair game, "especially in the world of AI." The instructor's standard is that you should know the code base you are working in, as you would at work, whatever the grading. *(00:03:15)*

## 2. Why branches: escaping the 521 push/pull friction

*00:06:49–00:09:43*

- **Q:** Once each group member owns a self-contained part of the project, the group proposes that everyone keep committing and pushing directly to `main`, as in the DSCI 521 shared slide-deck exercise. Assess this plan.
    - **A:** It is a poor plan for that phase of the project. When several people push to the same branch, you keep hitting the friction of having to pull before you can push, whether or not there is a conflict. The class's goal was parallel streams on branches, where each person can push and pull freely until their work is ready for review. *(00:08:41)*

## 3. Review: the local–remote picture

*00:09:46–00:11:47*

- **Q:** Before a milestone deadline, a teammate says their analysis is "done" because it is committed on their laptop, and they will push it next week. Judge whether their part of the milestone is complete.
    - **A:** It is not complete. The GitHub remote is the thing that matters: it is what gets graded and published. Work that exists only on your local computer "effectively doesn't really exist" for grading or project purposes, like a product that was never shipped. *(00:10:53)*

## 4. What a branch is: `main`, `HEAD` and `origin/main` ([8 Git branches](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html))

*00:12:03–00:17:54*

- **Q:** A teammate is still exploring the dataset and wants to commit their half-finished EDA plots straight to `main` so everyone can see them. Critique this plan.
    - **A:** The work belongs on a branch, not on `main`. In class, `main` was described as the production version: the stable branch where at least the code works. Exploratory work that isn't ready stays on the author's branch, while `main` holds the shared, cleaned dataset that everyone builds on. *(00:15:24)*

- **Q:** A student working alone argues that branches are pointless without collaborators and commits every experiment directly to `main`. Argue for or against this approach.
    - **A:** Argue against it. The instructor uses branches even when he is the only contributor, because they section off work and keep `main` from changing until he has reviewed it. A failed idea on a branch is easy to discard by switching back to `main`. By contrast, undoing part of a commit that "did twenty different things" means digging through history. *(00:17:22)*

## 5. Creating and switching branches ([8.1 Creating a branch using the command line](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#creating-a-branch-using-the-command-line))

- **Q:** A group member who hasn't touched the project in a few days runs `git switch -c` straight away to start a new feature that builds on the team's shared work. Judge this sequence.
    - **A:** It skips a step. If your work builds on coordinated work, you should first sync your starting point with `git pull origin main`, so that you branch from everything the team has already pushed. Otherwise you risk redoing work. The instructor described wasting time this way after forgetting that half the work was already done on another laptop. *(00:18:39)*

*00:17:54–00:26:29*

## 6. `git checkout` and `git branch` versus `git switch` ([8.1.3 Useful command line Git branching commands](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#useful-command-line-git-branching-commands))

*00:26:40–00:28:26*

- **Q:** ChatGPT gives you a `git checkout` command that you don't fully understand, to run in your group project's repository. Decide whether to run it as given.
    - **A:** Don't run it blindly. `checkout` does far more than move `HEAD`: it also does much of what `restore` and `revert` do. If you don't know what a command does, the instructor's advice was to ask for the `switch` version instead, and to think carefully about what you type, especially when you're worried about losing work. *(00:27:44)*

## 7. Pushing a branch and viewing it on GitHub ([8.2 Useful things you can do with branches on GitHub](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#useful-things-you-can-do-with-branches-on-github))

*00:28:31–00:33:40*

- **Q:** A teammate finishes their work on branch `dan-b1` and plans to merge it into `main` on their own laptop, then push `main`. Recommend whether the group should accept this workflow.
    - **A:** Don't accept it. The class's recommended route is not to merge on your local computer, but to push the branch with `git push origin dan-b1` and merge it through a pull request. That way the work goes through a review process before it reaches `main`. *(00:28:58)*

## 8. Opening a pull request ([9.1 Creating a pull request](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/github-pull-requests.html#creating-a-pull-request))

*00:33:40–00:41:16*

- **Q:** On the "Compare & pull request" page, the file list shows your notebook, an `.ipynb_checkpoints` folder and a `.DS_Store` file. The assignment doesn't mention these files. Decide whether to click "Create pull request" as it is.
    - **A:** No. Files that don't belong in the repository, such as checkpoint folders, `.DS_Store` and hidden backup files, lose points even when the instructions don't mention them. Reviewing this file list is your second line of defence. Remove the files and fix your `.gitignore` before you create the pull request. *(00:39:16)*

- **Q:** As a pull request grows, its author adds a new comment each time ("now I'm also doing…") and leaves the original description unchanged. Assess this habit.
    - **A:** It is a poor habit. The very first message is what people read, so all of the changes should be defined and explained there. Edit the opening comment instead of piling on follow-ups. *(00:41:03)*

- **Q:** A student plans to wait until a branch is completely finished before opening its pull request. Judge this plan against the instructor's practice.
    - **A:** It is risky. The "Compare & pull request" pop-up disappears after about a day, so the instructor opens a pull request right away, even after a tiny commit, and keeps pushing to it. You can still recover the page from the Branches tab with "New pull request", but opening the pull request early avoids the problem entirely. *(00:35:15)*

## 9. Code review and updating a pull request ([10 Code review on GitHub](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/github-code-review.html))

*00:41:16–00:45:41*

- **Q:** While reviewing a teammate's pull request, you spot a bug, so you plan to rewrite their code yourself in the "Files changed" tab. Judge this as a reviewer's approach.
    - **A:** It goes against the rule of thumb from class. If it's your pull request, it is your job to fix it. The reviewer's job is to point out problems ("rewrite this", "this doesn't look right") in a comment, not to fix the author's code. *(00:42:17)*

- **Q:** After getting review comments on pull request #1, the author plans to close it and open a fresh pull request containing the fixes. Recommend whether to do this.
    - **A:** Don't do it. There's no need to close the pull request. Go back to the branch it was made from (`dan-b1`), then add, commit and push to that same branch, and the pull request updates itself, as the second commit did in class. *(00:43:15)*

## 10. AI reviewers and draft pull requests ([9.2 Draft pull requests](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/github-pull-requests.html#draft-pull-requests))

*00:52:11–00:55:41*

- **Q:** A group decides that every comment from a Copilot review must be applied before merging. Assess this rule.
    - **A:** The rule goes too far. Asking Copilot for a review is fine, since more eyes are never really a bad idea. But not every comment an LLM makes is one you have to keep. You can push back, reject it or accept it. *(00:53:01)*

- **Q:** You open a pull request early for work that will take several days, and keep pushing to it. A teammate who sees green buttons might merge it. Justify converting it to a draft.
    - **A:** Converting it is the right call. A draft shows a grey bar that signals "not ready yet", and it greys out the merge button, so nobody can merge it by accident. The instructor believes a draft also stops an agent from merging everything that's green. Click "Ready for review" when the work is done. *(00:54:30)*

## 11. Merging and deleting the branch on GitHub ([8.2 Useful things you can do with branches on GitHub](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#useful-things-you-can-do-with-branches-on-github))

*00:55:41–00:59:07*

- **Q:** After pull request #1 is merged, a teammate refuses to click "Delete branch" on `dan-b1`, worried that it will erase the branch's commits. Assess their concern.
    - **A:** The concern is unfounded. Deleting the branch marker doesn't delete the commits: `main`'s history still shows the branch's two commits plus the "Merge pull request #1" commit, so you can still find and undo the feature. Deleting merged branches keeps the branch list from growing into a giant list, so at least clean up your own. The exception is a workplace with compliance rules that forbid deleting. *(00:58:19)*

## 12. Syncing and cleaning up locally after a merge ([8.1.3 Useful command line Git branching commands](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#useful-command-line-git-branching-commands))

*00:59:07–01:03:51*

- **Q:** To clean up local branches, ChatGPT suggests `git branch -D` on every branch, including one with an experiment you never merged. Would you run it?
    - **A:** No: use lowercase `git branch -d`. It deletes a branch only if it has been merged, because Git deliberately makes it harder to lose work. Capital `-D` force-deletes even unmerged branches, and the instructor warned to be very careful copying this one-character difference from ChatGPT, since it can delete commits you're still working on. *(01:03:21)*

## 13. Setting up two conflicting pull requests ([8.3 What happens when my feature branch falls behind main?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#what-happens-when-my-feature-branch-falls-behind-main))

*01:04:00–01:10:00*

- **Q:** To practise merge conflicts alone, a student pushes `dan-fetch`, opens its pull request and merges it immediately. Only then do they create `dan-delete` from `main` and edit the same line. Critique this setup.
    - **A:** It won't produce the conflict. The key is not to merge the first pull request right away, but to keep it open while you create the second branch from the same `main`. That mimics two people with pull requests that change the same line. *(01:06:07)*

## 14. When a merge creates the conflict: resolving on GitHub

*01:10:00–01:12:44*

- **Q:** Pull requests #2 and #3 both show green buttons, so a teammate plans to open both tabs and click merge on each without coordinating. Judge this plan.
    - **A:** It is unsafe. Each pull request on its own gives no sign of a coming conflict. But once one is merged, `main` changes and GitHub rechecks every other pull request that targets `main`, which is how #3 ended up in conflict. Green buttons aren't a guarantee when people aren't paying attention and coordinating their work. *(01:10:31)*

- **Q:** A teammate resolves a conflict on line 13 of a script in GitHub's web editor by deleting the `<<<<<<<`, `=======` and `>>>>>>>` markers, but their choice renamed a variable that line 50 still uses. Is the conflict resolved?
    - **A:** No. In this class, fixing a conflict in code means the code works from top to bottom again, not just that the markers are gone. A change at the conflicting line can break code elsewhere, and that is still your problem to deal with. *(01:11:39)*

## 15. Resolving the conflict locally with rebase ([8.3.2 Using rebase](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#using-rebase))

*01:12:44–01:20:42*

- **Q:** After `git rebase main` and `git rebase --continue` on `dan-delete`, a student says a plain `git push origin dan-delete` should be enough, and that force-pushing is always wrong. Assess this claim.
    - **A:** The claim is wrong here. The rebase changed the branch's history: its commit now sits on a different parent. A simple push can't update it, so you can't get around force-pushing, as in class with `git push --force-with-lease origin dan-delete`. The instructor noted that this does "mangle history", and GitHub records that a force push happened, which matters in compliance settings. *(01:19:47)*

- **Q:** Midway through `git rebase main`, a student panics at the conflict and plans to delete the repository and re-clone. Recommend a better course.
    - **A:** Re-cloning is unnecessary. Let `git status` guide you: it tells you to `git add` the fixed file and then run `git rebase --continue`. If you're scared that something got messed up, `git rebase --abort` gets you back to the state before the rebase. *(01:18:20)*

---

- prompt: prompt-recall-5-evaluate.md @ 65eb21c
- prompt-hash: 6b82591e2f8e
- model: claude-opus-5-5 (requested: opus)
- backend: claude
- inputs: transcript-plaud.md, terminal.txt, materials.md, notes-class-main--claude-opus-5-5.md
- generated: 2026-11-23
- notes-input: notes-class-main--claude-opus-5-5.md @ d979d4ea6828, links and section references removed, diagrams removed
