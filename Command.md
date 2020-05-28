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
解压.gz文件 gzip -d CTCF_SE_CTRL_chr22_50k.bed.gz
显示文件某一列出现的不重复字符 awk '{print $4}' run_pileup_CTRL.bed.bdg | sort | uniq
df -h ./ 
du -h ./
# Vim
-   $
-   ^
-   GG
-   g
-   w
-   b
-   Visual - d
-   Visual - y
-   Visual - p

<!--stackedit_data:
eyJoaXN0b3J5IjpbMjAzNTI0NjAwNywtMzUwNzk5Nzc5LC0xNT
gwNTUxNDY5LC0xODM0MzQ2NDc2LDE1NDY4MDE5ODgsMjQ0OTY5
NjM5LDg5MDcyMTM0MCwxMDI0MDEzMjc3LDIxMTE0MjY3NzcsLT
YwNTQ1ODQ0NSwtMjU1MTAzMzcsLTE3NTAzNDIwOTUsMTQxMDcx
MjU2MywxMjg0NzIyNDc4LDMwMzQ4NzQ3NiwtMTk3OTM5OTYzNC
wtNjk1ODMzODYyLC0xMDg4ODcyNTAwXX0=
-->