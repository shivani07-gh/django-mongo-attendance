from mongoengine import Document, StringField, IntField, DateField, BooleanField, ReferenceField

class Student(Document):
    name = StringField(required=True)
    roll_number = IntField(required=True, unique=True)

    def __str__(self):
        return self.name


class Attendance(Document):
    student = ReferenceField(Student)
    date = DateField(required=True)
    is_present = BooleanField(default=False)

    def __str__(self):
        return f"{self.student.name} - {self.date}"


from mongoengine import Document, StringField

class AppUser(Document):
    username = StringField(required=True, unique=True)
    password = StringField(required=True)

    def __str__(self):
        return self.username
