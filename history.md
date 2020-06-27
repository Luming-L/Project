
> cpgHMM_2K <- sample(cpgHMM, 2000)
> pt <- overlapPermTest(cpgHMM_2K, promoters, ntimes=1000, genome="hg19", count.once=TRUE)
Error in if (alt == "less") { : missing value where TRUE/FALSE needed
In addition: Warning messages:
1: In mclapply(seq_len(ntimes), randomize_and_evaluate, ...) :
  all scheduled cores encountered errors in user code
2: In mean.default(rand.ev, na.rm = TRUE) :
  argument is not numeric or logical: returning NA
>
>
>
> set.seed(my.seed, kind = "L'Ecuyer-CMRG" )
Error in set.seed(my.seed, kind = "L'Ecuyer-CMRG") :
  object 'my.seed' not found
> pt <- overlapPermTest(cpgHMM_2K, promoters, ntimes=1000, genome="hg19", count.once=TRUE, force.parallel=FALSE)
Error in .stopOnAvailablePkg(genome) :
  BSgenome.Hsapiens.UCSC.hg19 package is not currently installed.
  You first need to install it, which you can do with:
      library(BiocManager)
      install("BSgenome.Hsapiens.UCSC.hg19")
> pt <- overlapPermTest(cpgHMM_2K, promoters, ntimes=1000, count.once=TRUE, force.parallel=FALSE)
Error in .stopOnAvailablePkg(genome) :
  BSgenome.Hsapiens.UCSC.hg19 package is not currently installed.
  You first need to install it, which you can do with:
      library(BiocManager)
      install("BSgenome.Hsapiens.UCSC.hg19")
> library(BiocManager)
Bioconductor version 3.10 (BiocManager 1.30.10), ?BiocManager::install for help
Bioconductor version '3.10' is out-of-date; the current release version '3.11'
  is available with R version '4.0'; see https://bioconductor.org/install
> install("BSgenome.Hsapiens.UCSC.hg19")
Bioconductor version 3.10 (BiocManager 1.30.10), R 3.6.3 (2020-02-29)
Installing package(s) 'BSgenome.Hsapiens.UCSC.hg19'
Warning in install.packages(...) :
  'lib = "/gpfs/igmmfs01/software/pkg/el7/apps/R/3.6.3/lib64/R/library"' is not writable
Would you like to use a personal library instead? (yes/No/cancel) yes
Would you like to create a personal library
‘~/R/x86_64-pc-linux-gnu-library/3.6’
to install packages into? (yes/No/cancel) No
Error in install.packages(...) : unable to install packages
> install("BSgenome.Hsapiens.UCSC.hg19")
Bioconductor version 3.10 (BiocManager 1.30.10), R 3.6.3 (2020-02-29)
Installing package(s) 'BSgenome.Hsapiens.UCSC.hg19'
Warning in install.packages(...) :
  'lib = "/gpfs/igmmfs01/software/pkg/el7/apps/R/3.6.3/lib64/R/library"' is not writable
Would you like to use a personal library instead? (yes/No/cancel) yes
Would you like to create a personal library
‘~/R/x86_64-pc-linux-gnu-library/3.6’
to install packages into? (yes/No/cancel) yes
trying URL 'https://bioconductor.org/packages/3.10/data/annotation/src/contrib/BSgenome.Hsapiens.UCSC.hg19_1.4.0.tar.gz'
Content type 'application/x-gzip' length 688190187 bytes (656.3 MB)
==================================================
downloaded 656.3 MB

* installing *source* package ‘BSgenome.Hsapiens.UCSC.hg19’ ...
** using staged installation
** R
** inst
** byte-compile and prepare package for lazy loading
** help
*** installing help indices
** building package indices
** testing if installed package can be loaded from temporary location
** testing if installed package can be loaded from final location
** testing if installed package keeps a record of temporary installation path
* DONE (BSgenome.Hsapiens.UCSC.hg19)

The downloaded source packages are in
        ‘/tmp/RtmpNFofkD/downloaded_packages’
> pt <- overlapPermTest(cpgHMM_2K, promoters, ntimes=1000, genome="hg19", count.once=TRUE, force.parallel=FALSE)

Attaching package: ‘Biostrings’

The following object is masked from ‘package:base’:

    strsplit

The masked version of 'hg19' is not installed. Using the unmasked version. This means that no automatic masking will be avai                  lable.
> pt
$numOverlaps
P-value: 0.000999000999000999
Z-score: 67.5369
Number of iterations: 1000
Alternative: greater
Evaluation of the original region set: 628
Evaluation function: numOverlaps
Randomization function: randomizeRegions

attr(,"class")
[1] "permTestResultsList"
>
> pt$permuted
NULL
> mean(pt$permuted)
[1] NA
Warning message:
In mean.default(pt$permuted) :
  argument is not numeric or logical: returning NA
> pt
$numOverlaps
P-value: 0.000999000999000999
Z-score: 67.5369
Number of iterations: 1000
Alternative: greater
Evaluation of the original region set: 628
Evaluation function: numOverlaps
Randomization function: randomizeRegions

attr(,"class")
[1] "permTestResultsList"
> mean(pt$permuted)
[1] NA
Warning message:
In mean.default(pt$permuted) :
  argument is not numeric or logical: returning NA
>  plot(pt)
> png("pt.png",width = 960,height = 960)
>  plot(pt)
> dev.off()
X11cairo
       2
>
> set.seed(12345)
> download.file("http://hgdownload-test.cse.ucsc.edu/goldenPath/hg19/encodeDCC/wgEncodeAwgTfbsUniform/wgEncodeAwgTfbsSydhHepg2Rad21IggrabUniPktrying URL 'http://hgdownload-test.cse.ucsc.edu/goldenPath/hg19/encodeDCC/wgEncodeAwgTfbsUniform/wgEncodeAwgTfbsSydhHepg2Rad21IggrabUniPk.narr
Error in download.file("http://hgdownload-test.cse.ucsc.edu/goldenPath/hg19/encodeDCC/wgEncodeAwgTfbsUniform/wgEncodeAwgTfbsSydhHepg2Rad21IggrowPeak.gz",  :
  cannot open URL 'http://hgdownload-test.cse.ucsc.edu/goldenPath/hg19/encodeDCC/wgEncodeAwgTfbsUniform/wgEncodeAwgTfbsSydhHepg2Rad21IggrabUnik.gz'
In addition: Warning message:
In download.file("http://hgdownload-test.cse.ucsc.edu/goldenPath/hg19/encodeDCC/wgEncodeAwgTfbsUniform/wgEncodeAwgTfbsSydhHepg2Rad21IggrabUniP.gz",  :
  URL 'https://hgdownload-test.cse.ucsc.edu/goldenPath/hg19/encodeDCC/wgEncodeAwgTfbsUniform/wgEncodeAwgTfbsSydhHepg2Rad21IggrabUniPk.narrowPeus was 'SSL peer certificate or SSH remote key was not OK'
> download.file("http://hgdownload.cse.ucsc.edu/goldenpath/hg19/database/wgEncodeAwgTfbsSydhHepg2Rad21IggrabUniPk.txt.gz", "Rad21.gz")        trying URL 'http://hgdownload.cse.ucsc.edu/goldenpath/hg19/database/wgEncodeAwgTfbsSydhHepg2Rad21IggrabUniPk.txt.gz'
Content type 'application/x-gzip' length 720731 bytes (703 KB)
==================================================
downloaded 703 KB

> download.file("http://hgdownload.cse.ucsc.edu/goldenpath/hg19/database/wgEncodeAwgTfbsUwHepg2CtcfUniPk.txt.gz", "Ctcf.gz")
trying URL 'http://hgdownload.cse.ucsc.edu/goldenpath/hg19/database/wgEncodeAwgTfbsUwHepg2CtcfUniPk.txt.gz'
Content type 'application/x-gzip' length 812838 bytes (793 KB)
==================================================
downloaded 793 KB

> HepG2_Rad21 <- toGRanges(gzfile("Rad21.gz"), header=FALSE)
Error in value[[3L]](cond) :
  Error in toGRanges when trying to read the file "3": Error in utils::read.table(file = A, header = has.head, sep = sep, skip = num.skip, : fnt "header" matched by multiple actual arguments
> HepG2_Rad21 <- toGRanges(gzfile("Rad21.gz"))
Error in value[[3L]](cond) :
  Error in toGRanges when building a GRanges with the content of file "4": Error in .Call2("solve_user_SEW0", start, end, width, PACKAGE = "IRrange 1: at least two out of 'start', 'end', and 'width', must
  be supplied.
In addition: Warning message:
In toGRanges(file.cont) : NAs introduced by coercion
> gzfile("Rad21.gz"
+ )
A connection with
description "Rad21.gz"
class       "gzfile"
mode        "rb"
text        "text"
opened      "closed"
can read    "yes"
can write   "yes"
> toGRanges(gzfile("Rad21.gz"))
Error in value[[3L]](cond) :
  Error in toGRanges when building a GRanges with the content of file "5": Error in .Call2("solve_user_SEW0", start, end, width, PACKAGE = "IRrange 1: at least two out of 'start', 'end', and 'width', must
  be supplied.
In addition: Warning message:
In toGRanges(file.cont) : NAs introduced by coercion
> HepG2_Ctcf <- toGRanges(gzfile("Ctcf.gz"), header=FALSE)
Error in value[[3L]](cond) :
  Error in toGRanges when trying to read the file "5": Error in utils::read.table(file = A, header = has.head, sep = sep, skip = num.skip, : fnt "header" matched by multiple actual arguments
> HepG2_Ctcf <- toGRanges(gzfile("Ctcf.gz"), header=has.head)
Error in toGRanges(gzfile("Ctcf.gz"), header = has.head) :
  object 'has.head' not found
>
>
> HepG2_Rad21 <- toGRanges(read.delim(gzfile("Rad21.gz"),header=FALSE,sep = "\t")[,c(2,3,4)],header=FALSE,sep = "\t")
Warning messages:
1: In c2 : closing unused connection 6 (Ctcf.gz)
2: In c2 : closing unused connection 5 (Ctcf.gz)
3: In c2 : closing unused connection 3 (Rad21.gz)
> HepG2_Ctcf <- toGRanges(read.delim(gzfile("Ctcf.gz"),header=FALSE,sep = "\t")[,c(2,3,4)],header=FALSE,sep = "\t")
> promoters <- toGRanges("http://gattaca.imppc.org/regioner/data/UCSC.promoters.hg19.bed")
Error in value[[3L]](cond) :
  Error in toGRanges when trying to read the BED file "http://gattaca.imppc.org/regioner/data/UCSC.promoters.hg19.bed". BED files do can NOT h
Error in scan(file = file, what = what, sep = sep, quote = quote, dec = dec, : scan() expected 'an integer', got 'start'
>
> promoters <- toGRanges("http://gattaca.imppc.org/regioner/data/UCSC.promoters.hg19.bed")
Error in value[[3L]](cond) :
  Error in toGRanges when trying to read the BED file "http://gattaca.imppc.org/regioner/data/UCSC.promoters.hg19.bed". BED files do can NOT h
Error in scan(file = file, what = what, sep = sep, quote = quote, dec = dec, : scan() expected 'an integer', got 'start'
> promoters <- toGRanges(read.delim("http://gattaca.imppc.org/regioner/data/UCSC.promoters.hg19.bed",header = TRUE,sep = "\t)
+ )
+ )
+
> read.delim("http://gattaca.imppc.org/regioner/data/UCSC.promoters.hg19.bed",header = TRUE,sep = "\t)
+

<!--stackedit_data:
eyJoaXN0b3J5IjpbNzA4ODgzNDEwXX0=
-->