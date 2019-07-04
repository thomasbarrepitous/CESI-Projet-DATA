library (xlsx)
database <- read.xlsx(file.choose(), 2, encoding = "UTF-8")

nbIteration<-c(database$Nombre.itérations)
tpsGeneration<-c(database$Temps.de.génération)

plot(nbIteration, tpsGeneration, type = "o", col = "blue", pch = 19, xlab="Nombre d'itérations", ylab="Temps de génération en s", main="Temps de génération en fonction du nombre d'itérations")
lines(lowess(nbIteration, tpsGeneration))


