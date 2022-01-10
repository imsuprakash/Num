import numpy as np

def f(x):
    return (10-x**2)

def trap(a,b,n):
    h=(b-a)/n

    s=(f(a)+f(b))

    i=1
    while i<n:
        s += 2*f(a+i*h)
        i +=1
    s=s*(h/2)
    return(s)
x1=-2
x2=2
n=100
I=trap(x1,x2,n)
print("The value of the integral: ", I)
