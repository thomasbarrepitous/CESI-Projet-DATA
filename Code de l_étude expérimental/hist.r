library (xlsx)
database <- read.xlsx(file.choose(), 4, encoding = "UTF-8")

hist(database$Pond�ration, breaks=5, main="Fr�quence de la pond�ration (pour 100 it�rations et 100 villes)", las=1, xlab="Pond�ration", ylab="Frequence", xlim=c(480,420))
