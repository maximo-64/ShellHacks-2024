#quizzes.py

import streamlit as st

home, budget, quiz, tutorial = st.columns(4, vertical_alignment="top", gap="medium")
with home:
    st.page_link("app.py", label="Home", icon="🏠")

with budget:
    st.page_link("pages/budget-dashboard.py", label="Budgeting", icon="🧾")

with quiz:
    st.page_link("pages/quizzes.py", label="Quiz Me", icon="✏")

with tutorial:
    st.page_link("pages/tutorial.py", label="Tutorial")

st.title("Quiz")
st.write("Standalone quizzes on financial literacy that test what you learned in the tutorial. they also give points. ")