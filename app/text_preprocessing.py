import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

for resource in ["punkt", "punkt_tab", "stopwords"]:
    try:
        nltk.data.find(f"tokenizers/{resource}" if "punkt" in resource else f"corpora/{resource}")
    except LookupError:
        nltk.download(resource)

stop_words = set(stopwords.words("english"))

def preprocess_text(text):
    text = re.sub(r"[^a-zA-Z]", " ", text).lower()

    words = word_tokenize(text)

    filtered_words = [w for w in words if w not in stop_words and len(w) > 1]

    return " ".join(filtered_words)
