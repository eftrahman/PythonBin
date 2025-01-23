#A set is an unordered collection of unique elements #{}

unique_numbers = {1, 2, 3, 3, 3, 4}
print(unique_numbers) #Duplicates will be removed

#Adding elements
unique_numbers.add(5)
unique_numbers.add(4) #This is also a duplicate. It will not be in the set.
print(unique_numbers)

#Checking membership
print(3 in unique_numbers) #if member then output : True

#Looping through a set
for num in unique_numbers:
    print(num)
