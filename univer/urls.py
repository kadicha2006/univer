from django.urls import path
from .views import *
urlpatterns = [

    path('', UserProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='user_list'),
    path('users/<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='user_detail'),


    path('faculty/', FacultyViewSet.as_view({'get': 'list', 'post': 'create'}), name='faculty_list'),
    path('faculty/<int:pk>/', FacultyViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='faculty_detail'),


    path('professor/', ProfessorViewSet.as_view({'get': 'list', 'post': 'create'}), name='professor_list'),
    path('professor/<int:pk>/', ProfessorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='professor_detail'),


    path('students/', StudentViewSet.as_view({'get': 'list', 'post': 'create'}), name='student_list'),
    path('students/<int:pk>/', StudentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='student_detail'),


    path('courses/', CourseViewSet.as_view({'get': 'list', 'post': 'create'}), name='course_list'),
    path('courses/<int:pk>/', CourseViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='course_detail'),


    path('classrooms/', ClassRoomViewSet.as_view({'get': 'list', 'post': 'create'}), name='classroom_list'),
    path('classrooms/<int:pk>/', ClassRoomViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='classroom_detail'),


    path('schedule/', ScheduleViewSet.as_view({'get': 'list', 'post': 'create'}), name='schedule_list'),
    path('schedule/<int:pk>/', ScheduleViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='schedule_detail'),


    path('course_enrolled/', CourseEnrolledViewSet.as_view({'get': 'list', 'post': 'create'}), name='course_enrolled_list'),
    path('course_enrolled/<int:pk>/', CourseEnrolledViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='course_enrolled_detail'),


    path('homework/', HomeWorkViewSet.as_view({'get': 'list', 'post': 'create'}), name='homework_list'),
    path('homework/<int:pk>/', HomeWorkViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='homework_detail'),


    path('homework_submission/', HomeWorkSubmissionViewSet.as_view({'get': 'list', 'post': 'create'}), name='homework_submission_list'),
    path('homework_submission/<int:pk>/', HomeWorkSubmissionViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='homework_submission_detail'),
]
