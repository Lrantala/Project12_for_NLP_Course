from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords as nltk_stopwords

def preprocess(sentence, use_stemmer=False, use_lowercase=False, use_stopwords = False):
    if use_stopwords:
        stopwords = list(set(nltk_stopwords.words('english')))
    else:
        stopwords = []

    # We always tokenize
    words = word_tokenize(sentence)

    if use_lowercase:
        words = [word.lower() for word in words if
                 word.isalpha() and word not in stopwords]

    # We stem if asked to, although it will cause problems with synset searches
    if use_stemmer:
        stemmer = SnowballStemmer(
            "english")
        words = [stemmer.stem(word) for word in words]
    return words
