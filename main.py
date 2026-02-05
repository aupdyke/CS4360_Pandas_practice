import pandas as pd
import numpy as np
from scipy.stats import zscore

#PART A)
np.random.seed(0)

df = pd.DataFrame({
    "A": np.random.normal(50, 10, 10),
    "B": np.random.normal(30, 5, 10),
    "C": np.random.normal(100, 20, 10),
    "D": np.random.normal(0, 1, 10),
    "E": np.random.normal(75, 15, 10)
})

baseline_mean = df.mean()
baseline_std = df.std()

df.loc[2, "A"] = baseline_mean["A"] + 6 * baseline_std["A"]
df.loc[7, "C"] = baseline_mean["C"] + 6 * baseline_std["C"]

threshold = 3

z_scores = (df - baseline_mean) / baseline_std

outlier_rows = df[(np.abs(z_scores) > threshold).any(axis = 1)]

print("Standard DataFrame:")
print(df)

print("\nZ-Scores")
print(z_scores)

print("\nRows Containing Outliers: ")
print(outlier_rows)

#PART B)
import matplotlib.pyplot as plt

all_z_scores = z_scores.values.flatten()

plt.figure()
plt.hist(all_z_scores, bins = 20)
plt.axvline(threshold, color = "red")
plt.axvline(-threshold, color = "red")
plt.title("Z-Score Distribution")
plt.xlabel("Z-Score")
plt.ylabel("Frequency")
plt.show()


#PART C)
df_cleaned = df.copy()

for col in df.columns:
    median = df[col].median()
    df_cleaned.loc[np.abs(z_scores[col]) > threshold, col] = median

print("DataFrame after replacing outliers with median:")
print(df_cleaned)