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
for cancer in 23 cancer
for sample in ACC_samples
Bedrolls intersect -u -a ACC -b ACC_sample_peaks -r 0.8
```
```bash
grep "chr" ACC_peakCalls.txt > ACC_peakCalls.headerNo.txt
```

## overlap
## merge peaks in different replicates
# Motif finding

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTc2NDY2MjcwMSwyODg1OTkyOTAsMTU4Nz
czOTM1MiwtMjA1MjI3MDMxMiwxNDU0MDkzNjM3LC0xNTE5Mzgy
NDE2LC0zNDIxNjM3MSwtMTk1MTA0MzAyN119
-->