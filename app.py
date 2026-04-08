import streamlit as st

# --- 網頁設定 ---
st.set_page_config(page_title="語音作文教練", layout="wide")

# --- CSS: 清爽直排文字樣式 ---
st.markdown("""
<style>
    /* 這裡拿掉了格線，改用大方、有質感的直排字體 */
    .vertical-text-container {
        writing-mode: vertical-rl;
        text-orientation: upright;
        background-color: #ffffff;
        padding: 40px;
        border-left: 5px solid #2e7d32; /* 左側邊界線裝飾 */
        min-height: 600px;
        width: 100%;
        font-family: "Noto Serif TC", "Microsoft JhengHei", serif;
        font-size: 28px;
        line-height: 2; /* 讓行間距變寬，方便閱讀 */
        color: #1a1a1a;
        margin-top: 20px;
    }
    .title-display {
        writing-mode: vertical-rl;
        font-size: 36px;
        font-weight: bold;
        margin-left: 50px;
        color: #2e7d32;
    }
</style>
""", unsafe_allow_html=True)

# --- 側邊欄：完全自定義區 ---
with st.sidebar:
    st.title("⚙️ 寫作設定")
    
    # 1. 題目
    essay_title = st.text_input("📍 作文題目", value="我的生活點滴")
    
    st.divider()
    
    # 2. 元素內容 (使用者自行建立)
    st.subheader("💎 我的特色元素")
    custom_element = st.text_input("元素名稱", "例如：我的鋼琴之路")
    custom_contents = st.text_area("輸入 7 個靈感內容 (每行一個)", 
                                 "旋律的起伏\n黑白鍵的對話\n指尖的靈魂\n反覆練習的汗水\n曲終的餘韻\n鋼琴的結構\n比賽的節奏",
                                 height=200)
    contents_list = custom_contents.split('\n')[:7]

    st.divider()

    # 3. 成語自定義 (使用者自行打)
    st.subheader("📖 挑戰成語")
