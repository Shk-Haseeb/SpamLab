import math
import re

class SpamFilter:
    def __init__(self, spam_file, ham_file):
        self.spam_counts = self._load_word_counts(spam_file)
        self.ham_counts = self._load_word_counts(ham_file)

        self.vocabulary = set(self.spam_counts.keys()).union(self.ham_counts.keys())
        self.spam_total = sum(self.spam_counts.values())
        self.ham_total = sum(self.ham_counts.values())
        self.vocab_size = len(self.vocabulary)

        # Prior probabilities (assuming equal distribution)
        self.spam_prior = 0.5
        self.ham_prior = 0.5

    def _load_word_counts(self, filepath):
        word_map = {}
        with open(filepath, 'r', encoding='utf-8') as file:
            for line in file:
                parts = re.split(r'\s+', line.strip())
                if len(parts) >= 2:
                    count = int(parts[0])
                    word = parts[1]
                    word_map[word] = count
        return word_map

    def _tokenize(self, text):
        return re.findall(r'\b\w+\b', text.lower())

    def _word_prob(self, word, counts, total):
        return (counts.get(word, 0) + 1) / (total + self.vocab_size)

    def classify(self, words):
        log_spam = math.log(self.spam_prior)
        log_ham = math.log(self.ham_prior)

        for word in words:
            log_spam += math.log(self._word_prob(word, self.spam_counts, self.spam_total))
            log_ham += math.log(self._word_prob(word, self.ham_counts, self.ham_total))

        return "SPAM" if log_spam > log_ham else "HAM"

    def classify_from_file(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        words = self._tokenize(content)
        return self.classify(words)

    def classify_from_input(self):
        message = input("Enter a message to classify: ")
        words = self._tokenize(message)
        return self.classify(words)
