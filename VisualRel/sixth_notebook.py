# 7. Test NN

# Summary
# 1. read data and conv net from multi_class multi_labels (open_nenos)
# 2. outputs from neural_net (ME) (to check N_OUT_CLASSES vs. N_CLASSES)
# 3. took out evaluation of inputs, custom prints and saving data

# 4. scheduled training
# 5. batch accuracy

# 6.r loss defined as mean, maybe change penalization
# the current loss can get stuck in local minima (eg. always choose background)
# 7.r the network capacity might be too low for medium ds
# thus without being able to capture the data properties it always predicts background

# 8. evaluation - more than one batch (todo)
# 9. training time - more iterations (doing)


import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import fifth_notebook as data
import tensorflow as tf
import analysis as co
import pickle

# General architecture

IMG_SZ = 32
INPUT_DIR = './medium_grid_cells/'
VAL_DIR = './medium_val_grid_cells/'
BATCH_SZ = 64
IMG_HEIGHT = IMG_SZ
IMG_WIDTH = IMG_SZ

N_CLASSES = 2 
N_OUT_CLASSES = 58 # total number of classes

# Parameters
learning_rate_1 = 0.001
learning_rate_2 = 0.0005
learning_rate_3 = 0.0001

num_steps = 18000
display_step = 1000

# Network Parameters
dropout = 0.6 # Dropout, probability to keep units

# Change limit_background to include background grid cells
X, Y = data.read_images(input_directory = INPUT_DIR, batch_size = BATCH_SZ, limit_background = True)
print ('finished reading train images')
X_val, Y_val = data.read_images(input_directory = VAL_DIR, batch_size = BATCH_SZ, limit_background = True)
print ('finished reading validation images')

# Create model
def conv_net(x, num_classes, num_labels, dropout, reuse, is_training):
    # Define a scope for reusing the variables
    with tf.variable_scope('ConvNet', reuse=reuse):

        # Convolution Layer with 32 filters and a kernel size of 4
        conv1 = tf.layers.conv2d(x, 32, 4, activation=tf.nn.relu)
        # Max Pooling (down-sampling) with strides of 2 and kernel size of 2
        conv1 = tf.layers.max_pooling2d(conv1, 2, 2)

        # Convolution Layer with 64 filters and a kernel size of 4
        conv2 = tf.layers.conv2d(conv1, 64, 4, activation=tf.nn.relu)
        # Max Pooling (down-sampling) with strides of 2 and kernel size of 2
        conv2 = tf.layers.max_pooling2d(conv2, 2, 2)

        # Flatten the data to a 1-D vector for the fully connected layer
        fc1 = tf.contrib.layers.flatten(conv2)

        # Fully connected layer (in contrib folder for now)
        fc1 = tf.layers.dense(fc1, 256)
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

# Define the loss operation
loss_op = tf.constant(0.0, dtype = tf.float32)
for i in range(N_OUT_CLASSES):
    loss_op = loss_op + tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(\
    logits = logits_train[i], labels = Y[:,i]))

# Define loss and optimizer (with train logits, for dropout to take effect)
optimizer_1 = tf.train.AdamOptimizer(learning_rate = learning_rate_1)
train_op_1 = optimizer_1.minimize(loss_op)
optimizer_2 = tf.train.AdamOptimizer(learning_rate = learning_rate_2)
train_op_2 = optimizer_2.minimize(loss_op)
optimizer_3 = tf.train.AdamOptimizer(learning_rate = learning_rate_3)
train_op_3 = optimizer_3.minimize(loss_op)

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

THRESH_1 = 3000
THRESH_2 = 6000
with tf.Session() as sess:
    # Run the initializer
    sess.run(init)
    # Start the data queue
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess = sess, coord = coord)

    # Training cycle
    for step in range(1, num_steps+1):
        if step % display_step == 0:
            # Run optimization
            if step <= THRESH_1:
                sess.run([train_op_1])
            elif step <= THRESH_2:
                sess.run([train_op_2])
            else:
                sess.run([train_op_3])
            # Calculate average batch loss and accuracy
            total_loss = 0.0
            training_accuracy = 0.0
            validation_accuracy = 0.0

            RUNS = 100
            for i in range(RUNS):
                loss, acc_train, acc_val = sess.run([loss_op, accuracy_train, accuracy_val]) 
                if i == 0:
                    correct_pred, logits, y_exp, x = sess.run([correct_pred_val, logits_val, Y_val, X_val])
                    co.debugger(correct_pred, logits, y_exp, x)
                    co.print_pretty(correct_pred, logits, y_exp, x, step)
                    co.batch_accuracy(correct_pred, logits, y_exp, x, step)
                total_loss += loss
                training_accuracy += acc_train
                validation_accuracy += acc_val

            total_loss /= float(RUNS)
            training_accuracy /= (N_OUT_CLASSES * float(RUNS))
            validation_accuracy /= (N_OUT_CLASSES * float(RUNS))

            print("Step " + str(step) + ", Loss= " + \
                "{:.4f}".format(total_loss) + ", Training Accuracy= " + \
                "{:.3f}".format(training_accuracy) + ", Validation Accuracy= " + \
                "{:.3f}".format(validation_accuracy))
        else:
            # Only run the optimization op (backprop)
            if step <= THRESH_1:
                sess.run([train_op_1])
            elif step <= THRESH_2:
                sess.run([train_op_2])
            else:
                sess.run([train_op_3])

    print("Optimization Finished!")
    # Stop threads
    coord.request_stop()
    coord.join(threads)