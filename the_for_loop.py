
#with a range
for i in range(1, 6):
    print(i)

#through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
#for i in fruits:
#    print(i)

#through a list
for char in "python":
    print(char)


for i in range(1,21):
#    print(i)
    m=i%3
    n=i%5
    if m ==0 and n==0:
        print(str(i)+" >FizzBuzz")
    elif m == 0 : 
        print(str(i)+" >Fizz")
    elif n==0:
        print(str(i)+" >Buzz")
    
