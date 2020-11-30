class course:
    TOTAL_COURSES = 0

    def __init__(self, name, room, max_students):
        self.name = name
        self.room = room
        self.max_students = max_students
        self.student_list = []
        course.TOTAL_COURSES += 1
    
    def addStudent(self, student):
        # Checks if the class is below max capacity
        if len(self.student_list) < self.max_students:
            self.student_list.append(student)
            # Adds the course to the student's course list
            student.course_list.append(self)
            return True
        return False


class student:
    TOTAL_STUDENTS = 0

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.course_list = []
        student.TOTAL_STUDENTS += 1


s1 = student("Tom", 14, "Male")
s2 = student("Rom", 14, "Male")
s3 = student("Crom", 14, "Female")

c = course("Physics", "P123", 2)
c.addStudent(s1)
c.addStudent(s2)
c.addStudent(s3)