class Problem:

    sentences = []

    def __init__(self, problem_num, passage=None, answer_description=None, answer=None, choices=None):
        self.__problem_num = problem_num
        self.__passage = passage
        self.__answer_description = answer_description
        self.__answer = answer
        self.__choices = choices

    def addsentence(self, eng_sentence, kor_sentence, first_char=None):
        self.sentences.append(Sentence(eng_sentence, kor_sentence, first_char))


class Sentence:

    phrases = []

    def __init__(self, eng_sentence, kor_sentence, gender=None):
        self.__eng_sentence = eng_sentence
        self.__kor_sentence = kor_sentence
        self.__gender = gender

    def addphrase(self, eng_phrase, kor_phrase, doc=None):
        self.phrases.append(Phrase(eng_phrase, kor_phrase, doc))

class Phrase:

    def __init__(self, eng_phrase, kor_phrase, doc=None):
        self.__eng_phrase = eng_phrase
        self.__kor_phrase = kor_phrase
        self.__doc = doc

    def getall(self):
        return (self.__eng_phrase, self.__kor_phrase)