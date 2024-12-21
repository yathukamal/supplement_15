#Import libraries
import pandas as pd

#Load dataset
data = pd.read_csv("simplified_supplementary_15_32.csv")

#Function to calculate GC3 content
def calculate_gc3_content(codon):
    if len(codon) == 3:
        return 1 if codon[2] in ["g", "c"] else 0
    else:
        return None

#Function to calculate GC3 for all codons in the sequence
def gc3_content_for_codons(sequence):
    codons = [sequence[i:i+3] for i in range(0, len(sequence), 3)]
    gc3_content = [calculate_gc3_content(codon) for codon in codons]
    return gc3_content

#Empty list to store GC3 content
gc3_contents = []

#Loop to loop through the dataset and calculate the gc content
for index, row in data.iterrows():
    sequence = row["gs.sequence"]
    gc3_content = gc3_content_for_codons(sequence)
    gc3_contents.append(gc3_content)

#Add the calculated GC3 content for each column
for i in range(32):
    data[f"gc3_content_codon_{i+2}"] = [gc_list[i] if len(gc_list) > i else None for gc_list in gc3_contents]

#Save to new csv
data.to_csv("supplementary_codon_gc3_32.csv", index=False)

#print to say all done
print("All done")
