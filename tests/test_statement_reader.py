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
    with pytest.raises(FileNotFoundError):
        StatementReader(test_file)


def test_read_statement_content():
    test_dir = pathlib.Path(__file__).parent
    test_file = test_dir / "test.xls"
    r = StatementReader(test_file)
    recs = r.read_records()
    assert len(recs) > 0
