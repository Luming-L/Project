[Identifying ChIP-seq enrichment using MACS](https://www.nature.com/articles/nprot.2012.101)
how macs2 call peaks
two important steps: adjust read position, calculate peak enrichment

### calculate local lambda without control
The local lambda is the maximum of the averages of tags for 1/5/10 kb regions and a whole genome background. If there is no control data, the ChIP data will be used instead, where the 1kb region is not considered.
### the principle of tweaking the region that lambda generates from
not affect good peak which has low FDR, big fold- enrichment, and high '-10*log(10,pvalue)', if the parameter is reasonable.
[](https://groups.google.com/forum/#!msg/macs-announcement/JkufzGpUNRk/kUx0z2M2b_cJ)
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
# Step 4: Build local bias track from control
By default, MACS2 _callpeak_ function computes the local bias by taking the maximum bias from 
- surrounding 1kb (set by --slocal)
- surrounding 10kb (set by --llocal)
- the size of fragment length _d_ (predicted as what you got from _predictd_)
- the whole genome background
## The d background
extend the control read to both sides (-B option) using _pileup_ function.
The idea is that the cutting site from control sample contains the noise representing a region surrounding it. To do this, take half of _d_ you got from _predictd_, 127 (1/2 of 254) for our example, then:
```bash
pileup -f BED -i CTCF_Control_200K_filterdup.bed -B --extsize 127 -o d_bg.bdg
sort -k4,4nr d_bg.bdg | cut -f 4 | uniq # 0-74
```
## The slocal background
```bash
 macs2 pileup -i CTCF_Control_200K_filterdup.bed -B --extsize 500 -o 1k_bg.bdg
 sort -k4,4nr 1k_bg.bdg | cut -f 4 | uniq #0-240
 macs2 bdgopt -i 1k_bg.bdg -m multiply -p 0.254 -o 1k_bg_norm.bdg
 sort -k4,4nr 1k_bg_norm.bdg | cut -f 4 | uniq #0- 60.96
```
## The llocal background
```bash
pileup -f BED -i CTCF_Control_200K_filterdup.bed -B --extsize 5000 -o 10k_bg.bdg
sort -k4,4nr 10k_bg.bdg | cut -f 4 | uniq | head # 0-1191
macs2 bdgopt -i 10k_bg.bdg -m multiply -p 0.0254 -o 10k_bg_norm.bdg
sort -k4,4nr 10k_bg_norm.bdg | cut -f 4 | uniq | head # 0-30.25140
```
## The genome background
_the_number_of_control_reads*fragment_length/genome_size_: 199867*254/2700000000 ~= .0188023.
## Combine and generate the maximum background noise
Step 5: Scale the ChIP and control to the same sequencing depth
Step 6: Compare ChIP and local lambda to get the scores in pvalue or qvalue
Step 7: Call peaks on score track using a cutoff
Summary
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTg2ODgzNzUzOCwtMTUwOTI3NzkwMCw3Mz
U0ODc4ODIsLTk3MDkwNDA1MSwtMTU3Njc5MjgwNywtNTU3ODQ2
Njc3LC02MDA2Nzg0NTAsMTM5MTc4NTg3MywtODk4OTMwNTkzLD
EyNDUwOTI1NzEsMTQzOTIzMDk4MCwyMjIyNjA5MjgsLTE0MTYy
MTM1NDUsLTc2Nzg1ODQ4Myw4NzM5NTcyOTIsLTUxMTI1Mzg0Ny
wyMTI4NzkzMDI1LC03NTM4NTAzMjUsLTQyMzUxMjM2NywxNzk1
NTIwMTg5XX0=
-->