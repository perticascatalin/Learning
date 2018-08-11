import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

sess = tf.Session()

# Data
x = np.linspace(-5, 5, 100)
double_x = np.linspace(-5, 5, 200)

# Activations
sigmoid = tf.nn.sigmoid(x)
relu = tf.nn.relu(x)
tanh = tf.nn.tanh(x)
softplus = tf.nn.softplus(x)
softsign = tf.nn.softsign(x)
dropout = tf.nn.dropout(x, 0.9)
elu = tf.nn.elu(x)
crelu = tf.nn.crelu(x)

# Run session to compute all activations
[sigmoid_y, relu_y, tanh_y, softplus_y, softsign_y, dropout_y, elu_y, crelu_y] = sess.run([sigmoid, relu, tanh, softplus, softsign, dropout, elu, crelu])

# Plot activations
plt.figure(1, figsize = (10, 8))

plt.subplot(421)
plt.plot(x, sigmoid_y, c = 'red', label = 'sigmoid')
plt.ylim((-0.5, 1))
plt.legend(loc = 'best')

plt.subplot(422)
plt.plot(x, tanh_y, c = 'pink', label = 'tanh')
plt.ylim((-2, 2))
plt.legend(loc = 'best')

plt.subplot(423)
plt.plot(x, relu_y, c = 'blue', label = 'relu')
plt.ylim((-1, 5))
plt.legend(loc = 'best')

plt.subplot(424)
plt.plot(x, elu_y, c = 'gray', label = 'elu')
plt.ylim((-2, 5))
plt.legend(loc = 'best')

plt.subplot(425)
plt.plot(x, softplus_y, c = 'green', label = 'softplus')
plt.ylim((-1, 5))
plt.legend(loc = 'best')

plt.subplot(426)
plt.plot(x, softsign_y, c = 'orange', label = 'softsign')
plt.ylim((-1, 2))
plt.legend(loc = 'best')

plt.subplot(427)
plt.plot(x, dropout_y, c = 'magenta', label = 'dropout 0.9')
plt.ylim((-10, 10))
plt.legend(loc = 'best')

plt.subplot(428)
plt.plot(double_x, crelu_y, c = 'black', label = 'crelu')
plt.ylim((-2, 5))
plt.legend(loc = 'best')

#plt.show()
plt.savefig('activations.png')