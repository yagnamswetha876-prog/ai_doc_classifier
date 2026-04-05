# frontend.py

import streamlit as st
from backend import extract_text, classify_document, summarize_text

def run_frontend():
    st.set_page_config(page_title="AI Document Classifier", layout="centered")

    st.title("📄 AI Document Classifier & Summarizer")
    st.markdown("Upload a document to classify and summarize it.")

    # -------------------------
    # FILE UPLOAD
    # -------------------------
    uploaded_file = st.file_uploader(
        "📂 Upload your document (PDF, DOCX, TXT)",
        type=["pdf", "docx", "txt"]
    )

    if uploaded_file is not None:

        # Extract text
        text = extract_text(uploaded_file)

        if text.strip() == "":
            st.warning("⚠️ No text found in the document")
        else:
            st.success("✅ File uploaded successfully!")

            # -------------------------
            # ANALYZE BUTTON
            # -------------------------
            if st.button("🔍 Analyze Document"):

                category, scores = classify_document(text)
                summary = summarize_text(text)

                # -------------------------
                # CONFIDENCE CALCULATION
                # -------------------------
                total_score = sum(scores.values())
                confidence = (scores[category] / total_score * 100) if total_score != 0 else 0

                # -------------------------
                # OUTPUT
                # -------------------------
                st.subheader("📌 Category")
                st.success(f"{category} ({confidence:.2f}% confidence)")

                st.subheader("📝 Summary")
                st.info(summary)

                # -------------------------
                # DOCUMENT INFO
                # -------------------------
                st.subheader("📊 Document Info")
                st.write(f"📄 Words: {len(text.split())}")
                st.write(f"🔤 Characters: {len(text)}")

                # -------------------------
                # SCORE DETAILS (OPTIONAL)
                # -------------------------
                with st.expander("🔍 Show Detailed Scores"):
                    st.write(scores)

                # -------------------------
                # DOWNLOAD SUMMARY
                # -------------------------
                st.download_button(
                    label="📥 Download Summary",
                    data=summary,
                    file_name="summary.txt",
                    mime="text/plain"
                )