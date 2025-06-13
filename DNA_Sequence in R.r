#DNA Sequence generator
D_Gen<- function(){
  print("Generating Sequence...")
  purine <- c("A","T")
  pyramidine <- c("G","C")
  gene <- c(purine,pyramidine)
  seq <- sample(gene, size = 100, replace = TRUE)
  print("Counting Sequence...")
  print(table(seq))
}

#DNA Sequence Validator
D_Val<- function(Seq){
  print("Validatig Sequence...")
  purine <- c("A","T")
  pyramidine <- c("G","C")
  gene <- c(purine,pyramidine)
  for i in Seq:
    if i != gene[i]
    print ("invalid Sequence")
}
