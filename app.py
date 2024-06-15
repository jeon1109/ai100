import streamlit as st

st.write('동물 이미지 가져오기 🙂');

title = st.text_input("영어로 동물이름 찾기", "")

if st.button('찾아보기') : 
    url = 'https://edu.spartacodingclub.kr/random/?' + title
    st.image(url)
