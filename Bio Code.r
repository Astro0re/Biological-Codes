#DNA combinations generator
D_Gen<- function(){
  purine <- c("A","T")
  pyramidine <- c("G","C")
  gene <- c(purine,pyramidine)
  sample(gene, size = 100, replace = TRUE) 
}
D_Gen()
#Count
table(D_Gen())