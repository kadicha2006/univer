from rest_framework import generics, viewsets, permissions
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers
    permission_classes = [permissions.IsAuthenticated]


class FacultyViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializers
    filter_backends = [DjangoFilterBackend, SearchFilter,]
    filterset_fields = ['name']
    search_fields = ['name']


class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter,]
    filterset_fields = ['user', 'department', 'title', 'bio']
    search_fields = ['user']
    permission_classes = [permissions.IsAuthenticated]


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    permission_classes = [permissions.IsAuthenticated]


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter,]
    filterset_fields = ['name', 'description', 'department', 'professor']
    search_fields = ['name']
    permission_classes = [permissions.IsAuthenticated]


class ClassRoomViewSet(viewsets.ModelViewSet):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomSerializers
    permission_classes = [permissions.IsAuthenticated]


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializers
    permission_classes = [permissions.IsAuthenticated]


class CourseEnrolledViewSet(viewsets.ModelViewSet):
    queryset = CourseEnrolled.objects.all()
    serializer_class = CourseEnrolledSerializers
    permission_classes = [permissions.IsAuthenticated]


class HomeWorkViewSet(viewsets.ModelViewSet):
    queryset = HomeWork.objects.all()
    serializer_class = HomeWorkSerializers
    permission_classes = [permissions.IsAuthenticated]


class HomeWorkSubmissionViewSet(viewsets.ModelViewSet):
    queryset = HomeWorkSubmission.objects.all()
    serializer_class = HomeWorkSubmissionSerializers
    permission_classes = [permissions.IsAuthenticated]


