% NTU lectures (2)
% Matthew Faytak<br/>University at Buffalo
% <img src="./assets/media/UB_Stacked_Small.png" width="200"> <img src="./assets/media/ntu-logo.png" width="200"><br/><img src="./assets/media/qr1.png" width="170">

# Overview

Last time, we discussed **feature selection**

This time, we will discuss **feature extraction**

* Especially using dimensionality reduction
* Approach sometimes called "feature engineering"


## Feature extraction

Creation of *new features* from combination or rescaling/reweighting of other features

* As opposed to *selecting* a subset <span class="cite">Liu (2011)</span>
* Usually fewer in number than original features
* Reduces the number of features required to describe a data set


## Outlook

Different motivations sometimes underpin feature extraction

* Concerned with *performance* of feature as an input to some task
* Especially frequent in **machine learning** and "artificial intelligence" applications


# Dimensionality reduction

## Dimensionality reduction

Converts a high dimensional space consisting of numerous features into a lower dimensional space consisting of many fewer features

Technically, feature selection is also a way of reducing dimensionality
<span class="cite">Liu (2011)</span>, though not often used in that sense (we are mainly discussing algorithmic approaches here)

## example

a simple metaphor/image: ball on spring from Shlens?

## Curse of dimensionality 

Adding a lot of dimensions exponentially increases the amount of space that needs to be covered, with numerous undesirable side effects <span class="cite">Bellman (1957); Keough & Mueen (2011)</span>

* Computation becomes exponentially more difficult
* Exponentially more samples needed to evenly cover the space and maintain good performance

Distance in very high-dimensional spaces space becomes nonsensical <span class="cite">Aggarwal et al (2001)</span>

* Objects more or less all equidistant from one another


## principal component analysis

Eigenvectors: the latent dimensions discovered by PCA, which form a better basis for describing the data
Eigenvalues: the amount of variance in data set explained by each eigenvector
Projections ("scores"): transform of data into this new space, in terms of eigenvectors

## principal component analysis

A basic example in NB


# "Black box" methods

## Why this lecture doesn't cover neural nets

If we are theoretically motivated, we must be able to *understand* human behavioral reasons for a certain outcome

NNs make this quite hard because they merely *perform*


## Transparent dimensionality reduction

Styler paper notes


# Wrapping up

## Feature extraction: advantages

Speed, consistency/replicability, holistic description

Dimred can speed along discovery of new features to select


## Feature extraction: disadvantages

New n-dimensional space may not be *interpretable*: what does a dimension "mean"?

* Dimensions may not correspond to anything linguistically relevant


## Next time

## References {.bib}

Aggarwal, C., Hinneburg, A. & Keim, D. (2001). On the surprising behavior of distance metrics in high dimensional space. In <i>International Conference on Database Theory</i>, 420-434. Springer.

Bellman, R. (1957). <i>Dynamic Programming</i>. Princeton University Press.

Keogh, E. & Mueen, A. (2011). Curse of dimensionality. In Sammut, C. & Webb, G. (eds.), <i>Encyclopedia of Machine Learning</i>, 257-258. Springer.

Shlens

Styler
