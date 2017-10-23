# Fork of [DEAP](https://github.com/DEAP/deap) to replace Python random modules with Numpy random to keep consistent seed across Python 2 and 3 (Development stage)

Note: An explanation of the issue is available [here](https://github.com/DEAP/deap/issues/138).

[![Build status](https://travis-ci.org/DEAP/deap.svg?branch=master)](https://travis-ci.org/DEAP/deap) [![Download](https://img.shields.io/pypi/dm/deap.svg)](https://pypi.python.org/pypi/deap) [![Join the chat at https://gitter.im/DEAP/deap](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/DEAP/deap?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

DEAP is a novel evolutionary computation framework for rapid prototyping and testing of 
ideas. It seeks to make algorithms explicit and data structures transparent. It works in perfect harmony with parallelisation mechanism such as multiprocessing and [SCOOP](http://pyscoop.org).

DEAP includes the following features:

  * Genetic algorithm using any imaginable representation
    * List, Array, Set, Dictionary, Tree, Numpy Array, etc.
  * Genetic programing using prefix trees
    * Loosely typed, Strongly typed
    * Automatically defined functions
  * Evolution strategies (including CMA-ES)
  * Multi-objective optimisation (NSGA-II, SPEA2, MO-CMA-ES)
  * Co-evolution (cooperative and competitive) of multiple populations
  * Parallelization of the evaluations (and more)
  * Hall of Fame of the best individuals that lived in the population
  * Checkpoints that take snapshots of a system regularly
  * Benchmarks module containing most common test functions
  * Genealogy of an evolution (that is compatible with [NetworkX](http://networkx.lanl.gov))
  * Examples of alternative algorithms : Particle Swarm Optimization, Differential Evolution, Estimation of Distribution Algorithm

## Downloads

Following acceptation of [PEP 438](http://www.python.org/dev/peps/pep-0438/) by the Python community, we have moved DEAP's source releases on [PyPI](https://pypi.python.org).

You can find the most recent releases at: https://pypi.python.org/pypi/deap/.

## Documentation
See the [DEAP User's Guide](http://deap.readthedocs.org/) for DEAP documentation.

In order to get the tip documentation, change directory to the `doc` subfolder and type in `make html`, the documentation will be under `_build/html`. You will need [Sphinx](http://sphinx.pocoo.org) to build the documentation.

### Notebooks
Also checkout our new [notebook examples](https://github.com/DEAP/notebooks). Using [IPython's](http://ipython.org/) notebook feature you'll be able to navigate and execute each block of code individually and tell what every line is doing. Either, look at the notebooks online using the notebook viewer links at the botom of the page or download the notebooks, navigate to the you download directory and run

```bash
ipython notebook --pylab inline
```

## Installation

The latest version can be installed with 
```bash
pip install git+https://github.com/justinshenk/deap@master
```

If you wish to build from sources, download or clone the repository and type

```bash
python setup.py install
```

## Requirements
The most basic features of DEAP requires Python2.6. In order to combine the toolbox and the multiprocessing module Python2.7 is needed for its support to pickle partial functions. CMA-ES requires Numpy, and we recommend matplotlib for visualization of results as it is fully compatible with DEAP's API.

Since version 0.8, DEAP is compatible out of the box with Python 3. The installation procedure automatically translates the source to Python 3 with 2to3.
