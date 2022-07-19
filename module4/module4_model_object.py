from abc import ABC, abstractmethod
from typing import Optional
import pandas as pd
import numpy as np

from module4_eda_cleaning import EDACleaning


class BaseModel:
    def __init__(self, filename: str):
        self.df = self._load_file(filename)
        self.cleaner = EDACleaning()

    def _load_file(self, filename: str) -> pd.DataFrame:
        """Load file from filename and set target field
        Args:
            filename: filename in csv format
        Returns:
            pd.DataFrame: df loaded from file
        """
        return pd.read_csv(filename, on_bad_lines="skip")

    def set_target(self, target: str):
        """Sets model target field
        Args:
            target: target field for model
        """
        self.target = target
        self.cleaner._set_target(target)

    def print_statistics(self):
        """Print basic statistics for data"""
        self.cleaner.print_statistics(self.df)

    @abstractmethod
    def split_data(self, stratify: Optional[bool]):
        pass

    @abstractmethod
    def basic_regression(self):
        pass
