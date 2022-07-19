import pandas as pd


class EDACleaning:
    def __init__(self):
        pass

    def _set_target(self, target):
        """set model target variable"""
        self.target = target

    def print_statistics(self, df):
        """Print basic dataframe statistics"""
        print(df.head())
        print(f"DF shape: {df.shape}\n")
        print(f"Data types: {df.dtypes}\n")
        print(f"Describe: {df.describe()}\n")
        print(f"isna sum: {df.isna().sum()}\n")
