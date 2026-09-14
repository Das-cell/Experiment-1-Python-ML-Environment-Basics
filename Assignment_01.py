# Problem 1

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

data = {
    "Age": [22, 25, None, 28, 30],
    "Salary": [25000, 30000, 35000, None, 45000],
    "Department": ["IT", "HR", "IT", "Sales", "HR"],
    "Experience": [1, 2, 3, None, 5]
}

df = pd.DataFrame(data)

X = df[["Age", "Salary", "Department", "Experience"]]

numeric_features = ["Age", "Salary", "Experience"]
categorical_features = ["Department"]

numeric_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features)
    ]
)

X_processed = preprocessor.fit_transform(X)

X_train, X_test = train_test_split(
    X_processed, test_size=0.2, random_state=42
)

print("--- Original Dataset ---")
print(df)

print("\n--- Processed Data Shape ---")
print(X_processed.shape)

print("Training Samples:", X_train.shape[0])
print("Testing Samples:", X_test.shape[0])