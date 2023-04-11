# 1. Write a Python program to get the largest number from a list.
def largest_number(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

# Example usage
numbers = [3, 7, 1, 9, 5, 4]
print(largest_number(numbers))



