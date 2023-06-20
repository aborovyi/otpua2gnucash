#!/usr/bin/env python3
"""
Reader for statements
"""
import pathlib
import logging
import json
import os
import pyexcel


class StatementReader:
    """
    General class to read data from the file
    """

    instance = None

    def __init__(self, statement_file: str | pathlib.Path = None):
        """
        Create a new instance of StatementReader.

        :arg statement_file: - Path to the file that contains a statement
        :returns: On success - an instance of StatementReader, None otherwise
        """
        tmp_path = pathlib.Path(statement_file)
        logging.info(tmp_path)
        if not tmp_path.exists():
            raise FileNotFoundError(f"{tmp_path}")
        self.statement_file = tmp_path
        self.config = None

    def read_records(self):
        """
        Read data from the file
        """
        records = pyexcel.get_records(
            file_name=str(self.statement_file.resolve())
        )
        return records
