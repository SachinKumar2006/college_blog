
# Create your models here.

from django.db import models
from django.utils.text import slugify


class Department(models.Model):
    dept_name = models.CharField(max_length=100)
    dept_code = models.CharField(max_length=10)

    def __str__(self):
        return self.dept_name


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    roll_number = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    slug = models.SlugField(blank=True)

    class Meta:
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1

            while Student.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name