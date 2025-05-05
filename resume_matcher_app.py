import streamlit as st
import re

# Sample resume text (replace this with real data or file upload functionality)
resume_text = """
Personal skills: Strong programming skills in Python (pandas, numpy), R, SQL.
Experience: Worked with various machine learning algorithms, including regression, classification, and clustering.
Education: MSc in Data Science. 
Technical skills: Python, SQL, Machine Learning, Deep Learning, NLP, Data Visualization (Tableau, Matplotlib).
"""

# Function to highlight matching keywords in the resume
def highlight_keywords(resume_text, job_description):
    # Extract keywords from the job description (simple word extraction)
    job_keywords = re.findall(r'\b\w+\b', job_description.lower())  # Extract words as keywords
    highlighted_resume = resume_text
    
    # Highlight the keywords in the resume text
    for keyword in job_keywords:
        # Use regex to match and highlight the keywords in the resume text
        highlighted_resume = re.sub(rf'\b({keyword})\b', r'<span style="color: red; font-weight: bold;">\1</span>', highlighted_resume, flags=re.IGNORECASE)
    
    return highlighted_resume

# Streamlit Interface
st.title("Resume Keyword Matching and Highlighting")
st.write("""
    This tool allows you to input a job description and highlights matching keywords in the resume.
""")

# Create a text area for entering the job description
job_description = st.text_area("Enter Job Description:", value="Python, Machine Learning, SQL", height=200)

# Check if job description is entered
if job_description:
    # Highlight the keywords in the sample resume based on the job description
    highlighted_resume = highlight_keywords(resume_text, job_description)
    
    # Display the highlighted resume
    st.write("### Highlighted Resume")
    st.markdown(f"**Highlighted Resume**:<br>{highlighted_resume}", unsafe_allow_html=True)
else:
    st.write("Please enter a job description to see highlighted matches in the resume.")

