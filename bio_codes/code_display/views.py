from django.http import HttpResponse
from django.shortcuts import render

# Function imports from modules without import-time prompts or function calls.
from bio_modules.Cellular.cellular_pathways import readings, temprature, cell_fate
from bio_modules.Genetic.DNA_Sequence import (
    val,
    dna_gen,
    dna_ver,
    count_dna,
    start_locate,
    AT,
    GC,
)
from bio_modules.Genetic.Sequence_Alignment import s_a, diff_s_a, relational

# Find method to include python scripts
#from "/Genetic/DNA_Sequence.py" import dna_ver
#from Genetic.Punnett_Squares import punn_simple
#from Genetic.Phylogenetic_tree import  phylo_tree
from bio_modules.Cellular.Cellular_division import simp_cell
from bio_modules.Genetic.Punnett_Squares import punn_simple, punn_multi

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
def cell(request):
    # insert python code here
    # Work out inputs
    simp_cell()
    return render(request, "cell/index.html", {'cell_1' : simp_cell()} )

# Genetic Functions 
def genetic(request):
    return render(request, "genetic/index.html")

# Gross Anatomy Functions
def gross(request):
    return render(request, "gross/index.html")
