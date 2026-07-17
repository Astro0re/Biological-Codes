"""
Code to stimulate celle division to a certain stage till a reset occurs

cell starts at base value, cell division/growth occur, when threshold is reached cell divides to form a new organism and both continue to grow and divide (max division 10) determined by time input
"""

# Code takes in a time input in seconds to determine how big a cell will grow within that given time 


def cell_div():
    time = int(input("Input observation time(seconds): "))
    expected_div = round(time / 20)
    k = 0
    out_cell = {f'cell{k}' : 0}
    next_cell = 1

    for i in range(expected_div):
        out_cell[f'cell{i}'] = 0
    
    for i in range(time): 
        out_cell[f'cell{k}'] += 1
        if out_cell[f'cell{k}'] >= 20: 
            break
    if (time - 20)  > 0: 
        for i in range(time - 20): 
            k +=  1
            out_cell[f'cell{k}'] += 1
            if out_cell[f'cell{k}'] >= 20: 
                break
    
    print(f"At the end of {time} seconds there are {len(out_cell)} cells")
    print(out_cell)


cell_div()