import streamlit as st
from Chapter03Streamlit import *
from Chapter04Streamlit import *
from Chapter05Streamlit import *
from Chapter09Streamlit import *

def AllChapterUI():
    # Thêm CSS để tùy chỉnh giao diện
    st.markdown("""
    <style>
    /* Nhập phông chữ Poppins */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');


    /* Nội dung chính */
    .main .block-container {
        background: white;
        border-radius: 12px;
        padding: 40px;
        margin: 20px;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.1);
    }

    /* Tiêu đề chính */
    #main-header {
        color: #F0F8FF;
        font-size: 3.5em;
        text-align: center;
        margin-bottom: 30px;
        font-weight: 700;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    /* Tabs */
    .stTabs [role="tablist"] {
        background: #ecf0f1;
        border-radius: 10px;
        padding: 10px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }

    .stTabs [role="tab"] {
        background: #3498db;
        color: white;
        border-radius: 8px;
        padding: 12px 24px;
        margin: 0 5px;
        font-weight: 500;
        transition: all 0.3s ease;
        cursor: pointer;
    }

    .stTabs [role="tab"]:hover {
        background: #2980b9;
        transform: translateY(-2px);
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
    }

    .stTabs [role="tab"][aria-selected="true"] {
        background: #00e676;
        color: #fff;
        box-shadow: 0 0 12px rgba(0, 230, 118, 0.5);
    }

   
    </style>
    """, unsafe_allow_html=True)

    # Thiết lập tiêu đề chính với id
    st.markdown('<h1 id="main-header">All Chapter</h1>', unsafe_allow_html=True)

    # Thiết lập tabs với id cho container
    tab1, tab2, tab3, tab4 = st.tabs(["Chapter03", "Chapter04", "Chapter05", "Chapter09"])

    # Nội dung các tab với id chung cho container nội dung
    with tab1:
        st.markdown('<div id="tab-content">', unsafe_allow_html=True)
        Chapter3StreamlitUI()
        st.markdown('</div>', unsafe_allow_html=True)
    with tab2:
        st.markdown('<div id="tab-content">', unsafe_allow_html=True)
        Chapter4StreamlitUI()
        st.markdown('</div>', unsafe_allow_html=True)
    with tab3:
        st.markdown('<div id="tab-content">', unsafe_allow_html=True)
        Chapter5StreamlitUI()
        st.markdown('</div>', unsafe_allow_html=True)
    with tab4:
        st.markdown('<div id="tab-content">', unsafe_allow_html=True)
        Chapter9StreamlitUI()
        st.markdown('</div>', unsafe_allow_html=True)

