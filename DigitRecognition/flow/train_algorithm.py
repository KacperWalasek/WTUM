from data_preparation.data_extraction import extract_data


def train_algorithm(algorithm, training_set):
    data = list(map(lambda ent: extract_data(ent), training_set))
    labels = list(map(lambda ent: ent.label, training_set))

    algorithm.train(data, labels)
