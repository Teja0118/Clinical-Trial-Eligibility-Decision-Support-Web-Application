import pandas as pd
from database import session_local
from models import Patient

df = pd.read_csv("../data/patients.csv")

db = session_local()

for _, row in df.iterrows():
    patient = Patient(
        patient_id=row["patient_id"],
        age=row["age"],
        gender=row["gender"],
        condition=row["condition"],
        medication=row["medication"]
    )
    db.add(patient)
    
db.commit()
db.close()

print("Patients data loaded successfully!")