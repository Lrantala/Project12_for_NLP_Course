from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords as nltk_stopwords

def preprocess(sentence, use_stemmer=False, use_lowercase=False, use_stopwords = False, remove_nonalpha=False):
    # We always tokenize
    words = word_tokenize(sentence)


    if use_stopwords:
        stopwords = list(set(nltk_stopwords.words('english')))
    else:
        stopwords = []

    # Using just stop words without preprocessing to lower makes little sense, as it doesn't find all of them then
    words = [word for word in words if word not in stopwords]

    if use_lowercase:
        words = [word.lower() for word in words if word.lower() not in stopwords]

    # Note that this also removes all words, which have a number in them
    if remove_nonalpha:
        words = [word for word in words if
                 word.isalpha() and word not in stopwords]
    # We stem if asked to, although it will cause problems with synset searches
    # Stemmer also makes words lowercase by default
    if use_stemmer:
        stemmer = SnowballStemmer("english")
        words = [stemmer.stem(word) for word in words]
    return words
