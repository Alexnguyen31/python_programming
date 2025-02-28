#exercise1
def print_triangle(height: int, p_char: str = '*', e_char: str = ' '):
    for i in range(height):
        spaces = e_char * (height - i - 1)
        stars = p_char * (2 * i + 1)
        print(spaces + stars)

#exercise2
def find_high(matrix: list[list[int]]) -> tuple[int, int]:
    max_value = float('-inf')
    max_index = (0, 0)
    
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value > max_value:
                max_value = value
                max_index = (i, j)
    
    return max_index

#exercise3
def is_palindrome(word: str) -> bool:
    return word == word[::-1]

#exercise4
def nth_fibonacci(n: int) -> int:
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a

#exercise5
import random

def random_numbers_to_dict() -> dict:
    numbers = [random.randint(-50, 50) for _ in range(100)]
    return {
        "positive": [n for n in numbers if n > 0],
        "negative": [n for n in numbers if n < 0],
        "zero": [n for n in numbers if n == 0]
    }
