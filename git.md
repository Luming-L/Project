set up a repository
manipulate the contents of a repository
store a repository on GitHub to make it available to others



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
eyJoaXN0b3J5IjpbLTU1MTIwMDAxLC0yMDExOTU0NDAwLDE4MT
E4OTE1OSwxNjUwMzk0MDg3LC03ODg5NDQxNTIsMTQ5NDkzNzY1
MiwyOTUyNzYxNTAsMTY0NTM1ODA0NywtNzcxMjc2NjY0LDI0MT
YwNDI0MCwtMTk1Mjc2MTU1OCw4NTQxOTM3MTksMTYwMjk3Mjc5
N119
-->