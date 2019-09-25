# 7. Test NN
# Summary
# 1. read data and conv net from multi_class multi_labels (open_nenos)
# 2. outputs from neural_net (ME) (to check N_OUT_CLASSES vs. N_CLASSES)
# 3. took out evaluation of inputs , custom prints and saving data

import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import fifth_notebook as data
import tensorflow as tf
import pickle

# General architecture

IMG_SZ = 32
INPUT_DIR = './grid_cells/'
VAL_DIR = './val_grid_cells/'
BATCH_SZ = 2
IMG_HEIGHT = IMG_SZ
IMG_WIDTH = IMG_SZ

N_CLASSES = 2 
#N_OUT_CLASSES = 58 # total number of classes
# to revert this change later
N_OUT_CLASSES = 10

# Parameters
learning_rate = 0.001
num_steps = 100
display_step = 10

# Network Parameters
dropout = 0.6 # Dropout, probability to keep units

X, Y = data.read_images(input_directory = INPUT_DIR, batch_size = BATCH_SZ)
print ('finished reading train images')
X_val, Y_val = data.read_images(input_directory = VAL_DIR, batch_size = BATCH_SZ)
print ('finished reading validation images')

# Create model
def conv_net(x, num_classes, num_labels, dropout, reuse, is_training):
    # Define a scope for reusing the variables
    with tf.variable_scope('ConvNet', reuse=reuse):

        # Convolution Layer with 4 filters and a kernel size of 4
        conv1 = tf.layers.conv2d(x, 4, 4, activation=tf.nn.relu)
        # Max Pooling (down-sampling) with strides of 2 and kernel size of 2
        conv1 = tf.layers.max_pooling2d(conv1, 2, 2)

        # Convolution Layer with 8 filters and a kernel size of 4
        conv2 = tf.layers.conv2d(conv1, 8, 4, activation=tf.nn.relu)
        # Max Pooling (down-sampling) with strides of 2 and kernel size of 2
        conv2 = tf.layers.max_pooling2d(conv2, 2, 2)

        # Flatten the data to a 1-D vector for the fully connected layer
        fc1 = tf.contrib.layers.flatten(conv2)

        # Fully connected layer (in contrib folder for now)
        fc1 = tf.layers.dense(fc1, 32)
        # Apply Dropout (if is_training is False, dropout is not applied)
        fc1 = tf.layers.dropout(fc1, rate=dropout, training=is_training)

        # Define outputs
        outputs = list()
        for i in range(num_classes):
            out_i = tf.layers.dense(fc1, num_labels)
            out_i = tf.nn.softmax(out_i) if not is_training else out_i
            outputs.append(out_i)

    return outputs

# Define the logits for all datasets
logits_train = conv_net(X, N_OUT_CLASSES, N_CLASSES, dropout, reuse = False, is_training = True)
logits_test = conv_net(X, N_OUT_CLASSES, N_CLASSES, dropout, reuse = True, is_training = False)
logits_val = conv_net(X_val, N_OUT_CLASSES, N_CLASSES, dropout, reuse = True, is_training = False)
logits_eye = conv_net(X_val, N_OUT_CLASSES, N_CLASSES, dropout, reuse = True, is_training = False)

print ('defined logits')

# Define the loss operation
loss_op = tf.constant(0.0, dtype = tf.float32)
for i in range(N_OUT_CLASSES):
    loss_op = loss_op + tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(\
    logits = logits_train[i], labels = Y[:,i]))

print ('defined loss op')

# Define loss and optimizer (with train logits, for dropout to take effect)
optimizer = tf.train.AdamOptimizer(learning_rate = learning_rate)
train_op = optimizer.minimize(loss_op)

# Define loss for prediction on training dataset
correct_pred_train = tf.constant(0.0, dtype = tf.float32)
for i in range(N_OUT_CLASSES):
    correct_pred_train = correct_pred_train + tf.cast(tf.equal(tf.argmax(logits_test[i], 1), tf.cast(Y[:,i], tf.int64)), tf.float32)
accuracy_train = tf.reduce_mean(correct_pred_train)

# Define loss for prediction ong validation dataset
correct_pred_val = tf.constant(0.0, dtype = tf.float32)
for i in range(N_OUT_CLASSES):
    correct_pred_val = correct_pred_val + tf.cast(tf.equal(tf.argmax(logits_val[i], 1), tf.cast(Y_val[:,i], tf.int64)), tf.float32)
accuracy_val = tf.reduce_mean(correct_pred_val)

# Initialize the variables (i.e. assign their default value)
init = tf.global_variables_initializer()
saver = tf.train.Saver()

print ('defined other, start session')

with tf.Session() as sess:
    # Run the initializer
    sess.run(init)
    # Start the data queue
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess = sess, coord = coord)

    # Training cycle
    for step in range(1, num_steps+1):
        if step % display_step == 0:
            print 'run evaluation step'
            # Run optimization
            sess.run([train_op])
            # Calculate average batch loss and accuracy
            total_loss = 0.0
            training_accuracy = 0.0
            validation_accuracy = 0.0

            for i in range(10):
                loss, acc_train, acc_val = sess.run([loss_op, accuracy_train, accuracy_val]) 
                total_loss += loss
                training_accuracy += acc_train
                validation_accuracy += acc_val

            total_loss /= 10.0
            training_accuracy /= 10.0    
            validation_accuracy /= 10.0

            print("Step " + str(step) + ", Loss= " + \
                "{:.4f}".format(total_loss) + ", Training Accuracy= " + \
                "{:.3f}".format(training_accuracy) + ", Validation Accuracy= " + \
                "{:.3f}".format(validation_accuracy))
        else:
            # Only run the optimization op (backprop)
            print 'run training step'
            sess.run(train_op)

    print("Optimization Finished!")
    # Stop threads
    coord.request_stop()
    coord.join(threads)