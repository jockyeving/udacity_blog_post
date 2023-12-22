import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

def clean_data(df, test_size):
    '''
    INPUT:
    df (pd.DataFrame) - raw dataset
    test_size (float) - size of the test dataset relative to the whole dataframe
    OUTPUT:
    X_train (pd.DataFrame) - Training data
    X_test (pd.DataFrame) - Test data
    y_train (pd.Series) - Training labels
    y_test (pd.Series) - Test labels
    
    Filters the raw dataset into x: variables that are more related to social status/preference, and y: 
    Job Satisfaction. Then dummy variables are created for categorical variables, and finally x and y 
    are split into train and test datasets respectively.
    '''

    df = df.dropna(subset=['JobSatisfaction'], axis=0).reset_index().drop('index', axis=1)
    y = df['JobSatisfaction']
    x = df[['FriendsDevelopers', 'HomeRemote', 'ProgramHobby', 'FormalEducation', 'OtherPeoplesCode', 'HighestEducationParents', 'KinshipDevelopers']]

    cat_vars = x.select_dtypes(include=['object']).copy().columns
    for var in  cat_vars:
        # for each cat add dummy var, drop original column
        x = pd.concat([x.drop(var, axis=1), pd.get_dummies(x[var], prefix=var, prefix_sep='_', drop_first=True)], axis=1)
    reduce_X = x.iloc[:, np.where((x.sum() > 2000) == True)[0]]
    X_train, X_test, y_train, y_test = train_test_split(reduce_X, y, test_size = test_size, random_state=42)

    return X_train, X_test, y_train, y_test

def coef_weights(lm_model, X_train):
    '''
    INPUT:
    lm_model (model) - trained linear model
    X_train (pd.DataFrame) - the training data, so the column names can be used
    OUTPUT:
    coefs_df (pd.DataFrame) - a dataframe holding the coefficient, estimate, and abs(estimate)
    
    Provides a dataframe that can be used to understand the most influential coefficients
    in a linear model by providing the coefficient estimates along with the name of the 
    variable attached to the coefficient.
    '''
    coefs_df = pd.DataFrame()
    coefs_df['est_int'] = X_train.columns
    coefs_df['coefs'] = lm_model.coef_
    coefs_df['abs_coefs'] = np.abs(lm_model.coef_)
    coefs_df = coefs_df.sort_values('abs_coefs', ascending=False)
    return coefs_df

def plot_result(coef_df):
    '''
    INPUT:
    coef_df (pd.DataFrame) - coefficients for each variable from the linear model
    
    Plots which variable has the highest impact on Job Satisfaction
    '''

    df_forplot = coef_df.head(15).reset_index().drop(['index','coefs'], axis=1)
    x = x = np.arange(len(df_forplot))
    y = df_forplot.abs_coefs

    fig, ax = plt.subplots(figsize =(12, 8))
    ax.grid(b = True, color ='grey',
                linestyle ='-.', linewidth = 0.5,
                alpha = 0.2)
    plt.barh(x, y, height=0.3, color= 'blue', tick_label = df_forplot.est_int, label = 'Coefficients')

    ax.set_title('Effect of social preferences on Job Satisfaction',
                    loc ='left', )

    plt.legend()
    plt.show()