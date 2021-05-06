from data_preparation.binarization import binarize
from data_preparation.read_data import read_data


def prepare_sets():
    entries = read_data('data_preparation/train.csv')
    binarized_entries = list(map(lambda ent: binarize(ent), entries))
    length = len(binarized_entries)
    training_set = binarized_entries[0:int(length*0.7)]
    testing_set = binarized_entries[int(length*0.7):int(length*0.8)]
    validation_set = binarized_entries[int(length*0.8):length]
    return training_set, testing_set, validation_set
