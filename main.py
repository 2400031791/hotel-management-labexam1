import re
from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Karmayogi.AI Assessment Engine")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def is_valid_email(email: str) -> bool:
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

@app.get("/")
def read_root():
    return {"status": "Online", "message": "Karmayogi.AI Backend Running"}

@app.post("/api/v1/register")
async def register_user(
    name: str = Form(...),
    email: str = Form(...),
    degree: str = Form(...),
    batch: str = Form(...),
    organization: str = Form(...)
):
    if not is_valid_email(email):
        raise HTTPException(status_code=400, detail="Invalid email format.")
    return {"status": "Success", "message": "Registered successfully"}

@app.post("/api/v1/generate-mcq")
async def generate_mcq(
    user_id: str = Form(...),
    file: UploadFile = File(...)
):
    mcqs = [
        {
            "question": f"Based on your uploaded document ({file.filename}), what is the core objective of capacity building?",
            "options": [
                "A. Systematic alignment of skill gaps and role benchmarks",
                "B. Manual entry processing without oversight",
                "C. Eliminating digital records permanently",
                "D. Restricting accessibility entirely"
            ],
            "correct_answer": "A. Systematic alignment of skill gaps and role benchmarks",
            "explanation": "Capacity building focuses on identifying competency gaps to target appropriate learning modules."
        },
        {
            "question": "How are assessments validated under the Karmayogi framework integration?",
            "options": [
                "A. Through automated AI competency metrics and iGOT tracking",
                "B. Through physical paper mail only",
                "C. By manual administrative locking",
                "D. Through external unverified spreadsheets"
            ],
            "correct_answer": "A. Through automated AI competency metrics and iGOT tracking",
            "explanation": "Automated assessments provide real-time proficiency scores mapped to national standards."
        }
    ]
    return {"status": "Success", "mcqs": mcqs}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)