import os
from common import make_apply

import streamlit as st
from datetime import datetime, timedelta


## 제목 타이틀
make_apply();
projectNm = st.session_state['title'];
title = st.text_input(label='👥 기획서명', placeholder='사업명을 입력하세요', value=projectNm, disabled=True);
projectSupport = st.text_area(label='👤 프로젝트 목적', placeholder='프로젝트 목적을 입력하세요', max_chars=500);
projectOverview = st.text_area(label='👤 프로젝트 개요', placeholder='프로젝트 개요를 입력하세요', max_chars=100);
projectPropose = st.text_area(label='👤 프로젝트 추진방향', placeholder='프로젝트 추진방향을 입력하세요', max_chars=300);

start_date = datetime(2024, 1, 1)
end_date = start_date + timedelta(days=30)
 
selected_date_range = st.slider(
    "프로젝트 기간 설정",
    min_value=start_date,
    max_value=end_date,
    value=(start_date, start_date + timedelta(days=7)),
    step=timedelta(days=1),
)

persons = st.text_input(label='👥 프로젝트 참여인원', placeholder='참여인원을 입력하세요', max_chars=10);
money = st.text_input(label='👥 프로젝트 예산', placeholder='소요예산을 입력하세요');
projectRequirement = st.text_area(label='👤 프로젝트 요구사항', placeholder='프로젝트 요구사항 입력하세요', max_chars=500);

projectCompnay = st.session_state['name'];
st.markdown(
    f"""
    <div style="text-align: center; color: gray; font-size: 0.875em; margin-top: 1rem;">
        {projectCompnay}
    </div>
    """,
    unsafe_allow_html=True
)

## 밸리데이션 함수
def needValue():
    if projectSupport == "":
        st.error('에러: 프로젝트 목적을 입력해야 합니다.') ;
        st.stop()
    elif projectOverview == "":
        st.error('에러: 프로젝트 개요를 입력해야 합니다.') ;
        st.stop()    
    elif projectPropose == "":
        st.error('에러: 프로젝트 추진방향을 입력해야 합니다.') ;
        st.stop()    
    elif persons == "":
        st.error('에러: 프로젝트 참여인원을 입력해야 합니다.') ;
        st.stop() 
    elif money == "":
        st.error('에러: 프로젝트 예산을 입력해야 합니다.') ;
        st.stop()
    elif projectRequirement == "":
        st.error('에러: 프로젝트 요구사항을 입력해야 합니다.') ;
        st.stop()                       

isOk = st.button('맞춤법 검사하기');

if isOk : 
    needValue();
    st.page_link("pages/excel.py", label="기획서 엑셀로 만들기", icon="🙂")
    st.session_state['title'] = title;
    st.session_state['projectSupport'] = projectSupport;
    st.session_state['projectOverview'] = projectOverview;
    st.session_state['projectPropose'] = projectPropose;
    st.session_state['projectSupport'] = projectSupport;
    st.session_state['selected_date_range'] = selected_date_range;
    st.session_state['persons'] = persons;
    st.session_state['money'] = money;
    st.session_state['projectRequirement'] = projectRequirement;
            
    
