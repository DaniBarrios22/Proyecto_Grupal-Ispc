from django.db import models

# Create your models here.

class Course(models.Model):
    id_course = models.AutoField(primary_key=True)
    name = models.CharField (max_length=45)
    languaje = models.CharField (max_length=45)
    tag_1 = models.CharField (max_length=45)
    tag_2 = models.CharField (max_length=45)
    link = models.CharField (max_length=45)

    def __str__(self):
        return "{} {} {}".format(self.id_course, self.name, self.languaje)
    



