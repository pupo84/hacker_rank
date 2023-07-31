# import textwrap


def wrap(string, max_width):
    wraped = []
    partial = ""
    counter = 0

    for idx, s in enumerate(string):
        partial += s
        counter += 1

        if counter == max_width or idx == len(string) - 1:
            wraped.append(partial)
            counter = 0
            partial = ""

    return "\n".join(wraped)
    # return "\n".join(textwrap.wrap(string, max_width)) easy way


if __name__ == "__main__":
    string, max_width = input(), int(input())
    print(wrap(string, max_width))
