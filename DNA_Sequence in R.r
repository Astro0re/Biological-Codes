#DNA combinations generator
D_Gen<- function(){
  print("Generating Sequence...")
  purine <- c("A","T")
  pyramidine <- c("G","C")
  gene <- c(purine,pyramidine)
  seq <- sample(gene, size = 100, replace = TRUE)
  print("Counting Sequence...")
  print(table(seq))
}
