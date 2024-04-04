
# AGILe: Ancient Greek Inscriptions Lemmatizer
AGILe is a lemmatizer for Ancient Greek inscriptions developed at the University of Groningen. Details can be found in:

de Graaf, E., Stopponi, S., Bos, J., Peels-Matthey, S. & Nissim, M. (2022). AGILe: The First Lemmatizer for Ancient Greek Inscriptions. Proceedings of the 13th Conference on Language Resources and Evaluation (LREC 2022), Marseille, 20-25 June 2022. pp. 5334–5344. [http://www.lrec-conf.org/proceedings/lrec2022/pdf/2022.lrec-1.571.pdf](http://www.lrec-conf.org/proceedings/lrec2022/pdf/2022.lrec-1.571.pdf)

**This branch contains an experimental, new version of AGILe, trained on more data and with an augmented lexicon:** 
- the initial CGRN training data has been augmented with the new 25 inscriptions recently added to the corpus;
- all particles and articles have been lemmatized, partly automatically (the non-ambiguous word forms) partly manually (all remaining forms in CGRN 1-123 + 248 + 250);
- the lexicon has been augmented with the lemmatized particles and lemmas from the new 25 CGRN inscriptions.

## Installation
### 1. Clone this branch of the repository in a dedicated folder
```
mkdir agile-particles
cd agile-particles
git clone -b particles --single-branch https://github.com/agile-gronlp/agile
```

### 2. Install dependencies
AGILe works with **version 1.0.21 of the CLTK**. If you are using a more recent version of the CLTK, please install the required packages in a virtual environment.

AGILe supports Python 3.7 or later on POSIX–compliant operating systems. To install all required dependencies, simply run:

```
cd agile
pip install -r requirements.txt
```

### 3. Download Stanza models
To download the Ancient Greek models from Stanza, follow these steps in your Python interactive interpreter:

```
>>> import stanza
>>> stanza.download('grc')
```

## Running AGILe
Below is an example of performing lemmatization on a short inscription:

```
>>> from agile import lemmatize

>>> doc = lemmatize("αἲξ θύεται τάδε μὴ ἐσφέρεν ἐς τὸ τέμενος τοῦ Ἀπόλλωνος τοῦ Οὐλίου εἱμάτιον")
>>> for sent in doc.sentences:
...    for word in sent.words:
...        print(f'word: {word.text + " ":15}lemma: {word.lemma}')
```

This demo gives the following output:
```
word: αἲξ            lemma: αἴξ
word: θύεται         lemma: μετά
word: τάδε           lemma: ὅδε
word: μὴ             lemma: μή
word: ἐσφέρεν        lemma: εἰσφέρω
word: ἐς             lemma: εἰς
word: τὸ             lemma: ὁ
word: τέμενος        lemma: τέμενος
word: τοῦ            lemma: ποῦ
word: Ἀπόλλωνος      lemma: Ἀπολλωνία
word: τοῦ            lemma: ποῦ
word: Οὐλίου         lemma: ξύλον
word: εἱμάτιον       lemma: ἱμάτιον
```
N.B. Adding particles and articles to the training data improved the lemmatization of such items, but also brought new errors.

The lexicon lookup can be disabled by setting the `use_lexicon` parameter of the `lemmatize` function to `False`.

## Interactive Notebook on Google Colab
If you want to try AGILe without downloading it: https://colab.research.google.com/drive/1YZMGxF8ORCrk_tyD1muHkgVsMXxeWHJJ?usp=drive_link

## Acknowledgements
The `lexicon.p` used is extracted from a XML edition with composed Unicode of the LSJ, as transformed by [Giuseppe G. A. Celano](https://github.com/gcelano/LSJ_GreekUnicode). The original text [is] provided under a CC BY-SA license by Perseus Digital Library, http://www.perseus.tufts.edu, with funding from The National Endowment for the Humanities.
Data accessed from https://github.com/PerseusDL/lexica/.

## License
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

## BibTex
```
@InProceedings{degraaf-EtAl:2022:LREC,
  author    = {de Graaf, Evelien  and  Stopponi, Silvia  and  Bos, Jasper K.  and  Peels-Matthey, Saskia  and  Nissim, Malvina},
  title     = {AGILe: The First Lemmatizer for Ancient Greek Inscriptions},
  booktitle      = {Proceedings of the Language Resources and Evaluation Conference},
  month          = {June},
  year           = {2022},
  address        = {Marseille, France},
  publisher      = {European Language Resources Association},
  pages     = {5334--5344},
  url       = {https://aclanthology.org/2022.lrec-1.571}
}
```
