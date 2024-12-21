#Install libraries to use
#install.packages("psych")
library(psych)


#Set working directory
setwd("D:/supplementary_15")

#Load dataset and read the CSV file 
data1 <-read.csv("supplementary_codon_gc3_32.csv")

#Prepare the dataset 
#Remove column 1 and convert to data frame
data2 <- as.data.frame(data1[-1])

#get number of columns 
dims <-dim(data2)[2]
#do partial correlations
par.r <- partial.r(data2, method="pearson")

#calculate degrees of freedom
N <-dim(data2)[1] - dims+1

#determine p values 
cp <- corr.p(par.r, n = N)
#Extract p values 
cp.p <- as.data.frame(cp[4])

prot_by_codon <- par.r[1,]
p <- cp.p[1,][-1]

x <- c(2:32)

#adjust for multiple testing
pb <- p.adjust(p,method = "bonferroni")

#plot
mycolours <- as.character(cut(pb,c(1,0.05,0.01,0.005,0), right=F,labels=c("red","orange","green","grey"), include.lowest=T))

#df <- data.frame(x=x, y=prot_by_codon[-1])
pdf("Partials_Cambray_GC3_v_prot.pdf")
plot(x,prot_by_codon[-1],col=mycolours,pch=20,xlab="Codon position",ylab ="Partial correlation, GC3 content v protein per RNA")
abline(h=0)
dev.off()
