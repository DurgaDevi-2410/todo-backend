from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=20)

    class Meta:
        unique_together = ('user', 'name')

    def __str__(self):
        return self.name

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)
    dueDate = models.DateField(null=True, blank=True)
    dueTime = models.TimeField(null=True, blank=True)
    recurrence = models.CharField(max_length=50, default='None')
    reminder = models.IntegerField(default=0) # in minutes
    priority = models.CharField(max_length=20, default='Medium')
    category = models.CharField(max_length=100, default='Personal') # Store name to avoid complex FK issues for now given the simple frontend structure
    # Alternatively, could be FK to Category. But if we delete a category, we might want to keep the tasks or move them.
    # Frontend logic: "Reassign orphan tasks to 'Personal'".
    # Let's simple store the name for now as the frontend relies heavily on strings.

    def __str__(self):
        return self.text
