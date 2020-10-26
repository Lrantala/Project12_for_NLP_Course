import wordnet_implementation.wordnet_implementation as wni
import custom_similarity_measure.custom_similarity_measure as csm
from sentence_and_word_processing.sentence_and_word_processing import preprocess
import soc_pmi.soc_pmi as soc
from scipy.stats import pearsonr
import pandas as pd

def calculate_pearson_for_sts131(stemming, lowercase, stopwords, remove_notalpha, analyze_measure):
    stss131_df = pd.read_csv("./data/stss131.csv", sep=",")

    # First we run through the dataset row by row, and append the results to a list
    list_of_similarity_values = []
    for s1, s2 in zip(stss131_df.Sentence1, stss131_df.Sentence2):
        if analyze_measure == "original":
            similarity_score = wni.calculate_path_similarity_for_sentences(sentence1=s1, sentence2=s2,
                                                        stemming=stemming, lowercase=lowercase,
                                                        stopwords=stopwords, remove_notalpha=remove_notalpha)
            print("Similarity score of the current sentence pair is:", similarity_score)

        elif analyze_measure == "hypers_and_hypos":
            similarity_score = csm.count_custom_similarity_measure(sentence1=s1, sentence2=s2,
                                                                   stemming=stemming, lowercase=lowercase,
                                                                   stopwords=stopwords,
                                                                   remove_notalpha=remove_notalpha)
            print("Similarity score of the current sentence pair is:", similarity_score)

        elif analyze_measure == "soc_pmi":
            sentence1_words = preprocess(s1, stemming, lowercase, stopwords, remove_notalpha)

            sentence2_words = preprocess(s2, stemming, lowercase, stopwords, remove_notalpha)

            s1_word_list, s2_word_list = [], []

            for word1 in sentence1_words:
                s1_word_list.append(word1[0])

            for word2 in sentence2_words:
                s2_word_list.append(word2[0])

            similarity_score = soc.soc_pmi(s1_word_list, s2_word_list)
            print("Similarity score of the current sentence pair is:", similarity_score)

        list_of_similarity_values.append(similarity_score)

    stss131_df["R"] = pd.Series(list_of_similarity_values)
    pearson_corr = pearsonr(stss131_df.X, stss131_df.R)
    print("Pearson correlation between Rater mean: {corr}, p-value {pval}".format(corr=pearson_corr[0],
                                                                                  pval=pearson_corr[1]))
