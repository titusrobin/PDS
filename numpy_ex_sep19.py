import numpy as np

# Seed insures results are stable.
np.random.seed(21)
random_integers = np.random.randint(1, high=500000, size=(20, 5))
random_integers

print(random_integers[:,2])
ex2_avg_val = np.average(random_integers[:,2])