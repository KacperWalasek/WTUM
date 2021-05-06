from Utils.compare import compare
from data_preparation.data_extraction import extract_data


def validate(algorithm, validation_set):
    result = algorithm.predict(list(map(lambda ent: extract_data(ent), validation_set)))
    return compare(validation_set, result)
