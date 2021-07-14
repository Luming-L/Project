```
# clone the repository
git clone https://github.com/MareesAT/GWA_tutorial.git
# change the directory
cd GWA_tutorial/
```
## PLINK Installation
Check hardware
```
# 32-bit or 64-bit
uname -m
```
>x86_64

Install PLINK 1.07
```bash
# download
wget http://zzz.bwh.harvard.edu/plink/dist/plink-1.07-x86_64.zip -O ../Tools/plink-1.07-x86_64.zip
# enter the directory
cd ../Tools/
# unzip
unzip plink-1.07-x86_64.zip
# enter the directory
cd plink-1.07-x86_64/
# run
./plink -h
```
>Segmentation fault (core dumped)
>use PLINK 2.00 instead

Install PLINK 2.00 alpha
```bash
# download
wget https://s3.amazonaws.com/plink2-assets/alpha2/plink2_linux_x86_64.zip
# unzip
unzip plink2_linux_x86_64.zip
# run
./plink2 --help
```
## Data
HapMap
hapmap3_r3_b36_fwd.consensus.qc
a binary phenotype simulated
HapMap_3_r3_1
http://hapmap.ncbi.nlm.nih.gov/downloads/genotypes/2010-05_phaseIII/plink_format/ 
https://www.ncbi.nlm.nih.gov/variation/tools/1000genomes/
## QC
Seven steps:

 - Missingness of SNPs and individuals
 - Sex discrepancy
 - Minor allele frequency (MAF)
 - Hardy–Weinberg equilibrium (HWE)
 - Heterozygosity
 - Relatedness
 - Population stratification
```
# unzip 1_QC_GWAS
unzip 1_QC_GWAS.zip 
# enter its directory
cd 1_QC_GWAS
```

## Population stratification
## Association analyses
## Polygenic risk score (PRS) analyses.
The fourth tutorial (4_ PRS.doc) is a MS Word document, and runs independently of the previous 3 tutorials.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTQ3MjYzNjIwMiwtNDM4OTI4MjI0LDYwNz
g4MDI2NiwtNTExNDAyMzcyLC00MzkxMzk4NzUsLTE2NTkxNzQz
MjksMzMxOTM3NTEsLTUyMTAyNjY4NCwxMzk1NDA5MDIzLC01MD
kwNTUwNzcsLTE2ODQ1MzI5NTUsLTU1ODg3ODgwOCwtMzczNDA3
NDcsMjA3MDIyNTM4OCwtMTQxMDE2NDIyNCwtNTc4OTA4MTk1XX
0=
-->