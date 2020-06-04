# bdgpeakcall
```bash
macs2 bdgpeakcall -i CTCF_ChIP_200K_qvalue.bdg -c 1.301 -l 245 -g 100 -o CTCF_ChIP_200K_peaks.bed
```
options
`-c` 0/0.01 
-c CUTOFF, --cutoff CUTOFF
                        Cutoff depends on which method you used for score
                        track. If the file contains pvalue scores from MACS2,
                        score 5 means pvalue 1e-5. DEFAULT: 5
`l` 501
 -l MINLEN, --min-length MINLEN
                        minimum length of peak, better to set it as d value.
                        DEFAULT: 200
`-g` 75/100
  -g MAXGAP, --max-gap MAXGAP
                        maximum gap between significant points in a peak,
                        better to set it as tag size. DEFAULT: 30
`--cutoff-analysis`
  --cutoff-analysis     While set, bdgpeakcall will analyze number or total
                        length of peaks that can be called by different cutoff
                        then output a summary table to help user decide a
                        better cutoff. Note, minlen and maxgap may affect the
                        results. DEFAULT: False
```bash
macs2 bdgpeakcall -l 501 -g 100 -i out_ACCx_025FE5F8_885E_433D_9018_7AE322A92285_X034_S09_L133_B1_T1_PMRG.insertions.bg -o peaks1.bed --cutoff-analysis
```
pscore  npeaks  lpeaks  avelpeak
479.15  2       1400    700.00
469.57  2       1400    700.00
459.99  2       1400    700.00
450.40  3       2000    666.67
440.82  4       2600    650.00
431.24  4       2600    650.00
421.65  6       4200    700.00
412.07  9       6000    666.67
402.49  13      8400    646.15
...
105.41  1874    1478200 788.79
95.83   2279    1844000 809.13
86.25   2903    2403800 828.04
76.66   3663    3112400 849.69
67.08   4584    4056500 884.93
57.50   5872    5404700 920.42
47.92   7630    7376598 966.79
38.33   10212   10399898        1018.40
**28.75**   13812   15288697        1106.91
**19.17**   20324   25188092        1239.33
```bash
macs2 bdgpeakcall -l 501 -g 100 -i out_ACCx_025FE5F8_885E_433D_9018_7AE322A92285_X034_S09_L133_B1_T1_PMRG.insertions.bg -o peaksg100.bed
wc -l peaksg100.bed # 66542 peaksg100.bed
awk '($5>191.7)' peaksg100.bed | wc -l # 48773 -10log(pvalue)
awk '($5>290)' peaksg100.bed | wc -l # 42359
```
75/100
```bash
wc -l peaksg75.bed # 52519 peaksg75.bed
```
```bash
macs2 bdgpeakcall -c 0.01 -g 100 -l 501 -i out_ACCx_025FE5F8_885E_433D_9018_7AE322A92285_X034_S09_L133_B1_T1_PMRG.insertions.bg -o peaksg100c001.bed
wc -l peaksg100c001.bed # 584510 peaksg100c001.bed
awk '($5>13.01)' peaksg100c001.bed | wc -l # 523279
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzNjUzNDMyMTddfQ==
-->