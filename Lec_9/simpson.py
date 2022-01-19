def f(x):
    return 10-3*x**2

n=4
a=-1
b=3
h=(b-a)/n

integral=f(a)+f(b)
for i in range(1,n):
    k=a+i*h
    if i%2 ==0:
        integral=integral+2*f(k)
    else:
        integral=integral+4*f(k)

integral=(h/3)*integral
print(integral)
