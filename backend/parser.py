import fitz
from backend.skills import SKILLS
import re

def extract_text(pdf_path):
    doc = fitz.open(pdf_path)

    text = ""

    for page in doc:
        text += page.get_text()

    return text


def extract_email(text):
    match = re.search(
        r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',
        text
    )

    return match.group() if match else None


def extract_phone(text):
    match = re.search(
        r'\+?\d[\d\s-]{8,}',
        text
    )

    return match.group() if match else None
def extract_skills(text):

    found_skills = []

    text = text.lower()

    for skill in SKILLS:

        if skill.lower() in text:
            found_skills.append(skill)

    return list(set(found_skills))
def extract_projects(text):

    projects = []

    patterns = [
        r'Projects(.*?)(Education|Experience|Skills|$)'
    ]

    for pattern in patterns:

        match = re.search(
            pattern,
            text,
            re.DOTALL | re.IGNORECASE
        )

        if match:

            project_section = match.group(1)

            lines = project_section.split('\n')

            for line in lines:

                line = line.strip()

                if len(line) > 3 and len(line) < 60:
                    projects.append(line)

    return list(set(projects))
def extract_education(text):

    education_keywords = [
        "b.tech",
        "b.e",
        "bachelor",
        "m.tech",
        "m.e",
        "master",
        "phd",
        "bs"
    ]

    lines = text.split("\n")

    education = []

    for line in lines:

        line_lower = line.lower()

        for keyword in education_keywords:

            if keyword in line_lower:
                education.append(line.strip())

    return list(set(education))
def extract_experience(text):

    experience_keywords = [
        "intern",
        "internship",
        "software engineer",
        "developer",
        "research assistant",
        "teaching assistant",
        "freelance",
        "work experience"
    ]

    lines = text.split("\n")

    experience = []

    for line in lines:

        line_lower = line.lower()

        for keyword in experience_keywords:

            if keyword in line_lower:
                experience.append(line.strip())

    return list(set(experience))