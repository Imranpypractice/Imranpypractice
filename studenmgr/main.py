from student import Student
import grade

student1 = Student("Alice", 101)
student1.add_grade(5)
student1.add_grade(30)
student1.add_grade(5)

student2 = Student("Jack", 101)
student2.add_grade(80)
student2.add_grade(30)
student2.add_grade(100)


avg = student1.get_average()
print(f"Student: {student1.name}, Roll No: {student1.roll_no}")
print(f"Average Score: {avg}")
print(f"Passed: {grade.is_pass(avg)}")
print(f"Grade Letter: {grade.grade_letter(avg)}")
avg = student2.get_average()
print(f"Student: {student2.name}, Roll No: {student2.roll_no}")
print(f"Average Score: {avg}")
print(f"Passed: {grade.is_pass(avg)}")
print(f"Grade Letter: {grade.grade_letter(avg)}")