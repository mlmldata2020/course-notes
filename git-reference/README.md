# Git Reference

[Push changes to a remote repository: quick steps](#Push-changes-to-a-remote-repository-quick-steps)

[Initialize a local repository on your computer](#initialize-a-local-repository-on-your-computer)

[Set up a remote repository on GitHub](#Set-up-a-remote-repository-on-GitHub)

## Push changes to a remote repository: quick steps

If you have already [initialized a local repository on your computer](#Initialize-a-local-repository-on-your-computer) and [set up a remote repository on GitHub](#Set-up-a-remote-repository-on-GitHub), running the three commands below in your local project directory will add all new files and changes and push them to GitHub.

```
git add .
git commit -m "Write a descriptive commit message here."
git push origin master
```
__Replace the commit message between the quotes with a brief description of the changes that you have made.__

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

Follow the quick steps to [push changes to a remote repository](#Push-changes-to-a-remote-repository:-quick-steps)

You only have to do this once for each project.
