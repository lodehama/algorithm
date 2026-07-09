class Student:
  def __init__(self, number, name, grade):
    self.number = number
    self.name = name
    self.grade = grade


def equal(student1, student2):
  return student1.number == student2.number


a = Student(1, "lee", 3.8)
b = Student(2, "kim", 4.0)

if equal(a, b):
  print("같은 학생")
else:
  print("다른 학생")