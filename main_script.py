import argparse
import logging
import wordnet_implementation.wordnet_implementation as wni
from gooey import Gooey

@Gooey()
def argument_parser():
    parser = argparse.ArgumentParser(description="Parser to read arguments from the command line.")
    parser.add_argument("-s1", "--sentence1", help="First sentence to be processed/analyzed")
    parser.add_argument("-s2", "--sentence2", help="Second sentence to be processed/analyzed")

    parser.add_argument("-l", "--lowercase", action="store_true", help="Whether the sentences should be lowercased.")
    parser.add_argument("-s", "--stem", action="store_true", help="Whether the sentences should be stemmed.")
    parser.add_argument("-v", "--verbose", action="store_true", help="Whether to display logging information.")
    parser.add_argument("-na", "--nonalpha", action="store_true", help="Whether to remove non-alpha characters.")
    parser.add_argument("-st", "--stopwords", action="store_true", help="Whether to use stopwords.")
    return parser

if __name__ == "__main__":
    parser = argument_parser()
    args = parser.parse_args()
    if args.verbose:
        logging.basicConfig(level=logging.INFO)

    logging.info("Calculating path similarity for sentences.")
    wni.calculate_path_similarity_for_sentences(sentence1=args.sentence1, sentence2=args.sentence2,
                                                stemming=args.stem, lowercase=args.lowercase,
                                                stopwords=args.stopwords, remove_notalpha=args.nonalpha)

