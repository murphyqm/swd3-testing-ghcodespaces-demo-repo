# Template repository

You can create your own version of this repository by clicking the `Use Template` option.

You can set the name of your new repository to your Python project name. See [our webapp](https://package-your-python.streamlit.app/) for details on choosing a package and project name.

## Launch in codespaces

This repository contains a `devcontainer.json` file, which includes details to set up a cloud virtual machine in GitHub codespaces.

Once you launch the codespace from your repository (it will take a while to set up), you will have a view that matches the app VSCode, including a terminal
window at the bottom of the screen, which allows you to interact with the virtual machine.

If you use `pwd` to check the working directory, you will get `/workspaces/YOUR-REPO-NAME`: you are positioned inside the git repository folder. This is essentially
a local clone of the repository on a virtual machine; you will have to use git as your would on your desktop (such as pushing changes to `origin BRANCH-NAME` from the terminal).

## Essential linux/bash commands

The virtual machine is running on Ubuntu, a Linux distribution.

```bash
cd # change directory to home
cd /workspaces # return to the /workspaces directory
cd .. # go up a level in the directory structure
ls # list the contents of the current directory
pwd # get the path to the current working directory
```

## Essential git commands

We will use git and a GitHUb remote to track our changes. You can use git in the same way you would from your local machine.

```bash
git status # check on status of current git repo
git branch NAME # create a branch called NAME
git checkout NAME # swap over to the branch called NAME
git add . # stage all changed files for commit, you can replace "." with FILE to add a single file called FILE
git commit # commit the staged files (this will open your text editor to create a commit message)
git push origin NAME # push local commits to the remote branch tracking the branch NAME
```

## Essential conda commands

The devcontainer/codespaces virtual machine comes preloaded with `miniforge`, an open source alternative to anaconda with the fast
libmamba solver available. You use this in the same way you would conda from your local machine. Your codespaces machine
comes with a basic Python packaging environment prebuilt.

```bash
# from terminal/outside a conda env
conda env list # list built environments
conda env create --file PATH/TO/A/FILE # build a conda env from a file
conda env create --file .devcontainer/env-files/linting-env.yml # build a conda env from a file
conda activate ENV-NAME  # activate the environment ENV-NAME

# from inside a conda env (after activating the env)
conda list # lists installed packages in the env
conda env export --no-builds > exported-env.yml # exports all packages in the env
conda env export --from-history  > exported-env.yml # exports the packages that were explicitly installed
```

## mkdocs commands

```bash
mkdocs new . # initialise a new mkdocs project
TZ=UTC mkdocs serve # serve the mkdocs website without time zone errors
```