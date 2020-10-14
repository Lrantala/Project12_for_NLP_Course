import wordnet_implementation.wordnet_implementation as wni

def test_return_whole_synset_list_from_word():
    word = "computer"
    # Testing here just that the synset names are right, if they are the correct synsets are returned
    test_computer_synsets = ["computer.n.01", "calculator.n.01"]
    computer_synsets = wni.retrieve_synset_list_for_word(word, whole_synset=True)
    computer_synset_name_list = [name.name() for name in computer_synsets]
    assert test_computer_synsets == computer_synset_name_list


def test_return_name_synset_list_from_word():
    word = "computer"
    test_computer_synsets = ["computer.n.01", "calculator.n.01"]
    computer_synsets = wni.retrieve_synset_list_for_word(word, whole_synset=False)
    assert test_computer_synsets == computer_synsets


def test_return_hyponym_list_for_synset():
    computer_synset = wni.retrieve_synset_list_for_word("computer")
    computer_synset_1 = computer_synset[0]
    computer_hyponyms = wni.retrieve_hyponym_or_hypernym_list_for_synset(computer_synset_1,
                                                                         whole_synset=False,
                                                                         hypo_or_hyper=0)
    computer_hyponyms_checklist = ["analog_computer.n.01", "digital_computer.n.01",
                                   "home_computer.n.01", "node.n.08", "number_cruncher.n.02",
                                   "pari-mutuel_machine.n.01", "predictor.n.03", "server.n.03",
                                   "turing_machine.n.01", "web_site.n.01"]
    assert computer_hyponyms == computer_hyponyms_checklist


def test_return_hypernym_list_for_synset():
    computer_synset = wni.retrieve_synset_list_for_word("computer")
    computer_synset_1 = computer_synset[0]
    computer_hyponyms = wni.retrieve_hyponym_or_hypernym_list_for_synset(computer_synset_1,
                                                                         whole_synset=False,
                                                                         hypo_or_hyper=1)
    computer_hyponyms_checklist = ["machine.n.01"]
    assert computer_hyponyms == computer_hyponyms_checklist


def test_calculate_path_similarity_for_synset_lists():
    computer_synset = wni.retrieve_synset_list_for_word("computer")
    analog_computer_synset = wni.retrieve_synset_list_for_word("analog_computer")
    similarity_score = wni.calculate_path_similarity_for_synset_lists(computer_synset, analog_computer_synset)
    assert similarity_score == 0.5


def test_calculate_path_similarity_for_synset_lists():
    computer_synset = wni.retrieve_synset_list_for_word("cat")
    analog_computer_synset = wni.retrieve_synset_list_for_word("dog")
    similarity_score = wni.calculate_path_similarity_for_synset_lists(computer_synset, analog_computer_synset)
    assert similarity_score == 0.2
