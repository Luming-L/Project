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
eyJoaXN0b3J5IjpbMTY1MDM5NDA4NywtNzg4OTQ0MTUyLDE0OT
Q5Mzc2NTIsMjk1Mjc2MTUwLDE2NDUzNTgwNDcsLTc3MTI3NjY2
NCwyNDE2MDQyNDAsLTE5NTI3NjE1NTgsODU0MTkzNzE5LDE2MD
I5NzI3OTddfQ==
-->