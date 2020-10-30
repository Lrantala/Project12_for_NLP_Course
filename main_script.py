import argparse
import logging
import wordnet_implementation.wordnet_implementation as wni
import similarity_functions.pearson_correlation_stss131 as pcorr
import custom_similarity_measure.custom_similarity_measure as csm
from sentence_and_word_processing.sentence_and_word_processing import preprocess
import soc_pmi.soc_pmi as soc
from gooey import Gooey


@Gooey()
def argument_parser():
    parser = argparse.ArgumentParser(description="Parser to read arguments from the command line.")
    parser.add_argument("-s1", "--sentence1", help="First sentence to be processed/analyzed")
    parser.add_argument("-s2", "--sentence2", help="Second sentence to be processed/analyzed")

    parser.add_argument("--measure",
                        default="original",
                        type=str.lower,
                        const="original",
                        nargs="?",
                        choices=("original", "hyp-ed method", "semantic text similarity method"),
                        help="Select similarity measure to use (default: 'original')")

    parser.add_argument("-l", "--lowercase", action="store_true", help="Whether the sentences should be lowercased.")
    parser.add_argument("-s", "--stem", action="store_true", help="Whether the sentences should be stemmed.")
    parser.add_argument("-le", "--lemma", action="store_true", help="Whether the sentences should be lemmatized.")
    parser.add_argument("-v", "--verbose", action="store_true", help="Whether to display logging information.")
    parser.add_argument("-na", "--nonalpha", action="store_true", help="Whether to remove non-alpha characters.")
    parser.add_argument("-st", "--stopwords", action="store_true", help="Whether to use stopwords.")

    parser.add_argument("-stest", "--stss131test", action="store_true", help="Whether to run Pearson correlation to"
                                                                           "STSS-131 dataset with these processing settings.")
    return parser


if __name__ == "__main__":
    parser = argument_parser()
    args = parser.parse_args()

    if bool(args.stem) & bool(args.lemma):
        parser.error('--stem and --lemma can not be given together')

    if args.verbose:
        logging.basicConfig(level=logging.INFO)

    if args.stss131test:
        pcorr.calculate_pearson_for_sts131(stemming=args.stem, lowercase=args.lowercase,
                                           stopwords=args.stopwords, remove_notalpha=args.nonalpha,
                                           analyze_measure=args.measure)

    elif args.measure == "original":
        logging.info("Calculating path similarity for sentences using original formula.")
        sentence_similarity_score = wni.calculate_path_similarity_for_sentences(sentence1=args.sentence1,
                                                                                sentence2=args.sentence2,
                                                                                stemming=args.stem,
                                                                                lowercase=args.lowercase,
                                                                                stopwords=args.stopwords,
                                                                                remove_notalpha=args.nonalpha)
        print("Sentence similarities: " + str(sentence_similarity_score))
    elif args.measure == "hyp-ed method":
        logging.info("Calculating path similarity for sentences using hypernyms and hyponyms.")
        sentence_similarity_score = csm.count_custom_similarity_measure(sentence1=args.sentence1,
                                                                        sentence2=args.sentence2,
                                                                        stemming=args.stem, lowercase=args.lowercase,
                                                                        stopwords=args.stopwords,
                                                                        remove_notalpha=args.nonalpha)
        print("Sentence similarities: " + str(sentence_similarity_score))
    elif args.measure == "semantic text similarity method":
        logging.info("Calculating path similarity for sentences using SOC PMI Alogrithm.")
        sentence1_words = preprocess(sentence=args.sentence1, use_stemmer=args.stem, use_lowercase=args.lowercase,
                                     use_stopwords=args.stopwords, remove_nonalpha=args.nonalpha)

        sentence2_words = preprocess(sentence=args.sentence2, use_stemmer=args.stem, use_lowercase=args.lowercase,
                                     use_stopwords=args.stopwords, remove_nonalpha=args.nonalpha)

        s1_word_list, s2_word_list = [], []

        for word1 in sentence1_words:
            s1_word_list.append(word1[0])

        for word2 in sentence2_words:
            s2_word_list.append(word2[0])

        sentence_similarity_score = soc.soc_pmi(s1_word_list, s2_word_list)
        print("Sentence similarities: " + str(sentence_similarity_score))

