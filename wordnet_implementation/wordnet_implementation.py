from nltk.corpus import wordnet as wn


def return_synset_list_for_word(word, whole_synset=True):
    """Returns the synset list for a word. Possibility to return whole synsets or just names
    of synsets."""
    if whole_synset:
        return wn.synsets(word)
    else:
        return [name.name() for name in wn.synsets(word)]


def return_hyponym_or_hypernym_list_for_synset(synset, whole_synset=True, hypo_or_hyper=0):
    """Returns the hyponym synset list for a synset. Possibility to return whole synsets or just names
    of synsets. Parameter hypo_or_hyper takes either 0 for hyponyms, or 1 for hypernyms. Default: 0"""
    if hypo_or_hyper == 1:
        synset_list = synset.hypernyms()
    elif hypo_or_hyper == 0:
        synset_list = synset.hyponyms()
    else:
        synset_list = []

    if whole_synset:
        return synset_list
    else:
        return [name.name() for name in synset_list]


