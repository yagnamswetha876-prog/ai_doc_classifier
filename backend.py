# backend.py

import PyPDF2
import docx2txt
import re
from collections import Counter

# -------------------------
# TEXT EXTRACTION
# -------------------------
def extract_text(file):
    text = ""

    if file.type == "application/pdf":
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() or ""

    elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        text = docx2txt.process(file)

    elif file.type == "text/plain":
        text = str(file.read(), "utf-8")

    return text


# -------------------------
# CLASSIFICATION (SMART SCORING)
# -------------------------
def classify_document(text):
    text = text.lower()

    categories = {
        "Business & Finance": ["stock", "market", "finance", "money", "investment", "bank", "economy", "profit", "loss"],
        "Education / Notes": ["study", "notes", "education", "exam", "lecture", "subject", "theory", "chapter", "formula", "concept", "probability", "math"],
        "News Article": ["breaking", "news", "report", "headline", "journal", "update"],
        "Social Media Content": ["instagram", "post", "tweet", "social", "facebook", "comment", "like"],
        "Story": ["once upon", "king", "queen", "forest", "adventure", "fairy", "magic", "story"]
    }

    scores = {category: 0 for category in categories}

    for category, keywords in categories.items():
        for word in keywords:
            if word in text:
                scores[category] += 1

    best_category = max(scores, key=scores.get)

    if scores[best_category] == 0:
        return "Story", scores

    return best_category, scores


# -------------------------
# SUMMARIZATION (SMART)
# -------------------------
def summarize_text(text):
    text = text.replace("\n", " ")

    sentences = re.split(r'(?<=[.!?]) +', text)

    if len(sentences) <= 2:
        return text

    sentences = [s for s in sentences if len(s.split()) > 5]

    words = re.findall(r'\w+', text.lower())

    stopwords = set([
        "the","is","in","and","to","of","a","for","on","with",
        "as","by","at","an","be","this","that","it","from"
    ])

    filtered_words = [w for w in words if w not in stopwords]
    word_freq = Counter(filtered_words)

    sentence_scores = {}

    for sentence in sentences:
        for word in sentence.lower().split():
            if word in word_freq:
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + word_freq[word]

    for sentence in sentence_scores:
        sentence_scores[sentence] /= len(sentence.split())

    top_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:2]

    final_summary = [s for s in sentences if s in top_sentences]

    return " ".join(final_summary)