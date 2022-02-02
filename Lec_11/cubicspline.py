from scipy.interpolate import CubicSpline
import numpy as np

x=[0,1,2]
y=[1,2,4]

f=CubicSpline(x,y)
xint=1.5
yint=f(xint)
print(yint)

