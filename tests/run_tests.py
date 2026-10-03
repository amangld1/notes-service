"""Runs the tests and prints one normalised line: TESTS: passed/total."""
import sys
import unittest
from pathlib import Path

root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(root))

suite = unittest.defaultTestLoader.discover(str(root / "tests"), top_level_dir=str(root))
result = unittest.TextTestRunner(stream=sys.stderr, verbosity=1).run(suite)

total = result.testsRun
failed = len(result.failures) + len(result.errors)
print(f"TESTS: {total - failed}/{total}")
sys.exit(0 if result.wasSuccessful() and total > 0 else 1)
