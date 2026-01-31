from fastapi import FastAPI, UploadFile
#from database import session_local
from backend.database import session_local
from backend.models import Patient
from backend.nlp import extract_criteria
from backend.rules import check_eligibility

app = FastAPI()

@app.post("/match")
async def match_trial(file: UploadFile):
    text = (await file.read()).decode()
    criteria = extract_criteria(text)

    db = session_local()
    try:
        patients = db.query(Patient).all()

        results = []
        for p in patients:
            result = check_eligibility(p, criteria)
            results.append({
                "patient_id": p.patient_id,
                "eligible": result['eligible'],
                "explanation": result['explanation']
            })

        return results
    finally:
        db.close()