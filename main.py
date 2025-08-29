#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from utils import plot2d, read_root
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

fname = "./data/LYSO15x4NTUmentor.root"
df = read_root(fname)
print(df)

# Prepare features and target
X = df.drop("ID", axis=1)  # Features (all columns except ID)
y = df["ID"]  # Target variable

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.4f}")

x_axis = "S5"
y_axis = "S6"

# Plot original data
plot2d(df, x_axis, y_axis, 1, "original_data.png")

# Create a dataframe with predicted IDs for plotting
df_predicted = X_test.copy()
df_predicted["ID"] = y_pred

# Plot predicted data
plot2d(df_predicted, x_axis, y_axis, 1, "predicted_data.png")

# Create a dataframe with misclassified points
df_misclassified = X_test.copy()
df_misclassified["ID"] = y_test
misclassified_mask = y_test != y_pred
df_misclassified = df_misclassified[misclassified_mask]

print(df_misclassified)

# Plot misclassified points
if not df_misclassified.empty:
    plot2d(df_misclassified, x_axis, y_axis, 5, "misclassified_data.png")
    print(f"Number of misclassified points: {len(df_misclassified)}")
else:
    print("No misclassified points found")
