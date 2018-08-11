import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

sess = tf.Session()

# Data
x = np.linspace(-5, 5, 100)

# Data placeholder tensor
tensor_x = tf.placeholder(tf.float64, shape = (100,))

# Activations
tensor_sigmoid = tf.nn.sigmoid(tensor_x)
tensor_tanh = tf.nn.tanh(tensor_x)
tensor_relu = tf.nn.relu(tensor_x)
tensor_elu = tf.nn.elu(tensor_x)

# Gradients
sigmoid_grad = tf.gradients(xs = [tensor_x], ys = [tensor_sigmoid])
tanh_grad = tf.gradients(xs = [tensor_x], ys = [tensor_tanh])
relu_grad = tf.gradients(xs = [tensor_x], ys = [tensor_relu])
elu_grad = tf.gradients(xs = [tensor_x], ys = [tensor_elu])

gradients = sess.run([sigmoid_grad, tanh_grad, relu_grad, elu_grad], feed_dict = {tensor_x: x})
#print gradients

sigmoid_grad_y = gradients[0][0]
tanh_grad_y = gradients[1][0]
relu_grad_y = gradients[2][0]
elu_grad_y = gradients[3][0]

plt.figure(1, figsize = (10, 8))

plt.subplot(221)
plt.plot(x, sigmoid_grad_y, c = 'red', label = 'sigmoid grad')
plt.ylim((-0.5, 1))
plt.legend(loc = 'best')

plt.subplot(222)
plt.plot(x, tanh_grad_y, c = 'pink', label = 'tanh grad')
plt.ylim((-0.5, 1))
plt.legend(loc = 'best')

plt.subplot(223)
plt.plot(x, relu_grad_y, c = 'blue', label = 'relu grad')
plt.ylim((-0.5, 5))
plt.legend(loc = 'best')

plt.subplot(224)
plt.plot(x, elu_grad_y, c = 'gray', label = 'elu grad')
plt.ylim((-0.5, 5))
plt.legend(loc = 'best')

#plt.show()
plt.savefig('gradients.png')