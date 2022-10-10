from module5.module5_model_object import BaseModel
from typing import Optional


class RegressionModel(BaseModel):
    def __init__(self, filename: str):
        super().__init__(filename)

    def basic_regression(self):
        """basic linear regression"""
        pass

    def split_data(self, stratify: Optional[bool] = True):
        """train_test_split data"""
        pass
