import streamlit as st
import pandas as pd
import numpy as np
from streamlit import container
from streamlit_carousel import carousel
import base64

Noeh = "static/noeh.jpg"
st.set_page_config(page_title='Noeh Introduction', page_icon=Noeh, layout='wide', initial_sidebar_state = 'expanded')

GH_ICON = "static/github.png"
LI_ICON = "static/linkedin.png"
IMAGE_FILE = "static/radiant_dire5.jpg"
HERO_UNIVERSAL_ICON = "static/hero_universal.png"
VIDEO_FILE = "static/dota_montage_webm.webm"
LOGO_ICON = "static/logo.png"
EXCELONE_ICON = "static/excel.png"
IMMORTAL_ICON = "static/immo.png"
MLBB_ICON = "static/mlbbnobg.png"


def local_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"CSS file not found. Make sure 'static/styles.css' exists.")

local_css("static/styles.css")

@st.cache_data
def get_file_as_base64(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except FileNotFoundError:
        st.error(f"File not found: {file_path}")
        return None

image_base64 = get_file_as_base64(IMAGE_FILE)
video_base64 = get_file_as_base64(VIDEO_FILE)
logo_base64 = get_file_as_base64(LOGO_ICON)
excelone_base64 = get_file_as_base64(EXCELONE_ICON)
immortal_base64 = get_file_as_base64(IMMORTAL_ICON)
mlbb_base64 = get_file_as_base64(MLBB_ICON)
hero_universal_base64 = get_file_as_base64(HERO_UNIVERSAL_ICON)


if all([image_base64, video_base64, logo_base64, excelone_base64, immortal_base64, mlbb_base64, hero_universal_base64]):
    IMAGE_HTML = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
        background-image: url("data:image/jpg;base64,{image_base64}");
        background-size: cover;
        background-position: center center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        position: relative;
        z-index: 1;
    }}
    [data-testid="stAppViewContainer"] > .main::before {{
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(0, 0, 0, 0.7); 
        z-index: -1; 
    }}
    [data-testid="stSidebar"] {{
        background: rgba(10, 10, 10, 0.9) !important;
        z-index: 1;
    }}
    .main .block-container {{
        background: transparent;
    }}
    </style>
    """
    st.markdown(IMAGE_HTML, unsafe_allow_html=True)
else:
    st.error("A static asset was not found. Please check your 'static' folder and make sure all images are present.")


with st.sidebar:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(Noeh, width=150)

    st.divider()

    st.subheader("Hobbies & Interests")
    st.markdown("""
    * Sports
    * Hiking & Nature Trails
    """)

    st.divider()

    st.subheader("My Big Goal")
    st.info("To become an Ironman athlete!!️")

    st.divider()

    st.subheader("Tech Skills")
    st.html("""
        <div class="skill-pill">C/C++</div>
        <div class="skill-pill">Python</div>
        <div class="skill-pill">Java</div>
        <div class="skill-pill">HTML/CSS</div>
        <div class="skill-pill">JavaScript</div>
        <div class="skill-pill">SQL</div>
        <div class="skill-pill">Kotlin</div>
    """)

st.html(f"""
        <video autoplay loop muted playsinline class="main-content-video">
            <source src="data:video/webm;base64,{video_base64}" type="video/webm">
            Your browser does not support the video tag.
        </video>
    """)


cpp = """
cout << "Hello, World! I am Noeh!";
cout << "I am a BSCS - 3 Student from Cebu Institute of Technology - University";
"""
st.code(cpp, language='cpp')



st.html("""
    <p style="font-family: 'Radiance', sans-serif; font-size: 1rem; color: #E0E0E0;">
    I’m a total adrenaline junkie who loves trying out different sports and activities that get my heart racing. 
    If it’s fast, high, or a little crazy, I’m always ready to give it a shot because I love the thrill and excitement. 
    At the same time, I really enjoy being outdoors and exploring nature. 
    Hiking and discovering new trails is one of my favorite ways to relax and enjoy the fresh air whenever I get the chance. 
    I also dream to become an Ironman someday!
    </p>
""")

st.balloons()


st.subheader("My Journey So Far")

st.code("""// adjust the sidebar to reveal text contents """, language = 'cpp')
carousel_items = [
    {
        "title": "Project: ExcelOne (OOP1)",
        "text": "A platform for tutors and teachers to interact and make calls, built for our Object-Oriented Programming 1 project using Java and WebRTC Components.",
        "img": f"data:image/png;base64,{excelone_base64}"
    },
    {
        "title": "Project: Operation: BOOM! (Kotlin)",
        "text": "A Minesweeper game built using Kotlin, featuring classic pixel art and gameplay mechanics.",
        "img": f"data:image/png;base64,{logo_base64}"
    },
    {
        "title": "Achievement: Immortal 2 (Valorant)",
        "text": "Peaked at the Immortal 2 rank in Valorant, placing me in the top percentile of competitive players.",
        "img": f"data:image/png;base64,{immortal_base64}"
    },
    {
        "title": "Achievement: Mythical Immortal (MLBB)",
        "text": "Reached the top-tier Mythical Immortal rank in Mobile Legends: Bang Bang.",
        "img": f"data:image/png;base64,{mlbb_base64}"
    }
]

carousel(items=carousel_items, width=0.5)


st.html(f"""
    <div class="custom-columns">
        <div class="custom-column">
            <h3>Fun Facts About Me</h3>
            <div data-testid="stVerticalBlockBorderWrapper"> 
                <div class="custom-success">I flew a C-150 aircraft and still have my SPL up until now. (student)</div>
                <div class="custom-success" style="margin-bottom: 0;">I love playing games during my free time, especially FPS, MOBA, and Open World games.</div>
            </div>
        </div>

        <div class="custom-column">
            <h3>Quests</h3>
            <div data-testid="stVerticalBlockBorderWrapper">
                <div class="custom-info">I want to skydive at least once before I turn 30!</div>
                <div class="custom-info" style="margin-bottom: 0;">Leave Philippines and start a new life abroad and explore the world.</div>
            </div>
        </div>
    </div>
""")

st.html('<div class="custom-divider"></div>')

st.html("<h1 style='text-align: center;'>Find me online!</h1>")

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        img_col, title_col = st.columns([1, 5])
        with img_col:
            st.image(GH_ICON, width=48)
        with title_col:
            st.html("<h3 style='margin: 0; padding-top: 0.5rem;'>GitHub</h3>")

        st.html(f"""
            <p style="font-family: 'Radiance', sans-serif; margin-top: 1rem;">
                View my projects and code repositories.
            </p>
            <a href="https://github.com/naweeeeeh" target="_blank" class="custom-link-button">
                GitHub
            </a>
        """)

with col2:
    with st.container(border=True):
        img_col, title_col = st.columns([1, 5])
        with img_col:
            st.image(LI_ICON, width=48)
        with title_col:
            st.html("<h3 style='margin: 0; padding-top: 0.5rem;'>LinkedIn</h3>")

        st.html(f"""
            <p style="font-family: 'Radiance', sans-serif; margin-top: 1rem;">
                Connect with me professionally.
            </p>
            <a href="https://www.linkedin.com/in/naweeeeeh/" target="_blank" class="custom-link-button">
                LinkedIn
            </a>
        """)

st.html("""
    <p class="quote">
    "Live with your eyes open to the world, not closed to your wallet. The true richness of life is found in the breadth of our experiences and the courage to try new things, not the depth of our pockets. While we should pursue a life full of adventure, we must guard our hearts against the insatiable hunger of greed, for that is a hunger that is never satisfied and one that corrodes the foundations of all we build together."
    </p>
""")

st.html("<p class='sign-off'>— makulong na sana mga corrupt</p>")