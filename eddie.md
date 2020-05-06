[BPSM eddie](http://129.215.170.35/07_Using_Eddie.html)
[research service-eddie](https://www.wiki.ed.ac.uk/display/ResearchServices/Anaconda)

# Logging In
ssh <YOUR UUN>@eddie.ecdf.ed.ac.uk
# Storage 

# Applications 
#see available modules
module available
#make modules available, by loading them
module load <MODULENAME/MODULEVERSION>
#see a list of currently loaded modules
module list
# Running Jobs 
qsub jobscript.sh
# Interactive Sessions 
# Staging Data from 
# DataStore 
# Monitoring Jobs 

# login:
ssh -X s1949868@eddie.ecdf.ed.ac.uk
Lin&2019
VPN
# space
/home/s1234567/: 2GB
/exports/eddie/scratch/s1234567/: 2TB, **deleted after one month**
group's DataStore

You would:
1.  Copy your dataset to the scratch space
2.  Complete your analysis
3.  Copy your results elsewhere
# information for scheduling the job
#tell Eddie to run our script in its current working directory
#$ cwd
#specify the name of the job
#$ -N Hello
#**overestimate** the time and space needed
#Specify the amount of time the job will require .
#$ -l h_rt=00:01:00
#Specify the amount of memory needed: asking for 1GB RAM (default)
#$ -l h_vmem=1G
#define where you want the outputs and errors to be sent
#$ -o hello.o
#$ -e hello.e

# submit a job

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIxMTYwNDY4NDAsLTEyMzE4ODM0NTYsNz
IyNjIzMTgwLDE1MTgwMzUwNjYsNDQ3NTY5Mzc4LDE3MDAyMDM2
NjgsODU1NDkwMDcsLTE1NTc2NTUwNDMsNTU1MzEzMjExLDMwMz
EyNjg3NiwtMTM3NTM3MTIzNCwtNTM3NzM5MTQ1LC0xMzI3Njg4
MjgyLDcwMjAwMTIzMCwzNjk1NjAwNTBdfQ==
-->