import sqlite3


def recommend_courses(missing_skills):

    conn = sqlite3.connect("skills.db")
    cursor = conn.cursor()

    recommendations = []

    for skill in missing_skills:

        cursor.execute("""
            SELECT skill_name, category, demand_level, recommended_course
            FROM skills
            WHERE LOWER(skill_name) = LOWER(?)
        """, (skill,))

        result = cursor.fetchone()

        if result:
            recommendations.append({
                "skill": result[0],
                "category": result[1],
                "demand_level": result[2],
                "recommended_course": result[3]
            })

        else:
            recommendations.append({
                "skill": skill,
                "category": "Unknown",
                "demand_level": "Unknown",
                "recommended_course": "Recommended Training for " + skill
            })

    conn.close()

    return recommendations


# ================= TEST =================

missing_skills = [
    "React",
    "Machine Learning"
]

courses = recommend_courses(missing_skills)

print("===== COURSE RECOMMENDATIONS =====")

for course in courses:
    print(
        course["skill"],
        "→",
        course["recommended_course"]
    )