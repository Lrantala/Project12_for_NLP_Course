from textblob import Word

def retrieve_synset_list_for_word(word, whole_synset=True, pos_tag=None):
    """Returns the synset list for a word. Possibility to return whole synsets or just names
    of synsets. Also possible to limit to specific POS tags"""
    blob_word = Word(word)

    if whole_synset:
        return blob_word.get_synsets(pos_tag)
    else:
        return [name.name() for name in blob_word.get_synsets(pos_tag)]


def retrieve_hyponym_or_hypernym_list_for_synset(synset, whole_synset=True, hypo_or_hyper=0):
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


def calculate_path_similarity_for_synset_lists(synset_list1, synset_list2):
    """Take two lists of synsets, calculate the path similarities between all permutations in them, and
    return the highest score as the similarity score."""

    # Set highest score to -1, which is given if there's no matches at all in path similarities
    highest_score = -1

    for synset1 in synset_list1:
        for synset2 in synset_list2:
            path_score = synset1.path_similarity(synset2)
            if path_score:
                if path_score > highest_score:
                    highest_score = path_score

    return highest_score

