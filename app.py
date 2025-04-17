import textwrap

def analyze_cv_text(text):
    pros = []
    cons = []

    # --- PROS ---
    if "Python" in text or "Java" in text:
        pros.append("Strong programming skills.")
    if "SQL" in text or "MySQL" in text:
        pros.append("Database knowledge.")
    if "HTML" in text or "CSS" in text:
        pros.append("Web development skills.")
    if "Git" in text:
        pros.append("Familiar with version control (Git).")
    if "project" in text.lower():
        pros.append("Hands-on project experience.")
    if "problem-solving" in text.lower():
        pros.append("Good problem-solving ability.")
    if any(skill in text.lower() for skill in ["team", "collaboration", "communication"]):
        pros.append("Strong soft skills (teamwork, communication).")

    # --- CONS ---
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

def display_pros_and_cons(pros, cons):
    print("\n" + "="*50)
    print("PROS:")
    print("="*50)
    if pros:
        for p in pros:
            print(f"✅ {p}")
    else:
        print("⚠️ No strong points detected.")
    
    print("\n" + "="*50)
    print("CONS:")
    print("="*50)
    if cons:
        for c in cons:
            print(f"❌ {c}")
    else:
        print("🎉 No major weaknesses found!")

# Input resume text
resume_text = input("Paste resume-like text below:\n\n")

# Analyze and show results
pros_list, cons_list = analyze_cv_text(resume_text)
display_pros_and_cons(pros_list, cons_list)
