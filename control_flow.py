x = int(input("enter tc : "))
while x>0:
    x=x-1
    number = int(input("Enter a number : "))
    if number > 0:
        print(str(number)+" is Positive")
        i = number
        while i >= 1:
            print(number)
            i = i-1
    elif number < 0:
        print(str(number)+" is Negative")
        i = number
        while i <= -1:
            print(number)
            i = i+1
    else:
        print("The number is zero.")

    if number >= 0 and number <= 9:
        print(str(number)+" is in between 0 and 9")

    
