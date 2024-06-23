import streamlit as st

def display_markdown():
    st.markdown("# 기획서명 입력");

    st.markdown(
    """
    <style>
     /* Streamlit 기본 컴포넌트 스타일 조정 */
    .blue-button {
        display : inline-block;
        background-color: #6dabe4;
        color: #fff;
        border: none;
        padding: 15px 39px;
        text-align: center;
        text-decoration: none;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 8px;
        transition : all 0.2s;
        cursor: pointer;
        margin-left : 20%;
    }
    
    </style>
    """,
    unsafe_allow_html=True
);
    
def make_apply() :
    st.markdown("# 기획서 구성하기");



    