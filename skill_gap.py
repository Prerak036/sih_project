from skill_normalizer import normalize_skill


def calculate_skill_gap(required_skills, user_skills):

    # Normalize required skills
    required = set(
        normalize_skill(skill)
        for skill in required_skills
    )

    # Normalize user skills
    user = set(
        normalize_skill(skill)
        for skill in user_skills
    )

    # Find matched and missing skills
    matched_skills = required & user
    missing_skills = required - user

    # Calculate match percentage
    if len(required) > 0:
        match_percentage = (
            len(matched_skills) / len(required)
        ) * 100
    else:
        match_percentage = 0

    return matched_skills, missing_skills, match_percentage


# ================= TEST =================

required_skills = [
    "Python",
    "Machine Learning",
    "SQL",
    "React"
]

user_skills = [
    "Python",
    "SQL",
    "ML",
    "ReactJS"
]


matched, missing, percentage = calculate_skill_gap(
    required_skills,
    user_skills
)


print("===== SKILL GAP ANALYSIS =====")

print("\nMatched Skills:")
for skill in matched:
    print("✓", skill)

print("\nMissing Skills:")
for skill in missing:
    print("✗", skill)

print("\nSkill Match:", round(percentage, 2), "%")