import re
from typing import Callable

def generator_numbers(text: str):
    # Regular expression pattern to find float numbers
    pattern = re.compile(r'\b\d+\.\d+\b')
    
    # Iterate over all matches found in the text
    for match in pattern.finditer(text):
        # Yield each match as a float number
        yield float(match.group())

def sum_profit(text: str, func: Callable[[str], float]) -> float:
    # Sum all float numbers yielded by the generator function
    return sum(func(text))

# Example usage:
text = "The total income of the employee consists of several parts: 1000.01 as the main income, supplemented by additional receipts of 27.45 and 324.00 dollars."
total_income = sum_profit(text, generator_numbers)
print(f"Total income: {total_income}")