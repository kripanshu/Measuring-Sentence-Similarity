from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
class SyntacticMeasures(object):

    def getCosineSimilarity(tokenList1, tokenList2):
        bowList1 = {}
        bowList2 = {}
        for i in range(0, len(tokenList1)):
            if tokenList1[i] in bowList1:
            # if bowList1.has_key(tokenList1[i]):
                bowList1[tokenList1[i]] += 1
            else:
                bowList1[tokenList1[i]] = 1
        for i in range(0, len(tokenList2)):
            if tokenList2[i] in bowList2:
            # if bowList2.has_key(tokenList2[i]):
                bowList2[tokenList2[i]] += 1
            else:
                bowList2[tokenList2[i]] = 1
        # print(bowList1, " and ", bowList2)

        x = list(bowList1.values())
        y = list(bowList2.values())
        if len(x) == 0:
            return 0.0
        if len(x) > len(y):
            y.extend([0 for _ in range(0, len(x) - len(y))])
        elif len(y) > len(x):
            x.extend([0 for _ in range(0, len(y) - len(x))])
        x = np.array(x).reshape(1,-1)
        y = np.array(y).reshape(1,-1)

        # print( x , " and " , y)
        return cosine_similarity(x, y)[0][0]

    def normal_jaccard_distance(tokenList1, tokenList2):
        """ jackard distance using only tokens """
        text1Set = set(tokenList1)
        text2Set = set(tokenList2)
        if len(text1Set.union(text2Set)) > 0:
            return (len(text1Set.intersection(text2Set)) * 1.0) / (len(text1Set.union(text2Set)) * 1.0)

    def lemma_jaccard_distance(lemma1, lemma2):
        """ jackard distance using lemmas """
        text1Set = set(lemma1)
        text2Set = set(lemma2)
        if len(text1Set.union(text2Set)) > 0:
            return (len(text1Set.intersection(text2Set)) * 1.0) / (len(text1Set.union(text2Set)) * 1.0)


    def overallSyn(q1, q2,  R):

        sum_X = 0.0
        sum_Y = 0.0


        for i in range(len(q1)):
            max_i = 0.0
            for j in range(len(q2)):
                if R[i, j] > max_i:
                    max_i = R[i, j]
            sum_X += max_i

        for i in range(len(q1)):
            max_j = 0.0
            for j in range(len(q2)):
                if R[i, j] > max_j:
                    max_j = R[i, j]
            sum_Y += max_j


        if (float(len(q1)) + float(len(q2))) == 0.0:
            return 0.0

        overall = (sum_X + sum_Y) / (float(len(q1)) + float(len(q2)))

        return overall
