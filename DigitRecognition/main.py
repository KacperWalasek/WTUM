from data_preparation.read_data import read_data
from interface.show_picture import show_pictures
from data_preparation.binarization import binarize

if __name__ == '__main__':
    entries = read_data('data_preparation/train.csv')
    for ent in entries:
        print(ent.label)
    print(entries[50].pixels)
    show_pictures([
        [entries[80], 'picture80'], [binarize(entries[80]), 'binarized80'],
        [entries[2], 'picture2'], [binarize(entries[2]), 'binarized2'],
        [entries[3], 'picture3'], [binarize(entries[3]), 'binarized3'],
    ])

