# pylint: disable=C0115, C0116, C0103
"""
Advent of Code 2024, Day 2
"""

def read_input(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    reports = []
    for line in lines:
        report = list(map(int, line.split()))
        reports.append(report)
    return reports

def is_safe_question_one(report):
    if len(report) < 2:  # trivial
        return True
    increasing = report[0] < report[1]
    for i in range(0, len(report) - 1):
        diff = abs(report[i + 1] - report[i])
        if diff > 3 or diff < 1:
            return False
        temp_increasing = report[i] < report[i + 1]
        if increasing != temp_increasing:
            return False
    return True

def analyze_reports(reports):
    total_safe_reports = 0
    for report in reports:
        if is_safe_question_one(report):
            total_safe_reports += 1
    print(total_safe_reports)


def main():
    reports = read_input("input.txt")
    analyze_reports(reports)


if __name__ == "__main__":
    main()
