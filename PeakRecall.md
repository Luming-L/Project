# input file
The input files for peak recalling are ATAC-seq signal tracks that have been normalized by the number of reads in peaks. The format of signal tracks files provided by author are BigWig and we convert them to BedGraph.
**Method of generating ATAC-seq signal tracks in the paper:**
 1. bin genome into 100-bp intervals
 2. convert the Tn5 offset-corrected insertion sites into a coverage
 3. 
Then, to determine the number of Tn5 insertions within each bin we constructed a “Views” object and 
calculated the sum in each bin with “ViewSums”.
# rationale
In macs2, the `call peak` function can be decomposed to a series of subcommands. These subcommands follow these steps: 1. Filter duplicates, 2.Decide the fragment length d, 3.Extend ChIP sample to get ChIP coverage track, 4.Build local bias track from control, 5.Scale the ChIP and control to the same sequencing depth, 6.Compare ChIP and local lambda to get the scores in pvalue or qvalue, and 7.Call peaks on score track using a cutoff. Here we start from step4.
In step 4, to build local bias track from control, macs2 will will choose the maximum bias from fragment length surrounding 1k, 10k, and genome background. For fragment length, the reads will be extend to length of fragment; As to surrounding 1k or 10k, the reads will be extended by both sides. Then the pileup read counts will be the score in bedGraph file. Because our file just contain peaks, so we just calculate genome background noise. The genome backgound bias is calculated by read length*read number/genome length. In each position, the maximum of these four value will be the lambda. In step 6, for each position, the qvalue will be calculate based on poisson distribution. In step 7, with the given cutoff, gap length and peak length, position higher than the cutoff will be selected and small gap will be merged, and finally report the peaks larger than the length.  
# test
# result
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE2NzQ2ODk1MTYsMTM1MDQ1MjEzLDY2Mz
gzMDQ3MCwxNTY5NDcyMDg1LC0xMjc3MTY5MDk4LDEyOTA2Njk0
NzMsNzkyNjMxNTQ5LC0xMjQ5MDcwODg4LDYwMjA5MTM0LC0xMz
Q3Mzg4MjUyLC0xMzMxMzAzMjM3LC0zOTk2NDY2NTUsLTE2Nzk2
NzkyODFdfQ==
-->