## Blood Spectroscopy Classification Challenge: Project Report

### 1. Blood Spectroscopy Flux

- The challenge and the dataset
- Tools: Julia & Flux
- Neural Network model: individual tasks
- Heavy overfitting on ok: unbalanced dataset

#### 1.1 Introduction

*Fig 1.1.1: spectroscopy sample*

#### 1.2 Team discussion

Although we are aware of how unbalanced the training data is (See Fig. 1), we decide on training 3 individual task neural networks (LDL, HDL, HGB) using the Flux package in Julia.

To begin with, we only use the absorption features in the range 1-170 and we train each of the 3 models to classify a spectroscopy sample as indicating "low" (1), "ok" (2) or "high" (3). The temperature and the humidity are disregarded for now because they are measured in different units (also based on x_train in the starter notebook).

![unbalanced](https://raw.githubusercontent.com/perticascatalin/Learning/master/MDA/imgs/unbalanced.png)

*Fig 1.2.1: unbalanced*

#### 1.3 Neural Network implementation using Flux

```
using Flux
m_ldl = Chain(
    Dense(170, 32, relu),
    Dense(32, 3),
    softmax)
```

```
datasetx_ldl = repeated((x_train, y_train_ldl), 1000)
C_ldl = collect(datasetx_ldl);
evalcb_ldl = () -> @show(loss(x_train,y_train_ldl))
ps_ldl = Flux.params(m_ldl)
```

```
loss(x, y) = Flux.crossentropy(m_ldl(x), y)
Flux.train!(loss, ps_ldl, datasetx_ldl, opt, cb = throttle(evalcb_ldl, 15))
```
![basic network](https://raw.githubusercontent.com/perticascatalin/Learning/master/MDA/imgs/basic_network.png)

*Fig 1.3.1: basic network - parameters*

|Measure     |LDL |HDL |HGB |
|:----------:|:--:|:--:|:--:|
|Accuracy    |56% |57% |89% |
|Loss (final)|0.83|0.93|0.42|

Except for one of the donation ids which included some of the HDL levels labeled as "high", all of the other measures overfitted to "ok" in all of the cases. However, one might be fooled by the accuracy levels indicated on the training dataset.

This can be explained if we look at the proportions of the "low" and "high" labels on each of the individual tasks. If a sample labeled "x" appears in y% of the dataset's samples, always guessing "x" will return an accuracy of y%, which is simply predicting the most commonly found label.

To note that on the contrary, by training the neural network with labels which don't coincide with the input data in the case of a balanced dataset, then at testing time, each of the 3 labels will be almost randomly guessed with equal probability (~33%, discovered later on through a bug). So we can conclude that the ability of the NN to learn the right parameters is heavily influenced by the dataset's statistics.

### 2. Balance the Dataset and Aggregate

- Balanced dataset
	- 13.140 samples
	- augment so that measure values are approx. the same for all categories
	- shuffle
	- ~30 min of training overall
- *Updated_Test.csv*
- Aggregation of predictions
	- low: -1, ok: 0, high: +1
	- sum up by donation id
	- 60 datapoints per patient
	- thresholds at -30 & +30
- Trial submission

Balancing the dataset: although we introduce a large bias towards the few data samples which we duplicate, the advantage gained is that we will correctly penalize the model at training time when attempting to classify as "ok" a measure which is either "low", or "high".

![balanced](https://raw.githubusercontent.com/perticascatalin/Learning/master/MDA/imgs/balanced.png)
*Fig 2.1: balanced*

|Measure     |LDL |HDL |HGB |
|:----------:|:--:|:--:|:--:|
|Accuracy    |54% |47% |51% |
|Loss (final)|0.95|1.05|0.93|

|Measure|No Samples|
|:-----:|:--------:|
|LDL    |18.540    |
|HDL    |21.360    |
|HGB    |31.500    |

These models no longer overfit on "ok" and we get ~30% correct predictions on 20% of the competition's test data for our trial submission.

### 3. Further considerations

- Further considerations
- *Update_train.csv*
	- Double-sized data: 29.160 samples
	- More training time: ~4h of training overall
- Another submission

|Measure     |LDL |HDL |HGB |
|:----------:|:--:|:--:|:--:|
|Accuracy    |58% |45% |49% |
|Loss (final)|0.90|1.05|0.98|

|Measure|No Samples|
|:-----:|:--------:|
|LDL    |43.680    |
|HDL    |43.380    |
|HGB    |75.240    |

Only 13.5% correct predictions. Not sure why.

### X. Documentation

- zindi\_starter\_julia\_notebook
- zindi\_individual\_julia\_notebook (section 1)
- zindi\_indi\_bal\_julia\_notebook (section 2)
- zindi\_julia\_notebook (section 3)