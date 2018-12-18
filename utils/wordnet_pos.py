from nltk.corpus import wordnet

class GetWordnetPos(object):
    def __init__(self, pos_tag):
        """ get the tag and return wordnet tag """
        self.pos_tag = pos_tag
    def get_wordnet_pos(self):
        if self.pos_tag.startswith('J'):
            return wordnet.ADJ
        elif self.pos_tag.startswith('V'):
            return wordnet.VERB
        elif self.pos_tag.startswith('N'):
            return wordnet.NOUN
        elif self.pos_tag.startswith('R'):
            return wordnet.ADV
        else:
            return None
