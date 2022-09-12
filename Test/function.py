def car():
    print("BMW")


car()


# How to pass argument  to function
# what is Parameter: A parameter is the variable listed inside the parentheses in function definition .
# what is Argument: An argument  is the value that is sent to the function when it called .
def myBike(name):
    print("My bike name is " + name)


myBike("Activa")


# Arbitrary Argument , *args

# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

def my_function(*kids):
    print("The youngest child is " + kids[1])


my_function("Email", "Tobias", "linus")


# How to pass list agrument to function

def my_function(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "carrot"]
my_function(fruits)


# how to get return value from function:

def math(a, b):
    c = a + b
    return c


print(math(3, 4, ))
