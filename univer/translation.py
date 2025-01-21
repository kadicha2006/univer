from .models import Faculty, Professor, Student, Course, ClassRoom, Schedule, CourseEnrolled, HomeWork, \
    HomeWorkSubmission
from modeltranslation.translator import TranslationOptions, register


@register(Faculty)
class FacultyTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Professor)
class ProfessorTranslationOptions(TranslationOptions):
    fields = ('user', 'department', 'title', 'bio')


@register(Student)
class StudentTranslationOptions(TranslationOptions):
    fields = ('user', 'department', )


@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields = ('name', 'department', 'description', 'professor',)


@register(ClassRoom)
class ClassRoomTranslationOptions(TranslationOptions):
    fields = ('room_number', 'building',)


@register(Schedule)
class ScheduleTranslationOptions(TranslationOptions):
    fields = ('day_of_week',)


@register(CourseEnrolled)
class CourseEnrolledTranslationOptions(TranslationOptions):
    fields = ('grade',)


@register(HomeWork)
class HomeWorkTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


@register(HomeWorkSubmission)
class HomeWorkSubmissionTranslationOptions(TranslationOptions):
    fields = ('feedback',)

