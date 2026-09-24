# 7. Abstract class Question with evaluate_answer()

from abc import ABC, abstractmethod

class Question(ABC):
    @abstractmethod
    def evaluate_answer(self, given_answer):
        pass


class MCQQuestion(Question):
    def __init__(self, correct_option):
        self.correct_option = correct_option

    def evaluate_answer(self, given_answer):
        return given_answer == self.correct_option


class TrueFalseQuestion(Question):
    def __init__(self, correct_answer):
        self.correct_answer = correct_answer

    def evaluate_answer(self, given_answer):
        return given_answer == self.correct_answer


class DescriptiveQuestion(Question):
    def __init__(self, keywords):
        self.keywords = keywords   # expected keywords in answer

    def evaluate_answer(self, given_answer):
        return any(k in given_answer for k in self.keywords)


mcq = MCQQuestion("B")
tf = TrueFalseQuestion(True)
desc = DescriptiveQuestion(["polymorphism", "inheritance"])

print("MCQ Correct:", mcq.evaluate_answer("B"))
print("True/False Correct:", tf.evaluate_answer(True))
print("Descriptive Correct:", desc.evaluate_answer("It uses polymorphism heavily"))
