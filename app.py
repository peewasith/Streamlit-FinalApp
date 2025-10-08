import streamlit as st

# ==============================
# Page Config
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
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        margin-bottom: 20px;
        text-align: center;
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
    .stButton>button {
        background-color: #FFA07A;
        color: #000000;
        font-size: 16px;
        border-radius: 12px;
        padding: 12px 24px;
        margin-top: 10px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #FFB347;
        transform: scale(1.05);
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

st.markdown("---")

# ==============================
# Navigation Cards
# ==============================
st.markdown("## 🔹 เลือกหน้าเพื่อเข้าถึงโปรเจกต์", unsafe_allow_html=True)

# ใช้ 2 คอลัมน์สำหรับวางปุ่มสวย ๆ
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("<h3>👤 Profile</h3>", unsafe_allow_html=True)
    st.markdown("<p>ดูข้อมูลผู้จัดทำและโปรไฟล์โครงการ</p>", unsafe_allow_html=True)
    if st.button("เปิด Profile"):
        st.switch_page("1_Profile")  # ต้องตรงกับชื่อไฟล์ใน pages/
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("<h3>📺 YouTube Analysis</h3>", unsafe_allow_html=True)
    st.markdown("<p>สาธิตการวิเคราะห์ข้อมูลจาก YouTube</p>", unsafe_allow_html=True)
    if st.button("เปิด YouTube Analysis"):
        st.switch_page("2_YouTube")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("<h3>📱 Samsung Prediction</h3>", unsafe_allow_html=True)
    st.markdown("<p>สาธิตการทำนายสมาร์ทโฟน Samsung จากโมเดล</p>", unsafe_allow_html=True)
    if st.button("เปิด Samsung Prediction"):
        st.switch_page("3_Samsung")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("<h3>🐾 Animal Classifier</h3>", unsafe_allow_html=True)
    st.markdown("<p>สาธิตการจำแนกรูปสัตว์ด้วย AI</p>", unsafe_allow_html=True)
    st.markdown(
        '<a href="https://animal-classifier-na5hzbrtutdzzvjz7wuxv5.streamlit.app/" target="_blank">'
        '<button style="background-color:#FFA07A;color:#000000;border:none;padding:12px 24px;'
        'border-radius:12px;font-size:16px;cursor:pointer;">เปิด Animal Classifier</button>'
        '</a>',
        unsafe_allow_html=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

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



