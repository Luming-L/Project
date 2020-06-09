Download
http://hgdownload.cse.ucsc.edu/admin/exe/linux.x86_64/bedGraphToBigWig

sort -k1,1 -k2,2n unsorted.bedGraph > sorted.bedGraph
bedGraphToBigWig in.bedGraph chrom.sizes out.bw

bed to bedgraph
column5: 

bedgraph to bigwig

```bash
awk -v OFS="\t" '{$5=$5>1000?1000:$5} {print}' ACCx_025FE5F8_885E_433D_9018_7AE322A92285_X034_S09_L133_B1_T1_PMRG.insertions.bed > ACCx_025FE5F8_885E_433D_9018_7AE322A92285_X034_S09_L133_B1_T1_PMRG.insertions.1000.bed
cut -f 5 ACCx_025FE5F8_885E_433D_9018_7AE322A92285_X034_S09_L133_B1_T1_PMRG.insertions.1000.bed | sort | head
```

[UCSC narrowPeak](https://genome.ucsc.edu/FAQ/FAQformat.html#format12)
<!--stackedit_data:
eyJoaXN0b3J5IjpbNzkxMTI3MTE4LDIzNTk0NzQ0NSwyMDkwNz
YwMTczXX0=
-->