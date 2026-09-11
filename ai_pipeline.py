from resume_parser import extract_text_from_pdf, detect_skills
from skill_normalizer import normalize_skill
from skill_gap import calculate_skill_gap
from recommendation import recommend_courses


def run_ai_pipeline(pdf_path, required_skills):

    # 1. Resume se text extract
    text = extract_text_from_pdf(pdf_path)

    # 2. Resume se skills detect
    detected_skills = detect_skills(text)

    # 3. Skills normalize
    normalized_skills = []

    for skill in detected_skills:
        skill = normalize_skill(skill)

        if skill not in normalized_skills:
            normalized_skills.append(skill)

    # 4. Skill Gap Analysis
    matched_skills, missing_skills, match_percentage = calculate_skill_gap(
        required_skills,
        normalized_skills
    )

    # 5. Course Recommendations
    recommendations = recommend_courses(missing_skills)

    # Final Result
    result = {
        "detected_skills": normalized_skills,
        "matched_skills": list(matched_skills),
        "missing_skills": list(missing_skills),
        "match_percentage": match_percentage,
        "recommendations": recommendations
    }

    return result


# ================= TEST =================

if __name__ == "__main__":

    pdf_path = r"C:\Users\muska\Downloads\Aryan_Rathore_Resume_Final_Updated.pdf"

    required_skills = [
        "Python",
        "JavaScript",
        "React",
        "Node.js",
        "MongoDB",
        "SQL",
        "Machine Learning"
    ]

    result = run_ai_pipeline(pdf_path, required_skills)

    print("\n===== AI PIPELINE RESULT =====")

    print("\nDetected Skills:")
    for skill in result["detected_skills"]:
        print("✓", skill)

    print("\nMatched Skills:")
    for skill in result["matched_skills"]:
        print("✓", skill)

    print("\nMissing Skills:")
    for skill in result["missing_skills"]:
        print("✗", skill)

    print("\nSkill Match:", result["match_percentage"], "%")

    print("\nCourse Recommendations:")
    for recommendation in result["recommendations"]:
        print("→", recommendation)
        