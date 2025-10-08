import streamlit as st

# =============================
# Page Config
# =============================
st.set_page_config(
    page_title="Final ML Project",
    page_icon="🚀",
    layout="wide"
)

# =============================
# CSS Pastel Theme
# =============================
st.markdown("""
<style>
.main {
    background-color: #F7E9D7; /* Pastel Cream */
    color: #000000;
    font-family: 'Arial', sans-serif;
}
.header-box {
    background-color: #FFF4E1;
    padding: 40px;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0 8px 30px rgba(0,0,0,0.15);
    margin-bottom: 50px;
}
.header-box h1 {
    margin: 0;
    font-size: 46px;
    color: #000000;
    font-family: 'Arial Black', sans-serif;
    letter-spacing: 1px;
}
.card {
    background-color: #FFF4E1;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.1);
    margin-bottom: 20px;
    color: #000000;
}
.card h2 {
    font-size: 26px;
    margin-bottom: 15px;
}
.card ul {
    padding-left: 20px;
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
""", unsafe_allow_html=True)

# =============================
# Header
# =============================
st.markdown("""
<div class="header-box">
    <h1>🚀 Final ML Project: AI Showcase</h1>
</div>
""", unsafe_allow_html=True)

st.markdown(
    '<p style="text-align:center; font-size:18px; margin-bottom:50px;">สาธิตการประยุกต์ใช้ AI Classification ผ่าน Streamlit พร้อม Data, Model, และ Evaluation</p>',
    unsafe_allow_html=True
)

# =============================
# Section 1: Project Overview
# =============================
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("### 📌 Project Overview", unsafe_allow_html=True)
st.markdown("""
ในหน้านี้เราจะแสดงตัวอย่างการประยุกต์ใช้ **AI Classification** บน **รูปภาพสัตว์** โดยใช้โมเดล **Deep Learning / Transfer Learning** เช่น VGG16 เพื่อจำแนกสัตว์หลายประเภท เช่น แมว สุนัข และนก ผู้ชมสามารถทดลองอัปโหลดรูปและทำนายผลได้ทันทีผ่าน **Streamlit App** โมเดลนี้สามารถนำไปประยุกต์ใช้ในงานจริงได้หลากหลาย เช่น การจำแนกประเภทสัตว์ในฟาร์มหรือสัตว์เลี้ยง และการวิเคราะห์ข้อมูลเชิงธุรกิจที่เกี่ยวข้องกับสัตว์ นอกจากนี้แนวคิดการสร้าง Classification Model และการประเมินผลต่อยอดจาก Mini Project Samsung จะช่วยให้เข้าใจวิธีพัฒนาโมเดลและนำไปใช้งานจริงได้อย่างมีประสิทธิภาพ
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# =============================
# Section 2: Libraries & Techniques
# =============================
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("### 📚 Libraries & Techniques", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.markdown("**Streamlit**")
    st.markdown("""
    - st.set_page_config(), st.markdown(), st.file_uploader()  
    - st.image(), st.progress(), st.caption(), st.info(), st.success()  
    - ใช้ทำ Web App / Dashboard แบบ interactive
    """)
    st.markdown("**TensorFlow / Keras**")
    st.markdown("""
    - model_from_json(), model.load_weights()  
    - image.load_img(), image.img_to_array(), np.expand_dims()  
    - ใช้ Pretrained Model / CNN / Transfer Learning
    """)
with col2:
    st.markdown("**Keras Applications – VGG16**")
    st.markdown("""
    - include_top=False → ใช้เป็น feature extractor  
    - vgg16.preprocess_input() → preprocessing ของภาพ
    """)
    st.markdown("**NumPy & gdown**")
    st.markdown("""
    - NumPy: จัดการ array ของภาพ  
    - gdown: ดาวน์โหลดไฟล์โมเดลจาก Google Drive
    """)
st.markdown('</div>', unsafe_allow_html=True)

# =============================
# Section 3: Demo & Link
# =============================
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("### 💻 Try the Model", unsafe_allow_html=True)
st.markdown("คุณสามารถทดลอง **Image Classification** ผ่านแอปจริงได้ที่ลิงก์ด้านล่าง:")
if st.button("ไปที่ Animal Classifier App"):
    st.markdown("[คลิกที่นี่เพื่อเปิดแอป](https://animal-classifier-na5hzbrtutdzzvjz7wuxv5.streamlit.app/)", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# =============================
# Section 4: Real World Benefit
# =============================
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("### 💡 Real World Benefit", unsafe_allow_html=True)
st.markdown("""
- ช่วย **ลดเวลาและแรงงาน** ในการจำแนกประเภทข้อมูล  
- ใช้ได้ในงานธุรกิจ, การศึกษา, การวิจัย และงานด้าน AI อื่นๆ  
- ทำให้สามารถ **ตัดสินใจเชิงข้อมูลได้เร็วขึ้น** และมีประสิทธิภาพมากขึ้น
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
