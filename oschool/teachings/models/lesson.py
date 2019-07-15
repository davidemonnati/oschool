from django.db import models
from django.utils.text import slugify
from django.urls import reverse_lazy
from .subject import Subject


class Lesson(models.Model):
    date = models.DateField(auto_now_add=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(db_index=True, unique=True, max_length=200)
    description = models.TextField(null=True, blank=True)
    subject = models.ForeignKey(
        Subject,
        on_delete=models.PROTECT,
        related_name='lessons',
        related_query_name='lesson',
    )

    class Meta:
        verbose_name = "lesson"
        verbose_name_plural = "lessons"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        time_overlapping_start = Lesson.objects.filter(start_time__gte=self.start_time, start_time__lte=self.end_time).count()

        time_overlapping_end = Lesson.objects.filter(end_time__gte=self.start_time, end_time__lte=self.end_time).count()

        if (time_overlapping_start > 0 or time_overlapping_end > 0):
            return
        else:
            super(Lesson, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('teachings:lesson-detail', kwargs={'lesson_slug': self.slug})

