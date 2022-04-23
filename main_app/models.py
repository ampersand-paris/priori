from django.db import models
from django.contrib.auth.models import User

# Create your models here.


DAY_CHOICES = (
    ("Mon", "Monday"),
    ("Tue", "Tuesday"),
    ("Wed", "Wednesday"),
    ("Thurs", "Thursday"),
    ("Fri", "Friday"),
    ("Sat", "Saturday"),
    ("Sun", "Sunday")
)
class Task(models.Model):

    task = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    days = models.CharField(max_length=10, choices=DAY_CHOICES)
    is_complete = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.task
    
    class Meta:
        ordering = []

class Day(models.Model):

    day = models.DateField()
    tasks = models.ManyToManyField(Task)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.day.strftime("%B %d, %Y")