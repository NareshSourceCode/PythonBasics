import student as s

def test_get_grade(name,age, grade):
    student1 = s.student(name, age, grade)
    print(student1.get_grade())
    if(student1.get_grade() >= 85):
        print("Test passed")
    elif(student1.get_grade() < 85):
        print("Test failed")


test_get_grade("Naresh",20,77)
test_get_grade("NareshGoud",20,85)