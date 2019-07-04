library (xlsx)
database <- read.xlsx(file.choose(), 2, encoding = "UTF-8")

nbIteration<-c(database$Nombre.it�rations)
tpsResolution<-c(database$Temps.de.r�solution)

plot(nbIteration, tpsResolution, type = "o", col = "blue", pch = 19, xlab="Nombre d'it�rations", ylab="Temps de r�solution en s", main="Temps de r�solution en fonction du nombre d'it�rations")
lines(lowess(nbIteration, tpsResolution))

