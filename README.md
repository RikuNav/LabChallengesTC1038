# LabChallengesTC1038

Optional challenges for the **TC1038 Programming Laboratory**.

This repository contains additional programming challenges designed to help students practice and reinforce the concepts covered in class. The challenges are **optional** and are intended for students who want additional practice or a greater challenge.

> **Important:** This repository belongs to the course professors. Students should **not** push their solutions directly to this repository.

---

## 📚 Repository Structure

Each challenge is organized in its own directory:

```text
LabChallengesTC1038/
├── README.md
├── Challenge01/
│   └── README.md
├── Challenge02/
│   └── README.md
├── Challenge03/
│   └── README.md
└── ...
```

Each challenge should include its own instructions, requirements, and any necessary files.

---

# 👨‍🎓 Instructions for Students

## 1. Fork the Repository

Since this repository belongs to the professors, you must first create your own copy of the repository using a **fork**.

Go to the repository on GitHub and click:

**Fork → Create fork**

This will create a copy of `LabChallengesTC1038` under your own GitHub account.

Your fork will look something like:

```text
YourUsername/LabChallengesTC1038
```

while the original repository remains:

```text
Professor/LabChallengesTC1038
```

---

## 2. Clone Your Fork

Clone **your fork**, not the original repository:

```bash
git clone https://github.com/YOUR-USERNAME/LabChallengesTC1038.git
```

Then enter the repository:

```bash
cd LabChallengesTC1038
```

---

## 3. Work on a Challenge

Choose the challenge you want to solve and read its instructions carefully.

For example:

```text
Challenge01/
Challenge02/
Challenge03/
```

Complete your solution **inside your own fork**.

Do not modify the original professors' repository.

---

## 4. Commit Your Work

Once you have completed a challenge, add your changes:

```bash
git add .
```

Create a commit:

```bash
git commit -m "Complete Challenge 01"
```

Then push your changes to your fork:

```bash
git push
```

---

## 5. Submit Your Work

If your professor asks you to submit the challenge, create a **Pull Request** from your fork to the original repository.

On GitHub:

1. Open your fork.
2. Select **Pull requests**.
3. Click **New pull request**.
4. Make sure the **base repository** is the professors' `LabChallengesTC1038` repository.
5. Make sure the **head repository** is your fork.
6. Select the appropriate branch.
7. Add a description of your solution.
8. Create the Pull Request.

### ⚠️ Important

Creating a Pull Request **does not mean your changes are automatically added to the course repository**.

The professors will review the Pull Request before deciding whether it should be merged.

---

# 🔄 Keeping Your Fork Updated

The original repository may receive new challenges or updates during the semester.

To keep your fork synchronized with the professors' repository, you can add it as an `upstream` remote.

First, check your current remotes:

```bash
git remote -v
```

Add the original repository as `upstream`:

```bash
git remote add upstream https://github.com/RikuNav/LabChallengesTC1038.git
```

Then retrieve the latest changes:

```bash
git fetch upstream
```

Update your local branch:

```bash
git merge upstream/main
```

Finally, push the updates to your fork:

```bash
git push
```

---

# 📌 Rules

- Do **not** push directly to the professors' repository.
- Always work from your own fork.
- Do not modify the challenge instructions unless explicitly authorized.
- Keep your solutions organized according to the structure specified by each challenge.
- Do not upload unnecessary files, such as IDE configuration files, compiled binaries, or personal files.
- Follow the programming style and submission requirements specified by the professor.
- If a challenge requires a Pull Request, submit it through GitHub.
- It's forbidden the use of AI for solving any problem.


## 💡 Recommended Workflow

```
              Original Repository
                (Professors)
                     │
                     │ Fork
                     ▼
                Your Fork
                     │
                     │ Clone
                     ▼
              Local Repository
                     │
                     │ Solve challenge
                     ▼
                   Commit
                     │
                     │ Push
                     ▼
                Your Fork
                     │
                     │ Pull Request
                     ▼
              Original Repository
                (Professors)
```


## 🎯 Purpose

These challenges are intended to provide **additional practice** beyond the regular laboratory activities.

They are optional unless your professor explicitly states otherwise.

Good luck and have fun solving the challenges! 🚀
