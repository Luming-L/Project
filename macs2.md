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

# Step 1: Filter duplicates
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
eyJoaXN0b3J5IjpbLTc3MDE0NzMwMiwxNDg2Mzk3MDUyLC0yMD
g4NzQ2NjEyXX0=
-->