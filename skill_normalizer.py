ALIASES = {
    # Programming / AI
    "ml": "Machine Learning",
    "machine learning": "Machine Learning",
    "ai": "Artificial Intelligence",
    "artificial intelligence": "Artificial Intelligence",

    # JavaScript
    "js": "JavaScript",
    "javascript": "JavaScript",
    "javascript language": "JavaScript",

    "ts": "TypeScript",
    "typescript": "TypeScript",

    # HTML / CSS
    "html5": "HTML",
    "html": "HTML",

    "css3": "CSS",
    "css": "CSS",

    # React
    "reactjs": "React",
    "react.js": "React",
    "react js": "React",
    "react": "React",

    # Node
    "node": "Node.js",
    "nodejs": "Node.js",
    "node.js": "Node.js",

    # Database
    "mongo": "MongoDB",
    "mongodb": "MongoDB",

    "postgres": "PostgreSQL",
    "postgresql": "PostgreSQL",

    # DSA
    "dsa": "Data Structures",
    "data structures": "Data Structures",

    # AI/ML
    "dl": "Deep Learning",
    "deep learning": "Deep Learning",

    "nlp": "Natural Language Processing",
    "natural language processing": "Natural Language Processing",

    "cv": "Computer Vision",
    "computer vision": "Computer Vision",

    "tf": "TensorFlow",
    "tensorflow": "TensorFlow",

    # Data Science
    "np": "NumPy",
    "numpy": "NumPy",

    "pd": "Pandas",
    "pandas": "Pandas",

    # Cloud
    "powerbi": "Power BI",
    "power bi": "Power BI",

    "gcp": "Google Cloud",
    "google cloud": "Google Cloud"
}


def normalize_skill(skill):
    skill = skill.strip().lower()

    if skill in ALIASES:
        return ALIASES[skill]

    return skill.title()


# Test
test_skills = [
    "Python",
    "ML",
    "JS",
    "HTML5",
    "CSS3",
    "React.js",
    "Node.js",
    "DSA",
    "MongoDB"
]

print("===== SKILL NORMALIZATION =====")

for skill in test_skills:
    print(skill, "→", normalize_skill(skill))