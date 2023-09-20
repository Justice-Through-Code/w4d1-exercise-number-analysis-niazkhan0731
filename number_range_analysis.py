#number_range_analysis.py

'''
Implement Number Analysis Functions

- Function to calculate the sum of numbers within the range.
- Function to find the smallest number within the range.
- Function to find the largest number within the range.
- Function to count the number of even numbers within the range.
- Function to count the number of odd numbers within the range.

'''
# TODO: IN A COMMENT WITHIN EACH DEF, WRITE PSEUDOCODE FOR EACH SOLUTION

def calculate_sum(start, end):
    """
    Calculate the sum of numbers within the specified range.
    Arguments:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The sum of numbers within the range.
    """
    # TODO: Implement the logic to calculate the sum of numbers within the range.
    # TODO: Return the calculated sum.

    # Initialize a variable "sum" to 0
    sum = 0
    
    # Loop from start to end (inclusive)
    for number in range(start, end + 1):
        # Add the current number to "sum"
        sum += number
    
    # Return the calculated sum
    return sum
    
def find_smallest_number(start, end):
    """
    Find the smallest number within the specified range.

    Arguments:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The smallest number within the range.
    """
    # TODO: Implement the logic to find the smallest number within the range.
    # TODO: Return the found smallest number.

    # Initialize a variable "smallest" as start
    smallest = start

    # Loop from start to end (inclusive)
    for number in range(start, end + 1):
        # If the current number is smaller than "smallest", update "smallest" with the current number
        if number < smallest:
            smallest = number
    
    # Return the found smallest number
    return smallest

def find_largest_number(start, end):
    """
    Find the largest number within the specified range.

    Args:
        start (int): The starting number of the range ( inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The largest number within the range.
    """
    # TODO: Implement the logic to find the largest number within the range.
    # TODO: Return the found largest number.

    # Initialize the largest with the first number in the range
    largest = start

    # Loop from start to end (inclusive)
    for number in range(start, end + 1):
        # If the current number is larger than "largest", update "largest" with the current number
        if number > largest:
            largest = number
    
    # Return the found largest number
    return largest

def count_even_numbers(start, end):
    """
    Count the number of even numbers within the specified range.

    Args:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The count of even numbers within the range.
    """
    # TODO: Implement the logic to count even numbers within the range.
    # TODO: Return the count of even numbers.
        # Initialize a variable "count" to 0
    count = 0

    # Loop from start to end (inclusive)
    for number in range(start, end + 1):
        # If the current number is even (i.e., divisible by 2 with remainder 0), increment "count" by 1
        if number % 2 == 0:
            count += 1
    
    # Return the count of even numbers
    return count

def count_odd_numbers(start, end):
    """
    Count the number of odd numbers within the specified range.

    Args:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The count of odd numbers within the range.
    """
    # TODO: Implement the logic to count odd numbers within the range.
    # TODO: Return the count of odd numbers.
        # Initialize a variable "count" to 0
    count = 0

    # Loop from start to end (inclusive)
    for number in range(start, end + 1):
        # If the current number is odd (i.e., not divisible by 2 with remainder 1), increment "count" by 1
        if number % 2 != 0:
            count += 1
    
    # Return the count of odd numbers
    return count