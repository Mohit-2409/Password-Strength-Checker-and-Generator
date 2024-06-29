import pandas as pd
import numpy as np
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
data = pd.read_csv("C:/Users/delta/OneDrive/Desktop/VS Code Files/Password Gen and Strength Checker/pass classifier.csv.csv")
print(data.head())
print(data[data['password'].isnull()])
data.dropna(inplace=True)

