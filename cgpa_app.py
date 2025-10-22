import streamlit as st

# --- Title and description ---
st.title("🎓 COMSATS CGPA Calculator")
st.write("Enter your course marks and credit hours to calculate your CGPA according to COMSATS criteria.")

# --- Define grade point calculation function ---
def get_grade_point(marks):
    if marks >= 85:
        return 4.00
    elif marks >= 80:
        return 3.67
    elif marks >= 75:
        return 3.33
    elif marks >= 70:
        return 3.00
    elif marks >= 65:
        return 2.67
    elif marks >= 60:
        return 2.33
    elif marks >= 55:
        return 2.00
    elif marks >= 50:
        return 1.67
    else:
        return 0.00

# --- Number of courses ---
num_courses = st.number_input("Enter number of courses:", min_value=1, max_value=10, value=6)

total_points = 0
total_credits = 0

# --- Input for each course ---
for i in range(int(num_courses)):
    st.subheader(f"Course {i+1}")
    marks = st.number_input(f"Marks for course {i+1}:", 0.0, 100.0, key=f"marks_{i}")
    credits = st.number_input(f"Credit hours for course {i+1}:", 1.0, 4.0, key=f"credit_{i}")
    grade_point = get_grade_point(marks)
    total_points += grade_point * credits
    total_credits += credits

# --- Calculate and display CGPA ---
if total_credits > 0:
    cgpa = total_points / total_credits
    st.success(f"🎯 Your CGPA is: **{cgpa:.2f}**")
