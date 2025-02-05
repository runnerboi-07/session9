def greet():
    """ # doc string - 3 double quotes & enter
    Simple function that prints hello
    :return: None
    """
    print("Hello!\n" * 3)

def greet2(name):
    """
    Simple function that greets a person
    :param name: The name of a person
    :return: None
    """
    print(f"Hello, {name}")

def special_op(a=1, b=1): # implicit values - setting parameters to a=1, b = 1
    """
    Special op is (10 * a) + b
    :param a: 1st number
    :param b: 2nd number
    :return: value, 10a+b
    """
    return (10 * a) + b

greet()

greet2("Jane")
greet2("Mary")

print(special_op(10, 2))
print(special_op(2, 10))
result = special_op(8, 9) # calling 8, 9 is using positional values to call arguments
print(f"The special op for 8 & 9 is {result}")
print(special_op(b = 8, a = 9))
print(special_op())
print(special_op(a=9))

# functions that call other functions - output of a function can be an input for another function

def bond_greet(name):
    """

    :param name:
    :return:
    """
    print(f"The name is {name}")

def bondise_name(first_name = "John", last_name = "Doe"):
    """

    :param first_name:
    :param last_name:
    :return:
    """
    return f"{last_name}, {first_name} {last_name}"

print(bondise_name("John", "Doe"))
bond_greet(bondise_name("John", "Doe"))
