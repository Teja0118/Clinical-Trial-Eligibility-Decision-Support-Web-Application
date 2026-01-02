def check_eligibility(patient, criteria):
    reasons = []
    score = 0

    # Age minimum check
    if criteria.get("age_min") is not None:
        if patient.age < criteria["age_min"]:
            reasons.append(
                f"Age {patient.age} is below minimum required age {criteria['age_min']}."
            )
        else:
            score += 30

    # Age maximum check
    if criteria.get("age_max") is not None:
        if patient.age > criteria["age_max"]:
            reasons.append(
                f"Age {patient.age} is above maximum allowed age {criteria['age_max']}."
            )
        else:
            score += 30

    # Condition check (MANDATORY)
    if criteria.get("condition") is not None:
        if patient.condition.lower() != criteria["condition"].lower():
            reasons.append(
                f"Condition mismatch (required: {criteria['condition']}, found: {patient.condition})."
            )
        else:
            score += 40

    # Eligibility decision
    eligible = len(reasons) == 0

    # Explanation
    if eligible:
        explanation = "Eligible: All inclusion and exclusion criteria satisfied."
    else:
        explanation = "Not eligible: " + " ".join(reasons)

    return {
        "eligible": eligible,
        "score": score,
        "explanation": explanation
    }
