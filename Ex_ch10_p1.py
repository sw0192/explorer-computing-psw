# 아래에 코드를 작성해주세요.
import streamlit as st
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

intro()
