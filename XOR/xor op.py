import numpy as np

w11 = 1
w12 = -1

w21 = 1
w22 = -1

b11 = -0.5
b12 = 1.5

w31 = 1
w32 = 1

b2 = -1.5

def step(x):
    if x <= 0:
        return 0
    else:
        return 1

def predict(i1,i2):
    
    h11 = step(i1 * w11 + i2 * w21 + b11)
    h12 = step(i1 * w12 + i2 * w22 + b12)
    output = step(h11 * w31 + h12 * w32 + b2)

    return output

print(predict(0,0))
print(predict(0,1))
print(predict(1,0))
print(predict(1,1))