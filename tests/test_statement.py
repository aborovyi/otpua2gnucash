import pytest
import datetime

from otpua2gnucash.core import StatementRecord


def test_statement_record_empty():
    """
    Verify no exceptions if no data passed to the StatementRecord
    """
    StatementRecord()


def test_statement_record_complete_via_kwargs():
    """
    Verify complete data passed as dict doesn't cause any issues
    """
    data_dict = {
        "source_account": "111",
        "date": datetime.datetime.now().date(),
        "number": datetime.datetime.now(),
        "description": "demo",
        "destination": "222",
        "src_value": 4.5,
        "dst_value": 4.5,

    }
    StatementRecord(**data_dict)


def test_statement_record_complete_via_args():
    """
    Verify complete data passed via args doesn't cause any issues
    """
    rec = StatementRecord(
        source_account="111",
        date=datetime.datetime.now().date(),
        number=datetime.datetime.now(),
        description="demo",
        destination="222",
        src_value=4.5,
        dst_value=4.5,
    )
    assert rec.source_account == "111"
