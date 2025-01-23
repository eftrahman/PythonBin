#a tuple is a order, immutable collection of elements #()

coordinates = (10, 20, 30)

print(coordinates[1])

#tuples are immutable, so we cannot change their elements 
#coordinates[1] = 25 #this will raise an error

for i in coordinates:
    print(i)

for i in range(0,3):
    print(str(i)+" number coordinate is: "+str(coordinates[i]))