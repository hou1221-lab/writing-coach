import streamlit as st

# --- 網頁設定 ---
st.set_page_config(page_title="語音作文教導助手", layout="wide")

# --- CSS: 直排與介面美化 ---
st.markdown("""
<style>
    .vertical-text-container {
        writing-mode: vertical-rl;
        text-orientation: upright;
        background-color: #ffffff;
        padding: 40px;
        border-left: 5px solid #2e7d32;
        min-height: 600px;
        width: 100%;
        font-family: "Noto Serif TC", "Microsoft JhengHei", serif;
        font-size: 28px;
        line-height: 2;
        color: #1a1a1a;
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

# --- 側邊欄：全功能設定區 ---
with st.sidebar:
    st.title("⚙️ 寫作設定")
    
    # 1. 作文題目
    essay_title = st.text_input("📍 作文題目", value="我的生活點滴")
    
    st.divider()
    
    # 2. 七大元素管理 (內容讓使用者自行新增)
    st.subheader("💎 我的七大特色元素")
    element_options = ["1.圍棋", "2.程式設計", "3.樂高", "4.運動", "5.過動", "6.昆蟲", "7.鋼琴"]
    selected_el = st.selectbox("選擇要編輯/參考的元素", element_options)
    
    # 這裡讓使用者輸入該元素的 7 個內容
    # 使用 session_state 來暫時記住輸入的內容
    el_content = st.text_area(f"編輯【{selected_el}】的 7 個內容 (每行一個)", 
                             placeholder="內容 1\n內容 2\n內容 3\n...",
                             height=200,
                             key=f"content_{selected_el}")

    st.divider()

    # 3. 成語自定義
    st.subheader("📖 挑戰成語 (自行輸入)")
    idioms = []
    for i in range(4):
        idioms.append(st.text_input(f"段落 {i+1} 成語", key=f"idiom_{i}"))

# --- 主畫面 ---
st.title("🎙️ 語音寫作教練")

# 4. 語音上傳與辨識
st.subheader("第一步：語音輸入")
col_audio, col_text = st.columns([1, 1])

with col_audio:
    uploaded_file = st.file_uploader("上傳語音檔 (mp3/wav/m4a)", type=["mp3", "wav", "m4a"])
    if uploaded_file is not None:
        st.audio(uploaded_file, format='audio/wav')
        st.success("語音上傳成功！")

with col_text:
    raw_input = st.text_area("或者直接在此輸入語音辨識後的文字：", 
                            height=200, 
                            placeholder="請在此處編輯或貼上您的故事內容...",
                            key="main_input")

# 5. 修飾與產出
if st.button("🚀 執行微修飾並直排產出"):
    if raw_input:
        # 微修飾邏輯：去除贅字
        fillers = ["然後", "那個", "呃", "啊", "呢", "喔", "就是說", "那"]
        refined_text = raw_input
        for f in fillers:
            refined_text = refined_text.replace(f, "")
        
        # 顯示區
        st.divider()
        res_col1, res_col2 = st.columns([1, 9])
        
        with res_col1:
            st.markdown(f'<div class="title-display">{essay_title}</div>', unsafe_allow_html=True)
            
        with res_col2:
            st.markdown(f'<div class="vertical-text-container">{refined_text}</div>', unsafe_allow_html=True)
        
        # 檢查成語
        used_idioms = [i for i in idioms if i and i in refined_text]
        if used_idioms:
            st.balloons()
            st.success(f"✅ 達成成語任務：{', '.join(used_idioms)}")
    else:
        st.warning("請先提供內容或上傳語音喔！")

# 顯示目前選定元素的備忘錄
if el_content:
    with st.expander("💡 靈感提取備忘錄"):
        st.write(f"**當前元素：{selected_el}**")
        for line in el_content.split('\n'):
            if line.strip():
                st.write(f"- {line}")
