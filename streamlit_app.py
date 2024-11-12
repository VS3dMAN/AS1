import streamlit as st
import os

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf'}
MAX_FILE_SIZE_MB = 5

# Simple security check function (just mimicking a scan)
def simple_security_check(file_path):
    # This is a placeholder for a more advanced scan.
    # For now, let's assume that files with "virus" in their name are malicious.
    if 'virus' in file_path.lower():
        return False
    return True

# Streamlit app
st.title("Simple File Upload with Security Check")

uploaded_file = st.file_uploader("Choose a file", type=list(ALLOWED_EXTENSIONS))

if uploaded_file:
    file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Check file size
    file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
    if file_size_mb > MAX_FILE_SIZE_MB:
        st.error("File size exceeds the limit.")
        os.remove(file_path)
    elif uploaded_file.name.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS:
        # Perform simple security check
        if simple_security_check(file_path):
            st.success("File is safe!")
        else:
            st.error("Malicious file detected!")
        os.remove(file_path)
    else:
        st.error("Invalid file type.")
