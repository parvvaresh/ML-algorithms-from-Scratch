import numpy as np

def euclidean_distance(point1 : np.array,
                       point2 : np.array) -> np.float:
    return np.sqrt(np.sum((point1 - point2) ** 2))

def sigmoid(points : np.array) -> np.array:
    return 1 / (1 + np.exp(-points))