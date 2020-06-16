#!/usr/bin/python3
import numpy as np
import pandas as pd
import os, sys
import subprocess as sp

# store the path of the bedGraph file
file_path  = sys.argv[1]
print(file_path)

# get the name of the bedGraph file without leading directory components and a trailing SUFFIX.
cmd='basename -s ".bdg" '+file_path
result = sp.check_output(cmd, shell=True)
fileName = str(result).split("'",1)[1].split("\\",1)[0]
print(fileName)

# read bedgraph file containing read counts as score
df = pd.read_csv(file_path, sep="\t",header=None,names=["chr","start","end","score"])

# obtain the length of each chromosome, and use a dictionary to store them
Chrs={}
for chrName in df['chr'].drop_duplicates().values.tolist():
    Chrs[chrName]=df[df['chr']==chrName].iloc[-1:,]['end'].values[0]

# For each track in the bedGraph, multiply the length by score as total score of a track
df['totalScore']=df.apply(lambda x : (x['end']-x['start'])*x['score'], axis=1)
# sum up the length of each chromosome as genome length
# sum up all totalscore and divide the sum by the length of whole genome, as bias from the whole genome background
# It will be the lambda in poisson distribution
Lambda = df['totalScore'].sum()/sum(Chrs.values())
print(df['totalScore'].sum())
print(sum(Chrs.values()))

# the first column is chromosome name
s1 = pd.Series(list(Chrs.keys()))
# the second column is the first position in each chromosome
s2 = pd.Series(np.zeros(len(Chrs.keys()),int))
# the third column is the last position in each chromosome
s3 = pd.Series(list(Chrs.values()))
# the fourth column is Lambda
s4 = pd.Series(np.full(len(Chrs.keys()),Lambda))

# make a dataframe to store tracks
df2=pd.DataFrame({'chr':s1,'start':s2,'end':s3,'Lambda':s4})

df2.to_csv(fileName+".lambda.bdg",sep="\t",header=False,index=False)

# use `bdgcmp` to calculate the qvalue for each position based on poisson distribution
#os.system("macs2 bdgcmp -t "+file_path+" -c " +fileName+".lambda.bdg"+" -m qpois -o "+fileName+".qvalue.bdg")
print("macs2 bdgcmp -t "+file_path+" -c " +fileName+".lambda.bdg"+" -m qpois -o "+fileName+".qvalue.bdg")
# According to the cutoff, gap, and length, merge positions to form a peak
#os.system("macs2 bdgpeakcall -i "+fileName+".qvalue.bdg"+" -c 1.301 -l 245 -g 100 -o "+fileName+".peaks.bed")
print("macs2 bdgpeakcall -i "+fileName+".qvalue.bdg"+" -c 1.301 -l 245 -g 100 -o "+fileName+".peaks.bed")
