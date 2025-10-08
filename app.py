import streamlit as st

# =============================
# ตั้งค่าหน้า
# =============================
st.set_page_config(page_title="Data Science Mini Project", page_icon="📊", layout="wide")

# =============================
# CSS Pastel Theme
# =============================
st.markdown(
    """
    <style>
    .main {
        background-color: #FFF8E7; /* Pastel Cream Background */
        color: #333;
    }
    .header-box {
        background-color: #FFF4E1;
        padding: 40px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 8px 30px rgba(0,0,0,0.1);
        margin-bottom: 40px;
    }
    .header-box h1 {
        margin: 0;
        font-size: 42px;
        color: #333;
        font-family: 'Arial Black', sans-serif;
    }
    .header-box p {
        font-size: 18px;
        color: #555;
    }
    .button-card {
        background-color: #FFF4E1;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        text-align: center;
        margin-bottom: 20px;
    }
    .button-card a button {
        background-color:#FFA07A;
        color:#000;
        border:none;
        padding:12px 24px;
        border-radius:12px;
        font-size:16px;
        cursor:pointer;
        transition: all 0.3s ease;
    }
    .button-card a button:hover {
        background-color:#FFB347;
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
        <h1>📊 Data Science Mini Project Showcase</h1>
        <p>เว็บไซต์นี้รวบรวมผลงาน Mini Project ของนักศึกษา พร้อมตัวอย่างการประยุกต์ใช้งานจริง</p>
    </div>
    """,
    unsafe_allow_html=True
)

# =============================
# ปุ่มไปแต่ละหน้า
# =============================
st.markdown("---")

st.markdown("""
    <a href="https://your-streamlit-profile-link" target="_blank" class="link-button">👤 Profile</a>
    <a href="https://your-streamlit-youtube-link" target="_blank" class="link-button">📺 YouTube Analysis</a>
    <a href="https://your-streamlit-samsung-link" target="_blank" class="link-button">📱 Samsung Prediction</a>
    <a href="https://animal-classifier-na5hzbrtutdzzvjz7wuxv5.streamlit.app/" target="_blank" class="link-button">🐾 Animal Classifier</a>
""", unsafe_allow_html=True)


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




