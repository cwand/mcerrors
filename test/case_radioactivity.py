# Estimate the activity on a radioacitve source some time into the future from
# counting data

import mcerrors
import matplotlib.pyplot as plt
import numpy as np
import math

# Background counted for 30 seconds: 82 counts
B = 82
# Distribution is Poisson for radioactive counting data:
B_smpls = np.random.poisson(B, 10000).tolist()
B_var = mcerrors.DistVariable(B_smpls)

# Sample+background counted for 30 seconds: 532 counts
G = 532
# Distribution is Poisson for radioactive counting data:
G_smpls = np.random.poisson(G, 10000).tolist()
G_var = mcerrors.DistVariable(G_smpls)

# The half-life of the radioactive isotope is 122.24(16) seconds (Gaussian)
t12_smpls = np.random.normal(122.24, 0.16, 10000)
t12_var = mcerrors.DistVariable(t12_smpls)


# Function to estimate net counting rate in 400 seconds
def f(x):
	# unpack input
	b = x[0] # background
	g = x[1] # gross rate
	t12 = x[2] # half life

	# calculate net counting rate now:
	n = g/30.0 - b/30.0

	# decay to 40 seconds
	n400 = n * math.pow(0.5, 400.0/t12)
	return n400


p = mcerrors.Propagator(f)
p.addDistVariable(B_var)
p.addDistVariable(G_var)
p.addDistVariable(t12_var)
smpls = p.propagate(samples=100000)


n, bins, patches = plt.hist(smpls, 50, density=True, facecolor='g', alpha=0.75)
plt.xlabel('f')
plt.ylabel('Probability')
plt.grid(True)
plt.show()
