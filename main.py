import streamlit as st
import db
from streamlit_cookies_controller import CookieController
import time

controller = CookieController()

if not (controller.get("username") and controller.get("role")):

    st.title("เข้าสู่ระบบ")

    tab1, tab2, tab3 = st.tabs(["นักสึกษา", "อาจารย์", "ผู้ดูแลระบบ"])

    with tab1:
        with st.form("student_form"):
            username = st.text_input("username")
            password = st.text_input("password", type="password")
            
            if st.form_submit_button("เข้าสู่ระบบ", type="primary"):
                user = db.fetch_one(
                    "SELECT * FROM students WHERE student_id = %s AND idcard = %s",
                    (username, password)
                )
                if not user:
                    st.error("รหัสไม่ถูกต้อง")
                else:
                    st.success("เข้าสู่ระบบสำเร็จ!")
                    controller.set("username", username)
                    controller.set("role", "student")
                    time.sleep(1.5)
                    st.rerun()
                    
    
                    
    with tab3:
        with st.form("admin_form"):
            username = st.text_input("username")
            password = st.text_input("password", type="password")
            
            if st.form_submit_button("เข้าสู่ระบบ", type="primary"):
                if username == "admin" and password == "123456":
                    st.success("เข้าสู่ระบบสำเร็จ!")
                    controller.set("username", username)
                    controller.set("role", "student")
                    time.sleep(1.5)
                    st.rerun()
                else:
                    st.error("รหัสไม่ถูกต้อง")

else:
    st.set_page_config(layout="wide")
    
    pg = st.navigation([st.Page("_pages/home.py"), st.Page("_pages/students.py"), st.Page("_pages/teachers.py"), st.Page("_pages/departments.py"), st.Page("_pages/schedules.py")], position="hidden")
    pg.run()
    
    with st.sidebar:
        st.page_link(page=st.Page("_pages/home.py") ,label="หน้าแรก", icon=":material/home:")
        st.page_link(page=st.Page("_pages/students.py") ,label="นักศึกษา", icon=":material/people:")
        st.page_link(page=st.Page("_pages/teachers.py") ,label="อาจารย์", icon=":material/people:")
        st.page_link(page=st.Page("_pages/departments.py") ,label="แผนกวิชา", icon=":material/home:")
        st.page_link(page=st.Page("_pages/schedules.py") ,label="ตาราง", icon=":material/home:")

    

