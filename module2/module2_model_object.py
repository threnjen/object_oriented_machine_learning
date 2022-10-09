import pandas as pd


class BaseModel:
    def __init__(self, filename):
        self.df = self._load_file(filename)
        self.target = None

    def _load_file(self, filename):
        """Load file from filename and set target field
        Args:
            filename: filename in csv format
        Returns:
            df loaded from file
        """
        return pd.read_csv(filename, on_bad_lines="skip")

    def set_target(self, target):
        """Sets model target field
        Args:
            target: target field for model
        """
        self.target = target

    def print_statistics(self):
        """Print basic dataframe statistics"""
        print(f"DF columns: {self.df.columns}\n")
        print(f"DF shape: {self.df.shape}\n")
        print(f"Data types: {self.df.dtypes}\n")
        print(f"Describe: {self.df.describe()}\n")
        print(f"isna sum: {self.df.isna().sum()}\n")
        print(self.df.head())
