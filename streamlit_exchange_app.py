
import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

st.set_page_config(layout="wide", page_title="환율 비교 대시보드")

# ===============================
# 1. 데이터 불러오기
# ===============================
df = pd.read_excel("환율_1개월_데이터.xlsx")

# 중복 컬럼 제거 (날짜 중복 방지)
df = df.loc[:, ~df.columns.duplicated()]

# -------------------------------
# 날짜 컬럼 정리
# -------------------------------
if "날짜" not in df.columns:
    st.error("❌ 엑셀 파일에 '날짜' 컬럼이 없습니다.")
    st.stop()

def fix_date(x):
    """
    11.27 / 11.5 / '11.27' → datetime
    """
    try:
        x = str(x).strip()
        month, day = x.split(".")
        month = int(month)
        day = int(day)
        year = datetime.now().year
        return datetime(year, month, day)
    except:
        return pd.NaT

df["날짜"] = df["날짜"].apply(fix_date)
df = df.dropna(subset=["날짜"])
df = df.sort_values("날짜").reset_index(drop=True)

# ===============================
# 2. 통화 컬럼 추출 (통화명 오류 해결 핵심)
# ===============================
currency_cols = [c for c in df.columns if c != "날짜"]

if len(currency_cols) == 0:
    st.error("❌ 통화 데이터 컬럼이 없습니다.")
    st.stop()

# ===============================
# 3. 사이드바 메뉴
# ===============================
menu = st.sidebar.radio("메뉴 선택", ["설명", "환율 비교"])

# ===============================
# 4. 설명 페이지
# ===============================
if menu == "설명":
    st.title("환율 비교 웹 앱 설명")

    st.markdown("""
    ### 학번 / 학과 / 이름
    2025-12284 / 인문계열 / 박선우

    ---

    ### 웹 앱에 대한 설명
    본 웹 애플리케이션은 여러 국가의 환율 데이터를 한 화면에서 비교·분석할 수 있도록 설계된 환율 비교 대시보드이다.  
    사용자는 미국 달러, 유로, 일본 엔 등 주요 통화의 **매매기준율 변화와 증감률을 동시에 확인**할 수 있으며,  
    이를 통해 **해외여행 시 환율 추이를 파악하거나, 환율 변동을 투자 관점에서 분석하는 데 도움**을 받을 수 있다.  

    특히 여러 통화를 동시에 선택·해제하며 비교할 수 있어, 단일 환율 조회가 아닌 **상대적인 환율 흐름 파악**에 초점을 둔 웹 앱이다.

    ---

    ### 데이터에 대한 설명
    본 웹 앱에서 사용된 데이터는 네이버 금융 환율 페이지에서 수집한 **최근 1개월간의 일별 환율 데이터**이다.  
    각 데이터에는 다음 정보가 포함되어 있다.

    - **날짜**: 환율이 적용된 기준 날짜  
    - **통화별 매매기준율**: 해당 날짜에 은행 거래의 기준이 되는 대표 환율  
    - **증감률(%)**: 전일 대비 환율의 변동 비율  

    매매기준율이란, 외화를 사고팔 때 기준이 되는 평균적인 환율로,  
    실제 매수·매도 환율 계산의 기준점 역할을 하는 지표이다.

    ---

    ### 작동 방식 설명
    사용자는 웹 앱 좌측 사이드바를 통해 기능을 선택할 수 있다.

    - **설명 버튼**을 클릭하면 웹 앱의 목적, 데이터 구성, 작동 방식에 대한 설명을 확인할 수 있다.
    - **환율 비교 버튼**을 클릭하면 환율 비교 대시보드 화면으로 이동한다.
    - 대시보드에서는 전체 통화를 한 번에 선택하거나,  
    개별 통화를 체크박스 형태로 선택·해제할 수 있다.
    - 선택된 통화에 따라 **매매기준율 선 그래프**와 **증감률 선 그래프**가 실시간으로 갱신된다.
    - 그래프 하단에서는 선택된 통화들을 기준으로  
    환율 순위 및 투자 가치 분석 결과가 자동으로 변경되어 표시된다.

    이를 통해 사용자는 관심 있는 통화만 선별하여 직관적으로 환율 변화를 분석할 수 있다.

    ---

    ### 한계
    본 웹 앱은 다음과 같은 한계를 가진다.

    - 수집 데이터가 **최근 1개월로 한정**되어 있어 장기적인 환율 추세 분석에는 한계가 있다.
    - 매매기준율은 실제 은행별 매수·매도 환율과 차이가 존재할 수 있다.
    - 환율 변동에 영향을 미치는 금리, 경제 지표, 정치적 요인 등은 분석에 포함되지 않았다.
    - 투자 가치는 단순한 수치 기반 지표로 산출되며, 실제 투자 판단을 대체할 수는 없다.

    따라서 본 웹 앱은 **참고용 분석 도구**로 활용하는 것이 적절하다.

    ---

    ### 한 학기 소감
    학기 시작 후 두 프로젝트를 실시해야한다는 것에 많은 부담이 있었습니다. 
    하지만 수업을 들으며 다양한 내용들을 배우고 AI의 도움을 받아 직접 프로젝트를 만들어보니 자신감이 생겼습니다.
    한 학기 동안 교수님, 조교님들 모두 정말 수고 많으셨고 연말 잘 마무리 하시길 바라겠습니다.
    정말 감사드립니다!!
    """)

    st.stop()

# ===============================
# 5. 환율 비교 페이지
# ===============================
st.title("📈 환율 비교 대시보드")

st.sidebar.subheader("통화 선택")
select_all = st.sidebar.checkbox("전체 선택", value=True)

if select_all:
    selected_currencies = st.sidebar.multiselect(
        "표시할 통화",
        currency_cols,
        default=currency_cols
    )
else:
    selected_currencies = st.sidebar.multiselect(
        "표시할 통화",
        currency_cols,
        default=[]
    )

if not selected_currencies:
    st.warning("⚠ 최소 1개 이상의 통화를 선택해야 합니다.")
    st.stop()

st.markdown(
    """
**통화 코드 설명**  
USD(미국 달러), JPY(일본 엔), EUR(유로), CNY(중국 위안), GBP(영국 파운드), 
AUD(호주 달러), CAD(캐나다 달러), CHF(스위스 프랑), 
HKD(홍콩 달러), SGD(싱가포르 달러)를 의미합니다.
"""
)
rate_df = df[["날짜"] + selected_currencies]
rate_long = rate_df.melt(
    id_vars="날짜",
    var_name="통화",
    value_name="매매기준율"
)
# ===============================
# 8. 데이터 미리보기
# ===============================
st.markdown("---")
st.subheader("📋 데이터 미리보기")
st.dataframe(rate_df)


# ===============================
# 6. 매매기준율 그래프
# ===============================
st.subheader("💵 매매기준율 선 그래프")

fig1 = px.line(
    rate_long,
    x="날짜",
    y="매매기준율",
    color="통화",
    markers=True
)
st.plotly_chart(fig1, use_container_width=True)

# ===============================
# 7. 증감률 그래프
# ===============================
st.subheader("📊 증감률(%) 선 그래프")

pct_df = df[selected_currencies].pct_change() * 100
pct_df.insert(0, "날짜", df["날짜"])

pct_long = pct_df.melt(
    id_vars="날짜",
    var_name="통화",
    value_name="증감률"
)

fig2 = px.line(
    pct_long,
    x="날짜",
    y="증감률",
    color="통화",
    markers=True
)
st.plotly_chart(fig2, use_container_width=True)

# ===============================
# 9. 데이터 분석 영역
# ===============================
# ==================================================
# 📘 데이터 분석 영역
# ==================================================
st.markdown("---")
st.subheader("📘 선택 화폐 데이터 분석")

analysis_df = df[["날짜"] + selected_currencies].copy()

# --------------------------------------------------
# 1. 환율 평균 및 순위 테이블
# --------------------------------------------------
mean_rates = analysis_df[selected_currencies].mean().sort_values(ascending=False)

rank_df = pd.DataFrame({
    "순위": range(1, len(mean_rates) + 1),
    "통화명": mean_rates.index,
    "평균 환율": mean_rates.values
})

st.markdown("### 💱 평균 환율 순위")
st.write(
    "선택된 기간 동안의 **평균 매매기준율**을 기준으로 화폐를 정렬한 결과입니다."
)
st.dataframe(rank_df, use_container_width=True)

highest_currency = mean_rates.idxmax()

st.write(
    f"- **선택된 화폐들 중 평균 환율이 가장 높은 화폐는 "
    f"'{highest_currency}'입니다.**"
)

# --------------------------------------------------
# 2. 투자 가치 기준 설명
# --------------------------------------------------
st.markdown("### 📈 투자 가치 평가 기준")
st.write(
    """
본 대시보드에서는 투자 가치가 높은 화폐를  
**① 평균 증감률이 높고, ② 변동성(표준편차)이 낮은 화폐**로 정의합니다.

- 평균 증감률이 높다는 것은 해당 화폐가 전반적으로 상승하는 경향을 보였음을 의미합니다.
- 변동성이 낮다는 것은 가격 변동 폭이 비교적 작아 투자 리스크가 낮음을 뜻합니다.
- 따라서 두 요소를 함께 고려해야 단기 수익성과 안정성을 동시에 반영할 수 있습니다.

이를 수치화하기 위해 다음과 같은 투자 점수를 계산합니다.
"""
)

st.code("투자 점수 = 평균 증감률 − 변동성")

# --------------------------------------------------
# 3. 투자 점수 테이블
# --------------------------------------------------
pct_change_df = analysis_df[selected_currencies].pct_change() * 100

investment_df = pd.DataFrame({
    "평균 증감률(%)": pct_change_df.mean(),
    "변동성(표준편차)": pct_change_df.std()
})

investment_df["투자 점수"] = (
    investment_df["평균 증감률(%)"] - investment_df["변동성(표준편차)"]
)

investment_df = investment_df.sort_values("투자 점수", ascending=False)

st.markdown("### 📊 투자 점수 비교 테이블")
st.dataframe(investment_df, use_container_width=True)

best_currency = investment_df.index[0]

st.write(
    f"- **위 기준에 따라 선택된 화폐들 중 투자 가치가 가장 높다고 "
    f"판단되는 화폐는 '{best_currency}'입니다.**"
)
