from cltk.alphabet.grc import grc  # For normalizing texts
import re
import stanza
import pickle
from Levenshtein import distance
from stanza.models.common.doc import Document


def lemmatize(text, use_lexicon=True):
    """
    Lemmatizes (and tokenizes) Ancient Greek inscriptions given custom rules,
    a custom trained model in Stanza and a lexicon lookup.

    :param text: inscription text to be lemmatized
    :param use_lexicon: bool to enable or disable the correction by the lexicon lookup
    :return: Stanza Document containing id, text, lemma, start_char and end_char annotations
    """

    # Handle extra-alphabetical characters
    original_text = grc.normalize_grc(text)
    original_text = re.sub('[|∣·∙∶:,.⁝⋮⁞⁙“”]+', ' \g<0> ', original_text)  # Pre-tokenize
    original_text = re.sub(' +', ' ', original_text)
    original_text = re.sub('\n+', '\n', original_text)  # Sentence tokenization not supported

    # Add custom rules (chars have been normalized)
    processed_text = re.sub('(?<!\s)[Ϝϝh](?!\s)', '', original_text)  # [Ϝϝh] within token
    processed_text = re.sub('(?<=\s)[Ϝϝh](?!\s)(?=.)', '', processed_text)  # [Ϝϝh] begin of token
    processed_text = re.sub('(?<=.)(?<!\s)[Ϝϝh](?=\s)', '', processed_text)  # [Ϝϝh] end of token
    processed_text = re.sub('(κς)|(κσ)|(χς)|(χσ)', 'ξ', processed_text)
    processed_text = re.sub('(Κς)|(Κσ)|(Χσ)|(Χς)', 'Ξ', processed_text)
    processed_text = re.sub('(φς)|(φσ)', 'ψ', processed_text)
    processed_text = re.sub('(Φς)|(Φσ)', 'Ψ', processed_text)
    processed_text = re.sub(' [|∣·∙∶:,.⁝⋮⁞⁙“”]+', '', processed_text)

    lemma_nlp = stanza.Pipeline(lang='grc', processors='tokenize,lemma', tokenize_no_ssplit=True,
                                lemma_model_path='grc_agile_lemmatizer.pt', verbose=False)
    token_nlp = stanza.Pipeline(lang='grc', processors='tokenize', tokenize_no_ssplit=True, verbose=False)
    token_dict = token_nlp(original_text).to_dict()[0]  # Dict for all tokens (lemmas to be inserted)
    lemma_dict = lemma_nlp(processed_text).to_dict()[0]  # Dict for lemmas given by model
    lexicon = pickle.load(open("lexicon.p", "rb"))

    # Add lemmas to token dict
    lemma_i = 0
    for token_i, token in enumerate(token_dict):
        if re.search('[|∣·∙∶:,.⁝⋮⁞⁙“”]+', token['text']):  # Custom lemmatization
            token_dict[token_i]['lemma'] = token['text']
        else:
            try:
                predicted = lemma_dict[lemma_i]['lemma']  # Lemmatization by model
            except KeyError:  # No lemma
                predicted = ""
            # Handle lexicon correction
            if use_lexicon:
                if predicted != "" and predicted not in lexicon:
                    lowest = distance(lexicon[0], predicted)
                    closest = lexicon[0]
                    for entry in lexicon[1:]:
                        dist = distance(entry, predicted)
                        if dist == 1:  # Speed optimisation
                            closest = entry
                            break
                        elif dist < lowest:
                            lowest = dist
                            closest = entry
                    token_dict[token_i]['lemma'] = closest
                else:
                    token_dict[token_i]['lemma'] = predicted
            else:
                token_dict[token_i]['lemma'] = predicted
            lemma_i += 1

    return Document([token_dict])
