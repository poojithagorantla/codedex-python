a = int(input("Length of a short side:"))
b = int(input("Length of another short side:"))
c =  (a**2 + b**2) ** 0.5
print(c)

#quadradic 
x = (-b + ((b**2) - (4*a*c))**0.5 )/2*a
x1 = (-b - ((b**2) - (4*a*c))**0.5 )/2*a
print(x)
print(x1)