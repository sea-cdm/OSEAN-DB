# Use to download query....
BiocManager:: install ("GEOquery")
library(GEOquery)

#paath = 'C:/Users/huffmaar/OneDrive - Michigan Medicine/Documents/GitHub/OSEAN-DB/ETL_TestCases/ImmPort UseCase/ImmPortsample_'



paath = 'C:/Users/huffmaar/OneDrive - Michigan Medicine/Documents/GitHub/OSEAN-DB/ETL_TestCases/ImmPort UseCase/ImmPortsample.csv'

lista <- read.csv(paath)
a <- lista[c(1:10),]


GSM_EX <- 'GSM3030156'
GSE_EX <- 'GSE111404'

GEOquery(GSE_EX)

gds <- getGEO(filename=system.file("extdata/GDS507.soft.gz",package="GEOquery"))

names(GSMList(gse))
GSMList(gse)[[1]]

