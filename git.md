A version control system to record what was done and when, by who.

# term
**commit:** record the changes that are made at each step (each one becomes a version with associated information/metadata) when we want it to
**repository: ** complete history of commits/metadata for a particular project
**branching: ** 
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
eyJoaXN0b3J5IjpbLTM1OTgyNjEzNiwtNzM2NDIxMjM4LC0xMD
cyODEwOTYyLDIxMjE1MzUwMjIsMTIxNDM0MjM3MSwtMTMzOTgz
NzI1NiwtNTUxMjAwMDEsLTIwMTE5NTQ0MDAsMTgxMTg5MTU5LD
E2NTAzOTQwODcsLTc4ODk0NDE1MiwxNDk0OTM3NjUyLDI5NTI3
NjE1MCwxNjQ1MzU4MDQ3LC03NzEyNzY2NjQsMjQxNjA0MjQwLC
0xOTUyNzYxNTU4LDg1NDE5MzcxOSwxNjAyOTcyNzk3XX0=
-->