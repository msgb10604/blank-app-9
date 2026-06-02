import streamlit as st

# 1. 웹 페이지 제목 설정 (선택 사항이지만 배포 시 필수적인 시각 요소)
st.title("🍿 영화관 세트메뉴 조합 생성기")
st.markdown("코랩에서 작성한 파이썬 코드가 스트림릿 앱으로 실행된 화면입니다.")
st.divider() # 화면 구분선

# 2. 원본 데이터 정의
popcorn_options = ['기본', '카라멜', '어니언']
drink_options = ['생수', '탄산음료']

# 3. 원본 2중 for문 로직 유지 및 스트림릿 출력으로 변경
st.subheader("🎬 생성된 세트메뉴 리스트")

for popcorn in popcorn_options:
    for drink in drink_options:
        # st.write()를 활용하여 웹 화면에 텍스트 출력
        st.write(f"🎁 세트메뉴: **{popcorn}** 팝콘, **{drink}**")