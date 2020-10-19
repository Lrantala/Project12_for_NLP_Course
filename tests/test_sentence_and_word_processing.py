import sentence_and_word_processing.sentence_and_word_processing as swp

def test_preprocessing_tokenize():
    test_sentence = "This is A TEST SENtence, to Make Sure Lower works"
    result_sentence = ["This", "is", "A", "TEST", "SENtence", "to", "Make", "Sure", "Lower", "works"]
    preprocessed_sentence = swp.preprocess(sentence=test_sentence, use_stemmer=False,
                                           use_lowercase=False, use_stopwords=False, remove_nonalpha=False)
    preprocessed_sentence_just_words = [word[0] for word in preprocessed_sentence]
    assert result_sentence == preprocessed_sentence_just_words

def test_preprocessing_tolower():
    test_sentence = "This is A TEST SENtence, to Make Sure Lower works"
    result_sentence = ["this", "is", "a", "test", "sentence", "to", "make", "sure", "lower", "works"]
    preprocessed_sentence = swp.preprocess(sentence=test_sentence, use_stemmer=False,
                                           use_lowercase=True, use_stopwords=False, remove_nonalpha=False)
    preprocessed_sentence_just_words = [word[0] for word in preprocessed_sentence]
    assert result_sentence == preprocessed_sentence_just_words

def test_preprocessing_remove_stopwords():
    test_sentence = "This is A TEST SENtence, to Make Sure Lower works"
    result_sentence = ["TEST", "SENtence", "Make", "Sure", "Lower", "works"]
    preprocessed_sentence = swp.preprocess(sentence=test_sentence, use_stemmer=False,
                                           use_lowercase=False, use_stopwords=True, remove_nonalpha=False)
    preprocessed_sentence_just_words = [word[0] for word in preprocessed_sentence]
    assert result_sentence == preprocessed_sentence_just_words

def test_preprocessing_stem():
    test_sentence = "This is A TEST SENtence, to Make Sure Lower works"
    result_sentence = ["this", "is", "a", "test", "sentenc", "to", "make", "sure", "lower", "work"]
    preprocessed_sentence = swp.preprocess(sentence=test_sentence, use_stemmer=True,
                                           use_lowercase=False, use_stopwords=False, remove_nonalpha=False)
    preprocessed_sentence_just_words = [word[0] for word in preprocessed_sentence]
    assert result_sentence == preprocessed_sentence_just_words

def test_preprocessing_tolower_remove_nonalpha():
    test_sentence = "This is A TEST SENtence, to Make Sure Lower works"
    result_sentence = ["this", "is", "a", "test", "sentence", "to", "make", "sure", "lower", "works"]
    preprocessed_sentence = swp.preprocess(sentence=test_sentence, use_stemmer=False,
                                           use_lowercase=True, use_stopwords=False, remove_nonalpha=True)
    preprocessed_sentence_just_words = [word[0] for word in preprocessed_sentence]
    assert result_sentence == preprocessed_sentence_just_words

def test_preprocessing_tokenize_remove_nonalpha():
    test_sentence = "This is A TEST SENtence, to Make6 Sure Lower works"
    result_sentence = ["This", "is", "A", "TEST", "SENtence", "to", "Sure", "Lower", "works"]
    preprocessed_sentence = swp.preprocess(sentence=test_sentence, use_stemmer=False,
                                           use_lowercase=False, use_stopwords=False, remove_nonalpha=True)
    preprocessed_sentence_just_words = [word[0] for word in preprocessed_sentence]
    assert result_sentence == preprocessed_sentence_just_words

def test_preprocessing_lower_remove_stopwords():
    test_sentence = "This is A TEST SENtence, to Make6 Sure Lower works"
    result_sentence = ["test", "sentence", "make6", "sure", "lower", "works"]
    preprocessed_sentence = swp.preprocess(sentence=test_sentence, use_stemmer=False,
                                           use_lowercase=True, use_stopwords=True, remove_nonalpha=False)
    preprocessed_sentence_just_words = [word[0] for word in preprocessed_sentence]
    assert result_sentence == preprocessed_sentence_just_words

def test_preprocessing_lower_remove_stopwords_and_nonalpha():
    test_sentence = "This is A TEST SENtence, to Make6 Sure Lower works"
    result_sentence = ["test", "sentence", "sure", "lower", "works"]
    preprocessed_sentence = swp.preprocess(sentence=test_sentence, use_stemmer=False,
                                           use_lowercase=True, use_stopwords=True, remove_nonalpha=True)
    preprocessed_sentence_just_words = [word[0] for word in preprocessed_sentence]
    assert result_sentence == preprocessed_sentence_just_words