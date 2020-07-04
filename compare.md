

## PRDM9 peaks set in 23 types of cancer
```bash
mkdir PRDM9_binding_perCancer
awk '{FS=OFS="\t";{print $1,$4,$5,$NF}}' fimo.gff > acc_fimo_out.bed
```

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTgxNTIxNTEwOCwtODQ4MjA4MjczLC03ND
E3MTIwNDcsNjM2MDUyMjI2LDE5MzExMTY1MjcsLTE0MTkxOTgx
MTYsLTE2MTQ0MDczNTAsLTE1NzkzODQwODEsMTQ0MDgyMjMzMC
wtMTc0NzcwNTA3MywtODc2MTA5Njc0LC04MDc4OTU5NzgsMjY3
ODMzMjgzLC0xMTg4Mzk1NDA2LDExMjQxODIwMTcsLTkxMzEwMD
E2OCwtMTYzMTk5NzkwOCwxODkxODc3NzYsLTE1OTM5NDM2MzEs
NjE2Mzg3MDI3XX0=
-->