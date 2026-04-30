from django.db import models
from django.utils.text import slugify
import uuid


class Student(models.Model):
    name = models.CharField(max_length=50)
    surename = models.CharField(max_length=50)
    age = models.PositiveIntegerField(default=18)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    picture = models.ImageField(upload_to='images/', default='images/default.jpg', blank=True)
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.surename}-{str(uuid.uuid4())[:4]}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} {self.surename}"