import spacy

nlp = spacy.load("en_core_web_sm")

COMMON_SKILLS = ["python", "java", "sql", "flask", "machine learning"]

def analyze_resume(text):
    doc = nlp(text.lower())

    skills_found = []
    for skill in COMMON_SKILLS:
        if skill in text.lower():
            skills_found.append(skill)

    sections = {
        "education": "education" in text.lower(),
        "experience": "experience" in text.lower(),
        "skills": "skills" in text.lower(),
        "projects": "projects" in text.lower()
    }

    return {
        "skills": skills_found,
        "sections": sections,
        "text_length": len(text)
    }