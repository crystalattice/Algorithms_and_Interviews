from operator import itemgetter, attrgetter, methodcaller

student_tuples = [
        ('henry', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10),
]

class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))

    def weighted_grade(self):
        return 'CBA'.index(self.grade) / float(self.age)

student_objects = [
        Student('henry', 'A', 15),
        Student('jane', 'B', 12),
        Student('dave', 'B', 10),
]

if __name__ == "__main__":
    print(f"Sort by index\n{sorted(student_tuples, key=itemgetter(0))}\n")
    print(f"Sort by name\n{sorted(student_objects, key=attrgetter('age'))}\n")
    print(f"Sort by grade, then age (index)\n{sorted(student_tuples, key=itemgetter(1, 2))}\n")
    print(f"Sort by grade, then age (name)\n{sorted(student_objects, key=attrgetter('grade', 'age'))}\n")
    print(f"Calculate weighted grades\n{[(student.name, student.weighted_grade()) for student in student_objects]}\n")
    print(f"Sort by method, highest first\n{sorted(student_objects, key=methodcaller('weighted_grade'), reverse=True)}\n")