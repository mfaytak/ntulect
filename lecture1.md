% NTU lectures (1)
% Matthew Faytak<br/>University at Buffalo
% <img src="./assets/media/UB_Stacked_Small.png" width="200"> <img src="./assets/media/ntu-logo.png" width="200"><br/><img src="./assets/media/qr1.png" width="170">


# About me

## About me

Matthew Faytak [ˈfeɪˌtæk], assistant professor in Linguistics at the University at Buffalo (State Univ. of New York) since mid-2021

*   PhD UC Berkeley 2018
*   Postdoc UCLA 2018-2021

Personal

*   Pronouns he/him/his, they, etc
*   blah


## About me

My expertise is in articulatory phonetics

*   Specialization in tongue ultrasound imaging
*   I have worked on a number of languages in China and Cameroon, plus English and French
*   I can speak French and Standard Chinese

I have additional interests in phonetic typology, sound change, and phonological structure


# The format of these lectures

## Slidy slides

These lecture slides are permanently hosted in **Slidy** HTML format on my personal site

* Displays slide by slide by default; use arrow keys or click to navigate
* "C" key displays table of contents
* "A" key shows all slides in order
* "P" key prints slides

Each linked by a QR code, as we've already discussed

* See the title slide


# About the course

## About the course

This lecture series concerns two topics: ultrasound as a tool for phonetics and speech science, and dimensionality reduction as a way of simplifying the processing of ultrasound data

* ultrasound is well-suited to a variety of data collection situations, non-invasive, relatively inexpensive
* but it creates very high dimensional data, which requires researchers to get creative in processing it

## About this course

Topics covered will include:

* Feature selection and feature engineering in phonetics
* Dimensionality reduction as a type of feature engineering
* Ultrasound methods and basic data types; more typical processing routines
* Dimensionality reduction and ultrasound
* Case study (Taiwanese Mandarin)

## The rest of this lecture

Feature selection in phonetics

Basically, the major way we arrive at **predictive features** for research purposes

* differences in research philosophy
* practical differences
* limits and advantages of each approach

# feature selection

## characters and features

## predictive power

## ease of use

Of course, ease-of-use also factors in to whether a feature is frequently used in phonetics as a metric

This might have undesirable effects on some occasions

* feature is easy and compares well to other studies, but does not actually measure the relevant speech phenomenon
* sometimes a speech phenomenon does not have clear, easily extracted features in the acoustic signal

## theoretical motivations

I am not sure what the slide means, but it should probably be replaced with two slides discussing examples of the bullet points in the previous slide

# a review of feature selection in phonetics

## feature selection in phonetics

Because the acoustic signal resulting from speech is highly complex and time varying along very short temporal scales, selecting a single relevant feature or small bundle of features has a long history in phonetics

## Voice onset time

Perhaps the single most substantial example of a hand-picked feature

Lisker & Abramson (1964)

Selected after an exhaustive overview of the data and knowledge of first principles, i.e. plosive production


## formants

Another classic, this time relating to the perceptually important acoustic properties of vowel and sonorant production



## Single features as less than optimal

Even in these two well-established cases of successful feature selection, the features which have been selected do not necessarily extend well to all related speech phenomena and cannot capture all phonological contrasts

In particular due to language to language variation, or even differences in how a contrastive property is coproduced on various segment types


## Voice onset time?

Certain dimensions of contrast are not captured using voice onset time alone

* Preaspirated, voiced aspirated or breathy plosives
* tense-lax contrasts (Korean, Otomanguean)


## Formants?

Not all vowel contrasts can be captured using formant measurements alone, particularly static formant measurements


## Nasality

Measuring the degree of nasality in a vowel or sonorant has long been a problem for phoneticians, since nasality is signaled by a huge number of acoustic cues working in concert


## Voice quality

Recent Garellek & Keating work: voice quality is clearly multi dimensional


## Advanced tongue root

Advanced town Road is perhaps one of the most difficult contrasts to capture acoustically, since the underlying cavity shape difference not only varies from language to language, but languages may also recruit voice quality differences to support


# wrap up

## feature selection: advantages

**Ease**: easy to work with, which non-trivially makes replication easier

**Interpretability**: because feature is selected based on first principles, we know how to interpret variation in that feature

## feature selection: disadvantages

Ease and being well-established can create a "false sense of security": property measured in one study might not be suitable for further exploration of related sounds

* Hand-picking and  of a large set of features often needed at this stage


## References {.bib}

Lisker, L. and Abramson, A. (1964). A cross-language study of voicing in initial stops: acoustical measurements. <i>Word</i> 20, 384-422.
