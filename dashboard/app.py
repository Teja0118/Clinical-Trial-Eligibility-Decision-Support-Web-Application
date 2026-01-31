import streamlit as st
import requests
import pandas as pd

# App title
st.set_page_config(page_title="Clinical Trial Eligibility Dashboard", layout="wide")

st.title("Clinical Trial Eligibility Decision Support Web Application")

st.write("Upload a clinical trial eligibility document to evaluate patient eligibility "
            "based on age, condition and exclusion rules"
)

# File upload
trial_file = st.file_uploader(
    "Upload Clinical Trial Eligibility Document (.txt)",
    type=["txt"]
)

# Process File
if trial_file is not None:
    st.info("Processing Trial Document...")

    # Call FastAPI backend
    response = requests.post(
        "http://localhost:8000/match",
        files={"file": trial_file}
    )

    if response.status_code == 200:
        results = response.json()

        if len(results) == 0:
            st.warning("No Patients found in the System!")
        else:
            df = pd.DataFrame(results)
            df["eligible"] = df["eligible"].apply(
                lambda x: "Eligible" if x else "Not Eligible"
            )

            st.success("Eligibility Evaluation completed.")
            st.subheader("Eligibility Results")

            st.dataframe(df, width='stretch')
    else:
        st.error("Error communicating with backend API.")