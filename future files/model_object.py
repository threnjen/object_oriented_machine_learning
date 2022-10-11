from abc import ABC, abstractmethod
from typing import Optional
import pandas as pd
import numpy as np

from core.visualization_tools import VisualizationTool
from core.eda_cleaning import EDACleaning
from core.feature_engineering import FeatureEngineer


class BaseModel(ABC):
    def __init__(self, filename: str, seed: Optional[int] = None):
        self.df = self._load_file(filename)
        if seed:
            np.random.seed(seed)
            self.randomstate = np.random.random(1)
        else:
            self.randomstate = np.random.random(1)
        self.cleaner = EDACleaning(target)
        self.model_visuals = VisualizationTool(target)
        self.feature_engineer = FeatureEngineer(target)

    def _load_file(self, filename: str) -> pd.DataFrame:
        """Load file from filename and set target field
        Args:
            filename (str): filename in csv format
        Returns:
            pd.DataFrame: df loaded from file
        """
        return pd.read_csv(filename, on_bad_lines="skip")

    def set_target(self, target: str):
        """Sets model target field
        Args:
            target (str): target: target field for model
        """
        self.target = target
        self.cleaner.set_target(target)

    def print_statistics(self):
        """Print basic statistics for data"""
        self.cleaner.print_statistics(self.df)

    def drop_dupes(self, subset: list = None):
        self.df = self.cleaner.drop_dupes(self.df, subset)

    def remove_outliers(
        self, fields: list = [], method: str = "iqr", range: float = 1.5
    ):
        self.df = self.cleaner.remove_outliers(self.df, fields, method, range)

    def print_sorted(self, field=None, asc: bool = False, groupby=None):
        if not field:
            field = self.target
        self.cleaner.print_sorted(df=self.df, field=field, asc=asc, groupby=groupby)

    def check_value_proportions(self, field=None):
        if not field:
            field = self.target
        self.cleaner.check_value_proportions(self.df, field)

    def reset_df_index(self):
        print(self.df.head())
        self.df = self.cleaner.reset_df_index(self.df)
        print(self.df.head())

    def log_target(self):
        self.target = self.feature_engineer.log_target(self.df, self.target)

    def turn_field_binary(self, field, new_name):
        self.df = self.feature_engineer.turn_field_binary(self.df, field, new_name)
        print(self.df.head())

    @abstractmethod
    def split_data(self, stratify: Optional[bool]):
        pass

    @abstractmethod
    def basic_regression(self):
        pass
