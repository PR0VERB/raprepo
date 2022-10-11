from django.db import models
from django.contrib.auth.models import User
User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')

Abraham = 0

class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    number_of_pages = models.PositiveIntegerField(default=1)
    # updated_time

    def __str__(self):
        return self.title
