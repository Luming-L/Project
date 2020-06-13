# input file
The input files for peak recalling are ATAC-seq signal tracks that have been normalized by the number of reads in peaks. The format of signal tracks files provided by author are BigWig and we convert them to BedGraph.
**Method of generating ATAC-seq signal tracks in the paper:**
 1. bin genome into 100-bp intervals
 2. convert the Tn5 offset-corrected insertion sites into a coverage
 3. calculate the sum of per position coverage in each bin as the number of Tn5 insertions within each bin
 4. normalize the total number of reads by a scale factor that converted all samples to a constant 30 million reads within peaks
 5. normalize samples by their quality and read depth

In the BedGraph file, the score is the signal in each 100-bp bin. We can take the average signal of all bins as genome background and calculate the statistical significance for signal in each bin.
|chr|start|end|score|
|--|--|--|--|
|chr1|0|9999|0.000000|
|chr1|9999|10099|9.525880|
|chr1|10099|10199|14.288800|
# rationale
In MACS2, the main function `callpeak` can be decomposed into a pipeline containing MACS2 subcommands. The pipeline follows these steps: 
1. Filter duplicates
2. Decide the fragment length d
3. Extend ChIP sample to get ChIP coverage track
4. Build local bias track from control
5. Scale the ChIP and control to the same sequencing depth
6. Compare ChIP and local lambda to get the scores in pvalue or qvalue
7. Call peaks on score track using a cutoff

For our input files, we start from step 4.
In step 4, `callpeak` by default computes the local noise by taking the maximum noise from surrounding 1kb, 10kb, the size of fragment length _d_ (the predicted length of the DNA fragment that you are interested), and the whole genome background. For d, 1kb and 10kb background, the control read will be extended to both sides by d/2, 500 and 5000 bp, respectively, to reproduce noise from a region surrounding the read. The coverage at each position after normalization will be the corresponding local noise. The noise from genome background is calculated as _the_number_of_control_reads*fragment_length/genome_size_. At each position, the maximum in these four values will be the local noise, which is regarded as the lambda and can be compared with ChIP signals using the local Poisson test. When a control sample is not available, lambda is calculated from the ChIP-seq sample, excluding d and 1kb.
In our case, we just have normalized ATAC-seq signal tracks in BedGraph and thus cannot extend reads, the genome-wide average signal will be used as noise. We can calculate it as:
(_sum_of_signals_in_all_bins/genome_zise)*bin_size_
We generate a BedGraph file to store the lambda.

In step 6, the ATAC-seq signal at each genomic location stored in BedGraph will be tested against the lambda  with Poisson distribution. The score in the output file is -log10(p-value)s or -log10(q-value)s (according to the option `-m`) for each location.
```bash
macs2 bdgcmp -t CTCF_ChIP_200K_filterdup.pileup.bdg -c local_lambda.bdg -m qpois -o CTCF_ChIP_200K_qvalue.bdg
```
Step 7 is the final task of peak calling. Regions with scores higher than certain cutoff (set by `-c`) will be kept. If two nearby regions are both above cutoff but the region in-between is lower, and if the region in-between is small enough (set by `-g`), we will merge the two nearby regions together into a bigger one. `-g` is set as the read length since the read length represent the resolution of the dataset. `-l` sep a minimum length for the peak, which is . MACS2 _callpeak_ function automatically uses the fragment size _d_ as the parameter of minimum length of peak, and as for _bdgpeakcall_, you need to set the _-l_ option as the _d_ you got from Step 2.
with the given cutoff, gap length and peak length, position higher than the cutoff will be selected and small gap will be merged, and finally report the peaks larger than the length.  
# test
# result

<!--stackedit_data:
eyJoaXN0b3J5IjpbODg3NTY3ODc0LC0xMjc3NzU4NjkyLDEyMT
A5MzY0OTAsLTEzMTk3NjUyODUsLTE3ODk4ODE3NjEsMTY1OTI5
ODI0NywtMTE3MDExOTgxOSwtNTc3NzQ0Mzg2LC00Njk5NjgwMT
ksLTE0NTg5NzI1MjEsMTE3NzQ2Nzk2OSwxMTczNDc4Niw5OTMw
NzIwNjAsMTg2NjAyNTY3NCwtMTMxNDQyMzc0MSwtMTk4MTAzNT
YxLC01NDczMTIyNDMsLTE5Mzk1NjkzNDcsMzc5MzczMzMxLC02
OTU1MjU1NF19
-->