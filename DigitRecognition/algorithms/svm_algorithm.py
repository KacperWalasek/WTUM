from sklearn.model_selection import GridSearchCV

from algorithms.algorithm import AlgorithmInterface
from sklearn import svm


class SVMAlgorithm(AlgorithmInterface):
    algorithm = None

    def train(self, data, labels) -> None:
        parameters = {'kernel': ('linear', 'rbf'), 'C': [1, 10]}
        self.algorithm = GridSearchCV(svm.SVC(), parameters).fit(data, labels)
        print(self.algorithm.best_estimator_)

    def predict(self, data) -> list:
        results = self.algorithm.predict(data)
        return results
