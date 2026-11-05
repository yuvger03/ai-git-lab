"""Command-line interface: python -m gradebook <command> <csv file>."""

import argparse

from .grades import final_grade, letter_grade, passed
from .loader import load_students
from .stats import mean, median


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="gradebook", description="Course grade reports.")
    commands = parser.add_subparsers(dest="command", required=True)

    report = commands.add_parser("report", help="final grade, letter and result per student")
    report.add_argument("csv_file")

    stats = commands.add_parser("stats", help="course statistics")
    stats.add_argument("csv_file")

    return parser


def cmd_report(args: argparse.Namespace) -> int:
    students = load_students(args.csv_file)
    print(f"{'Student':<10} {'Final':>6}  Letter  Result")
    for student in students:
        grade = final_grade(student.scores)
        result = "pass" if passed(grade) else "FAIL"
        print(f"{student.name:<10} {grade:>6.1f}  {letter_grade(grade):^6}  {result}")
    return 0


def cmd_stats(args: argparse.Namespace) -> int:
    grades = [final_grade(student.scores) for student in load_students(args.csv_file)]
    pass_rate = sum(passed(grade) for grade in grades) / len(grades)
    print(f"Students:  {len(grades)}")
    print(f"Mean:      {mean(grades):.1f}")
    print(f"Median:    {median(grades):.1f}")
    print(f"Pass rate: {pass_rate:.0%}")
    return 0


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "report":
        return cmd_report(args)
    return cmd_stats(args)
