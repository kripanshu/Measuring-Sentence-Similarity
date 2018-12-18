from utils.syntactic_similarity_measures import SyntacticMeasures

class SyntacticFeatures(object):
    @staticmethod
    def compute_cosine_similarity(token1, token2):
        """ compute cosine similarity """
        cosine_similarity = SyntacticMeasures.getCosineSimilarity(token1,token2)
        return cosine_similarity

    @staticmethod
    def compute_jaccard_similarity(token1, token2):
        """ compute jaccard similarity"""
        jaccard_similarity = SyntacticMeasures.normal_jaccard_distance(token1,token2)

        return jaccard_similarity

    @staticmethod
    def compute_lemma_jaccard_similarity(lemma1, lemma2):
        """ compute lemma jaccard similarity"""
        lemma_jaccard_similarity = SyntacticMeasures.lemma_jaccard_distance(lemma1,lemma2)

        return lemma_jaccard_similarity

    @staticmethod
    def compute_combined_score_syn(r1, r2, r3):
        """ get the combined score"""
        return (r1+r2+r3)/ 3

    @staticmethod
    def overall_similarity_combined(token1, token2, lemma1, lemma2):
        """ calculate combined similarity """

        R1 = SyntacticFeatures.compute_cosine_similarity(token1,token2)
        R2 = SyntacticFeatures.compute_jaccard_similarity(token1,token2)
        R3 = SyntacticFeatures.compute_lemma_jaccard_similarity(lemma1,lemma2)
        R = SyntacticFeatures.compute_combined_score_syn(R1,R2,R3)

        return R
