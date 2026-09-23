from django.http import HttpResponse
from django.shortcuts import render

# Find method to include python scripts
#from "/Genetic/DNA_Sequence.py" import dna_ver
#from Genetic.Punnett_Squares import punn_simple
#from Genetic.Phylogenetic_tree import  phylo_tree

code = 0

# Create your views here.
def index(request):
    return render(request, "home/index.html", {
        'code': code
    })
    

def ore(request):
    return HttpResponse("Hello, Ore")

# General Display for site 

# Cellular Functions 
def functions(request):
    return 

# Generic Functions 

# Gross Anatomy Functions