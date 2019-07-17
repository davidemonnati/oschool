from django.urls import path
from .views import (
    aggiungiClasse,
    ViewClassList,
    ViewClassDetail,
)


app_name = 'school_classes'
urlpatterns = [
    path("classes/", view=ViewClassList.as_view(), name='classes-list'),
    path("classes/create", view=aggiungiClasse.as_view(), name='class-create'),
    path("classes/detail/<slug:class_slug>/", view=ViewClassDetail.as_view(), name='class-detail'),
]