import streamlit as st
import db
import pandas as pd
import time

st.title("นักศึกษา")
st.write("จัดการข้อมูลนักศึกษา")
st.divider()

students = pd.DataFrame(db.query("SELECT * FROM students"))

csv = st.file_uploader("", type="csv")

if csv and st.button("นำเข้าข้อมูล"):
    st.success("นำเข้าข้อมูลเสร็จสิน")
    

editable = st.data_editor(students, column_config={
    'prefix': st.column_config.SelectboxColumn("คำนำหน้า", options=['นาย','นาง','นางสาว'])
})

if not editable.equals(students):
    if st.button("บันทึกการแก้ไข", type="primary"):
        for i, row in editable.iterrows():
            
            if not row.equals(students.loc[i]):
                db.execute(
                    """
                    UPDATE students SET
                            student_id = %s,
                            idcard = %s,
                            prefix = %s,
                            firstname = %s,
                            lastname = %s,
                            grade = %s,
                            group_id = %s,
                            status = %s
                        WHERE id = %s
                    """,
                    (
                        row["student_id"],
                        row["idcard"],
                        row["prefix"],
                        row["firstname"],
                        row["lastname"],
                        row["grade"],
                        row["group_id"],
                        row["status"],
                        row["id"]
                    )
                )
        st.success("บันทึกข้อมูลเรียบร้อยแล้ว!")
        time.sleep(1.5)
        st.rerun()