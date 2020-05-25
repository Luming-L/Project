# R
清空控制台 Ctrl+L
去重 unique()
identify if an element belongs to a vector %in%
把字符串x_name变成变量再给变量赋值，用于批量读取文件并按规律命名  assign(x_name, read.table(file_name)
返回与字符串同名的变量 get(x_name)
下载bioconductor包管理器  
if (!requireNamespace("BiocManager", quietly = TRUE)) install.packages("BiocManager")
创建文件夹 dir.create("E:/project/CountsMatrices")
数据框两列相减 atac_acc_norm_ct$end-atac_acc_norm_ct$start
查看数据框数据类型 str(atac_acc_norm_ct)
[数据框操作](https://www.cnblogs.com/studyzy/p/R_DataFrame_Operation.html)
# unix
Shebang #!/bin/sh
解压到指定目录 unzip .zip -d directory
统计当前目录下文件的个数（不包括目录）ls -l | grep "^-" | wc -l
解压.tar.gz tar xvfz HINT_ATACTest.tar.gz
"--strip-components 8" extracts the files without copying their original directory structure: tar -zxvf file_name.tgz --strip-components 8
df -h ./ 
du -h ./

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE4MzQzNDY0NzYsMTU0NjgwMTk4OCwyND
Q5Njk2MzksODkwNzIxMzQwLDEwMjQwMTMyNzcsMjExMTQyNjc3
NywtNjA1NDU4NDQ1LC0yNTUxMDMzNywtMTc1MDM0MjA5NSwxND
EwNzEyNTYzLDEyODQ3MjI0NzgsMzAzNDg3NDc2LC0xOTc5Mzk5
NjM0LC02OTU4MzM4NjIsLTEwODg4NzI1MDBdfQ==
-->