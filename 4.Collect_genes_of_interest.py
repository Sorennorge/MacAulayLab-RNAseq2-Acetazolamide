# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 09:50:24 2021

@author: dcs839
"""

### Transporters and ion channels of interest ###

## Import Packages ##

import os
import math

## Folders ##

Folder1 = "Lookup"
Folder2 = "Lookup/Count Tables"

Folder_out = "Results"
Folder_out2 = "Results/Table 1"

if os.path.exists(Folder_out):
    pass
else:
    os.mkdir(Folder_out)

if os.path.exists(Folder_out2):
    pass
else:
    os.mkdir(Folder_out2)

## Files ##

# File in #
File1 = "Transporters of interest.csv"
File2 = "Sample13_Control_TPM.csv"
File3 = "Sample14_Acetazolamide_TPM.csv"

# File out #
File_out = "Table 1.csv"

## Global Variables ##

Genes_of_interest = {}
Control_dict = {}
Acetazolamide_dict = {}

log2FC = {}

## Function ##

def Log2foldchange( a, b ):
    log2FC = round(math.log2( b / a ),4)
    return( log2FC )

### read files ###

## Genes of interest ##
# a csv file with the genes of interest #
with open(os.path.join(Folder1,File1),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        Genes_of_interest[line[0]] = line[1]
read.close

# Control #
with open(os.path.join(Folder2,File2),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        Control_dict[line[0]] = line[1:]
read.close

# Acetazolamide #
with open(os.path.join(Folder2,File3),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        Acetazolamide_dict[line[0]] = line[1:]
read.close

## Calculate the Log2FC for the genes of interest ##
for key in Genes_of_interest:
    A = float(Control_dict[key][1].replace(",","."))
    B = float(Acetazolamide_dict[key][1].replace(",","."))
    log2FC[key] = Log2foldchange(A,B)

## Save to file ##
with open(os.path.join(Folder_out2,File_out),'w+') as out:
    out.write("Ensembl ID;Gene symbol;Control (TPM);Acetazolamide (TPM);Log2FC\n")
    for key in Genes_of_interest:
        log2FC_string = str(log2FC[key]).replace(".",",")
        out.write("{};{};{};{};{}\n".format(key,Genes_of_interest[key],Control_dict[key][1],Acetazolamide_dict[key][1],log2FC_string))
out.close
