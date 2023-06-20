"""
Config Mapper. This class class reads configuration for each statement and
creates a map between statement data and GnuCash internals
"""

from collections import OrderedDict
from typing import Optional
from otpua2gnucash.core import profiles, StatementRecord


class ConfigMapper():
    """
    Mapping class to transform incoming data into requested representation.
    """

    def __init__(self, name: str):
        """
        Initializes the class with the given configuration.
        """
        try:
            source = profiles.__getattribute__(name)
        except AttributeError as exc:
            raise ValueError(
                f"Request name '{name}' is not in profiles"
            ) from exc
        self.languages = source.get("languages")
        self.reverted_lang_map = self.__reorder_langs()
        self.map = source.get("mapping")

    def __reorder_langs(self):
        """
        Reorder locale values, to map field name to exact GnuCash value
        """
        res = {}
        for language in self.languages:
            for locale, field_no in self.languages[language]:
                if field_no not in res:
                    res[field_no] = [locale]
                else:
                    res[field_no].append(locale)
        return res

    def get_field_by_name(self, name) -> Optional[str]:
        """
        Detect field to which a record belongs
        """
        for key, value in self.reverted_lang_map.items():
            if name in value:
                return key
        return None

    def format_field(self, field_str: str, mapping: dict) -> list:
        """
        Extract a list of fields and formatting rules to apply to fields
        """
        if isinstance(field_str, list):
            tmp_res = []
            for itm in field_str:
                if isinstance(itm, list):
                    tmp_res.extend(
                        self.format_field(itm, mapping)
                    )
                else:
                    try:
                        tmp_res.append(itm.format(**mapping))
                    except KeyError:
                        tmp_res.append("")
            res = list(filter(lambda x: x != 'None', tmp_res))[0]
        else:
            try:
                res = field_str.format(**mapping)
            except KeyError:
                res = ""
        return res if res != "None" else ""

    def parse(self, data: OrderedDict) -> dict:
        """
        Parse the incoming data and put it into correct fields of
        StatementRecord
        """
        int_vars = {}

        # Detect field which must be assigned to the incoming key
        for key, val in data.items():
            target_field = self.get_field_by_name(key)
            int_vars[target_field] = val

        # Extract formatting rules
        final_data = {}
        for key, val in self.map.items():
            final_data[key] = self.format_field(val, int_vars)

        res = StatementRecord(**final_data)
        return res
