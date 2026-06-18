import pandas as pd

def load_jobs():

    df = pd.read_csv("data/jobs.csv")

    jobs = []

    for _, row in df.iterrows():

        jobs.append({
            "title": row["title"],
            "skills": row["skills"].split(",")
        })

    return jobs