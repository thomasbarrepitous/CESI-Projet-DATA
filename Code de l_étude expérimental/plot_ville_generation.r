library (xlsx)
database <- read.xlsx(file.choose(), 1, encoding = "UTF-8")

nbVilles<-c(database$Nombre.de.villes)
tpsGeneration<-c(database$Temps.de.génération)

plot(nbVilles, tpsGeneration, type = "o", col = "blue", pch = 19, xlab="Nombre de villes", ylab="Temps de génération en s", main="Temps de génération en fonction du nombre de villes")
lines(lowess(nbVilles, tpsGeneration))


