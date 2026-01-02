# This model predicts product profit based on advertising spend

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

data = {
    'Products_Sold': [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],
    'Profit': [5000, 12000, 18000, 25000, 31000, 38000, 45000, 52000, 60000, 68000]
}

df = pd.DataFrame(data)
X = df[['Products_Sold']]  # Feature
Y = df['Profit']           # Target

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, Y_train)
Y_pred = model.predict(X_test)
print("Predictions:", Y_pred)
mse = mean_squared_error(Y_test, Y_pred)
print("Mean Squared Error:", mse)
r2 = r2_score(Y_test, Y_pred)
print("R^2 Score:", r2)
# Visualization
X_1D = X['Products_Sold'].values
Y_pred_Full = model.predict(X)
plt.scatter(X_1D, Y, color='blue', label='Actual Profit')
plt.plot(X_1D, Y_pred_Full, color='red', label='Predicted Line')
plt.xlabel('Products Sold')
plt.ylabel('Profit')
plt.title('Products Sold vs Profit Prediction')
plt.legend()
plt.show()
