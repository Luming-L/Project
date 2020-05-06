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
#submit work to the cluster as batch jobs
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
eyJoaXN0b3J5IjpbMTcwMzA4MzU4OCwtMTIzMTg4MzQ1Niw3Mj
I2MjMxODAsMTUxODAzNTA2Niw0NDc1NjkzNzgsMTcwMDIwMzY2
OCw4NTU0OTAwNywtMTU1NzY1NTA0Myw1NTUzMTMyMTEsMzAzMT
I2ODc2LC0xMzc1MzcxMjM0LC01Mzc3MzkxNDUsLTEzMjc2ODgy
ODIsNzAyMDAxMjMwLDM2OTU2MDA1MF19
-->