fact=1
n=int(input("Enter a number of your choice: "))

if n<0:
    print("You entered a negative number, try a positive one!")
elif n==0:
    print("The factorial of 0 equals to: ",1)
else:
    for i in range(1,n+1):
        fact=fact*i
    print("The factorial of ",n," equals to ",fact)
