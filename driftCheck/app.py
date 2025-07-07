import streamlit as st
import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset
import tempfile
import os

st.set_page_config(page_title="Data Drift Detector", layout="wide")
st.title("📊 Data Drift Detection with Evidently")

st.markdown("Upload **Reference (baseline)** data and **Production (new)** data to check for data drift.")

# Upload files
ref_file = st.file_uploader("Upload Reference CSV", type=["csv"], key="ref")
prod_file = st.file_uploader("Upload Production CSV", type=["csv"], key="prod")

# If both files are uploaded
if ref_file is not None and prod_file is not None:
    try:
        ref_data = pd.read_csv(ref_file)
        prod_data = pd.read_csv(prod_file)

        # Drop rows with any missing values
        ref_data.dropna(inplace=True)
        prod_data.dropna(inplace=True)

        # Ensure both datasets have common columns only
        common_cols = list(set(ref_data.columns) & set(prod_data.columns))
        ref_data = ref_data[common_cols]
        prod_data = prod_data[common_cols]

        # Check if there are still columns to compare
        if not common_cols:
            st.error("⚠️ No common columns found between the datasets after preprocessing.")
        else:
            # Create Evidently report
            report = Report(metrics=[DataDriftPreset()])
            rep=report.run(reference_data=ref_data, current_data=prod_data)

            # Save report to temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as tmp:
                rep.save_html(tmp.name)
                tmp.flush()
                tmp_path = tmp.name

            # Display report
            with open(tmp_path, "r", encoding="utf-8") as f:
                html_content = f.read()
                st.components.v1.html(html_content, height=1000, scrolling=True)

            # Clean up
            os.remove(tmp_path)

    except Exception as e:
        st.error(f"🚨 Error while processing files: {e}")
else:
    st.info("Please upload **both** Reference and Production CSV files to proceed.")
