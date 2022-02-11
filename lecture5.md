% NTU lectures (5)
% Matthew Faytak<br/>University at Buffalo
% <img src="./assets/media/UB_Stacked_Small.png" width="200"> <img src="./assets/media/ntu-logo.png" width="200"><br/><img src="./assets/media/qr1.png" width="170">




## Overview



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


## training and testing

New data (which was not included in the PCA) can also be projected into the low dimensionality space

Lingvan paper should be brought in here


## segment detector

As an extension of this, LDA can characterize held-out data in terms of the data it has seen

Example of American English /r/ "detector" from Mielke et al. 2016


## segment class detector

Example?


## case study

Your labphon paper


