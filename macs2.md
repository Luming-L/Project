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
filterdup -i CTCF_ChIP_200K.bed.gz --keep-dup=1 -o CTCF_ChIP_200K_filterdup.bed
filterdup -i CTCF_SE_CTRL_chr22_50k.bed.gz --keep-dup=1 -o CTCF_SE_CTRL_chr22_50k_filterdup.bed
wc -l CTCF_SE_ChIP_chr22_50k_filterdup.bed # 48047 CTCF_SE_ChIP_chr22_50k_filterdup.bed
wc -l CTCF_SE_CTRL_chr22_50k_filterdup.bed # 50783 CTCF_SE_CTRL_chr22_50k_filterdup.bed
```
ChIP: tag size = 100 tags after filtering in alignment file: 199583
CRTL: tag size = 86 tags after filtering in alignment file: 199867
They will be used to scale the ChIP and control signals to the same depth.
# Step 2: Decide the fragment length d
The location of sequenced read may only tell you the end of a DNA fragment that you are interested in (such as TFBS or DNA hypersensitive regions). 
You have to estimate how long this DNA fragment is in order to recover the actual enrichment.
Normally, we only need to do this for ChIP data.
```bash
macs2 predictd -i CTCF_ChIP_200K_filterdup.bed -g hs -m 5 50
```
`-m` mfold parameters. To simulate the default behavior of _macs2 callpeak_, set _-m 5 50_.
Output the fragment length _d_: 254.
# Step 3: Extend ChIP sample to get ChIP coverage track
Generate a pileup track in BEDGRAPH format for ChIP sample. 
For ChIP-Seq data, we extend reads in 5' to 3' direction by the fragment length estimated, which is the default behavior of _pileup_ function.
```bash
macs2 pileup -f BED -i CTCF_ChIP_200K_filterdup.bed -o CTCF_ChIP_200K_filterdup.pileup.bdg --extsize 254
```
The file 'CTCF_ChIP_200K_filterdup.pileup.bdg' contains the fragment pileup signals for ChIP sample.
For DNAse-Seq data or you think the cutting site, that is detected by short read sequencing, is just in the _middle_ of the fragment you are interested in, you need to use _-B_ option to extend the read in both direction. This option will be ignored when the format is set as BAMPE or BEDPE. DEFAULT: False
```bash
sort -k4,4nr CTCF_ChIP_200K_filterdup.pileup.bdg | cut -f 4 | uniq # 0-27
```

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
eyJoaXN0b3J5IjpbLTE0MTYyMTM1NDUsLTc2Nzg1ODQ4Myw4Nz
M5NTcyOTIsLTUxMTI1Mzg0NywyMTI4NzkzMDI1LC03NTM4NTAz
MjUsLTQyMzUxMjM2NywxNzk1NTIwMTg5LC0xMzgzMzY0NDIsLT
E0NjI0MDMzMjMsLTE3NjE5NjAwLDc5MTkxMDY5NywtMjEyOTQ5
NjY5NywtMjA2MDc5OTUzMiwyMTI2NjEyOTM1LDE0ODI5MjQ5MT
csMTIzNjE0MzEzNiwtMTk5NDE2NDcwOCwtMTMzODEzOTgxMSwx
MDkxNTcyODAxXX0=
-->