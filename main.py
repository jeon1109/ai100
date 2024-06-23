import os
from openai import OpenAI
from common import display_markdown

import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from  PIL import Image
import numpy as np
import pandas as pd
import io

## 제목 타이틀
display_markdown();
title = st.text_input(label='👥 사업명 입력', placeholder='사업명을 입력하세요');
name = st.text_input(label='👤 작성자 입력', placeholder='작성자 이름을 입력하세요');

agree = st.checkbox("기획서 작성에 동의하십니까?");

## 밸리데이션 함수
def needValue():
    if title == "":
        st.error('에러: 사업명을 입력해야 합니다.') ;
        st.stop()
    elif name == "":
        st.error('에러: 이름을 입력해야 합니다.') ;
        st.stop()    

## 버튼 설정하기
if agree:
    needValue();
    st.page_link("pages/apply.py", label="기획서 만들러가기", icon="🙂")
    st.session_state['title'] = title;
    st.session_state['name'] = name;
    

    