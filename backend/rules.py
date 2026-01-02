def check_eligibility(patient, criteria):
    if criteria["age_min"] and patient.age < criteria["age_min"]:
        return False
    if criteria["age_max"] and patient.age > criteria["age_max"]:
        return False
    if criteria["condition"] and patient.condition != criteria["condition"]:
        return False
    return True