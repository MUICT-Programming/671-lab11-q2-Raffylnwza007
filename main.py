# YOUR CODE HERE
import math
def cal_dist(x1, y1, z1, x2, y2, z2,x1d=7.0, y1d=4.0, z1d=3.0, x2d=17.0, y2d=6.0, z2d=2.0): 
    if (x1 =="q" or y1 =="q" or z1 =="q") and (x2 =="q" or y2 =="q" or z2 =="q"):
        x1=x1d
        y1=y1d
        z1=z1d
        x2=x2d
        y2=y2d
        z2=z2d
    elif x2 =="q" or y2 =="q" or z2 =="q": 
        x2=x2d
        y2=y2d
        z2=z2d
        x1=float(x1)
        y1=float(y1)
        z1=float(z1)
    elif x1 =="q" or y1 =="q" or z1 =="q":
        x1=x1d
        y1=y1d
        z1=z1d
        x2=float(x2)
        y2=float(y2)
        z2=float(z2)
    else:
        x1=float(x1)
        y1=float(y1)
        z1=float(z1)
        x2=float(x2)
        y2=float(y2)
        z2=float(z2)
    print(x1, y1, z1, x2, y2, z2)
    dist = math.sqrt((x1-x2)2 + (y1)2 + (z1-z2)**2)
    return dist

x1=input()
y1=input()
z1=input()
x2=input()
y2=input()
z2=input()
print(round(cal_dist(x1, y1, z1, x2, y2, z2),2))
