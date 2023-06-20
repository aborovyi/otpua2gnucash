import pathlib
import pytest

from otpua2gnucash import StatementReader


def test_statement_file_opens():
    """
    Verify statement file exists
    """
    test_dir = pathlib.Path(__file__).parent
    test_file = test_dir / "test.xls"
    r = StatementReader(test_file)
    assert r is not None


def test_statement_file_doesnt_exist():
    """
    Verify exception on missing statement file 
    """
    test_dir = pathlib.Path(__file__).parent
    test_file = test_dir / "no-such-file.xls"
    with pytest.raises(FileNotFoundError):
        StatementReader(test_file)


def test_read_statement_content():
    """
    Verify statement file records are read
    """
    test_dir = pathlib.Path(__file__).parent
    test_file = test_dir / "test.xls"
    r = StatementReader(test_file)
    recs = r.read_records()
    assert len(recs) > 0
