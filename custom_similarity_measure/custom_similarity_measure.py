import nltk
from nltk.corpus import wordnet

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
            print("Neither a noun nor a verb in the supplied synset. That's strange")
            break

    for syns in synset2:
        if syns.pos() == 'n':
            synset2_hyper.append(syns.hypernyms())
        elif syns.pos() == 'v':
            synset2_hypo.append(syns.hyponyms())
        else:
            print("Neither a noun nor a verb in the supplied synset. That's strange")
            break

## Takes care of the equation that's inside the bracket, minus the 'max' part
    common_hyper = commonality(synset1_hyper,synset2_hyper)
    total_hyper = hyp_union(synset1_hyper) + hyp_union(synset2_hyper)
    noun_hyper = common_hyper/total_hyper

    common_hypo = commonality(synset1_hypo, synset2_hypo)
    total_hypo = hyp_union(synset1_hypo) + hyp_union(synset2_hypo)
    verb_hypo = common_hypo / total_hypo

    return noun_hyper, verb_hypo # to be returned to the function that makes the call for the custom similarity measure

def commonality(synset1, synset2):
    count = 0
    for item1 in synset1:
        for item2 in synset2:
               if item1 == item2 and item1==item2 != []:
                   count += 1
    return count

def hyp_union(hyp_list):
    count = 0
    for item in hyp_list:
        if item:
            count += 1
    return count

## The following block of code should be in the module where the call is made to the custom similarity measure
    all_noun_hyper.append(noun_hyper)
    all_verb_hypo.append(verb_hypo)

    custom_similarity = 0.5*(max(all_noun_hyper) + max(all_verb_hypo))

## the block of code ends here


