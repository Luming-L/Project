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

```
**awk** '{FS="_"; print NF;}' file1
## overlap
## merge peaks in different replicates
# Motif finding

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIxMTc4OTYzMSw1Nzk1OTkxNzUsLTE5Mj
U3OTA1NiwtNzY0NjYyNzAxLDI4ODU5OTI5MCwxNTg3NzM5MzUy
LC0yMDUyMjcwMzEyLDE0NTQwOTM2MzcsLTE1MTkzODI0MTYsLT
M0MjE2MzcxLC0xOTUxMDQzMDI3XX0=
-->