# Task1
import numpy as np
t = np.arange(0,5,0.1)
f = 3
y = np.exp(-t) * np.cos(2*np.pi*f*t)
print(y)

# Task2
import numpy as np
arr = np.array([[1,2],[3,4]])
print(arr.flatten())

# Task3
import numpy as np
matrix = np.array([[50,100,50],
                   [100,200,100],
                   [50,100,50]
                   ])
border = np.pad(matrix, pad_width=1,mode='constant',constant_values=255)
print(border)

# Task4
import time
import numpy as np

dims = [100, 1000, 10000, 100000, 1000000]

print(f"{'dim':<10} | {'Normal python':<15} | {'Numpy':<15}")
print("-" * 45)

for dim in dims:
    a = list(range(dim))
    b = list(range(dim))
    
    a_np = np.array(a)
    b_np = np.array(b)
    
    start = time.time()
    result_python = 0
    for i in range(dim):
        result_python += a[i] * b[i]
    end = time.time()
    time_python = end - start
    
    
    start = time.time()
    result_numpy = 0
    for i in range(dim):
        result_numpy += np.dot(a_np, b_np)
    end = time.time()
    time_numpy = end - start

    print(f"{dim:<10} | {time_python:<15.5f} | {time_numpy:<15.5f}")
    