# Benchmarking-specific code
import csv
import importlib
import os
import sys
import time


def set_base():
    os.system('git checkout master')


def set_mkl():
    os.environ['MKL_RANDOM'] = "1"


def main(script_name):
    module = importlib.import_module(script_name)
    for case in ['mkl_random', 'numpy_random', 'base']:
        if case == 'base':  # Base Python random
            set_base()
        else:  # Numpy random
            os.system('git checkout numpy-random-mkl')
        if case is 'mkl_random':
            set_mkl()
        else:
            os.environ.pop('MKL_RANDOM', None)
        # Sanity check
        print('MKL_RANDOM value: {}'.format(
            os.environ.pop('MKL_RANDOM', "False")))
        if script_name == 'knapsack':
            LAMBDAS = [1000, 5000, 10000]
            repetitions = 4
            filename = '{}_benchmark_{}.csv'.format(script_name, case)
            with open(filename, 'wb') as csvfile:
                writer = csv.writer(csvfile, delimiter=' ')
                writer.writerow(["seconds", "lambda", "case"])
                for LAMBDA in LAMBDAS:
                    for rep in range(repetitions):
                        start = time.time()
                        module.main(LAMBDA=LAMBDA)
                        end = time.time()
                        duration = end - start
                        writer.writerow([duration, LAMBDA, case])

                        print duration, LAMBDA, case
                print "Saved to {}".format(filename)


if __name__ == '__main__':
    print(sys.argv)
    script_name = sys.argv[1]
    main(script_name)
