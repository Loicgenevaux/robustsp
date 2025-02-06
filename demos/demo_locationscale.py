import numpy as np
from robustsp import MLocHUB, MscaleHUB, MLocTUK, MscaleTUK

x_normal = np.random.normal(10, 2, 100)

print(f"Data without outliers :")
print(f"Mean ={np.mean(x_normal):.2f}, Standard deviation={np.std(x_normal):.2f}")
print(f"MLocHUB : {MLocHUB(x_normal):.4f}")
print(f"MScaleHUB : {MscaleHUB(x_normal):.4f}")
print(f"MLocTuk : {MLocTUK(x_normal):.4f}")
print(f"MScaleTuk : {MscaleTUK(x_normal):.4f}")

x_outlier = np.array([1, 2, 3, 4, 100])
print(f"Data with outliers :")
print(f"Mean ={np.mean(x_outlier):.2f}, Standard deviation={np.std(x_outlier):.2f}")
print(f"MLocHUB : {MLocHUB(x_outlier):.4f}")
print(f"MScaleHUB : {MscaleHUB(x_outlier):.4f}")
print(f"MLocTuk : {MLocTUK(x_outlier):.4f}")
print(f"MScaleTuk : {MscaleTUK(x_outlier):.4f}")