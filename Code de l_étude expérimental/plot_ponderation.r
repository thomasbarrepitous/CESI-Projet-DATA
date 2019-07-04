library (xlsx)
database <- read.xlsx(file.choose(), 3, encoding = "UTF-8")

iteration<-c(database$Nombre.itérations)
ponderation<-c(database$Pondération)

plot(iteration, ponderation, col = "blue", pch = 19, ylab="Pondération", xlab="Nombre itération", main="Pondération en fonction du nombre d'itérations (sur 5 jeux de données)")
lines(lowess(iteration, ponderation))


