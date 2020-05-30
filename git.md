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
`.gitconfig` can be set at one or more of three different locations:
- Global (`/localdisk/home/_s0000000_/.gitconfig` or ~/.config/git/config): at the user level, the most common use
- System (`/etc/.gitconfig`): rarely used, establishes for the entirety of the local system (all users on this computer).
- Local (`/localdisk/home/_s0000000_/LectureExercises/.git/config`): at the repository level, establishes configuration options that only affect this repository. If this `.git/config` file was "committed", the settings contained within would impact all users that clone this repository, so be careful what you commit!

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
eyJoaXN0b3J5IjpbLTcxODY0MzIxMiwtMTM2NjE2MTQ1MSwtNT
gzOTg3MDMyLC0xOTE0MDEwMTcwLDE3NjQyMDM3NSwtNzM2NDIx
MjM4LC0xMDcyODEwOTYyLDIxMjE1MzUwMjIsMTIxNDM0MjM3MS
wtMTMzOTgzNzI1NiwtNTUxMjAwMDEsLTIwMTE5NTQ0MDAsMTgx
MTg5MTU5LDE2NTAzOTQwODcsLTc4ODk0NDE1MiwxNDk0OTM3Nj
UyLDI5NTI3NjE1MCwxNjQ1MzU4MDQ3LC03NzEyNzY2NjQsMjQx
NjA0MjQwXX0=
-->