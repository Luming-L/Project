determine_REase
input:  subSequences, default_REase, REase_list
output: REase/None
process:
change the order of REase_list, make default one be the first
Iterate the REase_list
1. subSequences to overlapped_subSequences
2. check REase

Class REase
properties:
name, recognition_site, cleave_location
methods: 
get_name
get_recognition_site
cleave_location

Class OligoGroup
properties:
sequence, REase, division
methods:
get_overlapped_subSequences(sequence, subSequences_positions, REase)
1. [0,1], [2,4],[5,6],[7,9]
2. [0,2],[2,5],[5,7],[7,9]
3. abc, cabc, cab, bab
half_on_positive_half_on_negative(division, overlapped_subSequences)
get_oligos(overlapped_subSequences, division, REase, )

add_recognition_site(REase)
add_conplementary
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTM5MTM3MTg5MiwtMzcxNzg1NDQwLC0xMT
cxNDYxMzExLDE3OTkyMjM3NV19
-->