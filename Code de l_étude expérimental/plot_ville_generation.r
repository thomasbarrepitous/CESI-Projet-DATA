library (xlsx)
database <- read.xlsx(file.choose(), 1, encoding = "UTF-8")

nbVilles<-c(database$Nombre.de.villes)
tpsGeneration<-c(database$Temps.de.g�n�ration)

plot(nbVilles, tpsGeneration, type = "o", col = "blue", pch = 19, xlab="Nombre de villes", ylab="Temps de g�n�ration en s", main="Temps de g�n�ration en fonction du nombre de villes")
lines(lowess(nbVilles, tpsGeneration))


