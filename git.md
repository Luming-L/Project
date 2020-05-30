A version control system to record what was done and when, by who.

# term


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
eyJoaXN0b3J5IjpbLTE0NzIzMzg1NDUsLTEwNzI4MTA5NjIsMj
EyMTUzNTAyMiwxMjE0MzQyMzcxLC0xMzM5ODM3MjU2LC01NTEy
MDAwMSwtMjAxMTk1NDQwMCwxODExODkxNTksMTY1MDM5NDA4Ny
wtNzg4OTQ0MTUyLDE0OTQ5Mzc2NTIsMjk1Mjc2MTUwLDE2NDUz
NTgwNDcsLTc3MTI3NjY2NCwyNDE2MDQyNDAsLTE5NTI3NjE1NT
gsODU0MTkzNzE5LDE2MDI5NzI3OTddfQ==
-->