"""
https://www.hackerrank.com/challenges/validating-credit-card-number
"""

import re
from itertools import groupby


def is_valid(credit_card: str) -> str:
    is_valid_start_digit: bool = re.match("^[4|5|6].*$", credit_card) is not None
    is_valid_size: bool = len(credit_card.replace("-", "")) == 16
    is_valid_format: bool = (
        re.fullmatch("^[0-9]{4}(-)?[0-9]{4}(-)?[0-9]{4}(-)?[0-9]{4}$", credit_card)
        is not None
    )
    do_not_have_consecutive_digits: bool = (
        len(
            [
                group
                for group in [
                    "".join(g) for _, g in groupby(credit_card.replace("-", ""))
                ]
                if len(group) >= 4
            ]
        )
        == 0
    )

    return (
        "Valid"
        if (
            is_valid_start_digit
            and is_valid_size
            and is_valid_format
            and do_not_have_consecutive_digits
        )
        else "Invalid"
    )


if __name__ == "__main__":
    rows: int = int(input())

    [print(is_valid(input())) for _ in range(rows)]
