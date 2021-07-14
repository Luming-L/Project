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
## Data
HapMap
hapmap3_r3_b36_fwd.consensus.qc
a binary phenotype simulated
## QC
7 steps:
1: Missingness of SNPs and individuals
2: Sex discrepancy
3: Minor allele frequency (MAF)
4: Hardy–Weinberg equilibrium (HWE)
5: Heterozygosity
6: Relatedness
7: Population stratification
```
# unzip 1_QC_GWAS
unzip 1_QC_GWAS.zip 
# enter its directory
cd 1_QC_GWAS
```
Missingness of SNPs and individuals
```
# Investigate missingness per individual and per SNP and make histograms.
plink --bfile HapMap_3_r3_1 --missing
```
Sex discrepancy
Minor allele frequency (MAF)
Hardy–Weinberg equilibrium (HWE)
## Population stratification
## Association analyses
## Polygenic risk score (PRS) analyses.
The fourth tutorial (4_ PRS.doc) is a MS Word document, and runs independently of the previous 3 tutorials.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTM5NTQwOTAyMywtNTA5MDU1MDc3LC0xNj
g0NTMyOTU1LC01NTg4Nzg4MDgsLTM3MzQwNzQ3LDIwNzAyMjUz
ODgsLTE0MTAxNjQyMjQsLTU3ODkwODE5NV19
-->