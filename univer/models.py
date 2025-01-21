from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(AbstractUser):
    phone_number = PhoneNumberField(null=True, blank=True, region='KG')
    age = models.PositiveIntegerField(default=0, null=True, blank=True)
    profile_image = models.ImageField(upload_to='UserProfile_images/')
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name},{self.last_name}'


class Faculty(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Professor(models.Model):
    user = models.OneToOneField(UserProfile, related_name='professor', on_delete=models.CASCADE)
    department = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return f'{self.department} - {self.title}'


class Student(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    department = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    enrollment_date = models.DateField()
    graduation_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.department}'


class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=16)
    description = models.TextField()
    department = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ClassRoom(models.Model):
    room_number = models.CharField(max_length=10)
    building = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.room_number


class Schedule (models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    STATUS_CHOICES = (
        ('Понедельник', 'Понедельник'),
        ('Вторник', 'Вторник'),
        ('Среда', 'Среда'),
        ('Четверг', 'Четверг'),
        ('Пятница', 'Пятница'),
    )
    day_of_week = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f'{self.course}- {self.classroom}'


class CourseEnrolled(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateField()
    grade = models.CharField(max_length=16,null=True, blank=True)

    def __str__(self):
        return f"{self.student} - {self.course}"


class HomeWork(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.course.name}"


class HomeWorkSubmission(models.Model):
    homework = models.ForeignKey(HomeWork, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    submission_date = models.DateField()
    grade = models.CharField(max_length=2, null=True, blank=True)
    feedback = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.student}- {self.homework}'
