from data_preparation.read_data import read_data
from interface.show_picture import show_pictures
from data_preparation.binarization import binarize
from algorithms.knearest_algorithm import KNearestAlgorithm

if __name__ == '__main__':
    entries = read_data('data_preparation/train.csv')
    for ent in entries:
        print(ent.label)
    print(entries[50].pixels)
    # show_pictures([
    #     [entries[80], 'picture80'], [binarize(entries[80]), 'binarized80'],
    #     [entries[2], 'picture2'], [binarize(entries[2]), 'binarized2'],
    #     [entries[3], 'picture3'], [binarize(entries[3]), 'binarized3'],
    # ])
    alg = KNearestAlgorithm()
    alg.train([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]], [1, 0, 9, 3, 4, 5])
    alg.predict([[-3.1, -2.3]])
