Visualize the overlap between PRDM9 binding regions in cancer cells and those in testes: This step starts from the PRDM9 binding regions in 404 tumour samples and in testes. A histogram will be plotted to visualize the distribution of overlap fraction between regions in each cancer sample and testes. The x axis of this histogram is 0 to 100% overlap, and the y axis is number of samples. 
Per cancer level analysis
For a specific type of cancer, whether the PRDM9 binding regions in peaks are overlapped with those in the breakpoints of testis. How much they overlap?

# Files
## breakpoints in testes-driven data
liftOver
```bash
grep -v ^#  GSE59836_Peak_data_Supplementary_File_1.txt  |awk '$17 ==1 {print}' >GSE59836_Peak_data_Supplementary_File_1.AA_AB_hotspots
 | wc -l # 40598
```
## PRDM9 peaks set in 23 types of cancer

# Programmes
## liftOver
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
eyJoaXN0b3J5IjpbLTE2MzE5OTc5MDgsMTg5MTg3Nzc2LC0xNT
kzOTQzNjMxLDYxNjM4NzAyNywxNDc1MTM5MzEzLC04MDA1ODAy
MjFdfQ==
-->