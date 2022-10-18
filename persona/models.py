from django.db import models


class Persona(models.Model):
    nombre = models.CharField(max_length=120)
    edad = models.PositiveIntegerField()
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'persona'
        verbose_name_plural = 'personas'
        db_table = 'personas'