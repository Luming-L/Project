Download
http://hgdownload.cse.ucsc.edu/admin/exe/linux.x86_64/bedGraphToBigWig

sort -k1,1 -k2,2n unsorted.bedGraph > sorted.bedGraph
bedGraphToBigWig in.bedGraph chrom.sizes out.bw

bed to bedgraph

bedgraph to bigwig
<!--stackedit_data:
eyJoaXN0b3J5IjpbNzEzMTA4NjA5LDc4Njg2MDQwOSwtNjI1MD
Y2ODQyLC0zMjcyMDAxNzldfQ==
-->