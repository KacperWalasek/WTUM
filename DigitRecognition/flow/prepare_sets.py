from data_preparation.binarization import binarize
from data_preparation.read_data import read_data
from data_preparation.skeletonization import skeletonize
from flow.sort_entries import sort_entries

def prepare_sets():
    entries = read_data('data_preparation/train.csv')
    sorted_entries = sort_entries(entries)
    training_set = []
    validation_set = []
    for i in range(0, 10):
        binarized_entries = list(map(lambda ent: binarize(ent), sorted_entries[i]))
        length = len(binarized_entries)
        training_set = training_set + binarized_entries[0:int(length * 0.8)]
        validation_set = validation_set + binarized_entries[int(length * 0.8):length]
        # for sceletization
        #   scel_b_e = list(map(lambda ent: skeletonize(binarize(ent)), sorted_entries[i]))
        #   scel_train_set = scel_train_set + scel_b_e[0:int(length * 0.8)]
        #   scel_val_set = scel_val_set + scel_b_e[int(length * 0.8):length]
    return training_set, validation_set
