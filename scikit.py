import matplotlib.pyplot as plt
import pandas as pd
import  sklearn.datasets
import sklearn.linear_model
import  sklearn.model_selection

boston = sklearn.datasets.load_boston()
x = boston.data
y = boston.target
df = pd.DataFrame(boston.data, columns=boston.feature_names)
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.2)
lr = sklearn.linear_model.LinearRegression()
lr.fit(x_train, y_train)
print(lr.score(x_test, y_test))