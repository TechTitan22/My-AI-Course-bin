# Classification Problem (Custom Dataset)

import pandas as pd

# 1. Load the dataset (CSV)
df = pd.read_csv("MachineLearningPractice/data-2.csv")

print("Dataset shape:", df.shape)           # Dataset shape: (569, 33)
print(df.head())

# 2. Separate features & target

# Target column
target_column = "diagnosis"

# Feature columns
feature_names = df.drop(columns=["id", target_column]).columns

# Features (X) and Target (y)
X = df[feature_names].copy()
y = df[target_column].copy()

print("X shape:", X.shape)
print("y shape:", y.shape)

# 3. Handle missing values (VERY IMPORTANT)
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy="mean")
X = imputer.fit_transform(X)

# 4. Feature Scaling
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("First scaled row:", X_scaled[0])

# 5. Train-Test Split
from sklearn.model_selection import train_test_split

X_train_scaled, X_test_scaled, y_train, y_test = train_test_split(
    X_scaled,
    y,
    train_size=0.7,
    random_state=25
)

print(f"Train size: {round(len(X_train_scaled) / len(X_scaled) * 100)}%")
print(f"Test size: {round(len(X_test_scaled) / len(X_scaled) * 100)}%")

# 6. Model Training
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

logistic_regression = LogisticRegression(max_iter=5000)
svm = SVC()
tree = DecisionTreeClassifier(random_state=25)

logistic_regression.fit(X_train_scaled, y_train)
svm.fit(X_train_scaled, y_train)
tree.fit(X_train_scaled, y_train)

# 7. Predictions
log_reg_preds = logistic_regression.predict(X_test_scaled)
svm_preds = svm.predict(X_test_scaled)
tree_preds = tree.predict(X_test_scaled)

# 8. Model Evaluation
from sklearn.metrics import classification_report

model_preds = {
    "Logistic Regression": log_reg_preds,
    "Support Vector Machine": svm_preds,
    "Decision Tree": tree_preds
}

for model, preds in model_preds.items():
    print(f"\n{model} Results:")
    print(classification_report(y_test, preds))
