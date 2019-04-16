from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Port(models.Model):
    name = models.CharField(max_length=200, blank=True)
    port = models.IntegerField(validators=[MaxValueValidator(65536), MinValueValidator(1)])
    protocol    = models.CharField(max_length=3)
    description = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.port