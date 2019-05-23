from django.urls import path
from .views import (
    SubjectCreateView,
    SubjectDetailView,
    SubjectDeleteView,
    SubjectListView,
)

app_name = 'didactics'
urlpatterns = [
    path("subjects/", view=SubjectListView.as_view(), name='subject-list'),
    path("subjects/create/", view=SubjectCreateView.as_view(), name='subject-create'),
    path("subjects/detail/<slug:subject_slug>/", view=SubjectDetailView.as_view(), name='subject-detail'),
    path("subjects/delete/<slug:subject_slug>/", view=SubjectDeleteView.as_view(), name='subject-delete'),
]
