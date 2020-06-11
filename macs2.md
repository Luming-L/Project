[Identifying ChIP-seq enrichment using MACS](https://www.nature.com/articles/nprot.2012.101)
[https://www.biorxiv.org/content/10.1101/496521v1.full.pdf](https://www.biorxiv.org/content/10.1101/496521v1.full.pdf)
[atac-seq peak-calling](https://galaxyproject.github.io/training-material/topics/epigenetics/tutorials/atac-seq/tutorial.html#peak-calling)
[MACS](https://github.com/macs3-project/MACS)
[MACS2 subcommand](https://github.com/macs3-project/MACS/wiki/Advanced%3A-Call-peaks-using-MACS2-subcommands#Step_4_Build_local_bias_track_from_control)
select significant bins and combine
calculate different lambda 
select lamda use average read counts to model the genome background lambda
poisson distribution
merge regions

### calculate local lambda without control
The local lambda is the maximum of the averages of tags for 1/5/10 kb regions and a whole genome background. If there is no control data, the ChIP data will be used instead, where the 1kb region is not considered.
### the principle of change the range that the lambda generates from
not affect good peak which has low FDR, big fold- enrichment, and high '-10*log(10,pvalue)', if the parameter is reasonable.
> [macs group](https://groups.google.com/forum/#!msg/macs-announcement/JkufzGpUNRk/kUx0z2M2b_cJ)

## bdgpeakcall





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

`



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
> skip. already extend when calling peaks. now it is read counts for each bin. 
> We already have peak regions and peak signal.
# Step 4: Build local bias track from control
get maximum number of reads at a certain position
By default, MACS2 _callpeak_ function computes the local bias by taking the maximum bias from 
- surrounding 1kb (set by --slocal)
- surrounding 10kb (set by --llocal)
- the size of fragment length _d_ (predicted as what you got from _predictd_)
- the whole genome background
## The d background
extend the control read to both sides with EXTSIZE bps (-B option) 
The idea is that the cutting site from control sample contains the noise representing a region surrounding it. To do this, take half of _d_ you got from _predictd_, 127 (1/2 of 254) for our example.
```bash
macs2 pileup -f BED -i CTCF_Control_200K_filterdup.bed -B --extsize 127 -o d_bg.bdg
```
## The slocal background
extend the control read to both sides with 500 bps by default.
Simply imagine that each cutting site (sequenced read) represent a 1kb (default, you can tweak it) surrounding noise.
```bash
macs2 pileup -i CTCF_Control_200K_filterdup.bed -B --extsize 500 -o 1k_bg.bdg
```
normalize the background noise track
Because the ChIP signal track was built by extending reads into _d_ size fragments, we have to normalize the 1kb noise by multiplying the values by _d_/slocal, which is 254/1000=0.254 in our example.
```bash
macs2 bdgopt -i 1k_bg.bdg -m multiply -p 0.254 -o 1k_bg_norm.bdg
```
## The llocal background
extend the control read to both sides with 5000 bps by default.
represent a 10 kb surrounding noise.
```bash
macs2 pileup -f BED -i CTCF_Control_200K_filterdup.bed -B --extsize 5000 -o 10k_bg.bdg
```
the multiplier now is _d_/llocal
```bash
bdgopt -i 10k_bg.bdg -m multiply -p 0.0254 -o 10k_bg_norm.bdg
```
## The genome background
_the_number_of_control_reads*fragment_length/genome_size_: 199867*254/2700000000 ~= .0188023.
You don't need to run subcommands to build a genome background track since it's just a single value.
## Combine and generate the maximum background noise
Combine all background noises
Compute the maximum bias for each genomic location 
```bash
# Take the maximum between slocal (1k) and llocal (10k) background
macs2 bdgcmp -m max -t 1k_bg_norm.bdg -c 10k_bg_norm.bdg -o 1k_10k_bg_norm.bdg
# Then, take the maximum then by comparing with _d_ background
macs2 bdgcmp -m max -t 1k_10k_bg_norm.bdg -c d_bg.bdg -o d_1k_10k_bg_norm.bdg
# Finally, combine with the genome wide background using _bdgopt_ subcommand
macs2 bdgopt -i d_1k_10k_bg_norm.bdg -m max -p .0188023 -o local_bias_raw.bdg
```
> need genome background
# Step 5: Scale the ChIP and control to the same sequencing depth
Scale down the larger sample to the smaller one.
This will make sure the noise won't be amplified through scaling and improve the specificity of the final results.
Scaled down the control bias by multiplying with the ratio between ChIP and control which is 199583/199867=.99858
The values in the output file can be regarded as the lambda (or expected value) and can be compared with ChIP signals using the local Poisson test.
```bash
macs2 bdgopt -i local_bias_raw.bdg -m multiply -p .99858 -o local_lambda.bdg
```
> genome background noise as lambda
# Step 6: Compare ChIP and local lambda to get the scores in pvalue or qvalue
Test the ChIP signal at each basepair against the corresponding local lambda derived from control with Poisson model.
Output score for each basepair in the genome.
Merge nearby regions with the same score
```bash
# qpois
macs2 bdgcmp -t CTCF_ChIP_200K_filterdup.pileup.bdg -c local_lambda.bdg -m qpois -o CTCF_ChIP_200K_qvalue.bdg
# ppois
macs2 bdgcmp -t CTCF_ChIP_200K_filterdup.pileup.bdg -c local_bias.bdg -m ppois -o CTCF_ChIP_200K_pvalue.bdg
```
test the output score
```bash
sort -k1,1 -k2,2n local_lambda.bdg | head  
```
chr1    0       559459  0.01877
```bash
sort -k1,1 -k2,2n CTCF_ChIP_200K_filterdup.pileup.bdg | head
```
chr1    0       115537  0.00000
chr1    115537  115791  1.00000
chr1    115791  237643  0.00000
chr1    237643  237681  1.00000
chr1    237681  237897  2.00000
```bash
sort -k1,1 -k2,2n CTCF_ChIP_200K_pvalue.bdg | head
```
chr1    0       115537  1.73061
chr1    115537  115791  3.75953
chr1    115791  237643  1.73061
chr1    237643  237681  3.75953
chr1    237681  237897  5.96387
```r
-log10(ppois(0, lambda=0.01877, lower=FALSE))
[1] 1.730605
-log10(ppois(1, lambda=0.01877, lower=FALSE))
[1] 3.759532
-log10(ppois(2, lambda=0.01877, lower=FALSE))
[1] 5.963869
```
Output BedGraph has -log10(p-value)s/ -log10(q-value)s for each basepair through local Poisson test.
# Step 7: Call peaks on score track using a cutoff
simple peak calling tool 
check the 4th column in bedGraph file and call the regions above a given cutoff.
Take the scores and call those regions higher than certain cutoff
`-g`
If two nearby regions are both above cutoff but the region in-between is lower, and if the region in-between is small enough, we should merge the two nearby regions together into a bigger one and tolerate the fluctuation. This value is set as the read length in MACS2 _callpeak_ function since the read length represent the resolution of the dataset.
`-l`
Set a minimum length for the peak.
`-c`
Set the cutoff value. Remember the scores in the output from _bdgcmp_ are in -log10 form, so if you need the cutoff as 0.05, the -log10 value is about 1.3.
```bash
macs2 bdgpeakcall -i CTCF_ChIP_200K_qvalue.bdg -c 1.301 -l 245 -g 100 -o CTCF_ChIP_200K_peaks.bed
```
5th: integer score for display. It's calculated as 10 * score in the summit from bedGraph. `int(-10*log10pvalue)` or `int(-10*log10qvalue)` depending on whether `-m ppois` (-log10pvalue) or `-m qpois` (-log10qvalue) is used in bdgcmp.
10th: relative summit position to peak start
[issues379](https://github.com/macs3-project/MACS/issues/379)
[bdgpeakcall_cmd.py](https://github.com/macs3-project/MACS/blob/master/MACS2/bdgpeakcall_cmd.py)
[BedGraph.pyx def  call_peaks](https://github.com/macs3-project/MACS/blob/master/MACS2/IO/BedGraph.pyx)
# Call peaks from alignment results by main MACS2 Function `callpeak`
```bash
macs2 callpeak -t CTCF_ChIP_200K.bed.gz -c CTCF_Control_200K.bed.gz -f BED -g hs -n test -B
```
```bash
head test_summits.bed
```
chr1    840239  840240  test_peak_1     7.0862
chr1    919549  919550  test_peak_2     8.70937
```bash
sort -k1,1 -k2,2n local_lambda.bdg | more
```
chr1    821897  826397  0.02536
chr1    826397  851460  0.01877
chr1    851460  855960  0.02536
chr1    855960  856333  0.25364
```bash
sort -k1,1 -k2,2n CTCF_ChIP_200K_filterdup.pileup.bdg | more
```
chr1    840081  840146  2.00000
chr1    840146  840147  3.00000
chr1    840147  840332  4.00000
chr1    840332  840335  3.00000
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEyMTI4MjMwMDAsLTI1MzgxMDIwNSwtOT
gxNDYxNTIwLDE1NDQ4NTg2NjEsLTE5NTU5ODI0MjcsNjQyMjkx
MTgzLDg2MTM0MzQ3MiwtMTQ5NTIzNjcxMCwtMTk0ODM1NjMyOS
wyNzk5NTI0MTAsMTg1MDY3ODk0LC0zMjExMzM4MzMsNjQ5NTk1
MjkxLC0xMjc3OTQ1MDg1LC0xNzc5MDQyODQ0LDMxOTU2MDEwNy
wtMTU5ODU1NDM4LC03MzcyODI4MzEsMTY3OTE4OTQ2NCwtMTAw
MzgzMzcxNl19
-->