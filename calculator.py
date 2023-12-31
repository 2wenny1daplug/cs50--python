"""# Addition with int [using get_int]

from cs50 import get_int

# Prompt user for x
x = get_int("x: ")

# Prompt user for y
y = get_int("y: ")

# Perform addition
print(x + y)

Notice how the CS50 library is imported. Then, x and y are gathered from the user. 
Finally, the result is printed. Notice that the main function that would have been seen in a C program is gone entirely! 
While one could utilize a main function, it is not required.

It’s possible for one to remove the training wheels of the CS50 library. Modify your code as follows:



# Addition with int [using input]

# Prompt user for x
x = input("x: ")

# Prompt user for y
y = input("y: ")

# Perform addition
print(x + y)

Notice how executing the above code results in strange program behavior. Why might this be so?

You may have guessed that the interpreter understood x and y to be strings. 
You can fix your code by employing the int function as follows:


# Addition with int [using input]

# Prompt user for x
x = int(input("x: "))

# Prompt user for y
y = int(input("y: "))

# Perform addition
print(x + y)

Notice how the input for x and y is passed to the int function which converts it to an integer.

We can expand the abilities of our calculator. Modify your code as follows:


# Division with integers, demonstration lack of truncation

# Prompt user for x
x = int(input("x: "))

# Prompt user for y
y = int(input("y: "))

# Divide x by y
z = x / y
print(z)

Notice that executing this code results in a value, but that if you were to see more digits after .333333 you’d see that we are faced with floating-point imprecision.

We can reveal this imprecision by modifying our codes slightly:"""

# Floating-point imprecision

# Prompt user for x
x = int(input("x: "))

# Prompt user for y n 
y = int(input("y: "))

# Divide x by y
z = x / y
print(f"{z:.50f}")

#Notice that this code reveals the imprecision. Python still faces this issue, just as C does.

