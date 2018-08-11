import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

import tensorflow as tf
import import_data as data

# General architecture

IMG_SZ = 28
L_SZ = 2 # Labels size: Shape and Color
C_SZ = 3 # Classes size: (Circle, Square, Triangle) and (Red, Green, Blue)

INPUT_DIR = './figures/'
BATCH_SZ = 32
IMG_HEIGHT = IMG_SZ
IMG_WIDTH = IMG_SZ

N_CLASSES = 3 # total number of classes

# Parameters
learning_rate = 0.001
batch_size = 128
num_steps = 1000
display_step = 100

# Network Parameters
dropout = 0.75 # Dropout, probability to keep units

# multi label
X, Y = data.read_images(input_directory = INPUT_DIR, batch_size = BATCH_SZ, 
	img_height = IMG_HEIGHT, img_width = IMG_WIDTH, mode = 'multi_label')

#print (X, Y)


# Create model
def conv_net(x, n_classes, dropout, reuse, is_training):
    # Define a scope for reusing the variables
    with tf.variable_scope('ConvNet', reuse=reuse):

        # Convolution Layer with 8 filters and a kernel size of 5
        conv1 = tf.layers.conv2d(x, 32, 5, activation=tf.nn.relu)
        # Max Pooling (down-sampling) with strides of 2 and kernel size of 2
        conv1 = tf.layers.max_pooling2d(conv1, 2, 2)

        # Convolution Layer with 16 filters and a kernel size of 3
        conv2 = tf.layers.conv2d(conv1, 64, 3, activation=tf.nn.relu)
        # Max Pooling (down-sampling) with strides of 2 and kernel size of 2
        conv2 = tf.layers.max_pooling2d(conv2, 2, 2)

        # Flatten the data to a 1-D vector for the fully connected layer
        fc1 = tf.contrib.layers.flatten(conv2)

        # Fully connected layer (in contrib folder for now)
        fc1 = tf.layers.dense(fc1, 1024)
        # Apply Dropout (if is_training is False, dropout is not applied)
        fc1 = tf.layers.dropout(fc1, rate=dropout, training=is_training)

        # Output layer, class prediction
        out_1 = tf.layers.dense(fc1, n_classes)
        out_2 = tf.layers.dense(fc1, n_classes)
        # Because 'softmax_cross_entropy_with_logits' already apply softmax,
        # we only apply softmax to testing network
        out_1 = tf.nn.softmax(out_1) if not is_training else out_1
        out_2 = tf.nn.softmax(out_2) if not is_training else out_2

    return out_1, out_2

# Because Dropout have different behavior at training and prediction time, we
# need to create 2 distinct computation graphs that share the same weights.

# Create a graph for training
logits_train_1, logits_train_2 = conv_net(X, N_CLASSES, dropout, reuse=False, is_training=True)
# Create another graph for testing that reuse the same weights
logits_test_1, logits_test_2 = conv_net(X, N_CLASSES, dropout, reuse=True, is_training=False)

# Define loss and optimizer (with train logits, for dropout to take effect)
loss_op = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(
    logits=logits_train_1, labels=Y[:,0])) + tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(
    logits=logits_train_2, labels=Y[:,1]))

optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate)
train_op = optimizer.minimize(loss_op)

# Evaluate model (with test logits, for dropout to be disabled)
correct_pred = tf.logical_and(
    tf.equal(tf.argmax(logits_test_1, 1), tf.cast(Y[:,0], tf.int64)),
    tf.equal(tf.argmax(logits_test_2, 1), tf.cast(Y[:,1], tf.int64)))
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

# Initialize the variables (i.e. assign their default value)
init = tf.global_variables_initializer()

# Saver object
saver = tf.train.Saver()

# Start training
with tf.Session() as sess:

    # Run the initializer
    sess.run(init)

    # Start the data queue
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess = sess, coord = coord)

    # Training cycle
    for step in range(1, num_steps+1):

        if step % display_step == 0:
            # Run optimization and calculate batch loss and accuracy
            _, loss, acc = sess.run([train_op, loss_op, accuracy])
            print("Step " + str(step) + ", Minibatch Loss= " + \
                  "{:.4f}".format(loss) + ", Training Accuracy= " + \
                  "{:.3f}".format(acc))
        else:
            # Only run the optimization op (backprop)
            sess.run(train_op)

    print("Optimization Finished!")

    # Save your model
    saver.save(sess, './checkpts/shape_multi_class')

    # Stop threads
    coord.request_stop()
    coord.join(threads)

'''
x = tf.placeholder(shape = [None, IMG_SZ, IMG_SZ, 3], dtype = tf.float32)
y = tf.placeholder(shape = [None, N_SZ, C_SZ])

W1 = tf.Variable(tf.truncated_normal(shape = shape, stddev = 0.1))
b1 = tf.Variable(tf.constant(0.1, shape = shape))

conv1 = tf.nn.conv2d(x, W1, strides = [1, 1, 1, 1], padding = 'SAME')
layer1 = tf.nn.relu(conv1 + b1)
pool1 = tf.nn.max_pool(layer1, ksize = [1, 28, 28, 1], strides=[1, 1, 1, 1], padding = 'VALID')

W2 = tf.Variable(tf.truncated_normal(shape = shape, stddev = 0.1))
b2 = tf.Variable(tf.constant(0.1, shape = shape))

conv2 = tf.nn.conv2d(pool1, W2, strides = [1, 1, 1, 1], padding = 'SAME')
layer2 = tf.nn.relu(conv2 + b2)
pool2 = tf.nn.max_pool(layer2, ksize = [1, 28, 28, 1], strides = [1, 1, 1, 1], padding = 'VALID')

flattened = tf.reshape(pool2, [-1, 7 * 7 * 64])

# maybe add another dense here

# do this for number of labels

wd1 = tf.Variable(tf.truncated_normal([7 * 7 * 64, 1000], stddev = 0.03), name = 'wd1')
bd1 = tf.Variable(tf.truncated_normal([1000], stddev = 0.01), name = 'bd1')

dense_layer1 = tf.matmul(flattened, wd1) + bd1
dense_layer1 = tf.nn.relu(dense_layer1)
'''

