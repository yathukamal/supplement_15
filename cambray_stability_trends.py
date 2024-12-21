#Import libraries to use
import os
import re
import RNA

#Open outfile and write into it
outfile1 = open("Stability_PR.csv", "w")
outfile1.write("seq,protein_per_rna,stability_first,stability_mid,stability_last10\n")

#Input file with data
ecoli_cds_file = "Cambray_sequence_protein_per_rna.csv"

#Read the data file
f_o = open(ecoli_cds_file, "r")
all_cds = f_o.read()
f_o.close()

#Process input data by splitting into lines and skip the header
each_cds = all_cds.splitlines()
each_cds = each_cds[1:]

#Initilise variables for storing processed data
all_good_seq = []
all_good_seq_mid = []
all_good_seq_last10 = []
all_good_PR = []

numNA = 0
#Function to extract and process data
for gn in each_cds:
    parts = gn.split(",")
    cds = re.sub("[^A-Za-z]", "", parts[1])
    prot_per_rna = parts[2]

#Extract specific sections of the sequence
    cds_10 = cds[0:30]
    cds_mid = cds[30:60]
    cds_last10 = cds[60:90]
#Handle N/A data
    if prot_per_rna == "NA":
        numNA += 1
        print(f"NA found: {numNA} in {len(each_cds)}")
    else:
#Otherwise convert protein per RNA values to float and store the data
        prot_per_rna = float(prot_per_rna)
        all_good_seq.append(cds_10)
        all_good_seq_last10.append(cds_last10)
        all_good_seq_mid.append(cds_mid)
        all_good_PR.append(prot_per_rna)

#Print a summary of the number of valid constructs found
num_good = len(all_good_seq)
print(f"Found {num_good} constructs out of {len(each_cds)}")

#Calculate RNA stability using ViennaRNA for each sequence region (First10, mid, Last10)
for i in range(0, num_good):

    fc = RNA.fold_compound(all_good_seq[i]) #first10codons
    (ss, mfe) = fc.mfe()
    stab = mfe

    fc1 = RNA.fold_compound(all_good_seq_mid[i]) #midcodons
    (ss, mfe) = fc1.mfe()
    stab_mid = mfe

    fc2 = RNA.fold_compound(all_good_seq_last10[i]) #last10codons
    (ss, mfe) = fc2.mfe()
    stab_l10 = mfe

#Write the processed data and calculated MFE to the output file
    outfile1.write(f"{all_good_seq[i]},{all_good_PR[i]},{stab},{stab_mid},{stab_l10}\n")
#Print the progress
    if i % 1000 == 0:
        print(f"{i + 1}:{all_good_seq[i]},{all_good_PR[i]},{stab},{stab_mid},{stab_l10}\n")
#Close the output file after writing in all the data
outfile1.close()
