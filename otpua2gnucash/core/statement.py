"""
Storage for statement-related data
"""


class Statement:
    """
    Container for statement parsed from a file
    """
    def __init__(self, **kwargs):
        pass


class StatementRecord:
    """
    Container for individual statement records
    """

    fields = [
        "source",  # Initial account for manipulations
        "date",  # Operation date
        "number",  # Operation number
        "descripton",  # More details on operation
        "destination",  # Target account were assets move to
        "src_value",  # Amount in the initial account's currency
        "dest_value",  # Amount in the target account's currency
    ]

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            if k not in self.fields:
                raise AttributeError("Got the unsupported field: '{k}'")
            self.__setattr__(k, v)
