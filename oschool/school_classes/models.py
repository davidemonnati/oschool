from django.db import models
from django.utils.text import slugify


class SchoolClass(models.Model):
    section = models.CharField(max_length=5)
    course_year = models.IntegerField()
    slug = models.SlugField(db_index=True, unique=True, max_length=5)

    class Meta:
        verbose_name = "lesson"
        verbose_name_plural = "lessons"

    def __str__(self):
        return self.section

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.coucourse_year + self.section)

        super(SchoolClass, self).save(*args, **kwargs)
