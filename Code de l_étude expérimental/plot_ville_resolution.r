library (xlsx)
database <- read.xlsx(file.choose(), 1, encoding = "UTF-8")

nbVilles<-c(database$Nombre.de.villes)
tpsResolution<-c(database$Temps.de.r�solution)

plot(nbVilles, tpsResolution, type = "o", col = "blue", pch = 19, xlab="Nombre de villes", ylab="Temps de r�solution en s", main="Temps de r�solution en fonction du nombre de villes")
lines(lowess(nbVilles, tpsResolution))

