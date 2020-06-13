# rationale
In macs2, the `call peak` function can be decomposed to a series of subcommands. These subcommands follow these steps: 1.Filter duplicates, 2.Decide the fragment length d, 3.Extend ChIP sample to get ChIP coverage track, 4.Build local bias track from control, 5.Scale the ChIP and control to the same sequencing depth, 6.Compare ChIP and local lambda to get the scores in pvalue or qvalue, and 7.Call peaks on score track using a cutoff. Because we just have the BigWig file 
# application
# result
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzNDczODgyNTIsLTEzMzEzMDMyMzcsLT
M5OTY0NjY1NSwtMTY3OTY3OTI4MV19
-->