A version control system to record what was done and when, by who.
```bash
git add Results/
git commit -m "add selectPRDM9BoundPeaks.sh to MotifFind"
git push -u MScProject master

git clone https://github.com/Luming-L/MScProject
```

# term
**commit:** record the changes that are made at each step (each one becomes a version with associated information/metadata) when we want it to
**repository: ** complete history of commits/metadata for a particular project
**branching: ** go back to previous versions and modify in a different direction

# GitHub
```bash
# CREATE a repository in your account on GitHub 
# user: Luming-L
curl -u Luming-L https://api.github.com/user/repos -d '{"name":"MscProject"}'

# Tell git our repository on GitHub (MscProject.git), we call it MscProject 
git remote add MScProject https://github.com/Luming-L/MScProject.git

# # push our repository off to our repository on GitHub
git push -u MscProject master
```

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
# Configure
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
# Work
four states of files in the repository:
1.  untracked
2.  tracked
3.  staged for addition
4.  committed to repository
 ```mermaid
graph LR
A(working directory) -- git add --> B(staging area)
B  -- git commit --> C(repository)
```
```bash
#stage the file
git add motif_file.txt
# commit what is staged
# AND give it a comment/message
git commit -m "First file added"
# stage the .gitignore file, for if/when we share the repository
git add .gitignore
# remove a file from the staging area
# Unstaging

# stage 
git add GroupByPRDM9Expression/
git commit -m "compare two groups defined by PRDM9 expression"
```bash
# log
git log
git log --oneline
```

# Zip
```bash
#Make a zip file, move the file into the zip
zip -m Assignment.zip motif_file.txt
```

```bash
git remote add origin https://github.com/Luming-L/MScProject.git
```

# Reference
[https://stackoverflow.com/questions/12258399/how-do-i-create-a-folder-in-a-github-repository](https://stackoverflow.com/questions/12258399/how-do-i-create-a-folder-in-a-github-repository)
[https://stackoverflow.com/questions/28429819/rejected-master-master-fetch-first](https://stackoverflow.com/questions/28429819/rejected-master-master-fetch-first)

<!--stackedit_data:
eyJoaXN0b3J5IjpbNzU5Njg5MDksLTE5MDcwNzM2ODMsLTczOT
kwMTA0MywtMTc1MzkxODU0MCwtMTM0Mzg1MzQzNCwzNjI2NTgw
OTcsLTE0MzUwMDQ5NTksLTIxMTcyNzU5NzksMTI2Njg5MTAzMS
wtMTY0NjQ5NDA4NiwtNjgyNTY5MDk0LDYyODkzOTgyMywtMTkx
MzI2ODIsLTExNTQ2MzIwOTQsMTMwMjg3MDg3MCwxNTcyMDU2NT
g4LDk2MTk2ODMxNSwxMTMzNzg0MjM4LDIwNTMzMjMzOTQsLTYz
NDcwNTY0NF19
-->