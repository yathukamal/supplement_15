##Install and load required packages##
#install.packages("relaimpo", repos = "https://CRAN.R-project.org/package=relaimpo")
library(relaimpo)
#install.packages("svglite", repos = "http://cran.us.r-project.org")
library(svglite)
#install.packages("gridExtra", repos = "http://cran.us.r-project.org")
library(gridExtra)

#Specify file path
infile_C <- "D:/supplementary_15/supplementary_codon_20_gc.csv"
#Load the dataset	
df <- read.csv(infile_C)

#Rename columns for codon positions (p_2 to p_20)
colnames(df)[3:22] <- paste(c('p'), c(2:20), sep='_')
#df <- df[,1:35]

#Define the formula for the linear model
#Model protein_per_rna as a function of GC content across the codons 2-20
formula <- protein_per_rna ~ p_2 + p_3 + p_4 +
  p_5 + p_6 + p_7 + p_8 +
  p_9 + p_10 + p_11 + p_12 +
  p_13 + p_14 + p_15 + p_16 + p_17 + p_18 + p_19 + p_20

#Build the linear model
lm_model <- lm(formula, data = df)

#Perform relative importance analysis using bootstrapping
relaimpo_results_C <- boot.relimp(lm_model, b = 100 , type = "lmg", rela=TRUE, rank = FALSE)

#print(booteval.relimp(relaimpo_results, sort = FALSE))
#pdf(outname, width = 4, height = 4)

#Generate and save the plot of relative importance results
#Open a PDF device to save into, plot the results into the pdf, close the pdf
pdf("Fig_relaimpo_20_100.pdf", width=12, height=10)
#par(mfrow = c(2,1))
plot(booteval.relimp(relaimpo_results_C, sort = FALSE, level=0.9))

dev.off()
