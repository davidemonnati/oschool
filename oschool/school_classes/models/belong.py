from django.db import models
from .schoolclass import SchoolClass
from django.conf import settings


class Belong(models.Model):
    school_class = models.ForeignKey(
        SchoolClass,
        related_name='SchoolClass',
    )
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
    )

    def __str__(self):
        return

    def save(self, *args, **kwargs):
        super(Belong, self).save(*args, **kwargs)
