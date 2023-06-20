fields = [
    "source", "date", "number", "descripton", "destination", "value"
]

otpsmart = {
    "languages": {
        "uk": [
            ("Номер рахунку/картки", "B1"),
            ("Тип операції", "B2"),
            ("Дата здійснення операції", "B3"),
            ("Дата обробки операції в банку", "B4"),
            ("Опис операції", "B5"),
            ("Сума операції", "B6"),
            ("Валюта операції", "B7"),
            ("Сума операції в валюті рахунку", "B8"),
            ("Валюта рахунку", "B9"),
            ("Код категорії підприємства", "B10"),
        ],
        "en": [
            ("Account/card number", "B1"),
            ("Transaction type", "B2"),
            ("Transaction date", "B3"),
            ("Date of transaction processing in the bank", "B4"),
            ("Transaction description", "B5"),
            ("Transaction amount", "B6"),
            ("Transaction currency", "B7"),
            ("Transaction amount in account currency", "B8"),
            ("Account currency", "B9"),
            ("Code of enterprise type", "B10"),
        ]
    },
    "mapping": {
        "source_account": "{B1}",
        "date": "{B3:%d.%m.%Y}",
        "number": "{B3}",
        "description": "{B5}",
        "destination": "<internal>",
        "value": ["{B8}", "{B6}"],  # Set with first not None value
    }
}
