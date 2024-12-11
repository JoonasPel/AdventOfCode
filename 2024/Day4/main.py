# pylint: disable=C0115, C0116, C0103
"""
Advent of Code 2024, Day 4
"""
import numpy as np

def read_input(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    data = []
    for line in lines:
        separated = [*line]
        if separated[-1] == "\n":
            del separated[-1]
        data.append(separated)
    return np.asarray(data)

# Check all 8 directions from the "X" found and see if "MAS" is found
def traverse(i, j, data: np.ndarray):
    xmas_found = 0
    horizontal = data[i, j + 1:j + 4]
    if np.array_equal(horizontal, ["M", "A", "S"]):
        xmas_found += 1
    horizontal_rev = data[i, j - 3: j]
    if np.array_equal(horizontal_rev, ["S", "A", "M"]):
        xmas_found += 1
    vertical = data[i + 1:i + 4, j]
    if np.array_equal(vertical, ["M", "A", "S"]):
        xmas_found += 1
    vertical_rev = data[i - 3:i, j]
    if np.array_equal(vertical_rev, ["S", "A", "M"]):
        xmas_found += 1
    # top right diagonal
    if i >= 3 and j <= data.shape[1] - 4:
        if data[i - 1, j + 1] == "M" and data[i - 2, j + 2] == "A" and data[i - 3, j + 3] == "S":
            xmas_found += 1
    # top left diagonal
    if i >= 3 and j >= 3:
        if data[i - 1, j - 1] == "M" and data[i - 2, j - 2] == "A" and data[i - 3, j - 3] == "S":
            xmas_found += 1
    # bottom right diagonal
    if i <= data.shape[0] - 4 and j <= data.shape[1] - 4:
        if data[i + 1, j + 1] == "M" and data[i + 2, j + 2] == "A" and data[i + 3, j + 3] == "S":
            xmas_found += 1
    # bottom left diagonal
    if i <= data.shape[0] - 4 and j >= 3:
        if data[i + 1, j - 1] == "M" and data[i + 2, j - 2] == "A" and data[i + 3, j - 3] == "S":
            xmas_found += 1
    return xmas_found

# Sorry
def traverse2(i, j, data: np.ndarray):
    if i >= 1 and i <= data.shape[0] - 2 and j >= 1 and j <= data.shape[1] - 2:
        if ((data[i - 1, j - 1] == "M" and data[i + 1, j + 1] == "S") or
                (data[i - 1, j - 1] == "S" and data[i + 1, j + 1] == "M")):
            if ((data[i - 1, j + 1] == "M" and data[i + 1, j - 1] == "S") or
                    (data[i - 1, j + 1] == "S" and data[i + 1, j - 1] == "M")):
                return 1
    return 0


def question_one(data):
    total_xmas = 0
    for i, row in enumerate(data):
        for j, char in enumerate(row):
            if char == "X":
                total_xmas += traverse(i, j, data)
    return total_xmas

def question_two(data):
    total_xmas = 0
    for i, row in enumerate(data):
        for j, char in enumerate(row):
            if char == "A":
                total_xmas += traverse2(i, j, data)
    return total_xmas


def main():
    data = read_input("input.txt")
    print(question_one(data))
    print(question_two(data))


if __name__ == "__main__":
    main()
