Visualize the overlap between PRDM9 binding regions in cancer cells and those in testes: This step starts from the PRDM9 binding regions in 404 tumour samples and in testes. A histogram will be plotted to visualize the distribution of overlap fraction between regions in each cancer sample and testes. The x axis of this histogram is 0 to 100% overlap, and the y axis is number of samples. 
Per cancer level analysis
For a specific type of cancer, whether the PRDM9 binding regions in peaks are overlapped with those in the breakpoints of testis. How much they overlap?

# Files
[Pratto et al. 2014](https://science.sciencemag.org/content/suppl/2014/11/12/346.6211.1256442.DC1?_ga=2.236340424.892408700.1591381155-1358157743.1587248675)
## breakpoints in testes-driven data
```bash
# extract A_hotspots_union, i.e.Hotspots found in at least one of the AA1, AA2, AB1 and AB2 individuals
grep -v ^# humanDSBhotspots.txt | awk '$17 ==1 {print}' | wc -l # 40598
grep -v ^# humanDSBhotspots.txt | awk '{FS=OFS="\t";if($17==1){print $1,$2,$3};}' > humanDSBhotspots_AA_AB.txt
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
gzip -d hg19ToHg38.over.chain.gz
usage:
liftOver oldFile map.chain newFile unMapped
 ~/Tools/liftOver humanDSBhotspots_AA_AB.txt ~/Tools/hg19ToHg38.over.chain humanDSBhotspots_AA_AB.hg38.txt unMapped
Reading liftover chains
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
eyJoaXN0b3J5IjpbLTU2Mzc1NTg5MSwxNDQwODIyMzMwLC0xNz
Q3NzA1MDczLC04NzYxMDk2NzQsLTgwNzg5NTk3OCwyNjc4MzMy
ODMsLTExODgzOTU0MDYsMTEyNDE4MjAxNywtOTEzMTAwMTY4LC
0xNjMxOTk3OTA4LDE4OTE4Nzc3NiwtMTU5Mzk0MzYzMSw2MTYz
ODcwMjcsMTQ3NTEzOTMxMywtODAwNTgwMjIxXX0=
-->