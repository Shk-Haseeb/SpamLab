import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")

try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords")

stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    text = re.sub(r"[^a-zA-Z]", " ", text)

    words = word_tokenize(text.lower())

    filtered_words = [w for w in words if w not in stop_words and len(w) > 1]

    return " ".join(filtered_words)
