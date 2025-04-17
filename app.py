import streamlit as st

def analyze_cv_text(text):
    pros = []
    cons = []

    # PROS
    if "Python" in text or "Java" in text:
        pros.append("Strong programming skills.")
    if "SQL" in text or "MySQL" in text:
        pros.append("Database knowledge.")
    if "HTML" in text or "CSS" in text:
        pros.append("Web development skills.")
    if "Git" in text:
        pros.append("Familiar with version control.")
    if "project" in text.lower():
        pros.append("Hands-on project experience.")
    if "problem-solving" in text.lower():
        pros.append("Good problem-solving ability.")
    if any(skill in text.lower() for skill in ["team", "collaboration", "communication"]):
        pros.append("Strong soft skills.")

    # CONS
    if "JavaScript" not in text:
        cons.append("No mention of JavaScript.")
    if "React" not in text and "frontend framework" not in text:
        cons.append("Frontend framework not mentioned.")
    if "internship" not in text.lower() and "experience" not in text.lower():
        cons.append("No work or internship experience mentioned.")
    if "cloud" not in text.lower():
        cons.append("Cloud technologies not included.")
    if "API" not in text:
        cons.append("No API-related work mentioned.")

    return pros, cons

st.set_page_config(page_title="Resume Pros & Cons Analyzer", layout="centered")

st.title("📄 Resume Pros & Cons Analyzer")
st.markdown("Paste **resume-like text** below to see an instant analysis.")

resume_text = st.text_area("Paste resume-like text below:", height=250)

if st.button("Analyze"):
    if resume_text.strip():
        pros, cons = analyze_cv_text(resume_text)

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("✅ Pros")
            if pros:
                for item in pros:
                    st.markdown(f"- {item}")
            else:
                st.info("No strong points detected.")

        with col2:
            st.subheader("❌ Cons")
            if cons:
                for item in cons:
                    st.markdown(f"- {item}")
            else:
                st.success("No major weaknesses found!")
    else:
        st.warning("Please enter some resume text.")
