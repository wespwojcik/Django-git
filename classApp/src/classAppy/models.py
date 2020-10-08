from django.db import models

# Create your models here.






class DjangoClasses(models.Model):
    Title = models.CharField(max_length=60)
    CourseNum = models.IntegerField()
    InstructorName = models.CharField(max_length=60)
    Duration = models.FloatField()

    objects = models.Manager()


    def __str__(self):
        return self.Title


