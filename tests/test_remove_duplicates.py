"""
Sample implementation of a function that removes duplicates from a list
while preserving the original order of first occurrence.
"""

def remove_duplicates(nums):
    """Removes duplicates from a list of numbers while preserving order.
    :param nums: A list of numbers (int and float) that may contain duplicates (e.g. [1, 2, 3, 2, 4, 1, 5])
    :return: A new list containing only the unique numbers from the original list, in the same order they first appeared (e.g. [1, 2, 3, 4, 5])
    """

    # Check if the input is a list
    if not isinstance(nums, list):
        raise TypeError("Input must be a list of numbers")
    
    # Check if the input is a list of int/float values
    if not all(isinstance(num, (int, float)) for num in nums):
        raise ValueError("Input list must be numbers (int or float).")
    
    seen = set() # keep track of which numbers we have already seen
    result = []  # store the unique numbers in the order they first occurred

    # Functional-style approach (less readable but valid)
    result = list(filter(lambda num: num not in seen and not seen.add(num), nums))

    # Using a loop version is more readable
    # Iterate through each number in the input list and check if it has been seen before, else we skip it and move on to the next number
    # for num in nums:
    #     # If the number is not seen before, then add it to the seen set and also append it to the result list
    #     if num not in seen:
    #         seen.add(num)
    #         result.append(num)
    
    return result


# Usage: pytest tests/test_remove_duplicates.py
def test_remove_duplicates():
    # Define a list of test cases as tuples, each tuple contains: (input list, expected output after removing duplicates)
    test_cases = [
        ([1, 2, 3, 2, 4, 1, 5], [1, 2, 3, 4, 5]),  # mixed duplicated
        ([1, 1, 1], [1]),                          # all duplicated
        ([], []),                                  # empty list case
    ]

    # Iterate through each test case
    for test_case, expected in test_cases:
        # Call the function to remove duplicates with current input
        result = remove_duplicates(test_case)

        # Print input and outputs for debugging/visibility purpose
        print(f"\nInput:  {test_case}")
        print(f"Result: {result}")
        print(f"Expect: {expected}")

        # Assert that the actual output matches expected output
        assert result == expected, f"Failed for input {test_case}"
