
global_var = "*** I'm global"  # Global variable

def my_function():
    global_var = "### I'm local"  # This creates a local variable with the same name
    print("Inside function:", global_var)
    #global global_var      #here I tried to use the global with the same name of local again
    #global_var = "*#* Changed Globally"
    #this block of code will cause Syntax Error.
    #SyntaxError: name 'global_var' is used prior to global declaration

def my_function2():
    global global_var
    global_var = "*#* Changed Globally"
print("Before function:", global_var)  # This prints the global variable
my_function()  # This prints the local variable inside the function
my_function2()
print("After function:", global_var)  # This still prints the global variable
