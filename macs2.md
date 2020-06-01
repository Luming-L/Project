Example for regular peak calling: 
```bash
macs2 callpeak -t ChIP.bam -c Control.bam -f BED -g hs -n test -B -q 0.01
```
`-f`/`--format FORMAT`
MACS2 can detect and read gzipped file. For example,  `.bed.gz`  file can be directly used without being uncompressed with  `--format BED`.
 `-n`/`--name`
The name string of the experiment. MACS will use this string NAME to create output files like  `NAME_peaks.xls`,  `NAME_negative_peaks.xls`,  `NAME_peaks.bed`  ,  `NAME_summits.bed`,  `NAME_model.r`  and so on. 
`-B`/`--bdg`
If this flag is on, MACS will store the fragment pileup, control lambda in bedGraph files. The bedGraph files will be stored in the current directory named  `NAME_treat_pileup.bdg`  for treatment data,  `NAME_control_lambda.bdg`  for local lambda values from control.
`-q`/`--qvalue`
The q-value (minimum FDR) cutoff to call significant regions. Default is 0.05. For broad marks, you can try 0.05 as the cutoff. Q-values are calculated from p-values using the Benjamini-Hochberg procedure.

# Step 1: Filter duplicates
Remove the redundant reads at each genomic loci in Control and ChIP data.
By default, the maximum number of allowed duplicated reads is 1, or _--keep-dup=1_ for _callpeak_.
```bash
macs2 filterdup -i CTCF_SE_ChIP_chr22_50k.bed.gz --keep-dup=1 -o CTCF_SE_ChIP_chr22_50k_filterdup.bed
filterdup -i CTCF_SE_CTRL_chr22_50k.bed.gz --keep-dup=1 -o CTCF_SE_CTRL_chr22_50k_filterdup.bed
wc -l CTCF_SE_ChIP_chr22_50k_filterdup.bed # 48047 CTCF_SE_ChIP_chr22_50k_filterdup.bed
wc -l CTCF_SE_CTRL_chr22_50k_filterdup.bed # 50783 CTCF_SE_CTRL_chr22_50k_filterdup.bed
```
ChIP: tag size = 101 tags after filtering in alignment file: 48047
CRTL: tag size = 101 tags after filtering in alignment file: 50783
They will be used to scale the ChIP and control signals to the same depth.
# Step 2: Decide the fragment length d

# Step 3: Extend ChIP sample to get ChIP coverage track
Step 4: Build local bias track from control
The d background
The slocal background
The llocal background
The genome background
Combine and generate the maximum background noise
Step 5: Scale the ChIP and control to the same sequencing depth
Step 6: Compare ChIP and local lambda to get the scores in pvalue or qvalue
Step 7: Call peaks on score track using a cutoff
Summary
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjEyNjYxMjkzNSwxNDgyOTI0OTE3LDEyMz
YxNDMxMzYsLTE5OTQxNjQ3MDgsLTEzMzgxMzk4MTEsMTA5MTU3
MjgwMSwxNDg2Mzk3MDUyLC0yMDg4NzQ2NjEyXX0=
-->