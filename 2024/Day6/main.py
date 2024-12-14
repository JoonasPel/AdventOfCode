# pylint: disable=C0115, C0116, C0103
"""
Advent of Code 2024, Day 6
"""
from enum import Enum

Directions = Enum("Directions", [("UP", 0), ("RIGHT", 1), ("DOWN", 2), ("LEFT", 3)])

def read_input(filename):
    laboratory_map: list[list[chr]] = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip("\n")
            temp = [*line]
            laboratory_map.append(temp)
    return laboratory_map

def valid_position(laboratory_map, row, column):
    return 0 <= row < len(laboratory_map) and 0 <= column < len(laboratory_map[0])

def question_one(laboratory_map):
    current_row, current_column = -1, -1
    # find guard
    for i, row in enumerate(laboratory_map):
        for j, _ in enumerate(row):
            if row[j] == "^":
                current_row, current_column = i, j
    # traverse route
    distinct_positions: set[tuple[int, int]] = set()
    distinct_positions.add((current_row, current_column))  # Starting position
    current_direction = Directions.UP  # Starting direction
    while True:
        match current_direction:
            case Directions.UP:
                new_row = current_row - 1
                new_column = current_column
                new_direction = Directions.RIGHT
            case Directions.RIGHT:
                new_row = current_row
                new_column = current_column + 1
                new_direction = Directions.DOWN
            case Directions.DOWN:
                new_row = current_row + 1
                new_column = current_column
                new_direction = Directions.LEFT
            case Directions.LEFT:
                new_row = current_row
                new_column = current_column - 1
                new_direction = Directions.UP
        if not valid_position(laboratory_map, new_row, new_column):  # Went out of map
            break
        if laboratory_map[new_row][new_column] == "#":  # Blocked, need to turn
            current_direction = new_direction
        else:  # Not blocked, can move
            current_row, current_column = new_row, new_column
            distinct_positions.add((new_row, new_column))
    return len(distinct_positions)

def main():
    laboratory_map = read_input("input.txt")
    print(question_one(laboratory_map))


if __name__ == "__main__":
    main()
