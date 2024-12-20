# ##Part 1 cleaning the dataset##
#import libraries
import pandas as pd

#Load CSV file and read it
data = pd.read_csv("Supplementary_Data_15.csv")

#Remove rows where the data is NA in the protein or RNA column
data_cleaned = data.dropna(subset=["clean.lin.prot.mean", "ss.rna.dna.mean"])

#Get the id and the gs.sequence
extracted_data = data_cleaned[["id", "gs.sequence", "clean.lin.prot.mean", "ss.rna.dna.mean"]]

#Save the extracted data to a new CSV file and print that the action is completed
extracted_data.to_csv("simplified_supplementary_15_32.csv", index=False)
print("All done")

##Part 2 calculating protein by RNA##
#Import libraries
import pandas as pd

#Load the dataset
data = pd.read_csv('simplified_supplementary_15_32.csv')

#Calculate protein per RNA by dividing the protein column by RNA column
data["protein_per_rna"] = data["clean.lin.prot.mean"] / data["ss.rna.dna.mean"]

#Update csv with new column of protein per rna data
data.to_csv("simplified_supplementary_15_32.csv", index=False)

print("All done")
