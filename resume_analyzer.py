import re

resume_text = """
I have experience in Python, SQL, and Excel.
Worked on data analysis and automation projects.
"""

skills = ["Python", "SQL", "Excel", "Power BI", "Machine Learning", "AI"]

matched_skills = []
missing_skills = []

for skill in skills:
    if re.search(skill, resume_text, re.IGNORECASE):
        matched_skills.append(skill)
    else:
        missing_skills.append(skill)

score = int((len(matched_skills) / len(skills)) * 100)

print("Resume Score:", score, "%")
print("Matched Skills:", matched_skills)
print("Missing Skills:", missing_skills)

if score < 60:
    print("Suggestion: Add more relevant skills.")
else:
    print("Good profile!")
