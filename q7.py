# 7. Write a python script to check whether a given number is positive, negative or zero.

num=eval(input("Enter a number: "))

if(num>0):
    print("%d is a Positive number"%num)
elif(num<0):
    print("%d is a Negative number"%num)    
else:
    print("%d"%num)    
   
