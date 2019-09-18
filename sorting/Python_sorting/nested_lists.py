student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10),
]

student_tuples.sort(key=lambda student: student[2])  # Sort by age
print(student_tuples)