import numpy as np

data = np.array([84.485, 51.3625, 85.28, 84.485, 85.28])

q3, q1 = np.percentile(data, [75, 25])

iqr = q3 - q1

for value in data:
    if value < q1 - (1.5 * iqr):
        print(value)