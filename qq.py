import streamlit as st
import pandas as pd
import numpy as np
from streamlit import container


GH_ICON = "static/github.png"
LI_ICON = "static/linkedin.png"
Noeh = "static/noeh.jpg"


st.set_page_config(page_title= 'Noeh Introduction', page_icon=Noeh, layout='wide')

cpp = """
cout << "Hello, World! I am Noeh!";
cout << "I am a BSCS - 3 Student from Cebu Institute of Technology - University";
"""

st.code(cpp, language='cpp')
st.markdown(
    "I’m a total adrenaline junkie who loves trying out different sports and activities that get my heart racing. "
    "If it’s fast, high, or a little crazy, I’m always ready to give it a shot because I love the thrill and excitement. "
    "At the same time, I really enjoy being outdoors and exploring nature. "
    "Hiking and discovering new trails is one of my favorite ways to relax and enjoy the fresh air whenever I get the chance. "
    "I also dream to become an Ironman someday!")

with st.sidebar:
    col1, col2, col3 = st.columns([1, 2, 1])
    st.image(Noeh, width=150)

    st.divider()

    st.subheader("Hobbies & Interests")
    st.markdown("""
    * Sports
    * Hiking & Nature Trails
    """)

    st.divider()

    st.subheader("My Big Goal")
    st.info("To become an Ironman athlete!")

    st.divider()

    st.subheader("Tech Skills")
    st.markdown("""
    * C/C++
    * Python
    * Java
    * HTML/CSS
    * JavaScript
    * SQL
    * Kotlin
    """)
st.balloons()

left, right = st.columns(2)
with left:
    st.subheader("Fun Facts About Me")
    with container(border=True):
        st.success("I flew a C-150 aircraft and still have my SPL up until now. (student)")
        st.success("I love playing games during my free time, especially FPS and Open World games.")
with right:
    st.subheader("Quests")
    with container(border=True):
        st.info("I want to skydive at least once before I turn 30!")
        st.info("Leave Philippines and start a new life abroad and explore the world.")


st.divider()


st.subheader("Find me online")

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        img_col, title_col = st.columns([1, 5])
        with img_col:
            st.image(GH_ICON, width=48)
        with title_col:
            st.subheader("GitHub")
        st.markdown("View my projects and code repositories.")
        st.link_button("GitHub", "https://github.com/naweeeeeh")

with col2:
    with st.container(border=True):
        img_col, title_col = st.columns([1, 5])
        with img_col:
            st.image(LI_ICON, width=48)
        with title_col:
            st.subheader("LinkedIn")

        st.markdown("Connect with me professionally.")
        st.link_button("LinkedIn", "https://www.linkedin.com/in/naweeeeeh/")

st.subheader("Live with your eyes open to the world, not closed to your wallet. The true richness of life is found in the breadth of our experiences and the courage to try new things, not the depth of our pockets. While we should pursue a life full of adventure, we must guard our hearts against the insatiable hunger of greed, for that is a hunger that is never satisfied and one that corrodes the foundations of all we build together.")

st.markdown("_makulong na sana mga corrupt_")