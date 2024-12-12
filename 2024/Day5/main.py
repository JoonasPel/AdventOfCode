# pylint: disable=C0115, C0116, C0103
"""
Advent of Code 2024, Day 5
"""

def read_input(filename):
    orders: dict[int, set[int]] = {}
    updates = []
    with open(filename, "r") as file:
        for line in file:
            if line == "\n":
                break
            line = line.strip("\n")
            numbers = list(map(int, line.split("|")))
            if numbers[0] not in orders:
                orders[numbers[0]] = {numbers[1]}
            else:
                orders[numbers[0]].add(numbers[1])
        for line in file:
            line = line.strip("\n")
            numbers = list(map(int, line.split(",")))
            updates.append(numbers)
    return updates, orders

def valid_update(update, orders):
    prev_numbers = []
    for number in update:
        for prev_num in prev_numbers:
            if number in orders and prev_num in orders[number]:
                return False
        prev_numbers.append(number)
    return True

def question_one(updates, orders):
    result = 0
    for update in updates:
        if valid_update(update, orders):
            result += update[len(update) // 2]
    return result

def main():
    updates, orders = read_input("input.txt")
    print(question_one(updates, orders))


if __name__ == "__main__":
    main()
