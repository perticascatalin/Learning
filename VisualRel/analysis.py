import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from mpl_toolkits.mplot3d import Axes3D
import pdb

def debugger(correct_pred, logits, y_exp, x):
	N_OUT_CLASSES = 58
	print (str(int(correct_pred[0])) + " out of " + str(N_OUT_CLASSES))

def print_1by1(arr, title):
	N_OUT_CLASSES = 58
	line = ""
	for i in range(N_OUT_CLASSES):
		line += (str(int(arr[i])) + " ")
	print (title + line)

def print_pretty(correct_pred, logits, y_exp, x, epoch):
	N_OUT_CLASSES = 58
	out = list()
	y_pred = list()
	for j in range(N_OUT_CLASSES):
		y_pred.append(np.argmax(logits[j][0]))
	print_1by1(y_exp[0], 'expect:')
	print_1by1(y_pred, 'pred:  ')
