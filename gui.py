import streamlit as st
import os
from main import run_assessment

# Define expected file paths
CV_UPLOAD_PATH = os.path.join('input', 'resume', 'uploaded_cv.pdf')
REQ_UPLOAD_PATH = os.path.join('input', 'requirements', 'uploaded_req.txt')
OUTPUT_JSON_PATH = os.path.join('results', 'parsed_cv.json')

st.title('CV Scrutinizer')
st.write('Upload a candidate CV and job requirements to assess the fit.')

cv_file = st.file_uploader('Upload Candidate CV (PDF)', type=['pdf'])
req_file = st.file_uploader('Upload Job Requirements (TXT)', type=['txt'])

if st.button('Run Assessment'):
    if not cv_file or not req_file:
        st.error('Please upload both a CV and a requirements file.')
    else:
        # Save uploaded files to expected locations
        os.makedirs(os.path.dirname(CV_UPLOAD_PATH), exist_ok=True)
        os.makedirs(os.path.dirname(REQ_UPLOAD_PATH), exist_ok=True)
        with open(CV_UPLOAD_PATH, 'wb') as f:
            f.write(cv_file.read())
        with open(REQ_UPLOAD_PATH, 'wb') as f:
            f.write(req_file.read())
        try:
            assessment = run_assessment(CV_UPLOAD_PATH, REQ_UPLOAD_PATH, OUTPUT_JSON_PATH)
            st.subheader('Candidate Assessment')
            st.write(assessment)
        except Exception as e:
            st.error(f'Error: {e}')
