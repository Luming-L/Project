[BPSM eddie](http://129.215.170.35/07_Using_Eddie.html)
[research service-eddie](https://www.wiki.ed.ac.uk/display/ResearchServices/Anaconda)

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

# **

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTQ1NTU0NTEyOCwxNzAwMjAzNjY4LDg1NT
Q5MDA3LC0xNTU3NjU1MDQzLDU1NTMxMzIxMSwzMDMxMjY4NzYs
LTEzNzUzNzEyMzQsLTUzNzczOTE0NSwtMTMyNzY4ODI4Miw3MD
IwMDEyMzAsMzY5NTYwMDUwXX0=
-->