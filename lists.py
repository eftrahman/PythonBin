#A list is an order, mutable collection of elements #[]

fruits = ["apple","banana","cherry"]
print(fruits[0])

#Modifying list
fruits[1]="blueberry"
print(fruits)

#Adding element
fruits.append("orange")
print(fruits)

#Looping through a list
for fruit in fruits:
    print(fruit)

#Length of a list
print(len(fruits))

