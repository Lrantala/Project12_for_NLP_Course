import sentence_and_word_processing.sentence_and_word_processing as swp

def test_preprocessing_tolower():
    test_sentence = "This is A TEST SENtence, to Make Sure Lower works"
    result_sentence = ["this", "is", "a", "test", "sentence", "to", "make", "sure", "lower", "works"]
    preprocessed_sentence = swp.preprocess(sentence=test_sentence, use_stemmer=False, use_lowercase=True,use_stopwords=False)
    assert result_sentence == preprocessed_sentence

