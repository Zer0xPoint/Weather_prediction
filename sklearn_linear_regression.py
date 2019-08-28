from sklearn.externals import joblib
import pandas as pd

tree_model = joblib.load('weather_predictor.pkl')

print("-" * 48)
print("Enter the details of the date you would like to predict")
print("\n")
# option = input("Year: ")
# year = option
# option = input("Month number (00): ")
# month = option
# option = input("Day number (00): ")
# theday = option

# df = pd.DataFrame('2019-08-27 09:00:00').apply(pd.to_timedelta)

# day = str(month) + str(theday)
#
# date = [[day, (str(int(day) + 1)), day]]
# temp = tree_model.predict(date)[0]
temp = tree_model.predict(['2019-08-27 09:00:00'])[0]

print("-" * 48)
print("\nThe temperature is estimated to be: " + str(temp) + "\n")
print("-" * 48)
