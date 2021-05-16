from data_preparation.binarization import binarize
from data_preparation.read_data import read_data
from flow.sort_entries import sort_entries

def prepare_sets():
    entries = read_data('data_preparation/train.csv')
    sorted_entries = sort_entries(entries)
    training_set = []
    testing_set = []
    validation_set = []
    for i in range(0, 10):
        binarized_entries = list(map(lambda ent: binarize(ent), sorted_entries[i]))
        length = len(binarized_entries)
        training_set = training_set + binarized_entries[0:int(length * 0.7)]
        testing_set = testing_set + binarized_entries[int(length * 0.7):int(length * 0.8)]
        validation_set = validation_set + binarized_entries[int(length * 0.8):length]
    return training_set, testing_set, validation_set
