#DNA Sequence generator
D_Gen <- function(){
  print("Generating Sequence...")
  purine <- c("A","T")
  pyramidine <- c("G","C")
  gene <- c(purine,pyramidine)
  seq <- sample(gene, size = 100, replace = TRUE)
  print(seq)
  
}

#DNA Sequence Validator and counter
D_Val <- function(Seq){
  print("Validatig Sequence...")
  gene <- c("A", "T", "G", "C")
  for (i in Seq) {
    if (i != gene){
      print("Invalid sequence")
    }
  }
  print(table(Seq))
}

# Test Function
seq_x <- D_Gen()

D_Val(seq_x)
