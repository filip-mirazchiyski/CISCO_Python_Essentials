# 1 parameter Function:

def hi(name):
    print("Hi,", name)

hi("Greg")

# 2 parameter Function:

def hi_all(name_1, name_2):
    print("Hi,", name_2)
    print("Hi,", name_1)

hi_all("Sebastian", "Konrad")

# 3 parameter Function:

def address(street, city, postal_code):
    print("Your address is:", street, "St.,", city, postal_code)

s = input("Street: ")
p_c = input("Postal Code: ")
c = input("City: ")
address(s, c, p_c)

###

Ex.1
def subtra(a, b):
    print(a - b)
subtra(5, 2)  # outputs: 3
subtra(2, 5)  # outputs: -3

Ex.2
def subtra(a, b):
    print(a - b)
subtra(a=5, b=2)  # outputs: 3
subtra(b=2, a=5)  # outputs: 3

Ex.3
def subtra(a, b):
    print(a - b)
subtra(5, b=2)  # outputs: 3
subtra(5, 2)  # outputs: 3


def name(first_name, last_name="Smith"):
    print(first_name, last_name)
name("Andy")  # outputs: Andy Smith
name("Betty", "Johnson")  # outputs: Betty Johnson (the keyword argument replaced by "Johnson")

# 1. You can use the return keyword to tell a function to return some value. The return statement exits the function, e.g.:

def multiply(a, b):
    return a * b

print(multiply(3, 4))    # outputs: 12


def multiply(a, b):
    return

print(multiply(3, 4))    # outputs: None

# 2. The result of a function can be easily assigned to a variable, e.g.:

def wishes():
    return "Happy Birthday!

w = wishes()

print(w)    # outputs: Happy Birthday!

###

# Example 1
def wishes():
    print("My Wishes")
    return "Happy Birthday

wishes()    # outputs: My Wishes


# Example 2
def wishes():
    print("My Wishes")
    return "Happy Birthday

print(wishes())

# outputs: My Wishes
#          Happy Birthday

# 3. You can use a list as a function's argument, e.g.:

def hi_everybody(my_list):
    for name in my_list:
        print("Hi,", name)


hi_everybody(["Adam", "John", "Lucy"])

# 4. A list can be a function result, too, e.g.:

def create_list(n):
    my_list = []
    for i in range(n):
        my_list.append(i)
    return my_list

print(create_list(5))

### SCOPE

# 1. A variable that exists outside a function has scope inside the function body (Example 1) unless the function defines a variable of the same name (Example 2, and Example 3), e.g.:

# Example 1:

var = 2


def mult_by_var(x):
    return x * var


print(mult_by_var(7))  # outputs: 14

# Example 2:


def mult(x):
    var = 5
    return x * var


print(mult(7))  # outputs: 35

# Example 3:

def mult(x):
    var = 7
    return x * var


var = 3
print(mult(7))  # outputs: 49

# 2. A variable that exists inside a function has scope inside the function body (Example 4), e.g.:


def adding(x):
    var = 7
    return x + var


print(adding(4))  # outputs: 11
print(var)  # NameError

# 3. You can use the global keyword followed by a variable name to make the variable's scope global, e.g.:

var = 2
print(var)  # outputs: 2


def return_var():
    global var
    var = 5
    return var


print(return_var())  # outputs: 5
print(var)  # outputs: 5
