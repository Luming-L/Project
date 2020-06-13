# input file
The input files for peak recalling are ATAC-seq signal tracks that have been normalized by the number of reads in peaks. The format of signal tracks files provided by author are BigWig and we convert them to BedGraph as input.

**Method of generating ATAC-seq signal tracks in the paper:**
 1. bin genome into 100-bp intervals
 2. convert the Tn5 offset-corrected insertion sites into a coverage
 3. calculate the sum of per position coverage in each bin as the number of Tn5 insertions within each bin
 4. normalize the total number of reads by a scale factor that converted all samples to a constant 30 million reads within peaks
 5. normalize samples by their quality and read depth

**Usage:**

In the BedGraph file, the score is the signal in each 100-bp bin. We can take the average signal of all bins as genome background and calculate the statistical significance for signal in each bin.
|chr|start|end|score|
|--|--|--|--|
|chr1|0|9999|0.000000|
|chr1|9999|10099|9.525880|
|chr1|10099|10199|14.288800|
# rationale
> `callpeak` used by author: For each sample, peak calling was performed on the Tn5-corrected single-base insertions using the MACS2 callpeak command with parameters “--shift -75 --extsize 150 --nomodel --call-summits --nolambda --keep-dup all -p 0.01”. The peak summits were then extended by 250 bp on either side to a final width of 501 bp.

> read length: 75 bp paired-end.

In MACS2, the main function `callpeak` can be decomposed into a pipeline containing MACS2 subcommands. The pipeline follows these steps: 
1. Filter duplicates
2. Decide the fragment length d
3. Extend ChIP sample to get ChIP coverage track
4. Build local bias track from control
5. Scale the ChIP and control to the same sequencing depth
6. Compare ChIP and local lambda to get the scores in pvalue or qvalue
7. Call peaks on score track using a cutoff

For our input files, we follow step 4, 6 and 7.
# Step 4: Build local bias track from control
`callpeak` by default computes the local noise by taking the maximum noise from surrounding 1kb, 10kb, the size of fragment length _d_ (the predicted length of the DNA fragment that you are interested), and the whole genome background. For d, 1kb and 10kb background, the control read will be extended to both sides by d/2, 500 and 5000 bp, respectively, to reproduce noise from a region surrounding the read. The coverage at each position after normalization will be the corresponding local noise. As to the noise from genome background, it is calculated as _the_number_of_control_reads*fragment_length/genome_size_. At each position, the maximum in these four values will be the local noise, which is regarded as the lambda and can be compared with ChIP signals using the local Poisson test. When a control sample is not available, lambda is calculated from the ChIP-seq sample, excluding d and 1kb.

**In our case**, `callpeak` used by author turned on `--nolambda` option, which means MACS used the background lambda as local lambda, and we just have normalized ATAC-seq signal tracks in BedGraph and thus cannot extend reads. Therefore, the genome-wide average signal will be used as noise. We can calculate it as:
(_sum_of_signals_in_all_bins/genome_zise)*bin_size_
We generate a new BedGraph file to store the lambda.

# Step 6: Compare ChIP and local lambda to get the scores in pvalue or qvalue
the ATAC-seq signal at each genomic location stored in BedGraph will be tested against the lambda  with Poisson distribution. The score in the output file is -log10(p-value)s or -log10(q-value)s (according to the option `-m`) for each location.
The main function `callpeak` by default uses 0.05 as q-value (minimum FDR) cutoff to call significant regions. So in our case, we set `-m qpois` in `bdgcmp` and `-c 1.301` in `bdgpeakcall`.
```bash
macs2 bdgcmp -t CTCF_ChIP_200K_filterdup.pileup.bdg -c local_lambda.bdg -m qpois -o CTCF_ChIP_200K_qvalue.bdg
```
# Step 7: Call peaks on score track using a cutoff
is the final task of peak calling. 
In this step, positions with scores higher than certain cutoff (set by `-c`) will be kept. Remember the scores in the output from _bdgcmp_ are in -log10 form, so we set `-c 1.301` when we want to select positions with p-value lower than 0.05 (-log10(0.05) = 1.301). If two nearby regions are both above cutoff but the region in-between is lower, and if the region in-between is small enough (set by `-g`, i.e. `--max-gap`), we will merge the two nearby regions together into a bigger one. `-g` is set as the read length since the read length represent the resolution of the dataset. Finally, only peaks larger than a minimum length (set by `-l`, i.e. `--min-length`) will be reported. `-l` is set as the fragment size _d_ by default. 
We set  `-c 1.301`, `-g 75` and `-l 501` here.
`-l 501`: The peak width is 501 bp.

# test
# result
# Ref
[Advanced:-Call-peaks-using-MACS2-subcommands](https://github.com/macs3-project/MACS/wiki/Advanced:-Call-peaks-using-MACS2-subcommands)
[MACS#macs-model-based-analysis-for-chip-seq](https://github.com/macs3-project/MACS#macs-model-based-analysis-for-chip-seq)
[Identifying ChIP-seq enrichment using MACS](https://www.nature.com/articles/nprot.2012.101)

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIwNDQwMjU2NTcsLTE5MjI1Mzk5NjEsMT
k3Njg2OTc3MiwtNjE5NTk4NDU2LC0xNDcwODg2MTEwLDEzNTUz
OTM3NTksMjAzNzgxMjU2OCwtNzU4MjgxODQ5LC01NzkzNDU2MD
MsMTA3Mjg2OTczOSwtMjQyODcxNTA2LC0xMTg3NTg0MDMzLC0x
MzgzNjIxMzg1LC05MzEzMDYzODQsLTEyMjU4NjIzNTAsLTc1MD
YzMjE3MCwxMzU0NzA0MDU1LC00Mjc2NzYwODMsLTEwOTE2NjY0
MTMsMjUwODcwMjg3XX0=
-->