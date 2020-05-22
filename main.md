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
The whole workflow for differential accessiblity
1. _MACS2_ constructs an ATAC fragment pileup from aligned paired-end data
2. builds a local bias track through a series of parameters to estimate background noise
3. 

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTk2ODM4OTc4NCw3MjAyOTA3ODYsLTEyMT
EwOTYyNCwtMTgwMTk1MzEwNywxNjU5MzY4OTI1LC0xNDM2MjM3
NzI0LDIxMDA5OTI3MSwzNDI0Mzg2NDAsLTIwNzQ3MDgyMDEsLT
E2NTc5MTg4NTgsLTU1NjM5Nzk3MiwtMTQ4MjU1NjgwNCwtOTYy
MTQ0MzcyLDEyMjY5MzQxMzAsLTE2MTUyNzg4MDQsLTE1OTY5MT
ExNTEsMTE0MTY2NzQxMCw0NDI4NDcwNDAsLTE4NjI1NDc1MTRd
fQ==
-->