from .models import *
from rest_framework import serializers


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['last_name', 'first_name']


class FacultySerializers(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ['name', 'description']


class ProfessorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ['user', 'department', 'title']


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['user', 'department', 'enrollment_date', 'graduation_date']


class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['name', 'code', 'description', 'department', 'professor']


class ClassRoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ['room_number', 'building', 'capacity']


class ScheduleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['course', 'classroom', 'start_time', 'end_time', 'day_of_week']


class CourseEnrolledSerializers(serializers.ModelSerializer):
    class Meta:
        model = CourseEnrolled
        fields = ['student', 'course', 'date_enrolled', 'grade']


class HomeWorkSerializers(serializers.ModelSerializer):
    class Meta:
        model = HomeWork
        fields = ['course', 'title', 'description', 'due_date']


class HomeWorkSubmissionSerializers(serializers.ModelSerializer):
    class Meta:
        model = HomeWorkSubmission
        fields = ['homework', 'student', 'submission_date', 'grade', 'feedback']


