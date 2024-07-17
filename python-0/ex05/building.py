import sys


def count_chars(input: str):
    """simple funtion to count each type of characters on the string and print it in an ordely manner"""
    upper_letters = 0
    lower_letters = 0
    puctuation = 0
    spaces = 0
    digits = 0
    total = 0
    for i in input:
        total += 1
        if i.isdigit():
            digits += 1
        elif i.isspace():
            spaces += 1
        elif i.islower():
            lower_letters += 1
        elif i.isupper():
            upper_letters += 1
        else:
            puctuation += 1
    print(f"the text contains {total} characters:")
    print(f"{upper_letters} upper letters")
    print(f"{lower_letters} lower letters")
    print(f"{puctuation} puntuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main():
    try:
        if len(sys.argv) == 1:
            argument = input("please provide a string to count")
        elif len(sys.argv) == 2 and not sys.argv[1]:
            argument = input("please enter a string to count")
        elif len(sys.argv) == 2:
            argument = sys.argv[1]
        else:
            raise AssertionError("invalid arguments")
        count_chars(argument)
    except AssertionError as error:
        print(error)


if __name__ == "__main__":
    main()
