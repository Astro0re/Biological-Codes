"""
Code to stimulate celle division to a certain stage till a reset occurs

cell starts at base value, cell division/growth occur, when threshold is reached cell divides to form a new organism and both continue to grow and divide (max division 10) determined by time input
"""

# Code takes in a time input in seconds to determine how big a cell will grow within that given time 


# Simple execution
time = int(input('Time(seconds):'))
if time != int:
    print('Wrong input, enter a number')

divison = round(time / 20)

for i in range(divison):
    print(f'Cell{i} grown')

import seaborn as sns

sns.scatterplot(x = time , y = divison)