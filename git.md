set up a repository





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
eyJoaXN0b3J5IjpbMTgxMTg5MTU5LDE2NTAzOTQwODcsLTc4OD
k0NDE1MiwxNDk0OTM3NjUyLDI5NTI3NjE1MCwxNjQ1MzU4MDQ3
LC03NzEyNzY2NjQsMjQxNjA0MjQwLC0xOTUyNzYxNTU4LDg1ND
E5MzcxOSwxNjAyOTcyNzk3XX0=
-->