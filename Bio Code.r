#DNA combinations generator
D_Gen<- function(){
  purine <- c("A","T")
  pyramidine <- c("G","C")
  gene <- c(purine,pyramidine)
  seq <- sample(gene, size = 100, replace = TRUE) 
  print(table(seq))
}

D_Gen()
