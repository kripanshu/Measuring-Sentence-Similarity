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

References:
1]  Han, Lushan and Kashyap, Abhay L and Finin, Tim and Mayfield, Jamesand  Weese,  Jonathan,  UMBC  EBIQUITY-CORE:  Semantic  TextualSimilarity Systems., NAACL-HLT, 44-52, 2013.
[2]  Dao TN, Simpson T, Measuring similarity between sentences, WordNet.Net, Tech. Rep., 2005.
3]  Sravanthi, P., and Srinivase, D.,SEMANTIC SIMILARITY BETWEENSENTENCES, 2017
[4]  Salton,  G.  and  Lesk,  M.E.,  Computer  evaluation  of  indexing  and  textprocessing, Journal of the ACM (JACM), 15(1), pp.8-36, 1968.
[5]  Hybridapproach-https://drive.google.com/file/d/1kd79of1vrQ–9fSxY9g6hvvduDoPpQIv/view
[6]  Choi, S. S., Cha, S. H., Tappert, C. C., A survey of binary similarity anddistance  measures.  Journal  of  Systemics,  Cybernetics  and  Informatics,8(1), 43-48, 2010.
[7]  Jurafsky, D., Speech and language processing: An introduction to naturallanguage processing. Computational linguistics, and speech recognition,2000.
[8]  https://en.wikipedia.org/wiki/Quora
[9]  https://www.quora.com/How-many-people-use-Quora-7/answer/Adam-DAngelo
[10]  WordNet NLTK documentation -http://www.nltk.org/howto/wordnet.html
[11]  Documents similarity- http://text2vec.org/similarity.html
[12]  George A. Miller, A Lexical Database for English, Communications ofthe ACM Vol. 38, No. 11: 39-41, 1995.
[13]  Dataset-https://www.kaggle.com/c/quora-question-pairs
[14]  lemmajaccard-https://jktauber.com/2017/07/29/nt-book-similarity-jaccard-distance-lemma-sets/
[15]  KaggleSimilarity-https://www.kaggle.com/antriksh5235/semantic-similarity-using-wordnet
[16]  Result   analysis   features   -   https://towardsdatascience.com/accuracy-precision-recall-or-f1-331fb37c5cb9
