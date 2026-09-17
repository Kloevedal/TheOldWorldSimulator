#!/usr/bin/env python3
"""Run the test suite.

    python3 run_tests.py              # quick tier: every test, small samples
    python3 run_tests.py --full       # large samples + whole-roster round robin
    python3 run_tests.py -k mirror    # only tests whose name matches
    python3 run_tests.py --gaps       # list the rules the engine does not simulate yet

The quick tier is what the pre-commit hook runs. Run --full after any major
addition: a new faction or unit batch, a new rule, or an engine change.
"""

from __future__ import annotations

import argparse
import os
import sys
import time
import unittest

ROOT = os.path.dirname(os.path.abspath(__file__))
TESTS = os.path.join(ROOT, "tests")


def print_gaps():
    sys.path[:0] = [ROOT, TESTS]
    import rule_catalogue as rc

    sources = rc.rule_sources()
    gaps = sorted(rule for rule in rc.NOT_SIMULATED if rule in sources)
    print(f"{len(gaps)} rules would matter in a duel but are not simulated yet:\n")
    for rule in gaps:
        where = sources[rule]
        more = f" (+{len(where) - 2} more)" if len(where) > 2 else ""
        print(f"  {rule:40} {', '.join(where[:2])}{more}")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--full", action="store_true",
                        help="large samples and the whole-roster round robin")
    parser.add_argument("-k", dest="patterns", action="append", default=[],
                        help="only run tests matching this substring (repeatable)")
    parser.add_argument("-v", "--verbose", action="store_true", help="list every test")
    parser.add_argument("--failfast", action="store_true", help="stop at the first failure")
    parser.add_argument("--gaps", action="store_true",
                        help="list rules that are not simulated yet, then exit")
    args = parser.parse_args(argv)

    if args.gaps:
        print_gaps()
        return 0

    # The tier is read when tests/support.py is imported, so set it first.
    os.environ["TOW_FULL_TESTS"] = "1" if args.full else "0"
    sys.path[:0] = [ROOT, TESTS]

    loader = unittest.TestLoader()
    if args.patterns:
        loader.testNamePatterns = [f"*{p}*" for p in args.patterns]
    suite = loader.discover(TESTS, top_level_dir=TESTS)

    tier = "full" if args.full else "quick"
    print(f"Running the {tier} tier ({suite.countTestCases()} tests)...", flush=True)
    started = time.perf_counter()
    result = unittest.TextTestRunner(
        verbosity=2 if args.verbose else 1, failfast=args.failfast, buffer=True
    ).run(suite)
    elapsed = time.perf_counter() - started

    status = "PASSED" if result.wasSuccessful() else "FAILED"
    print(f"\n{status} - {result.testsRun} tests, {len(result.failures)} failures, "
          f"{len(result.errors)} errors, {len(result.skipped)} skipped "
          f"in {elapsed:.1f}s ({tier} tier)")
    if not args.full and result.wasSuccessful():
        print("Run `python3 run_tests.py --full` before merging a major addition.")
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(main())
