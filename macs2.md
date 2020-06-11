[Identifying ChIP-seq enrichment using MACS](https://www.nature.com/articles/nprot.2012.101)
[https://www.biorxiv.org/content/10.1101/496521v1.full.pdf](https://www.biorxiv.org/content/10.1101/496521v1.full.pdf)
[atac-seq peak-calling](https://galaxyproject.github.io/training-material/topics/epigenetics/tutorials/atac-seq/tutorial.html#peak-calling)
[MACS](https://github.com/macs3-project/MACS)
[MACS2 subcommand](https://github.com/macs3-project/MACS/wiki/Advanced%3A-Call-peaks-using-MACS2-subcommands#Step_4_Build_local_bias_track_from_control)

calculate different lambda 
select lamda
poisson distribution
merge regions

### calculate local lambda without control
The local lambda is the maximum of the averages of tags for 1/5/10 kb regions and a whole genome background. If there is no control data, the ChIP data will be used instead, where the 1kb region is not considered.
### the principle of change the range that the lambda generates from
not affect good peak which has low FDR, big fold- enrichment, and high '-10*log(10,pvalue)', if the parameter is reasonable.
> [macs group](https://groups.google.com/forum/#!msg/macs-announcement/JkufzGpUNRk/kUx0z2M2b_cJ)

## bdgpeakcall
simple peak calling tool 
check the 4th column in bedGraph file and call the regions above a given cutoff.
The 5th column score = 10 * score in the summit from bedGraph.

> [issues379](https://github.com/macs3-project/MACS/issues/379)


> [bdgpeakcall_cmd.py](https://github.com/macs3-project/MACS/blob/master/MACS2/bdgpeakcall_cmd.py)



ATAC-seq Counts Matrices normalized
- -2 - 8 
- 
ATAC-seq Counts Matrices raw
- 

BigWig Files for All Samples
- per sample level (796 files)
- 100bp bin 
- normalized read counts
- call by signal, gap, length

```bash
### Filter duplicates
macs2 filterdup -i CTCF_ChIP_200K.bed.gz --keep-dup=1 -o CTCF_ChIP_200K_filterdup.bed
macs2 filterdup -i CTCF_Control_200K.bed.gz --keep-dup=1 -o CTCF_Control_200K_filterdup.bed
### Decide the fragment length  _d_
macs2 predictd -i CTCF_ChIP_200K_filterdup.bed -g hs -m 5 50
### Extend ChIP sample to get ChIP coverage track
macs2 pileup -i CTCF_ChIP_200K_filterdup.bed -o CTCF_ChIP_200K_filterdup.pileup.bdg --extsize 254
### Build local bias track from control
#### The  _d_  background
macs2 pileup -i CTCF_Control_200K_filterdup.bed -B --extsize 127 -o d_bg.bdg
#### The slocal background
macs2 pileup -i CTCF_Control_200K_filterdup.bed -B --extsize 500 -o 1k_bg.bdg
macs2 bdgopt -i 1k_bg.bdg -m multiply -p 0.254 -o 1k_bg_norm.bdg
#### The llocal background
macs2 pileup -i CTCF_Control_200K_filterdup.bed -B --extsize 5000 -o 10k_bg.bdg
macs2 bdgopt -i 10k_bg.bdg -m multiply -p 0.0254 -o 10k_bg_norm.bdg
#### Combine and generate the maximum background noise
macs2 bdgcmp -m max -t 1k_bg_norm.bdg -c 10k_bg_norm.bdg -o 1k_10k_bg_norm.bdg
macs2 bdgcmp -m max -t 1k_10k_bg_norm.bdg -c d_bg.bdg -o d_1k_10k_bg_norm.bdg
macs2 bdgopt -i d_1k_10k_bg_norm.bdg -m max -p .0188023 -o local_bias_raw.bdg
### Scale the ChIP and control to the same sequencing depth
macs2 bdgopt -i local_bias_raw.bdg -m multiply -p .99858 -o local_lambda.bdg
### Compare ChIP and local lambda to get the scores in pvalue or qvalue
macs2 bdgcmp -t CTCF_ChIP_200K_filterdup.pileup.bdg -c local_lambda.bdg -m qpois -o CTCF_ChIP_200K_qvalue.bdg
macs2 bdgcmp -t CTCF_ChIP_200K_filterdup.pileup.bdg -c local_bias.bdg -m ppois -o CTCF_ChIP_20
### Call peaks on score track using a cutoff
macs2 bdgpeakcall -i CTCF_ChIP_200K_qvalue.bdg -c 1.301 -l 245 -g 100 -o CTCF_ChIP_200K_peaks.bed
```



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

# Input files
```bash
wget https://github.com/taoliu/MACS/blob/aafbcaf04e6fdd363ad8ebd01cc1779712875974/test/CTCF_ChIP_200K.bed.gz?raw=true
mv CTCF_ChIP_200K.bed.gz\?raw\=true CTCF_ChIP_200K.bed.gz
wget https://github.com/taoliu/MACS/blob/aafbcaf04e6fdd363ad8ebd01cc1779712875974/test/CTCF_Control_200K.bed.gz?raw=true
mv CTCF_Control_200K.bed.gz?raw=true CTCF_Control_200K.bed.gz
```


# Step 1: Filter duplicates
Remove the redundant reads at each genomic loci in Control and ChIP data.
By default, the maximum number of allowed duplicated reads is 1, or _--keep-dup=1_ for _callpeak_.
```bash
macs2 filterdup -i CTCF_ChIP_200K.bed.gz --keep-dup=1 -o CTCF_ChIP_200K_filterdup.bed
macs2 filterdup -i CTCF_Control_200K.bed.gz --keep-dup=1 -o CTCF_Control_200K_filterdup.bed
wc -l CTCF_ChIP_200K_filterdup.bed # 199583 CTCF_ChIP_200K_filterdup.bed
wc -l CTCF_Control_200K_filterdup.bed # 199867 CTCF_Control_200K_filterdup.bed
```
ChIP: tags after filtering in alignment file: 199583
Control: tags after filtering in alignment file: 199867
They will be used to scale the ChIP and control signals to the same depth.
In this case, the number is 199583 for ChIP and 199867 for control, and the ratio between them is 199583/199867=.99858
> skip
# Step 2: Decide the fragment length d
The location of sequenced read may only tell you the end of a DNA fragment that you are interested in (such as TFBS or DNA hypersensitive regions). 
You have to estimate how long this DNA fragment is in order to recover the actual enrichment.
Normally, we only need to do this for ChIP data.
```bash
macs2 predictd -i CTCF_ChIP_200K_filterdup.bed -g hs -m 5 50
```
`-m` mfold parameters. To simulate the default behavior of _macs2 callpeak_, set _-m 5 50_.
Output the fragment length _d_: 254.
> you have a better estimation on fragment length, you can simply skip this step.
# Step 3: Extend ChIP sample to get ChIP coverage track
Extend each read and Generate a pileup track in BEDGRAPH format
## For ChIP-seq:
- Extend each read towards downstream direction with  EXTSIZE bps (default).
## For DNAse-Seq data
- or the cutting site, that is detected by short read sequencing, is in the _middle_ of the fragment you are interested in
- use _-B_ option to extend the read in both direction
```bash
macs2 pileup -f BED -i CTCF_ChIP_200K_filterdup.bed -o CTCF_ChIP_200K_filterdup.pileup.bdg --extsize 254
```
```bash
sort -k1,1 -k2,2n CTCF_ChIP_200K_filterdup.bed | head
```
chr1    115691  115791  .       .       -
chr1    237797  237897  .       .       -
```bash
sort -k1,1 -k2,2n CTCF_ChIP_200K_filterdup.pileup.bdg | head
```
chr1    0       115537  0.00000
chr1    115537  115791  1.00000
chr1    115791  237643  0.00000
# Step 4: Build local bias track from control
By default, MACS2 _callpeak_ function computes the local bias by taking the maximum bias from 
- surrounding 1kb (set by --slocal)
- surrounding 10kb (set by --llocal)
- the size of fragment length _d_ (predicted as what you got from _predictd_)
- the whole genome background
## The d background
use _pileup_ function to extend the control read to both sides (-B option) 
The idea is that the cutting site from control sample contains the noise representing a region surrounding it. To do this, take half of _d_ you got from _predictd_, 127 (1/2 of 254) for our example.
```bash
macs2 pileup -f BED -i CTCF_Control_200K_filterdup.bed -B --extsize 127 -o d_bg.bdg
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
macs2 pileup -f BED -i CTCF_Control_200K_filterdup.bed -B --extsize 500 -o 1k_bg.bdg


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
eyJoaXN0b3J5IjpbLTE4MjU5NDM1NzMsLTEzNzc5NTg0NzksMz
M2NTMzNDEzLC01OTEwOTkzMjMsLTEyMTY1Nzg3NzYsLTMwNDc3
MDUwMiwxMTM0MDQ4MDUzLC0xODc0NzAwMzM1LDEwOTE3OTAxOT
EsNzY1NzYzMTgzLDk5ODA0Mjk2OSwtMTMwNzA2OTQ3MiwtMTU3
MjgyNzU0MSwtNjQ3MjQ4NzA4LDE2MDU3MjkxNzgsLTE5MDAwOT
Q5MDQsMjMxNTI0ODA4LC05OTg2OTk1NDgsMTI4ODE4MDQ2NCw1
NzYwMTg2MjddfQ==
-->