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
sample set ()
for sample in ACC_samples
Bedrolls intersect -u -a ACC -b ACC_sample_peaks -r 0.8
```
```bash
sort -k1,1 -k2n ACC_peakCalls.txt | grep "chr" | awk '{FS=OFS="\t"; {print $1,$2,$3,$4}}' > ACC_peakCalls.pure.txt
awk '{FS=OFS="\t"; {print $1,$2,$3}}' ACCx_025FE5F8_885E_433D_9018_7AE322A92285_X034_S09_L133_B1_T1_PMRG.insertions.peaks001.bed | grep "chr"> ACCx_025FE5F8_885E_433D_9018_7AE322A92285_X034_S09_L133_B1_T1_PMRG.insertions.peaks001.pure.bed


bedtools intersect -wa -a ACC_peakCalls.pure.txt -b ACCx_025FE5F8_885E_433D_9018_7AE322A92285_X034_S09_L133_B1_T1_PMRG.insertions.peaks001.pure.bed -sorted -filenames -f 1.0 

bedtools intersect -wa -a ACC_peakCalls.pure.txt -b ACCx_025FE5F8_885E_433D_9018_7AE322A92285_X034_S09_L133_B1_T1_PMRG.insertions.peaks001.pure.bed -sorted -filenames -c -f 1.0
```
`-f`： Minimum overlap required as **a fraction of A**. `-f 1.0` means 100% of the query record is overlapped by a database record
`-c`: For each entry in A, report the number of hits in B while restricting to -f.
`-sorted`: For very large B files, invoke a “sweeping” algorithm that requires position-sorted (e.g.,  `sort  -k1,1  -k2,2n`  for BED files) input. When using -sorted, memory usage remains low even for very large files.
## overlap
## merge peaks in different replicates
# Motif finding

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTM4NjM0OTEwOSwtMTE1MjU3NTk2NywtNj
cyMDYwNjg4LC0xMDc0Mzc4NDYsLTE4NDczMjc5MzksMzUzMjE5
LC0yMTM3NzU5Nzk1LC0yMTE3ODk2MzEsNTc5NTk5MTc1LC0xOT
I1NzkwNTYsLTc2NDY2MjcwMSwyODg1OTkyOTAsMTU4NzczOTM1
MiwtMjA1MjI3MDMxMiwxNDU0MDkzNjM3LC0xNTE5MzgyNDE2LC
0zNDIxNjM3MSwtMTk1MTA0MzAyN119
-->