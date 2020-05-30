A version control system to record what was done and when, by who.

# term
**commit:** record the changes that are made at each step (each one becomes a version with associated information/metadata) when we want it to
**repository: ** complete history of commits/metadata for a particular project
**branching: ** go back to previous versions and modify in a different direction



set up a repository
manipulate the contents of a repository
store a repository on GitHub to make it available to others
interact with our repository/repositories on GitHub
toring code in repositories, and/or on GitHub


```bash
git init
ls -IR .git
ls -lR .git
```
# configure
`git config` will generate `.gitconfig` file that stores all the relevant bits of information for using git.
```bash
# name and email address
git config --global user.name "LumingLin"
git config --global user.email "s1949868@ed.ac.uk"
git config --global merge.tool vimdiff
git config --global merge.conflictstyle diff3
git config --global mergetool.prompt false
# preferred Unix text editor
git config --global core.editor "vim -w"
git config --list
git config --global core.autocrlf inuput
git config --global alias.st status

```

```bash
touch .gitignore
echo -e "mypasswordsfile\n*.pdf\n*.c\n*.log" >> .gitignore
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE5MTQwMTAxNzAsMTc2NDIwMzc1LC03Mz
Y0MjEyMzgsLTEwNzI4MTA5NjIsMjEyMTUzNTAyMiwxMjE0MzQy
MzcxLC0xMzM5ODM3MjU2LC01NTEyMDAwMSwtMjAxMTk1NDQwMC
wxODExODkxNTksMTY1MDM5NDA4NywtNzg4OTQ0MTUyLDE0OTQ5
Mzc2NTIsMjk1Mjc2MTUwLDE2NDUzNTgwNDcsLTc3MTI3NjY2NC
wyNDE2MDQyNDAsLTE5NTI3NjE1NTgsODU0MTkzNzE5LDE2MDI5
NzI3OTddfQ==
-->