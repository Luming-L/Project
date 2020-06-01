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
motif alphabet
background frequencies of the letters in the alphabet, and 
strand information
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
eyJoaXN0b3J5IjpbMTg1NjEwNjE2MSw3MzQ1MTE1NjksMTYwNz
Y5NjY3LDQ3NTQyNjU0NSwxNDkyNTE5MzE5LDExNzc5MDA4MTMs
NDA4MDM5MTA0LC0yMDExMzUwODY4LDg0MzgwNzQ2OCwtOTg0Mz
Y4MzMzLDE5MTQ3ODQ5MTYsLTE2ODM4NDU3MzMsMTc3ODY4Nzk3
OSwyMDU4ODgxMTk1XX0=
-->