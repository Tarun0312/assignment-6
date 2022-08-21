# 12. Write a python script to accept one complex number from the user and display the
# greater number between real part and imaginary part    

num=complex(input("Enter a complex number:\n"))

if(num.real>num.imag):
    print(eval(num.real),"\tReal part is greater")
else:
    print(eval(num.imag),"\tImaginary part is greater")