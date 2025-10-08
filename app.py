import streamlit as st

# =============================
# หน้า App หลัก
# =============================
st.set_page_config(
    page_title="Animal Classifier Showcase",
    page_icon="🐾",
    layout="wide"
)

# =============================
# CSS Pastel Theme
# =============================
st.markdown(
    """
    <style>
    .main {
        background-color: #FFF8E7; /* Pastel cream */
        color: #000000;
        padding: 30px;
    }
    .card {
        background-color: #FFF4E1;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        color: #000000;
    }
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
        font-size: 42px;
        color: #333;
        font-family: 'Arial Black', sans-serif;
        letter-spacing: 1px;
    }
    .btn-link {
        display: block;
        background-color: #FFA07A;
        color: #000;
        text-align: center;
        padding: 15px 25px;
        border-radius: 12px;
        font-size: 18px;
        font-weight: bold;
        text-decoration: none;
        transition: all 0.3s ease;
        margin-bottom: 15px;
    }
    .btn-link:hover {
        background-color: #FFB347;
        transform: scale(1.05);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =============================
# Header
# =============================
st.markdown(
    """
    <div class="header-box">
        <h1>🐾 Animal Classifier Mini Project</h1>
        <p style="font-size:18px; color:#555;">
            เว็บไซต์นี้สาธิตการประยุกต์ใช้ AI Classification
            ผ่าน Streamlit พร้อม Data, Model, และ Evaluation
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# =============================
# ปุ่มลิงก์ไปแต่ละหน้า
# =============================
st.markdown('<div class="card" style="text-align:center;">', unsafe_allow_html=True)

st.markdown("### 🔗 ไปยังแต่ละหน้าโปรเจกต์", unsafe_allow_html=True)

# เพิ่มปุ่มลิงก์ (URL ต้องตรงกับ GitHub หรือที่อัปโหลดไว้)
pages = {
    "👤 Profile": "https://your-github-link.com/1_Profile.py",
    "📺 YouTube Analysis": "https://your-github-link.com/2_YouTube.py",
    "📱 Samsung Prediction": "https://your-github-link.com/3_Samsung.py"
}

for name, link in pages.items():
    st.markdown(f'''
        <a href="{link}" target="_blank" class="btn-link">{name}</a>
    ''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# =============================
# ตัวอย่างการใช้งานจริง
# =============================
st.markdown(
    """
    <div class="card" style="text-align:center;">
        <h3>ทดลองใช้งานโปรเจกต์จริง</h3>
        <p>คลิกเพื่อเปิด Animal Classifier App และดูการทำงานจริง</p>
        <a href="https://animal-classifier-na5hzbrtutdzzvjz7wuxv5.streamlit.app/" target="_blank">
        <button style="background-color:#FFA07A;color:#000000;border:none;padding:12px 24px;
        border-radius:12px;font-size:16px;cursor:pointer;">🐾 เปิดแอป Animal Classifier</button>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)


