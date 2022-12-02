import ctypes

C_INT_MAX = 2147483647

# Get input from user
a = int(input("Please enter an integer value for A: "))
b = int(input("Please enter an integer value for B: "))
c = int(input("Please enter an integer value for C: "))


# Call the c "library"
func = ctypes.CDLL("mylib.so")

# Specify the c integer arguments for the function
func.doMath.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int]


# Call the c function with a, b, and c arguments and assign the return value to output
output = func.doMath(a, b, c)

# If the c function returns INT_MAX - 1 (signals divide by 0 error), let user know
if output == C_INT_MAX - 1:
    print("Error: Division by zero")

# Else, print output
else:
    print(f"Value is: {output}")
