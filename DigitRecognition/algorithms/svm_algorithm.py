from sklearn.model_selection import GridSearchCV

from algorithms.algorithm import AlgorithmInterface
from sklearn import svm


class SVMAlgorithm(AlgorithmInterface):
    algorithm = None

    def train(self, data, labels) -> None:
        parameters = [
          {'C': [50, 75, 100, 125, 150], 'kernel': ['linear']},
          {'C': [50, 75, 100, 125, 150], 'gamma': [0.01, 0.001, 0.0001], 'kernel': ['rbf']},
         ]
        # 12:10 - 12:16
        # 12:20
        self.algorithm = svm.SVC(kernel='rbf', C=100, gamma=0.01).fit(data, labels)

    def predict(self, data) -> list:
        results = self.algorithm.predict(data)
        return results

    def name(self) -> str:
        return 'svm'