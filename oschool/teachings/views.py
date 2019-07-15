from django.views.generic import (
    CreateView,
    DetailView,
    DeleteView,
    ListView,
)
from django.urls import reverse_lazy
from .models import Subject, Lesson
from .forms import LessonCreationForm


class SubjectCreateView(CreateView):
    model = Subject
    fields = ['name']


class SubjectDeleteView(DeleteView):
    model = Subject
    context_object_name = 'subject'
    slug_field = 'slug'
    slug_url_kwarg = 'subject_slug'

    def get_success_url(self):
        return reverse_lazy('teachings:subject-list')


class SubjectDetailView(DetailView):
    model = Subject
    context_object_name = 'subject'
    slug_field = 'slug'
    slug_url_kwarg = 'subject_slug'


class SubjectListView(ListView):
    model = Subject
    context_object_name = 'subjects'
    queryset = Subject.objects.all().values('name', 'slug')


class LessonCreateView(CreateView):
    model = Lesson
    form_class = LessonCreationForm
    template_name = 'teachings/lessons/lesson_form.html'


class LessonListView(ListView):
    model = Lesson
    context_object_name = 'lessons'
    queryset = Lesson.objects.all()
    template_name = 'teachings/lessons/lesson_list.html'


class LessonDetailView(DetailView):
    model = Lesson
    context_object_name = 'lesson'
    slug_field = 'slug'
    slug_url_kwarg = 'lesson_slug'
    template_name = 'teachings/lessons/lesson_detail.html'


class LessonDeleteView(DeleteView):
    model = Lesson
    context_object_name = 'lesson'
    slug_field = 'slug'
    slug_url_kwarg = 'lesson_slug'
    template_name = 'teachings/lessons/lesson_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('teachings:lesson-list')
