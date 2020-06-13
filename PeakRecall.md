# input file
The input files for peak recalling are ATAC-seq signal tracks that have been normalized by the number of reads in peaks. The format of signal tracks files provided by author are BigWig and we convert them to BedGraph.
**Method of generating ATAC-seq signal tracks in the paper:**
 1. bin genome into 100-bp intervals
 2. convert the Tn5 offset-corrected insertion sites into a coverage
 3. calculate the sum of per position coverage in each bin as the number of Tn5 insertions within each bin
 4. normalize the total number of reads by a scale factor that converted all samples to a constant 30 million reads within peaks
 5. normalize samples by their quality and read depth

In the BedGraph file, the score is the signal in each 100-bp bin. We can take the average signal of all bins as genome background and calculate the statistical significance for signal in each bin.

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
In step 4, `callpeak` by default computes the local bias by taking the maximum bias from surrounding 1kb, 10kb, the size of fragment length _d_ (the predicted length of the DNA fragment that you are interested), and the whole genome background. For d, 1kb and 100kb background, the control read will be extended to both sides
 For fragment length, the reads will be extend to length of fragment; As to surrounding 1k or 10k, the reads will be extended by both sides. Then the pileup read counts will be the score in bedGraph file. Because our file just contain peaks, so we just calculate genome background noise. The genome backgound bias is calculated by read length*read number/genome length. In each position, the maximum of these four value will be the lambda. In step 6, for each position, the qvalue will be calculate based on poisson distribution. In step 7, with the given cutoff, gap length and peak length, position higher than the cutoff will be selected and small gap will be merged, and finally report the peaks larger than the length.  
# test
# result
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIwMTM3NTEyMTksLTE5ODEwMzU2MSwtNT
Q3MzEyMjQzLC0xOTM5NTY5MzQ3LDM3OTM3MzMzMSwtNjk1NTI1
NTQsNzQ2Nzc1MjUxLC0xOTk3NzUzMjE3LC0yNzE0OTAwMjMsLT
IxMzQ4NDE4MTAsMTAyNjkyOTQzMCwtNTY3MTQxMTMyLDEzNTA0
NTIxMyw2NjM4MzA0NzAsMTU2OTQ3MjA4NSwtMTI3NzE2OTA5OC
wxMjkwNjY5NDczLDc5MjYzMTU0OSwtMTI0OTA3MDg4OCw2MDIw
OTEzNF19
-->