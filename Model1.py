#This model will help to predict the marks of student based on the number of hours he studied


#import libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

#Prepare the data 
data = {
    'Hours_Studied' : [1,2,3,4,5,6,7,8,9,6],
    'Score' : [23,54,57,76,45,98,99,56,34,23,65]
}

df = pd.DataFrame(data)

#Features andd target
X = df(['Hours_Studied']) #input {dataframe}
Y = df('Score') #output {series}

#split the data
X_train , X_test , Y_train , Y_test = train_test_split(X,Y,test_size=0.2 , random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train,Y_train)

# Make predictions
Y_pred = model.predict(X_test)
print("Predictions : " , Y_pred)

# Evaluate the model
mse = mean_squared_error(Y_test,Y_pred)
print("Mean Squared Error : " , mse)

# Visualize results 
# Convert X to 1D array for plotting
X_1D = X['Hours_Studied'].values
Y_pred_Full = model.predict(X).flatten()

plt.scatter(X_1D,Y,color = 'blue' , label = 'Actual Scores')
plt.plot(X_1D , Y_pred_Full , color = 'red ' , label = 'Predicted Line')
plt.xlabel('Hours Studied')
plt.ylabel('Score')
plt.title('Hours Studied VS Score Prediction ')
plt.legend()
plt.show()