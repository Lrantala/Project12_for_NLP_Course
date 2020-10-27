from joblib.numpy_pickle_utils import xrange
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer

import try1
# import word as wd
import wn3
import wordSim


def soc_pmi(s1, s2):


    #tokenizer = RegexpTokenizer(r'\w+')
    #S1 = tokenizer.tokenize(s1)
    #S2 = tokenizer.tokenize(s2)

    #ltz = WordNetLemmatizer()
    #S1 = [ltz.lemmatize(word.lower()) for word in s1]
    #S2 = [ltz.lemmatize(word.lower()) for word in s2]

    '''
    tokenizer = RegexpTokenizer(r'\w+')
    S1 = tokenizer.tokenize(S1)
    S2 = tokenizer.tokenize(S2)
    '''
    #S1_filtered = [word for word in S1 if word not in stopwords.words('english')]
    #S2_filtered = [word for word in S2 if word not in stopwords.words('english')]


    # Start of Step 2
    score, common = wordSim.wordSim(s1, s2)

    S1_next = [word for word in s1 if word not in common]
    S2_next = [word for word in s2 if word not in common]

    h, w = len(S1_next), len(S2_next)

    Matrix1 = [[0.0 for x in range(w)] for x in range(h)]


    for i in range(len(S1_next)):
        for j in range(len(S2_next)):
            Matrix1[i][j] = try1.calling(S1_next[i], S2_next[j])

    # End of Step 3

    # Begining of Step 4
    Matrix2 = [[0.0 for x in range(w)] for x in range(h)]

    for i in range(len(S1_next)):
        for j in range(len(S2_next)):
            Matrix2[i][j] = wn3.returnWordSim(S1_next[i], S2_next[j])

    # End of Step 4

    # Begining of Step 5
    Matrix = [[0.0 for x in range(w)] for x in range(h)]
    for i in range(len(S1_next)):
        for j in range(len(S2_next)):
            Matrix[i][j] = (0.5 * Matrix1[i][j]) + (0.5 * Matrix2[i][j])


    # Looping to find Pi
    def delete(matrix, i, j):
        for row in matrix:
            del row[j]
        matrix = [matrix[i1] for i1 in range(len(matrix)) if i1 != i]
        return matrix

    Pi = []
    while (len(Matrix) > 0 and len(Matrix[i]) > 0):
        # Search for maximum Element
        maxelement = 0
        maxi, maxj = 0, 0
        for i in range(len(Matrix)):
            for j in range(len(Matrix[i])):
                if Matrix[i][j] > maxelement:

                    maxelement = Matrix[i][j]
                    maxi = i
                    maxj = j
        Pi.append(Matrix[maxi][maxj])

        Matrix = delete(Matrix, maxi, maxj)

        for i in range(len(Matrix)):
            print(Matrix[i])
    # End of Step 5

    #Begining of Step 6
    Delta = 2.0

    if len(Pi) == 0:
        similarity = 1.8
        print("Forced similarity score is", similarity)
    else:
        similarity = ((Delta + sum(Pi)) * (len(S1_next) + len(S2_next))) / (2 * len(S1_next) * len(S2_next))
        print("Similarity Score", similarity)
    return similarity
