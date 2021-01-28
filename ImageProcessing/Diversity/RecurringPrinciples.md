# Recurring principles for classifying objects in medical images

There is a wide range of structures that can be classified automatically for practical purposes. However, the underlying principles for training a machine to distinguish between different structures are very few.

Let's have a look at three basic principles applied to the following image:

![alt](http://www.weheartcv.com/wp-content/uploads/2015/01/unedged-e1421363165889.jpg) 

## Segmentation

The segmentation of the image (scans) into several objects of interest. In some cases, it is referred to as unsupervised learning or clustering.  
 
*What could be the objects of interest in this image?*
 
**Mock segmentation**
 
![alt](http://www.weheartcv.com/wp-content/uploads/2015/01/segmentation-e1420910874899.jpg)

The objects of interest are the little colored organisms. The segmentation delimited the objects with black edges and the separation is based on color. The background is red, while the foreground has other different colors.

## Feature Extraction

The extraction of relevant enough features in order to distinguish between the classes.

*What features have you observed so far in the objects extracted?*

**Mock feature extraction**

![alt](http://www.weheartcv.com/wp-content/uploads/2015/01/features_extr-e1420912524472.jpg)

The features that I extracted are **shape** (circular, slightly elongated and curved), **color** (yellow, green, blue and purple) and **orientation** (none, vertical, horizontal, toward northwest and northeast).

## Supervision

Supervision of the learning process (telling the machine which is the right category for a number of objects).

**Mock human labeling**

![alt](http://www.weheartcv.com/wp-content/uploads/2015/01/supervision-e1420913843854.jpg)

Given enough data and the proper learning model, a machine can learn different concepts based on which it can automatically classify the data fed to it.

*What concepts do you think a machine should learn in the mock example?*

*Are all the features relevant for the classification?*

The concepts that a machine is supposed to learn in the mock example are:

1. **Color** and **shape** can tell the age. 
	- baby organisms are yellow  
	- as they grow up they transition to blue  
	- young ones are circular  
	- mature ones are elongated and the old ones are curved
	
2. **Orientation** is irrelevant.
	- most of the categories(adolescents, matures) have different orientations  
	- this feature doesn't really tell us a lot about the category, so we can exclude it


This is how a machine typically learns from data. 