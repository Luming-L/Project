#!/bin/sh
# Grid Engine options (lines prefixed with #$)
#$ -cwd -V                  
#$ -l h_rt=48:05:00 
#$ -l h_vmem=50G


# Initialise the environment modules
. /etc/profile.d/modules.sh
 

 module load igmm/apps/MACS2/2.1.1 

#call peaks with same parameters as HINT people
#based on https://genomebiology.biomedcentral.com/articles/10.1186/s13059-019-1642-2
#Materials and experimental design

#macs2 callpeak -f BAMPE -t /exports/igmm/eddie/semple-lab/vkaiser2/Data/Lana_ATACSeq/sprmt_5.5_5.2_merged.sorted.readname.fixmate.sorted2.nodups.bam  -g hs --nomodel --nolambda --keep-dup auto --call-summits -n sprmt_5.5_5.2_merged.fixmate
 

### next, run HINT to get footprints:
module unload python
module load anaconda
source activate mypython.2.7.10

module load igmm/apps/samtools/1.6 
module load igmm/apps/meme/4.11.1 


#export RGTDATA="/exports/igmm/eddie/semple-lab/vkaiser2/Data/rgtdata"

echo $(date)
#rgt-hint footprinting --atac-seq --paired-end /exports/igmm/eddie/semple-lab/vkaiser2/Data/Lana_ATACSeq/sprmt_5.5_5.2_merged.sorted.readname.fixmate.sorted2.nodups.bam  sprmt_5.5_5.2_merged.fixmate_peaks.narrowPeak.chr1  --organism=hg38 --bias-correction --output-prefix=sprmt_5.5_5.2_merged_footprints.fixmate.chr1

#echo "done with footprinting; it's now:"
echo $(date)
 


echo "done with footprinting" 

#do Motif matching on identified footprints:
#rgt-motifanalysis matching --organism=hg38 --input-files sprmt_5.5_5.2_merged_footprints.fixmate.chr1.bed   --remove-strand-duplicates --output-location matches_no_dups.5.5_5.2_merged.fixmate.chr1

