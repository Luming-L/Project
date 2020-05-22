Data:
404 donors
410 samples
796 replicates = 386 technical replicate pairs (772) + 24 single replicate samples 

Donor – An individual person. Multiple tumor samples can come from a single donor.
Sample – A piece of tumor tissue. Multiple technical replicates can exist per sample.
Technical Replicate – Tumor tissue was homogenized prior to ATAC-seq into a nuclei suspension. Each technical replicate represents an individual ATAC-seq reaction performed in a separate tube on different nuclei isolated from the same sample.

counts matrix
raw and normalized counts
The normalized peak score of the given peak (i.e. "score-per-million")
To do this, the MACS2 peak scores (-log10(p-value)) for each sample were converted to a “score per million” by dividing each individual peak score by the sum of all of the peak scores in the given sample divided by 1 million. 
MACS2 output files:
The score (5th) column contains 10 times of the average score in the broad region
5th: integer score for display. It's calculated as `int(-10*log10pvalue)` or `int(-10*log10qvalue)` depending on whether `-p` (pvalue) or `-q` (qvalue) is used as score cutoff.

## Normalised read count matrix

A data table that is obtained after  [normalisation](https://www.ebi.ac.uk/training/online/glossary/normalisation)  of next-generation sequencing data. It usually organises the samples in columns and genes/genomic loci in rows. The values represent the summarised read counts per genomic region (e.g. gene, transcript) after normalisation (e.g.  [RPKM](https://www.ebi.ac.uk/training/online/glossary/rpkm)  values).

# why read counts matrix
ATAC-seq can be used to compare chromatin accessibility between two cellular conditions.
The normalization method will affect the result of differential analysis.
ATAC-seq users should be aware of the interpretations of potential bias within experimental data and the assumptions of the normalization method implemented.

constructs a consensus read count matrix from _MACS2_ replicate peak sets of _m_ query regions by _n_ samples.


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE1NTE2NzA4OTYsNzIwMjkwNzg2LC0xMj
ExMDk2MjQsLTE4MDE5NTMxMDcsMTY1OTM2ODkyNSwtMTQzNjIz
NzcyNCwyMTAwOTkyNzEsMzQyNDM4NjQwLC0yMDc0NzA4MjAxLC
0xNjU3OTE4ODU4LC01NTYzOTc5NzIsLTE0ODI1NTY4MDQsLTk2
MjE0NDM3MiwxMjI2OTM0MTMwLC0xNjE1Mjc4ODA0LC0xNTk2OT
ExMTUxLDExNDE2Njc0MTAsNDQyODQ3MDQwLC0xODYyNTQ3NTE0
XX0=
-->