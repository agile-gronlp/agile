
# AGILe: Ancient Greek Inscriptions Lemmatizer
AGILe is a lemmatizer for Ancient Greek inscriptions developed at the University of Groningen. Details can be found in:

de Graaf, E., Stopponi, S., Bos, J., Peels-Matthey, S. & Nissim, M. (2022). AGILe: The First Lemmatizer for Ancient Greek Inscriptions. Proceedings of the 13th Conference on Language Resources and Evaluation (LREC 2022), Marseille, 20-25 June 2022. pp. 5334–5344. [http://www.lrec-conf.org/proceedings/lrec2022/pdf/2022.lrec-1.571.pdf](http://www.lrec-conf.org/proceedings/lrec2022/pdf/2022.lrec-1.571.pdf)

Peels-Matthey, S., de Graaf, E., Nissim, M., Bos, J. & Stopponi, S. (2024). Automatic lemmatization of ancient Greek inscriptions: A presentation of AGILe. "Journal of epigraphic studies". 7, 2024: 29-50. [https://pure.rug.nl/ws/portalfiles/portal/1054237044/Peels-Matthey_et_al_2024_Automatic_lemmatization_of_Ancient_Greek_inscriptions_-_A_presentationof_AGILe.pdf](https://pure.rug.nl/ws/portalfiles/portal/1054237044/Peels-Matthey_et_al_2024_Automatic_lemmatization_of_Ancient_Greek_inscriptions_-_A_presentationof_AGILe.pdf)


## Installation
### 1. Clone this repository
```
git clone https://github.com/agile-gronlp/agile
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
word: θύεται         lemma: θύω
word: τάδε           lemma: ὅδε
word: μὴ             lemma: μή
word: ἐσφέρεν        lemma: εἰσφέρω
word: ἐς             lemma: εἰς
word: τὸ             lemma: τε
word: τέμενος        lemma: τέμενος
word: τοῦ            lemma: ποῦ
word: Ἀπόλλωνος      lemma: Ἀπόλλων
word: τοῦ            lemma: ποῦ
word: Οὐλίου         lemma: οὔλιος
word: εἱμάτιον       lemma: ἱμάτιον
```
The lexicon lookup can be disabled by setting the `use_lexicon` parameter of the `lemmatize` function to `False`.

## Interactive Notebook on Google Colab
If you want to try AGILe without downloading it: https://colab.research.google.com/drive/1YZMGxF8ORCrk_tyD1muHkgVsMXxeWHJJ?usp=drive_link

## Acknowledgements
The `lexicon.p` used is extracted from a XML edition with composed Unicode of the LSJ, as transformed by [Giuseppe G. A. Celano](https://github.com/gcelano/LSJ_GreekUnicode). The original text [is] provided under a CC BY-SA license by Perseus Digital Library, http://www.perseus.tufts.edu, with funding from The National Endowment for the Humanities.
Data accessed from https://github.com/PerseusDL/lexica/.

## License
[![Creative Commons License](https://licensebuttons.net/l/by-sa/4.0/88x31.png)](https://creativecommons.org/licenses/by-sa/4.0/)<br />
This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

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

```
@article{peels2024automatic,
  title={Automatic lemmatization of ancient Greek inscriptions: A presentation of AGILe},
  author={Peels-Matthey, Saskia and de Graaf, Evelien and Nissim, Malvina and Bos, Jasper and Stopponi, Silvia},
  journal={Journal of epigraphic studies: 7, 2024},
  pages={29--50},
  year={2024},
  publisher={Fabrizio Serra}
}
```
