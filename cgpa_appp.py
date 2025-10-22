import streamlit as st

st.set_page_config(page_title="COMSATS CGPA Calculator", page_icon="🎓", layout="centered")
st.title("🎓 COMSATS CGPA Calculator")
st.write("Calculate your current semester GPA and cumulative CGPA including all previous semesters.")

# --- Grading function (COMSATS scale) ---
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

# --- Input number of courses ---
st.header("Enter Current Semester Courses")
num_courses = st.number_input("Number of courses this semester:", min_value=1, max_value=10, value=6)

total_points = 0
total_credits = 0
courses = []

for i in range(int(num_courses)):
    st.subheader(f"Course {i+1}")
    course_name = st.text_input(f"Course name #{i+1} (optional):", key=f"name_{i}")
    marks = st.number_input(f"Marks (%) for course #{i+1}:", 0.0, 100.0, key=f"marks_{i}")
    credits = st.number_input(f"Credit hours for course #{i+1}:", 0.5, 6.0, value=3.0, key=f"credit_{i}")
    gp = get_grade_point(marks)
    total_points += gp * credits
    total_credits += credits
    courses.append({"name": course_name, "marks": marks, "credits": credits, "gp": gp})

# --- Input previous semesters ---
st.header("Previous Semesters")
num_prev = st.number_input("Number of previous semesters:", min_value=0, max_value=10, value=0)

prev_total_points = 0
prev_total_credits = 0
for i in range(int(num_prev)):
    st.subheader(f"Previous Semester {i+1}")
    prev_gpa = st.number_input(f"Semester GPA #{i+1}:", 0.0, 4.0, step=0.01, key=f"prev_gpa_{i}")
    prev_credits = st.number_input(f"Total credits in semester #{i+1}:", 0.0, 50.0, step=0.5, key=f"prev_credit_{i}")
    prev_total_points += prev_gpa * prev_credits
    prev_total_credits += prev_credits

# --- Calculate current semester GPA ---
semester_gpa = total_points / total_credits if total_credits > 0 else 0

# --- Calculate cumulative CGPA ---
cumulative_points = prev_total_points + total_points
cumulative_credits = prev_total_credits + total_credits
cumulative_cgpa = cumulative_points / cumulative_credits if cumulative_credits > 0 else 0

# --- Display results ---
st.write("---")
st.subheader("Results")
st.success(f"Current Semester GPA: **{semester_gpa:.3f}**")
st.success(f"Cumulative CGPA (including all previous semesters): **{cumulative_cgpa:.3f}**")

# --- Breakdown ---
st.write("---")
st.subheader("Current Semester Breakdown")
for i, c in enumerate(courses, start=1):
    course_name = c['name'] if c['name'] else f"Course {i}"
    st.write(f"- **{course_name}** — Marks: {c['marks']}% — GP: {c['gp']} × Credit: {c['credits']} = {c['gp']*c['credits']:.2f}")
