import random

class ProblemBank:
    def __init__(self):
        self.data = {
            "1.1": ["1b", "1c", "3b", "3c", "4", "5a", "5d", "7", "9", "14", "18", "19", "21"],
            "1.2": ["1", "4", "7", "10", "13", "16", "17", "26", "29", "36", "42", "49", "50"],
            "1.3": ["1", "3", "5", "7", "10", "12", "13", "18", "19", "20", "22", "23", "24", "28", "32", "36", "37"],
            "2.1": ["1", "3", "4", "11", "13", "15", "17", "21", "29", "31"],
            "2.2": ["1", "3", "5", "7", "14", "23", "26", "35", "37", "42", "48"],
            "2.3": ["1", "3", "8", "9", "11", "15", "24", "26"],
            "3.1": ["2", "4", "9", "14", "16", "18", "19", "21", "39a", "39c"],
            "3.2": ["2", "4", "7", "9", "11", "13", "15", "23", "37", "40", "42"],
            "3.3": ["2", "4", "11", "13a", "13b", "23", "27", "32", "34", "42", "52", "53"],
            "3.5": ["1", "2", "6", "7", "12", "18", "22", "27", "40", "46", "51"],
            "3.6": ["2", "6", "10", "14", "17", "22", "31", "37"],
            "4.1": ["2", "6", "8", "11", "20", "21", "24", "25"],
            "4.2": ["2", "4", "7", "14", "16", "23", "29", "33", "39", "46", "48", "49", "64"],
            "4.3": ["4", "8", "15"],
            "4.4": ["2", "4", "6", "11", "21", "27", "36"],
            "5.1": ["2", "4", "8", "10", "14", "18"],
            "5.2": ["2", "4", "8", "10", "12", "16", "20"],
            "5.3": ["3", "6", "8", "9", "15"]
        }

        self.current_pool = []
        self.completed = []
        self.needs_review = []
        self.current_problem = None

    def load_exam(self, exam_name):
        exam_sections = {
            "Exam 1": ["1.1", "1.2", "1.3", "2.1"],
            "Exam 2": ["2.2", "2.3", "3.1", "3.2", "3.3"],
            "Exam 3": ["3.5", "3.6", "4.1", "4.2", "4.3", "4.4", "5.1", "5.2", "5.3"],
            "Final": list(self.data.keys())
        }

        self.current_pool = []
        self.completed = []
        self.needs_review = []

        for section in exam_sections[exam_name]:
            for problem in self.data[section]:
                self.current_pool.append((section, problem))

        random.shuffle(self.current_pool)

    def get_next_problem(self):
        if not self.current_pool:
            self.current_problem = None
            return None

        self.current_problem = self.current_pool.pop()
        return self.current_problem

    def mark_solved(self):
        if self.current_problem:
            self.completed.append(self.current_problem)

    def mark_needs_review(self):
        if self.current_problem:
            self.needs_review.append(self.current_problem)

    def skip_problem(self):
        if self.current_problem:
            self.current_pool.insert(0, self.current_problem)

    def problems_left(self):
        return len(self.current_pool)

    def total_completed(self):
        return len(self.completed) + len(self.needs_review)