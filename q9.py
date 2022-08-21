# 9. Write a python script to check whether a given year is a leap year or not.

yr=int(input("Enter a year to check whether it is a leap year or not: "))

if(yr%100):
    if(yr%4):
        print(yr,"is not a leap year")
    else:    
        print(yr,"is a leap year")    

else:
    if(yr%400):
        print(yr,"is not a leap year")
    else:
        print(yr,"is a leap year")   
input()        