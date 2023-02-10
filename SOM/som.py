from typing import Tuple

import numpy as np
from sklearn.neural_network import MiniBatchKMeans


class SelfOrganizingMap:
    def __init__(self, dims: Tuple[int, int], iterations: int, learning_rate: float):
        """Generated"""
        self.dims = dims
        self.iterations = iterations
        self.learning_rate = learning_rate
        self.model = MiniBatchKMeans(n_clusters=dims[0] * dims[1], max_iter=iterations,
                                     batch_size=32, learning_rate=learning_rate)

    def train(self, data: np.ndarray):
        """Generated"""
        self.model.fit(data)

    def map_input(self, input_vector: np.ndarray):
        """Generated"""
        return self.model.predict(input_vector.reshape(1, -1))[0]
