[BPSM eddie](http://129.215.170.35/07_Using_Eddie.html)
[research service-eddie](https://www.wiki.ed.ac.uk/display/ResearchServices/Anaconda)
[igmm-Eddie3](http://wikilocal.igmm.ed.ac.uk/wiki/index.php/Cluster2-Eddie3)

# Logging In
ssh <YOUR UUN>@eddie.ecdf.ed.ac.uk
# Storage 
- home directory: 2GB backed up
/home/s1949868/
- "scratch" space: 2 TB for temporary files, they will be deleted after 1 month
/exports/eddie/scratch/s1949868/
> How to make use of them:
> 1.  Copy your dataset to the scratch space
> 2.  Complete your analysis
> 3.  Copy your results elsewhere
# Applications 
#see available modules
module available
#make modules available, by loading them
module load <MODULENAME/MODULEVERSION>
#see a list of currently loaded modules
module list
# Running Jobs 

```
qsub jobscript.sh
```
```
#!/bin/sh
#Grid Engine options (lines prefixed with #$)
#$ -N hello              
#$ -cwd                  
#$ -l h_rt=00:05:00 
#$ -l h_vmem=1G
#These options are:
#job name: -N
#use the current working directory: -cwd
#runtime limit of 5 minutes: -l h_rt
#memory limit of 1 Gbyte: -l h_vmem
```
> give the queuing system (Grid Engine) information that it can use when scheduling our job.
> cwd: run our script in its current working directory
> -N hello: give the job a name to identify it
> -l h_rt: Specify the amount of time the job will require (approx).
> -l h_vmem: Specify the amount of memory needed: asking for 1GB RAM (default). If your program definitely needs more, split it into smaller files or request more memory
> -o hello.o/-e hello.e: define where you want the outputs and errors to be sent

#Initialise the environment modules
. /etc/profile.d/modules.sh
 
#Load Python
module load python/3.4.3
 
#Run the program
./hello.py
# Interactive Sessions 
#there are a limited number of nodes that accept interactive login sessions
#allow you to run interactive jobs or graphical applications. #to start an interactive session run:
qlogin
# Staging Data from DataStore 
#A subset of nodes have access to DataStore group spaces via NFS. 
#These nodes are intended for batch _and_ interactive jobs that copy data between DataStore and Eddie. 
#To send a job to these nodes, select the staging queue with the Grid Engine option `-q staging`. 
#For example, to get an interactive session run:
qlogin -q staging
# Monitoring Jobs 
#To query the status of your jobs
qstat
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

# Others 
## Move files
scp [file you want to copy] [destination]
```bash
# Moving a file from bioinfmsc server to your home directory on Eddie 
scp myfavouritefile s1949868@eddie.ecdf.ed.ac.uk:/home/s1949868  
# Moving a file  to  your scratch space on
```

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE0NDgwNjM2ODcsMTY4NzMzMzIwOSwtMT
E5MTA1NTkzOSwxODQwMzI1Nzk1LDE5NzU3Mzc2NjcsLTQ2NTQ2
MjQ1OCwtMTU2ODU4MjE0MSw2NTA4MjMwNjgsMTg0OTU5MDM2Ni
wxNDc1OTA0MTkyLDMyMjIwMjAyMiwxOTY3NTI5ODI2LC0xMDAy
NTI5NzEyLC0xNTA2NzI3ODAyLDM4OTUyNTEwNiwtMTIzMTg4Mz
Q1Niw3MjI2MjMxODAsMTUxODAzNTA2Niw0NDc1NjkzNzgsMTcw
MDIwMzY2OF19
-->