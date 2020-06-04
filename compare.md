Visualize the overlap between PRDM9 binding regions in cancer cells and those in testes: This step starts from the PRDM9 binding regions in 404 tumour samples and in testes. A histogram will be plotted to visualize the distribution of overlap fraction between regions in each cancer sample and testes. The x axis of this histogram is 0 to 100% overlap, and the y axis is number of samples. 
# Files
breakpoints in testes-driven data
```bash
grep -v ^#  GSE59836_Peak_data_Supplementary_File_1.txt  |awk '$17 ==1 {print}' 
PRDM9 peaks set in 23 types of cancer
```
# Programmes
## bedtools
## R
# 
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE5ODkyNjYxMTMsMTQ3NTEzOTMxMywtOD
AwNTgwMjIxXX0=
-->