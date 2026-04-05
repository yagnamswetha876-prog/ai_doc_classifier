# 📄 AI Document Classifier & Summarizer

A lightweight AI-powered web app that classifies documents into categories and generates a short summary using text analysis.

---

## 🔹 Features

* Upload documents (PDF, DOCX, TXT)
* Automatic text extraction
* AI-based document classification
* Generates **2-line meaningful summary**
* Displays word & character count
* Shows classification confidence
* Download summary as text file

---

## 🔹 Categories Supported

* 📖 Story
* 📚 Education / Notes
* 💼 Business & Finance
* 📱 Social Media Content
* 📰 News Article

---

## 🔹 Tech Stack

* **Frontend:** Streamlit
* **Backend:** Python
* **Text Processing:** PyPDF2, docx2txt
* **Logic:** Scoring-based NLP classification
* **Visualization (optional):** Streamlit UI components

---

## 🔹 Installation

```bash
git clone <repo-link>
cd ai_doc_classifier
python -m venv myenv
myenv\Scripts\activate  # Windows
pip install -r requirements.txt
```

---

## 🔹 Running

```bash
streamlit run main.py
```

Open the link shown in terminal (`http://localhost:8501`).

---

## 🔹 Usage

1. Upload a document (PDF / DOCX / TXT)
2. Click **Analyze Document**
3. View:

   * 📌 Category of document
   * 📝 2-line summary
   * 📊 Document statistics
4. Download summary if needed

---

## 🔹 Code Structure

```text
ai_doc_classifier/
├── backend.py
├── frontend.py
├── main.py
├── requirements.txt
├── README.md
```

---

## 🔹 How It Works

* Extracts text from uploaded files
* Uses a scoring-based algorithm to classify content
* Identifies important sentences for summarization
* Displays results with confidence score

---

## 🔹 Future Improvements

* Integration with advanced AI models (NLP / Transformers)
* Multi-document upload support
* Language translation
* Enhanced UI and visual analytics

---

## 🎓 Conclusion

This project demonstrates a simple and efficient approach to **AI-based document classification and summarization**, suitable for real-world applications and easy deployment.

---
