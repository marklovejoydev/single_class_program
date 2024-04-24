class GrammarStats:
    def __init__(self):
        self.total_count = 0
        self.correct_count = 0

    def check(self, text):
        if text[0].isupper() and text[-1] in".?!":
            self.total_count += 1
            self.correct_count += 1
            return True
        else:
            self.total_count += 1
            return False

    def percentage_good(self):
        if self.total_count == 0:
            return "No checks performed yet"
        else:
            percentage = int((self.correct_count / self.total_count) * 100)
            return f"{percentage}%"