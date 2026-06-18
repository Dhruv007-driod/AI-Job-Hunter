from backend.job_loader import load_jobs

def match_jobs(user_skills):

    JOBS = load_jobs()
    results = []

    user_skills = set(user_skills)

    for job in JOBS:

        job_skills = set(job["skills"])

        matched = user_skills.intersection(job_skills)

        score = (
            len(matched)
            / len(job_skills)
        ) * 100

        results.append({
            "job": job["title"],
            "score": round(score, 2),
            "matched_skills": list(matched),
            "missing_skills": list(
                job_skills - user_skills)
    
    })

    return sorted(
        results,
        key=lambda x: x["score"],
        reverse=True
    )