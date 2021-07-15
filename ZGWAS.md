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
Set PATH
```
PATH=$PATH:/home/luminglin/Tools
```
## Data
HapMap
hapmap3_r3_b36_fwd.consensus.qc
a binary phenotype simulated
HapMap_3_r3_1
http://hapmap.ncbi.nlm.nih.gov/downloads/genotypes/2010-05_phaseIII/plink_format/ 
https://www.ncbi.nlm.nih.gov/variation/tools/1000genomes/
## Data Format
- text PLINK data
`.ped` - pedigree, sex, phenotype and genotypes of all individuals, text
`.map` - physical positions of SNPs, text
- binary PLINK data
`.bed` - individual identifiers and their genotypes, binary
`.fam` - half of `.ped`, pedigree, sex, phenotype of all individuals, text
`.bim` - an extended `.map`, with allele names in two extra cols, text
>pedigree means family relationship with other participants in this study
>`.bed` is a binary version of `.ped`
>`--make-bed` can transform `.ped` to `.bed`, and generated `.fam` and `.bim`. `.bed` connects `.fam` to `.bim`

![image](https://onlinelibrary.wiley.com/cms/asset/6e29248d-8bf5-4fc4-b707-339a5312526a/mpr1608-fig-0001-m.png)
## QC
Seven steps
 - Missingness of SNPs and individuals
 - Sex discrepancy
 - Minor allele frequency (MAF)
 - Hardy–Weinberg equilibrium (HWE)
 - Heterozygosity
 - Relatedness
 - Population stratification

Get files
```
# unzip 1_QC_GWAS
unzip 1_QC_GWAS.zip 
# enter its directory
cd 1_QC_GWAS
```
Step 1: Missingness of SNPs and individuals
```
plink2 --bfile HapMap_3_r3_1 --missing
```
>input: pedigree, sex, phenotype and genotypes of individuals, and physical positions of SNPs. user binary version (`.bed`, `.fam`, `.bim`)
>process: 
>output:
>8062 MiB RAM detected; reserving 4031 MiB for main workspace.
Using up to 8 compute threads.
165 samples (85 females, 80 males; 112 founders) loaded from HapMap_3_r3_1.fam.
1457897 variants loaded from HapMap_3_r3_1.bim.
1 binary phenotype loaded (56 cases, 56 controls).
Calculating sample missingness rates... done.
Calculating allele frequencies... done.
--missing: Sample missing data report written to plink2.smiss .
--missing: Variant missing data report written to plink2.vmiss .
End time: Thu Jul 15 09:09:19 2021

## Population stratification
## Association analyses
## Polygenic risk score (PRS) analyses.
The fourth tutorial (4_ PRS.doc) is a MS Word document, and runs independently of the previous 3 tutorials.
## Questions
what are genotypes, genetic markers, SNPs, variants, alleles, allele names?
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE2NDM4NTYyMjEsLTk2MDM2MDM0NCwxNj
Q2MzYwODE3LC00OTAwODAwMzcsLTE5MTYwNDgxMzEsLTE4MzI5
MTE5MTYsLTMxMDk1Nzg1NSw1MTUyNTc2NTEsNDI2MTQzMzM2LC
0xOTM4OTQ3ODU5LC0xODE3OTk5NjUxLC0xNjM3MDIzMzA5LDE3
NzQ5NDkyNTQsLTE2MTUwNjQ1MCwtMTM1OTgwNzM5OCwxMjQzND
kyNDgyLDEzMzU5NjQ5NCwtMTkyMDgyMTc5MSwtNDM4OTI4MjI0
LDYwNzg4MDI2Nl19
-->