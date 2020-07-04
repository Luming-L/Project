

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
eyJoaXN0b3J5IjpbLTg0ODIwODI3MywtNzQxNzEyMDQ3LDYzNj
A1MjIyNiwxOTMxMTE2NTI3LC0xNDE5MTk4MTE2LC0xNjE0NDA3
MzUwLC0xNTc5Mzg0MDgxLDE0NDA4MjIzMzAsLTE3NDc3MDUwNz
MsLTg3NjEwOTY3NCwtODA3ODk1OTc4LDI2NzgzMzI4MywtMTE4
ODM5NTQwNiwxMTI0MTgyMDE3LC05MTMxMDAxNjgsLTE2MzE5OT
c5MDgsMTg5MTg3Nzc2LC0xNTkzOTQzNjMxLDYxNjM4NzAyNywx
NDc1MTM5MzEzXX0=
-->