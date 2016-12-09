x1 = 1
x2 = 2
x3 = 3
a = 1664525
c = 1013904223
m = 2**32
while True:
    a1 = 4*x1 + a
    c1 = 4*x2 + c
    x4 = (a*x3+c) % m
    x1 = x2
    x2 = x3
    x3 = x4
    print('x =', x4)
    
