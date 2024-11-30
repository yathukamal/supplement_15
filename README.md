# Supplement_15

Data, in the form of supplement 15, from Cambray et al's paper. For every id, protein per RNA was calculated and also gc content for codons 1-30

1. First the data was cleaned using this script cleaning_script.py. The data was read in and any NA values removed, the protein_per_rna value was calculated and every sequence was reduced to 90 nucleotides (30 codons). This produced the "simplified_supplementary_15.csv"
   
2. The "simplifed_supplementary_15.csv" was read into gc_for_codon_position.py. The scrupt calculated the gc content for each codon for each id, from 1-30 codons and added this to a new csv "supplementary_codon_gc.csv". This table showed the id, protein per rna, codon 1, codon 2, codon...

3.relaimpo_20_100 -> relaimpo analysis for 20 codons, 100 bootstraps 
