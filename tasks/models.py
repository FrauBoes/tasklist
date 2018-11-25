from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    owner = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    due_date = models.DateField('due date')

    def __str__(self):
        return self.title


class Member(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
