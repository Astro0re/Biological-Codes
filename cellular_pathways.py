# Search cellular pathways, through system/function search or gene search


# Conditional requirments that point to the type of cellular reaction taking place

def temprature():
    temp= int(input("At what temprature is this reaction occuring(C): "))
    if temp > 45:
        print('This reaction is exthermic')
    elif temp < 30:
        print('This reaction is endothermic')

# Cell Fate Dicision Network
# Outcomes: Apoptosis(death) or Prolifiration(replication)
# Caused by known and unknown parameters
# Known Parameters are : Turgor pressure, Osmolarity, Cell structure paremeters, Colony Count

#| Category   | Parameter                             | Regular Levels (Stem/Progenitor) | Irregular Levels (Differentiation/Commitment) | Measurement Method          |
#| ---------- | ------------------------------------- | -------------------------------- | --------------------------------------------- | --------------------------- |
#| Molecular  | mRNA of fate genes (e.g., Etv2)       | Low/basal expression             | Threshold/high expression (e.g., Etv2 hi)     | scRNA-seq, qPCR             |
#| Molecular  | Cell-cell gene expression correlation | High correlation (R near 1)      | Decreased correlation (R reduction)           | Bulk/single-cell RNA-seq    |
#| Metabolic  | Optical redox ratio (ORR)             | Higher (OXPHOS dominant)         | Lower (glycolysis shift)                      | Label-free MOB imaging      |
#| Metabolic  | Glycolysis uptake (e.g., 6NBDG)       | Lower uptake                     | Higher uptake                                 | Fluorescence imaging        |
#| Metabolic  | FAO (PPARδ activity)                  | High for self-renewal            | Reduced, shifts to symmetric commitment       | Metabolic assays, knockouts |
#| Epigenetic | Histone H3 content                    | ~30% lower than differentiated   | 2-10x higher mRNA/protein                     | Western blot, mass spec     |
#| Epigenetic | H3K4me2/H3K27me3 marks                | Balanced for pluripotency        | H3K4me2 up, H3K27me3 shifts in differentiated | sc-CUT&RUN, ChIP-seq        |

# Take readings from sensors 
def cell_fate():
    # Histone requires western blot for readings, import image and run through function (Machince Language) to quantify 
    Histone = input('Histone h3 content = ')
    mR= input('Messanger RNA Sequence = s')
    Gly = input('Glycolisis Uptake = ')