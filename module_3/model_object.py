from abc import ABC, abstractmethod
from typing import Optional
import pandas as pd
import numpy as np


class BaseModel(ABC):
    def __init__(self, filename: str, target: str):
        self.df = self._load_file(filename)
        self.target = target

    def _load_file(self, filename: str) -> pd.DataFrame:
        """Load file from filename and set target field

        Args:
            filename (str): filename in csv format
        """
        return pd.read_csv(filename, on_bad_lines="skip")

    def print_statistics(self):
        """Print basic dataframe statistics"""
        print(self.df.head())
        print(f"DF shape: {self.df.shape}\n")
        print(f"Data types: {self.df.dtypes}\n")
        print(f"Describe: {self.df.describe()}\n")
        print(f"isna sum: {self.df.isna().sum()}\n")

    @abstractmethod
    def split_data(self, stratify):
        pass

    @abstractmethod
    def basic_regression(self):
        pass
