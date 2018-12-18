import math
import numpy as np
from scipy import spatial
from nltk.corpus import wordnet as wn
from nltk.metrics import edit_distance


class SemanticMeasures(object):
        def path(set1, set2):
            return wn.path_similarity(set1, set2)


        def wup(set1, set2):
            return wn.wup_similarity(set1, set2)


        def edit(word1, word2):
            if float(edit_distance(word1, word2)) == 0.0:
                return 0.0
            return 1.0 / float(edit_distance(word1, word2))

        def computePath(q1, q2):

            R = np.zeros((len(q1), len(q2)))

            for i in range(len(q1)):
                for j in range(len(q2)):
                    if q1[i][1] == None or q2[j][1] == None:
                        sim = SemanticMeasures.edit(q1[i][0], q2[j][0])
                    else:
                        sim = SemanticMeasures.path(wn.synset(q1[i][1]), wn.synset(q2[j][1]))

                    if sim == None:
                        sim = SemanticMeasures.edit(q1[i][0], q2[j][0])

                    R[i, j] = sim

            # print R

            return R
        def computeWup(q1, q2):

            R = np.zeros((len(q1), len(q2)))

            for i in range(len(q1)):
                for j in range(len(q2)):
                    if q1[i][1] == None or q2[j][1] == None:
                        sim = SemanticMeasures.edit(q1[i][0], q2[j][0])
                    else:
                        sim = SemanticMeasures.wup(wn.synset(q1[i][1]), wn.synset(q2[j][1]))

                    if sim == None:
                        sim = SemanticMeasures.edit(q1[i][0], q2[j][0])

                    R[i, j] = sim

            # print R

            return R

        def overallSim(q1, q2, R):

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
