# 6. Write a python script to check whether a given number is a three digit number or not.

num=int(input("Enter a number to check whether it is 3 digit number or not:\n"))

# Using if else
# if(100<=num<=999):
#     print(num,"is a 3 digit number")
# else:
#     print(num,"is not a 3 digit number")    

# Precise coding
# single line if else
print("Given number is a 3 digit number" if(num>=100 and num<=999) else "Given number is not a 3 digit number")