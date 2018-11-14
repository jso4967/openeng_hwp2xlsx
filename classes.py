class Problem:

    sentences = []

    def __init__(self, problem_num, passage=None, answer_description=None, answer=None, choices=None):
        self.__problem_num = problem_num
        self.__passage = passage
        self.__answer_description = answer_description
        self.__answer = answer
        self.__choices = choices

class Sentence:

    phrases = []

    def __init__(self, eng_sentence, kor_sentence, first_char=None):
        self.__eng_sentence = eng_sentence
        self.__kor_sentence = kor_sentence
        self.__first_char = first_char

class Phrase:

    def __init__(self, eng_phrase, kor_phrase, doc=None):
        self.__eng_phrase = eng_phrase
        self.__kor_phare = kor_phrase
        self.__doc = doc