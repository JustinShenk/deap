# Benchmarking Intel's Math Kernel Library-based Numpy psuedo-random number generator in evolutionary algorithms

DEAP is an evolutionary algorithm library. The master branch uses base Python pseudo-random number generator. A Numpy variant was introduced into the branch `numpy-random` which guarantees consistent seeding.

This `numpy-random-mkl` branch patches the numpy.random.uniform and other methods with the `mkl_random` methods, designed for Intel hardware, and improving speed up to 25% in the knapsack problem.

## Benchmarking setup

Create two Python environments:

MKL-based random:

```bash
conda create -n deap-mkl python=2 -c intel mkl_random
pip install git+https://github.com/JustinShenk/deap.git@numpy-random-mkl
```

Numpy random:

```bash
conda create -n deap-numpy python=2
pip install git+https://github.com/JustinShenk/deap.git@numpy-random-mkl
```

Optional third environment can test the base (non-Numpy) random module:

```bash
conda create -n deap-base python=2
pip install deap
```

Run the script `python benchmark_mkl.py knapsack 1` to run the knapsack.py with various `lambda` parameters for 4 iterations. The `1` is a binary argument specifying whether the current environment is using the `numpy` random module or not. For the `deap-base` enviroment, run the command with `python benchmark_mkl.py knapsack 0`.

## Results
