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
sort -k1,1 -k2n ACC_peakCalls.txt | grep "chr" | awk '{FS=OFS="\t"; {print $1,$2,$3,$4}}' > ACC_peakCalls.pure.txt
awk '{FS=OFS="\t"; {print $1,$2,$3}}' ACCx_025FE5F8_885E_433D_9018_7AE322A92285_X034_S09_L133_B1_T1_PMRG.insertions.peaks001.bed | grep "chr"> ACCx_025FE5F8_885E_433D_9018_7AE322A92285_X034_S09_L133_B1_T1_PMRG.insertions.peaks001.pure.bed
bedtools intersect -wa -wb -a ACC_peakCalls.pure.txt -b ACCx_025FE5F8_885E_433D_9018_7AE322A92285_X034_S09_L133_B1_T1_PMRG.insertions.peaks001.pure.bed -sorted -filenames -f 1.0 | wc -l
bedtools intersect -a A.bed -b B.bed C.bed -c
bedtools intersect -wa -a ACC_peakCalls.pure.txt -b ACCx_025FE5F8_885E_433D_9018_7AE322A92285_X034_S09_L133_B1_T1_PMRG.insertions.peaks001.pure.bed -sorted -filenames -c -f 1.0
```
**awk** '{FS="_"; print NF;}' file1
## overlap
## merge peaks in different replicates
# Motif finding

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE4MzEwNDY5MTQsLTIxMzc3NTk3OTUsLT
IxMTc4OTYzMSw1Nzk1OTkxNzUsLTE5MjU3OTA1NiwtNzY0NjYy
NzAxLDI4ODU5OTI5MCwxNTg3NzM5MzUyLC0yMDUyMjcwMzEyLD
E0NTQwOTM2MzcsLTE1MTkzODI0MTYsLTM0MjE2MzcxLC0xOTUx
MDQzMDI3XX0=
-->