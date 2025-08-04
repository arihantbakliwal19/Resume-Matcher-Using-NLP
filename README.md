# 🤖 Resume Matcher using NLP and Streamlit

This project is a smart resume matching application that uses Natural Language Processing (NLP) to semantically compare resumes against a job description. It leverages pre-trained Sentence-BERT models to generate similarity scores, helping recruiters or job platforms rank candidates by relevance.

---

## 🚀 Features

- Upload one or more resumes in `.pdf` or `.txt` format
- Paste a job description into the UI
- Get a match score (%) for each resume
- Uses Sentence-BERT embeddings and cosine similarity
- Interactive web interface built with Streamlit

---

## 🛠️ Technologies Used

- **Python**
- **Streamlit** – for building the web app
- **Sentence-Transformers** – to generate embeddings (`all-MiniLM-L6-v2`)
- **PyMuPDF** – for PDF parsing
- **NumPy** – for similarity calculations

---

## 💻 How It Works

1. Job description and resumes are embedded using Sentence-BERT
2. Cosine similarity compares the job description with each resume
3. The app ranks resumes by match score and displays results


---
Example :
We are hiring a Data Analyst with strong skills in SQL, Power BI, and Excel.
Experience in dashboards, KPI tracking, and statistical reporting preferred.
You can copy this into the "Paste the Job Description" box on the Streamlit interface.

📄 Sample Resumes Used :
Resume File	Highlights in the Content	Expected Match
resume_data_analyst.pdf	SQL, Excel, Power BI, Dashboards, Statistics	✅ High (80–90%)
resume_ml_engineer.pdf	Python, TensorFlow, Deep Learning, M.Tech	❌ Low (40–60%)
resume_digital_marketer.pdf	SEO, Google Ads, Content Marketing	❌ Very Low (20–30%)

Output :

📄 resume_data_analyst.pdf — Match Score: 87.3%
📄 resume_ml_engineer.pdf — Match Score: 50.4%
📄 resume_digital_marketer.pdf — Match Score: 26.8%


📬 Author
Arihant Bakliwal
GitHub Profile










Ask ChatGPT

