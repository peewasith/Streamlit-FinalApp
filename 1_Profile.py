import streamlit as st

st.set_page_config(page_title="Profile", page_icon="🥬", layout="wide")

# =============================
# CSS Pastel Theme + Card + Modern Header
# =============================
st.markdown(
    """
    <style>
    /* พื้นหลังหลัก */
    .main {
        background-color: #F7E9D7; /* Pastel Cream */
        color: #000000;
    }
    /* Card ของ Section */
    .card {
        background-color: #FFF4E1; /* Pastel Light */
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        color: #000000;
    }
    /* Header Box สำหรับ Profile */
    .header-box {
        background-color: #FFF4E1;
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 8px 30px rgba(0,0,0,0.15);
        margin-bottom: 40px;
    }
    .header-box h1 {
        margin: 0;
        font-size: 48px;
        color: #000000;
        font-family: 'Arial Black', sans-serif;
        letter-spacing: 2px;
    }
    /* ปุ่มสวยทันสมัย */
    .stButton>button {
        background-color: #FFA07A; /* Salmon Pastel */
        color: #000000;
        font-size: 16px;
        border-radius: 12px;
        padding: 10px 20px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #FFB347; /* Orange Pastel */
        transform: scale(1.05);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =============================
# Modern Header
# =============================
st.markdown(
    """
    <div class="header-box">
        <h1>🥬 PROFILE 🥬</h1>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    '<p style="text-align:center; color:#000000; font-size:16px;">Email: je_peewasith_st@tni.ac.th | Tel: 093-023-2033 </p>',
    unsafe_allow_html=True
)

# =============================
# Card แนะนำตัว
# =============================
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<h2>ข้อมูลส่วนตัว</h2>', unsafe_allow_html=True)
st.markdown("""
- ชื่อ–สกุล: นายพีวสิษฐ์ จีนเพ็ชร
- คณะ: เทคโนโลยีสารสนเทศ
- สาขา: เทคโนโลยีสารสนเทศทางธุรกิจดิจิทัล
- รหัสนักศึกษา: 2213310341
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# =============================
# Card ความสนใจ & ประสบการณ์
# =============================
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<h2>ความสนใจและประสบการณ์</h2>', unsafe_allow_html=True)
st.markdown("""
- ความสนใจ: Data Science, Data Mining และ Visualization
- ประสบการณ์: ทำโปรเจกต์เกี่ยวกับการสร้าง Ai ในการช่วยตัดสินใจต่างๆ เช่น ทำนายรุ่น Samsung ที่เหมาะสมกับคุณ, ทำการสอน Ai ให้เรียนรู้ว่าภาพไหนคืออะไร เช่น ทำนายรูปสัตว์ 
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# =============================
# Card Skillset
# =============================
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<h2>Skillset</h2>', unsafe_allow_html=True)
st.markdown("""
- Python, SQL, Streamlit
- Visualization Tools: Matplotlib, Seaborn, Plotly
- Machine Learning: scikit-learn
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)