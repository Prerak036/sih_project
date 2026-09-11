import sqlite3

# Database connection
conn = sqlite3.connect("skills.db")
cursor = conn.cursor()

# Create skills table
cursor.execute("""
CREATE TABLE IF NOT EXISTS skills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    skill_name TEXT UNIQUE NOT NULL,
    category TEXT,
    demand_level TEXT,
    recommended_course TEXT
    )
""")

# Skills data
skills = [

    # ================= PROGRAMMING =================
    ("Python", "Programming", "High", "Python Programming"),
    ("Java", "Programming", "High", "Java Development"),
    ("C", "Programming", "High", "C Programming"),
    ("C++", "Programming", "High", "C++ and DSA"),
    ("C#", "Programming", "High", "C# Development"),
    ("Go", "Programming", "High", "Go Programming"),
    ("Rust", "Programming", "Medium", "Rust Programming"),
    ("Kotlin", "Programming", "High", "Kotlin Development"),
    ("Swift", "Programming", "High", "Swift Development"),
    ("R", "Programming", "High", "R Programming"),
    ("PHP", "Programming", "High", "PHP Development"),

    # ================= WEB DEVELOPMENT =================
    ("HTML", "Web Development", "High", "HTML & Web Fundamentals"),
    ("CSS", "Web Development", "High", "CSS & Responsive Design"),
    ("JavaScript", "Web Development", "High", "JavaScript Development"),
    ("TypeScript", "Web Development", "High", "TypeScript Development"),
    ("React", "Web Development", "High", "React Web Development"),
    ("Angular", "Web Development", "High", "Angular Development"),
    ("Vue.js", "Web Development", "High", "Vue.js Development"),
    ("Next.js", "Web Development", "High", "Next.js Development"),
    ("Nuxt.js", "Web Development", "Medium", "Nuxt.js Development"),
    ("Node.js", "Web Development", "High", "Node.js Backend Development"),
    ("Express.js", "Web Development", "High", "Express.js Development"),
    ("Django", "Web Development", "High", "Django Development"),
    ("Flask", "Web Development", "High", "Flask Development"),
    ("FastAPI", "Web Development", "High", "FastAPI Development"),
    ("Spring Boot", "Web Development", "High", "Spring Boot Development"),
    ("Laravel", "Web Development", "Medium", "Laravel Development"),
    ("Bootstrap", "Web Development", "High", "Bootstrap"),
    ("Tailwind CSS", "Web Development", "High", "Tailwind CSS"),

    # ================= DATABASE =================
    ("SQL", "Database", "High", "SQL & Database Management"),
    ("MySQL", "Database", "High", "MySQL Database"),
    ("PostgreSQL", "Database", "High", "PostgreSQL"),
    ("MongoDB", "Database", "High", "MongoDB"),
    ("Redis", "Database", "High", "Redis"),
    ("Oracle", "Database", "High", "Oracle Database"),
    ("SQLite", "Database", "Medium", "SQLite"),
    ("Firebase", "Database", "High", "Firebase"),
    ("Cassandra", "Database", "Medium", "Apache Cassandra"),
    ("DynamoDB", "Database", "High", "AWS DynamoDB"),

    # ================= AI / MACHINE LEARNING =================
    ("Artificial Intelligence", "AI/ML", "Very High", "Artificial Intelligence"),
    ("Machine Learning", "AI/ML", "Very High", "Machine Learning with Python"),
    ("Deep Learning", "AI/ML", "Very High", "Deep Learning"),
    ("Natural Language Processing", "AI/ML", "High", "NLP with Python"),
    ("Computer Vision", "AI/ML", "High", "Computer Vision"),
    ("Generative AI", "AI/ML", "Very High", "Generative AI"),
    ("Large Language Models", "AI/ML", "Very High", "Large Language Models"),
    ("Prompt Engineering", "AI/ML", "High", "Prompt Engineering"),
    ("Reinforcement Learning", "AI/ML", "Medium", "Reinforcement Learning"),
    ("Scikit-learn", "AI/ML", "High", "Scikit-learn & Machine Learning"),
    ("TensorFlow", "AI/ML", "High", "TensorFlow & Deep Learning"),
    ("PyTorch", "AI/ML", "High", "PyTorch & Deep Learning"),
    ("Keras", "AI/ML", "High", "Keras Deep Learning"),
    ("OpenCV", "AI/ML", "High", "OpenCV & Computer Vision"),
    ("Hugging Face", "AI/ML", "High", "Hugging Face NLP"),
    ("LangChain", "AI/ML", "High", "LangChain & LLM Applications"),

    # ================= DATA SCIENCE =================
    ("Data Science", "Data Science", "High", "Data Science with Python"),
    ("NumPy", "Data Science", "High", "NumPy for Data Science"),
    ("Pandas", "Data Science", "High", "Pandas for Data Analysis"),
    ("Matplotlib", "Data Science", "High", "Matplotlib Data Visualization"),
    ("Seaborn", "Data Science", "High", "Seaborn Data Visualization"),
    ("Statistics", "Data Science", "High", "Statistics for Data Science"),
    ("Data Analysis", "Data Science", "High", "Data Analysis"),
    ("Data Visualization", "Data Science", "High", "Data Visualization"),
    ("Feature Engineering", "Data Science", "High", "Feature Engineering"),
    ("Time Series Analysis", "Data Science", "Medium", "Time Series Analysis"),

    # ================= DATA ANALYTICS =================
    ("Excel", "Data Analytics", "High", "Advanced Excel"),
    ("Power BI", "Data Analytics", "High", "Power BI Data Analytics"),
    ("Tableau", "Data Analytics", "High", "Tableau Data Visualization"),
    ("Google Analytics", "Data Analytics", "High", "Google Analytics"),
    ("ETL", "Data Analytics", "High", "ETL & Data Pipelines"),
    ("Data Cleaning", "Data Analytics", "High", "Data Cleaning"),
    ("Business Intelligence", "Data Analytics", "High", "Business Intelligence"),

    # ================= CLOUD =================
    ("Cloud Computing", "Cloud", "High", "Cloud Computing Fundamentals"),
    ("AWS", "Cloud", "High", "AWS Cloud Computing"),
    ("Microsoft Azure", "Cloud", "High", "Microsoft Azure"),
    ("Azure", "Cloud", "High", "Microsoft Azure"),
    ("Google Cloud", "Cloud", "High", "Google Cloud Platform"),
    ("Google Cloud Platform", "Cloud", "High", "Google Cloud Platform"),
    ("AWS EC2", "Cloud", "High", "AWS EC2"),
    ("AWS S3", "Cloud", "High", "AWS S3"),
    ("AWS Lambda", "Cloud", "High", "AWS Lambda"),

    # ================= DEVOPS =================
    ("Git", "DevOps", "High", "Git & Version Control"),
    ("GitHub", "DevOps", "High", "GitHub"),
    ("GitLab", "DevOps", "High", "GitLab"),
    ("Docker", "DevOps", "High", "Docker & DevOps"),
    ("Kubernetes", "DevOps", "Very High", "Kubernetes"),
    ("Jenkins", "DevOps", "High", "Jenkins CI/CD"),
    ("CI/CD", "DevOps", "High", "CI/CD Pipeline"),
    ("Terraform", "DevOps", "High", "Terraform"),
    ("Ansible", "DevOps", "Medium", "Ansible Automation"),
    ("Linux", "DevOps", "High", "Linux Administration"),

    # ================= CYBER SECURITY =================
    ("Cyber Security", "Cyber Security", "High", "Cyber Security Fundamentals"),
    ("Network Security", "Cyber Security", "High", "Network Security"),
    ("Ethical Hacking", "Cyber Security", "High", "Ethical Hacking"),
    ("Penetration Testing", "Cyber Security", "High", "Penetration Testing"),
    ("Cryptography", "Cyber Security", "High", "Cryptography"),
    ("Information Security", "Cyber Security", "High", "Information Security"),
    ("Web Security", "Cyber Security", "High", "Web Application Security"),
    ("OWASP", "Cyber Security", "High", "OWASP Web Security"),

    # ================= MOBILE =================
    ("Android Development", "Mobile Development", "High", "Android Development"),
    ("Android Studio", "Mobile Development", "High", "Android Studio"),
    ("Flutter", "Mobile Development", "High", "Flutter Development"),
    ("Dart", "Mobile Development", "High", "Dart Programming"),
    ("React Native", "Mobile Development", "High", "React Native"),
    ("iOS Development", "Mobile Development", "High", "iOS Development"),

    # ================= TESTING =================
    ("Software Testing", "Testing", "High", "Software Testing"),
    ("Manual Testing", "Testing", "High", "Manual Software Testing"),
    ("Automation Testing", "Testing", "High", "Automation Testing"),
    ("Selenium", "Testing", "High", "Selenium Automation"),
    ("PyTest", "Testing", "High", "PyTest"),
    ("JUnit", "Testing", "High", "JUnit Testing"),
    ("Postman", "Testing", "High", "API Testing with Postman"),
    ("Jest", "Testing", "High", "Jest JavaScript Testing"),

    # ================= API / BACKEND =================
    ("REST API", "Backend", "High", "REST API Development"),
    ("GraphQL", "Backend", "High", "GraphQL"),
    ("API Development", "Backend", "High", "API Development"),
    ("Microservices", "Backend", "High", "Microservices Architecture"),
    ("Authentication", "Backend", "High", "Authentication & Authorization"),
    ("JWT", "Backend", "High", "JWT Authentication"),

    # ================= UI / UX =================
    ("UI/UX Design", "Design", "High", "UI/UX Design"),
    ("Figma", "Design", "High", "Figma UI/UX"),
    ("Adobe XD", "Design", "Medium", "Adobe XD"),
    ("Wireframing", "Design", "High", "UI/UX Wireframing"),
    ("Prototyping", "Design", "High", "UI/UX Prototyping"),
    ("User Research", "Design", "High", "UX User Research"),

    # ================= COMPUTER SCIENCE =================
    ("Data Structures", "Computer Science", "Very High", "Data Structures & Algorithms"),
    ("Algorithms", "Computer Science", "Very High", "Algorithms & DSA"),
    ("Object Oriented Programming", "Computer Science", "Very High", "Object Oriented Programming"),
    ("Operating Systems", "Computer Science", "High", "Operating Systems"),
    ("Computer Networks", "Computer Science", "High", "Computer Networks"),
    ("Database Management", "Computer Science", "High", "Database Management Systems"),
    ("Software Engineering", "Computer Science", "High", "Software Engineering"),

    # ================= SOFT SKILLS =================
    ("Communication", "Soft Skills", "High", "Communication Skills"),
    ("Problem Solving", "Soft Skills", "High", "Problem Solving"),
    ("Teamwork", "Soft Skills", "High", "Teamwork & Collaboration"),
    ("Leadership", "Soft Skills", "High", "Leadership Skills"),
    ("Time Management", "Soft Skills", "High", "Time Management"),
    ("Critical Thinking", "Soft Skills", "High", "Critical Thinking"),
    ("Presentation Skills", "Soft Skills", "High", "Presentation Skills"),
]

# Insert data without duplicates
cursor.executemany("""
INSERT OR IGNORE INTO skills
(skill_name, category, demand_level, recommended_course)
VALUES (?, ?, ?, ?)
""", skills)

conn.commit()

print("Skill database updated successfully!")

# Display database
cursor.execute("""
SELECT id, skill_name, category, demand_level, recommended_course
FROM skills
""")

for row in cursor.fetchall():
    print(row)

conn.close()