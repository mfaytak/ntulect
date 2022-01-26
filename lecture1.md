% NTU lectures (1)
% Matthew Faytak<br/>University at Buffalo
% <img src="./assets/media/UB_Stacked_Small.png" width="200"> <img src="./assets/media/ntu-logo.png" width="200"><br/><img src="./assets/media/qr1.png" width="170">


# About me

## About me

Matthew Faytak [ˈfeɪˌtæk], assistant professor in Linguistics at the University at Buffalo (State Univ. of New York) since mid-2021

*   PhD UC Berkeley 2018
*   Postdoc UCLA 2018-2021

Pronouns he/him/his, they/them/their (in the sense of 他)


## About me

My expertise is in articulatory phonetics

*   Specialization in ultrasound tongue imaging
*   I have worked on languages of China and Cameroon, plus English and French
*   I can use French and Standard Chinese
	* ... just not well enough to give this lecture in

Additional interests in phonetic typology, sound change, and phonological structure


# The format of these lectures

## Slidy slides

These lecture slides are hosted in **Slidy** HTML format on my personal site

* Displays slide by slide by default; use arrow keys or click to navigate
* "C" key displays table of contents
* "A" key shows all slides in order
* "P" key prints slides

Each linked by a QR code (see title slide)


# About this course

## About this course

Two main areas: 

* Ultrasound as a *tool* for phonetics and speech science 
* **Dimensionality reduction** as one of several ways of handling ultrasound data

Helps to solve a conundrum:

* Ultrasound is non-invasive, well-suited to field situations, relatively inexpensive and speaker-friendly
* ... but creates very complex, noisy data, which normally requires labor-intensity post-processing


## About this course

Specific topics covered will include:

* **Features**, **feature selection** and **feature extraction** in phonetics
* Dimensionality reduction as a type of feature extraction
* Ultrasound data and typical processing
* Case studies (Shanghai Mandarin; Suzhou Wu)
	* with follow-along Python notebooks


## The rest of *this* lecture

**Feature selection** in phonetics

* Major way we arrive at predictive features for research purposes


* differences in research philosophy
* practical differences
* limits and advantages of each approach

# Feature selection

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

* Coined very early <span class="cite">Lisker & Abramson (1964)</span> 
* After extensive research into parameters of linguistic plosive "voicing" contrasts <span class="cite">Stetson (1951); Liberman, Delattre & Cooper (1952)</span>
* Building on knowledge of first principles (knowing how plosives are generally produced)

Extremely general usefulness <span class="cite">Cho & Ladefoged (1999)</span>


## formants

Another classic, this time relating to the perceptually important acoustic properties of vowel and sonorant production

Some `code text` mixed into regular text


## Single features as less than optimal

Even in these two well-established cases of successful feature selection, the features which have been selected do not necessarily extend well to all related speech phenomena and cannot capture all phonological contrasts

In particular due to language to language variation, or even differences in how a contrastive property is coproduced on various segment types


## Voice onset time?

Certain dimensions of contrast are not captured using voice onset time alone <span class="cite">see Abramson & Whalen (2017)</span>

* Preaspirated, voiced aspirated or breathy plosives <span class="cite">Löfqvist & Yoshida (1981); CITE</span>
* tense-lax contrasts (Korean, Otomanguean)


## Formants?

Not all vowel contrasts can be captured using formant measurements alone, particularly static formant measurements


## Nasality

Measuring the degree of nasality in a vowel or sonorant has long been a problem for phoneticians, since nasality is signaled by a huge number of acoustic cues working in concert


## Voice quality

Recent work: voice quality is clearly multi dimensional <span class="cite">Keating et al (n.d.)</span>

Particularly in langs. with many phonation types, i.e. !Xóõ <span class="cite">Garellek (2019)</span>


## Advanced tongue root

Perhaps one of the most difficult contrasts to capture acoustically

* Underlying cavity shape difference not only varies from language to language
* Languages may also recruit voice quality differences to support


# wrap up

## feature selection: advantages

**Ease**: easy to work with, which non-trivially makes replication easier

**Interpretability**: because feature is selected based on first principles, we know how to interpret variation in that feature

## feature selection: disadvantages

Ease and being well-established can create a "false sense of security": property measured in one study might not be suitable for further exploration of related sounds

* Hand-picking and testing of a large set of features often needed at this stage (it took years to develop VOT, for example)


## References {.bib}

Abramson, A., & Whalen, D. (2017). Voice Onset Time (VOT) at 50: Theoretical and practical issues in measuring voicing distinctions. <i>Journal of Phonetics</i> 63, 75-86.

Cho, T. & Ladefoged, P. (1999). Variation and universals in VOT: evidence from 18 languages. <i>Journal of Phonetics</i> 27(2), 207-229.

Garellek, M. (2019). Acoustic discriminability of the complex phonation system in !Xóõ.
<i>Phonetica</i> 77(2), 1–30. <a href="https://doi.org/10.1159/000494301">DOI</a>

Keating, P., Kuang, J., Garellek, M., Esposito, C. & Khan, S. (n.d.) A cross-language acoustic space for phonation distinctions. Unpublished manuscript, UCLA. <a href="https://linguistics.ucla.edu/people/keating/Keating-etal_2019_ms.pdf">PDF</a>

Liberman, A., Delattre, P. & Cooper, F. (1952). The role of selected stimulus variables in the perception of the unvoiced stop consonants. <i>Amer J. Psychol.</i> 65, 497.

Lisker, L. & Abramson, A. (1964). A cross-language study of voicing in initial stops: acoustical measurements. <i>Word</i> 20, 384-422.

Löfqvist A. & Yoshida H. (1981). Laryngeal activity in Icelandic obstruent production. <i>Nordic J Linguistics</i> 4, 1–18. 

Stetson, R. H. (1951). <i>Motor phonetics.</i> Amsterdam: North-Holland Publishing Company.
