import random
from openpyxl import Workbook
import datetime

import streamlit as st

st.title('엑셀 자동으로 다운로드가 됩니다.');

title = st.session_state['title'] ;
projectSupport = st.session_state['projectSupport'];
projectOverview = st.session_state['projectOverview'];
projectPropose = st.session_state['projectPropose'];
# 주어진 기간
start_date = datetime.datetime(2024, 1, 1, 0, 0)
end_date = datetime.datetime(2024, 1, 8, 0, 0)
selected_date_range = f"{start_date.strftime('%Y-%m-%d')} - {end_date.strftime('%Y-%m-%d')}"
persons = st.session_state['persons'];
money = st.session_state['money'];
projectRequirement = st.session_state['projectRequirement'];

# 기획서 내용
requirements = [
    ["기획서명", "프로젝트 목적", "프로젝트 개요", "프로젝트 추진방향", "프로젝트 기간", "프로젝트 참여인원", "프로젝트 예산", "프로젝트 요구사항"],
    [title, projectSupport, projectOverview, projectPropose, selected_date_range , persons, money, projectRequirement]
]

# 새로운 워크북 생성
wb = Workbook()
ws = wb.active
# 기획서 내용을 세로로 엑셀 파일에 작성
for col_num, row_data in enumerate(requirements, 1):
    for row_num, cell_value in enumerate(row_data, 1):
        cell = ws.cell(row=row_num, column=col_num)
        cell.value = cell_value

# 엑셀 파일 저장
wb.save("project_plan.xlsx")
