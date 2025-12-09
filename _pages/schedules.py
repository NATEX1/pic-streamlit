import streamlit as st
import db
import pandas as pd
import time
import streamlit.components.v1 as components

st.title("ตาราง")
st.divider()

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    group = st.selectbox("เลือกระดับชั้น", ["ปวช.1", "ปวช.2", "ปวช.3"])
    
html = f"""

<style>
    @page {{
        size: A4 landscape;
        margin: 10mm;
    }}

    @media print {{
        body * {{
            visibility: hidden;
        }}
        #export-area, #export-area * {{
            visibility: visible;
        }}
        #export-area {{
            position: absolute;
            left: 0;
            top: 0;
            width: 100%;
        }}
    }}
    table, td, th {{
        border: 1px solid black;
        padding: 6px;
        font-size: 11px;
    }}
    
    
    
    button {{
        padding: 10px 20px;
        font-size: 18px;
        border-radius: 8px;
        border: none;
        background-color: #8B0000;
        color: white;
        cursor: pointer;
        display: block;
        margin-bottom: 20px;
    }}
</style>
<button onclick="window.print()">Export ตารางเรียน</button>
<div id="export-area" style="aspect-ratio: 297 / 210;">
    <table style="border-collapse: collapse; width: 100%;  background: #fff; color: #000;">
        <thead >
            <tr>
                <td colspan="13" style="text-align: center; font-size: 22px; padding: 10px 0;">
                    ตารางการเรียน {group}
                </td>
            </tr>
            <tr>
                <td rowspan="8" colspan="3" style="text-align:center;">
                    <img src="https://www.pic.ac.th/wp-content/uploads/2023/02/cropped-piclogo.png"
                         height="80">
                    <p>ตารางเรียน</p>
                </td>
            </tr>
            <tr><td colspan="5">ภาษาไทย</td><td colspan="5">ภาษาไทย</td></tr>
            <tr><td colspan="5">ภาษาไทย</td><td colspan="5">ภาษาไทย</td></tr>
            <tr><td colspan="5">ภาษาไทย</td><td colspan="5">ภาษาไทย</td></tr>
            <tr><td colspan="5">ภาษาไทย</td><td colspan="5">ภาษาไทย</td></tr>
            <tr><td colspan="5">ภาษาไทย</td><td colspan="5">ภาษาไทย</td></tr>
            <tr><td colspan="5">ภาษาไทย</td><td colspan="5">ภาษาไทย</td></tr>
            <tr><td colspan="5">ภาษาไทย</td><td colspan="5">ภาษาไทย</td></tr>
        </thead>

        <tbody style="text-align: center;">
            <tr>
                <td rowspan="2">วัน-เวลา</td>
                {''.join([f"<td>{i}</td>" for i in range(1, 13)])}
            </tr>
            <tr>
                {''.join([f"<td>{t}</td>" for t in [
                    "8:00-9:00","9:00-10:00","10:00-11:00","11:00-12:00","12:00-13:00",
                    "13:00-14:00","14:00-15:00","15:00-16:00","16:00-17:00","17:00-18:00",
                    "18:00-19:00","19:00-20:00"
                ]])}
            </tr>

            <!-- จันทร์ -->
            <tr>
                <td>จันทร์</td>
                <td><div class="subj">ภาษาไทย</div><div class="teacher">ครู: วรเทพ</div><div class="room">ห้อง 101</div></td>
                <td><div class="subj">ภาษาไทย</div><div class="teacher">ครู: วรเทพ</div><div class="room">ห้อง 101</div></td>
                <td><div class="subj">ภาษาไทย</div><div class="teacher">ครู: วรเทพ</div><div class="room">ห้อง 101</div></td>
                <td><div class="subj">คณิต</div><div class="teacher">ครู: นภัส</div><div class="room">ห้อง 204</div></td>
                <td><div class="subj">พัก</div></td>
                <td><div class="subj">คณิต</div><div class="teacher">ครู: นภัส</div><div class="room">ห้อง 204</div></td>
                <td><div class="subj">อังกฤษ</div><div class="teacher">ครู: มลิวัลย์</div><div class="room">ห้อง 305</div></td>
                <td><div class="subj">อังกฤษ</div><div class="teacher">ครู: มลิวัลย์</div><div class="room">ห้อง 305</div></td>
                <td><div class="subj">ว่าง</div></td>
                <td><div class="subj">ว่าง</div></td>
                <td><div class="subj">ว่าง</div></td>
                <td><div class="subj">ว่าง</div></td>
            </tr>

            <!-- อังคาร -->
            <tr>
                <td>อังคาร</td>
                <td><div class="subj">ฟิสิกส์</div><div class="teacher">ครู: ธนากร</div><div class="room">ห้อง 207</div></td>
                <td><div class="subj">ฟิสิกส์</div><div class="teacher">ครู: ธนากร</div><div class="room">ห้อง 207</div></td>
                <td><div class="subj">ฟิสิกส์</div><div class="teacher">ครู: ธนากร</div><div class="room">ห้อง 207</div></td>
                <td><div class="subj">โปรแกรม</div><div class="teacher">ครู: พิชญะ</div><div class="room">ห้อง คอม 1</div></td>
                <td><div class="subj">พัก</div></td>
                <td><div class="subj">โปรแกรม</div><div class="teacher">ครู: พิชญะ</div><div class="room">ห้อง คอม 1</div></td>
                <td><div class="subj">โปรแกรม</div><div class="teacher">ครู: พิชญะ</div><div class="room">ห้อง คอม 1</div></td>
                <td><div class="subj">อังกฤษ</div><div class="teacher">ครู: มลิวัลย์</div><div class="room">ห้อง 305</div></td>
                <td><div class="subj">อังกฤษ</div><div class="teacher">ครู: มลิวัลย์</div><div class="room">ห้อง 305</div></td>
                <td><div class="subj">ว่าง</div></td>
                <td><div class="subj">ว่าง</div></td>
                <td><div class="subj">ว่าง</div></td>
            </tr>

            <!-- พุธ -->
            <tr>
                <td>พุธ</td>
                <td><div class="subj">คอมพื้นฐาน</div><div class="teacher">ครู: ชัยวัฒน์</div><div class="room">ห้อง คอม 2</div></td>
                <td><div class="subj">คอมพื้นฐาน</div><div class="teacher">ครู: ชัยวัฒน์</div><div class="room">ห้อง คอม 2</div></td>
                <td><div class="subj">คอมพื้นฐาน</div><div class="teacher">ครู: ชัยวัฒน์</div><div class="room">ห้อง คอม 2</div></td>
                <td><div class="subj">กิจกรรม</div></td>
                <td><div class="subj">พัก</div></td>
                <td><div class="subj">กิจกรรม</div></td>
                <td><div class="subj">คณิต</div><div class="teacher">ครู: นภัส</div><div class="room">ห้อง 204</div></td>
                <td><div class="subj">คณิต</div><div class="teacher">ครู: นภัส</div><div class="room">ห้อง 204</div></td>
                <td><div class="subj">ว่าง</div></td>
                <td><div class="subj">ว่าง</div></td>
                <td><div class="subj">ว่าง</div></td>
                <td><div class="subj">ว่าง</div></td>
            </tr>

            <!-- พฤหัส -->
            <tr>
                <td>พฤหัสฯ</td>
                <td><div class="subj">ไทย</div><div class="teacher">ครู: วรเทพ</div><div class="room">ห้อง 101</div></td>
                <td><div class="subj">ไทย</div><div class="teacher">ครู: วรเทพ</div><div class="room">ห้อง 101</div></td>
                <td><div class="subj">ไทย</div><div class="teacher">ครู: วรเทพ</div><div class="room">ห้อง 101</div></td>
                <td><div class="subj">อังกฤษ</div><div class="teacher">ครู: มลิวัลย์</div><div class="room">ห้อง 305</div></td>
                <td><div class="subj">พัก</div></td>
                <td><div class="subj">อังกฤษ</div><div class="teacher">ครู: มลิวัลย์</div><div class="room">ห้อง 305</div></td>
                <td><div class="subj">วิทย์</div><div class="teacher">ครู: ธนากร</div><div class="room">ห้อง 207</div></td>
                <td><div class="subj">วิทย์</div><div class="teacher">ครู: ธนากร</div><div class="room">ห้อง 207</div></td>
                <td><div class="subj">ว่าง</div></td>
                <td><div class="subj">ว่าง</div></td>
                <td><div class="subj">ว่าง</div></td>
                <td><div class="subj">ว่าง</div></td>
            </tr>

            <!-- ศุกร์ -->
            <tr>
                <td>ศุกร์</td>
                <td><div class="subj">กีฬา</div><div class="teacher">ครู: มงคล</div><div class="room">สนาม</div></td>
                <td><div class="subj">กีฬา</div><div class="teacher">ครู: มงคล</div><div class="room">สนาม</div></td>
                <td><div class="subj">กีฬา</div><div class="teacher">ครู: มงคล</div><div class="room">สนาม</div></td>
                <td><div class="subj">กิจกรรม</div></td>
                <td><div class="subj">พัก</div></td>
                <td><div class="subj">กิจกรรม</div></td>
                <td><div class="subj">อังกฤษ</div><div class="teacher">ครู: มลิวัลย์</div><div class="room">ห้อง 305</div></td>
                <td><div class="subj">อังกฤษ</div><div class="teacher">ครู: มลิวัลย์</div><div class="room">ห้อง 305</div></td>
                <td><div class="subj">ว่าง</div></td>
                <td><div class="subj">ว่าง</div></td>
                <td><div class="subj">ว่าง</div></td>
                <td><div class="subj">ว่าง</div></td>
            </tr>

        </tbody>
    </table>
</div>


"""

components.html(html, height=748)