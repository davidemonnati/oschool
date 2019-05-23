from django.db import models
from django.db.models import Q
from .subject import Subject


class Lesson(models.Model):
    date = models.DateField(auto_now_add=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    name = models.CharField(max_length=200)
    description = models.TextField()
    subject = models.OneToOneField(
        Subject,
        on_delete=models.PROTECT,
        related_name='subject_of'
    )

    class Meta:
        verbose_name = "lesson"
        verbose_name_plural = "lessons"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.__time_range_is_free:
            super(Lesson, self).save(*args, **kwargs)

    def __time_range_is_free(self):
        try:
            Lesson.objects.get(
                Q(start_time__range=(self.start_time == self.end_time))
                | Q(endDate__range=(self.start_time, self.end_time))
                | Q(startDate__lt=self.start_time, end_time__gt=self.end_time)
            )
        except Lesson.DoesNotExist:
            return True
        return False
