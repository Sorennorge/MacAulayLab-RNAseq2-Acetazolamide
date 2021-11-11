# MacAulayLab RNAseq2 Acetazolamide #

## Raw data analysis - Library Build, Mapping and Quantification ##
*Remember* rewrite file_names and folder_names suitable for your pipeline.
### RNA-STAR and RSEM Library build and indexing ###
Use these two files:
1.1.RNA_STAR_Indexing.sh
2.1.RSEM_Indexing.sh

### RNA-STAR Mapping and RSEM quantification ###
Use:
1.2.RNA_STAR_RNAseq2.sh
2.2.RSEM_RNAseq2.sh

### Count Tables with gene information ###
Requirements:
Biomart of Rnor6.0 with Attributes: Gene stable ID & Gene name
use:
3.RSEM_to_count_tables.py

### Get genes of interest and Log2FC ###
Use:
4.Collect_genes_of_interest.py

### Get expression and Log2FC of Carbonic anhydrases ###
Use:
5.Carbonic anhydrases.py
