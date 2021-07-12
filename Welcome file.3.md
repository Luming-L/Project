```
# clone the repository
git clone https://github.com/MareesAT/GWA_tutorial.git
# change the directory
cd GWA_tutorial/
```
Install PLink
```
# check hardware (32-bit or 64-bit)
uname -m
```
>x86_64
```
wget http://zzz.bwh.harvard.edu/plink/dist/plink-1.07-x86_64.zip -O ../Tools/plink-1.07-x86_64.zip
# enter the directory
cd ../Tools/
unzip plink-1.07-x86_64.zip
cd plink-1.07-x86_64/
./plink -h
```
## All essential GWAS QC steps along with scripts for data visualization.
```
# unzip tutorial1 zip and move files into the newly created directory
unzip 1_QC_GWAS.zip -d 1_QC_GWAS
# enter the 
cd ../../GWA_tutorial/
```
## Dealing with population stratification, using 1000 genomes as a reference.
## Association analyses of GWAS data.
## Polygenic risk score (PRS) analyses.
The fourth tutorial (4_ PRS.doc) is a MS Word document, and runs independently of the previous 3 tutorials.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzMjQxMDgwOTEsMTQxNTk1NDQ3NiwtMT
IzNTY1MzE2NSwtNTAyMjQ1NzUzLC0xNzcyODQzNDYyLC0xMzA0
MzEwODAzLDE2MzkxMjY0NjAsLTMzMjQ1NTM2M119
-->