import streamlit as st

# ==============================
# ตั้งค่า Page
# ==============================
st.set_page_config(
    page_title="Data Science Mini Project Showcase",
    page_icon="📊",
    layout="wide"
)

# ==============================
# CSS Theme (Pastel Cream)
# ==============================
st.markdown(
    """
    <style>
    .main {
        background-color: #FFF8E7; /* Pastel Cream */
        color: #000000;
    }
    .hero-box {
        background-color: #FFF4E1;
        padding: 50px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 8px 30px rgba(0,0,0,0.12);
        margin-bottom: 50px;
    }
    .hero-box h1 {
        margin: 0;
        font-size: 48px;
        color: #333333;
        font-family: 'Arial Black', sans-serif;
    }
    .hero-box p {
        margin-top: 15px;
        font-size: 18px;
        color: #555555;
    }
    .card {
        background-color: #FFF4E1;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        margin-bottom: 20px;
    }
    .card h3 {
        margin-top: 0;
        font-size: 24px;
        color: #333333;
    }
    .card p {
        font-size: 16px;
        color: #555555;
    }
    .page-links {
        display: flex;
        justify-content: center;
        gap: 20px;
        flex-wrap: wrap;
        margin-top: 30px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ==============================
# Hero Section
# ==============================
st.markdown(
    """
    <div class="hero-box">
        <h1>📊 Data Science Mini Project Showcase</h1>
        <p>เว็บไซต์นี้รวบรวมผลงาน Mini Project ด้าน Data Science และ Machine Learning  
        แสดงตัวอย่างการประยุกต์ใช้ AI และการทำงานจริงผ่าน Streamlit App</p>
    </div>
    """,
    unsafe_allow_html=True
)

# ==============================
# 🔗 Project Navigation Links
# ==============================
st.markdown("## 🚀 Explore Each Project", unsafe_allow_html=True)
st.markdown('<div class="page-links">', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

st.page_link("1_Profile.py", label="👤 Profile", icon="📄")
st.page_link("2_Youtube.py", label="🎥 YouTube Analysis", icon="📊")
st.page_link("3_Samsung.py", label="📱 Samsung Prediction", icon="📱")
st.page_link("4_Final.py", label="🐾 Animal Classifier", icon="🐾")
st.markdown('</div>', unsafe_allow_html=True)

# ==============================
# Project Overview
# ==============================
st.markdown("---")
st.markdown("## 🔹 Project Overview", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        <div class="card">
            <h3>🥬 Profile</h3>
            <p>ข้อมูลส่วนตัวและ Mini Project ของผู้ทำ  
            แสดงประสบการณ์และการวิเคราะห์ข้อมูลเบื้องต้น</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <div class="card">
            <h3>📺 YouTube Analysis</h3>
            <p>วิเคราะห์ข้อมูลจาก YouTube เช่น จำนวนผู้ชม ความนิยม  
            และแสดง Insight ที่สามารถนำไปต่อยอดได้</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="card">
            <h3>📱 Samsung Prediction</h3>
            <p>สร้างโมเดล Machine Learning เพื่อทำนายรุ่น Samsung ที่เหมาะสม  
            ต่อยอดเป็น Recommendation System</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <div class="card">
            <h3>🐾 Animal Classifier</h3>
            <p>สาธิตการประยุกต์ใช้ AI Classification สำหรับรูปสัตว์</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# ==============================
# Key Highlights
# ==============================
st.markdown("---")
st.markdown("## 🌟 Key Highlights", unsafe_allow_html=True)
st.markdown(
    """
    <div class="card">
        <h3>เทคโนโลยีที่ใช้</h3>
        <p>- Streamlit สำหรับ Web-based UI / Dashboard  
        - TensorFlow / Keras สำหรับ Deep Learning (Image Classification)  
        - Machine Learning โมเดลหลายแบบ (Decision Tree, Random Forest)  
        - Transfer Learning กับ Pretrained Model (VGG16)  
        - Data Preprocessing, Evaluation Metrics และ Visualization</p>
    </div>
    """,
    unsafe_allow_html=True
)

# ==============================
# Footer / CTA
# ==============================
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



