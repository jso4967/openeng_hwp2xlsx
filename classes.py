class Problem:

    def __init__(self, problem_num, passage=None, answer_description=None, answer=None, choices=None):
        self.__problem_num = problem_num
        self.__passage = passage
        self.__answer_description = answer_description
        self.__answer = answer
        self.__choices = choices
        self.__sentences = []

    def addsentence(self, eng_sentence, kor_sentence, first_char=None):
        self.__sentences.append(Sentence(eng_sentence, kor_sentence, first_char))

    def getsentences(self):
        return self.__sentences


class Sentence:

    def __init__(self, eng_sentence, kor_sentence, gender=None):
        self.__eng_sentence = eng_sentence
        self.__kor_sentence = kor_sentence
        self.__gender = gender
        self.__phrases = []

    def addphrase(self, eng_phrase, kor_phrase, doc=None):
        self.__phrases.append(Phrase(eng_phrase, kor_phrase, doc))

    def getphrases(self):
        return self.__phrases

    def edit_phrase(self, eng_phrase, kor_phrase, doc=None):
        self.__phrases[0].add_phrase_at_end(eng_phrase, kor_phrase)

    def edit_sentence(self, eng_sentence, kor_sentence):
        self.__eng_sentence += eng_sentence
        self.__kor_sentence += kor_sentence

class Phrase:

    def __init__(self, eng_phrase, kor_phrase, doc=None):
        self.__eng_phrase = eng_phrase
        self.__kor_phrase = kor_phrase
        self.__doc = doc

    def getall(self):
        return (self.__eng_phrase, self.__kor_phrase)

    def add_phrase_at_end(self, eng_phrase, kor_phrase):
        self.__eng_phrase += eng_phrase
        self.__kor_phrase += kor_phrase

    def get_eng_phrase(self):
        return self.__eng_phrase

    def get_kor_phrase(self):
        return self.__kor_phrase