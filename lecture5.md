% NTU lectures (5)
% Matthew Faytak<br/>University at Buffalo
% <img src="./assets/media/UB_Stacked_Small.png" width="200"> <img src="./assets/media/ntu-logo.png" width="200"><br/><img src="./assets/media/qr1.png" width="170">

## Overview

Practical how-to: image dimensionality reduction on an ultrasound data set

* With follow-along iPython notebooks
* Assumes some basic familiarity with Python
* includes a general walk-through of the packages used

# The general approach

## Review: Eigenstuff

Decompose data sets consisting of many ultrasound images of the tongue

* into eigenvectors and eigenvalues
* convert to "eigentongues"

Same type of data as:

* Face recognition (Eigen faces)
* handwriting recognition


## Cleaning data

Before dimensionality reduction, data generally need to be centered, scaled, and normalized

Ultrasound data usually does not require this because:

* all data is already scaled on same 0-255 range for pixel values
* 


## Filtering

Ultrasound data is notably noisy; many approaches exist for filtering the specific noise type (speckle)

ex. of noise

But we also need to preserve edge information


## Filtering

Specific approach taken here: spackle reducing anisotropic diffusion filter

* preserves edges while removing most speckle
* crucial for ultrasound data and very well suited to it, since edges provide us with the location of reflections

Pre-processing for SRAD:

* median filter
* Laplacian of Gaussian added to image to sharpen edges


## why filter?

Technically, this is optional, but it improves performance of dimensionality reduction

By removing a lot of noise that we know is uninformative, we allow dimensionality reduction to focus specifically on the details in the image that we know to be informative


## rearranging data

All images should contain the same number of pixels and the same height and width (expected given how an ultrasound imaging system works)

Once filtered, the data needs to be converted from two dimensions to one

* from a two dimensional matrix of size w x h to a much longer one dimensional matrix of length wh


## running PCA

Instantiate the type of model we would like to run

Run on data


## fitting data

...


# Exploring eigentongues


## eigenvectors

...


## eigenvalues


## converting… to eigentongues


## converting… to PC scores

Loadings

...

## informativity and rank order

PCs are rank ordered in order of their informativity

* due to way they are learned from the data
* PC1 is extracted first, is most informative
* PC2 is second most informative which is orthogonal to PC1
* repeat down to PCn-1, where n is the number of observations in the data set
	* maximum number of PCs possible is n-1


## visualizing PC scores

PC scores are simple numerical values, which can be plotted against each other to reveal structure in the data

Conventional to use highest rank order PCs

show ex


## interpreting PCs using eigentongues

Each PC used to visualize the data can be understood by the patterns of covariation shown among pixels in its eigentongue

show example


## further analysis of PC scores

PC scores can be used directly as low dimensional representations of variation in the data set, and can be treated like any other numerical variable

* regression analysis
* correlation analysis

Pouplier & ??? As an example of direct analysis of PC1


## Time series of PC scores

If the data include all frames in a target interval, then the PCs can be used to track dynamical changes across the duration of the target interval

* Mielke & Carignan
* Kochetov, Faytak, Nara


# extending to new data

## training and testing

New data (which was not included in the PCA) can also be projected into the low dimensionality space

Lingvan paper should be brought in here


# By-products: LDA

## linear discriminant analysis (LDA)

Another dimensionality reduction technique, with different goals than PCA

* Data needs to be labeled
* LDA further reduces dimensionality to maximize discriminability of the labeled categories
* the learned dimensionality is the one which maximizes discriminability (no similar goal for PCA)


## how to LDA

Also very easily implemented using scikit-learn

* instantiate LDA model of choice
* use that object to fit Data
* fitted scores result


## interpretation of LDA

The resulting linear discriminant(s) are essentially a measure of how similar to the canonical member of the labeled category some new data is

* can be used as a "detector" of a segment or segment type if conditions are met


## segment detector

Example of American English /r/ from Mielke et al. 2016


## segment class detector

Example?


## case study

Your labphon paper


# By-products: reconstruction

## Reconstruction using eigentongues

Reconstruction of basis data from linear combination and weighting of eigentongues is easily achieved

The one figure goes here


## case study

Reconstruction in Faytak et al. 2020

* velar nasal versus alveolar nasal
* most reconstruct categorically as alveolar or velar
* a proportion of data doesn't reconstruct like either


