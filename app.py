import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_core.output_parsers import StrOutputParser
import fitz  # PyMuPDF
import docx

# Load API Key
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize LLM
llm = ChatGroq(api_key=groq_api_key, model_name="llama3-8b-8192")

# ========= File Readers ========= #
def read_pdf(file):
    text = ""
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

def read_docx(file):
    doc = docx.Document(file)
    return "\n".join([p.text for p in doc.paragraphs])

def read_file(file):
    if file.name.endswith(".pdf"):
        return read_pdf(file)
    elif file.name.endswith(".docx"):
        return read_docx(file)
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    else:
        return "Unsupported file type."

# ========= Streamlit App ========= #
st.title("📄 JD & Resume MCQ Generator")
st.write("Paste Job Description and upload Resume to check match & generate MCQs.")

jd_text = st.text_area("Paste Job Description Here")
resume_file = st.file_uploader("Upload Resume (PDF/DOCX/TXT)", type=["pdf", "docx", "txt"])

# Initialize session state
if "mcqs" not in st.session_state:
    st.session_state.mcqs = []
if "answers" not in st.session_state:
    st.session_state.answers = []
if "generated" not in st.session_state:
    st.session_state.generated = False

if jd_text.strip() and resume_file:
    resume_text = read_file(resume_file)

    with st.spinner("🔍 Checking resume against job description..."):
        match_prompt = PromptTemplate.from_template(
            "Check if the following resume matches this job description. Reply with only 'YES' or 'NO'.\n\nJob Description:\n{jd}\n\nResume:\n{resume}"
        )
        chain = match_prompt | llm | StrOutputParser()
        match_result = chain.invoke({"jd": jd_text, "resume": resume_text}).strip().upper()

    if "YES" in match_result:
        st.success("✅ Resume matches the Job Description!")

        # Generate MCQs once
        if not st.session_state.generated:
            NUM_MCQS = 5
            generated_questions = set()
            attempts = 0
            with st.spinner("🧠 Generating MCQs..."):
                while len(st.session_state.mcqs) < NUM_MCQS and attempts < NUM_MCQS * 3:
                    mcq_prompt = PromptTemplate.from_template(
                        "From the job description below, create ONE unique fill-in-the-blank MCQ question. Also provide the correct answer.\n\nJob Description:\n{jd}\n\nFormat:\nQuestion: <your question>\nAnswer: <correct answer>"
                    )
                    mcq_chain = mcq_prompt | llm | StrOutputParser()
                    mcq_raw = mcq_chain.invoke({"jd": jd_text})
                    attempts += 1

                    try:
                        question = mcq_raw.split("Answer:")[0].replace("Question:", "").strip()
                        answer = mcq_raw.split("Answer:")[1].strip()

                        if question.lower() not in generated_questions:
                            generated_questions.add(question.lower())
                            st.session_state.mcqs.append(question)
                            st.session_state.answers.append(answer)
                    except:
                        continue

            st.session_state.generated = True

        st.subheader("📝 Answer the following questions:")
        user_inputs = []
        for i, q in enumerate(st.session_state.mcqs):
            user_input = st.text_input(f"{i+1}. {q}", key=f"input_{i}")
            user_inputs.append(user_input)

        if st.button("Submit All"):
            st.subheader("🧪 Evaluation Results:")
            score = 0
            total = len(st.session_state.answers)

            for i, user_input in enumerate(user_inputs):
                correct = st.session_state.answers[i]
                if user_input.lower().strip() == correct.lower():
                    st.markdown(f"✅ **Q{i+1} Correct!**")
                    score += 1
                else:
                    st.markdown(f"❌ **Q{i+1} Incorrect** — Correct answer: `{correct}`")

            st.success(f"🎯 Final Score: {score} / {total}")
    else:
        st.warning("❌ Resume does not match the Job Description. MCQs not generated.")






