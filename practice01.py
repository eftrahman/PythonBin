myInput=None
myInput=int(input("myInput : "))
myInput2=int(input("input : "))
myInput=myInput+myInput2
print("myInput : ",myInput)
print("z"*10)
t1 = 'f'
t2 = int(input("quantity : "))
print('f'* t2)

# Python program to demonstrate the application of iskeyword()
# importing keyword library which has lists
import keyword

# displaying the complete list using "kwlist()."
print("The set of keywords in this version is: ")
print(keyword.kwlist)

# Boolean input
# To simulate a boolean input, we can check if the response is "yes" or "no"
likes_python = input("Do you like Python? (yes/no): ").strip().lower() == "yes"
print("Likes Python:", likes_python)

response = input("Do you like Python? (yes/no): ").strip().lower()
if response == "yes":
    likes_python = True
elif response == "no":
    likes_python = False
else:
    print("Invalid input. Please enter 'yes' or 'no'.")
    likes_python = None  # Or handle as you wish

print(None==0)
print(None==9)
print(None=="")
print(None==False)
print(None==True)
a=None
b=None
print(a==b) 
