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
`.map` - genetic markers, text
- binary PLINK data
`.bed` - individual identifiers and their genotypes, binary
`.fam` - half of `.ped`, pedigree, sex, phenotype of all individuals, text
`.bim` - an extended `.map`, with allele names in two extra cols, text
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
>input: .bed, individuals - .fam, SNPs - .bim)
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
eyJoaXN0b3J5IjpbMTc4NDM1NTIsMTY0NjM2MDgxNywtNDkwMD
gwMDM3LC0xOTE2MDQ4MTMxLC0xODMyOTExOTE2LC0zMTA5NTc4
NTUsNTE1MjU3NjUxLDQyNjE0MzMzNiwtMTkzODk0Nzg1OSwtMT
gxNzk5OTY1MSwtMTYzNzAyMzMwOSwxNzc0OTQ5MjU0LC0xNjE1
MDY0NTAsLTEzNTk4MDczOTgsMTI0MzQ5MjQ4MiwxMzM1OTY0OT
QsLTE5MjA4MjE3OTEsLTQzODkyODIyNCw2MDc4ODAyNjYsLTUx
MTQwMjM3Ml19
-->