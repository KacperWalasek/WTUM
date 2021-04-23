class AlgorithmInterface:
    def train(self, data, labels) -> None:
        pass

    def predict(self, data) -> list:
        pass
