# R
清空控制台 Ctrl+L
去重 unique()
identify if an element belongs to a vector %in%
把字符串x_name变成变量再给变量赋值，用于批量读取文件并按规律命名  assign(x_name, read.table(file_name)
返回与字符串同名的变量 get(x_name)
下载bioconductor包管理器  
if (!requireNamespace("BiocManager", quietly = TRUE)) install.packages("BiocManager")
创建文件夹 dir.create("E:/project/CountsMatrices")
# unix
Shebang #!/bin/sh
解压到指定目录 unzip .zip -d directory
统计当前目录下文件的个数（不包括目录）ls -l | grep "^-" | wc -l
解压.tar.gz tar xvfz HINT_ATACTest.tar.gz
"--strip-components 8" extracts the files without copying their original directory structure: tar -zxvf file_name.tgz --strip-components 8
df -h ./ 
du -h ./

<!--stackedit_data:
eyJoaXN0b3J5IjpbMjQ0OTY5NjM5LDg5MDcyMTM0MCwxMDI0MD
EzMjc3LDIxMTE0MjY3NzcsLTYwNTQ1ODQ0NSwtMjU1MTAzMzcs
LTE3NTAzNDIwOTUsMTQxMDcxMjU2MywxMjg0NzIyNDc4LDMwMz
Q4NzQ3NiwtMTk3OTM5OTYzNCwtNjk1ODMzODYyLC0xMDg4ODcy
NTAwXX0=
-->