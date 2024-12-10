# pylint: disable=C0115, C0116, C0103
"""
Advent of Code 2024, Day 3
"""
import re

def read_input(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    input = ""
    for line in lines:
        input += line
    return input

def question_one(input: str):
    mul_iter = re.finditer("mul\(\d+,\d+\)", input)
    valid_mul_indices = [m.start(0) for m in mul_iter]
    result = 0
    for index in valid_mul_indices:
        x = input.find("(", index)
        y = input.find(",", x)
        z = input.find(")", y)
        num1 = input[x + 1:y]
        num2 = input[y + 1:z]
        result += (int(num1) * int(num2))
    return result

def question_two(input: str):
    mul_iter = re.finditer("mul\(\d+,\d+\)", input)
    valid_mul_indices = [m.start(0) for m in mul_iter]
    do_iter = re.finditer("do\(\)", input)
    valid_do_indices = [m.start(0) for m in do_iter]
    dont_iter = re.finditer("don't\(\)", input)
    valid_dont_indices = [m.start(0) for m in dont_iter]
    # Change lists to sets for O(1) checking
    valid_mul_indices = set(valid_mul_indices)
    valid_do_indices = set(valid_do_indices)
    valid_dont_indices = set(valid_dont_indices)
    do_enabled = True
    result = 0
    for i in range(0, len(input)):
        if i in valid_dont_indices:
            do_enabled = False
        if i in valid_do_indices:
            do_enabled = True
        if do_enabled and i in valid_mul_indices:
            x = input.find("(", i)
            y = input.find(",", x)
            z = input.find(")", y)
            num1 = input[x + 1:y]
            num2 = input[y + 1:z]
            result += (int(num1) * int(num2))
    return result

def main():
    input = read_input("input.txt")
    print(question_one(input))
    print(question_two(input))


if __name__ == "__main__":
    main()
