#  Python Variables: Declaration, Naming Conventions, and Best Practices
# ======================================================================

# In Python, a variable is a name that refers to an object stored in memory. Variables allow us to store and manipulate data such as numbers, text, Boolean values, lists, and other objects.

#  1. How to declare variables in Python

# Unlike Java, C, or C++, Python does not require you to declare a variable's data type explicitly. You create a variable by assigning a value using the = operator.


name = "Rahul"
age = 25
salary = 45000.50
is_employee = True


# Here, Python automatically determines the type of each value.

# | Variable      | Value      	|Data type|
# | ------------- | --------------|---------|
# | name        	| "Rahul"  	| str     |
# | age         	| 25       	| int     |
# | salary      	| 45000.50 	| float   |
# | is_employee 	| True     	| bool    |

#  Check the type of a variable

# Use the built-in type() function.


name = "Rahul"
age = 25
salary = 45000.50
print(type(name))
print(type(age))
print(type(salary))


# Output:

# <class 'str'>
# <class 'int'>
# <class 'float'>


# You can also display a variable's value using print().


course = "Python Programming"
print(course)


# Output:

# Python Programming

#  2. Rules for naming variables

# Python has specific rules for valid variable names.

# Rule 1: A name can contain letters, digits, and underscores.


student_name = "Amit"
marks1 = 85
total_marks = 450


# Rule 2: A name must not start with a digit.


 Valid   age1 = 25 
 Invalid 1age = 25


# Rule 3: Variable names are case-sensitive.


age = 20
Age = 30
AGE = 40
print(age)   
print(Age)  
print(AGE)   

# 20
# 30
# 40

# These are three different variables.

# Rule 4: Spaces and special characters are not allowed in names.


#  Valid first_name = "Neha" 
# Invalid first name = "Neha" 
# first-name = "Neha" 
# @name = "Neha"


Rule 5: Python keywords cannot be variable names.


 Invalid class = "Python" if = 10 for = 20 Valid alternativesclass_name = "Python"if_value = 10


#  3. Python naming conventions

# A naming rule determines whether a name is legal. A naming convention is the recommended style for writing readable, maintainable code.

# | Convention              | Recommended style   | Example           |
# | ----------------------- | --------------------| ------------------|
# | Variables               | snake_case       	| student_name      |
# | Functions               | snake_case       	| calculate_total() |
# | Constants               | UPPER_SNAKE_CASE 	| MAX_RETRIES       |
# | Classes                 | PascalCase       	| StudentRecord     |
# | Internal-use attributes | Leading underscore 	| _internal_value   |

# These conventions are described in Python's PEP 8 style guide.

#  Example: good versus poor variable names


#  Poor naming
x = 50000
a = 10 
b = 20 
c = a + b 

# Better naming 

monthly_salary = 50000 
first_number = 10 
second_number = 20 
total = first_number + second_number


# The second version is easier to understand, especially when someone else reads your code.

# tip: Single-letter names such as i and j are appropriate for short loops or mathematical expressions. For business logic, prefer descriptive names.

#  4. Assigning values to variables

# Python supports several ways to assign values.

#  A. Single assignment

name = "Amit"
age = 22


#  B. Multiple assignments in one statement

name, age, city = "Amit", 22, "Indore"
print(name)
print(age)
print(city)


# Output:

# Amit
# 22
# Indore


#  C. Assign the same value to multiple variables


x = y = z = 100
print(x, y, z)


# Output:


# 100 100 100


#  D. Update an existing variable


count = 10
count = count + 1
print(count)   

11


# A shorter form uses the augmented assignment operator:


count = 10
count += 1
print(count)   
# 11


# Other examples include -=, *=, /=, and %=, where applicable.

#  5. Python is dynamically typed

# A variable does not have a permanently fixed type. Its name can be reassigned to an object of another type.


value = 100
print(type(value))
value = "Hello"
print(type(value))
value = 3.14
print(type(value))


# Output:


# <class 'int'>
# <class 'str'>
# <class 'float'>


# This is called dynamic typing.

# Important distinction: the variable name is rebound to a different object; Python is not converting the integer 100 into the string "Hello" automatically.

#  6. Variables and data types

# Python supports several built-in data types.

# | Data type  | Example                    | Description                   |
# | ---------- | ---------------------------| -------------------------------
# | int        | age = 25                   | Whole numbers                 |
# | float      | price = 99.99              | Decimal numbers               |
# | str        | name = "Ravi"              | Text                          |
# | bool       | is_active = True           | True or false                 |
# | list       | marks = [80, 90, 85]       | Ordered, mutable collection   |
# | tuple      | point = (10, 20)           | Ordered, immutable collection |
# | set        | unique_ids = {1, 2, 3}     | Collection of unique elements |
# | dict       | student = {"name": "Ravi"} | Key-value mapping             |
# | NoneType   | result = None              | Absence of a value            |

# Example:

student_name = "Ravi"
marks = [85, 90, 78]
student = { "name": student_name,    "marks": marks}
print(student["name"])
print(student["marks"])
print(student)

# Output:

# Ravi
# [85, 90, 78]


 #7. Constants in Python

#Python does not enforce constants in the same way some languages do. By convention, a constant is written in uppercase with underscores.

PI = 3.14159
MAX_ATTEMPTS = 3
COMPANY_NAME = "NEUEFISCHE"


# You can technically reassign these names:


# MAX_ATTEMPTS = 5


# Python will allow this. The uppercase name communicates to other programmers that the value is intended to remain unchanged.

#  8. Type conversion

# Sometimes you need to convert a value from one data type to another.


age_text = "25"
age_number = int(age_text)
print(age_number + 5)   
30


# Other common conversions:


number = 10
price = float(number)        
# 10.0
value = 100
text = str(value)           
# "100"
decimal_value = 9.8
whole_number = int(decimal_value)   
# 9


# Be careful: int() truncates the fractional part of a floating-point number; it does not round it to the nearest integer.

# An invalid conversion raises an exception:


#  This raises ValueError age = int("twenty")


#  9. Variable scope: local and global variables

# Scope determines where a variable name can be accessed.


company = "NEUEFISCHE"  #Global variable
def display_company():    
trainer = "Rahul"   #Local variable    
print(company)    
print(trainer)
display_company()


# Output:


# NEUEFISCHE
# Rahul

        

# The local variable trainer is available inside the function, but not directly outside it.


def calculate():    
total = 100   
print(total)calculate() print(total)   NameError: total is not defined here


# Avoid using global variables unnecessarily. Passing values as function arguments usually makes code easier to test and maintain.

#  10. Interactive practice

# Try changing the values and observe the output.

#  Variable playground

Student name (string)

Age (integer)

Marks (0–100)

# Simulated Python output

# student_name = "Amit" age = 22 marks = 85  Student: Amit Age: 22 Marks: 85 Passed: true

# This is a teaching simulation of Python variable assignment and output, not a live Python interpreter.

# 11. Common mistakes beginners should avoid

# - Using = when you mean comparison. Use = for assignment and == for equality comparison.
# - Using spaces in variable names. Use student_name, not student name.
# - Confusing Name with name; Python is case-sensitive.
# - Using meaningful built-in names such as list, str, or sum for your own variables, because this shadows the built-in names.
# - Assuming input() returns a number. It returns a string, so convert numeric input using int() or float() when appropriate.
# - Assuming a variable's type cannot change. Python permits reassignment to values of different types.
# - Using unclear names such as a1, b2, and temp when descriptive names would make the program easier to understand.

 #12. Complete classroom example

#Save this program as student_variables.py and run i