# 📄  MCQ Generator

A Streamlit web application that uses AI to check whether a resume matches a job description, and generates unique fill-in-the-blank multiple-choice questions (MCQs) based on that job description. Designed to help job seekers, hiring managers, and interview trainers evaluate alignment and comprehension interactively.

---

## 🚀 Features

- ✅ **Resume Matching**: Uses LLM (LLaMA 3) to check if the resume matches the job description.
- 🧠 **AI-Powered Question Generation**: Automatically generates 5 unique fill-in-the-blank MCQs from the job description.
- ✍️ **Interactive Quiz Interface**: Lets users answer all questions and receive final evaluation at once.
- 🧹 **Smart Cleanup**: Removes boilerplate phrasing like "Here is a unique..." from question text.
- 🔁 **Repeat Prevention**: Ensures no duplicate MCQs appear in the same session.

---

## 🛠️ Built With

- [Streamlit](https://streamlit.io) — App framework for Python
- [LangChain](https://www.langchain.com) — LLM orchestration library
- [LLaMA 3 via Groq API](https://groq.com/) — Lightning-fast inference of open-source large language models
- [PyMuPDF](https://github.com/pymupdf/PyMuPDF) — PDF reading
- [python-docx](https://python-docx.readthedocs.io/en/latest/) — DOCX file parsing
- [dotenv](https://pypi.org/project/python-dotenv/) — API key management

---

## 📦 Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/jd-resume-mcq-generator.git
   cd jd-resume-mcq-generator 

2. **Install Dependencies**

```bash
pip install -r requirements.txt
```
3. **Create .env File**

In the root folder, add your Groq API key to a .env file:

```
GROQ_API_KEY=your_groq_api_key_here
```

4. **Run the App**

```
streamlit run app.py
```
## 🖼️ Example Use Case

1. Paste a job description in the text area.  
2. Upload a resume in **PDF**, **DOCX**, or **TXT** format.  
3. If matched, answer the 5 auto-generated fill-in-the-blank questions.  
4. Submit all answers at once and receive a score breakdown.

---

## 🧠 Ideal For

- 💼 Job seekers preparing for interviews  
- 🧑‍💻 Hiring managers reviewing candidates  
- 🎓 Trainers creating competency quizzes  
- 🧪 Learning and development teams building ML assessments

---

## 🤝 Contributing

PRs and feature requests welcome! Want to add multiple-choice options, export to PDF, or integrate scoring into a database?  
Open an issue or submit a pull request!

---

## 🛡️ License

MIT License — feel free to use, modify, and share.

---

## 🙌 Acknowledgments

Built with ❤️ using [LangChain](https://www.langchain.com), [Streamlit](https://streamlit.io), and [Groq](https://groq.com).
