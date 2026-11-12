import streamlit as st

# 페이지 객체 생성
page_1 = st.Page("page_1.py", title="1 페이지")
page_2 = st.Page("page_2.py", title="2 페이지")
page_3 = st.Page("page_3.py", title="3 페이지")
# 네비게이션 설정
pages = st.navigation([page_1, page_2, page_3], position = "top")
# 실행
pages.run()

st.title("My First Streamlit App")

st.write("Hello, welcome to my app!")

st.markdown("안녕 *여러분*")
import streamlit as st

import streamlit as st

st.badge("New")
st.badge("Success", icon=":material/check:", color="green")

st.markdown(
    ":violet-badge[:material/star: Favorite] :orange-badge[⚠️ Needs review] :gray-badge[Deprecated]"
)
import streamlit as st

st.title("This is a title")
st.title("_Streamlit_ is :blue[cool] :sunglasses:")
st.title("Dashboard", icon=":material/dashboard:")

