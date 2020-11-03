# Project 12: Semantic Similarity 2

## We aim in this project to study a new semantic similarity for two short text document

1. Consider two sentences S1 and S2 which are tokenized for instance, say S1=(w1, w2,..,wn) and S2= (p1, p2, …, pm). Consider the approach implemented in Lab2 for calculating the semantic similarity between sentences using WordNet semantic similarity. Check the output for pair of sentences  (This city is awful these days, The city can improve better if better management is made) and comment on the result. Test various preprocessing approaches that you may use and discuss the impact of preprocessing on the result in terms of overall semantic similarity score.

2. We want to test this strategy on publicly available sentence database. For this purpose, use STSS-131 dataset, available in “A new benchmark dataset with production methodology for short text semantic similarity algorithms” by O’Shea, Bandar and Crockett (ACM Trans. on Speech and Language Processing, 10, 2013). Use Pearson correlation coefficient to test the correlation of your result with the provided human judgment. 

3.  Now we want to implement a new semantic similarity based measure. The idea is to use some hierarchical reasoning and explore the WordNet Hierarchy. For this purpose, proceed in the following. For each sentence, use the parser tree to identify various part-of-speech of individual token of the sentence. Generate the list of hypernyms H1 and hyponyms H2 of each noun of the sentence. Repeat this process for each verb. Compute the semantic similarity between the two sentences as

## Implement the above similarity expression in your python code

4. Test the above similarity on STSS-131 database and report the Pearson correlation with human judgments.

5. Study another text similarity using both wordnet semantic similarity and string similarity provided in https://github.com/pritishyuvraj/SOC-PMI-Short-Text-Similarity-. Check the behavior of program for some intuitive sentences (very similar sentences, ambiguous and very dissimilar ones)

6. Report the result of the above similarity on STSS-131 and report the corresponding Pearson correlation with human judgments

7. Suggest an interface of your choice that would allow the user to input a textual query in the form of a pair of sentences and output the similarity score according to the various methods described above.

## How to use the program

It is possible to run the program either from the GUI or from the command line. If it's run from the GUI, the selected options should be quite self-explanatory. The same options exist also for command line, and they can be given with the following parameters:

* -s1 / --sentence1
* -s2 / --sentence2
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
