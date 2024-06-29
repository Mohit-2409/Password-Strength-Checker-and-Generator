import pandas as pd
import numpy as np
import seaborn as sns
import warnings

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

warnings.filterwarnings('ignore')
data = pd.read_csv("C:/Users/delta/OneDrive/Desktop/VS Code Files/Password Gen and Strength Checker/pass classifier.csv")
#print(data.head())
#print(data[data['password'].isnull()])
data.dropna(inplace=True)
#print(data.isnull().sum())
#sns.countplot(data['strength'])
#plt.show()


password_tuple = np.array(data)
print(password_tuple)

import random 
random.shuffle(password_tuple)

x = [labels[0] for labels in password_tuple]
y = [labels[1] for labels in password_tuple]
print(x)
