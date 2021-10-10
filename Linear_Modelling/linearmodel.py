import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn.linear_model

data = pd.read_csv('cgpaToAdmission.csv')

print(data)

x = np.array(data['CGPA'])
y = np.array(data["Chance of Admit "])
#
# data.plot(kind='scatter', x='CGPA', y='Chance of Admission')
# plt.show()
plt.scatter(x,y)
plt.xlabel('CGPA')
plt.ylabel('Chance of Admissions')
plt.show()

model = sklearn.linear_model.LinearRegression()
# Train the model
model.fit(x, y)
# Make a prediction for Cyprus
# X_new = [[5]] # Cyprus' GDP per capita
# print(model.predict(X_new)) # outputs [[ 5.96242338]]
