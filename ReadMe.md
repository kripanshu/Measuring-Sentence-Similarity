### Insturctions
The project is to find the similarity between questions. In order to run the project follow the instructions:
1. Download the data from https://www.kaggle.com/c/quora-question-pairs/data
2. put 'test.csv' and 'train.csv' files in the data folder in home folder ('kxb162030_NLPproject')
3. Run the command using code sheet given below:
`python3 measure_similarity.py [Similarity feature] [classifer]`
`For example to run cosine_similarity with SVM => python3 measure_similarity.py "ONE" "EIGHT"`
CODE SHEET :
SyntacticFeatures:
ONE = COSINE_SIMILARITY
TWO = JACCARD_SIMILARITY
THREE = LEMMA_JACCARD_SIMILARITY
FOUR = COMBINED_SYNTACTIC
SemanticFeatures:
FIVE = PATH_SIMILARITY
SIX = WUP_SIMILARITY
SEVEN = COMBINED_SEMANTIC
Classifiers:
EIGHT = SVM
NINE = LOGISTIC_REGRESSION

Configuration:
1. Python3 is used.
2. sklearn, nltk, wordnet, pandas and numpy are major packages used.
MailTo : kxb162030@utdallas.edu if any problem occurs in running.
