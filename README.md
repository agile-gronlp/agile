
# AGILe: Ancient Greek Inscriptions Lemmatizer
AGILe is a lemmatizer for Ancient Greek inscriptions developed at the University of Groningen.

Details can be found in de Graaf, E., Stopponi, S., Bos, J., Peels-Matthey, S. & Nissim, M. (2022). AGILe: The First Lemmatizer for Ancient Greek Inscriptions. Proceedings of the 13th Language Resources and Evaluation Conference (LREC 2022), forthcoming.

## Installation
### 1. Clone this repository
```
git clone https://github.com/agile-gronlp/agile
```

### 2. Install dependencies
AGILe supports Python 3.7 or later. To install all required dependencies, simply run:

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

## Acknowledgements
The `lexicon.p` used is extracted from a XML edition with composed Unicode of the LSJ, as transformed by [Giuseppe G. A. Celano](https://github.com/gcelano/LSJ_GreekUnicode) under license CC BY-NC-SA 3.0. The original text [is] provided under a CC BY-SA license by Perseus Digital Library, http://www.perseus.tufts.edu, with funding from The National Endowment for the Humanities.
Data accessed from https://github.com/PerseusDL/lexica/.
