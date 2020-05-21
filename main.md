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


<!--stackedit_data:
eyJoaXN0b3J5IjpbMzQyNDM4NjQwLC0yMDc0NzA4MjAxLC0xNj
U3OTE4ODU4LC01NTYzOTc5NzIsLTE0ODI1NTY4MDQsLTk2MjE0
NDM3MiwxMjI2OTM0MTMwLC0xNjE1Mjc4ODA0LC0xNTk2OTExMT
UxLDExNDE2Njc0MTAsNDQyODQ3MDQwLC0xODYyNTQ3NTE0XX0=

-->