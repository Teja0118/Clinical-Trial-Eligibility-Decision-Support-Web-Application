import spacy
import re

nlp = spacy.load("en_core_web_sm")

def extract_criteria(text: str):
    text_lower = text.lower()

    criteria = {
        "age_min": None, 
        "age_max": None, 
        "condition": None
    }

    # Extract age range: "between X and Y"
    age_range = re.search(r'between\s+(\d+)\s+and\s+(\d+)', text_lower)
    if age_range:
        criteria["age_min"] = int(age_range.group(1))
        criteria["age_max"] = int(age_range.group(2))

    # Extract lower range exclusion: "below X"
    below_age = re.search(r'below\s+(\d+)', text_lower)
    if below_age:
        criteria["age_min"] = int(below_age.group(1))

    # Extract upper range exclusion: "above X"
    above_age = re.search(r'above\s+(\d+)', text_lower)
    if above_age:
        criteria["age_max"] = int(above_age.group(1))

    # Extract Condition (keyboard-based)
    conditions = ["diabetes", "hypertension", "asthma"]
    for cond in conditions:
        if cond in conditions:
            if cond in text_lower:
                criteria["condition"] = cond.capitalize()
                break
        
    return criteria

    