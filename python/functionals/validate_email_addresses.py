# https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem
from typing import List
import re


def fun(email: str) -> bool:
    return (
        re.match(r"^[a-zA-Z0-9_%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,3}$", email) is not None
    )


def filter_mail(emails: List[str]) -> List[str]:
    return list(filter(fun, emails))


if __name__ == "__main__":
    n = int(input())
    emails = []

    for _ in range(n):
        emails.append(input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)
