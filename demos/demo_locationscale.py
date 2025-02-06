import numpy as np
from robustsp import MLocHUB, MscaleHUB, MLocTUK, MscaleTUK

x_normal = np.random.normal(10, 2, 100)

print(f"Data without outliers :")
print(f"Mean={np.mean(x_normal):.2f}, Standard deviation={np.std(x_normal):.2f}")
print(f"MLocHUB : {MLocHUB(x_normal):.4f}")
print(f"MScaleHUB : {MscaleHUB(x_normal):.4f}")
print(f"MLocTuk : {MLocTUK(x_normal):.4f}")
print(f"MScaleTuk : {MscaleTUK(x_normal):.4f}\n\n")

x_outlier = np.array([1, 2, 3, 4, 100])
print(f"Data with one extreme outliers :")
print(f"Mean={np.mean(x_outlier):.2f}, Standard deviation={np.std(x_outlier):.2f}")
print(f"MLocHUB : {MLocHUB(x_outlier):.4f}")
print(f"MScaleHUB : {MscaleHUB(x_outlier):.4f}")
print(f"MLocTuk : {MLocTUK(x_outlier):.4f}")
print(f"MScaleTuk : {MscaleTUK(x_outlier):.4f}\n\n")

x_skewed = np.concatenate([np.random.normal(5, 1, 90), np.random.normal(20, 1, 10)])
print(f"Data with outliers (90% normal, 10% derivated) :")
print(f"Mean={np.mean(x_skewed):.2f}, Standard deviation={np.std(x_skewed):.2f}")
print(f"MLocHUB : {MLocHUB(x_skewed):.4f}")
print(f"MScaleHUB : {MscaleHUB(x_skewed):.4f}")
print(f"MLocTuk : {MLocTUK(x_skewed):.4f}")
print(f"MScaleTuk : {MscaleTUK(x_skewed):.4f}\n\n")

x_single = np.array([5])
print(f"Data with one value :")
print(f"Mean={np.mean(x_single):.2f}, Standard deviation={np.std(x_single):.2f}")
print(f"MLocHUB : {MLocHUB(x_single):.4f}")
print(f"MScaleHUB : {MscaleHUB(x_single):.4f}")
print(f"MLocTuk : {MLocTUK(x_single):.4f}")
print(f"MScaleTuk : {MscaleTUK(x_single):.4f}\n\n")

x_empty = np.array([])
print(f"Empty data :")
print(f"Mean={np.mean(x_empty):.2f}, Standard deviation={np.std(x_empty):.2f}")
print(f"MLocHUB : {MLocHUB(x_empty):.4f}")
print(f"MScaleHUB : {MscaleHUB(x_empty):.4f}")
print(f"MLocTuk : {MLocTUK(x_empty):.4f}")
print(f"MScaleTuk : {MscaleTUK(x_empty):.4f}\n\n")