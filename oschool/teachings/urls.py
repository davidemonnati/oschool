from django.urls import path
from .views import (
    SubjectCreateView,
    SubjectDetailView,
    SubjectDeleteView,
    SubjectListView,
    LessonListView,
    LessonCreateView,
    LessonDetailView,
    LessonDeleteView,
)

app_name = 'teachings'
urlpatterns = [
    path("subjects/", view=SubjectListView.as_view(), name='subject-list'),
    path("subjects/create/", view=SubjectCreateView.as_view(), name='subject-create'),
    path("subjects/detail/<slug:subject_slug>/", view=SubjectDetailView.as_view(), name='subject-detail'),
    path("subjects/delete/<slug:subject_slug>/", view=SubjectDeleteView.as_view(), name='subject-delete'),
    path("lessons/", view=LessonListView.as_view(), name='lesson-list'),
    path("lessons/create/", view=LessonCreateView.as_view(), name='lesson-create'),
    path("lessons/detail/<slug:lesson_slug>/", view=LessonDetailView.as_view(), name='lesson-detail'),
    path("lessons/delete/<slug:lesson_slug>/", view=LessonDeleteView.as_view(), name='lesson-delete'),
]
