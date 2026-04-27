def calculate_ats_score(data):
    score = 0

    # Skills score
    score += len(data["skills"]) * 10

    # Sections score
    score += sum(data["sections"].values()) * 15

    # Length score
    if data["text_length"] > 1000:
        score += 20

    return min(score, 100)