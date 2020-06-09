from django.db import models

# Create your models here.
class  Task(models.Model):
    date=models.DateTimeField()
    url=models.URLField()

    def __str__(self):
        return str(self.url)

