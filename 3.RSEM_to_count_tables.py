# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 08:38:58 2021

@author: dcs839
"""

### Rsem to count tables - Control and Acetazolamide ###

## Import Packages ##

import os

### Folder and Files ###

## Folders ##
folder = "Lookup"
folder2 = "Lookup/rsem"

folder_out = "Lookup/Count Tables"

# if output folder doesn't exists, make one
if os.path.exists(folder_out):
    pass
else:
    os.mkdir(folder_out)

## Files ##

# Biomart file attributes: Gene stable ID,Gene name,Gene Synonym from Rnor6.0 #
file_biomart = "Biomart_rat.txt"

# Files input #
file1 = "Sample13_control_rsem.txt"
file2 = "Sample14_Acetazolamide_rsem.txt"

# Files output #
file1_out = "Sample13_Control_TPM.csv"
file2_out = "Sample14_Acetazolamide_TPM.csv"


## Variables ##

biomart = {}

sample13_rsem_gene_ids = {}
sample14_rsem_gene_ids = {}


### Read files ###

## Read biomart ##
with open(os.path.join(folder,file_biomart),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(",")
        #if Stable IDs already in dict, check if gene name differs and/or add the difference synonyms
        if not line[0] in biomart:
            biomart[line[0]] = line[1].upper()
        elif line[0] in biomart:
            if biomart[line[0]] != line[1].upper():
                print(line[0],biomart[line[0]],line[1].upper())
                break
            else:
                pass
        else:
            print("Error case 1")
            break
read.close

### for each sample ###
## Sample 13 - control ##

with open(os.path.join(folder2,file1),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split("\t")
        #if TPM > 0, add to dict
        if float(line[5]) > 0:
            # Make sure there isnt dublicates
            if not line[0] in sample13_rsem_gene_ids:
                sample13_rsem_gene_ids[line[0]] = line[1:]
            else:
                print(line[0])
                break
read.close

## Sample 14 - Acetazolamide ##

with open(os.path.join(folder2,file2),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split("\t")
        #if TPM > 0, add to dict
        if float(line[5]) > 0:
            # Make sure there isnt dublicates
            if not line[0] in sample14_rsem_gene_ids:
                sample14_rsem_gene_ids[line[0]] = line[1:]
            else:
                print(line[0])
                break
read.close


### Save count tables to files ###
## Sample 13 - control ##

with open(os.path.join(folder_out,file1_out),'w+') as out:
    #Add header
    out.write("Ensembl gene id;Gene Symbol;TPM\n")
    for key in sample13_rsem_gene_ids:
        if biomart[key] == '':
            out.write("{};Missing information;{}\n".format(key,sample13_rsem_gene_ids[key][4].replace(".",",")))
        else:
            out.write("{};{};{}\n".format(key,biomart[key],sample13_rsem_gene_ids[key][4].replace(".",",")))
out.close

## Sample 14 - Acetazolamide ##

with open(os.path.join(folder_out,file2_out),'w+') as out:
    #Add header
    out.write("Ensembl gene id;Gene Symbol;TPM\n")
    for key in sample14_rsem_gene_ids:
        if biomart[key] == '':
            out.write("{};Missing information;{}\n".format(key,sample14_rsem_gene_ids[key][4].replace(".",",")))
        else:
            out.write("{};{};{}\n".format(key,biomart[key],sample14_rsem_gene_ids[key][4].replace(".",",")))
out.close
