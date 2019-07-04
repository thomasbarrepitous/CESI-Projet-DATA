library (xlsx)
database <- read.xlsx(file.choose(), 2, encoding = "UTF-8")

nbIteration<-c(database$Nombre.it�rations)
tpsGeneration<-c(database$Temps.de.g�n�ration)

plot(nbIteration, tpsGeneration, type = "o", col = "blue", pch = 19, xlab="Nombre d'it�rations", ylab="Temps de g�n�ration en s", main="Temps de g�n�ration en fonction du nombre d'it�rations")
lines(lowess(nbIteration, tpsGeneration))


