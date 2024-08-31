# Bin Wang
# Watching the short videos at codewithmosh.com is very important for
# understanding this chapter
from timeit import timeit

# Chapter 6.1 Exceptions
# nothing to code. Watch the video


# Chapter 6.2 Handling Exceptions
print("\nChapter 6.2 Handling Exceptions")
print("\nTo test the erorrs, enter correct and bad values for age('z', -1, etc.)")
# Run "python app.py" or "python3 app.py" in the terminal to allow for user input
# Start coding here...

try:
    age = int(input("Age: "))
except ValueError:
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
print("Execution continues.")

try:
    age = int(input("Age: "))
except ValueError as ex:
    print("You didn't enter a valid age.")
    print(ex)
    print(type(ex))
else:
    print("No exceptions were thrown.")
print("Execution continues.")

# Chapter 6.3 Handling Different Exceptions
print("\nChapter 6.3 Handling Different Exceptions")
try:
    age = int(input("Age: "))
    xfactor = 10/age
except ValueError:
    print("You didn't enter a valid age.")
except ZeroDivisionError:
    print("Age must be greater than zero.")
else:
    print("No exceptions were thrown.")
    print(xfactor)

try:
    age = int(input("Age: "))
    xfactor = 10/age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
    print(xfactor)


# Chapter 6.4 Cleaning Up
print("\nChapter 6.4 Cleaning Up")
try:
    file = open("app.py")
    age = int(input("Age: "))
    xfactor = 10/age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
finally:
    file.close()

# Chapter 6.5 The With Statement
print("\nChapter 6.5 The With Statement")
try:
    with open("app.py") as file:
        print("File opened.")
    age = int(input("Age: "))
    xfactor = 10/age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")

# Chapter 6.6 Raising Exceptions
print("\nChapter 6.6 Raising Exceptions")


def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10/age


try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)

# Chapter 6.7 Cost of Raising Exceptions
print("\nChapter 6.7 Cost of Raising Exceptions")

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10/age


try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
"""

code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10/age



xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""

print("first code=", timeit(code1, number=10000))
print("second code=", timeit(code2, number=10000))
