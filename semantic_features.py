import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import math
import nltk
from nltk.corpus import wordnet as wn
from nltk import word_tokenize
from utils.lesk_algorithm import Lesk
from utils.semantic_similarity_measures import SemanticMeasures
import re

class SemanticFeatures(object):

    @staticmethod
    def get_lesk(ques):
        """ get each word meaning out of the given question"""
        lesk_obj = Lesk(ques)
        sentence_means = []
        for word in ques:
            sentence_means.append(lesk_obj.lesk(word, ques))
        return sentence_means

    @staticmethod
    def compute_path_similarity(sentence_means1, sentence_means2):
        """ get the path similarity score for two sentences"""
        score = SemanticMeasures.computePath(sentence_means1, sentence_means2)

        return score

    @staticmethod
    def compute_combined_score(r1, r2):
        """ get the combined score"""
        return (r1+r2)/ 2

    @staticmethod
    def compute_wup_similarity(sentence_means1, sentence_means2):
        """ get the wup similarity score for two sentences"""
        score = SemanticMeasures.computeWup(sentence_means1, sentence_means2)

        return score

    # def runner(self):
    #     """Calls all function and classes"""
    #     sentence_means1 = SemanticFeatures.get_lesk(self.ques1)
    #     sentence_means2 = SemanticFeatures.get_lesk(self.ques2)
    #
    #     print("Sentence Means 1 : ", sentence_means1)
    #     print("Sentence Means 2 : ", sentence_means2)
    #
    #     R1 = SemanticFeatures.compute_path_similarity(sentence_means1, sentence_means2)
    #     R2 = SemanticFeatures.compute_wup_similarity(sentence_means1, sentence_means2)
    #
    #     print("R1 : ", R1)
    #     print("R2 : ", R2)
    #
    #     R = (R1 + R2) / 2
    #
    #     path_similarity_overall = SemanticFeatures.overall_similarity_wup_similarity(R1, sentence1Means, sentence2Means)
    #     wup_similarity_overall = SemanticFeatures.overall_similarity_wup_similarity(R2, sentence1Means, sentence2Means )
    #     combined_similarity_overall = SemanticFeatures.overall_similarity_wup_similarity( R, sentence1Means, sentence2Means)
    #
    #     print("overall similarity for wup_similarity : ", wup_similarity_overall )
    #     print("overall similarity for path_similarity : ", path_similarity_overall)
    #     print("overall similarity for wup_similarity + path_similarity : ", combined_similarity_overall)

    @staticmethod
    def overall_similarity_combined(ques1, ques2):
        """ calculate combined similarity """
        sentence_means1 = SemanticFeatures.get_lesk(ques1)
        sentence_means2 = SemanticFeatures.get_lesk(ques2)

        R1 = SemanticFeatures.compute_path_similarity(sentence_means1, sentence_means2)
        R2 = SemanticFeatures.compute_wup_similarity(sentence_means1, sentence_means2)

        R = SemanticFeatures.compute_combined_score(R1,R2)
        print("combined score for ", sentence_means1, " and ", sentence_means2, " is ", R)

        return SemanticMeasures.overallSim(sentence_means1, sentence_means2, R)

    @staticmethod
    def overall_similarity_wup_similarity(ques1, ques2):
        """ calculate wup similarity """
        sentence_means1 = SemanticFeatures.get_lesk(ques1)
        sentence_means2 = SemanticFeatures.get_lesk(ques2)

        R1 = SemanticFeatures.compute_wup_similarity(sentence_means1, sentence_means2)

        return SemanticMeasures.overallSim(sentence_means1, sentence_means2, R1)

    @staticmethod
    def overall_similarity_path_similarity(ques1, ques2):
        """ calculate path similarity """
        sentence_means1 = SemanticFeatures.get_lesk(ques1)
        sentence_means2 = SemanticFeatures.get_lesk(ques2)

        R1 = SemanticFeatures.compute_path_similarity(sentence_means1, sentence_means2)

        return SemanticMeasures.overallSim(sentence_means1, sentence_means2, R1)
