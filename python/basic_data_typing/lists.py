# https://www.hackerrank.com/challenges/python-lists/problem
from typing import List


def commands(size: int) -> List[List[str]]:
    cmds: List[List[str]] = []

    for _ in range(size):
        instruction: str = input()
        cmds.append(instruction.split(" "))

    return cmds


def process(cmds: List[List[str]]) -> None:
    arr: List[int] = []
    for cmd in cmds:
        instruction = cmd[0]
        if instruction == "insert":
            arr.insert(int(cmd[1]), int(cmd[2]))
        elif instruction == "append":
            arr.append(int(cmd[1]))
        elif instruction == "remove":
            arr.remove(int(cmd[1]))
        elif instruction == "sort":
            arr.sort()
        elif instruction == "pop":
            arr.pop()
        elif instruction == "reverse":
            arr.reverse()
        else:
            print(arr)


if __name__ == "__main__":
    cmds = commands(int(input()))
    process(cmds)
