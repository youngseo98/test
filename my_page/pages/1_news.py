import streamlit as st
import numpy as np
st.title('News')
st.header('최근 스포츠 뉴스')

st.link_button("네이버 스포츠 뉴스 보러가기", "https://sports.news.naver.com/wfootball/index")

prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")