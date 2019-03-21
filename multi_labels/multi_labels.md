# Multi-Label Classification

## Introduction

In the problem described here we look at the advantages of using the same learning model for inferring different properties of objects. For instance, we create a toy dataset with 2D shapes which can have 3 classes of colors and 3 classes of shapes. The initial problem we wanted to model was given a set of multiple choices tests written by hand, extract the chosen answer for each question in an automatic way.

## Dataset

- 28 x 28 x 3 sized images
- 2 labels: shape and color
- shapes: square, circle, triangle
- colors: red, green, blue

| Sample | Description | Sample | Description |
|:------:|:-----------:|:------:|:-----------:|
|![Sample 1](https://raw.githubusercontent.com/perticascatalin/HiddenDimensions/master/documentation/MLSC/373_square_red.png "Sample 1")| red square |![Sample 5](https://raw.githubusercontent.com/perticascatalin/HiddenDimensions/master/documentation/MLSC/560_triangle_red.png "Sample 5")| red triangle |
|![Sample 2](https://raw.githubusercontent.com/perticascatalin/HiddenDimensions/master/documentation/MLSC/402_circle_blue.png "Sample 2")| blue circle |![Sample 6](https://raw.githubusercontent.com/perticascatalin/HiddenDimensions/master/documentation/MLSC/573_circle_red.png "Sample 6")| red circle |
|![Sample 3](https://raw.githubusercontent.com/perticascatalin/HiddenDimensions/master/documentation/MLSC/418_square_green.png "Sample 3")| green square |![Sample 7](https://raw.githubusercontent.com/perticascatalin/HiddenDimensions/master/documentation/MLSC/569_triangle_blue.png "Sample 7")| blue triangle |
|![Sample 4](https://raw.githubusercontent.com/perticascatalin/HiddenDimensions/master/documentation/MLSC/500_triangle_green.png "Sample 4")| green triangle |![Sample 8](https://raw.githubusercontent.com/perticascatalin/HiddenDimensions/master/documentation/MLSC/598_square_blue.png "Sample 8")| blue square |

**Dataset Purpose**:

- explore multi-label, multi-class classification problem
- 3 options: 
	- multi-label (multiple logit sets)
	- combination of labels (one logit set, each logit is a combo)
	- one neural-network for each label