name = input("What is you name? ")
print("Hello, "+name+"!")

#input and data types :
#taking numeric input in string
age = input("What is you age? ")
print(age)
print(type(age))

#convert to integer
age = int(age)
print(age)
print(type(age))

#directly taking integer input
favourite_number = int(input("what is your favourite number : "))
print(favourite_number)
print(type(favourite_number))

print("Hi, " + name + " You are " + str(age) + " years old, your favorite number is " + str(favourite_number)+".")