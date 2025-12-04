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