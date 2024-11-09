global_var = "this is global"

def my_function():
    global global_var
    global_var = "globally changed"
def main():
    print("before function", global_var)
    print("after function", global_var)
    my_function()  # Calling the function inside main

if __name__ == "__main__":
    main()  # Running main if this script is executed

