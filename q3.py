# 3. Write a python script to check whether a given number is even or odd

num=int(input("Enter a number to check whether it is even or odd: "))

# Using only if statement
# if(num%2):
#     print(num,"is an Odd number")
# if(num%2==0):
#     print(num,"is an Even nuumber")   


# Using if else
# if(num//2*2==num):
#     print("Even number")
# else:
#     print("Odd number")    

# single line if else
print("Odd number" if(num&1) else "Even number")