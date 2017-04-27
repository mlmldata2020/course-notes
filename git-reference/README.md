# Git Reference

[Push changes to a remote repository: quick steps](#push-changes-to-a-remote-repository-quick-steps)

[Initialize a local repository on your computer](#initialize-a-local-repository-on-your-computer)

[Set up a remote repository on GitHub](#set-up-a-remote-repository-on-github)

## Push changes to a remote repository: quick steps

If you have already [initialized a local repository on your computer](#initialize-a-local-repository-on-your-computer) and [set up a remote repository on GitHub](#set-up-a-remote-repository-on-github), running the three commands below in your local project directory will add all new files and changes and push them to GitHub.

```
git add .
git commit -m "Write a descriptive commit message here."
git push origin master
```

Note that `git add .` adds all files in the working directory and subdirectory to the repository. You can also add specific files.

```
git add file1.txt file2.txt file3.txt
```

__Replace the commit message between the quotes with a brief description of the changes that you have made.__

## Ignoring and removing files from your repository

__Ignoring files__

Create a text file called `.gitignore` and place it in the main directory of your project. The contents of the file should contain a list of files (or file patterns) that are on your computer, but do not want to share with others (e.g. `.DS_Store`,`Thumbs.db`,`*.pyc`).

For more information: https://www.atlassian.com/git/tutorials/gitignore

__Removing files from your repository without removing them from your computer__

```
git rm --cached file1.txt file2.txt file3.txt
```

## Initialize a local repository on your computer

Run the following command in your local project directory:

```
git init
```

You only have to do this once for each project. You do not have to run this command in sub-directories.

## Set up a remote repository on GitHub

Go to the [class GitHub page](https://github.com/mlmldata2017) or your own GitHub account page

Click the green "New" button

Enter a name for the repository and select whether the repository will be public or private

In the project directory on your local computer, run the following command:
```
git remote add origin https://github.com/mlmldata2017/repository-name.git
```

__Replace the address above with the address of the remote repository you created on GitHub.__

If you have not done so already, [initialize a local repository on your computer](#initialize-a-local-repository-on-your-computer)

Follow the quick steps to [push changes to a remote repository](#push-changes-to-a-remote-repository-quick-steps)

You only have to do this once for each project.
