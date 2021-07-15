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
The seven QC steps should be conducted before genetic association analysis.
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
### Step 1: Missingness of SNPs and individuals
- Remove SNPs that are missed in most individuals, and individuals that miss most SNPs.
- first 0.2 (>20%) then 0.02 (>2%) 
- first remove SNPs then remove individuals
```bash
plink2 --bfile HapMap_3_r3_1 --missing
```
>INPUT: pedigree, sex, phenotype and genotypes of individuals, and physical positions of SNPs. user binary version (`.bed`, `.fam`, `.bim`)
>PROCESS: calculate sample missingness rates and allele frequencies, and generate reports.
>OUTPUT: 
Sample missing data report (`.smiss`)
>- PHENO1: Missing phenotype, Y means none
>- MISSING_CT: Number of missing SNPs
>- OBS_CT: Denominator
>- F_MISS: Proportion of missing SNPs 
>
>Variant missing data report (`.vmiss`). 
>- MISSING_CT:  Number of individuals missing this SNP
>- OBS_CT: Denominator
>- F_MISS: Proportion of sample missing for this SNP
>
>AMOUNT: 4G RAM and 8 threads. 
```R
# launch R
R
# read data into R 
indmiss<-read.table(file="plink2.smiss", header=TRUE)
snpmiss<-read.table(file="plink2.vmiss", header=TRUE)
# plot
png("histsmiss.png") #indicates png format and gives title to file
hist(indmiss[,6],main="Histogram individual missingness") #selects column 6, names header of file
png("histvmiss.png") 
hist(snpmiss[,5],main="Histogram SNP missingness")  
dev.off() # shuts down the current device
```
>INPUT: `.smiss` and `.vmiss`
>PROCESS: plot histogram
>OUTPUT: 
Results:
165 samples (85 females, 80 males; 112 founders)
1457897 variants
1 binary phenotype (56 cases, 56 controls)

### Step 2: Sex discrepancy
### Step 3: Minor allele frequency (MAF)
### Step 4: Hardy–Weinberg equilibrium (HWE)
### Step 5: Heterozygosity
### Step 6: Relatedness
### Step 7: Population stratification

## Population stratification
## Association analyses
## Polygenic risk score (PRS) analyses.
The fourth tutorial (4_ PRS.doc) is a MS Word document, and runs independently of the previous 3 tutorials.
## Questions
what are genotypes, genetic markers, SNPs, variants, alleles, allele names?
<!--stackedit_data:
eyJoaXN0b3J5IjpbNDE0NDc1MzIyLC0xNTMzMDMyMDk5LDE0OD
Q0MTg2NzgsLTI2NDc4MjA4MSwxNjMyNDA5MDEwLDcyMjk2MjU2
LDEyMjUxOTI4NDQsMTgxODU1NTUwOCwxODkzMDg5MzU2LDE2OT
YzOTY1OSwtOTYwMzYwMzQ0LDE2NDYzNjA4MTcsLTQ5MDA4MDAz
NywtMTkxNjA0ODEzMSwtMTgzMjkxMTkxNiwtMzEwOTU3ODU1LD
UxNTI1NzY1MSw0MjYxNDMzMzYsLTE5Mzg5NDc4NTksLTE4MTc5
OTk2NTFdfQ==
-->