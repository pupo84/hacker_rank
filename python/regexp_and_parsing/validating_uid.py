"""
https://www.hackerrank.com/challenges/validating-uid
"""

import re
from typing import Dict, List


def is_valid(password: str) -> str:
    at_least_two_uppercase_letters: bool = len(re.findall("[A-Z]", password)) >= 2
    at_least_three_numbers: bool = len(re.findall("[0-9]", password)) >= 3
    only_alpha_characters: bool = len(re.findall("[^a-zA-Z0-9]", password)) == 0
    exact_size: bool = len(password) == 10

    repeated_letters: bool = False

    letters_counter: Dict[str, int] = dict()

    for letter in password:
        if letters_counter.get(letter) is None:
            letters_counter[letter] = 1
        else:
            repeated_letters = True
            break

    return (
        "Valid"
        if (
            at_least_two_uppercase_letters
            and at_least_three_numbers
            and only_alpha_characters
            and exact_size
            and not repeated_letters
        )
        else "Invalid"
    )


if __name__ == "__main__":
    rows: int = int(input())

    passwords: List[str] = list()

    for _ in range(rows):
        password: str = input()
        print(is_valid(password))
