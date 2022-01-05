import numpy as np

def func(x):
    f=x**2-10.0
    return f
def fprime(y):
    f_p=2*x
    return f_p
x=1.0
for i in range(100):
    x=x-(func(x)/fprime(x))
print(x)
