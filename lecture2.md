% NTU lectures (2)
% Matthew Faytak<br/>University at Buffalo
% <img src="./assets/media/UB_Stacked_Small.png" width="200"> <img src="./assets/media/ntu-logo.png" width="200"><br/><img src="./assets/media/qr1.png" width="170">

# Overview

Last time, we discussed **feature selection**

This time, we will discuss **feature extraction**

* Especially using dimensionality reduction
* Approach sometimes called "feature engineering"


## Feature extraction

Creation of a *new feature* from combination or rescaling/reweighting of other features

Reduces the number of features required to describe a data set



## Outlook

Different motivations sometimes underpin feature extraction, as the name might imply

A closely related concept is "feature engineering"

* Concerned with *performance* of feature as an input to some task
* Especially frequent in **machine learning** and "artificial intelligence" applications


# Dimensionality reduction

## dimensionality reduction

Converts a high dimensional space consisting of numerous features into a lower dimensional space consisting of many fewer features

## example

a simple metaphor/image: ball on spring from Shlens?

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

Shlens

Styler
