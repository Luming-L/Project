We need "version control" so that we have a clear record of what was done and when, by who.

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
```bash
git config --global user.name "LumingLin"
git config --global user.email "s1949868@ed.ac.uk"
git config --global merge.tool vimdiff
git config --global merge.conflictstyle diff3
git config --global mergetool.prompt false
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
eyJoaXN0b3J5IjpbMTIxNDM0MjM3MSwtMTMzOTgzNzI1NiwtNT
UxMjAwMDEsLTIwMTE5NTQ0MDAsMTgxMTg5MTU5LDE2NTAzOTQw
ODcsLTc4ODk0NDE1MiwxNDk0OTM3NjUyLDI5NTI3NjE1MCwxNj
Q1MzU4MDQ3LC03NzEyNzY2NjQsMjQxNjA0MjQwLC0xOTUyNzYx
NTU4LDg1NDE5MzcxOSwxNjAyOTcyNzk3XX0=
-->