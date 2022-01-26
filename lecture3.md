% NTU lectures (4)
% Matthew Faytak<br/>University at Buffalo
% <img src="./assets/media/UB_Stacked_Small.png" width="200"> <img src="./assets/media/ntu-logo.png" width="200"><br/><img src="./assets/media/qr1.png" width="170">

## overview

Previous lecture: feature selection on ultrasound data

This lecture: various types of feature engineering

* dimensionality reduction on ultrasound contours
* pixel different methods
* dimensionality reduction on ultrasound frames
	* our focus


# dimensionality reduction on ultrasound contours

## refresher: contour extraction

Contours can be segmented from the ultrasound image using a combination of human and automatic processing

Increasingly, just automatic


## Analysis of contours

Usually done with an additive model which can handle non-linear relationships

* SSANOVA (smoothing spline ANOVA)
* GAMMs, which are really a specific sort of SSANOVA (check this)
	* very computationally intensive


## dimensionality reduction on contours 

Another method occasionally used: PCA of contour position

* XY positions are the input data
* PC scores show informative variation in tongue position in XY space


## Caveats

Hard to use this method without first normalizing data for inter-speaker differences

* PCA doesn't separate out linguistic differences and differences in speaker morphology
* can easily be conflated


# pixel difference methods

## pixel difference

Each ultrasound image is composed of tens of thousands of pixels, each of which has a numerical value indicating brightness

* directly relates to position of tongue because brightness means reflectivity
* tongue position change means changing brightness


## metric of pixel difference

Pixel by pixel change in brightness can be used as a measure of tongue movement over time

image


## Applications of pixel difference method

Detection of motion includes intrinsic tongue muscles, unlike other measures discussed so far; useful for detection of pre-speech articulation

* various psycholinguistic applications (refinement of production based reaction time)


## related methods

Related to pixel difference, but more computationally complex, is optical flow

* detects apparent motion evidenced by two images
* like basic pixel difference, returns the magnitude of the motion
* unlike pixel difference, yields direction of motion in addition to magnitude
* actual physical movement of rigid bodies can be calculated through further feature engineering

images (2x slides?)


# dimensionality reduction on ultrasound frames

## our focus today

Dimensionality reduction carried out not on ultrasound contours, but on ultrasound frames


## pixel structure

Recall that ultrasound frames are made up of tens of thousands of individual pixels

* each with their own value from 0 to 255, indicating brightness (black to white)


## Scan lines

Going into more detail, each ultrasound image can be thought of as a matrix of width w by height h

* w, h values must be fixed throughout data collection (images don't change in size)
* each column of pixels of size (1,h) represents a single scan line from the probe
* reflectivity data as sent out and received by a single element in the probe head


## High dimensionality

Keep in mind: each pixel across data sets with the same frame size w,h can be thought of as a separate feature

* tens of thousands of features


## feature selection problems

Clear at this point: this is a challenge for feature selection

* how to pick a small number of pixels which are highly informative for the analysis you would like to do?


## feature engineering solution

In this particular context, working directly from frames, the best solution is to engineer new features which capture interesting variation


# Enter: dimensionality reduction

## recap: products of dimensionality reduction

Eigenvectors: the latent dimensions discovered by PCA, which form a better basis for describing the data

Eigenvalues: the amount of variance in data set explained by each eigenvector

Projections ("scores"): transform of data into this new space, in terms of eigenvectors


## eigenimages

This method is very commonly extended to whole-image data in which the subject matter is controlled

Eigenvectors *directly represent* dimensions of spatial covariation in pixel intensities

* faces (eigenfaces)
* lips (eigenlips)
* hand written letters and numbers


## eigentongues

Hueber et al (2007) coinage, from eigenfaces

* shows patterns of negative and positive covariation in pixel brightness across a data set
* eigenfaces: patterns correspond to facial features
* eigentongues: patterns correspond to positions of the visible tongue contour
	* as well as any other patterning in the image (hyoid shadow position, internal musculature of tongue, etc.)
	* captures more information than tongue contour position in this way


## eigentongues

Blue = positive covariation with PC score; red = negative covariation with PC score

* Higher PC1 score makes red pixels light up
* Lower PC1 score makes blue pixels light up

[image]


# Wrapping up

## Pros

Very efficient once the basics are mastered

* Speedy (big advantage over basic contour extraction)
* Very replicable

Potentially more informative in some respects than contours

* Especially for data where parts of tongue contour aren't visible


## Convergence with other methods

converging on common analysis across methods: pixel and pixel dimred methods easy to use on other data types

MRI - Oh & Lee, Lee
Face video - ??


## Cons

Best suited to analyses of relative similarity and difference of sounds 

* Somewhat limited
* Fairly different from some approaches to ("engineering-y")


## Next lecture

A practical how-to of UTI image PCA

* Sample data
* Notebooking
