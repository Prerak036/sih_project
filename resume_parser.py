import sys
import sqlite3
import re
from pypdf import PdfReader
from skill_normalizer import normalize_skill


def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def detect_skills(text):
    conn = sqlite3.connect("skills.db")
    cursor = conn.cursor()

    cursor.execute("SELECT skill_name FROM skills")
    database_skills = cursor.fetchall()

    detected_skills = []

    text_lower = text.lower()

    for row in database_skills:
        skill = row[0]

        # Special handling for skills containing symbols
        escaped_skill = re.escape(skill.lower())

        # Normal word matching
        if re.search(r"(?<!\w)" + escaped_skill + r"(?!\w)", text_lower):

            normalized_skill = normalize_skill(skill)

            if normalized_skill not in detected_skills:
                detected_skills.append(normalized_skill)

    conn.close()

    return detected_skills


# ================= TEST =================

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Please provide a PDF file path.")
        print("Example:")
        print(r'python resume_parser.py "resume.pdf"')
        sys.exit()

    pdf_path = sys.argv[1]

    # STEP 1: Extract resume text
    text = extract_text_from_pdf(pdf_path)

    print("===== RESUME TEXT EXTRACTED =====")
    print(text)

    # STEP 2: Detect skills
    skills = detect_skills(text)

    print("\n===== DETECTED SKILLS =====")

    for skill in skills:
        print("✓", skill)

    print("\nTotal Skills Detected:", len(skills))