#A dictionary is a collection of key-value pairs. {"":"","":""}

person = {"name":"Eftear","age":25,"city":"Dhaka"}
print(person)

print(person["name"])
print(person["age"])
print(person["city"])

#Adding new key-value pairs
person["hobby"] = "coding"
print(person)

#Looping through a dictionary
for key, value in person.items():
    print(f"{key}:{value}")
#to understand the loop, with i and j
for i, j in person.items():
    print(f"{i} >> {j}")

#Checking membership
print("name" in person) #it should be true
print("favorite_color" in person) #it should be false