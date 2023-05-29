from django.db import models

class Todo(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=100, blank=True)
    date=models.DateTimeField(auto_now_add=True)
    done=models.BooleanField(default=False)
    def __str__(self):
        return self.title
        