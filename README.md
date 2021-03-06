# McErrors
Monte carlo error propagation:
Samples a function with uncertain input data in order to estimate the distribution of the function.

This is done by drawing random samples from the input distributions and calculating the function on the input samples. Thus a monte carlo estimate of the function can be obtained by a simple average. The uncertainty on the function can be estimated from the distribution of the monte carlo samples.

![Tests](https://github.com/cwand/gspec/actions/workflows/tests.yml/badge.svg)

## Installation

McErrors is most easily installed with pip:
```text
pip install mcerrors
```

## Usage
The code below shows a (very simple) use case of the code:
```text
import mcerrors
import math

a = mcerrors.DistVariable([1.5, 1.7, 1.7, 1.8])           # Input variable with the given distribution.
b = mcerrors.DistVariable([14.2, 12.1, 7.4, 15.6, 2.3])   # The input is samples with a uniform probability from the input distribution

# Define function ( x+sqrt(y) )
def f(x):
  return x[0] + math.sqrt(x[1])

p = mcerrors.Propagator(f)  # Make a propagator with the function as argument
p.addDistVariable(a)        # Add the input variables
p.addDistVariable(b)

s = p.propagate(samples=10) # Draw ten samples of the function.
```
