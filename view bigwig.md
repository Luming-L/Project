Download
http://hgdownload.cse.ucsc.edu/admin/exe/linux.x86_64/bedGraphToBigWig

sort -k1,1 -k2,2n unsorted.bedGraph > sorted.bedGraph
bedGraphToBigWig in.bedGraph chrom.sizes out.bw
<!--stackedit_data:
eyJoaXN0b3J5IjpbNzg2ODYwNDA5LC02MjUwNjY4NDIsLTMyNz
IwMDE3OV19
-->