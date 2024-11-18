#None is a Python keyword that means "nothing." None is known as nil, null, or undefined in different computer languages.
#If a function does not have a return clause, it will give None as the default output:
print(None == 0)       # False, because None is not equal to 0
print(None == 9)       # False, because None is not equal to any number
print(None == "")      # False, because None is not equal to an empty string
print(None == False)   # False, because None is not equal to False
print(None == True)    # False, because None is not equal to True
a = None
b = None
print(a == b)          # True, because both `a` and `b` are assigned to None


#if a function has no return, calling it will provide None value
def noReturnFunc():
    print(55+44)
sum=noReturnFunc()
print(sum)

# this function has return but only if the 'if' condition inside the function is true.
# it has no other condition and returns so for otherwise it will return None.
def withReturnFunc_1(num):
    if num%2==0:
        return False
number01=withReturnFunc_1(44) # satisfies the condition. has return.
number02=withReturnFunc_1(55) # doesn't satisfy. has no return.
print(number01)
print(number02)

# this function has two returns. for 'if' and also for 'else'.
def withReturnFunc_2(num):
    if num%2==0:
        return False
    else: return True
number01=withReturnFunc_2(44) # satisfies 'if'. has return.
number02=withReturnFunc_2(55) # satisfies 'else'. has return.
print(number01)
print(number02)
