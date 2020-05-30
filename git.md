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
`git config` will generate `.gitconfig` file that stores git settings.
A `.gitconfig` file can be found at one or more of three different locations, depending on how we set things up.

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
eyJoaXN0b3J5IjpbLTU4Mzk4NzAzMiwtMTkxNDAxMDE3MCwxNz
Y0MjAzNzUsLTczNjQyMTIzOCwtMTA3MjgxMDk2MiwyMTIxNTM1
MDIyLDEyMTQzNDIzNzEsLTEzMzk4MzcyNTYsLTU1MTIwMDAxLC
0yMDExOTU0NDAwLDE4MTE4OTE1OSwxNjUwMzk0MDg3LC03ODg5
NDQxNTIsMTQ5NDkzNzY1MiwyOTUyNzYxNTAsMTY0NTM1ODA0Ny
wtNzcxMjc2NjY0LDI0MTYwNDI0MCwtMTk1Mjc2MTU1OCw4NTQx
OTM3MTldfQ==
-->