from dataclasses import dataclass
from model_object import BaseModel
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

class RegressionModel(BaseModel):

    def __init__(self, filename, target, seed=None):
        super().__init__(filename, target, seed)
        
    def linear_regression(self):
        """Performs linear regression on the dataset
        """
        pass

    def basic_hist(self):
        """Calls on the VisualizationTool to make a basic histogram
        """
        self.model_visuals.basic_hist(self.df)
    
    def hist_norm_prob(self):
        self.model_visuals.hist_norm_prob(self.df, self.target)
    
    def time_series_plot(self, date_field):
        self.model_visuals.time_series_plot(df=self.df, date_field=date_field)

    def scatter(self, x, y):
        self.model_visuals.scatter(df=self.df, x=x, y=y, color=self.target)
    
    def split_data(self, seed=None, stratify=False):
        if stratify:
            bins = np.linspace(self.target.min(), self.target.max()+.01, 5)
            y_binned = np.digitize(y, bins)
            x_train, x_test, y_train, y_test = train_test_split(self.df, self.target, test_size=0.15, random_state=self.randomstate, stratify=y_binned)
        else:
            x_train, x_test, y_train, y_test = train_test_split(self.df, self.target, test_size=0.15, random_state=self.randomstate)
        
        x_train.reset_index(inplace=True, drop=True)
        x_test.reset_index(inplace=True, drop=True)
        y_train.reset_index(inplace=True, drop=True)
        y_test.reset_index(inplace=True, drop=True)

