# 📨 Simple Naive Bayes Email Classifier

A lightweight email spam filter built from scratch in Python using the **Naive Bayes algorithm**. No ML libraries, just word counts, probabilities, and math.

---

## ⚙️ What It Does

- Classifies text messages as **SPAM** or **HAM**.
- Uses word frequency data with **Laplace smoothing**.
- Applies log probabilities to avoid underflow.
- Decides based on which score (spam or ham) is higher.

---

## 🔍 `SpamFilter` Class

- `spam_counts` / `ham_counts`: Word frequencies from training data.
- `prior_spam` / `prior_ham`: Set to 0.5 by default.
- Tokenizes input, calculates conditional probabilities, and logs them.
- Outputs classification based on log score comparison.
