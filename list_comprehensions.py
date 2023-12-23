
students = ["Aaa", "Bbb", "Ccc", "Ddd"]

students_no = ["Aaa", "Ccc"]

[student.upper() if student in students_no else student.lower() for student in students]

