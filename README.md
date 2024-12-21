# Supplement_15

Data, in the form of supplement 15, from Cambray et al's paper. For every id, protein per RNA was calculated and also gc content for codons 1-30

1. First the data was cleaned using this script cleaning_script.py. The data was read in and any NA values removed, the protein_per_rna value was calculated and every sequence was reduced to 90 nucleotides (30 codons). This produced the "simplified_supplementary_15_.csv"
   
2. The "simplifed_supplementary_15_32.csv" was read into gc_for_codon_position_32.py. The script calculated the gc content for each codon for each id, from 1-32 codons and added this to a new csv "supplementary_codon_gc.csv". This table showed the id, protein per rna, codon 1, codon 2, codon...
3. The "simplifed_supplementary_15_32.csv" was read into gc3_for_codon_position_32.py. The script calculated the gc3 content for each codon for each id, from 1-32 codons and added this to a new csv "supplementary_codon_gc.csv". This table showed the id, protein per rna, codon 1, codon 2, codon...
4. relaimpo_20_100.R -> relaimpo analysis for 20 codons, 100 bootstraps. Modelling protein per rna as a function of GC content across codon positions 2-20. Perform relative importance of codons 2-20.
5. cambray_stability_trends.py -> The CDS was split into 3 sections: first 10 codons, middle 10 codons and last 10 codons. Then the MFE stability was calculated for each construct.
6. Using data generated by cambray_stability_trends.py individual columns were extracted and sorted into blocks of 1000 genes. Then the mean and SEM for each block was calculated.
 a. stability_1000_gene_block_mean_first_codons.py -> looked at data related first 10 codons
 b. stability_1000_block_mean_mid_codons -> data related to mid 10 codons
 c. stability_1000_block_mean_last_codons -> data related to last 10 codons
7. Partial correlation analysis of GC and GC3 at codon positions 2-30

