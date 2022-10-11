import pandas as pd
import numpy as np
from typing import Literal, Optional


class EDACleaning:
    def __init__(self):
        pass

    def set_target(self, target: str):
        """set model target variable"""
        self.target = target

    def print_statistics(self, df: pd.DataFrame) -> None:
        """Print basic dataframe statistics"""
        print(df.head())
        print(f"DF shape: {df.shape}\n")
        print(f"Data types: {df.dtypes}\n")
        print(f"Describe: {df.describe()}\n")
        print(f"isna sum: {df.isna().sum()}\n")

    def print_sorted(
        self,
        df: pd.DataFrame,
        field: str,
        groupby: Optional[str],
        asc: bool,
    ) -> None:
        if groupby:
            print(df.groupby(groupby)[field].mean().sort_values(ascending=asc))
        else:
            print(df.sort_values(field, ascending=asc).head())

    def check_value_proportions(self, df: pd.DataFrame, field: str) -> None:
        print(df[field].value_counts(normalize=True).head())

    def find_outliers(self, df: pd.DataFrame, field: str) -> None:
        find_outliers = df.groupby(field)[self.target].describe()
        outlier_report = find_outliers.sort_values("mean", ascending=False).head(20)
        print(outlier_report)

    def drop_dupes(self, df: pd.DataFrame, subset: list = None) -> pd.DataFrame:
        if subset:
            df.drop_duplicates(subset, keep="last", inplace=True)
        else:
            df.drop_duplicates(inplace=True)
        return df

    def remove_outliers(
        self, df: pd.DataFrame, fields: list, method: str, range: float
    ) -> pd.DataFrame:
        if method == "iqr":
            for field in fields:
                lower_range, upper_range = self._calculate_iqr(df[field], range)
                df = df.drop(
                    df[(df[field] > upper_range) | (df[field] < lower_range)].index
                )
        return df

    def _calculate_iqr(self, column: pd.Series, range: float) -> Literal(float, float):
        """return the lower range and upper range for the data based on IQR
        Arguments:
        column - column to be evaluated
        iqr_level - iqr range to be evaluated
        """
        Q1, Q3 = np.percentile(column, [25, 75])
        iqr = Q3 - Q1
        lower_range = Q1 - (range * iqr)
        upper_range = Q3 + (range * iqr)
        return lower_range, upper_range
