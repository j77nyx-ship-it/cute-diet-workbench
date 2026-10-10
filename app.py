import streamlit as st
import streamlit.components.v1 as components

# 页面基础设置，隐藏侧边栏
st.set_page_config(
    page_title="🍡可爱饮食工作台",
    page_icon="🍡",
    initial_sidebar_state="collapsed",
    menu_items={}
)

# 读取index.html网页
with open("index.html", "r", encoding="utf-8") as f:
    html_text = f.read()

# 嵌入你的饮食工作台网页
components.html(html_text, height=1300, scrolling=True)
