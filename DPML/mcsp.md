# Constraint Satisfaction in Music: Report

### Abstract

Music is a special kind of art form because of the following duality: it is created from inspiration, but at the same time, it has a mathematical basis - its representation is very clear and precise and sounds need to follow certain rules in order to be compatible with each other and to create a pleasant response in the listener's mind.

In recent years there have been a number of attempts to compose music in an autonomous way by using machine learning techniques. **This study attempts to explore some of the basics in music theory in order to identify constraint satisfaction problems in music and to find out ways in which constraint programming could be applied to music.** The focus is not to automatically generate music, but rather to identify ways of leveraging declarative programming and search techniques for the purpose of solving harmony and melody problems ([M2]), which is what many human composers do "manually" or "by ear".

Therefore, the fundamental premise is not to try and automate music composition, but to assist fitting musical patterns together through the use of computational power in searching for potential solutions adhering to the required musical rules. The examples in this study range from classical music canons to rock songs improvisation & harmonization. **These will illustrate how harmony, melody, intervals and chords can be defined using sets and then how these relate to each other based on constraints extracted from music theory.**

### Goals

- Briefly look over music theory to understand how musical patterns are represented
- Provide background on computer assisted composition (background research)
- Investigate combinatorial problems resulting from modelling musical patterns as CSPs
- Experimental work in progress

## 1. Introduction

Music is an art form which has been constanly developing for centuries now. We often listen to music to enhance or change our mood and therefore we can consider it as the most accessible form of art in our everyday lives. Disregarding the more experimental type of music, one can notice that although an art form, music has a bit of a rigid structure and adheres to certain rules in order to make it pleasant to the human ear. However, what was considered acceptable/pleasant music varied greatly across different periods, cultures, trends and genres in music - Howard Goodall explains this very well in [M0], a documentary about the general mechanisms underlying music. Even so, it is generally agreed upon that music has a mathematical structure at its basis.

The purpose of this study is to explore the fundamentals of music and its mathematical structures in order to get an idea on how to leverage constraint programing in the process of fitting musical themes together. A very good example of this idea will be showcased later on in Section 3.2, where I take a brief look into how classical music canons are constructed. I believe that canons show some potential to be modelled as constraint satisfaction problems as long as we are able to encode the rules of harmonization into constraints. Additionally, we are required to have the musical themes available (as a sequence of notes for instance). Then the task is to find the right overlaps of musical themes such that the notes played at the same time (belonging to different themes) are in harmony at each step. 


**TODO 1: Shoud revise because lacks development wrt. the abstract**

A similar idea is tackled for the structure of a rock song in section 4.6.

## 2. Music Theory Background

**Definitions**:

- **Interval**: the distance between 2 sounds (musical notes). 
- **Scale**: a succession of musical notes adhering to a musical pattern. For instance, the major scale is comprised of the following intervals: TTSTTTSTTSTTTSTTSTTTS... (T = tone, S = semitone)
- **Chord**: a group of musical notes which are played together.
- **Arpeggio**: a succession of musical notes extracted from a chord (played successively instead of together).

For our purpose to apply CSP to music, the most important part to understand are intervals & scales. Thus, in the coming paragraphs I will focus on their representation. Chords & arpeggios are slightly more advanced musical topics and studying them does not necessarily help towards realizing the purpose of this study.

**Table 1. Basic Concepts**:

|Musical Representation|Explanation|
|:-----------------------:|-----------|
|![Standard Scale](https://raw.githubusercontent.com/perticascatalin/open_nenos/master/DPML/imgs/scale.png)|Western music has a 12 note musical system. These can be obtained by taking the 7 basic notes (**A, B, C, D, E, F, G**) and then augmenting (# - sharp) or diminishing (b - flat) each with half a tone (semitone). The image to the left showcases a score with standard G tuning (key).|
|![Circle of Tonality](https://raw.githubusercontent.com/perticascatalin/open_nenos/master/DPML/imgs/notes_circle.png)|To note that the distance between notes varies, thus we have **1 tone** between G-A, A-B, C-D, D-E, F-G and **1 semitone** between B-C and E-F. Note that from G onwards, the notes repeat themselves (same notes, but higher pitch). This is referred to as **octaviation** (8 notes to get back to where we were). See image to the left ([image source](https://ezra-sandzer-bell.medium.com/music-theory-foundations-in-a-few-lines-of-code-90026efb5b23)).|
|![Major Scale Intervals](https://github.com/perticascatalin/open_nenos/blob/master/DPML/imgs/c_scale.png?raw=true)|**The Major Scale** is comprised of 5 tones and 2 semitones. The image to the left shows the C major scale (**C-D-E-F-G-A-B-C**) together with its intervals. By transposing 1 tone higher, we get the D major scale (**D-E-F#-G-A-B-C#-D**). Image source and explanation from [M4].|

**Table 2. Interval Notation** (source: [M4]):

|A-B Example|Name|Notation|Value|
|:---------:|:--:|:------:|:---:|
|C0-C0|unison (perfect)|1P|0|
|C-C#|augmented unison (semitone)|1+|0.5|
|C-Db|minor second (semitone)|2m|0.5|
|C-D|major second (tone)|2M|1|
|C-D#|augmented second (tone + semitone)|2+|1.5|
|C-Eb|minor third (tone + semitone)|3m|1.5|
|C-E|major third (2 tones)|3M|2|
|...|...|...|

**Note 1**: Even if the number of steps in an interval are equal (eg. both 2+ and 3m are 1 tone + 1 semitone long), their quality might differ and therefore their sound effect as well. This is where the distinction between an interval's quantity vs. quality appears.

[More on intervals quality](https://www.earmaster.com/wiki/music-memos/what-are-intervals-in-music.html) - Perfect, Diminished, Augmented, Major & Minor

[Musical Notes to Frequency](https://www.audiology.org/sites/default/files/ChasinConversionChart.pdf) - Eg: C0 at 16hz, C1 at 32hz ...

[Human Hearing Frequency Range](https://www.ncbi.nlm.nih.gov/books/NBK10924/#:~:text=Humans%20can%20detect%20sounds%20in,to%2015%E2%80%9317%20kHz.) - Eg: 20hz - 20khz.

## 3. Linking Music to Mathematics & AI

### 3.1 Generative RNNs for Musical Composition

There have been numerous attempts to generate music using software. One of the first approaches that I heard of is [M5] - [video source](https://www.youtube.com/watch?v=A2gyidoFsoI) & [tutorial](https://www.danieldjohnson.com/2015/08/03/composing-music-with-recurrent-neural-networks/). The experiment leverages the generative power of recurrent neural networks by using many musical pieces as training data. This approach focuses on classical music (Bach) and polyphony (several instrumental tracks). RNNs and other neural networks derived from them will usually map an input sequence to an output sequence (the NN learns the mapping from the input to the output based on history and current input). However, we can also feed an RNN its own output and thus generate a potentially novel sequence - eg. generating a handwritten sequence in [M6]. Another study on how to generate music using RNNs/LSTMs is [M7].

Whether deep learning with recurrent neural networks can actually compose new pieces of music of some artistic value is a debatable question. One reason to doubt this is that the whole mechanism of deep learning relies on some form of imitation. So the resulting music will be a hybrid comprised of the previously seen musical patterns at the best. In this sense, a loss function will not be able to compose a piece of music the way a human composer would do, because a composer would make music based on some deep internal senses or feelings, which are the result of real life human experience (I am not referring to general commercial music when making this statement). However, these generative systems look promising from the perspective of playing with music, creating variations and re-mixes, not in the sense of creating new music, but rather as an aiding system.

### 3.2 Ideas from GEB: Canons & Fugues

While reading through Douglas Hofstadter's book [M3], I came across these interesting musical constructs (canons & fugues), which could serve as a nice application of constraint programming to music. For instance, canons are musical pieces which begin by playing a theme and then after a time delay a second voice begins playing the same theme (possibly in a different key or inverted). Whichever is the case, the challenge is to harmonize the theme with itself given the time delay, or find a variation of the initial theme which is in harmony. Although Hofstadter showcases these musical examples to support the idea that strange loops (& self-reference) appear in numerous forms (including Bach's compositions and Esher's drawings), one can imagine solving the harmonization of a theme with itself or its inversions by using constraint programming. 

*"In order for a theme to work as a canon theme, each of its notes must be able to
serve in a dual (or triple, or quadruple) role: it must firstly be part of a melody, and
secondly it must be part of a harmonization of the same melody"* - [M3].

Musical Samples mentioned in [M3]:

- [Good King Wenceslas](https://www.youtube.com/watch?v=SQVUMG6LZGM), a christmas carol, fairly simple structure, but very melodic and pleasant
- [Crab Canon](https://www.youtube.com/watch?v=xUHQ2ybTejU), same theme played forwards and backwards at the same time, great symmetries

## 4. Modelling Musical Patterns through Constraint Programming

My starting point for modelling musical patterns using constraint programming are the ideas presented in [M1] and [M2]. This section showcases these ideas and makes further progress in formalizing the discovered problems as constraint satisfaction problems.[M1] showcases 2 applications of constraint programming in music, which I detail in sections 4.1 and 4.2. The 2 problems are solved by declaring variables and constraints using graphical interfaces linked to a lisp solver and the open music visual programming environment. The same problems are showcased in [M2] as problems 8 and 9 in the *(2.3) Melodies* section. Additionally, [M2] presents some applications to musical harmony: problems 1,2 & 3 in the *(2.1) Harmony* section. I detail and analyze these problems in sections 4.3, 4.4 and 4.5.

Based on these related studies,I make my own attempt at modelling a rock song harmonization as a CSP in section 4.6 (**TODO 2: Should Change because you don't say nothing**).

### 4.1 All Interval Series

This problem requires finding all the sequences consisting of 12 different pitches with 12 different intervals. It can be formalized as follows:

- variables `v_1`, `v_2` ... `v_n` with domains `[1..n]`, `[1..n]` ... `[1..n]`
- `all_diff(v_i)`
- `all_diff((v_i+1 - v_i) % n)`, `i <= n-1`

**Note 2**: the above assumes that the notes (from a whole chromatic scale) are labeled as integers: `1, 2, ..., 12`. These will represent the notes `A, A#, B, C, ... G, G#` in an octave, with `n = 12`. Depending on the use case, we might want to use notes or pitches (= notes + octave, then we go above 12, but 13 will simply represent note 1, but an octave higher - eg. if note 1 is C0, then note 13 is C1). However, in my own experiments, I use `0, 0.5, 1, ..., 6` instead, so that intervals (the distance between 2 notes) are then directly measured in tones, like they are in music (eg. `tone + semitone = 1.5`, and not 3).

Although the related studies do not mention this, the concept of using 12 different pitches / notes (from the chromatic scale) within any contiguous sequence of 12 notes is the basis for the **twelve-tone serialism** method of composition. This originated in the 1920s (see [M8]), so it is a very modern approach to musical composition. The purpose of using 12 different pitches is for the melody not to belong to a specific key.

[Sample from serialist composer Schoenberg](https://www.youtube.com/watch?v=vqODySSxYpc)

### 4.2 Michael Jarrel: Automated Generation of Music through Search

This application attempts to formalize a kind of automated generation of music by searching for a sequence of n musical notes which adhere to a set of rules / constraints. These are:

- starting and ending notes are fixed: `L_1`, `L_n`
- each note from the output should belong to a chord `Ch`
- fixed number of occurences for motives (a motif is a sequence of intervals)
- `OM_1`, `OM_2` ... `OM_A` for motives `M_1`, `M_2` ... `M_A`

As mentioned in [M2], the second constraint: the variable for the i-th note `L_i` to belong to a chord `Ch` is analogous to stating that `L_i` should belong to a fixed set `S(Ch)`, where `S(Ch)` are all the notes in chord `Ch` - `L_i ∈ S(Ch)`.

In order to determine the set of notes for a chord, we can simply take a look at how chords are built. Most fundamental chords are built on the 1st, 3rd and 5th notes (starting from a root note). For instance, the **C major chord** (**C**), will contain the notes: `C, E & G`. To determine whether the chord is minor or major, we look at the interval between the 1st note and the 3rd note (see Table 2). If it is a minor third, than the chord is minor, otherwise it's a major third interval and the chord is major. In the case of C major, we have a distance of 2 tones between C and E, so the chord containing C, E and G is the C major chord (see [M9] for more details). To get the **C minor chord** (**Cm**), we have to flat out the 3rd note one semitone (b flat), resulting in `C, Eb & G`. The distance between C and Eb is 1 tone and a half. We can also add the 7th note (from C), 9th and so on, in order to get more complex and colorful chords (like the ones which can be heard in jazz genres).

Going further into analyzing this musical constraint satisfaction setup (now looking at the third constraint), the motives (also referred to as gestures in [M2]), are simply interval patterns, so if I were to successively play C, E and G, I would get 2 intervals: C-E a major third (2) and E-G a minor third (1.5). At this point, 2 ways to model this problem arise:

- generate a sequence of intervals: `2, 1.5` and then constrain the resulting notes to be in a set
- generate a sequence of notes from the chord set: `E, G` and then constrain the resulting intervals

**TODO 3: Since the first model is the preferred choice in these studies, let us further formalize it:**

**TODO 4: intervals as relative to previous note or to the root note**

### 4.3 Fabien Levy: Chord Progressions with Common Notes

Let `Ch_1, Ch_2, ..., Ch_n` be a chord progression represented by n ordered variables. The variables are from a fixed domain and they are denoted by strings (eg. `Am, C, Em7, Asus2, GMaj7`). Each chord is associated a subset of notes from the set of all notes.

Let `S_all = {A, A#, B, C, ..., G, G#}` be the set of all notes. Then `S(Ch_i) ⊆ S_all` for any `Ch_i`. The set of common notes between 2 successive chords `Ch_i, Ch_i+1` is denoted by `SC(Ch_i, Ch_i+1) = S(Ch_i) ∩ S(Ch_i+1)`. We can then have constraints on the exact number of common notes or in a range:

- `card (SC(Ch_i, Ch_i+1)) = A`, for all `Ch_i`, `i < n`
- `min_A ≤ card (SC(Ch_i, Ch_i+1)) ≤ max_A`, for all `Ch_i`, `i < n`

**Note 3**: The domain of the chords needs to be pre-defined and one can vary the domain such that the chords are in the family of a given scale or not (eg. major, natural minor, harmonic minor, melodic minor, major pentatonic, minor pentatonic, etc).

**Note 4**: A preliminary implementation of this idea is available in *chords.cpp*.

### 4.4 Georges Bloch: Minimizing Estrada Distance between 2 Successive Chords

### 4.5 Travelling Salesman Problem on Chords

This problem refers to sorting a sequence of chords such that the sum of common notes between successive chords is maximized. If we view the given chords as nodes in a graph and draw edges with weights equal to the number of common notes, then this is analogous to the traveling salesman problem.

### 4.6 Harmony and Melody of a Rock Song as a Search Problem

If we take a look at more modern music, such as pop / rock songs for instance, we can notice that they still retain most of the structure of classical music. Generally there would be 2-3 themes: verse, refrain, bridge, solo. Then the song would go along playing a succession of verses and refrains, possibly with some small variations (exploring the theme), followed by a bridge, solo and then the ending. Separately from this structure, each theme would consist of a succession of chords, onto which a melody is played.

For instance, *"Let it be"* by Beatles has:

**Table 3. Sample Chord progression in a song**

|Theme|Progression|
|:----:|:----------:|
|Part A | `C-G-Am-F` |
|Part B | `Am-G-F-C` |
|Part C (after every A & B) | `C-G-F-CDmC` |

The chords make the harmony for the melody and within each chord there is only a limited number of notes which fit. Because *"Let it be"* is written in the C major key, we can create any melody using the notes from the C major scale, the A minor scale (the C major relative) & their pentatonic versions, and it will sound well across the whole song. There are quite a few general rules to relate scales to chords progressions and by adhering to them one can obtain decent solos / melodic improvisations on top of the existing harmony.

Take the chord progression in Table 3, we can determine that it is in the C major key because:

- it starts on C major
- it contains only chords in the C major scale (either looking at their root notes or the entire chords)
- F# would not belong to C major scale (only `C D E F G A B`)
- Gm would not belong to C major chords family (only `C Dm Em F G Am Bmb5`) - can check why in [M9]

[Songs in Key](https://www.songkeyfinder.com/learn/songs-in-key)

[Let it Be C Major](https://www.pianote.com/blog/how-to-play-let-it-be-piano/)

In order to model this kind of musical structures using CSP, we would need to have a set of variables for the chords progression (harmony) and a set of variables for the melody. Then the search problem would consist of finding the right scales within the chosen chords progression. The scales then determine the domain for the melody variables. On top of this, one can then add all kinds of rules to either avoid too much repetition in the melody or to use some recurring themes.

## 5. Conclusions

**MEGA TODO**

Constraints identified:

- DIFFERENT NOTES, DIFFERENT INTERVALS
- NOTES (STEPS) IN A SCALE
- INTERVALS IN A THEME


- CHORDS IN A SCALE FAMILY
- RELATIVE SCALES
- NUMBER OF COMMON NOTES BETWEEN 2 SUCCESSIVE CHORDS

I think solving harmony and melody problems by using search techniques would have more value (/ would be more practical) than trying to compose music automatically based on training data, at least from a musical perspective. One reason for this is that music should be a creative endeavour, rather than some kind of imitation based on a large collection of training data. On the other hand, there seems to be a lot of potential to apply CSP and search techniques to solve certain musical fitting problems. However, this is quite challenging because it would require a very extensive understanding of music theory and the process of musical composition.

![Dali's Swallowtail](https://raw.githubusercontent.com/perticascatalin/open_nenos/master/DPML/imgs/swallow_tail.jpg)

The Swallow Tail, Salvador Dali's last painting, based on mathematical catastrophy theory, includes cello f-holes.

### References

- [M0] How Music Works (Melody, Rhythm, Harmony, Bass), documentary, Howard Goodall, 2006
- [M1] Gelisp: A Library to Represent Musical CSPs and Search Strategies, M. Toro et al., 2015, *ArXiv: Artificial Intelligence*
- [M2] Musical Constraint Satisfaction Problems Solved with Adaptive Search, C. Truchet & P. Codognet, 2004, *Soft Computing, Springer Verlag*
- [M3] Goedel, Escher, Bach: An Eternal Golden Braid, Douglas Hofstadter, 1979, *Basic Books*
- [M4] Introducere in Studiul Chitarei Electrice, Andrei Rosulescu, 2008
- [M5] Generating Polyphonic Music using Tied Parallel Networks, Daniel D. Johnson, 2017, *International Conference on Evolutionary and Biologically Inspired Music, Sound, Art and Design*
- [M6] Generating Sequences with Recurrent Neural Networks, Alex Graves, 2014, *ArXiv: Neural and Evolutionary Computing*
- [M7] A First Look at Music Composition using LSTM Recurrent Neural Networks, Douglas Eck & Juergen Schmidthueber, 2002, *Technical Report IDSIA*
- [M8] Twelve-tone Technique, [Wikipedia](https://en.wikipedia.org/wiki/Twelve-tone_technique)
- [M9] Major Scale Study, myself, 2020