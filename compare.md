Visualize the overlap between PRDM9 binding regions in cancer cells and those in testes: This step starts from the PRDM9 binding regions in 404 tumour samples and in testes. A histogram will be plotted to visualize the distribution of overlap fraction between regions in each cancer sample and testes. The x axis of this histogram is 0 to 100% overlap, and the y axis is number of samples. 
Per cancer level analysis
For a specific type of cancer, whether the PRDM9 binding regions in peaks are overlapped with those in the breakpoints of testis. How much they overlap?

# Files
[Pratto et al. 2014](https://science.sciencemag.org/content/suppl/2014/11/12/346.6211.1256442.DC1?_ga=2.236340424.892408700.1591381155-1358157743.1587248675)
## breakpoints in testes-driven data

liftOver
```bash
grep -v ^# humanDSBhotspots.txt | awk '$17 ==1 {print}' > humanDSBhotspots_AA_AB.txt
grep -v ^#  GSE59836_Peak_data_Supplementary_File_1.txt  |awk '$17 ==1 {print}' >GSE59836_Peak_data_Supplementary_File_1.AA_AB_hotspots
 | wc -l # 40598
```
## PRDM9 peaks set in 23 types of cancer

# Programmes
## liftOver
convert coordinates from one assembly to another.
```bash
# download liftOver
wget http://hgdownload.cse.ucsc.edu/admin/exe/linux.x86_64/c
# make it executable
chmod 700 liftOver
# download map.chain file that has the old genome as the target and the new genome as the query. This file is required as input to the liftOver utility.
wget http://hgdownload.cse.ucsc.edu/goldenpath/hg19/liftOver/hg19ToHg38.over.chain.gz
usage:
liftOver oldFile map.chain newFile unMapped


```
http://hgdownload.cse.ucsc.edu/goldenpath/hg19/liftOver/
hg19ToHg38.over.chain.gz
```bash
liftOver oldFile map.chain newFile unMapped
```
## bedtools
```bash
bedtools intersect
```

## R
# 
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTY1MjIzOTM0NiwtODA3ODk1OTc4LDI2Nz
gzMzI4MywtMTE4ODM5NTQwNiwxMTI0MTgyMDE3LC05MTMxMDAx
NjgsLTE2MzE5OTc5MDgsMTg5MTg3Nzc2LC0xNTkzOTQzNjMxLD
YxNjM4NzAyNywxNDc1MTM5MzEzLC04MDA1ODAyMjFdfQ==
-->