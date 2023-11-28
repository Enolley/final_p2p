from django.db import models


# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    document = models.FileField(upload_to="uploads/task_docs")
    course = models.CharField(max_length=100, default="Any")
    budget = models.PositiveIntegerField(default=0)
    deadline = models.DateTimeField()
    status = models.CharField(max_length=100)
    uploaded_by = models.IntegerField(default=1)
    bid_by = models.IntegerField(default=1)
    approval = models.CharField(max_length=100, default="Pending")
    submission = models.FileField(upload_to="uploads/submissions", default="Pending")
    payment = models.CharField(max_length=100, default="Pending")

    def __str__(self):
        return self.title
