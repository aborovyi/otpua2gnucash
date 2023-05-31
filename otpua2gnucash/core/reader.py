"""
Reader for statements
"""
import pathlib
import logging
import pyexcel
import json


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

    def read_config(self, config_file: str | pathlib.Path = None):
        """
        Read a file that contains a configuration to parse the given statement
        """
        cfg = pathlib.Path(config_file)
        if not cfg.exists():
            raise FileNotFoundError(f"{cfg}")
        try:
            self.config = json.loads(cfg.read_text())
        except Exception as e:
            logging.error(e)

    def parse(self):
        """
        Parse the provided account statement, by groupping the incomming data 
        in the dict-like form:
            GNU_Book
              -> Account_name 
                -> (linked account)
                  -> operation date and time
                  -> operation description
                  -> operation amount (positive to increase account, negative to decrease)
                  -> operation currency
                  -> operation amount in account currency
                  -> account currency
        """
        


