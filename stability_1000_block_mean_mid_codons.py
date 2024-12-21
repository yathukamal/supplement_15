#Import libraries
import pandas as pd
import numpy as np

#Load data
file="Stability_PR_first10.csv"
data = pd.read_csv(file)

#Sort data for relevant column
stability_column = "stability_mid"
data_sorted = data.sort_values(by=stability_column).reset_index(drop=True)

#Split into blocks of 1000 genes
block_size = 1000
num_blocks = len(data_sorted)//block_size
blocks = [data_sorted.iloc[i*block_size: (i+1)* block_size]for i in range(num_blocks)]

#Calculate mean and SEM for each block
results=[]
for block in blocks:
    mean_stability = block[stability_column].mean()
    mean_protein = block["protein_per_rna"].mean()
    sem_stability = block[stability_column].sem()
    sem_protein = block["protein_per_rna"].sem()

    results.append({
        "mean_stability": mean_stability,
        "mean_protein": mean_protein,
        "sem_stability": sem_stability,
        "sem_protein": sem_protein
    })

#Save results to CSV
output_file = "stability_1000_block_mid_codons_results.csv"
results_df=pd.DataFrame(results)
results_df.to_csv(output_file,index=False)

print("All done")