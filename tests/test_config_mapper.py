"""
Verify ConfigMapper functionality
"""
import pytest
import datetime
from collections import OrderedDict

from otpua2gnucash.core import ConfigMapper, StatementRecord


def test_class_initialization_valid():
    """
    Verify class initializes with the existing profile
    """
    mapper = ConfigMapper(name="otpsmart")
    assert mapper.map


def test_class_initialization_invalid():
    """
    Verify we get a ValueError if profile doesn't exist
    """
    with pytest.raises(
        ValueError,
        match="Request name 'doesnt_exist' is not in profiles"
    ):
        ConfigMapper(name="doesnt_exist")


def test_reorder_langs_fields_amount():
    """
    Verify reorder_langs parses all fields from self.languages
    """
    mapper = ConfigMapper(name="otpsmart")
    langs = list(k for k in mapper.languages.keys())
    assert len(mapper.reverted_lang_map) == len(mapper.languages[langs[0]])


def test_reorder_langs_langs_amount():
    """
    Verify each field contains data from all languages
    """
    mapper = ConfigMapper(name="otpsmart")
    langs = list(k for k in mapper.languages.keys())
    reordered_langs = mapper.reverted_lang_map
    assert all(
        len(field) == len(langs) for field in reordered_langs.values()
    )


@pytest.mark.parametrize(
    "src_field, dest_field",
    [
        ("Номер рахунку/картки", "B1"),
        ("Transaction amount", "B6"),
        ("Empty field", None)
    ],
    ids=["Ukrainian", "English", "Empty"]
)
def test_get_field_by_name(src_field, dest_field):
    """
    Verify 'get_field_by_name' detects field correctly.
    """
    mapper = ConfigMapper(name="otpsmart")
    res = mapper.get_field_by_name(src_field)
    assert res == dest_field


@pytest.mark.parametrize(
    "incoming_field, exp",
    [
        ("{B1}", "1"),
        ("{B3}", ""),
        (["{B2}", "{B3}"], "Test"),
        (["{B3}", "{B2}"], "Test"),
        ("{B4}", "")
    ],
    ids=[
        "1 item, valid", "1 item None",
        "List, first present", "List, first missing",
        "Invalid key"
    ]
)
def test_format_field(incoming_field, exp):
    """
    Verify 'format_field' parses correctly incoming data.
    """
    mapper = ConfigMapper(name="otpsmart")
    ns = {
        "B1": 1,
        "B2": "Test",
        "B3": None
    }
    res = mapper.format_field(incoming_field, ns)
    assert res == exp


def test_parse_correct_instance():
    """
    Verify a single Statement Record will be parsed correctly
    """
    data = OrderedDict(
        [
            ('Account/card number', '234567****1111'), 
            ('', ''), 
            ('Transaction type', 'операція за карткою'), 
            ('Transaction date', datetime.datetime(2023, 5, 26, 15, 21, 7)), 
            (
                'Date of transaction processing in the bank',
                datetime.date(2023, 5, 28)
            ),
            (
                'Transaction description', 
                'Покупка (Оплата цифровим токеном) NIKORA 272(SH001527)'),
            ('Transaction amount', -18.51),
            ('Transaction currency', 'GEL'),
            ('Transaction amount in account currency', -271.44),
            ('Account currency', 'UAH'),
            ('Code of enterprise type', '5411')
        ]
    )
    mapper = ConfigMapper(name="otpsmart")
    statement = mapper.parse(data)
    assert isinstance(statement, StatementRecord)


def test_parse_correct_data():
    """
    Verify a single Statement Record will be parsed correctly
    """
    data = OrderedDict(
        [
            ('Номер рахунку/картки', '234567*****1111'),
            ('', ''),
            ('Тип операції', 'операція за карткою'),
            (
                'Дата здійснення операції',
                datetime.datetime(2023, 3, 30, 14, 14, 12)
            ),
            ('Дата обробки операції в банку', datetime.date(2023, 3, 31)),
            (
                'Опис операції',
                'Покупка (Оплата цифровим токеном) NIKORA 479(SH019281)'
            ),
            ('Сума операції', -12.49),
            ('Валюта операції', 'GEL'),
            ('Сума операції в валюті рахунку', -184.95),
            ('Валюта рахунку', 'UAH'),
            ('Код категорії підприємства', '5499')
        ]
    )
    mapper = ConfigMapper(name="otpsmart")
    statement = mapper.parse(data)
    expected_data = StatementRecord(
        source_account="234567*****1111",
        date=datetime.datetime(2023, 3, 30),
        number=datetime.datetime(2023, 3, 30, 14, 14, 12),
        description='Покупка (Оплата цифровим токеном) NIKORA 479(SH019281)',
        destination="<internal>",
        src_value=-184.95,
        dst_value=-12.49,
    )
    assert statement == expected_data
