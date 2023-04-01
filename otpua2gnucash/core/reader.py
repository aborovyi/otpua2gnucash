"""
Reader for statements
"""
import pathlib
import logging


class StatementReader:
    """
    General class to read data from the file
    """

    def __new__(cls, statement_file: str | pathlib.Path = None):
        """
        Create a new instance of StatementReader.

        :arg statement_file: - Path to the file that contains a statement
        :returns: On success - an instance of StatementReader, None otherwise
        """
        tmp_path = pathlib.Path(statement_file)
        logging.info(tmp_path)
        if tmp_path.exists():
            cls.statement_file = tmp_path
            return cls
        return None

    def read(self):
        """
        Read data from the file
        """
