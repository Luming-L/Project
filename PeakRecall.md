# input file
The input file for peak recalling is ATAC-seq signal tracks that have been normalized by the number of reads in peaks. 
# rationale
In macs2, the `call peak` function can be decomposed to a series of subcommands. These subcommands follow these steps: 1. Filter duplicates, 2.Decide the fragment length d, 3.Extend ChIP sample to get ChIP coverage track, 4.Build local bias track from control, 5.Scale the ChIP and control to the same sequencing depth, 6.Compare ChIP and local lambda to get the scores in pvalue or qvalue, and 7.Call peaks on score track using a cutoff. Here we start from step4.
In step 4, to build local bias track from control, macs2 will will choose the maximum bias from fragment length surrounding 1k, 10k, and genome background. For fragment length, the reads will be extend to length of fragment; As to surrounding 1k or 10k, the reads will be extended by both sides. Then the pileup read counts will be the score in bedGraph file. Because our file just contain peaks, so we just calculate genome background noise. The genome backgound bias is calculated by read length*read number/genome length. In each position, the maximum of these four value will be the lambda. In step 6, for each position, the qvalue will be calculate based on poisson distribution. In step 7, with the given cutoff, gap length and peak length, position higher than the cutoff will be selected and small gap will be merged, and finally report the peaks larger than the length.  
# test
# result
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTI5MDY2OTQ3Myw3OTI2MzE1NDksLTEyND
kwNzA4ODgsNjAyMDkxMzQsLTEzNDczODgyNTIsLTEzMzEzMDMy
MzcsLTM5OTY0NjY1NSwtMTY3OTY3OTI4MV19
-->