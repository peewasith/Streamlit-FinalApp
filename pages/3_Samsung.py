import streamlit as st

st.set_page_config(page_title="Samsung Mini Project", page_icon="📱", layout="wide")

# =============================
# CSS Pastel Theme
# =============================
st.markdown(
    """
    <style>
    .main {
        background-color: #F7E9D7; /* Pastel Cream */
        color: #000000;
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
        color: #000000;
        font-family: 'Arial Black', sans-serif;
        letter-spacing: 1px;
    }
    .stButton>button {
        background-color: #FFA07A;
        color: #000000;
        font-size: 16px;
        border-radius: 12px;
        padding: 10px 20px;
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

# =============================
# Header
# =============================
st.markdown(
    """
    <div class="header-box">
        <h1>📱 Samsung Mini Project</h1>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    '<p style="text-align:center; font-size:16px;">โครงการ Machine Learning สำหรับการจำแนกรุ่น Samsung</p>',
    unsafe_allow_html=True
)

# =============================
# Section 1: Business & Motivation
# =============================
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("### 💼 Business & ความน่าสนใจของ Project", unsafe_allow_html=True)
st.markdown(
    """
    ตลาดสมาร์ทโฟนของ **Samsung** มีรุ่นหลากหลาย ทำให้ผู้บริโภคมักสับสนว่าจะเลือกรุ่นใดให้ตรงกับความต้องการ  
    โปรเจกต์นี้จึงมุ่งเน้นการสร้าง **Model Classification** เพื่อช่วยแนะนำสมาร์ทโฟนที่เหมาะสม  
    โดยสามารถนำไปต่อยอดในการทำ **Recommendation System** สำหรับผู้ใช้งานจริง
    """,
    unsafe_allow_html=True
)
st.markdown('</div>', unsafe_allow_html=True)

# =============================
# Section 2: Data Source
# =============================
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("### 📂 Data Source", unsafe_allow_html=True)
st.markdown(
    """
    - ข้อมูลถูกจัดเก็บและสร้างขึ้นเพื่อการศึกษา โดยอ้างอิงจากคุณสมบัติสมาร์ทโฟน Samsung  
    - Dataset ถูกเตรียมในรูปแบบ `.pkl` เพื่อความสะดวกในการโหลดเข้าสู่โมเดล Machine Learning  
    - [🔗 ดู Dataset ที่ใช้จริง](https://colab.research.google.com/drive/1DbLJegR4PemwXeZH0Pl3iOGyRrt-AcZE)
    """,
    unsafe_allow_html=True
)
st.markdown('</div>', unsafe_allow_html=True)

# =============================
# Section 3: Data Preprocessing
# =============================
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("### 🧹 Data Preprocessing", unsafe_allow_html=True)
st.markdown(
    """
    - ทำการแปลงข้อมูลให้อยู่ในรูปแบบที่เหมาะสมต่อการนำไปเทรนโมเดล  
    - จัดการ Missing Values และการเข้ารหัสข้อมูล (Encoding)  
    - แบ่งข้อมูลออกเป็น Training และ Testing set
    """,
    unsafe_allow_html=True
)
st.markdown('</div>', unsafe_allow_html=True)

# =============================
# Section 4: Model Training
# =============================
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("### 🤖 Model Training", unsafe_allow_html=True)
st.markdown(
    """
    ใช้โมเดล Machine Learning หลายรูปแบบ เช่น:  
    - Decision Tree  
    - Random Forest  
    - Logistic Regression  

    จากนั้นวัดผลเพื่อเลือกโมเดลที่ให้ผลลัพธ์ดีที่สุด
    """,
    unsafe_allow_html=True
)
st.markdown('</div>', unsafe_allow_html=True)

# =============================
# Section 5: Evaluation
# =============================
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("### 📊 Evaluation", unsafe_allow_html=True)
st.markdown(
    """
    ทำการประเมินโมเดลด้วย Metric หลัก ได้แก่:  
    - Accuracy  
    - Precision  
    - Recall  
    - F1-score  
    - Confusion Matrix  
    - ROC-AUC  

    ผลลัพธ์ที่ได้ชี้ให้เห็นว่าโมเดล **Random Forest** มีประสิทธิภาพดีที่สุด
    """,
    unsafe_allow_html=True
)
st.markdown('</div>', unsafe_allow_html=True)

# =============================
# Section 6: Conclusion
# =============================
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("### ✅ Conclusion & ข้อเสนอแนะ", unsafe_allow_html=True)
st.markdown(
    """
    โปรเจกต์นี้แสดงให้เห็นถึงศักยภาพของ Machine Learning ในการช่วยผู้ใช้เลือกสมาร์ทโฟน Samsung  
    ในอนาคตสามารถต่อยอดไปสู่ **AI-based Recommendation System**  
    เพื่อช่วยแนะนำรุ่นโทรศัพท์ที่เหมาะสมยิ่งขึ้นสำหรับผู้บริโภค
    """,
    unsafe_allow_html=True
)
st.markdown('</div>', unsafe_allow_html=True)

# =============================
# Section 7: Link to App
# =============================
st.markdown('<div class="card" style="text-align:center;">', unsafe_allow_html=True)
st.markdown("### 🌐 ทดลองใช้งานจริง", unsafe_allow_html=True)

if st.button("ไปที่ Samsung App"):
    st.markdown("[คลิกที่นี่เพื่อเปิดแอป Samsung Mini Project](https://samsung-miniproject-ndicmquba2ihbcpnbitiss.streamlit.app/)", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
