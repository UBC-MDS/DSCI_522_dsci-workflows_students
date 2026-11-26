# Docker Compose and data validation with pointblank: review questions, tier 5 — Evaluate

Date: 2026-11-25

Instructor: Daniel Chen

*Tier 5 of 5: Evaluate. Decide and justify your verdict before you read the answer; the criteria are the ones given in class.*

## 2. Creating and cloning the repository

*00:04:52–00:07:44*

- **Q:** You are working inside your cloned `2026-11-25-docker-validate` folder and want to try the reference repository, so you plan to run `git clone` for it right there, inside the repository. Judge whether this plan is acceptable.
    - **A:** No, it is not acceptable. Cloning there nests one Git repository inside another, which the course says to avoid (from 521). Clone into a folder such as `~/git` instead, a place you know is not inside another repository. *(00:06:22)*

## 3. Using the template repository responsibly

*00:07:44–00:08:59*

- **Q:** A teammate copies the whole base template repository into your group project. It works, so they commit it under their name without reading it. Assess this approach.
    - **A:** It falls short of the standard set in class. A template is fine for saving typing and avoiding mistakes, but you are still responsible for understanding the work. Getting the work done is a given; what you are tested or interviewed on is whether you understand it. Any commit with your name on it is fair game for a question. *(00:08:23)*

## 4. The `Dockerfile`: base image and system software ([29.3 Choosing a base image for your Dockerfile](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#choosing-a-base-image-for-your-dockerfile))

*00:08:59–00:13:18*

- **Q:** Your group's project uses only Python, and a teammate wants to keep `FROM rocker/r-ver:4.6.2` because "it works for Python anyway." Would you approve this in a pull request?
    - **A:** It would work, but it is a poor choice. The R components take up extra storage, so everyone who uses the image downloads more, including the people grading it. The class's goal is the smallest image that has the bare minimum you need. A plain Ubuntu base suits a Python-only project better. *(00:09:51)*

- **Q:** To speed up builds, a teammate deletes the Quarto installation section from your milestone `Dockerfile`, as the instructor did in today's demo. Is that acceptable for the milestone?
    - **A:** No. Quarto was deleted only because today's class didn't need it. For your milestones, the container has to run your report, so it must install every piece of software the report needs, Quarto included. *(00:13:10)*

## 5. Installing `uv` and controlling tool versions ([29.1 Building container images from `Dockerfile`'s](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-building.html#building-container-images-from-dockerfiles))

*00:13:18–00:15:30*

- **Q:** A teammate argues that `pyproject.toml` and `uv.lock` already pin everything, so the `Dockerfile` can install whatever `uv` is current instead of `COPY --from=ghcr.io/astral-sh/uv:0.13.7`. Defend or reject this argument.
    - **A:** Reject it. Virtual environments control package versions, but `pyproject.toml` doesn't track the version of `uv` itself. The whole point of Docker is complete control over every piece of software installed, the tools included. Pinning the `uv` image tag provides that control. *(00:14:46)*

- **Q:** A tutorial you found online installs its packages from a `requirements.txt`, and a teammate wants to paste those steps into the project's `Dockerfile` as they are. Judge this plan.
    - **A:** Don't paste them blindly. MDS uses Python through `uv`, and outside instructions may not be `uv`-compatible; `requirements.txt` is not how `uv` generally works. Translate the steps into the project's `uv` workflow. *(00:13:22)*

## 6. `WORKDIR` and the `.venv` problem

*00:15:30–00:19:28*

- **Q:** A pull request removes `ENV UV_PROJECT_ENVIRONMENT=/opt/venv` from the `Dockerfile` as "unnecessary configuration." The team always runs the container with the project folder mounted. Would you approve it?
    - **A:** No. Without that line, `uv` uses the project's `.venv`. Mounting the folder brings in the laptop's `.venv`, which was built for a different operating system and CPU and doesn't match the container's Linux. With the line, the packages go into `/opt/venv` for Linux, and the mounted `.venv` is simply ignored. *(00:18:25)*

## 7. Environment variables, `uv sync --locked`, and the SSH setup

*00:27:21–00:30:18*

- **Q:** A teammate changes `RUN uv sync --locked` to `RUN uv sync` because the build "failed for no reason" after they edited `pyproject.toml`. Assess this change.
    - **A:** It is a bad change. `--locked` is a guard: the build fails when `pyproject.toml` and `uv.lock` are out of sync, which is exactly what happened here. It checks that what you want is what you expect. The right fix is to bring the lock file back in sync, not to remove the check. *(00:29:15)*

## 8. `pyproject.toml` and `.python-version`

*00:30:18–00:33:30*

- **Q:** To keep settings in one place, a teammate proposes moving the `/opt/venv` environment location out of the `Dockerfile` and into `[tool.uv]` in `pyproject.toml`. Recommend for or against.
    - **A:** Recommend against it. A setting in `pyproject.toml` would also apply on your own laptop. You want Docker to behave slightly differently from your computer, so that setting belongs in the `Dockerfile`. *(00:31:47)*

## 11. Mounting the project folder with `-v`

*00:38:22–00:42:42*

- **Q:** While actively developing the analysis, a teammate replaces the `-v` mount with a `COPY . .` line in the `Dockerfile`, so the files are "inside the container." Judge this approach.
    - **A:** It is a poor fit during active work. `COPY` captures the files only as they were at `docker build` time, so every change to the analysis would need a rebuild. Mounting gives a two-way sync in which changes appear immediately on both sides. Put the software in the image and mount the files. *(00:40:06)*

- **Q:** So that `git push` works inside the container, a teammate proposes copying their SSH key and Git credentials into the image. Is this acceptable?
    - **A:** No, it is a security problem. Your SSH key is effectively the password to your account, and anyone who pulls the container could find it. The container also resets every time and looks like a brand-new machine to GitHub. Mount the folder and run your Git commands on your own computer. *(00:41:50)*

- **Q:** At the end of a project, you must submit a frozen version of the analysis for compliance. Is it acceptable to `COPY` the project files into the image instead of mounting them?
    - **A:** Yes, in that case copying is appropriate, because the files then become part of the container itself. The advice against copying applies while you are actively working, when you don't want to rebuild constantly. *(00:42:20)*

## 12. Shared files and editing in two places

*00:42:42–00:44:42*

- **Q:** You edited `hello.py` inside the container through the mount. It is still open in your laptop's editor, which asks whether to overwrite when you save. You plan to click "overwrite." Assess this plan.
    - **A:** It is risky. Overwriting discards the changes made on the other side; it is like a Git conflict with no Git to help, and the last save wins. If you know you work in several places, use the IDE's revert file command before editing. *(00:43:59)*

## 13. The `docker-compose.yml` file ([33.1 Docker Compose to launch containers](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-docker-compose.html#docker-compose-to-launch-containers))

*00:44:42–00:52:06*

- **Q:** A teammate changes the `ports:` entry in `docker-compose.yml` from `"2222:22"` to `"22:22"` so the numbers "match." Would you approve it?
    - **A:** No. Port 22 is a very common port used for real things on your computer, so mapping it risks clashing with it by accident. The first number is the port on your own computer, and remapping it to 2222 avoids that clash. *(00:49:03)*

- **Q:** Someone shares a Compose file, you follow its README, and the app "doesn't work" at the port you tried. You conclude the file is broken. Judge that conclusion.
    - **A:** It is premature. When you get these files from others, check the first port number in each mapping, because that is where you connect on your own computer. A common reason something "doesn't work" is looking at the wrong port. *(00:49:43)*

- **Q:** A teammate installs an extra package by hand inside the running container, then plans to rely on it in the next session without touching the `Dockerfile`. Assess this plan.
    - **A:** It won't work. When the container is turned off and on again, it resets to what was built, and only mounted folders keep their changes. Installing by hand is fine as a sandbox experiment, but anything you need to keep must go into the image. *(00:50:38)*

- **Q:** Curious about `rm -rf /`, a classmate plans to try it on their laptop to see what happens. Recommend where, if anywhere, they should do this.
    - **A:** Never on their own computer, because it destroys the system. A container is a good place to try it: it kills the container, but turning the container off and on again resets it. *(00:51:42)*

## 14. Docker Compose commands ([33.2 Docker Compose commands](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-docker-compose.html#docker-compose-commands))

*00:52:06–00:58:03*

- **Q:** A teammate prefers to document the project's twenty-line `docker run` command in the README for others to copy and paste, rather than add a `docker-compose.yml`. Which would you recommend, and why?
    - **A:** Recommend the `docker-compose.yml`. Pasted long commands break on spaces, line breaks or a missing backslash, and in the terminal you can only move with the arrow keys to edit them. A file is documented, easier to change and experiment with, and plays well with version control. *(00:53:39)*

- **Q:** You use `docker compose up --detach` for several projects and never run `docker compose down`, since the containers "just sit in the background." Assess this habit.
    - **A:** It is a bad habit. Containers are essentially other computers that take up RAM, and with many running at once your free memory keeps shrinking. Be diligent about running `docker compose down` from your own computer. *(00:57:38)*

## 15. Running commands non-interactively ([33.3 Running a Docker container non-interactively using the Docker Compose](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-docker-compose.html#running-a-docker-container-non-interactively-using-the-docker-compose))

*00:58:03–01:01:10*

- **Q:** To fix `python` not being found, a teammate proposes switching the project to a prebuilt Python base image so that `docker compose run --rm analysis-env python` works. Judge this fix.
    - **A:** It is the wrong fix. A prebuilt Python image may have `python`, but your packages were installed through `uv`, so plain Python won't have them; the two are different installations. Use `uv run python`, the Python from `uv` with everything installed. *(00:59:22)*

- **Q:** Your report renders on your laptop, so a teammate says there is no need to also run `uv run quarto render` inside the container before submitting. Argue for or against.
    - **A:** Argue against it. The course is about reproducibility: you built a machine, and you test it by sending it commands. Rendering the report in the container checks that it builds in the custom environment, not just on your laptop. This is also one of the ways the project is graded. *(01:00:35)*

## 16. Connecting Positron or VS Code to the container over SSH

*01:01:10–01:06:55*

- **Q:** A classmate using Positron plans to open the container through Microsoft's container extension, as VS Code users do, and to connect to `localhost` without giving a username. Critique this plan.
    - **A:** Both parts fail. Forks such as Positron don't have access to Microsoft's extension store, so they connect with Remote SSH. Without a username, the connection uses your laptop's username, which doesn't exist in the container, so connect as `root` on the mapped port. *(01:02:23)*

- **Q:** Your laptop is short on RAM. You plan to keep the container running all day with Positron connected to it, instead of testing locally and running only the final command in the container. Judge this choice.
    - **A:** It is a poor choice for a resource-constrained laptop. The instructor tests locally and runs only the last command in the container, so not everything is open and running at once. If you are short on resources, don't keep Docker running unnecessarily. *(01:06:42)*

## 18. Adding the validation packages

*01:08:33–01:10:16*

- **Q:** `uv add pandera pointblank` fails with an error about a missing `[project]` table. A teammate wants to install the packages some other way outside `uv` just to get unblocked. Judge this compared with the workaround used in class.
    - **A:** Reject it in favour of the class's workaround. Adding the packages to `dependencies` in `pyproject.toml` by hand and running `uv sync` keeps everything in `uv` and regenerates the lock file from the TOML file. Stepping outside `uv` is where things go wrong, because the packages end up in a different installation. *(01:09:59)*

## 19. Why validate data, and exploring missing values ([41.1 Where are the missing values?](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/data-validation-python-pointblank.html#where-are-the-missing-values))

*01:10:16–01:13:41*

- **Q:** A health survey column contains many values of `99`. They fall within a plausible range, so a teammate plans to treat them as real measurements. Assess this plan.
    - **A:** It is risky. Survey data often codes missing values as `99`, and those are not real values. Check the codebook and treat them as missing where it says so. *(01:12:15)*

## 20. Building a validation with thresholds ([41.2 Checking values](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/data-validation-python-pointblank.html#checking-values))

*01:13:41–01:18:29*

- **Q:** A teammate proposes putting all of the project's pointblank checks in a single block at the end of the analysis. Recommend for or against.
    - **A:** Recommend against it. Data checks belong at several points, for example right after data cleaning and right before modelling, and which checks you need depends on the stage of the analysis. Checks at different points are also a natural way to split work in a team. *(01:15:31)*

## 21. Failing checks and splitting passing and failing rows ([41.4 Splitting the passing and failing rows](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/data-validation-python-pointblank.html#splitting-the-passing-and-failing-rows))

*01:18:29–01:20:48*

- **Q:** To keep things short, a teammate adds the missing-value checks to the same `pb.Validate()` chain as the value-range checks. Judge this design.
    - **A:** It is not what the class recommended. The instructor highly recommended checking missing values as a separate analysis, per column and then per row, kept apart from the checks on values. *(01:18:52)*

- **Q:** Your modelling teammate plans to wait until the data cleaner has fixed every row before starting the pipeline. Assess this plan, and say what pointblank offers instead.
    - **A:** It is a poor plan: data is never going to be 100% clean, so downstream work shouldn't wait for it. With `get_sundered_data(type="pass")` and `get_sundered_data(type="fail")`, you can hand the passing rows to the next teammate so they can build the pipeline now. Cleaning continues on the failing rows, and both can be saved as CSV files. *(01:19:36)*

---

- prompt: prompt-recall-5-evaluate.md @ 65eb21c
- prompt-hash: 6b82591e2f8e
- model: claude-opus-5-5 (requested: opus)
- backend: claude
- inputs: transcript-plaud.md, terminal.txt, materials.md, notes-class-main--claude-opus-5-5.md
- generated: 2026-11-25
- notes-input: notes-class-main--claude-opus-5-5.md @ 06f3ac544b79, links and section references removed, diagrams removed
