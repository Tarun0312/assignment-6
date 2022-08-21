# 8.Write a python script to check whether a given quadratic equation has two real &
# distinct roots, real & equal roots or imaginary roots

a=eval(input("Enter coefficient of quadratic equations: "))
b=int(input())
c=int(input())
D=b*b-4*a*c
if(D>0):
    print("Two Real and distinct roots")
elif(D<0):
    print("Imaginary roots")
else:
    print("Real and equal roots")       
input() 