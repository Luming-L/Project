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
- System (`/etc/.gitconfig`): at the local system level (all users on this computer), rarely used
- Local (`/localdisk/home/_s0000000_/LectureExercises/.git/config`): at the repository level. If this `.git/config` file was "committed", the settings contained within would impact all users that clone this repository, so be careful what you commit!
```bash
# name and email address
git config --global user.name "LumingLin"
git config --global user.email "s1949868@ed.ac.uk"
# merge.tool
git config --global merge.tool vimdiff
git config --global merge.conflictstyle diff3
git config --global mergetool.prompt false
# preferred Unix text editor
git config --global core.editor "vim -w"
# Specify how git deals with the ends of lines
git config --global core.autocrlf inuput
# Specify an alias
git config --global alias.st status
# list settings
git config --list
```
# .gitignore
If we dont want everything, we first need to tell git which files  shouldn't  be included in the repository  
# Create a .gitignore filetouch .gitignore
```bash
touch .gitignore
echo -e "mypasswordsfile\n*.pdf\n*.c\n*.log" >> .gitignore
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTE3NjM1ODU0Miw5NjM4Njg5OTMsMTM4Mz
cwMTI2MCwtMTM2NjE2MTQ1MSwtNTgzOTg3MDMyLC0xOTE0MDEw
MTcwLDE3NjQyMDM3NSwtNzM2NDIxMjM4LC0xMDcyODEwOTYyLD
IxMjE1MzUwMjIsMTIxNDM0MjM3MSwtMTMzOTgzNzI1NiwtNTUx
MjAwMDEsLTIwMTE5NTQ0MDAsMTgxMTg5MTU5LDE2NTAzOTQwOD
csLTc4ODk0NDE1MiwxNDk0OTM3NjUyLDI5NTI3NjE1MCwxNjQ1
MzU4MDQ3XX0=
-->