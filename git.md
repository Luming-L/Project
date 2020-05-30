A version control system to record what was done and when, by who.

# term
**commit: **record the changes that are made at each step (each one becomes a version with associated information/metadata) when we want it to
**repository: **complete history of commits/metadata for a particular project

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
eyJoaXN0b3J5IjpbLTczNjQyMTIzOCwtMTA3MjgxMDk2MiwyMT
IxNTM1MDIyLDEyMTQzNDIzNzEsLTEzMzk4MzcyNTYsLTU1MTIw
MDAxLC0yMDExOTU0NDAwLDE4MTE4OTE1OSwxNjUwMzk0MDg3LC
03ODg5NDQxNTIsMTQ5NDkzNzY1MiwyOTUyNzYxNTAsMTY0NTM1
ODA0NywtNzcxMjc2NjY0LDI0MTYwNDI0MCwtMTk1Mjc2MTU1OC
w4NTQxOTM3MTksMTYwMjk3Mjc5N119
-->