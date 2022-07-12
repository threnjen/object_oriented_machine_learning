from dataclasses import dataclass
from model_object import BaseModel
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split


class RegressionModel(BaseModel):
    def __init__(self, filename, target, seed=None):
        super().__init__(filename, target, seed)

    def basic_regression(self):
        """basic linear regression"""
        pass

    def split_data(self):
        """train_test_split data"""
        pass
