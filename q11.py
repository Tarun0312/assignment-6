# 11. Write a python script to take the month value in numeric format and display the
# number of days in it.
  

# using match
monthNo=int(input("Enter month number: "))

match monthNo:
    case 1,3:
        print("31 Days")
    # case 3:
    #     print("31 Days")    
    case 5:
        print("31 Days")
    case 7:
        print("31 Days")   
    case 8:
        print("31 Days")
    case 10:
        print("31 Days")
    case 12:
          print("31 Days")
    case 2:
        print("28/29 Days")    
    case 4:
        print("30 Days")
    case 6:    
        print("30 days")
    case 9:
          print("30 Days")
    case 11:
          print("30 Days")
    case _:
        print("Invalid month number")   
    
