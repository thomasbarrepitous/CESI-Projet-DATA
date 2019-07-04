library (xlsx)
database <- read.xlsx(file.choose(), 3, encoding = "UTF-8")

iteration<-c(database$Nombre.it�rations)
ponderation<-c(database$Pond�ration)

plot(iteration, ponderation, col = "blue", pch = 19, ylab="Pond�ration", xlab="Nombre it�ration", main="Pond�ration en fonction du nombre d'it�rations (sur 5 jeux de donn�es)")
lines(lowess(iteration, ponderation))


