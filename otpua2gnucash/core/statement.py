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
        "source_account",  # Initial account for manipulations
        "date",  # Operation date
        "number",  # Operation number
        "description",  # More details on operation
        "destination",  # Target account were assets move to
        "src_value",  # Amount in the initial account's currency
        "dst_value",  # Amount in the target account's currency
    ]

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            if k not in self.fields:
                raise AttributeError(f"Got the unsupported field: '{k}'")
            self.__setattr__(k, v)

    # ADDME Logic to set field values according to the expected data

    def __eq__(self, other):
        return all(
            self.__getattribute__(f) == other.__getattribute__(f)
            for f
            in self.fields
        )

    def __repr__(self):
        """
        Internal representation
        """
        fields = []
        fields = [
            f"{f}={self.__getattribute__(f).__repr__()}" for f in self.fields
        ]
        output = f'<StatementRecord({", ".join(fields)})>'
        return output
