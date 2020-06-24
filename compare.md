
# Files
[Pratto et al. 2014](https://science.sciencemag.org/content/suppl/2014/11/12/346.6211.1256442.DC1?_ga=2.236340424.892408700.1591381155-1358157743.1587248675)

```bash
# extract A_hotspots_union, i.e.Hotspots found in at least one of the AA1, AA2, AB1 and AB2 individuals
grep -v ^# humanDSBhotspots.txt | awk '$17 ==1 {print}' | wc -l # 40598
grep -v ^# humanDSBhotspots.txt | awk '{FS=OFS="\t";if($17==1){print $1,$2,$3};}' > humanDSBhotspots_AA_AB.txt
wc -l humanDSBhotspots_AA_AB.txt # 40598 humanDSBhotspots_AA_AB.txt

```
## PRDM9 peaks set in 23 types of cancer
```bash
mkdir PRDM9_binding_perCancer
awk '{FS=OFS="\t";{print $1,$4,$5,$NF}}' fimo.gff > acc_fimo_out.bed
```

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
# convert coordinates
~/Tools/liftOver humanDSBhotspots_AA_AB.txt ~/Tools/hg19ToHg38.over.chain humanDSBhotspots_AA_AB.hg38.txt unMapped
```
## bedtools
```bash

bedtools intersect
```
## R
# 
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTc0MTcxMjA0Nyw2MzYwNTIyMjYsMTkzMT
ExNjUyNywtMTQxOTE5ODExNiwtMTYxNDQwNzM1MCwtMTU3OTM4
NDA4MSwxNDQwODIyMzMwLC0xNzQ3NzA1MDczLC04NzYxMDk2Nz
QsLTgwNzg5NTk3OCwyNjc4MzMyODMsLTExODgzOTU0MDYsMTEy
NDE4MjAxNywtOTEzMTAwMTY4LC0xNjMxOTk3OTA4LDE4OTE4Nz
c3NiwtMTU5Mzk0MzYzMSw2MTYzODcwMjcsMTQ3NTEzOTMxMywt
ODAwNTgwMjIxXX0=
-->