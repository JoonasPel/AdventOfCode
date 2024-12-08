# pylint: disable=C0115, C0116, C0103
"""
Advent of Code 2024, Day 1
"""

def read_input(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    list1, list2 = [], []
    for line in lines:
        num1, num2 = map(int, line.split())
        list1.append(num1)
        list2.append(num2)
    return list1, list2

def first_question(list1, list2):
    list1, list2 = sorted(list1), sorted(list2)
    distance = 0
    for x, y in zip(list1, list2):
        distance += abs(x - y)
    print(distance)

def second_question(list1, list2):
    freqs = dict()
    for num in list2:
        if num in freqs:
            freqs[num] += 1
        else:
            freqs[num] = 1
    similarity = 0
    for num in list1:
        if num in freqs:
            similarity += num * freqs[num]
    print(similarity)

def main():
    test1, test2 = [3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3]
    list1, list2 = read_input("input.txt")
    first_question(list1, list2)
    second_question(list1, list2)


if __name__ == "__main__":
    main()
