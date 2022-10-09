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
        self.target = None
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
        """Drops duplicate dataframe rows
        Args:
            subset (list, optional): Subset on which to drop dupes. Defaults to None.
        """
        self.df = self.cleaner.drop_dupes(self.df, subset)

    def remove_outliers(
        self, fields: list = [], method: str = "iqr", range: float = 1.5
    ):
        """Removes outliers, defaultings to IQR with a default IQR range of 1.5
        Args:
            fields (list, optional): list of fields. Must be list even if one item.
            method (str, optional): outlier removal method. Defaults to "iqr".
            range (float, optional): IQR range. Defaults to 1.5.
        """
        self.df = self.cleaner.remove_outliers(self.df, fields, method, range)

    def print_sorted(self, asc: bool = False, field=None, groupby=None):
        """Prints sorted based on provided field. Will use target if no field provided.
        Args:
            asc (bool, optional): Sort ascending. Defaults to False.
            field (_type_, optional): Will sort by this field. Defaults to target.
            groupby (_type_, optional): If entered, will group by this field. Defaults to None.
        """
        if not field:
            field = self.target
        self.cleaner.print_sorted(df=self.df, field=field, asc=asc, groupby=groupby)

    def check_value_counts(self, field=None):
        """Will print value counts for field
        Args:
            field (_type_, optional): Will report on this field. Defaults to target.
        """
        if not field:
            field = self.target
        self.cleaner.check_value_counts(self.df, field)

    def reset_df_index(self):
        print(self.df.head())
        self.df.reset_index(inplace=True, drop=True)
        print(self.df.head())

    @abstractmethod
    def split_data(self, stratify: Optional[bool]):
        pass

    @abstractmethod
    def basic_regression(self):
        pass
