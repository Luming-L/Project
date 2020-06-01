Example for regular peak calling: 
```bash
macs2 callpeak -t ChIP.bam -c Control.bam -f BAM -g hs -n test -B -q 0.01
```

# Step 1: Filter duplicates
# Step 2: Decide the fragment length d
# Step 3: Extend ChIP sample to get ChIP coverage track
Step 4: Build local bias track from control
The d background
The slocal background
The llocal background
The genome background
Combine and generate the maximum background noise
Step 5: Scale the ChIP and control to the same sequencing depth
Step 6: Compare ChIP and local lambda to get the scores in pvalue or qvalue
Step 7: Call peaks on score track using a cutoff
Summary
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTQ4NjM5NzA1MiwtMjA4ODc0NjYxMl19
-->