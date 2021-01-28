import cv2
import random
import sys
import numpy as np
from sklearn.cluster import MeanShift

# applies mean shift clustering and returns the labeled samples
def mean_shift_clustering(features, bandwidth):
	ms = MeanShift(bandwidth = bandwidth, bin_seeding = True)
	ms.fit(features)
	labels = ms.labels_
	return labels

# finds the edges in the image(the regions where there are abrupt changes in intensities)
def get_edges(img):
	edges = cv2.Canny(img, threshold1=10, threshold2=70)
	cv2.imwrite('canny.png', edges)
	return edges

# prepares the image for clustering and outputs an image showing the formed clusters
def apply_mean_shift_clustering(img, with_edges):
	n = img.shape[0]
	m = img.shape[1]

	# preprocess the image for segmentation
	edges = get_edges(img)
	features = np.zeros((n*m, 5), np.uint8)
	for i in range(n):
		for j in range(m):
			features[i*m + j] = (i, j, img[i,j,0]/2, img[i,j,1]/2, img[i,j,2]/2)
			if (with_edges and edges[i, j]):
				features[i*m + j] = (0, 0, 255, 255, 255)

	# apply clustering
	labels = mean_shift_clustering(features, 17)

	# output the clusters in a nice way(for each cluster we take the mean intensity)
	which_cluster = np.zeros((n, m), np.uint8)
	unique_labels = np.unique(labels)
	sums = np.zeros((len(unique_labels), 3), np.float32)
	how_many = np.zeros((len(unique_labels)), np.float32)
	color_given = np.zeros((len(unique_labels), 3), np.uint8)

	for i in range(n):
		for j in range(m):
			cur_label = labels[i*m + j]
			which_cluster[i,j] = cur_label
			sums[cur_label, 0] += img[i, j, 0]
			print sums[cur_label, 0], '0'
			sums[cur_label, 1] += img[i, j, 1]
			print sums[cur_label, 1], '1'
			sums[cur_label, 2] += img[i, j, 2]
			print sums[cur_label, 2], '2'
			how_many[cur_label] += 1

	for i in range(len(color_given)):
		if (how_many[i] < 1):
			continue
		color_given[i] = (int(sums[i,0]/how_many[i]), int(sums[i,1]/how_many[i]), int(sums[i,2]/how_many[i]))

	clusters = np.zeros((n, m, 3), np.uint8)
	for i in range(n):
		for j in range(m):
			if (with_edges and edges[i,j]):
				clusters[i,j] = (255,255,255)
			else:
				clusters[i,j] = color_given[which_cluster[i,j]]

	cv2.imwrite('clusters.png', clusters)

	print len(np.unique(labels));


img = cv2.imread('apples_oranges.png', 1)
ratio = 250.0 / img.shape[1]
rows = 250
cols = int(ratio * img.shape[0])
img = cv2.resize(img, (rows, cols), interpolation = cv2.INTER_AREA)
img = cv2.GaussianBlur(img, (5,5), 0)
n = img.shape[0]
m = img.shape[1]
print n, m
val = bool(sys.argv[1])
#apply_mean_shift_clustering(img, val)
get_edges(img)
