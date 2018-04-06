import math
def find_next_square(sq):
    if(sq**(1/2) - int(sq**(1/2)) == 0.0):
        return (sq**(1/2) + 1) ** 2
    return -1

next_square = find_next_square(100)
print(int(next_square))
