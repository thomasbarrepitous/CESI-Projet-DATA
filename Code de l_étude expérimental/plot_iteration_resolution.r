library (xlsx)
database <- read.xlsx(file.choose(), 2, encoding = "UTF-8")

nbIteration<-c(database$Nombre.itérations)
tpsResolution<-c(database$Temps.de.résolution)

plot(nbIteration, tpsResolution, type = "o", col = "blue", pch = 19, xlab="Nombre d'itérations", ylab="Temps de résolution en s", main="Temps de résolution en fonction du nombre d'itérations")
lines(lowess(nbIteration, tpsResolution))

