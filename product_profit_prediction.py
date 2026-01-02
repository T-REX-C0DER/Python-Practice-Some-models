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
