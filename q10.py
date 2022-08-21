# 10. Write a python script to print greater among three numbers. Print number only once
# even if the numbers are the same.

a=eval(input("Enter three numbers to find greatest among them: "))
b=eval(input())
c=eval(input())

if(a>b):
    if(a>c):
        print(a,"is greatest number")
    else:
        print(c,"is greatest number")    
else:
    if(b>c):        
      print(b,"is greatest number")
    else:
      print(c,"is greatest number")    
input()      