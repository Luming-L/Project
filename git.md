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
git config --help
```
`.gitignore` tell git which files  shouldn't  be included in the repository.  
```bash
# Create a .gitignore file
touch .gitignore
echo -e "mypasswordsfile\n*.pdf\n*.c\n*.log" >> .gitignore
# These files could be anywhere in the repository, not just the current directory
echo -e "**/fastq.gz" >> .gitignore
#allows "bowtie2.log" to evade the ignore list: order is important!
# If you want to include a "!" then use an editor to do it
!bowtie2.log
# files that are being ignored
git check-ignore -v *
```
```bash
# check the status of the repository
git status
git st
```

four states of files in the repository:
1.  untracked
2.  tracked
3.  staged for addition
4.  committed to repository
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTYzNDcwNTY0NCwxMzY5MDk4MDA1LDE5MD
k2MTQ2NjEsMjA2MjAwODg2NCwtMTQ5MTQwMTg0MCwyMDMyNjY5
Njc3LDk2Mzg2ODk5MywxMzgzNzAxMjYwLC0xMzY2MTYxNDUxLC
01ODM5ODcwMzIsLTE5MTQwMTAxNzAsMTc2NDIwMzc1LC03MzY0
MjEyMzgsLTEwNzI4MTA5NjIsMjEyMTUzNTAyMiwxMjE0MzQyMz
cxLC0xMzM5ODM3MjU2LC01NTEyMDAwMSwtMjAxMTk1NDQwMCwx
ODExODkxNTldfQ==
-->