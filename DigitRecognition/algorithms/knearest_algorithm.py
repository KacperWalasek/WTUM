from algorithms.algorithm import AlgorithmInterface
from sklearn.neighbors import NearestNeighbors


class KNearestAlgorithm(AlgorithmInterface):
    algorithm = None
    labels = None

    def train(self, data, labels) -> None:
        self.algorithm = NearestNeighbors(n_neighbors=1, algorithm='ball_tree').fit(data)
        self.labels = labels

    def predict(self, data) -> list:
        distances, indices = self.algorithm.kneighbors(data)
        print('nearest', list(map( lambda index: self.labels[index[0]], indices)))
        return list(map(lambda index: self.labels[index[0]], indices))
