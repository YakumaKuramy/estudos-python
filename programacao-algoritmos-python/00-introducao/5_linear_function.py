# Make a program that retrieves the values "a", "b" and "x", 
# from the user to represent a function of the first degree. 
# The program should  using the notation f(x) = (a)x + (b) 
# and its result for the value of "x" in next line.

a_value = int(input("Enter the value of 'a': "))
b_value = int(input("Enter the value of 'b': "))
x_value = int(input("Enter the value of 'x': "))

result = (a_value * x_value) + b_value

print(f"f(x) = ({a_value})x + ({b_value})")
print(f"f({x_value}) = {result}")
