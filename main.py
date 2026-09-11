from fastapi import FastAPI, UploadFile, File
import shutil
import os

from ai_pipeline import run_ai_pipeline


app = FastAPI(
    title="AI Skill Gap & Recommendation API",
    description="Resume analysis, skill gap detection and course recommendation",
    version="1.0"
)


@app.get("/")
def home():
    return {
        "message": "AI Module API is running successfully"
    }


@app.post("/analyze-resume")
async def analyze_resume(
    file: UploadFile = File(...)
):
    
    # Temporary file path
    file_path = "uploaded_resume.pdf"

    # Save uploaded PDF
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Required skills for testing
    required_skills = [
        "Python",
        "JavaScript",
        "React",
        "Node.js",
        "MongoDB",
        "SQL",
        "Machine Learning"
    ]

    # Run AI Pipeline
    result = run_ai_pipeline(
        file_path,
        required_skills
    )

    # Delete temporary file
    if os.path.exists(file_path):
        os.remove(file_path)

    return result