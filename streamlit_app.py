import streamlit as st

st.title("👋🏻 Streamlit 앱 제작")
st.subheader("두번째 제목 환영합니다!")
st.write("오른쪽 위의 'fork' 버튼을 눌러주세요. 이 페이지와 앱이 그대로 복사됩니다.")

st.link_button("streamlit 매뉴얼 페이지 바로가기!(깃허브 페이지 바로가기 등 자유롭게 바꾸기 )", "https://surish.notion.site/streamlit-113eef51495c8083986cc65f2d07470c?pvs=73")

st.success("초록색 창")
# st.주석처럼 참고하기 위해 남길 떼 샵을 씀
# st.error("빨간색 창")
st.info("파란색 창")
# st.warning("노란색 창") # ctrl+/ : 주석처리
st.image("https://media.giphy.com/media/8bE0EERrvXkq5S9BCa/giphy.gif?cid=ecf05e479tvvde0o3d3do3g67yoq0jn4zzyg9hyt63stuf0x&ep=v1_gifs_related&rid=giphy.gif&ct=g", caption="Welcome to coding world") 
