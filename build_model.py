import statsmodels.api as sm
from statsmodels.api import add_constant
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, median_absolute_error
from sklearn.externals import joblib


df = pd.read_csv(
    '/Users/lee/Library/CloudStorage/iCloudDrive/Documents/PyCharmProjects/Weather_prediction/data/all_clean.csv')
# predictors = ['Date', 'Dewpoint', 'Dewpoint_1', 'Dewpoint_2', 'Dewpoint_3', 'Temperature_1', 'Temperature_2']
predictors = ['Dewpoint', 'Dewpoint_1', 'Dewpoint_2', 'Dewpoint_3', 'Temperature_1', 'Temperature_2']

# X = df[predictors].set_index('Date')
X = df[predictors]
y = df['Temperature']

X = sm.add_constant(X)
# print(X)
alpha = 0.05
model = sm.OLS(y, X).fit()
model.summary()

X = X.drop('const', axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=12)
# instantiate the regressor class
regressor = LinearRegression()
# fit the build the model by fitting the regressor to the training data
regressor.fit(X_train, y_train)

joblib.dump(regressor, 'weather_predictor.pkl')
# make a prediction set using the test set
prediction = regressor.predict(X_test)
# Evaluate the prediction accuracy of the model
print("The Explained Variance: %.2f" % regressor.score(X_test, y_test))
print("The Mean Absolute Error: %.2f degrees celsius" % mean_absolute_error(y_test, prediction))
print("The Median Absolute Error: %.2f degrees celsius" % median_absolute_error(y_test, prediction))
