import streamlit as st
import mysql.connector
import pandas as pd

# Database connection
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",          
        password="welcome@123",
        database="collage"
    )

conn = get_connection()
cursor = conn.cursor(buffered=True)

# Create Table 
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    std_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    course VARCHAR(50),
    cgpa FLOAT NOT NULL
)
""")
conn.commit()

st.title("Student Database Management System")

menu = st.sidebar.selectbox(
    "Menu",
    ["Insert Record", "View Records", "Update Record", "Delete Record"]
)

# Insert Record
if menu == "Insert Record":
    st.subheader("Insert Student Record")

    with st.form("insert_form"):
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=1, step=1)
        course = st.text_input("Course")
        cgpa = st.number_input("CGPA", min_value=0.0, max_value=10.0, step=0.01)

        submitted = st.form_submit_button("Insert")

        if submitted:
            sql = "INSERT INTO students (name, age, course, cgpa) VALUES (%s,%s,%s,%s)"
            cursor.execute(sql, (name, age, course, cgpa))
            conn.commit()
            st.success("Record inserted successfully")

# View Records 
elif menu == "View Records":
    st.subheader("Student Records")

    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()

    df = pd.DataFrame(records, columns=["ID", "Name", "Age", "Course", "CGPA"])
    st.dataframe(df)

    # Download Excel
    excel_file = "student_information.xlsx"
    df.to_excel(excel_file, index=False)

    with open(excel_file, "rb") as f:
        st.download_button(
            label="⬇ Download Excel",
            data=f,
            file_name="student_information.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

# Update Record 
elif menu == "Update Record":
    st.subheader("✏ Update Student Record")

    std_id = st.number_input("Student ID", min_value=1, step=1)
    name = st.text_input("Updated Name")
    age = st.number_input("Updated Age", min_value=1, step=1)
    course = st.text_input("Updated Course")
    cgpa = st.number_input("Updated CGPA", min_value=0.0, max_value=10.0, step=0.01)

    if st.button("Update"):
        sql = """
        UPDATE students 
        SET name=%s, age=%s, course=%s, cgpa=%s 
        WHERE std_id=%s
        """
        cursor.execute(sql, (name, age, course, cgpa, std_id))
        conn.commit()
        st.success("Record updated successfully")

# Delete Record 
elif menu == "Delete Record":
    st.subheader("🗑 Delete Student Record")

    std_id = st.number_input("Student ID to delete", min_value=1, step=1)

    if st.button("Delete"):
        cursor.execute("DELETE FROM students WHERE std_id=%s", (std_id,))
        conn.commit()
        st.warning("Record deleted successfully")
