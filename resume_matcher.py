import streamlit as st
import fitz  # PyMuPDF
from sentence_transformers import SentenceTransformer, util
import tempfile
import os

# 🎯 Page configuration
st.set_page_config(page_title="Resume Matcher", layout="centered")
st.title("🤖 Resume Matcher using NLP")

# ✅ Load Sentence-BERT model
model = SentenceTransformer("all-MiniLM-L6-v2")

# 🧾 Function to extract text from uploaded files
def extract_text(file):
    text = ""
    
    if file.name.endswith(".pdf"):
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(file.read())
            tmp_path = tmp.name

        doc = fitz.open(tmp_path)
        for page in doc:
            text += page.get_text()
        doc.close()
        os.remove(tmp_path)

    elif file.name.endswith(".txt"):
        file.seek(0)
        text = file.read().decode("utf-8", errors="ignore")

    return text.strip()

# 📋 Job Description Input
jd_text = st.text_area("📋 Paste the Job Description", height=200)

# 📄 Resume Upload Input
uploaded_resumes = st.file_uploader(
    "📁 Upload Resumes (.pdf or .txt)", type=["pdf", "txt"], accept_multiple_files=True
)

# 🔍 Match Button
if st.button("🔍 Match Resumes", key="match_button"):
    if not jd_text:
        st.warning("⚠️ Please enter a job description.")
    elif not uploaded_resumes:
        st.warning("⚠️ Please upload at least one resume.")
    else:
        with st.spinner("Matching resumes..."):
            jd_embedding = model.encode(jd_text, convert_to_tensor=True)
            results = []

            for resume in uploaded_resumes:
                resume_text = extract_text(resume)
                resume_embedding = model.encode(resume_text, convert_to_tensor=True)
                score = util.cos_sim(jd_embedding, resume_embedding)[0][0].item()
                results.append({
                    "filename": resume.name,
                    "score": round(score * 100, 2)
                })

            results.sort(key=lambda x: x["score"], reverse=True)

        # ✅ Display Results
        st.success("✅ Matching complete!")
        for res in results:
            st.write(f"📄 **{res['filename']}** — Match Score: `{res['score']}%`")
