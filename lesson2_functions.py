'''
In this lesson, we will learn the basics of FUNCTIONS.
It is good to learn about functions at the beginning because you should organise most of your code using functions.
Functions make your code easier to understand.
Functions are reusable. You can create a library of useful functions for reuse.
Your goal is to understand every line of code in the examples.
After that, type (or modify, if you like) and run the code to build your muscle memory.
'''

# EXAMPLE 1
def f1():
    print('Hello!')
    return None
f1()

# EXAMPLE 2
def f2():
    print('Hello again!')
f2()

# EXAMPLE 3
def f3():
    print('Hey!')
    print()
    print('Hey again!')
    return None
f3()

'''
FUNCTIONS
A function is a BLOCK OF CODE that performs a specific task and is defined with a name.
In EXAMPLE 1, the function is defined with the name f1.
When referring to a function, we write the name followed by parentheses, e.g. f1().

INPUT AND OUTPUT VALUES
Functions can take some input values and return some output values.
Functions can also take no inputs and return no outputs, such as f1(), f2() and f3() in the examples above.  

INDENTATION
Note the four-space indentation after def f1():.
Unlike other programming languages, Python code will not run if your indentation is inconsistent. 
The best practice is to use four spaces for all indentation.

FUNCTION CALL
To use and run a function, call the function, e.g. f1().

FUNCTION RETURN
If your function has no output, it's good practice to put return None at the last line of the function.
Python is case-sensitive. If you type return none, Python will output an error.
The return STATEMENT explicitly tells Python where the function ends. Being explicit is a best practice in Python.
However, EXAMPLE 2, with no return statement, will run with no errors.

KEYWORDS
In f1() and f3(), we use three KEYWORDS (also called RESERVED WORDS): def return None
Every programming language has a unique set of keywords (the language's vocabulary).
How many keywords are there in Python 3 (3.x is the latest version)? Ask ChatGPT!

BUILT-IN FUNCTIONS
In f1(), f2() and f3(), we use the print() function.
print() is a BUILT-IN FUNCTION. How many built-in functions are there in Python 3?

STRING
print() takes a STRING as input.
Any characters you type (including blank spaces) between single or double quotes form a string. 1234 is a number, but '1234' or "1234" is a string.
What happens if print() takes no input? (EXAMPLE 3)
'''

# EXAMPLE 4
def f4(x):
    print('The input is appended at the end of this string' + x)
    return None
f4('!')

# EXAMPLE 5
def f5(x):
    return 'Hello' + x
y = f5('!')
print(y)

# EXAMPLE 6
def f6(x):
    y = 'Hello' + x
    return y
y = f6('?')
print(y)

'''
FUNCTION INPUT AND OUTPUT
f4(), f5(), f6() take an input x. f5(), f6() return an output.
In f4(), f5(), f6(), we use the OPERATOR + to join two strings. Therefore, x must be a string.
What happens if you input a number instead of a string? Try calling f4(999).

STRING CONCATENATION
In programming, instead of "join", we say to CONCATENATE two strings.
Therefore, + is the STRING CONCATENATION OPERATOR. OPERATORS perform operations on values.

ASSIGNMENT
The character = is the ASSIGNMENT OPERATOR.
In f5(), we assign the function call f5('!') to the VARIABLE y.
In f6(), we assign the string 'Hello' + x to y.
f6() is equivalent to f5(). f5() is better. Always avoid redundant code!
'''
