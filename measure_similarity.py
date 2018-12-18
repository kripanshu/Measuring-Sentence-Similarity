""" Author : Kripanshu Bhargava kxb162030
This is the main python file we run.
Data : It is taken from kaggle which does not allow sharing of dataset. SO THE DATA FOLDER IS KEPT EMPTY.
In order to run the software, download the data from the link:
https://www.kaggle.com/c/quora-question-pairs/data
data folder should contain the 'test.csv' and 'train.csv' file.
"""
import sys
import pandas as pd
import numpy as np
from pre_processor import Preprocess
from semantic_features import SemanticFeatures
from syntactic_features import SyntacticFeatures
from machine_learning_processor import MachineLearningClassifier
from sklearn.metrics import precision_recall_fscore_support

"""

CODE SHEET :
ONE = COSINE_SIMILARITY
TWO = JACCARD_SIMILARITY
THREE = LEMMA_JACCARD_SIMILARITY
FOUR = COMBINED_SYNTACTIC

FIVE = PATH_SIMILARITY
SIX = WUP_SIMILARITY
SEVEN = COMBINED_SEMANTIC

EIGHT = SVM
NINE = LOGISTIC_REGRESSION
"""

class MeasureSimilarity(object):
    def __init__(self, feature_code, classifier_code):
        print("hello")
        self.training_dataset_size = 3000
        self.testing_dataset_size = 1000
        self.feature_code = feature_code
        self.classifier_code = classifier_code
        print(" feature_code : ",self.feature_code)
        print(" classifier_code : ",self.classifier_code)
        self.data_setup()

    def data_setup(self):
        """ sets up data and call functions for feature generations and classifer"""
        # Make sure the dataset is download and put into the data folder
        training_data = pd.read_csv('./data/train.csv', sep=',', nrows=self.training_dataset_size)
        testing_data = pd.read_csv('./data/test.csv', sep=',' , nrows=self.training_dataset_size)
        question_list1 = training_data['question1']
        question_list2 = training_data['question2']
        is_duplicate = training_data['is_duplicate']
        # for will
        X = []
        Y = []
        for i in range(0, 1000):
            print("*"*20, i ,"*"*20 )
            feature = self.call_feature_generator(question_list1[i],question_list2[i], self.feature_code )
            X.append(feature)
            Y.append(is_duplicate[i])
            print(feature)
            print(is_duplicate[i])
            print(question_list1[i])
            print(question_list2[i])

        # we train classifier

        classifer = self.call_classifier(X, Y, self.classifier_code)

        #  testing
        testX = []
        testY = []

        for i in range(1001, 1500):
            print("-"*20, i ,"-"*20 )
            feature = self.call_feature_generator(question_list1[i],question_list2[i], self.feature_code )
            testX.append(feature)
            testY.append(is_duplicate[i])

        X= np.array(testX).reshape(-1,1)

        calculate_y = classifer.predict(X)

        print(calculate_y)
        tp = 0.0
        fp = 0.0
        fn = 0.0

        for i in range(0, len(calculate_y)):
            if calculate_y[i] == testY[i]:
                print("Tp : ", testX[i], question_list1[i], question_list2[i], is_duplicate[i] )
                tp += 1.0
            else:
                if testY[i] == 1 and calculate_y[i] == 0:
                    print("Fn : ", testX[i] , question_list1[i], question_list2[i], is_duplicate[i] )
                    fn += 1.0
                else:
                    print("Fp : ", testX[i],  question_list1[i], question_list2[i], is_duplicate[i])
                    fp += 1.0

        print("Tp: ", tp, " Fp: ", fp, " Fn: ", fn)
        print("Accuracy ", tp/( tp+fn), "%")

        result = precision_recall_fscore_support(testY, calculate_y)
        print ("Precision: Class 1 - ", result[0][0], "% and Class 0 - ", result[0][1], "%")
        print ("Recall: Class 1 - ", result[1][0], "% and Class 0 - ", result[1][1], "%")
        print ("F-Score: Class 1 - ", result[2][0], "% and Class 0 - ", result[2][1], "%")

    def call_classifier(self, x, y, code):
        """ control the implementation """
        # print("X  :",x)
        # print("Y  :",y)
        print(code)
        if code == "EIGHT":
            classifier = MachineLearningClassifier.svm_classifier(x, y)
            return classifier
        elif code == "NINE":
            classifier = MachineLearningClassifier.logistic_regression_classifier(x, y)
            return classifier
        else:
            raise ValueError('Enter correct Code for classifier')


    def call_feature_generator(self, ques1, ques2, code):
        print(str(code))
        # using lemma
        processer1 = Preprocess(ques1)
        lemma_ques1 = processer1.preprocess_with_lemma()

        processer2 = Preprocess(ques2)
        lemma_ques2 = processer2.preprocess_with_lemma()

        # without using lemma
        processer1 = Preprocess(ques1)
        token_ques1 = processer1.preprocess_without_lemma()

        processer2 = Preprocess(ques2)
        token_ques2 = processer2.preprocess_without_lemma()


        syntactic_obj = SyntacticFeatures()
        semantic_obj = SemanticFeatures()

        if code == "ONE":
            cosine_similarity_score = syntactic_obj.compute_cosine_similarity(token_ques1, token_ques2)
            return cosine_similarity_score
        elif code == "TWO":
            jaccard_similarity_score = syntactic_obj.compute_jaccard_similarity(token_ques1, token_ques2)
            return jaccard_similarity_score
        elif code == "THREE":
            lemma_jaccard_similarity_score = syntactic_obj.compute_lemma_jaccard_similarity(lemma_ques1, lemma_ques2)
            return lemma_jaccard_similarity_score
        elif code == "FOUR":
            combined_syn_score = syntactic_obj.overall_similarity_combined(token_ques1, token_ques2, lemma_ques1, lemma_ques2)
            return combined_syn_score
        elif code == "FIVE":
            path_similarity_score = semantic_obj.overall_similarity_path_similarity(lemma_ques1, lemma_ques2)
            return path_similarity_score
        elif code == "SIX":
            wup_similarity_score = semantic_obj.overall_similarity_wup_similarity(lemma_ques1, lemma_ques2)
            return wup_similarity_score
        elif code == "SEVEN":
            combined_similarity_score = semantic_obj.overall_similarity_combined(lemma_ques1, lemma_ques2)
            return combined_similarity_score
        else:
            raise ValueError('Enter correct Code for feature')


if __name__ == '__main__':
    # creates an instance of the class
    feature_code = sys.argv[1]
    classifier_code = sys.argv[2]
    if feature_code is None:
        feature_code = "ONE"
    elif classifier_code is None:
        classifier_code = "EIGHT"
    my_obj = MeasureSimilarity(feature_code, classifier_code)
