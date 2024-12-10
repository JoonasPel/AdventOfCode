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

def main():
    input = read_input("input.txt")
    print(question_one(input))


if __name__ == "__main__":
    main()
