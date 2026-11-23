# Git branches, pull requests and rebasing to fix conflicts: review questions, tier 5 — Evaluate

Date: 2026-11-17

Instructor: Daniel Chen

*Tier 5 of 5: Evaluate. Decide and justify your verdict before you read the answer; the criteria are the ones given in class.*

## 1. Course logistics: lab groups, attendance and interview week

*00:00:01–00:04:04*

- **Q:** A group plans to send one representative to each 522 lab while the others work from home, because the project lives on GitHub anyway. Assess this plan.
  **A:** The plan isn't acceptable. Lab attendance is mandatory because this is a group project. The TAs go around and talk to every group, and each member should be there when the TA arrives. *(00:02:19)*

- **Q:** Before interview week, a student says they don't need to understand one module in their group's code base, because an AI tool wrote it and a teammate merged it. Judge this position.
  **A:** It's a poor position. The interview covers your group's actual code base, and anything in it is "fair game" to be talked about, "especially in the world of AI." You are expected to know the code you're working in, just as you would at work. *(00:03:15)*

## 2. Why branches: escaping the 521 push/pull friction ([8 Git branches](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html))

*00:06:49–00:09:43*

- **Q:** Once each teammate owns a self-contained part of the project, the group proposes that everyone keeps committing and pushing directly to `main` all week, as in the 521 shared slide-deck exercise. Would you recommend this?
  **A:** No. When everyone pushes to the same place, you keep hitting the friction from 521: you can't push until you pull what someone else pushed first, even when there's no conflict. Working in parallel streams on branches puts each person in "your own little world." You can push and pull freely, and the work gets coordinated at review time. *(00:08:46)*

- **Q:** On the first day of the project, a group splits into four branches and starts four parallel pieces of work before anything shared exists. Critique this plan.
  **A:** It's unrealistic. Not every project can start with four parallel pieces of work. Early on, everyone is bound by one or two people getting the basics in place, so that friction will exist somewhere in a project no matter what. Parallel branches pay off once each person has a part that is solely their responsibility. *(00:07:50)*

## 3. Review: the local–remote picture

*00:09:46–00:11:47*

- **Q:** On the night of a milestone, a teammate says their section is done: it's committed on their laptop, but they haven't pushed. Judge whether their part is submitted.
  **A:** It isn't. What's on GitHub is the thing that matters: it's what gets graded and what gets published. Work that exists only on a local computer "effectively doesn't really exist" for grading or project purposes, like a product that can't ship because the code isn't anywhere. *(00:10:53)*

## 4. What a branch is: `main`, `HEAD` and `origin/main` ([8 Git branches](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html))

*00:12:03–00:17:54*

- **Q:** A teammate commits their half-finished exploratory plots straight to `main` so that everyone can see them. Would you accept that?
  **A:** No. Treat `main` as the stable "production" version: even if the project isn't finished, the code on it should work. Exploration that isn't ready belongs on the teammate's own branch. `main` holds shared, finished pieces, such as the cleaned dataset that everyone builds from. *(00:15:24)*

- **Q:** A student working alone says branches are pointless for them, because they can always undo a mistake with `git reset` or `git revert`. Assess this argument.
  **A:** It's technically true but a weak argument. The instructor uses branches even when he's the only one working, so he can section off work and test it before `main` changes. If an idea fails, deleting the branch and switching back to `main` is easy. Untangling one commit that did twenty things means digging through history. Reset and revert work, but branches make this easier. *(00:17:22)*

## 5. Creating and switching branches ([8.1 Creating a branch using the command line](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#creating-a-branch-using-the-command-line))

*00:17:54–00:26:29*

- **Q:** Two days after last pulling, a teammate opens their laptop and immediately runs `git switch -c` to start a new feature for the group project. Critique this sequence.
  **A:** They skipped a step. If your work builds on coordinated work, first confirm you're on `main` and run `git pull origin main`, so your starting point includes everything others have pushed. Otherwise you can waste time redoing or conflicting with work that already exists. The instructor described doing exactly that when he forgot he had done half the work on another laptop. *(00:18:09)*

## 6. `git checkout` and `git branch` versus `git switch` ([8.1.3 Useful command line Git branching commands](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#useful-command-line-git-branching-commands))

*00:26:40–00:28:26*

- **Q:** ChatGPT gives you a `git checkout` command to fix something in your group repository, and you aren't sure what it will do. You have uncommitted work you don't want to lose. Is it reasonable to run it as given?
  **A:** No. `checkout` doesn't only move `HEAD`: it also does what `restore` and `revert` do. If you don't know what a command does, prompt the AI for the `switch` version instead. When you're scared of losing work, think about the commands you type rather than pasting a working answer. *(00:27:41)*

## 7. Pushing a branch and viewing it on GitHub ([8.2 Useful things you can do with branches on GitHub](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#useful-things-you-can-do-with-branches-on-github))

*00:28:31–00:33:40*

- **Q:** After committing on `dan-b1`, a student switches to `main`, runs `git push`, sees `Everything up-to-date`, and concludes the branch is on GitHub. Judge this conclusion.
  **A:** It's wrong. Pushing from `main` sent nothing from `dan-b1`. With branches, *where* and *what* you push matter. You need to be on the branch and name it: `git push origin dan-b1`. *(00:29:34)*

- **Q:** A teammate finishes their branch and plans to merge it into `main` on their own laptop and push `main`, skipping GitHub. Would you recommend this?
  **A:** No. The easiest way to combine a branch with `main` is to not do it on your local computer at all. Do it through a review process, where you push the branch and merge it through a pull request. *(00:28:58)*

## 8. Opening a pull request ([9.1 Creating a pull request](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/github-pull-requests.html#creating-a-pull-request))

*00:33:40–00:41:16*

- **Q:** A pull request's file list includes a `.DS_Store` file and an `.ipynb_checkpoints` folder alongside the real changes. Should it be created and merged as is?
  **A:** No. Files that don't belong in the repository, such as checkpoint files, `.DS_Store` and Word backup files, lose points even when the instructions don't mention them. Checking the file list on the pull request page is your second line of defence. Remove them and keep your `.gitignore` up to date. *(00:38:44)*

- **Q:** As a pull request grows, its author leaves the original description untouched and adds a new comment each time ("now I'm also doing…"). Critique this habit.
  **A:** It's the wrong habit. The first comment is what people read, so all the changes should be defined and explained there. Edit the opening description instead of appending updates. *(00:40:55)*

- **Q:** A teammate never looks at the line at the top of the "Open a pull request" page, because in this course it always says `main`. Defend or critique this.
  **A:** Critique it. `main` is probably the target in this class, but it's still a good idea to look and make sure the words make sense: your branch, then the branch you're merging into. In 524 the target won't always be `main`, and with forks you must make sure you're sending code to the right place. *(00:36:50)*

## 9. Code review and updating a pull request ([10 Code review on GitHub](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/github-code-review.html))

*00:41:16–00:45:41*

- **Q:** While reviewing a teammate's pull request, a reviewer finds a bug and decides to rewrite the code themselves. Is that the right division of work?
  **A:** No. The rule of thumb is that if it's your pull request, it's your job to fix it. The reviewer's job is to say "rewrite this" or "this doesn't look right" in a comment, and the author makes the change. *(00:42:17)*

- **Q:** To address review comments on PR #1, a student plans to close it and open a fresh pull request with the fixes. Assess this plan.
  **A:** It's unnecessary. You don't need to close the pull request and create a new one. Go back to the branch it was opened from (`dan-b1`), then add, commit and push to that same branch, and the pull request updates. *(00:43:09)*

## 10. AI reviewers and draft pull requests ([9.2 Draft pull requests](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/github-pull-requests.html#draft-pull-requests))

*00:52:11–00:55:41*

- **Q:** A group requests a Copilot review on every pull request and agrees to apply every comment it makes. Judge this policy.
  **A:** Requesting the review is fine, because more eyes on something is never really a bad idea. Applying every comment is not. You don't have to keep every comment an LLM makes: you can push back, reject it or accept it. *(00:52:30)*

- **Q:** A teammate opens a pull request on day one for work that will take two weeks and leaves it as a normal open pull request. Would you recommend converting it to a draft?
  **A:** Yes. A draft shows a grey bar that tells everyone "you can look, but it isn't ready yet." It also greys out the merge button, so nobody can accidentally merge unfinished work. The instructor believes it also stops an agent from merging everything that's green. *(00:54:30)*

## 11. Merging and deleting the branch on GitHub ([8.2 Useful things you can do with branches on GitHub](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#useful-things-you-can-do-with-branches-on-github))

*00:55:41–00:59:07*

- **Q:** After PR #1 is merged, a student refuses to click "Delete branch" on `dan-b1`, worried that this will erase its commits. Is the worry justified?
  **A:** No. Deleting the branch removes only the name. `main`'s history still shows the branch's two commits plus the merge commit, so you can still find and undo the feature later. Cleaning up keeps the branch list from growing into a giant, stale list. *(00:58:19)*

- **Q:** A data team at a regulated workplace adopts "always delete branches after merging" from this class. Is the rule appropriate there?
  **A:** Not necessarily. If there is a legal or compliance requirement, don't delete branches; some places don't allow it. The team's workflow decides. Where nothing forbids it, at least clean up your own branches. *(00:57:00)*

## 12. Syncing and cleaning up locally after a merge ([8.1.3 Useful command line Git branching commands](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#useful-command-line-git-branching-commands))

*00:59:07–01:03:51*

- **Q:** ChatGPT suggests `git branch -D dan-b1` to tidy up after a merge. Would you run it?
  **A:** Use lowercase `git branch -d dan-b1` instead. Lowercase `-d` refuses to delete a branch that hasn't been merged, because Git makes it harder to lose work. Capital `-D` force-deletes regardless. The two differ by one character, so be very careful copying commands from ChatGPT, because you could delete commits you're still working on. *(01:03:21)*

- **Q:** After PR #1 is merged on GitHub, a student runs `git switch main` and starts a new branch right away, assuming local `main` now includes the merge. Critique this.
  **A:** The assumption is wrong. Local `main` doesn't update itself, so you need a synchronisation step: `git pull origin main` while on `main`. In class, that step brought in the merged lines of `README.md`. *(01:00:17)*

- **Q:** A student wants their local view of the remote to drop the deleted `origin/dan-b1`, but doesn't want any files on disk to change. Is `git pull` or `git fetch --prune` the better choice?
  **A:** `git fetch --prune`. `git pull` runs fetch and then a merge, which changes your files. `fetch` alone only coordinates the history, and `--prune` removes local references to branches that were deleted on GitHub. *(01:01:52)*

## 13. Setting up two conflicting pull requests ([8.3 What happens when my feature branch falls behind main?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#what-happens-when-my-feature-branch-falls-behind-main))

*01:04:00–01:10:00*

- **Q:** To practise conflicts on their own, a student opens a pull request from `dan-fetch` and merges it immediately, then creates `dan-delete` from `main` to edit the same line. Will this plan produce the conflict they want?
  **A:** No. The key is not to merge the first pull request right away. Leave it open while you create the second branch from the same `main` commit, so both edit the same line in parallel. If the first is merged before the second branch exists, the second starts from the updated file and there's nothing to conflict. *(01:06:07)*

- **Q:** PRs #2 and #3 both show green and say they can be merged into `main`, so a teammate plans to click every green button without coordinating. Assess this plan.
  **A:** It's risky. Nothing on a pull request warns you that another one edits the same line. Once one is merged, `main` changes and GitHub rechecks every other pull request targeting `main`, so the second one can turn into a conflict. *(01:10:08)*

## 14. When a merge creates the conflict: resolving on GitHub ([8.3 What happens when my feature branch falls behind main?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#what-happens-when-my-feature-branch-falls-behind-main))

*01:10:00–01:12:44*

- **Q:** A teammate resolves a conflict on line 13 of an analysis script by deleting the `<<<<<<<`, `=======` and `>>>>>>>` markers. A variable they renamed there is still used under its old name on line 50. Is the conflict resolved?
  **A:** No. In this class, fixing a conflict means the code works from top to bottom again, not just that the markers are gone. A change at the conflicting line can break code elsewhere, and that's still the author's problem to deal with. *(01:11:39)*

- **Q:** A group rule says every conflict must be resolved locally, never in GitHub's web editor. Is that rule justified?
  **A:** Not for every case. Simple conflicts can be resolved in the web editor, and that's fine. The instructor showed the local route because it's more involved, not because the web route is wrong. *(01:12:19)*

## 15. Resolving the conflict locally with rebase ([8.3.2 Using rebase](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/git-branches.html#using-rebase))

*01:12:44–01:20:42*

- **Q:** To fix the conflicting PR #3, a student runs `git switch dan-delete` and `git rebase main` without first updating local `main`. Critique this sequence.
  **A:** It skips step one. The commit that was merged into `main` on GitHub has to be on your computer first: `git switch main`, then `git pull origin main`. Only then switch back and run `git rebase main`, so your commits are replayed on top of the change you conflict with. *(01:13:42)*

- **Q:** After a successful `git rebase --continue` on `dan-delete`, a student expects a plain `git push origin dan-delete` to update PR #3. Will it work?
  **A:** No. The rebase changed the commit's history: its parent is now the updated `main`. A plain push won't go through, and you can't get around force pushing. In class, `git push --force-with-lease origin dan-delete` worked, and GitHub then recorded the force push, since you've "mangled history." *(01:19:34)*

- **Q:** Halfway through a rebase with a conflict, a nervous teammate wants to delete the project folder and re-clone. Is that a sensible response?
  **A:** No. Let `git status` guide you: it tells you to `git add` the resolved file and then run `git rebase --continue`. If you're scared something got messed up, `git rebase --abort` returns you to where you started. *(01:18:20)*

- **Q:** A teammate who knows Git well says rebasing to fix conflicts is wrong and insists on another method. Is your rebase therefore incorrect?
  **A:** No. There are many ways to fix a conflict on your computer. The instructor uses rebase and expects people who know their way around Git to have opinions, "and that's okay." What counts is that the conflict is properly fixed and the branch can merge. *(01:12:48)*

---

- prompt: prompt-recall-5-evaluate.md @ 8bcc190
- prompt-hash: 91dbb814d755
- model: claude-opus-5-5 (requested: opus)
- backend: claude
- inputs: transcript-plaud.md, terminal.txt, materials.md, notes-class-main--claude-opus-5-5.md
- generated: 2026-11-20
- notes-input: notes-class-main--claude-opus-5-5.md @ d979d4ea6828, links and section references removed
