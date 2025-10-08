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
# CSS Theme (Pastel Cream + Modern Buttons without underline)
# ==============================
st.markdown(
    """
    <style>
    /* Background and general text */
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

    /* Card Style */
    .card {
        background-color: #FFF4E1;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 8px 8px 24px rgba(0,0,0,0.06), -8px -8px 24px rgba(255,255,255,0.5);
        margin-bottom: 20px;
        text-align: center;
        transition: transform 0.3s ease;
    }
    .card:hover {
        transform: translateY(-5px);
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

    /* Modern Glass Buttons without underline */
    .link-button {
        background: rgba(255, 248, 231, 0.8); /* Semi-transparent cream */
        color: #333333;
        border: 2px solid rgba(200,200,200,0.3);
        padding: 14px 28px;
        border-radius: 20px;
        font-size: 16px;
        font-weight: bold;
        cursor: pointer;
        transition: all 0.4s ease;
        text-decoration: none; /* Remove underline */
        display: inline-block;
        margin-top: 10px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.08), 0 0 10px rgba(255,255,255,0.3);
        backdrop-filter: blur(8px);
    }
    .link-button:hover {
        background: rgba(255, 248, 231, 1);
        box-shadow: 0 12px 28px rgba(0,0,0,0.12), 0 0 20px rgba(255,255,255,0.5);
        transform: scale(1.08);
        color: #222222;
        text-decoration: none; /* Ensure no underline on hover */
    }
    .link-button:focus {
        outline: none;
        text-decoration: none; /* Remove underline on click/focus */
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
# Project Overview Cards
# ==============================
st.markdown("---")
st.markdown("## 🔹 Project Overview", unsafe_allow_html=True)

projects = [
    {
        "title": "🥬 Profile",
        "description": "ข้อมูลส่วนตัวและ Mini Project \nประสบการณ์และการวิเคราะห์ข้อมูลเบื้องต้น",
        "url": "https://profile-wpynhxgkiogzasua4wgw6w.streamlit.app/"
    },
    {
        "title": "📺 YouTube Analysis",
        "description": "วิเคราะห์ข้อมูลจาก YouTube เช่น จำนวนผู้ชม ความนิยม\nแสดง Insight ที่สามารถนำไปต่อยอดได้",
        "url": "https://youtube-r8zgz3xwymqrumrjg9tjjk.streamlit.app/"
    },
    {
        "title": "📱 Samsung Prediction",
        "description": "สร้างโมเดล Machine Learning เพื่อทำนายรุ่น Samsung ที่เหมาะสม\nต่อยอดเป็น Recommendation System",
        "url": "https://samsungfinal-snzzb7rvkmxv2b9pnnp2v4.streamlit.app/"
    },
    {
        "title": "🐾 Animal Classifier",
        "description": "สาธิตการประยุกต์ใช้ AI Classification สำหรับรูปสัตว์\nทดสอบการจำแนกรูปภาพแบบ Deep Learning (VGG16)",
        "url": "https://7bbbzkxrabjl8jsiabbfwp.streamlit.app/"
    }
]

cols = st.columns(2)
for i, project in enumerate(projects):
    with cols[i % 2]:
        st.markdown(
            f"""
            <div class="card">
                <h3>{project['title']}</h3>
                <p>{project['description'].replace('\n','<br>')}</p>
                <a class="link-button" href="{project['url']}" target="_blank">View Project</a>
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
        <a class="link-button" href="https://7bbbzkxrabjl8jsiabbfwp.streamlit.app/" target="_blank">🐾 เปิด Animal Classifier</a>
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown("---")
st.markdown("## 🌟 Key Highlights", unsafe_allow_html=True)

st.markdown(
    """
    <div class="card">
        <h3>เทคโนโลยีที่ใช้</h3>
        <p>- Streamlit สำหรับ Web-based UI / Dashboard 
        , TensorFlow / Keras สำหรับ Deep Learning (Image Classification)
        , Machine Learning โมเดลหลายแบบ (Decision Tree, Random Forest)  
        , Transfer Learning กับ Pretrained Model (VGG16) 
        , Data Preprocessing, Evaluation Metrics และ Visualization</p>
    </div>
    """,
    unsafe_allow_html=True
)





