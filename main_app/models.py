from django.db import models

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

    task = models.CharField(max_lenth=50)
    description = models.CharField(max_length=250)
    days = models.CharField(max_length=10, choices=DAY_CHOICES)
    is_complete = models.BooleanField()

    def __str__(self):
        return self.task
    
    class Meta:
        ordering = []