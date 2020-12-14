# Constraint Programming applied to Music: Report

### Abstract

### Goals

- Briefly look over music theory to understand how musical patterns are represented
- Provide background on computer assisted (musical) composition
- Investigate combinatorial problems resulting from modelling musical patterns as CSPs
- Experimental part left as future work

## 1. Introduction

Music is known to have a mathematical structure at its basis, .... some link to [M0] ... although what was considered acceptable varied greatly across different periods, trends and genres in music.

The purpose and how we reach them:

Section 2: Basics in Music Theory: 
	- Melody, Harmony, Rhythm, Bass
	- Representation, Notes, Intervals, Scales, Chords, Arpegios

Section 3: Background on previous Experiments that:
	- relate Music to Mathematics (& AI in general)
	- use Software to generate or compose Music

Section 4: Model Musical Patterns using CSP

## 2. The Basics in Music Theory

|Musical Representation|Explanation|
|:-----------------------:|-----------|
|![Standard Scale](https://raw.githubusercontent.com/perticascatalin/open_nenos/master/DPML/imgs/scale.png)|Western music has a 12 note musical system. These can be obtained by taking the 7 basic notes (**A, B, C, D, E, F, G**) and then augmenting (# sharp) or diminishing (b bemol) each with half a tone (semitone).|
|![Circle of Tonality](https://raw.githubusercontent.com/perticascatalin/open_nenos/master/DPML/imgs/notes_circle.png)|To note that the distance between notes varies, thus we have **1 tone** between G-A, A-B, C-D, D-E, F-G and **1 semitone** between B-C and E-F. In the first image we have standard G tuning (key). Note that from G onwards, the notes repeat themselves (same notes, but higher pitch). This is referred to as **octaviation** (8 notes to get back to where we were). See second image ([image source](https://ezra-sandzer-bell.medium.com/music-theory-foundations-in-a-few-lines-of-code-90026efb5b23)).|
|![Major Scale Intervals](https://github.com/perticascatalin/open_nenos/blob/master/DPML/imgs/c_scale.png?raw=true)|smth|

## 3. Linking Music to Mathematics & AI

### 3.1 Generative RNNs for Musical Composition

There have been numerous attempts to generate music using software. One of the first approaches that I heard of is [M5] - [video source](https://www.youtube.com/watch?v=A2gyidoFsoI) & [tutorial](https://www.danieldjohnson.com/2015/08/03/composing-music-with-recurrent-neural-networks/), which leverages the generative power of recurrent neural networks based on many musical pieces as training data. This approach focuses on classical music (Bach) and polyphony (several instrumental tracks). RNNs and other neural networks derived from them will usually map an input sequence to an output sequence (the NN learns the mapping from the input to the output based on history and current input). However, we can also feed an RNN its own output and thus generate a potentially novel sequence - eg. generating a handwritten sequence in [M6]. Earlier studies for how to generate music using RNNs/LSTMs include [M7].

### 3.2 Ideas from GEB: Canons & Fugues

## 4. Modelling Musical Patterns through Constraint Programming



## 5. Conclusions

### References

- [M0] How Music Works (Melody, Rhythm, Harmony, Bass), documentary, Howard Goodall, 2006
- [M1] Gelisp: A Library to Represent Musical CSPs and Search Strategies, M. Toro et al., 2015, *ArXiv: Artificial Intelligence*
- [M2] Musical Constraint Satisfaction Problems Solved with Adaptive Search, C. Truchet & P. Codognet, 2004, *Soft Computing, Springer Verlag*
- [M3] Goedel, Escher, Bach: An Eternal Golden Braid, Douglas Hofstadter, 1979, *Basic Books*
- [M4] Introducere in Studiul Chitarei Electrice, Andrei Rosulescu, 2008
- [M5] Generating Polyphonic Music using Tied Parallel Networks, Daniel D. Johnson, 2017, *International Conference on Evolutionary and Biologically Inspired Music, Sound, Art and Design*
- [M6] Generating Sequences with Recurrent Neural Networks, Alex Graves, 2014, *ArXiv: Neural and Evolutionary Computing*
- [M7] A First Look at Music Composition using LSTM Recurrent Neural Networks, Douglas Eck & Juergen Schmidthueber, 2002, *Technical Report IDSIA*