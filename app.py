from pathlib import Path
import streamlit as st
from PIL import Image
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir /"styles"/"main.css"
resume_file = current_dir /"assets"/'CV_2023031711222677.pdf'
profile_pice = current_dir/"assets"/"profile-pic (1).png"

page_title = "Digital resume| Arjun"
page_icon = ":wave:"
name = "arjun"
discription = "I am a python developer"
email = "arjun830063@gmail.com"
scocial_media = {
    "linkedin":"https://www.linkedin.com/in/arjun-c-v-86262223b/",
    "Github":"https://github.com/mlarjun"
}
project={
"Finding Fraudulent transactions using RandomForestClassifier":"https://github.com/mlarjun/Data-Science-Internship---INSAID/tree/main",
"Finding Fake news using LogisticRegression model":"https://github.com/mlarjun/ml/blob/main/project_1"
}
st.set_page_config(page_title=page_title,page_icon=page_icon)
# load resume profile pic 
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html=True)
with open(resume_file,"rb") as pdf_file:
    PDF_byte = pdf_file.read()
profile_pice = Image.open(profile_pice)



col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pice, width=230)

with col2:
    st.title(name)
    st.write(discription)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDF_byte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", email)
 


st.write('\n')
cols = st.columns(len(scocial_media))
for index, (platform, link) in enumerate(scocial_media.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 1 year as ML Data Associate
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)



st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), opencv
- 📊 Data Visulization: MS Excel,
- 📚 Modeling: Logistic regression, linear regression, RandomForestClassifier
- 🗄️ Databases: None 
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Ml Data Associate | Teckleap**")
st.write("02/2023")
st.write(
    """
- ► Annotating data for machine learning models
- ► Modifying Execel sheet for better result 
"""
)

st.write('\n')
st.write("🚧", "**Digital Marketing | Web Nexs**")
st.write("05/2018 - 05/2019")
st.write(
    """
- ► Social Media Marketing 
- ► Content writing 
- ► SEO
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in project.items():
    st.write(f"[{project}]({link})")
