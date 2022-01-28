% NTU lectures (2)
% Matthew Faytak<br/>University at Buffalo
% <img src="./assets/media/UB_Stacked_Small.png" width="200"> <img src="./assets/media/ntu-logo.png" width="200"><br/><img src="./assets/media/qr1.png" width="170">

## Overview

In the previous lecture, we discussed **feature selection**

* Manually *selecting* a subset of features <span class="cite">see Liu (2011)</span>

Here, we will discuss **feature extraction** 

* Especially using dimensionality reduction <span class="cite">see Vlachos (2011)</span>
* Taking a large number of features and using them to generate a smaller number of features
* Reduces the number of features required to describe a data set


## Outlook

Some different motivations underpin feature extraction: **data-driven** rather than theory-driven

* Allows new features well-suited to task to emerge from data
* Mainly concerned with *performance* of feature as an input to some task
* Especially frequent in **machine learning** and "artificial intelligence" applications


# Dimensionality reduction


## Features as dimensions

Features (observable attributes) define **dimensions** in a data set

* i.e. lower formants define a 3D space (F1 dimension, F2 dimension, F3 dimension)
* 

[3D vowel space plot]


## Curse of dimensionality 

If we have 1,000 features (dimensions) per observation, why not just use all of them? The **curse of dimensionality** 😈 

Adding *many* dimensions exponentially increases the amount of space that needs to be covered, with numerous undesirable side effects <span class="cite">Bellman (1957); Keough & Mueen (2011)</span>

* Computation becomes exponentially more difficult
* Exponentially more samples needed to evenly cover the space and maintain good performance

Distance in very high-dimensional spaces becomes nonsensical <span class="cite">Aggarwal et al (2001)</span>

* Objects become more or less equidistant from one another



## Dimensionality reduction

Converts a high dimensional space consisting of numerous features into a lower dimensional space consisting of fewer features

* Technically, feature selection is also a way of reducing dimensionality <span class="cite">Liu (2011)</span>
* We are mainly discussing *data-driven* approaches here
* Feature selection is *theory-driven*, usually


Left off reading this:

https://books.google.com/books?hl=en&lr=&id=i8hQhp1a62UC&oi=fnd&pg=PT29&dq=feature+extraction+encyclopedia+of+machine+learning&ots=91mazyjCcQ&sig=JVvFpdWbwrFQnAf737nzjkuCJjI#v=onepage&q&f=false

## ...

Solves the curse 😈 , but also presents a workaround to feature selection

* ...


## Example

A simple metaphor/image: ball on spring from Shlens?

[ball on spring]

## Example

Observation of this phenomenon: we don't know the underlying system

[picture of ball on spring w/cameras]


## Principal component analysis

A basic primer on how **PCA** 🤖 works

* Eigenvectors: the latent dimensions discovered by PCA, which form a better basis for describing the data
* Eigenvalues: the amount of variance in data set explained by each eigenvector
* Projections ("scores"): transform of data into this new space, in terms of eigenvectors


## Eigendecomposition

A complicated term for **rotating** high-dimensional data to find a new **basis** for describing the data

🤖


## Projection

The data can then be **projected** from its "naive" basis (the features originally measured) into a new basis

[figure or figures here]


## Basic example 

A basic example in NB 👩‍💻🧑🏾‍💻👩🏻‍💻

* Opening a sample data set 
* Eigendecomposition
* Projection into new basis
* Basic data viz

...


# Wrapping up

## Feature extraction: advantages

Speed, consistency/replicability, holistic description

Dimred can speed along discovery of new features to select

## Dimensionality reduction: advantages

More specifically:

* Aids data visualization, even occasionally rendering it in intuitive terms



## Feature extraction: disadvantages

New n-dimensional space may not be *interpretable*: what does a dimension "mean"?

* Dimensions may not correspond to anything linguistically relevant


## Next time

## References {.bib}

Aggarwal, C., Hinneburg, A. & Keim, D. (2001). On the surprising behavior of distance metrics in high dimensional space. In <i>International Conference on Database Theory</i>, 420-434. Springer.

Bellman, R. (1957). <i>Dynamic Programming</i>. Princeton University Press.

Keogh, E. & Mueen, A. (2011). Curse of dimensionality. In Sammut, C. & Webb, G. (eds.), <i>Encyclopedia of Machine Learning</i>, 257-258. Springer.

Liu, H. (2011). Feature selection. In Sammut, C. & Webb, G. (eds.), <i>Encyclopedia of Machine Learning</i>, 402-406. Springer.

Shlens, Y. (200x).

Styler, W. (2015). On the Acoustical and Perceptual Features of Vowel Nasality. PhD thesis. University of Colorado, Boulder. <a href="https://wstyler.ucsd.edu/files/styler_dissertation_final.pdf">PDF</a>

Vlachos, M. (2011). Dimensionality reduction. In Sammut, C. & Webb, G. (eds.), <i>Encyclopedia of Machine Learning</i>, 402-406. Springer.
