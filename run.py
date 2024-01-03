#! /bin/python3

import argparse
import time
import traceback
from datetime import datetime, timedelta, timezone
from importlib import import_module, reload


def run(func, lines):
    start = time.monotonic_ns()
    print(func(lines))
    end = time.monotonic_ns()
    print(f"[{(end-start) / 10**6:.3f} ms]")

if __name__ == "__main__":
    now = datetime.now()
    parser = argparse.ArgumentParser(description="Run Advent of Code solutions.")
    parser.add_argument("--year", "-y", type=int, help="The year to run.", default=now.year)
    parser.add_argument("--day", "-d", type=int, help="The day to run.", default=now.day)
    parser.add_argument("--sample", "-s", help="Run solution with sample data.", action="store_true")
    args = parser.parse_args()

    if args.sample:
        input_paths = [f"{args.year}/input/{args.day}.sample1",
                       f"{args.year}/input/{args.day}.sample2"]
    else:
        input_paths = [f"{args.year}/input/{args.day}.data",
                       f"{args.year}/input/{args.day}.data"]

    module_name = f"{args.year}.{args.day}"
    module = import_module(module_name)

    for i, func in enumerate(["p1", "p2"]):
        if not hasattr(module, func):
            continue
        with open(input_paths[i]) as f:
            data = f.read().strip()
        lines = [x for x in data.split("\n")]

        print(f"--- {func} ---")
        run(getattr(module, func), lines)
