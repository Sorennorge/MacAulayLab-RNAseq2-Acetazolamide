# MacAulayLab RNAseq2 Acetazolamide #
The work and scripts are done by the MacAulay Lab.\
All programs used are free and open-source.
In the interest of open science and reproducibility, all data and source code used in our research is provided here.\
Feel free to copy and use code, but please cite:\ https://fluidsbarrierscns.biomedcentral.com/articles/10.1186/s12987-021-00289-6\
*Remember* rewrite file_names and folder_names suitable for your pipeline.\
Note: Many of the tables output have converted dot to comma for danish excel annotation.
## Raw data analysis - Library Build, Mapping and Quantification ##
*Remember* rewrite file_names and folder_names suitable for your pipeline.
### RNA-STAR and RSEM Library build and indexing ###
Use these two files:\
1.1.RNA_STAR_Indexing.sh\
2.1.RSEM_Indexing.sh

### RNA-STAR Mapping and RSEM quantification ###
Use:\
1.2.RNA_STAR_RNAseq2.sh\
2.2.RSEM_RNAseq2.sh

### Count Tables with gene information ###
Requirements:\
Biomart of Rnor6.0 with Attributes: Gene stable ID & Gene name\
Use:\
3.RSEM_to_count_tables.py

### Get genes of interest and Log2FC ###
Use:\
4.Collect_genes_of_interest.py

### Get expression and Log2FC of Carbonic anhydrases ###
Use:\
5.Carbonic anhydrases.py
