# R
清空控制台 Ctrl+L
去重 unique()
identify if an element belongs to a vector %in%
把字符串x_name变成变量再给变量赋值，用于批量读取文件并按规律命名  assign(x_name, read.table(file_name)
返回与字符串同名的变量 get(x_name)
下载bioconductor包管理器  
if (!requireNamespace("BiocManager", quietly = TRUE)) install.packages("BiocManager")
# unix
Shebang #!/bin/sh
解压到指定目录 unzip .zip -d directory
统计当前目录下文件的个数（不包括目录）ls -l | grep "^-" | wc -l
解压.tar.gz tar xvfz HINT_ATACTest.tar.gz
df -h ./ 
du -h ./

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTYyMDk1ODA2MSwxMDI0MDEzMjc3LDIxMT
E0MjY3NzcsLTYwNTQ1ODQ0NSwtMjU1MTAzMzcsLTE3NTAzNDIw
OTUsMTQxMDcxMjU2MywxMjg0NzIyNDc4LDMwMzQ4NzQ3NiwtMT
k3OTM5OTYzNCwtNjk1ODMzODYyLC0xMDg4ODcyNTAwXX0=
-->