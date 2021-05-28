from sklearn.model_selection import GridSearchCV

from algorithms.algorithm import AlgorithmInterface
from sklearn import svm


class SVMAlgorithm(AlgorithmInterface):
    algorithm = None

    def train(self, data, labels) -> None:
        self.algorithm = svm.SVC(kernel='rbf', C=100, gamma=0.01).fit(data, labels)

    def predict(self, data) -> list:
        results = self.algorithm.predict(data)
        return results

    def name(self) -> str:
        return 'svm'
