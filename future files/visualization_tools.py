import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
from scipy.stats import norm
from statsmodels.tsa.stattools import adfuller

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler, PolynomialFeatures


class VisualizationTool():

    def __init__(self, target):
        self.target = target
        pass

    def basic_hist(self, df):
        df.hist(figsize=(18,15), bins='auto')
    
    def hist_norm_prob(self, df, field:str):
        sns.distplot(df[field], fit=norm)
        fig = plt.figure()
        res = stats.probplot(df[field], plot=plt)
        print("Skewness: %f" % df[field].skew())
        print("Kurtosis: %f" % df[field].kurt())
    
    def scatter(self, df, x, y, color):
        # plotting latitude and longitude as a visual scatter plot to look for location outliers

        plt.figure(figsize=(25,25))

        sns.scatterplot(data=df, x=x, y=y, hue=color, palette="magma_r");

    def time_series_plot(self, df, date_field):

        time_series_df = df.copy()

        # make a new df with just the date and price
        time_series_df = time_series_df[[date_field, self.target]]

        # convert our date field to a proper datetime
        time_series_df[date_field] = pd.to_datetime(time_series_df[date_field])

        # set the date as our index
        time_series_df.set_index(date_field, inplace=True)

        # group our data by day
        self.grouped_time_series_df = time_series_df.groupby(pd.Grouper(freq='D')).mean()

        # backfill any empty days by getting previous day's mean
        self.grouped_time_series_df.bfill(inplace=True)

        # find the rolling mean and rolling standard deviation
        roll_mean = self.grouped_time_series_df.rolling(window=10, center=False).mean()
        roll_std = self.grouped_time_series_df.rolling(window=10, center=False).std()

        # plot the figure with rolling mean and standard deviation
        fig = plt.figure(figsize=(12,7))
        plt.plot(self.grouped_time_series_df, color='blue', label='Original')
        plt.plot(roll_mean, color='red', label='Rolling Mean')
        plt.plot(roll_std, color='black', label = 'Rolling Std')
        plt.legend(loc='best')
        plt.title('Rolling Mean & Standard Deviation')
        plt.show(block=False)

        self.dickey_fuller()

    def dickey_fuller(self):
        dftest = adfuller(self.grouped_time_series_df)

        # Extract and display test results in a user friendly manner
        dfoutput = pd.Series(dftest[0:4], index=['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])
        for key,value in dftest[4].items():
            dfoutput['Critical Value (%s)'%key] = value

        print ('Results of Dickey-Fuller test: \n')
        print(dfoutput)

    def correlation_heat_map(self, df):

        # look for multicollinearity of features
        fig, ax = plt.subplots(figsize=(20, 20))

        # get the correlations for our train data
        correlated_data = df.corr()

        # we want our heatmap to not show the upper triangle, which is redundant data
        # get a mask for the upper diagonal
        correlated_data_mask = np.triu(np.ones_like(correlated_data, dtype=np.bool))

        # adjust mask and df to hide center diagonal
        correlated_data_mask = correlated_data_mask[1:, :-1]
        corr = correlated_data.iloc[1:,:-1].copy()

        # color map
        cmap = sns.diverging_palette(220, 20, as_cmap=True)

        # plot heatmap
        sns.heatmap(corr, mask=correlated_data_mask, annot=True, fmt=".2f", cmap=cmap,
            vmin=-1, vmax=1, cbar_kws={"shrink": .8}, square=True)

        # title
        plt.title('PEARSON CORRELATION MATRIX', fontsize=18)

        plt.show()
    
    def check_polynomial(self, df, field):
        yearly_prices = df.groupby(field)[self.target].mean()

        plt.scatter(yearly_prices.index, yearly_prices)
        plt.title("Linearity check")
        plt.xlabel(f"{field}")
        plt.ylabel(f"{self.target}")
        plt.show()

    def visualize_categoricals(self, df, categoricals):

        # make our categorical data frame to work with
        df_categoricals = df[categoricals]

        # telling Pandas that these columns are categoricals
        for item in df_categoricals.columns:
            df_categoricals[item] = df_categoricals[item].astype('category')

        # temporarily adding price to our dataframe so that we can do some visualizations    
        df_categoricals[self.target] = df[self.target]

        # plot our categoricals as box plots vs price
        def boxplot(x, y, **kwargs):
            sns.boxplot(x=x, y=y)
            x=plt.xticks(rotation=90)

        #visualization categories
        f = pd.melt(df_categoricals, id_vars=[self.target], value_vars=categoricals)
        g = sns.FacetGrid(f, col="variable",  col_wrap=2, sharex=False, sharey=False, size=5)
        g = g.map(boxplot, "value", self.target)

        df_categoricals.drop(self.target, axis=1, inplace=True)

    def visualize_continuous(self, df, continuous):

        # make our continuous frame to work with
        x_continuous = df[continuous]
        x_continuous[self.target] = df[self.target]

        def boxplot(x, y, **kwargs):
            sns.boxplot(x=x, y=y)
            x=plt.xticks(rotation=90)

        f = pd.melt(x_continuous, id_vars=[self.target], value_vars=continuous)
        g = sns.FacetGrid(f, col="variable",  col_wrap=2, sharex=False, sharey=False, size=5)
        g = g.map(boxplot, "value", self.target)

    def visualize_scatters(self, df, continuous):

        x_continuous = df[continuous]
        x_continuous[self.target] = df[self.target]

        # plot our larger continuous as scatter plots vs price
        large_cont = ['sqft_living', 'sqft_living15', 'sqft_lot', 'sqft_basement', 'zip_smooth', 'year_smooth', 'month_smooth', 'lat_long']

        fig, axes = plt.subplots(nrows=4, ncols=2, figsize=(15,25), sharey=True)

        for ax, column in zip(axes.flatten(), large_cont):
            ax.scatter(x_continuous[column], x_continuous[self.target], label=column, alpha=.1)
            ax.set_title(f'{self.target} vs {column}')
            ax.set_xlabel(column)
            ax.set_ylabel('{self.target}')

        fig.tight_layout()

        x_continuous.drop(self.target, axis=1, inplace=True)
    
    def _plot_polys(self, y, xlabel, title):
        '''Takes in a y-axis, x-axis label, and title and plots with various polynomial levels
        ARGUMENTS:
        y axis variable values
        x-axis label
        visualization title'''
        x = y.index
    
        # express numbers as arrays and reshape
        y = np.array(y)
        x = np.array(x)
        x = x.reshape(-1, 1)
    
        # plot figure
        plt.figure(figsize=(16, 8))

        # standard linear regression
        linreg = LinearRegression()
        linreg.fit(x, y)

        # 2nd degree polynomial regression
        poly2 = PolynomialFeatures(degree=2)
        x_poly2 = poly2.fit_transform(x)
        poly_reg2 = LinearRegression()
        poly_reg2.fit(x_poly2, y)

        # third degree polynomial regression 
        poly3 = PolynomialFeatures(degree=3)
        x_poly3 = poly3.fit_transform(x)
        poly_reg3 = LinearRegression()
        poly_reg3.fit(x_poly3, y)

        # predict on x values
        pred = linreg.predict(x)
        pred2 = poly_reg2.predict(x_poly2)
        pred3 = poly_reg3.predict(x_poly3)

        # plot regression lines
        plt.scatter(x, y)
        plt.yscale('log')
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel('Average')
        plt.plot(x, pred, c='red', label='Linear regression line')
        plt.plot(x, pred2, c='yellow', label='Polynomial regression line 2')
        plt.plot(x, pred3, c='#a3cfa3', label='Polynomial regression line 3');

    def plot_polynomials(self, df, field):
        y = df.groupby(field)[self.target].mean()
        self._plot_polys(y, "Year Sold", "Year Sold Mean")