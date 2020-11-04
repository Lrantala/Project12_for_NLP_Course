import logging
import wordnet_implementation.wordnet_implementation as wni


def custom_similarity_measure(synset1, synset2):

    synset1_hyper, synset2_hyper =[], []
    synset1_hypo, synset2_hypo = [], []
    noun_hyper, verb_hypo = 0, 0

## Takes care of the hypernyms and hyponyms for the synsets of the sentence pairs
    for syns in synset1:
        if syns.pos()=='n':
            synset1_hyper.append(syns.hypernyms())
        elif syns.pos()=='v':
            synset1_hypo.append(syns.hyponyms())
        else:
            logging.info("Encountered a synset which is not a noun or verb")

    for syns in synset2:
        if syns.pos() == 'n':
            synset2_hyper.append(syns.hypernyms())
        elif syns.pos() == 'v':
            synset2_hypo.append(syns.hyponyms())
        else:
            logging.info("Encountered a synset which is not a noun or verb")

## Takes care of the equation that's inside the bracket, minus the 'max' part
    common_hyper = commonality(synset1_hyper, synset2_hyper)
    total_hyper = hyp_union(synset1_hyper + synset2_hyper)

    if total_hyper is not 0:
        noun_hyper = common_hyper/total_hyper

    common_hypo = commonality(synset1_hypo, synset2_hypo)
    total_hypo = hyp_union(synset1_hypo + synset2_hypo)
    if total_hypo is not 0:
        verb_hypo = common_hypo / total_hypo

    return noun_hyper, verb_hypo


def commonality(synset1, synset2):
    union_list = []
    for item1 in synset1:
        for item2 in synset2:
               if item1 == item2 and item1==item2 != []:
                   if item1 not in union_list:
                       union_list.append(item1)
    return len(union_list)


def hyp_union(hyp_list):
    union_list = []
    for item in hyp_list:
        if item not in union_list and item != []:
            union_list.append(item)
    return len(union_list)


def count_custom_similarity_measure(sentence1, sentence2, stemming, lowercase, stopwords, remove_notalpha):

    sentence1_words = wni.preprocess(sentence=sentence1, use_stemmer=stemming, use_lowercase=lowercase,
                                     use_stopwords=stopwords, remove_nonalpha=remove_notalpha)
    sentence2_words = wni.preprocess(sentence=sentence2, use_stemmer=stemming, use_lowercase=lowercase,
                                     use_stopwords=stopwords, remove_nonalpha=remove_notalpha)

    sentence_1_synset_list = []
    sentence_2_synset_list = []

    all_noun_hyper = []
    all_verb_hypo = []
    for word1 in sentence1_words:
        sentence_1_synset_list.append(wni.retrieve_synset_list_for_word(word=word1[0]))
    for word2 in sentence2_words:
        sentence_2_synset_list.append(wni.retrieve_synset_list_for_word(word=word2[0]))

    # Weeding out all synsets, which are not either verbs or nouns, as they are not needed
    sentence_1_synset_list = [[item for item in sub_synset if item.pos() == 'n' or item.pos() == 'v'] for sub_synset in sentence_1_synset_list]
    sentence_1_synset_list = [item for item in sentence_1_synset_list if item != []]

    sentence_2_synset_list = [[item for item in sub_synset if item.pos() == 'n' or item.pos() == 'v'] for sub_synset in
                              sentence_2_synset_list]
    sentence_2_synset_list = [item for item in sentence_2_synset_list if item != []]
    for synset1 in sentence_1_synset_list:
        for synset2 in sentence_2_synset_list:
            noun_hyper, verb_hypo= custom_similarity_measure(synset1=synset1, synset2=synset2)
            all_noun_hyper.append(noun_hyper)
            all_verb_hypo.append(verb_hypo)

    custom_similarity = 0.5*(max(all_noun_hyper) + max(all_verb_hypo))
    return custom_similarity
