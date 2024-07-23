from pathlib import Path
import streamlit as st
from modules import *
from PIL import Image
from data import *

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()



def About():
    resume_file = current_dir / "assets" / "CV.pdf"
    profile_pic = current_dir / "assets" / "profile-pic.jpg"
    with open(resume_file, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    profile_pic = Image.open(profile_pic)
    
    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image(profile_pic, width=230)
    with col2:
        st.title(NAME)
        st.write(DESCRIPTION)
        st.download_button(
            label="📃 Download Resume",
            data=PDFbyte,
            file_name=resume_file.name,
            mime="application/octet-stream",
        )
        st.write("📫", EMAIL)

def Social(SOCIAL_MEDIA):
    st.write("#")
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")


def ExpQua():
    st.write("#")
    st.subheader("Experience & Qualifications")
    st.write(
        """
        - ✨ abc xyz         
        - ✨ abc xyz         
        - ✨ abc xyz         
    """
    )


def Skills():
    st.write("#")
    st.subheader("Hard Skills")
    for i in SKILLS:
        st.write(i)


def Proj(PROJECTS):
    st.write("#")
    st.subheader("Projects & Accomplishments")
    st.write("---")
    for project, link in PROJECTS.items():
        st.write(f"[{project}]({link})")    


def App():
    
    InitPageSetting(st, current_dir, "My Blog", "⭐")
    with st.spinner("Loading..."):
        About()
        # --- SOCIAL LINKS ---
        Social(SOCIAL_MEDIA)
        # --- EXPERIENCE & QUALIFICATIONS ---
        # ExpQua()
        # --- SKILLS ---
        Skills()
        # --- Projects & Accomplishments ---
        Proj(PROJECTS)








if __name__ == '__main__':
    App()