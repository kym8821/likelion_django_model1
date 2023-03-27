from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    problem_number = models.IntegerField(default=1000)
    problem_text = models.TextField()
    
    def __str__(self):
        return self.title