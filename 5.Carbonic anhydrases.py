# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 14:38:06 2021

@author: dcs839
"""

### Carbonic anhydrases ###

## Import packages ##

import os 
import re
import math

## Functions ##
def Log2foldchange( a, b ):
    log2FC = round(math.log2( b / a ),4)
    return( log2FC )

## Folders ##
folder = "Lookup"
folder2 = "Lookup/Count Tables"
folder_out = "Results"
folder_out2 = "Results/Carbonic Anhydrase"

# if output folder doesn't exists, make one
if os.path.exists(folder_out):
    pass
else:
    os.mkdir(folder_out)

# if output folder doesn't exists, make one
if os.path.exists(folder_out2):
    pass
else:
    os.mkdir(folder_out2)

## Files ##

file_biomart = "Biomart_rat.txt"
file1 = "Sample13_Control_TPM.csv"
file2 = "Sample14_Acetazolamide_TPM.csv"

file_out = "Carbonic anhydrase.csv"

## Variables ##

biomart = {}
Carbonic_ensembls = []

Sample13_control_CA = {}
Sample14_Acetazolamide_CA = {}

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

## Collect carbonic anhydrasses ##

# Get all ensembl ids where CA+digits or CAR+digits is present - Carbonic anhydrases. 
for key in biomart:
    if bool(re.search(r'^CA+[\d]', biomart[key])) == True or bool(re.search(r'^CAR+[\d]', biomart[key])) == True :
        Carbonic_ensembls.append(key)
    else:
        pass

## Read files ##

# Control #
with open(os.path.join(folder2,file1),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        if line[0] in Carbonic_ensembls:
            Sample13_control_CA[line[0]] = line[1:]
read.close

# Acetazolamide #
with open(os.path.join(folder2,file2),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        if line[0] in Carbonic_ensembls:
            Sample14_Acetazolamide_CA[line[0]] = line[1:]
read.close

## Save to file ##
# check if all IDs are present #
if set(Sample13_control_CA.keys()) == set(Sample14_Acetazolamide_CA.keys()):
    with open(os.path.join(folder_out2,file_out),'w+') as out:
        # Header #
        out.write("Ensembl ID;Gene symbol;Control (TPM);Acetazolamide (TPM);Log2FC\n")
        # Save the findings to file #
        for key in Sample13_control_CA:
            # Calculate Log2FC #
            log2FC = Log2foldchange(float(Sample13_control_CA[key][1].replace(",",".")),float(Sample14_Acetazolamide_CA[key][1].replace(",",".")))
            # Save output #
            out.write("{};{};{};{};{}\n".format(key,Sample13_control_CA[key][0],Sample13_control_CA[key][1],Sample14_Acetazolamide_CA[key][1],str(log2FC).replace(".",",")))
    out.close
else:
    print("Error 2, Not the same entries")