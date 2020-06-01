Find Individual Motif Occurrences
# Knowledge
A motif is a sequence pattern that occurs repeatedly in a group of related sequences.
Motifs can be represented as position-dependent letter-probability matrices that describe the probability of each possible letter at each position in the pattern.
A text file in MEME minimal motif format can contain more than one motif, and also (optionally) specifies the 
# Options
`--parse-genomic--coord`
`--thresh`
`--max-stored-scores`
# Input
`motif file`
Format Specification
The minimal MEME format contains following sections:

- Version (required)
- Alphabet (recommended)
- Strands (optional)
- Background frequencies (recommended)
- Motifs (required)
[sample-dna-motif.meme](http://meme-suite.org/doc/examples/sample-dna-motif.meme)

`sequence file`
# Output
# Result
## ACC
79801 motif occurences with a p-value less than 0.0001
Each line stands for each significant match to a motif.
The lines are sorted in order of decreasing statistical significance (increasing _p_-value).
score
p-value
q-value: The _p_-values for each motif occurrence are converted to _q_-values following the method of Benjamini and Hochberg ("_q_-value" is defined as the minimal false discovery rate at which a given motif occurrence is deemed significant).
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzMDg4MjkxNjMsLTEzMjQxNDY5MTEsNz
M0NTExNTY5LDE2MDc2OTY2Nyw0NzU0MjY1NDUsMTQ5MjUxOTMx
OSwxMTc3OTAwODEzLDQwODAzOTEwNCwtMjAxMTM1MDg2OCw4ND
M4MDc0NjgsLTk4NDM2ODMzMywxOTE0Nzg0OTE2LC0xNjgzODQ1
NzMzLDE3Nzg2ODc5NzksMjA1ODg4MTE5NV19
-->