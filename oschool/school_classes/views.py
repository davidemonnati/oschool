from django.views.generic import (
    CreateView,
    DetailView,
    DeleteView,
    ListView,
)
from .models import SchoolClass


class aggiungiClasse(CreateView):
    model = SchoolClass
    fields = ['section']
    template_name = "school_classes/class_form.html"


class ViewClassList(ListView):
    model = SchoolClass
    context_object_name = 'classes'
    queryset = SchoolClass.objects.all().values('section', 'course_year')
    template_name = "school_classes/class_list.html"


class ViewClassDetail(DetailView):
    model = SchoolClass
    context_object_name = 'class'
    slug_field = 'slug'
    slug_url_kwarg = 'class_slug'
    template_name = "school_classes/class_detail.html"

