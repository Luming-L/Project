# Make PeakSet for each sample
## input files
**Cancer type-specific peak calls (23)**
Each text file represents all merged peak calls from each cancer type. 
**Recalled peaks in each technical replicate (796)**
```bash
# download cancer type-specific PeakCalls
wget https://api.gdc.cancer.gov/data/71ccfc55-b428-4a04-bb5a-227f7f3bf91c
unzip 71ccfc55-b428-4a04-bb5a-227f7f3bf91c
mkdir TCGA-ATAC_Cancer_Type-specific_PeakCalls
mv *.txt TCGA-ATAC_Cancer_Type-specific_PeakCalls
```
```bash
Bedrolls intersect -u -a  -b sample_peaks -r 0.8
```
## overlap
## merge peaks in different replicates
# Motif finding

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE4NDI5MzE1ODcsMTU4NzczOTM1MiwtMj
A1MjI3MDMxMiwxNDU0MDkzNjM3LC0xNTE5MzgyNDE2LC0zNDIx
NjM3MSwtMTk1MTA0MzAyN119
-->