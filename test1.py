import numpy as np
import random

X = [1,2,3]
Y = [2,4,6]

count = 0
input_x = 4
w = 0
b = 0

def num(input_num):
    output_num = input_num * w + b 
    return output_num

while count <= 1000:
    x = random.randint(1,3)
    num(X[x])

    if count % 10 == 0:
        print()
    count += 1