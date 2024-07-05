def squared(a):
    """
    Calculate the square of a number.

    Parameters:
    - a (int or float): The number to be squared.

    Returns:
    int or float: The square of the input number.
    """
    return a * a


def addition(a, b):
    """
    Add two numbers.

    Parameters:
    - a (int or float): The first number.
    - b (int or float): The second number.

    Returns:
    int or float: The sum of the two input numbers.
    """
    return a + b


def sqroot(a):
    """
    Calculate the square root of a number.

    Parameters:
    - a (int or float): The number for which the square root is calculated.

    Returns:
    float: The square root of the input number.
    """
    return a**0.5


def pythag(a, b):
    """Calculate the hypotenuse (c) or a triangle of sides a and b, using Pythagoras

    Can only use positive values
    Parameters:
    - a (int or float): The opposite/adjacent side
    - b (int or float): The opposite/adjacent side

    Returns:
        float: The hypotenuse
    """
    if (a or b) < 0:
        return "Sides of the triangle must be positive"
    c = sqroot(squared(a) + squared(b))
    return c
