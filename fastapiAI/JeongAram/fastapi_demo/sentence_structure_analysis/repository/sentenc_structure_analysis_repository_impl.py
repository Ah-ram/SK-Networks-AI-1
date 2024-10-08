import spacy
from nltk import sent_tokenize, word_tokenize

from sentence_structure_analysis.repository.sentence_structure_analysis_repository import \
    SentenceStructureAnalysisRepository


class SentenceStructureAnalysisRepositoryImpl(SentenceStructureAnalysisRepository):

    def sentenceTokenize(self, text):
        print(f'repository -> sentenceTokenize(): {text}')
        return sent_tokenize(text)

    def wordTokenize(self, text):
        return word_tokenize(text)

    def sentenceAnalysis(self, text):
        englishLanguagePack = spacy.load("en_core_web_sm")
        document = englishLanguagePack(text)

        # Noun(명사), Pron(대명사), Verb(동사), Adj(형용사), Adv(부사), Det(한정사), Part(조사)
        # Aux(조동사), Conj(접속사), Punct(구두점), SCONJ(종속 접속사), PROPN(고유 대명사)

        for token in document:
            print(f"단어: {token.text}, 품사: {token.pos_}, 종속 관계: {token.dep_}, 부모 단어: {token.head.text}")

        return document

