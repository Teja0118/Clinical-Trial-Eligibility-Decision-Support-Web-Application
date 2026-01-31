def check_eligibility(patient, criteria):
    reasons = []

    inc = criteria["inclusion"]
    exc = criteria["exclusion"]

    # AGE CHECKS

    if inc["age_min"] is not None and patient.age < inc["age_min"]:
        reasons.append(
            f"Age {patient.age} is below required minimum age {inc['age_min']}."
        )

    if inc["age_max"] is not None and patient.age > inc["age_max"]:
        reasons.append(
            f"Age {patient.age} exceeds allowed maximum age {inc['age_max']}."
        )

    if exc["age_min"] is not None and patient.age < exc["age_min"]:
        reasons.append(
            f"Age {patient.age} falls under exclusion criteria."
        )

    if exc["age_max"] is not None and patient.age > exc["age_max"]:
        reasons.append(
            f"Age {patient.age} falls under exclusion criteria."
        )

    # CONDITION (MANDATORY IF PRESENT)

    if inc["condition"] and patient.condition.lower() != inc["condition"].lower():
        reasons.append(
            f"Condition mismatch (required: {inc['condition']}, found: {patient.condition})."
        )

    # GENDER CHECK (OPTIONAL)

    if inc["gender"] and patient.gender.lower() != inc["gender"].lower():
        reasons.append(
            f"Gender mismatch (required: {inc['gender']}, found: {patient.gender})."
        )

    if exc["gender"] and patient.gender.lower() == exc["gender"].lower():
        reasons.append(
            f"Gender {patient.gender} is excluded by trial."
        )

    # MEDICATION EXCLUSION

    if patient.medication.title() in exc["medications"]:
        reasons.append(
            f"Medication {patient.medication} is excluded by trial protocol."
        )

    # CONDITION EXCLUSION

    if patient.condition.title() in exc["conditions"]:
        reasons.append(
            f"Condition {patient.condition} is excluded by trial protocol."
        )

    # FINAL DECISION

    eligible = len(reasons) == 0

    explanation = (
        "Eligible: All inclusion and exclusion criteria satisfied."
        if eligible
        else "Not eligible: " + " ".join(reasons)
    )

    return {
        "eligible": eligible,
        "explanation": explanation
    }
