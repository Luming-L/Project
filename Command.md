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
df -h ./ 
du -h ./

<!--stackedit_data:
eyJoaXN0b3J5IjpbODkwNzIxMzQwLDEwMjQwMTMyNzcsMjExMT
QyNjc3NywtNjA1NDU4NDQ1LC0yNTUxMDMzNywtMTc1MDM0MjA5
NSwxNDEwNzEyNTYzLDEyODQ3MjI0NzgsMzAzNDg3NDc2LC0xOT
c5Mzk5NjM0LC02OTU4MzM4NjIsLTEwODg4NzI1MDBdfQ==
-->