# Imports
import random
import numpy as np

# Functions
def main():
    arr1 = np.random.uniform(-10, 10, size=10).astype(np.float32)
    arr1 = np.concatenate([arr1, np.array([np.float32(0.0), np.float32(np.nan)])])
    arr2 = np.random.uniform(-5, 5, size=10).astype(np.float32)
    arr2 = np.concatenate([arr2, np.array([np.float32(0.0), np.float32(np.nan)])])
    arr3 = list(np.concatenate([arr1, arr2]))
    print("arr1:", arr1)
    print("arr2:", arr2)
    arr4 = random.shuffle(arr3)
    arr3 = sorted(arr4)
    n = len(arr4)
    first_quarter = arr3[:n]
    mean_first_quarter = sum(first_quarter)/n
    print("Mean of the first 25%:", mean_first_quarter)

if __name__ == '__main__':
    main() # 






