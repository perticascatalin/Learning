# Features for Bone Structures Classification


In this post I want to talk about a number of handmade features that can be used by a machine in order to learn how to label bone structures in medical images. 


[spoiler title = 'Do you know what features are?' collapse_link = 'true']

Examples that one can think of: 

Persons: short or long nose, eye color, hair color, height, age  
Cars: small or big engine, number of doors, color, price  

Any description of an observation (an image in our case) can be viewed in a broader way as a set of features.

[/spoiler]

[spoiler title = 'Do you know why features are important?' collapse_link = 'true']

Machines can be trained to perform a task by correlating features of the input to the desired output. How well the machine is trained depends a lot on what features it observes in the input.

[/spoiler]

[spoiler title = 'Why classify bone structures?' collapse_link = 'true']

Classifying bone structures can help the computer establish where other parts of the body are, like risk structures for example. This can be used in automated planning of surgeries or other interventions, such as radiotherapy.

[/spoiler]


These features work for segmentations with different granularity, but the amount of data required by the machine to learn the right concepts out of the given features might differ. 

[spoiler title = 'Do you know what a segmentation is?' collapse_link = 'true']

Segmenting an image means to divide it in a way such that you can identify different subjects to investigate.

[/spoiler]

[spoiler title = 'What does granularity refer to?' collapse_link = 'true']

Whether segmenting the image produces larger or smaller pieces.

[/spoiler]

[spoiler title = 'How does a machine learn concepts from data?' collapse_link = 'true']

The machine does this by investigating a lot of already annotated (labeled) data. In some cases it might do this by estimating how strong one feature influences the result. 

[/spoiler]

So here is the list of features for bone structures that I have come up with:

## Bone shape
 
We need to compare the shape of the bone with mathematically defined shapes in order to obtain a value to work with - **Circularity**, **Elongation**, **Principal Components** and others.

The skull is spherical, with a large volume contained inside.
The scapula is flat, covering a large area.
Leg bones and arm bones are elongated, like thin cylinders with robust ends. Every bone type presents its own peculiarity.

**Skull**

![alt](http://www.weheartcv.com/wp-content/uploads/2015/01/skulls.jpg)

**Scapula**

![alt](http://www.weheartcv.com/wp-content/uploads/2015/01/scapulas.jpg)

**Clavicle**

![alt](http://www.weheartcv.com/wp-content/uploads/2015/01/clavicles.jpg)

**Humerus**

![alt](http://www.weheartcv.com/wp-content/uploads/2015/01/humerus.jpg)   
    
## Relative position or distance
(**to structures that are easier to label**)  

Humans use spatial information to assess the identity of an object (eg. You would neither search for sugar in the diary products section of a supermarket, nor for the heart anywhere else than in the thorax region). Machines can also acquire this type of intuition. 

The ribs are very close to the lungs. The skull to the brain. Some bone structures have protective purposes for vital organs and thus we are able to find bones in their proximity. 

**Bone structures and their proximity to other structures**

![alt](http://www.weheartcv.com/wp-content/uploads/2015/01/feature-distance-e1421431013523.jpg)
	
## Orientation

If the body position remains unchanged, bones approximately maintain the same orientation/angle.

The spine follows a longitudinal line, while other bones like the clavicles are positioned diagonally, pointing to the sternum. 

**Orientation of the bones in the thoracic cage**

![alt](http://www.weheartcv.com/wp-content/uploads/2015/01/oriented-e1421536830270.jpg)

## Size 
(**Volume**, **Area**, **Perimeter**)

Leg, arm, foot and hand bones can have similar shapes and orientation, so using just these 2 features for training a classifier could lead to inaccurate results (assuming you want to decide between the 4 categories mentioned above). But the first two categories are many times larger in size than the rest. Thus the size of an object can also be used as a feature for learning, among others.

**The size of different bones**

![alt](http://www.weheartcv.com/wp-content/uploads/2015/01/bone_size-e1421536037245.jpg)


