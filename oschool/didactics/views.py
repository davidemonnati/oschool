from django.views.generic import (
    CreateView,
    DetailView,
    DeleteView,
    ListView,
)
from django.urls import reverse_lazy
from .models import Subject


class SubjectCreateView(CreateView):
    model = Subject
    fields = ['name']


class SubjectDeleteView(DeleteView):
    model = Subject
    context_object_name = 'subject'
    slug_field = 'slug'
    slug_url_kwarg = 'subject_slug'

    def get_success_url(self):
        return reverse_lazy('didactics:subject-list')


class SubjectDetailView(DetailView):
    model = Subject
    context_object_name = 'subject'
    slug_field = 'slug'
    slug_url_kwarg = 'subject_slug'


class SubjectListView(ListView):
    model = Subject
    context_object_name = 'subjects'
    queryset = Subject.objects.all().values('name', 'slug')