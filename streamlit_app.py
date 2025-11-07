# 아래에 코드를 작성해주세요.
import streamlit as st
import pandas as pd
import numpy as np

def intro():
    # Markdown 문법을 지원하여 헤더, 볼드, 이탤릭, 하이퍼링크 등 다양한 텍스트 스타일 가능
    st.markdown("# 나의 소개 페이지")
    st.markdown("## 자기소개")
    st.write("안녕하세요, 제 이름은 박선우입니다.")
    st.write("저는 **예술**과 *창작*에 관심이 있습니다.")

    st.markdown("## 좋아하는 것")
    st.write("저는 쉬는 것을 좋아합니다.")                       
    st.markdown("제가 이제 자주 방문할 사이트는 [Streamlit 공식 홈페이지](https://streamlit.io) 입니다.")

    st.header("중간 프로젝트 설명")
    st.write("'뉴턴이 사과에 맞지 않았다면?'이라는 주제로 진행했습니다.") 
    st.caption("중간 프로젝트에서 만든 코드 예시:")
    st.code("hit_apple = pygame.sprite.spritecollideany(newton, apple_group)", language="python")
    st.caption("뉴턴의 대표적인 공식")
    st.latex(r"F = ma")

def time():
    # 샘플 데이터
    data = {"요일": ["1교시", "2교시", "3교시", "4교시", "5교시"], "월": ["-", "-", "예술의 가치와 비평", "-", "초급 프랑스어2"], "화": ["대학 글쓰기2: 인문학 글쓰기", "-", "대학영어2: 말하기", "고중세미학","글쓰기세미나"], "수": ["-", "-", "예술의 가치와 비평", "-", "초급 프랑스어2"], "목":["대학 글쓰기2: 인문학 글쓰기", "-", "대학영어2: 말하기", "고중세미학","초급 프랑스어2"], "금": ["컴퓨팅 탐색", "-", "-", "-", "-"]}
    df = pd.DataFrame(data)
    
    st.markdown("# 나의 수업 시간표")
    st.write("### 정적 시간표(st.table)")
    st.table(df)
    
    # st.json(): JSON 데이터 구조를 트리 형태로 표시. 펼치기, 접기가 가능
    # JSON (JavaScript Object Notation), 자바스크립트 객체 표기법
    # 사람이 읽고 쓰기 쉽고, 컴퓨터가 분석하기도 쉬운 텍스트 기반 데이터 형식
    json_data = {"예술의 가치와 비평": {"교수": "조희원", "강의실": "43-1동 201호" }, "초급 프랑스어2": {"교수": "한정주", "강의실": "5동 206호" }, "대학 글쓰기 2: 인문학 글쓰기": {"교수": "황은미", "강의실": "3동 103호" }, "대학영어2: 말하기": {"교수": "Abigail", "강의실": "2동 101-1호" }, "고중세미학": {"교수": "권혁성", "강의실": "7동 106호"}, "글쓰기세미나": {"교수": "김광식", "강의실": "8동 304호" }, "컴퓨팅 탐색": {"교수": "변해선", "강의실": "26동 104호" }}
    st.write("### 수업 정보(st.json)")
    st.json(json_data)
    
    #지표(숫자+증감률) 표시 
    st.write("### 이번 학기 요약(st.metric)")
    st.metric(label="수강 과목 수", value="5")
    st.metric(label = "총 학점", value="15", delta="+3")

intro()
time()
