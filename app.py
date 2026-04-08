import streamlit as st
import json

st.set_page_config(page_title="數位直排作文稿紙", layout="wide")

def load_db():
    with open('writing_vault.json', 'r', encoding='utf-8') as f:
        return json.load(f)

db = load_db()

st.markdown("""
<style>
    .manuscript-paper {
        writing-mode: vertical-rl;
        text-orientation: upright;
        background-color: #fffdf5;
        background-image: 
            linear-gradient(#d1e7dd 1.5px, transparent 1.5px),
            linear-gradient(90deg, #d1e7dd 1.5px, transparent 1.5px);
        background-size: 40px 40px;
        line-height: 40px;
        padding: 40px;
        border: 3px solid #2e7d32;
        min-height: 700px;
        width: fit-content;
        margin: auto;
        font-family: "Noto Serif TC", "Microsoft JhengHei", serif;
        font-size: 26px;
        letter-spacing: 14px;
        color: #333;
    }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.title("作文靈感庫")
    selected_el = st.selectbox("🎯 選擇今日主題元素", list(db["elements"].keys()))
    st.write("---")
    st.subheader(f"{selected_el} 的 7 個內容：")
    for item in db["elements"][selected_el]:
        st.write(f"✅ {item}")
    st.write("---")
    st.subheader("📝 本次段落成語任務")
    for i, idm in enumerate(db["idioms"]):
        st.write(f"段落 {i+1}：{idm}")

st.title("✍️ 直排語音作文系統")
raw_input = st.text_area("🎙️ 請在此輸入或貼上語音辨識的文字：", height=200, placeholder="直接講出你的故事...")

if st.button("✨ 執行微修飾並填入直排稿紙"):
    if raw_input:
        fillers = ["然後", "就是說", "那個", "呃", "啊", "呢", "喔"]
        refined_text = raw_input
        for f in fillers:
            refined_text = refined_text.replace(f, "")
        st.markdown(f'<div class="manuscript-paper">{refined_text}</div>', unsafe_allow_html=True)
    else:
        st.warning("請先提供內容喔！")
