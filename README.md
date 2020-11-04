# Project 12: Semantic Similarity 2

This program is related to the Project 12 on the NLP Course. Please see the returned paper for details.


## How to use the program

It is possible to run the program either from the GUI or from the command line. If it's run from the GUI, the selected options should be quite self-explanatory. The same options exist also for command line, and they can be given with the following parameters:

* -s1 / --sentence1
* -s2 / --sentence2
* -m / --measure
* -l / --lowercase
* -s / --stem
* -le / --lemma
* -v / --verbose
* -na / --nonalpha
* -st / --stopwords
* -stest / --stss131test

### -s1 / --sentence1
First sentence to be processed/analyzed

### -s2 / --sentence2
Second sentence to be processed/analyzed

### -m / --measure
Semantic measure to be used. Possible choices are: "original", "hyp-ed method" or "emantic text similarity method". Default: "original".
"Original" refers to Wordnet Path Similarity Measure, "hyp-ed method" refers to the Hyponym and Hypernym Semantic Similarity Measure, and "semantic text similarity method" refers to SOC-PMI Semantic Text Similarity Measure.

### -l / --lowercase
Boolean flag. If present, the words in sentences are lowercased.

### -s / --stem
Boolean flag. If present, the words in sentences are stemmed. Note that this can degrade performance when utilizin WordNet Measure.

### -le / --lemma
Boolean flag. If present, the words in sentences are lemmatized.

### -v / --verbose
Boolean flag. If present, displays logging information. Present for debugging purposes.

### -na / --nonalpha
Boolean flag. If present, removes words containing non-alphabetic characters

### -st / --stopwords
Boolean flag. If present, removes words stopwords as presented in NLTK's stopwords list.

### -stest / --stss131test
Boolean flag. If present, utilizes the selected preprocessing parameters and selected semantic similarity measure, and runs it against the STSS131 dataset. Displays Pearson correlation with the selected measure and preprocessing settings against the human raters ratings from that dataset.
