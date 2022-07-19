import pandas as pd

from module3_eda_cleaning import EDACleaning


class BaseModel:
    def __init__(self, filename):
        self.df = self._load_file(filename)
        self.cleaner = EDACleaning()

    def _load_file(self, filename):
        """Load file from filename and set target field
        Args:
            filename: filename in csv format
        Returns:
            pd.DataFrame: df loaded from file
        """
        return pd.read_csv(filename, on_bad_lines="skip")

    def set_target(self, target):
        """Sets model target field
        Args:
            target: target field for model
        """
        self.target = target
        self.cleaner._set_target(target)

    def print_statistics(self):
        """Print basic statistics for data"""
        self.cleaner.print_statistics(self.df)
