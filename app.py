import streamlit as st
import facedetectionstreamlit as fd
import home
import chapter
import SeparateBackgourd 
import FruitRecognization
import VehicleRecognization


# Thiết lập cấu hình trang
st.set_page_config(page_title="Xử lí ảnh số", layout="wide")

# CSS tùy chỉnh
def local_css():
    st.markdown("""
    <style>
    /* Tổng thể */
    .stApp {
        font-family: 'Arial', sans-serif;
    }

    /* Sidebar */
    .css-1d391kg {
        background-color: #2c3e50;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    
    .css-1d391kg .stSelectbox, .css-1d391kg .stSlider {
        background-color: #34495e;
        color: white;
        border-radius: 8px;
        padding: 10px;
    }
    
    .css-1d391kg .stSelectbox > div > div > div {
        color: white !important;
    }
    
    .css-1d391kg label {
        color: #ecf0f1 !important;
        font-weight: bold;
    }
    
    /* Nội dung chính */
    .main .block-container {
        background-color: white;
        border-radius: 10px;
        padding: 30px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-top: 20px;
    }
    
    h1, h2, h3 {
        color: #2c3e50;
    }
    
    .stButton>button {
        background-color: #3498db;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
        border: none;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background-color: #2980b9;
        transform: translateY(-2px);
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .css-1d391kg {
            padding: 15px;
        }
        .main .block-container {
            padding: 20px;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# Áp dụng CSS
local_css()

# Sidebar
with st.sidebar:
    st.header("Bảng Điều Khiển")
    option = st.selectbox("Chọn danh mục", ["Trang chủ", 
                                            "Face Recognization", 
                                            "Fruit Recognization", 
                                            "All Chapter", 
                                            "Background Removal", 
                                            "Vehicle Recognization"])



if option == "Trang chủ":
    home.home()
elif option == "Face Recognization":
    fd.streamlit()
elif option == "Fruit Recognization":
    FruitRecognization.FruitRecognization()
elif option == "All Chapter":
    chapter.AllChapterUI()
elif option == "Background Removal":
    SeparateBackgourd.SepareateBackground()
elif option == "Vehicle Recognization":
    VehicleRecognization.VehicleRecognization()
