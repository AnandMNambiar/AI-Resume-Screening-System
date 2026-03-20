import os
import pdfplumber
import pandas as pd

# Required skills for ML Engineer
required_skills = [
    "python","machine learning","deep learning","tensorflow","pytorch",
    "sql","pandas","numpy","data preprocessing","feature engineering",
    "model evaluation","scikit-learn","aws","docker","spark"
]

# Read job description
with open("job_description.txt","r",encoding="utf-8") as f:
    jd = f.read().lower()

results = []

resume_folder = "resumes"

for file in os.listdir(resume_folder):

    if file.endswith(".pdf"):

        path = os.path.join(resume_folder,file)

        text = ""

        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text.lower()

        matched = []
        missing = []

        for skill in required_skills:
            if skill in text:
                matched.append(skill)
            else:
                missing.append(skill)

        score = int((len(matched)/len(required_skills))*100)

        if score >= 75:
            recommendation = "Strong Fit"
        elif score >= 50:
            recommendation = "Moderate Fit"
        else:
            recommendation = "Not Fit"

        results.append({
            "Candidate":file,
            "Score":score,
            "Strengths":", ".join(matched[:3]),
            "Gaps":", ".join(missing[:3]),
            "Recommendation":recommendation
        })

df = pd.DataFrame(results)

df = df.sort_values(by="Score",ascending=False)

df.to_csv("output.csv",index=False)

print("Screening Complete. Check output.csv")