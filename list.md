## Aim
compare PRDM9 site in different kind of cancer germline
search for structural variation and indel position 
different alleles ABC
how is PRDM9 expression related to the binding sites

## data
Gene expression and mutation data:
[Pan-Cancer](https://xenabrowser.net/datapages/?cohort=GDC%20Pan-Cancer%20(PANCAN)&removeHub=https%3A%2F%2Fxena.treehouse.gi.ucsc.edu%3A443)
BAM files once we got them from TCGA

## pipeline
Use HINT-ATAC pipeline to call footprints and binding sites:
[paper](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-019-1642-2)
[HINT-ATAC pipeline](http://www.regulatory-genomics.org/hint/introduction/)

Motif finding:
Familiarise yourself with Japspar database.
PWM (position weight matrix) for PRDM9 will be added to the Jaspar motifs, so you can search for the motif.

13-mer motif

## Environment
Let me know if you need access to eddie3:
username@eddie3.ecdf.ed.ac.uk
conda environment


PRDM9 allele link:

"The tissue donor used for the analysis was a carrier of the most common (European) alleles of PRDM9, using the SNP identified by (Hinch, Tandon et al. 2011) (rs6889665) which was also covered by our ATAC-Seq by 10 reads, all of which were “T”."

=> Check if you can distinguish the different PRDM9 alleles (using the ATAC-Seq BAM files or gene expression files)

Testis-derived PRDM9 sites come from Pratto et al:

[https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE59836](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE59836)

liftOver tool (on Eddie3) to lift over to different genome assemblies (19=37 & 38)

Circular Permutations: to get a p-value of overlap for tumour-versus-testis PRDM9 binding and also for mutation-versus-PRDM9 binding​:

[https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4708104/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4708104/)

More references on Methods

**[Mutational Biases Drive Elevated Rates of Substitution at Regulatory Sites across Cancer Types](https://www.research.ed.ac.uk/portal/en/publications/mutational-biases-drive-elevated-rates-of-substitution-at-regulatory-sites-across-cancer-types(5a00d7bc-a13f-4ce9-9ec6-e53ae92491a1).html "view on Edinburgh Research Explorer")**4 Aug 2016 In: PLoS Genetics, vol. 12, no. 8, pp. e1006207  
DOI: [https://doi.org/10.1371/journal.pgen.1006207](https://doi.org/10.1371/journal.pgen.1006207)

-   **[Chromatin loop anchors are associated with genome instability in cancer and recombination hotspots in the germline](https://www.research.ed.ac.uk/portal/en/publications/chromatin-loop-anchors-are-associated-with-genome-instability-in-cancer-and-recombination-hotspots-in-the-germline(9b7b0b32-7c43-4aa3-94cf-480a92a2863d).html "view on Edinburgh Research Explorer")**30 Jul 2018 In: Genome Biology, vol. 19, no. 1  
    DOI: [https://doi.org/10.1186/s13059-018-1483-4](https://doi.org/10.1186/s13059-018-1483-4)  
    Contribution to journal › Article (Published)



Seminars:

Wednesday lab meeting: Sessions for 2020, also listed below, will be held in E4.07 @ 1030 am unless otherwise stated.

22-Jan-2020 Stuart A

5-Feb-2020 Tom

19-Feb-2020 Ilya

4-Mar-2020 Vera

18-Mar-2020 Graeme

1-Apr-2020 Thomas

15-Apr-2020 Juliet

29-Apr-2020 Jan

13-May-2020 Kathryn

27-May-2020 Gogo

10-Jun-2020 Tracy

24-Jun-2020 Imke

2-Sep-2020 Elvina

16-Sep-2020 Craig

30-Sep-2020 Alhafidz – change of venue: S1.14

14-Oct-2020 Martin

28-Oct-2020 Colin

11-Nov-2020 Mike

25-Nov-2020 Ailith

Tuesday @2:30pm: Section meeting in South Seminar room

Wednesday 1pm: Section meeting (HGU seminars)

Thursday: 1pm IGMM seminars: in big liecture theatre on the left hand side when you come into the building:

[https://www.ed.ac.uk/igmm/news-and-events/events/igmm-seminar-series](https://www.ed.ac.uk/igmm/news-and-events/events/igmm-seminar-series)

> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbMzk2MTY4NTg4LDYxNDQ4MjIxMiwxNTU2Mj
c5OTA3LDEwNjU1OTU1MjZdfQ==
-->