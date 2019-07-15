from django.db import models
from django.utils.text import slugify
from django.urls import reverse_lazy


class Subject(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(db_index=True, unique=True, max_length=50)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Subject, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('teachings:subject-detail', kwargs={'subject_slug': self.slug})
