def calculate_score(
    skills,
    projects,
    education,
    experience
):

    score = 0

    score += min(len(skills) * 5, 40)

    score += min(len(projects) * 10, 20)

    score += min(len(education) * 10, 10)

    score += min(len(experience) * 15, 30)

    return min(score, 100)