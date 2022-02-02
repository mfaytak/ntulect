% NTU lectures (3)
% Matthew Faytak<br/>University at Buffalo
% <img src="./assets/media/UB_Stacked_Small.png" width="200"> <img src="./assets/media/ntu-logo.png" width="200"><br/><img src="./assets/media/qr1.png" width="170">

## Overview

this lecture

# ultrasound basics

## the basic method

Low intensity and very high frequency sound is transmitted through soft tissue and reflects back when the density of the medium changes

picture illustrating uti - mannequin head

## reflection

The signal in ultrasound data is the extent to which the high frequency energy reflects back to the probe

Occurs when the medium changes in density

* tissue tissue boundaries
* tissue air boundaries

## shadows

Rather than reflecting back energy, bone absorbs energy and casts a "shadow" in the ultrasound image

* hyoid shadow
* mandible or chin shadow

The two shadows delimit the useful range of data received from reflection

* this means the tongue tip is usually not visible in ultrasound data


## Rigid landmarks

A couple of rigid landmarks are often collected prior to recording the motion of the tongue

* palate trace, by doing a *swallow task*
* swallow water and watch as tongue suctions to roof of mouth
* provides position of the hard palate, useful for gauging constriction degree
* occlusal plane or bite plane, by having the speaker bite down on a rigid plate and press the tongue into it
* provides common angle for representation of data from multiple speakers


## Stabilization

[picture of course]


## a single frame

The landmarks which we have discussed are visible in this sample frame captured in midsagittal section


## other imaging planes

While we won't discuss them here, it's good to know that ultrasound is not constrained to mid sagittal images

* coronal slice can be taken by rotating the probe under the chin 90°
* laryngeal ultrasound at an oblique angle is also possible


## uses of ultrasound

Generally used for imaging posture or shape of the tongue from root to blade, or its change over time

* *broad* place and tongue position distinctions
* complex tongue shapes (laterals, rhotics)
* rapid tongue body and blade movements (flaps, clicks)


## Usage in the field

A critical tool for imaging vocal tract configurations in the field, outside of the lab

Non-invasive, generally not intimidating, and by far the most portable vocal track imaging technology

* no wall outlet required, draws power from laptop
* relatively hands off, especially if stabilization headset is used


## drawbacks

Only images the tongue in real time, no simultaneous imaging of hard palate possible, no imaging of larynx or velum

Image can be noisy, and not every potential participant images well

* small, young people image the best
* beards can get in the way
* Probe can press on larynges, causing pain


## Data type

Perhaps the biggest drawback is the data itself: raw reflectivity; requires extensive post processing

**Feature extraction**: extracting contours that represent the reflection at the tongue surface, or extracting motion of that contour along registration lines

* complex image processing, often requires manual intervention

Next lecture: **feature projection** methods


# ultrasound feature extraction

## contour extraction

By far the most common means of feature extraction for ultrasound data

* first principle: we know that reflection represents the surface of the tongue, which tells us something about the vocal tract area function

Certainly not unreasonable


## a brief history

The need to accurately extract contours is a long-standing problem for both general diagnostic and biomedical science and speech science so far as it concerns ultrasound imaging of the tongue

...

## manual tracing

Most solid, but completely impractical

## semi automated tracing

Basically the mainstream

Still very time consuming, since extensive manual intervention is still required, especially if reflection signal is of less than ideal strength


## State of the art

Active snake models provide good performance and relatively easy computation

* examples, especially edge track


## purely automatic tracing

In recent years it has started to become possible to do completely automatic contour extraction

* SLURP
* get contours?

Per some recent work, these work surprisingly well, often as well as hand checked work


## registration lines

Lines drawn in a fan shaped grid out from probe origin

Example picture


## M- Mode ultrasound

Registration lines mimic so-called m-mode ultrasound, commonly used to track rhythmic motion in biomedical contexts (i.e. heart or blood vessel motion)

image to demonstrate


## registration line uses

These can be used to track entire contours where they intersect the lines, but more commonly are used to track tongue motion in a small region of interest

Very common in tongue root retraction studies, or blade raising studies


# wrapping up

## Ultrasound pros

Most portable, least expensive, least invasive, often most familiar to participants

For fieldwork, it is really the only option


## ultrasound cons

Messy, high dimensional data, which does not lend itself immediately to analysis

* feature extraction required, in the most typical approach, then those features are analyzed in place of the whole image
* often very time consuming and requires a small army of annotators who must all agree on how to segment an image


## next lecture: some solutions

Various ways around the feature extraction problem

Going in the direction of **feature engineering**

