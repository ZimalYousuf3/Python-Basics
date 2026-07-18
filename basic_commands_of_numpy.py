import numpy as np

data = np.array([5, 10, 15, 20])

print('Sum:', data.sum())
print('Min:', data.min())
print('Max:', data.max())
print('Mean:', data.mean())
print('Each doubled:', data*2)
print('Each +200:', data+200)
print('Median:', np.median(data))
print('Standard Deviation:', data.std())
