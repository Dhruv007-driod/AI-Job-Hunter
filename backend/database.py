import sqlite3

def create_table():

    conn = sqlite3.connect("jobhunter.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS candidates (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT,
        phone TEXT,
        skills TEXT,
        projects TEXT,
        education TEXT,
        experience TEXT
    )
    """)

    conn.commit()
    conn.close()

def get_latest_candidate():

    conn = sqlite3.connect("jobhunter.db")

    cursor = conn.cursor()

    cursor.execute("""
    SELECT skills
    FROM candidates
    ORDER BY id DESC
    LIMIT 1
    """)

    row = cursor.fetchone()

    conn.close()

    return row


def save_candidate(
    email,
    phone,
    skills,
    projects,
    education,
    experience
):

    conn = sqlite3.connect("jobhunter.db")

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO candidates (
        email,
        phone,
        skills,
        projects,
        education,
        experience
    )
    VALUES (?, ?, ?, ?, ?, ?)
    """,
    (
        email,
        phone,
        str(skills),
        str(projects),
        str(education),
        str(experience)
    ))

    conn.commit()
    conn.close()