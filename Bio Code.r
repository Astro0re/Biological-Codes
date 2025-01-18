#DNA combinations generator
D_Gen<- function(){
  purine <- c("A","T")
  pyramidine <- c("G","C")
  gene <- c(purine,pyramidine)
  sample(gene, size = 10, replace = TRUE)
}
D_Gen()