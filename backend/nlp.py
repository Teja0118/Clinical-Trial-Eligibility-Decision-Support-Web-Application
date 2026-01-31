import re

def extract_criteria(text: str):
    text = text.lower()

    criteria = {
        "inclusion": {
            "age_min": None,
            "age_max": None,
            "condition": None,
            "gender": None
        },
        "exclusion": {
            "age_min": None,
            "age_max": None,
            "conditions": [],
            "medications": [],
            "gender": None
        }
    }

    # -------------------------
    # AGE EXTRACTION
    # -------------------------

    # between X and Y
    match = re.search(r'between\s+(\d+)\s+and\s+(\d+)', text)
    if match:
        criteria["inclusion"]["age_min"] = int(match.group(1))
        criteria["inclusion"]["age_max"] = int(match.group(2))

    # below X
    match = re.search(r'below\s+(\d+)', text)
    if match:
        criteria["exclusion"]["age_min"] = int(match.group(1))

    # above X
    match = re.search(r'above\s+(\d+)', text)
    if match:
        criteria["exclusion"]["age_max"] = int(match.group(1))

    # -------------------------
    # CONDITION EXTRACTION
    # -------------------------

    conditions = [
        "diabetes",
        "hypertension",
        "asthma",
        "hyperlipidemia",
        "coronary artery disease",
        "chronic kidney disease",
        "hypothyroidism"
    ]

    for cond in conditions:
        if f"with {cond}" in text or f"diagnosed with {cond}" in text:
            criteria["inclusion"]["condition"] = cond.title()

        if f"exclude patients with {cond}" in text:
            criteria["exclusion"]["conditions"].append(cond.title())

    # -------------------------
    # GENDER EXTRACTION
    # -------------------------

    if "female patients" in text:
        criteria["inclusion"]["gender"] = "Female"

    if "male patients" in text:
        criteria["inclusion"]["gender"] = "Male"

    if "exclude male patients" in text:
        criteria["exclusion"]["gender"] = "Male"

    if "exclude female patients" in text:
        criteria["exclusion"]["gender"] = "Female"

    # -------------------------
    # MEDICATION EXTRACTION (EXCLUSION ONLY)
    # -------------------------

    medications = [
        "insulin",
        "metformin",
        "amlodipine",
        "lisinopril",
        "salbutamol",
        "budesonide",
        "atorvastatin",
        "rosuvastatin",
        "aspirin",
        "clopidogrel",
        "levothyroxine",
        "erythropoietin",
        "furosemide"
    ]

    for med in medications:
        if f"taking {med}" in text:
            criteria["exclusion"]["medications"].append(med.title())

    return criteria
