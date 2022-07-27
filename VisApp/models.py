from django.db import models

# Create your models here.
class Participants(models.Model):
    Sample_nr = models.CharField(verbosed_name='Sample nr', max_length=32)
    Treadmill = models.CharField(verbosed_name='Treadmill')
    Freeliving = models.CharField(verbosed_name='Free living')
    Gender = models.CharField(verbosed_name='Gender')
    Age = models.CharField(verbosed_name='Age')
    Data_avaliability = models.CharField(verbosed_name='Data avaliability')