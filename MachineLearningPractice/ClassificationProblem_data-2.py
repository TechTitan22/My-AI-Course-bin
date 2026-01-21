# Classification Problem

import pandas as pd
from sklearn.model_selection import train_test_split

# 1. Local file load karein 
df = pd.read_csv('MachineLearningPractice/data-2.csv') 

# 2. Features (X) aur Target (y) alag karein
# Farz karein last column 'target' hai aur baqi features hain
X = df.drop('target_column_name', axis=1) 
y = df['target_column_name']

# 3. Train/Test split karein
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
