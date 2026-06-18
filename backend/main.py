from fastapi import FastAPI, UploadFile, File
import shutil
from backend.database import get_latest_candidate
import ast
from backend.scorer import calculate_score
from backend.matcher import match_jobs
from backend.database import create_table, save_candidate
from backend.parser import *
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
create_table()

@app.get("/")
def home():
    return {"message": "AI Job Hunter API is running"}

@app.post("/upload")
async def upload_resume(file: UploadFile = File(...)):

    path = f"uploads/{file.filename}"

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text(path)

    
    email = extract_email(text)
    phone = extract_phone(text)
    skills = extract_skills(text)
    from backend.matcher import match_jobs
    recommended_jobs = match_jobs(skills)
    projects = extract_projects(text)
    education = extract_education(text)
    experience = extract_experience(text)

    resume_score = calculate_score(
    skills,
    projects,
    education,
    experience
)
    save_candidate(
            email,
            phone,
            skills,
            projects,
            education,
            experience
        )
    return {
    "email": email,
    "phone": phone,
    "skills": skills,
    "projects": projects,
    "education": education,
    "experience": experience,
    "resume_score": resume_score,
    "recommended_jobs": recommended_jobs
}
@app.get("/jobs")
def get_jobs():

    row = get_latest_candidate()

    skills = ast.literal_eval(row[0])

    return match_jobs(skills)

for route in app.routes:
    print(route.path, route.methods)

