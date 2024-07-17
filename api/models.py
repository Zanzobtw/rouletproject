from django.db import models

# Create your models here.
class check_list(models.Model):
    task = models.CharField(max_lenfth=50)
    description = models.TextField()
    status = models.BooleanField(default = False)

    def __str__(self):
        return self.task
