# https://www.hackerrank.com/challenges/string-validators/problem


def validators(string: str) -> None:
    print(any(x.isalnum() for x in string))
    print(any(x.isalpha() for x in string))
    print(any(x.isdigit() for x in string))
    print(any(x.islower() for x in string))
    print(any(x.isupper() for x in string))
