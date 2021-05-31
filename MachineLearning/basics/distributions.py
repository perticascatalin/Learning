import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

p = tf.distributions.Normal(loc = 0., scale = 1.)
q = tf.distributions.Normal(loc = 1., scale = 1.)

num_samples = 2000

# Create tensors for the 2 normal distributions
p_sampling = p.sample([num_samples])
q_sampling = q.sample([num_samples])

#print p_sampling, q_sampling

# Run the sampling
sess = tf.Session()
[p_samples, q_samples] = sess.run([p_sampling, q_sampling])

#print p_samples, q_samples

# Create density intervals and initialize density values for intervals
density_values = np.linspace(-10, 10, 2000)

p_density = np.zeros((2000,), dtype = np.float32)
q_density = np.zeros((2000,), dtype = np.float32)

#print density_values.shape

# Epsilon for density interval
epsilon = 0.1

# Populate density intervals with values

for p_sample in p_samples:
	for index in range(len(p_density)):
		abs_diff = abs(p_sample - density_values[index])
		if abs_diff < epsilon:
			p_density[index] += 1.0

for q_sample in q_samples:
	for index in range(len(q_density)):
		abs_diff = abs(q_sample - density_values[index])
		if abs_diff < epsilon:
			q_density[index] += 1.0

#print p_density, q_density

# Plot sampled values
plt.figure(1, figsize = (10,8))

plt.plot(density_values, p_density, c = 'blue', label = 'p')
plt.plot(density_values, q_density, c = 'red', label = 'q')
plt.legend(loc = 'best')

plt.savefig('distributions.png')

