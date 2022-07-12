import pandas as pd
import numpy as np
import itertools

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, cross_validate, validation_curve, cross_val_score, GridSearchCV, KFold, RepeatedKFold
from sklearn.preprocessing import StandardScaler, PolynomialFeatures

class FeatureEngineer():

    def __init__(self, target):
        self.target = target

    def log_target(self, df) -> pd.DataFrame:
        return np.log(df[self.target])
    
    def log_continuous(self, df):
        return np.log(df)

    def scale_x_train(self, df):
        scaler = StandardScaler()
        scaled_df = pd.DataFrame(scaler.fit_transform(df),columns = df.columns)
        return scaled_df, scaler

    def scale_x_test(self, df, scaler):
        scaled_df = pd.DataFrame(scaler.transform(df),columns = df.columns)
        return scaled_df

    def turn_field_binary(self, df, field, new_name=None):
        df.loc[df[field] > 0, field] = 1
        df.loc[df[field] != 1, field] = 0
        if new_name:
            df.rename(columns={field : new_name}, inplace=True)
        return df

    # this function is by Max Halford at https://maxhalford.github.io/blog/target-encoding/
    def _calc_smooth_mean(self, df, by, on, m, target_df):
        '''Function returns a weighted mean value for the each member of a column.
        Arguments:
        df: The df being used to calculate the means
        by: the column being target encoded
        on: the thing to be encoded; almost always the learning target in this circumstance
        m: weight before moving toward global mean; usually a min # samples
        target_df: the target df for the mean encoding. Could be same as df or different.'''
        # Compute the global mean
        mean = df[on].mean() 

        # Compute the number of values and the mean of each group
        agg = df.groupby(by)[on].agg(['count', 'mean'])  
        counts = agg['count']
        means = agg['mean']

        # Compute the "smoothed" means
        smooth = (counts * means + m * mean) / (counts + m)

        # Replace each value by the according smoothed mean
        return round(target_df[by].map(smooth), 0) 

    def target_encoding(self, x_train, x_test, encoding_target):
        # Adding target encoding, which we will opt to try instead of one-hot with a few models

        # get size of training data
        num_of_samples = x_train.shape[0]

        # determining minimum number of samples for encoding_target to use their
        # own mean rather than expanding into the full data set mean 
        encoding_samples = num_of_samples/x_train[encoding_target].unique().shape[0]

        # create smooth additive encoded variables for encoding target
        x_train[f"{encoding_target}_smooth"] = self._calc_smooth_mean(x_train, encoding_target, self.target, encoding_samples, x_train)
        x_test[f"{encoding_target}_smooth"] = self._calc_smooth_mean(x_train, encoding_target, self.target, encoding_samples, x_test)

        return x_train, x_test

    def make_category_bins(self, df, categoricals):

        bin_threshold = df.shape[0]*.10

        for category in categoricals:
            if len(df[category].nunique() > bin_threshold):
                df[f"{category}_binned"] = pd.qcut(df[category], q=bin_threshold, labels=np.array(range(1,bin_threshold+1)))
        
        return df
    
    def one_hot_categories(self, df, categoricals):

        df_cats_train = pd.get_dummies(df[categoricals], prefix=categoricals, drop_first=True)
        
        return df_cats_train

    def test_feature_combinations(target_values, variables):
    
        """Function takes in target price and a dataframe of independent variables, and 
        tests model improvement for each combination of variables
        ARGUMENTS:
        Y of target values
        X-dataframe of continuous features
        Returns dataframe of score improvements over base score for each interaction combination"""

        randomstate = np.random()
    
        # select our estimator and our cross validation plan
        regression = LinearRegression()
        cv = RepeatedKFold(n_splits=5, n_repeats=2, random_state=1)
    
        # prepare our scoring dataframe
        scoring_df = pd.DataFrame()
    
        # prepare our lists to store our features and scores as we iterate
        scores = []
        feature1 = []
        feature2 = []
    
        # Get a list of all of our features, and remove our target variable 'price' from the list
        features = list(variables.columns)

        # make a list of all of our possible feature combinations
        feature_combos = itertools.combinations(features, 2)
        feature_combos = list(feature_combos)
    
        # set our y-value as our target variable
        y = target_values
    
        # prepare our x-value with our independent variables. We do an initial split here in order to run a 
        # linear regression to get a base r^2 on our basic model without interactions
        X = variables
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=randomstate)
        base_score = round(np.mean(cross_val_score(regression, X_train, y_train, scoring='r2', cv=cv)), 4)   
        print("Model base score is ",base_score)
    
        # now we run the regression on each feature combo
        for feature in feature_combos:
            feat1, feat2 = feature[0], feature[1]
        
            # create the test interaction on our data set
            variables['test_interaction'] = variables[feat1] * variables[feat2]
            # create a new X which includes the test interaction and drops our target value
            X = variables
            # make a new split so that our x-splits include the test interaction
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=randomstate)
        
            # Run a linear regression with cross-val just like our base model, and append the score to our scores list
            new_score = round(np.mean(cross_val_score(regression, X_train, y_train, scoring='r2', cv=cv)), 4)
            scores.append(new_score)
            # put feature 1 on a list
            feature1.append(feat1)
            # put feature 2 on a list
            feature2.append(feat2)
            print(feat1, feat2, new_score)
    
        # load all of our lists into the scoring dataframe
        scoring_df['feature1'] = feature1
        scoring_df['feature2'] = feature2
        scoring_df['scores'] = scores
        scoring_df['improvement'] = scoring_df['scores'] - base_score
        variables.drop('test_interaction', axis=1, inplace=True)

        # showing our improvement scores for our interactions

        scoring_df.sort_values('improvement', ascending=False)
    
    def add_polynomial(self, df, field, degree):
        '''takes a dataframe, a target column, and number of polynomial features
        returns a small dataframe of polynomial features
        '''
        values = df[field]
        poly_array = np.array(values)
        poly_array = poly_array.reshape(-1,1)
        poly_fit = PolynomialFeatures(degree=degree, include_bias=False)
        fit_features = poly_fit.fit_transform(poly_array)
        poly_df = pd.DataFrame(fit_features)
        return poly_df

    
    
