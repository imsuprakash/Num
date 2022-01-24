import numpy as np

n=int(input("number of data points: "))

x=np.zeros((n))
y=np.zeros((n))

for i in range(n):
    x[i]=float(input("enter x"+str(i)))
    y[i]=float(input("enter y"+str(i)))

xinter=1.5
yinter=0.0

for i in range(n):
    q=1
    for j in range(n):
        if i!=j:
            q=q*(xinter-x[j])/(x[i]-x[j])
    yinter=yinter+q*y[i]

print(xinter,yinter)

def f(x):
    return 2**x
print(f(xinter))
