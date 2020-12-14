# Constraint Programming applied to Music: Report

### Abstract

### Goals

- Briefly look over music theory to understand how musical patterns are represented
- Provide background on computer assisted (musical) composition
- Investigate combinatorial problems resulting from modelling musical patterns as CSPs
- Experimental part left as future work

## 1. Introduction

Music is known to have a mathematical structure at its basis, .... some link to [M0] ... although what was considered acceptable varied greatly across different periods, trends and genres in music.

The purpose of the paper and how we reach it:

Section 2: Music Theory Background: 
	- Melody, Harmony, Rhythm, Bass
	- Representation, Musical Notes, Intervals, Scales, Chords, Arpeggios

Section 3: Background on previous Experiments that:
	- relate Music to Mathematics (& AI in general)
	- use Software to generate or compose Music

Section 4: Model Musical Patterns using CSP

## 2. Music Theory Background

**Definitions**:

- **Interval**: the distance between 2 sounds (musical notes). 
- **Scale**: a succession of musical notes adhering to a musical pattern. For instance, the major scale is comprised of the following intervals: TTSTTTSTTSTTTSTTSTTTS... (T = tone, S = semitone)
- **Chord**: a group of musical notes which are played together.
- **Arpeggio**: a succession of musical notes extracted from a chord (played successively instead of together).

For our purpose to apply CSP to music, the most important part to understand are intervals & scales. Thus, in the coming paragraphs I will focus on their representation. Chords & arpeggios are slightly more advanced musical topics and studying them does not necessarily help towards realizing the purpose of this study.

|Musical Representation|Explanation|
|:-----------------------:|-----------|
|![Standard Scale](https://raw.githubusercontent.com/perticascatalin/open_nenos/master/DPML/imgs/scale.png)|Western music has a 12 note musical system. These can be obtained by taking the 7 basic notes (**A, B, C, D, E, F, G**) and then augmenting (# sharp) or diminishing (b bemol) each with half a tone (semitone). The image to the left showcases a score with standard G tuning (key).|
|![Circle of Tonality](https://raw.githubusercontent.com/perticascatalin/open_nenos/master/DPML/imgs/notes_circle.png)|To note that the distance between notes varies, thus we have **1 tone** between G-A, A-B, C-D, D-E, F-G and **1 semitone** between B-C and E-F. Note that from G onwards, the notes repeat themselves (same notes, but higher pitch). This is referred to as **octaviation** (8 notes to get back to where we were). See image to the left ([image source](https://ezra-sandzer-bell.medium.com/music-theory-foundations-in-a-few-lines-of-code-90026efb5b23)).|
|![Major Scale Intervals](https://github.com/perticascatalin/open_nenos/blob/master/DPML/imgs/c_scale.png?raw=true)|**The Major Scale** is comprised of 5 tones and 2 semitones. The image to the left shows the C major scale (**C-D-E-F-G-A-B-C**) together with its intervals. By transposing 1 tone higher, we get the D major scale (**D-E-F#-G-A-B-C#-D**). Image source and explanation from [M4].|

**Interval Notation** (source: [M4]):

|A-B Example|Name|Notation|
|:---------:|:--:|:------:|
|C1-C1|unison (perfect)|1P|
|C-C#|augmented unison (semitone)|1+|
|C-Db|minor second (semitone)|2m|
|C-D|major second (tone)|2M|
|C-D#|augmented second (tone + semitone)|2+|
|C-Eb|minor third (tone + semitone)|3m|
|C-E|major third (2 tones)|3M|
|...|...|...|

[More on intervals quality](https://www.earmaster.com/wiki/music-memos/what-are-intervals-in-music.html) - Perfect, Diminished, Augmented, Major & Minor

[Musical Notes to Frequency](https://www.audiology.org/sites/default/files/ChasinConversionChart.pdf)

[Human Hearing Frequency Range](https://www.ncbi.nlm.nih.gov/books/NBK10924/#:~:text=Humans%20can%20detect%20sounds%20in,to%2015%E2%80%9317%20kHz.)

## 3. Linking Music to Mathematics & AI

### 3.1 Generative RNNs for Musical Composition

There have been numerous attempts to generate music using software. One of the first approaches that I heard of is [M5] - [video source](https://www.youtube.com/watch?v=A2gyidoFsoI) & [tutorial](https://www.danieldjohnson.com/2015/08/03/composing-music-with-recurrent-neural-networks/), which leverages the generative power of recurrent neural networks based on many musical pieces as training data. This approach focuses on classical music (Bach) and polyphony (several instrumental tracks). RNNs and other neural networks derived from them will usually map an input sequence to an output sequence (the NN learns the mapping from the input to the output based on history and current input). However, we can also feed an RNN its own output and thus generate a potentially novel sequence - eg. generating a handwritten sequence in [M6]. Earlier studies for how to generate music using RNNs/LSTMs include [M7].

### 3.2 Ideas from GEB: Canons & Fugues

While reading through Douglas Hofstadter's book [M3], I came across these interesting musical constructs (canons & fugues), which could serve as a nice application of constraint programming to music. For instance, canons are musical pieces which begin by playing a theme and then after a time delay a second voice begins playing the same theme (possibly in a different key or inverted). Whichever is the case, the challenge is to harmonize the theme with itself given the time delay, or find a variation of the initial theme which is in harmony. Although Hofstadter showcases these musical examples to support the idea that strange loops (& self-reference) appear in numerous forms (including Bach's compositions and Esher's drawings), one can imagine solving the harmonization of a theme with itself or its inversions by using constraint programming. 

*"In order for a theme to work as a canon theme, each of its notes must be able to
serve in a dual (or triple, or quadruple) role: it must firstly be part of a melody, and
secondly it must be part of a harmonization of the same melody"* - [M3].

## 4. Modelling Musical Patterns through Constraint Programming

[M1] showcases 2 applications of constraint programming in music, which I detail in sections 4.1 and 4.2.

### 4.1 All Interval Series

This problem requires finding all the sequences consisting of 12 different pitches with 12 different intervals. It can be formalized as follows:

- variables `v_1`, `v_2` ... `v_n` with domains `[1..n]`, `[1..n]` ... `[1..n]`
- `all_diff(v_i)`
- `all_diff((v_i+1 - v_i) % n)`, `i <= n-1`

### 4.2 Jarrell's CSP

Automatically generate music by finding a sequence of n musical notes and applying a set of rules/ constraints. These are:

- fixed number of occurences for motives (a motif is a sequence of intervals)
- each note from the output should belong to a chord (from a preset collection of chords?)

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