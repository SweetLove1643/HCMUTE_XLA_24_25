import streamlit as st
from Chapter03Streamlit import *

# Thêm CSS để tùy chỉnh sidebar
st.markdown("""
<style>
/* Tùy chỉnh sidebar */
.sidebar .sidebar-content {
    background-color: #2c2c2c;
    border-right: 1px solid #00e676;
    box-shadow: 0 0 10px rgba(0, 230, 118, 0.3);
}

/* Tùy chỉnh tiêu đề trong sidebar */
.sidebar .sidebar-content h3 {
    color: #00e676;
    font-size: 1.8em;
    text-align: center;
    margin: 20px 0;
    text-shadow: 0 0 8px rgba(0, 230, 118, 0.5);
}

/* Tùy chỉnh selectbox trong sidebar */
.sidebar .stSelectbox > div > div {
    background-color: #333333;
    border: 1px solid #00e676;
    border-radius: 6px;
    padding: 12px;
    margin: 10px 0;
    transition: all 0.3s ease;
}
.sidebar .stSelectbox > div > div:hover {
    background-color: #4a4a4a;
    box-shadow: 0 0 10px rgba(0, 230, 118, 0.5);
}

/* Tùy chỉnh nội dung chính */
.main .block-container {
    padding: 30px;
}

/* Tải phông chữ Poppins */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap');
</style>
""", unsafe_allow_html=True)

# Thiết lập sidebar
st.sidebar.header("Menu")
page = st.sidebar.selectbox("Chọn trang", ["Chapter03", "Chapter04", "Chapter05", "Chapter09"])

# Điều hướng đến trang tương ứng
if page == "Chapter03":
    Chapter3()
else:
    st.title("Trang Khác")