library (xlsx)
database <- read.xlsx(file.choose(), 4, encoding = "UTF-8")

hist(database$Pondération, breaks=5, main="Fréquence de la pondération (pour 100 itérations et 100 villes)", las=1, xlab="Pondération", ylab="Frequence", xlim=c(480,420))
