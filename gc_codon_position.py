#Import libraries
import pandas as pd

#Load dataset
data = pd.read_csv("simplified_supplementary_15.csv")

#Function to calculate GC content
def calculate_gc_content(codon):
    if len(codon) == 3:
        return(codon.count("g") + codon.count("c")) / 3 * 100
    else:
        return None

#Function to calculate GC for all codons in the sequence
def gc_content_for_codons(sequence):
    codons = [sequence[i:i+3] for i in range(0, len(sequence), 3)]
    gc_content = [calculate_gc_content(codon) for codon in codons]
    return gc_content

#Empty list to store GC content
gc_contents = []

#Loop to loop through the dataset and calculate the gc content
for index, row in data.iterrows():
    sequence = row["gs.sequence"]
    gc_content = gc_content_for_codons(sequence)
    gc_contents.append(gc_content)

#Add the calculated GC content for each column 
for i in range(30):
    data[f"gc_content_codon_{i+1}"] = [gc_list[i] if len(gc_list) > i else None for gc_list in gc_contents]

#Save to new csv
data.to_csv("supplementary_codon_gc.csv", index=False)

#print to say all done
print("All done")
