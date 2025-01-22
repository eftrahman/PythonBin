i = 1
while i<=5:
    print(i)
    i+=1

while True:
    i = int(input("enter a number from 0 to 99 to exit: "))
    if i >= 0 and i <=99:
        print("Goodbye!")
        break
    else:
        print("again")