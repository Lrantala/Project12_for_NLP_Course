from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords as nltk_stopwords
from textblob import TextBlob
from textblob import Word
from nltk.stem import WordNetLemmatizer
import string

posTb2Wn = {'JJ': 'a', 'JJR': 'a', 'JJS': 'a', 'RB': 'r', 'RBR': 'r', 'RBS': 'r', 'VB': 'v', 'VBD': 'v', 'VBG': 'v',
            'VBN': 'v', 'VBP': 'v', 'VBZ': 'v', 'NN': 'n', 'NNS': 'n', 'NNP': 'n', 'NNPS': 'n', 'n': 'n', 'a': 'a',
            'r': 'r', 'v': 'v', 's': 's'}

def preprocess(sentence, use_stemmer=False, use_lowercase=False,
               use_stopwords = False,remove_nonalpha=False, use_lemma = False):
    # We always tokenize
    blob = TextBlob(sentence)

    # words = blob.words
    words_and_tags = blob.tags

    words_and_tags_list = [list(x) for x in words_and_tags]

    # This excludes all the words, which contain special characters. Needed due to the residue from blob.tags
    words_and_tags_list = [[word[0], word[1]] for word in words_and_tags_list if not any(c in string.punctuation for c in word[0])]

    if use_stopwords:
        stopwords = list(set(nltk_stopwords.words('english')))
    else:
        stopwords = []

    # Using just stop words without preprocessing to lower makes little sense, as it doesn't find all of them then
    # Therefore, we need to lowercase akk the words, and then look if they appear in stopwords.
    # Note that we still return the unlowered version for the word, if it's not found in stopwords.
    # words = [word for word in words if word.lower() not in stopwords]

    # List comprehension sorting out. Take the first element for each nested list, and check if it's
    # in the stopwords list. Then root out nested lists, which have only pos remaining.
    words_and_tags_list = [[word for word in wordpos if word.lower() not in stopwords] for wordpos in words_and_tags_list]

    words_and_tags_list = [x for x in words_and_tags_list if len(x) > 1]


    if use_lowercase:
        # words = [word.lower() for word in words if word.lower() not in stopwords]
        words_and_tags_list = [[word[0].lower(), word[1]] for word in words_and_tags_list]

    # Note that this also removes all words, which have a number in them
    if remove_nonalpha:
        # words = [word for word in words if word.isalpha() and word not in stopwords]
        words_and_tags_list = [[word for word in wordpos if word.isalpha()] for wordpos in words_and_tags_list]

        words_and_tags_list = [x for x in words_and_tags_list if len(x) > 1]


    # We stem if asked to, although it will cause problems with synset searches
    # Stemmer also makes words lowercase by default
    if use_stemmer:
        stemmer = SnowballStemmer("english")
        # words = [stemmer.stem(word) for word in words]
        words_and_tags_list = [[stemmer.stem(word[0]), word[1]] for word in words_and_tags_list]

    if use_lemma:
        words_and_tags_list = [[Word(word[0]).lemmatize(pos=posTb2Wn.get(word[1])), word[1]] for word in words_and_tags_list]

    return words_and_tags_list

