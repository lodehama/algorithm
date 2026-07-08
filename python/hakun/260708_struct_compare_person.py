class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age


def compare_persons(p1, p2):
  return p1.name == p2.name and p1.age == p2.age


person1 = Person("John", 25)
person2 = Person("John", 25)
person3 = Person("Alice", 30)

if compare_persons(person1, person2):
  print("사람1과 사람2는 같다.")
else:
  print("사람1과 사람2는 다르다.")

if compare_persons(person1, person3):
  print("사람1과 사람3은 같다.")
else:
  print("사람1과 사람3은 다르다.")
