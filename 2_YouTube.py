import streamlit as st

st.set_page_config(page_title="YouTube Data Analysis", page_icon="🎥", layout="wide")

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
        <h1>🎥 YouTube Data Analysis</h1>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    '<p style="text-align:center; font-size:16px;">การวิเคราะห์ข้อมูล YouTube: การทำความสะอาดข้อมูล, EDA, Visualization และ Insight</p>',
    unsafe_allow_html=True
)

# =============================
# Section 1: บทนำ
# =============================
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("### 📌 บทนำ", unsafe_allow_html=True)
st.markdown(
    """
    โครงการนี้เป็นการวิเคราะห์ข้อมูล YouTube Trending โดยมีเป้าหมายเพื่อทำความเข้าใจปัจจัยที่ส่งผลต่อความนิยมของวิดีโอ  
    เรามุ่งเน้นไปที่ **จำนวนการเข้าชม (Views)**, **จำนวนการกดถูกใจ (Likes)** และ **จำนวนความคิดเห็น (Comments)**  
    เพื่อนำไปสู่การสรุป Insight ที่เป็นประโยชน์ต่อผู้สร้างคอนเทนต์
    """,
    unsafe_allow_html=True
)
st.markdown('</div>', unsafe_allow_html=True)

# =============================
# Section 2: Data Cleaning & EDA
# =============================
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("### 🧹 Data Cleaning & EDA", unsafe_allow_html=True)
st.markdown(
    """
    - ทำการลบ Missing Values และค่าที่ไม่สมเหตุสมผล  
    - วิเคราะห์ Exploratory Data Analysis (EDA)  
      - ความสัมพันธ์ระหว่าง Views, Likes และ Comments  
      - จำนวนวิดีโอตามหมวดหมู่  
      - ความถี่ของการอัปโหลด  
    """,
    unsafe_allow_html=True
)
st.markdown('</div>', unsafe_allow_html=True)

# =============================
# Section 3: Visualization
# =============================
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("### 📊 Visualization", unsafe_allow_html=True)
st.markdown(
    """
    เราได้สร้างกราฟเพื่อนำเสนอความสัมพันธ์และรูปแบบที่น่าสนใจ เช่น  
    - Bar Chart แสดงจำนวนวิดีโอตามประเภทคอนเทนต์  
    - Scatter Plot ระหว่าง Views และ Likes  
    - Line Chart แสดงแนวโน้มการมีส่วนร่วมของผู้ชม  
    """,
    unsafe_allow_html=True
)
st.markdown('</div>', unsafe_allow_html=True)

# =============================
# Section 4: Insight
# =============================
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("### 💡 Insight", unsafe_allow_html=True)
st.markdown(
    """
    - วิดีโอที่มี **ความยาวปานกลาง** มักได้รับ Engagement สูงกว่า  
    - คอนเทนต์ประเภท **Music และ Entertainment** มีแนวโน้มได้รับ Views มากที่สุด  
    - การอัปโหลดถี่เกินไปอาจไม่ช่วยเพิ่ม Engagement อย่างมีนัยสำคัญ  
    """,
    unsafe_allow_html=True
)
st.markdown('</div>', unsafe_allow_html=True)

# =============================
# Section 5: Link to Full Analysis
# =============================
st.markdown('<div class="card" style="text-align:center;">', unsafe_allow_html=True)
st.markdown("### 🔗 รายละเอียดเพิ่มเติม", unsafe_allow_html=True)
st.markdown("สามารถอ่านรายละเอียดการวิเคราะห์ทั้งหมดได้ที่ลิงก์ด้านล่าง:", unsafe_allow_html=True)

if st.button("ไปที่ Notion Analysis"):
    st.markdown("[เปิดลิงก์การวิเคราะห์ใน Notion](https://prepared-pheasant.super.site/)", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)