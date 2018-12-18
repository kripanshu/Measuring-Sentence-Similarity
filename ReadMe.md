### Insturctions
The project is to find the similarity between questions. In order to run the project follow the instructions:
1. Download the data from https://www.kaggle.com/c/quora-question-pairs/data
2. put 'test.csv' and 'train.csv' files in the data folder in home folder ('kxb162030_NLPproject') <br/> <br/>
3. Run the command using code sheet given below: <br/>
<br/> `python3 measure_similarity.py [Similarity feature] [classifer]`
<br/> `For example to run cosine_similarity with SVM => python3 measure_similarity.py "ONE" "EIGHT"`
CODE SHEET :
SyntacticFeatures: <br/>
ONE = COSINE_SIMILARITY <br/>
TWO = JACCARD_SIMILARITY <br/>
THREE = LEMMA_JACCARD_SIMILARITY <br/>
FOUR = COMBINED_SYNTACTIC <br/> <br/>
SemanticFeatures: <br/> 
FIVE = PATH_SIMILARITY <br/>
SIX = WUP_SIMILARITY <br/>
SEVEN = COMBINED_SEMANTIC <br/> <br/>
Classifiers: <br/>
EIGHT = SVM <br/>
NINE = LOGISTIC_REGRESSION <br/>
 <br/>
Configuration:
1. Python3 is used.
2. sklearn, nltk, wordnet, pandas and numpy are major packages used.

References: <br/>
1]  Han, Lushan and Kashyap, Abhay L and Finin, Tim and Mayfield, Jamesand  Weese,  Jonathan,  UMBC  EBIQUITY-CORE:  Semantic  TextualSimilarity Systems., NAACL-HLT, 44-52, 2013. <br/>
[2]  Dao TN, Simpson T, Measuring similarity between sentences, WordNet.Net, Tech. Rep., 2005. <br/>
3]  Sravanthi, P., and Srinivase, D.,SEMANTIC SIMILARITY BETWEENSENTENCES, 2017 <br/>
[4]  Salton,  G.  and  Lesk,  M.E.,  Computer  evaluation  of  indexing  and  textprocessing, Journal of the ACM (JACM), 15(1), pp.8-36, 1968. <br/>
[5]  Hybridapproach-https://drive.google.com/file/d/1kd79of1vrQ–9fSxY9g6hvvduDoPpQIv/view <br/>
[6]  Choi, S. S., Cha, S. H., Tappert, C. C., A survey of binary similarity anddistance  measures.  Journal  of  Systemics,  Cybernetics  and  Informatics,8(1), 43-48, 2010. <br/>
[7]  Jurafsky, D., Speech and language processing: An introduction to naturallanguage processing. Computational linguistics, and speech recognition,2000. <br/>
[8]  https://en.wikipedia.org/wiki/Quora <br/>
[9]  https://www.quora.com/How-many-people-use-Quora-7/answer/Adam-DAngelo <br/>
[10]  WordNet NLTK documentation -http://www.nltk.org/howto/wordnet.html <br/>
[11]  Documents similarity- http://text2vec.org/similarity.html <br/>
[12]  George A. Miller, A Lexical Database for English, Communications ofthe ACM Vol. 38, No. 11: 39-41, 1995. <br/>
[13]  Dataset-https://www.kaggle.com/c/quora-question-pairs <br/>
[14]  lemmajaccard-https://jktauber.com/2017/07/29/nt-book-similarity-jaccard-distance-lemma-sets/ <br/>
[15]  KaggleSimilarity-https://www.kaggle.com/antriksh5235/semantic-similarity-using-wordnet <br/>
[16]  Result   analysis   features   -   https://towardsdatascience.com/accuracy-precision-recall-or-f1-331fb37c5cb9 <br/>
