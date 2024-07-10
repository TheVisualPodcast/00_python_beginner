#Variables and Data Types in Python codes
#Beginner level:
# Assigning values to variables
name = "Alice"
age = 30
print(name)   #Prints Alice
print(age)    #Prints 30

# Performing arithmetic operations
number1 = 10  
number2 = 5
sum = number1 + number2
print(sum)    #Prints 15

# Creating a string
message = "Hello, world!"
print(message)  #Prints Hello, world!

# Checking a boolean value
is_active = True
print(is_active)  #Prints True

#Graduate level:
# Using multiple assignment
x, y, z = 1, 2, 3
print(x, y, z)    #Prints  1 2 3

# Formatting strings
name = "Bob"
age = 25
formatted_message = f"My name is {name} and I am {age} years old."
print(formatted_message)  #Prints My name is Bob and I am 25 years old.

# Using string methods
text = "This is a sample text."
print(text.upper())  # Convert to uppercase   #Prints THIS IS A SAMPLE TEXT.
print(text.lower())  # Convert to lowercase   #Prints this is a sample text.
print(text.split()) # Split into a list of words    #Prints ['This', 'is', 'a', 'sample', 'text.']

#Advance level:
# Defining a function with type hints
def calculate_area(length: float, width: float) -> float:
    """Calculates the area of a rectangle."""
    return length * width

print(calculate_area(10,10))  #Prints 100

# Using a conditional statement with boolean operators
temperature = 25
if temperature > 30:
    print("It's hot!")
elif temperature < 10:
    print("It's cold!")
else:
    print("It's pleasant.")
#Prints It's pleasant.

# Working with complex numbers
complex_number = 3 + 4j
print(complex_number.real)  # Access the real part    #Prints 3.0
print(complex_number.imag)  # Access the imaginary part   #Prints 4.0
