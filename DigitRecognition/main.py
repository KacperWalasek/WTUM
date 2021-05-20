from algorithms.svm_algorithm import SVMAlgorithm
from data_preparation.skeletonization import skeletonize
from flow.prepare_sets import prepare_sets
from flow.train_algorithm import train_algorithm
from algorithms.knearest_algorithm import KNearestAlgorithm
from flow.validate import validate
from interface.show_interface import show_interface

if __name__ == '__main__':
    print('preparing data...')
    training_set, testing_set, validation_set = prepare_sets()
    algKN = KNearestAlgorithm()
    algSvm = SVMAlgorithm()
    # print('training k-nearest algorithm...')
    # train_algorithm(algKN, training_set)
    print('training svm algorithm...')
    train_algorithm(algSvm, training_set)
    show_interface(algSvm)
    # print('testing k_nearest algorithm...')
    # print('result: ', validate(algKN, validation_set)*100, '%')
    # print('testing svm algorithm...')
    # print('result: ', validate(algSvm, validation_set)*100, '%')
