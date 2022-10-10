from abc import ABC, abstractmethod
from typing import Optional
import pandas as pd
import numpy as np

from module5.module5_eda_cleaning import EDACleaning


class BaseModel(ABC):
    def __init__(self, filename: str, seed: Optional[int] = None):
        self.df = self._load_file(filename)
        self.target = None
        if seed:
            np.random.seed(seed)
            self.randomstate = np.random.random(1)
        else:
            self.randomstate = np.random.random(1)
        self.cleaner = EDACleaning()

    def _load_file(self, filename: str) -> pd.DataFrame:
        """Load file from filename and set target field
        Args:
            filename (str): filename in csv format
        Returns:
            pd.DataFrame: df loaded from file
        """
        return pd.read_csv(filename, on_bad_lines="skip")

    def set_target(self, target: str) -> None:
        """Sets model target field
        Args:
            target (str): target: target field for model
        """
        self.target = target
        self.cleaner.set_target(target)

    def _set_save(self, saved: str) -> None:
        """Sets a save point on the dataframe before performing an alteration task

        Args:
            saved (str): description of saved task to report if undone
        """
        self.saved_df = self.df.copy()
        self.saved_action = saved

    def undo(self) -> None:
        """Undoes the last data frame alteration task, and reports on Undo"""
        self.df = self.saved_df()
        print(f"Undid last change: {self.saved_action}")

    def print_statistics(self) -> None:
        """Print basic statistics for data"""
        self.cleaner.print_statistics(self.df)

    def print_sorted(
        self,
        field: Optional[str] = None,
        groupby: Optional[str] = None,
        asc: Optional[bool] = False,
    ) -> None:
        """Prints sorted based on provided field. Will use target if no field provided.
        Args:
            field (_type_, optional): Will sort by this field. Defaults to target.
            asc (bool, optional): Sort ascending. Defaults to False.
            groupby (_type_, optional): If entered, will group by this field. Defaults to None.
        """
        if not field:
            field = self.target
        self.cleaner.print_sorted(df=self.df, field=field, asc=asc, groupby=groupby)

    def check_value_counts(self, field: Optional[str] = None) -> None:
        """Will print value counts for field
        Args:
            field (_type_, optional): Will report on this field. Defaults to target.
        """
        if not field:
            field = self.target
        self.cleaner.check_value_counts(self.df, field)

    def find_outliers(self, field: str) -> None:
        self.cleaner.find_outliers(field)

    def drop_dupes(self, subset: Optional[list] = None, save: Optional[bool] = True):
        """Save point, then drops duplicate dataframe rows
        Args:
            subset (list, optional): Subset on which to drop dupes. Defaults to None.
            save (boolean, optional): Toggles to save. Defaults to None.
        """
        if save:
            self._set_save("drop_dupes")
        self.df = self.cleaner.drop_dupes(self.df, subset)

    def remove_outliers(
        self,
        fields: list = [],
        method: Optional[str] = "iqr",
        range: Optional[float] = 1.5,
        save: Optional[bool] = True,
    ) -> None:
        """Save point, then removes outliers, defaultings to IQR with a default IQR range of 1.5
        Args:
            fields (list): list of fields. Must be list even if one item.
            method (str, optional): outlier removal method. Defaults to "iqr".
            range (float, optional): IQR range. Defaults to 1.5.
            save (boolean, optional): Toggles to save. Defaults to None.
        """
        if save:
            self._set_save("remove_outliers")
        self.df = self.cleaner.remove_outliers(self.df, fields, method, range)

    def reset_index(self, save: Optional[bool] = True) -> None:
        """Save point, then resets dataframe index"""
        print(self.df.head())
        if save:
            self._set_save("reset_index")
        self.df.reset_index(inplace=True, drop=True)
        print(self.df.head())

    @abstractmethod
    def split_data(self, stratify: Optional[bool]):
        pass

    @abstractmethod
    def basic_regression(self):
        pass
