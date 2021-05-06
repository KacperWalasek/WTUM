from flow.prepare_sets import prepare_sets
from flow.train_algorithm import train_algorithm
from algorithms.knearest_algorithm import KNearestAlgorithm
from flow.validate import validate

if __name__ == '__main__':
    print('preparing data...')
    training_set, testing_set, validation_set = prepare_sets()
    alg = KNearestAlgorithm()
    print('training k-nearest algorithm...')
    train_algorithm(alg, training_set)
    print('testing algorithm...')
    print('result: ', validate(alg, validation_set)*100, '%')
