import pandas as pd
import numpy as np
from scipy.stats import zscore

np.random.seed(0)

df = pd.DataFrame({
    "A": np.random.normal(50, 10, 10),
    "B": np.random.normal(30, 5, 10),
    "C": np.random.normal(100, 20, 10),
    "D": np.random.normal(0, 1, 10),
    "E": np.random.normal(75, 15, 10)
})

df.loc[2, "A"] = 120
df.loc[7, "C"] = 200

threshold = 2

z_scores = df.apply(zscore)

outlier_rows = df[(np.abs(z_scores) > threshold).any(axis = 1)]

print("Z-Scores")
print(z_scores)

print("\nRows Containing Outliers: ")
print(outlier_rows)