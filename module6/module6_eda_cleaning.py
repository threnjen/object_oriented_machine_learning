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

    def check_value_counts(self, df: pd.DataFrame, field: str) -> None:
        print(df[field].value_counts(normalize=True).head())

    def find_outliers(self, field: str) -> None:
        find_outliers = self.df.groupby(field)[self.target].describe()
        find_outliers.sort_values("mean", ascending=False).head(20)

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

    def drop_feature(self, df, field):
        # drop multicollinear features and unneeded features
        df.drop([field], axis=1, inplace=True)

    def print_corr(self, df: pd.DataFrame):
        df.corr()

    def show_correlated_pairs(self, df: pd.DataFrame):
        # Get our list of highly correlated feature pairs with following steps:

        # save correlation matrix as a new data frame
        # converts all values to absolute value
        # stacks the row:column pairs into a multindex
        # reset the index to set the multindex to seperate columns
        # sort values. 0 is the column automatically generated by the stacking
        df_correlations = (
            df.corr().abs().stack().reset_index().sort_values(0, ascending=False)
        )

        # zip the variable name columns in a new column named "pairs"
        df_correlations["pairs"] = list(
            zip(df_correlations.level_0, df_correlations.level_1)
        )

        # set index to pairs
        df_correlations.set_index(["pairs"], inplace=True)

        # rename our results column to correlation
        df_correlations.rename(columns={0: "correlation"}, inplace=True)

        # Drop 1:1 correlations to get rid of self pairs
        df_correlations.drop(
            df_correlations[df_correlations["correlation"] == 1.000000].index,
            inplace=True,
        )

        # view pairs above 70% correlation and below 95% correlation (engineered features will correlate with each other above 95%)
        df_correlations[
            (df_correlations["correlation"] > 0.75)
            & (df_correlations["correlation"] < 0.95)
        ]

    def show_target_correlation(self, df):
        # Check out our variables correlationg with price
        df_correlations = (
            df.corr().abs().stack().reset_index().sort_values(0, ascending=False)
        )
        df_correlations.loc[df_correlations["level_0"] == self.target].sort_values(
            0, ascending=False
        )
