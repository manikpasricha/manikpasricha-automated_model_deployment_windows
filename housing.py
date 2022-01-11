
# import files and dependencies
import pandas
from datetime import datetime
from sklearn.linear_model import LinearRegression

# Sample housing data from Kaggle https://www.kaggle.com/c/house-prices-advanced-regression-techniques/overview

train = pandas.read_csv('./raw data/train.csv')
test = pandas.read_csv('./raw data/test.csv')
# ------------------------------------------------------------------------------------------------------------------
# keeping initial set of demo features
X_demo_vars = ["LotArea","OverallQual","OverallCond","YearRemodAdd","TotRmsAbvGrd","GarageCars"]
X_train = train[X_demo_vars]
X_test = test[X_demo_vars]
X_test = X_test.fillna(X_test.mean())
y_train = train["SalePrice"]

# ------------------------------------------------------------------------------------------------------------------
# running simple regression
regressor = LinearRegression()  
regressor.fit(X_train, y_train) #training the algorithm

y_pred = regressor.predict(X_test)
housing_predictions = pandas.DataFrame({'Predicted_SalePrice': y_pred.flatten()})
# ------------------------------------------------------------------------------------------------------------------
# Edits for export
# adding date stamp on file name
date = datetime.now().strftime("%Y_%m_%d")
filename = f"predictions_{date}.xlsx"
housing_predictions.to_excel(filename)

# ------------------------------------------------------------------------------------------------------------------



