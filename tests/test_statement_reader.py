import pytest
import sys
import pathlib

from otpua2gnucash import StatementReader


def test_statement_file_opens():
    test_dir = pathlib.Path(__file__).parent
    test_file = test_dir / "test.xls"
    r = StatementReader(test_file)
    assert r is not None


def test_statement_file_doesnt_exist():
    test_dir = pathlib.Path(__file__).parent
    test_file = test_dir / "no-such-file.xls"
    r = StatementReader(test_file)
    assert r is None
